#!/usr/bin/env python3
"""Standalone integral chain and symmetry certificate for two ordinary three-cut complexes.
Run: python3 verify.py certificate.json
Only Python standard library is used.
"""
import itertools, json, sys
from collections import Counter
from pathlib import Path

N=16
COORDS=tuple(itertools.product(range(4),repeat=2))
INDEX={x:i for i,x in enumerate(COORDS)}
STEPS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
FULL=(1<<N)-1

def graph(name):
    if name=='Shrikhande':
        return tuple(frozenset(INDEX[((x+a)%4,(y+b)%4)] for a,b in STEPS) for x,y in COORDS)
    if name=='Rook':
        return tuple(frozenset(j for j,(a,b) in enumerate(COORDS) if j!=i and (a==x or b==y))
                     for i,(x,y) in enumerate(COORDS))
    raise ValueError(name)

def edge_count(G,vertices):
    return sum(v in G[u] for u,v in itertools.combinations(vertices,2))

def check_graph(G):
    assert all(len(G[i])==6 and i not in G[i] for i in range(N))
    assert all(i in G[j] for i in range(N) for j in G[i])
    assert sum(len(s) for s in G)==96
    assert all(len(G[i]&G[j])==2 for i in range(N) for j in range(i+1,N))

def dual_faces(G):
    bad=[]
    for tri in itertools.combinations(range(N),3):
        if edge_count(G,tri)<2:
            bad.append(sum(1<<i for i in tri))
    assert len(bad)==384
    # Two independent membership constructions, compared for ALL 2^16 subsets.
    membership=[]
    cut_counts=Counter()
    for mask in range(1<<N):
        has_bad=any((mask&tri)==tri for tri in bad)
        complement=FULL^mask
        cut_by_facets=any((complement&tri)==tri for tri in bad)
        if not has_bad: membership.append(mask)
        if cut_by_facets: cut_counts[mask.bit_count()-1]+=1
    faces={d:[] for d in range(4)}
    for mask in membership:
        if mask==0: continue
        assert mask.bit_count()<=4
        face=tuple(i for i in range(N) if mask>>i&1)
        # Separate direct connected-triple test, not based on bad masks:
        assert all(edge_count(G,t)>=2 for t in itertools.combinations(face,3))
        faces[len(face)-1].append(face)
    # Converse for every subset of at most four vertices, independently:
    for size in range(5):
        for face in itertools.combinations(range(N),size):
            mask=sum(1<<i for i in face)
            assert (mask in membership)==all(edge_count(G,t)>=2 for t in itertools.combinations(face,3))
    membership_set=set(membership)
    for mask in range(1<<N):
        complement=FULL^mask
        cut_direct=any((complement&tri)==tri for tri in bad)
        assert cut_direct == (complement not in membership_set)
    assert sum(cut_counts.values())+len(membership)==1<<N
    return faces,dict(sorted(cut_counts.items()))

def boundary(upper,lower):
    index={x:i for i,x in enumerate(lower)}
    return [{index[c[:k]+c[k+1:]]:(-1)**k for k in range(len(c))} for c in upper]

def check_boundary_squared(cols_hi,cols_low):
    for col in cols_hi:
        acc={}
        for mid,a in col.items():
            for row,b in cols_low[mid].items():
                acc[row]=acc.get(row,0)+a*b
        assert not any(acc.values())

