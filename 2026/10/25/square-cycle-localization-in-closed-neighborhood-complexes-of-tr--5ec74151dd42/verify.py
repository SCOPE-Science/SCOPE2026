"""Exact finite checks for a closed-neighborhood line-graph splitting theorem.
Scientific object: vertex-centered closed-neighborhood simplicial complex of a line graph.
No third-party dependencies.
"""
from itertools import combinations
from random import Random


def norm(edges):
    return tuple(sorted({tuple(sorted(e)) for e in edges}))


def closed_faces(edges):
    E=norm(edges)
    facets=[]
    for a,b in E:
        f=frozenset(x for x in E if a in x or b in x)
        facets.append(f)
    return face_closure(facets)


def face_closure(facets):
    ans=set()
    for f in facets:
        L=list(f)
        for k in range(1,len(L)+1):
            ans.update(frozenset(c) for c in combinations(L,k))
    return ans


def check_one_sum(e1,e2,v):
    e1,e2=norm(e1),norm(e2)
    assert set(e1).isdisjoint(e2)
    assert set(sum((list(e) for e in e1),[])) & set(sum((list(e) for e in e2),[])) == {v}
    A=frozenset(e for e in e1 if v in e)
    B=frozenset(e for e in e2 if v in e)
    assert A and B
    # Triangle-free is a genuine hypothesis, not inferred from tests.
    E=e1+e2
    for a,b,c in combinations(set(sum((list(e) for e in E),[])),3):
        assert not all(tuple(sorted(x)) in E for x in ((a,b),(b,c),(a,c)))
    K=closed_faces(E)
    target=closed_faces(e1)|closed_faces(e2)|face_closure([A|B])
    assert target <= K
    rem=K-target
    center={}
    for s in rem:
        witnesses=[e for e in E if all(set(e)&set(f) for f in s)]
        assert len(witnesses)==1, (s,witnesses)
        w=witnesses[0]
        assert w in A|B
        center[s]=w
    pairs=[]
    for s in rem:
        w=center[s]
        if w not in s:
            upper=s|{w}
            assert upper in rem and center[upper]==w
            pairs.append((s,upper))
    assert len(pairs)*2==len(rem)
    # Descending-dimension elementary collapses; every lower face must be free.
    current=set(K)
    for low,high in sorted(pairs,key=lambda p:(-len(p[0]),repr(sorted(p[0])))):
        assert low in current and high in current
        containing=[f for f in current if low <= f and f!=low]
        assert containing==[high],(low,high,containing)
        current.remove(low);current.remove(high)
    assert current==target
    return len(K),len(rem),len(pairs)


def cycle(n,offset=0):
    return norm([(offset+i,offset+(i+1)%n) for i in range(n)])


def rank_mod(mat,p):
    # Sparse rows indexed by columns -> rank of boundary matrix over prime field.
    piv={};rank=0
    for col in mat:
        a={k:v%p for k,v in col.items() if v%p}
        while a:
            k=min(a)
            if k not in piv:
                inv=pow(a[k],-1,p)
                piv[k]={i:x*inv%p for i,x in a.items() if x%p}
                rank+=1;break
            fac=a[k]
            for i,x in piv[k].items():
                z=(a.get(i,0)-fac*x)%p
                if z:a[i]=z
                else:a.pop(i,None)
    return rank


def betti(edges,p=101):
    f=closed_faces(edges)
    d=max(map(len,f)); faces=[sorted((s for s in f if len(s)==i),key=lambda s:repr(sorted(s))) for i in range(1,d+1)]
    ranks=[0]
    for i in range(1,len(faces)):
        ix={f:j for j,f in enumerate(faces[i-1])}
        cols=[]
        for f in faces[i]:
            a=sorted(f)
            cols.append({ix[frozenset(a[:j]+a[j+1:])]:(-1)**j for j in range(len(a))})
        ranks.append(rank_mod(cols,p))
    ranks.append(0)
    b=[len(faces[i])-ranks[i]-ranks[i+1] for i in range(len(faces))]
    b[0]-=1
    return tuple(b)


def glue_cycles(lengths):
    # Every new cycle meets previous one at vertex 0 and is otherwise disjoint.
    out=[];i=1
    for n in lengths:
        vertices=[0]+list(range(i,i+n-1));i+=n-1
        out.extend((vertices[j],vertices[(j+1)%n]) for j in range(n))
    return norm(out)


def run():
    checks=[]
    for a in (4,5,6,7):
        for b in (4,5,6,7):
            e1=cycle(a)
            e2=glue_cycles([b])
            # ensure shared v=0 only
            e2=norm((0 if x==0 else x+a-1,0 if y==0 else y+a-1) for x,y in e2)
            checks.append(check_one_sum(e1,e2,0))
    cases=[[4],[5],[6],[4,4],[4,5],[5,6],[4,4,4],[4,5,7],[5,5,5],[4,6,6,5]]
    r=Random(57251)
    for ls in cases:
        E=list(glue_cycles(ls))
        for i in range(3):
            j=max(sum((list(e) for e in E),[]))+1
            attach=r.choice(sorted(set(sum((list(e) for e in E),[]))))
            E.append((attach,j))
        got=betti(E)
        want=(0,ls.count(5)+sum(n>=6 for n in ls),ls.count(4))
        got=got+(0,)*(max(len(want)-len(got),0))
        assert got[:len(want)]==want and all(x==0 for x in got[len(want):]),(ls,got,want)
    for n in range(3,11):
        got=betti(cycle(n))
        want={3:(0,),4:(0,0,1)}.get(n,(0,1))
        got=got+(0,)*(max(len(want)-len(got),0))
        assert got[:len(want)]==want,(n,got,want)
    print('PASS: 16 independent vertex-sum collapse certificates,',sum(x[2] for x in checks),'elementary pairs')
    print('PASS: 10 cactus-with-pendant-tree homology computations over GF(101)')
    print('PASS: 8 cycle base cases (lengths 3 through 10)')

if __name__=='__main__':run()
