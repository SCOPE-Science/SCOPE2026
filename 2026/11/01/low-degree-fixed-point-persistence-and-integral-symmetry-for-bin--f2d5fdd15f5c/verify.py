"""Independent finite checks of geometric two-bit translation fixed complexes and their symmetries."""
from itertools import combinations, permutations

def d(x,y):
    return (x^y).bit_count()

def orbit_set(n):
    flip=3
    remaining=set(range(1<<n)); out=[]
    while remaining:
        x=min(remaining);orb=frozenset([x,x^flip]);remaining.difference_update(orb);out.append(orb)
    return out

def lab(orb):
    x=min(orb)
    return ((x&1)^((x>>1)&1),x>>2)

def graph(n,r):
    orbs=orbit_set(n)
    assert all(d(*tuple(o))<=r for o in orbs) == (r>=2)
    e=set()
    for i,j in combinations(range(len(orbs)),2):
        if max(d(x,y) for x in orbs[i] for y in orbs[j])<=r:e.add((i,j))
    return orbs,e

def h1_rank_f2(N,edges):
    neigh=[set() for _ in range(N)]
    for i,j in edges:neigh[i].add(j);neigh[j].add(i)
    order=sorted(edges);index={e:i for i,e in enumerate(order)}
    basis={};triangles=0
    for a in range(N):
        for b in neigh[a]:
            if b<=a:continue
            for c in neigh[a]&neigh[b]:
                if c<=b:continue
                triangles+=1
                v=(1<<index[a,b])^(1<<index[a,c])^(1<<index[b,c])
                while v:
                    bit=v.bit_length()-1
                    if bit in basis:v^=basis[bit]
                    else:basis[bit]=v;break
    unseen=set(range(N)); comps=0
    while unseen:
        comps+=1;st=[unseen.pop()]
        while st:
            a=st.pop()
            for z in neigh[a]&unseen:unseen.remove(z);st.append(z)
    return len(edges)-N+comps-len(basis),triangles,comps

def symmetries(m):
    for pi in permutations(range(m)):
        for shift in range(1<<m):
            def h(x,pi=pi,shift=shift):
                z=shift
                for i in range(m):
                    if (x>>i)&1:z^=1<<pi[i]
                return z
            yield pi,shift,h

def check():
    cases=0;characters=0
    for m in range(6):
        n=m+2;orbs,e2=graph(n,2)
        labels=[lab(o) for o in orbs]
        assert len(set(labels))==len(orbs)==2**(m+1)
        model={(i,j) for i,j in combinations(range(len(orbs)),2)
               if labels[i][0]!=labels[j][0] and d(labels[i][1],labels[j][1])<=1}
        assert e2==model
        assert len(e2)==2**m*(m+1)
        rank,_,comps=h1_rank_f2(len(orbs),e2)
        assert comps==1 and rank==2**m*(m-1)+1
        if m<=3:
            _,e3=graph(n,3)
            expected={(i,j) for i,j in combinations(range(len(orbs)),2)
                      if d(labels[i][1],labels[j][1]) <= (1 if labels[i][0]==labels[j][0] else 2)}
            assert e3==expected
            b3,_,c3=h1_rank_f2(len(orbs),e3)
            assert b3==0 and c3==1
        cases+=1
        print('scale',n,'orbit_vertices',len(orbs),'scale2_edges',len(e2),'H1',rank)
    for m in range(1,4):
        orbs,e2=graph(m+2,2)
        lbs=[lab(o) for o in orbs]
        lookup={x:i for i,x in enumerate(lbs)}
        signed_edges={(i,j):k for k,(i,j) in enumerate(sorted(e2))}
        oriented=[(i,j) if lbs[i][0]==0 else (j,i) for i,j in sorted(e2)]
        # Each edge is oriented from color zero to color one.
        for _,_,h in symmetries(m):
            F={y for y in range(1<<m) if h(y)==y}
            E=sum(d(y,z)==1 for y in F for z in F)//2
            N=sum(h(h(y))==y and d(y,h(y))<=1 for y in range(1<<m))
            for eps in (0,1):
                verts=[lookup[(a^eps,h(y))] for a,y in lbs]
                assert len(set(verts))==len(verts)
                trace0=sum(i==verts[i] for i in range(len(verts)))
                trace1=0
                for i,j in oriented:
                    ai,bj=verts[i],verts[j]
                    assert tuple(sorted((ai,bj))) in e2
                    if ai==i and bj==j:trace1+=1
                    if ai==j and bj==i:trace1-=1
                observed=trace1-trace0+1
                expected=1-len(F)+2*E if eps==0 else 1-N
                assert observed==expected,(m,eps,observed,expected)
                characters+=1
    print('VERIFY_OK',cases,'size cases,',characters,'character evaluations')
if __name__=='__main__':check()

def all_orbits(n,generators):
    group={0}
    for g in generators:group|={x^g for x in tuple(group)}
    rem=set(range(1<<n));out=[]
    while rem:
        x=min(rem);o=frozenset(x^g for g in group)
        assert o<=rem;rem-=o;out.append(o)
    return out

def check_filtration_models():
    validations=0
    for n in range(2,8):
        generators_sets=[('unit',[1]),('two-flip',[3]),('coordinate-plane',[1,2])]
        if n>=3: generators_sets.append(('even-triangle',[3,5]))
        for name,gens in generators_sets:
            o=all_orbits(n,gens)
            defs=[]
            for orb in o:
                x=min(orb)
                if name=='unit': label=x>>1;base=1
                elif name=='coordinate-plane': label=x>>2;base=2
                elif name=='even-triangle':label=((x>>3)<<1)|(x&7).bit_count()%2;base=2
                else:label=lab(orb);base=2
                defs.append(label)
            assert len(set(defs))==len(o)
            for r in range(n+1):
                actual_available=all(max(d(x,z) for x,z in combinations(orb,2))<=r for orb in o)
                assert actual_available==(r>=base)
                if not actual_available: continue
                for i,j in combinations(range(len(o)),2):
                    actual=max(d(x,z) for x in o[i] for z in o[j])<=r
                    if name=='two-flip':
                        (a,y),(b,z)=defs[i],defs[j]
                        predicted=(d(y,z)<=r-2) if a==b else (d(y,z)<=r-1)
                    else:predicted=d(defs[i],defs[j])<=r-base
                    assert actual==predicted,(n,name,r,defs[i],defs[j])
                validations+=1
    print('MODEL_OK',validations,'full-filtration threshold models')

if __name__=='__main__':check_filtration_models()