def pivot_plan(columns,nrows,plan=None):
    # Unimodular row elimination, followed by column elimination of the pivot row;
    # the latter changes no remaining row because the pivot column has been cleared.
    rows=[{} for _ in range(nrows)]
    for j,col in enumerate(columns):
        for i,a in col.items():
            assert a in (-1,1)
            rows[i][j]=a
    active=set(range(nrows))
    activecols=set(range(len(columns)))
    pivots=[]
    while True:
        if plan is None:
            candidates=[]
            for i in active:
                for j,v in rows[i].items():
                    if abs(v)==1:
                        size=sum(j in rows[k] for k in active)
                        candidates.append(((len(rows[i])-1)*(size-1),len(rows[i])+size,i,j))
            if not candidates:break
            _,_,i,j=min(candidates)
        else:
            if len(pivots)==len(plan):break
            i,j=plan[len(pivots)]
            assert i in active and j in activecols and abs(rows[i].get(j,0))==1
        u=rows[i][j]
        pivot=rows[i].copy()
        for k in list(active):
            if k==i or j not in rows[k]:continue
            multiple=rows[k][j]//u
            for c,val in pivot.items():
                new=rows[k].get(c,0)-multiple*val
                if new:rows[k][c]=new
                else: rows[k].pop(c,None)
        active.remove(i); activecols.remove(j)
        for k in active:rows[k].pop(j,None)
        rows[i]={}
        pivots.append([i,j])
    # All remaining entries are zero. These are integer unit Smith pivots.
    assert all(not rows[i] for i in active)
    return pivots

def sign_sequence(s):
    return -1 if sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))%2 else 1

def permutation_cycles(p):
    seen=set();cyc=[]
    for i in range(len(p)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:
            seen.add(j);c.append(j);j=p[j]
        cyc.append(tuple(c))
    return cyc

def cycle_type(p):
    seen=set();dims=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;length=0
        while j not in seen:
            seen.add(j);length+=1;j=p[j]
        dims.append(length)
    return tuple(sorted(dims))

def automorphisms(G):
    # The vertex stabilizer acts faithfully on the induced six-cycle of neighbors:
    # every other vertex is uniquely identified by its pair of neighbors there.
    neigh=G[0]
    assert all(sum(w in G[v] for w in neigh)==2 for v in neigh)
    # The local graph really is a connected six-cycle, not two triangles.
    reached={next(iter(neigh))}
    stack=list(reached)
    while stack:
        v=stack.pop()
        for w in G[v]&neigh:
            if w not in reached: reached.add(w); stack.append(w)
    assert reached==neigh
    dist2=set(range(N))-(set(neigh)|{0})
    assert len({tuple(sorted(G[v]&neigh)) for v in dist2})==9
    perms=[]
    for a,b,c,d in itertools.product(range(4),repeat=4):
        if (a*d-b*c)%2==0:continue
        if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in STEPS}!=STEPS:continue
        for q,r in COORDS:
            p=tuple(INDEX[((a*x+b*y+q)%4,(c*x+d*y+r)%4)] for x,y in COORDS)
            assert all((j in G[i]) == (p[j] in G[p[i]]) for i in range(N) for j in range(N))
            perms.append(p)
    # At most 16 choices for the image of one vertex and 12 for the
    # dihedral automorphism of its neighbor six-cycle; equality proves fullness.
    assert len(perms)==len(set(perms))==192
    return perms

def chain_trace(faces,p):
    out=0
    for face in faces:
        image=tuple(p[i] for i in face)
        if tuple(sorted(image))==face:out+=sign_sequence(image)
    return out

def character(G,F):
    bad=[sum(1<<i for i in t) for t in itertools.combinations(range(N),3)
         if edge_count(G,t)<2]
    cut_faces={m for m in range(1<<N) if any(((FULL^m)&t)==t for t in bad)}
    assert len(cut_faces)==65163
    histogram=Counter()
    checks=0
    for perm in automorphisms(G):
        sign=sign_sequence(perm)
        assert sign==1  # The entire full automorphism group acts by even 16-point permutations.
        tr=[chain_trace(F[d],perm) for d in range(4)]
        chi_H2=tr[0]-tr[1]+tr[2]-tr[3]-1
        chi_cut=sign*chi_H2 # Integral Alexander duality's ambient orientation twist.
        # Independently compute equivariant Euler characteristic DIRECTLY on
        # the cut complex, using cycle-union fixed simplices. A selected
        # cycle contributes a factor -1 to oriented Euler sign; in degree 11
        # the homology character equals the alternating cycle-subset sum.
        cycles=permutation_cycles(perm)
        masks=[sum(1<<v for v in c) for c in cycles]
        total_direct=0
        for subset in range(1<<len(cycles)):
            m=0
            for k,cm in enumerate(masks):
                if subset>>k&1:m|=cm
            if m in cut_faces:
                total_direct+=(-1)**subset.bit_count()
        assert total_direct==chi_cut
        histogram[(cycle_type(perm),chi_cut)]+=1
        checks+=1
    return [[list(typ),chi,mult] for (typ,chi),mult in sorted(histogram.items())], checks

def analyze(name):
    G=graph(name);check_graph(G)
    F,cutf=dual_faces(G)
    f=[len(F[d]) for d in range(4)]
    B1=boundary(F[1],F[0]);B2=boundary(F[2],F[1]);B3=boundary(F[3],F[2])
    check_boundary_squared(B2,B1);check_boundary_squared(B3,B2)
    # Based at vertex 0: cycle lattice of complete one-skeleton is identified
    # integrally with its 105 non-star edges.
    roots=[i for i,e in enumerate(F[1]) if 0 not in e]
    assert len(roots)==105
    loc={r:i for i,r in enumerate(roots)}
    B2reduced=[{loc[i]:v for i,v in col.items() if i in loc} for col in B2]
    B3full=B3
    return G,F,cutf,f,B2reduced,B3full

def main():
    if len(sys.argv)!=2:raise SystemExit('Usage: python3 verify.py certificate.json')
    cert=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    assert cert['schema_version']==1
    allresults={}
    for name in ('Shrikhande','Rook'):
        G,F,cutf,f,B2,B3=analyze(name)
        obj=cert['graphs'][name]
        assert obj['dual_f_vector']==[1]+f
        assert obj['cut_f_vector']=={str(k):v for k,v in cutf.items()}
        p2=pivot_plan(B2,105,obj['unit_pivots_d2'])
        p3=pivot_plan(B3,len(F[2]),obj['unit_pivots_d3'])
        assert p2==obj['unit_pivots_d2'] and p3==obj['unit_pivots_d3']
        assert len(p2)==105 and len(p3)==len(F[3])
        # Algebraic Alexander duality: H_(16-i-3)(cut;Z) = H^i(dual;Z).
        # d2 is onto the 1-cycle lattice, d3 injective and primitive.
        rank=len(F[2])-len(p2)-len(p3)
        assert rank==obj['cut_wedge_rank']
        assert obj['cut_wedge_dim']==11
        assert all(k<=12 for k in cutf) and cutf[12]==384
        if name=='Shrikhande':
            rows,count=character(G,F)
            assert rows==cert['shrikhande_character_by_cycle_type_and_trace']
            assert count==192
            total=sum(chi*mult for _typ,chi,mult in rows)
            assert total==0
            assert sum(mult for _typ,chi,mult in rows)==192
            assert len(rows)==12
            assert obj['cut_wedge_rank']==11
            print('SHRIKHANDE_3CUT: 16 vertices, 48 edges, dual faces', obj['dual_f_vector'], 'cut faces',sum(cutf.values()))
            print('SHRIKHANDE_BOUNDARIES: d2',len(p2),'unit pivots, d3',len(p3),'unit pivots, H2 dual = Z^11')
            print('SHRIKHANDE_CHARACTER: 192 automorphisms, 12 trace/cycle groups, sum=0, invariant rank=0')
        else:
            assert obj['cut_wedge_rank']==27
            print('ROOK_3CUT: dual faces',obj['dual_f_vector'],'cut faces',sum(cutf.values()))
            print('ROOK_BOUNDARIES: d2',len(p2),'unit pivots, d3',len(p3),'unit pivots, H2 dual = Z^27')
        allresults[name]={'cut_wedge_rank':rank,'unit_pivots_d2':len(p2),'unit_pivots_d3':len(p3)}
    assert allresults['Shrikhande']['cut_wedge_rank'] != allresults['Rook']['cut_wedge_rank']
    print('SHRIKHANDE_ROOK_THREE_CUT_INTEGRAL_EQUIVARIANT_OK')

if __name__=='__main__':main()
