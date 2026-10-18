#!/usr/bin/env python3
"""Exact combinatorial checks for symmetry of a circular-ladder perfect-matching complex."""
from collections import Counter
from itertools import combinations

N=10

def graph_edges(n):
    edges=[]
    for layer in range(2):
        for i in range(n):
            edges.append(tuple(sorted((layer*n+i,layer*n+(i+1)%n))))
    for i in range(n):
        edges.append((i,n+i))
    assert len(edges)==3*n and len(set(edges))==3*n
    return edges

def perfect_matchings(n,edges):
    by_v={v:[] for v in range(2*n)}
    for j,(u,v) in enumerate(edges):
        by_v[u].append(j);by_v[v].append(j)
    out=set()
    def rec(unmatched,mask):
        if not unmatched:out.add(mask);return
        v=min(unmatched)
        for j in by_v[v]:
            u,w=edges[j];other=w if u==v else u
            if other in unmatched:
                rec(unmatched-{v,other},mask|(1<<j))
    rec(set(range(2*n)),0)
    return out

def all_faces(facets):
    faces={0}
    for f in facets:
        bits=[j for j in range(f.bit_length()) if f>>j&1]
        for k in range(len(bits)+1):
            for comb in combinations(bits,k):
                faces.add(sum(1<<j for j in comb))
    return faces

def conflict_graph(n,edges):
    pairs=set()
    for a,(u,v) in enumerate(edges):
        for b,(x,y) in enumerate(edges):
            if a<b and ({u,v}&{x,y}):pairs.add((a,b))
    # Extra forbidden staggered top/bottom pairs.
    for i in range(n):
        for a,b in ((i,n+(i+1)%n),(n+i,(i+1)%n)):
            pairs.add(tuple(sorted((a,b))))
    return pairs

def independent_faces(vcount,pairs):
    nbr=[0]*vcount
    for a,b in pairs:nbr[a]|=1<<b;nbr[b]|=1<<a
    ans=set()
    def rec(j,mask):
        if j==vcount:ans.add(mask);return
        rec(j+1,mask)
        if not (mask&nbr[j]):rec(j+1,mask|(1<<j))
    rec(0,0)
    return ans,nbr

def bitperm(mask,perm):
    out=0
    while mask:
        z=mask&-mask; j=z.bit_length()-1
        out|=1<<perm[j]
        mask-=z
    return out

def permutation(n,edges,rotation=0,reflection=False,swap=False):
    byedge={e:j for j,e in enumerate(edges)}
    def act(v):
        layer,i=divmod(v,n)
        i=(-i if reflection else i)
        i=(i+rotation)%n
        if swap:layer=1-layer
        return layer*n+i
    return [byedge[tuple(sorted((act(u),act(v))))] for u,v in edges]

def reduced_lefschetz(faces,perm):
    # A setwise-fixed face is a union of vertex-permutation cycles.
    cycles=[];seen=set()
    for i in range(len(perm)):
        if i in seen:continue
        mask=0;j=i
        while j not in seen:
            seen.add(j);mask|=1<<j;j=perm[j]
        cycles.append(mask)
    if len(cycles)<=20:
        # For an invariant face with t selected cycles,
        # (-1)^dimension * orientation sign = (-1)^(t-1).
        total=0
        def rec(i,mask,sign):
            nonlocal total
            if i==len(cycles):
                if mask in faces:total-=sign
                return
            rec(i+1,mask,sign)
            rec(i+1,mask|cycles[i],-sign)
        rec(0,0,1)
        return total
    # Identity action: use the f-vector instead.
    assert all(i==p for i,p in enumerate(perm))
    return -sum((-1)**f.bit_count() for f in faces)

def gf2_rank(columns):
    pivots={}
    for val in columns:
        while val:
            k=val.bit_length()-1
            if k in pivots:val^=pivots[k]
            else:pivots[k]=val;break
    return len(pivots)

def homology_mod2(faces):
    fs={k:sorted(x for x in faces if x.bit_count()==k+1) for k in range(11)}
    ranks={}
    for k in range(1,11):
        index={x:i for i,x in enumerate(fs[k-1])}
        cols=[]
        for f in fs[k]:
            col=0;m=f
            while m:
                z=m&-m;m-=z
                col^=1<<index[f^z]
            cols.append(col)
        ranks[k]=gf2_rank(cols)
    return {k:len(fs[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0) for k in range(11) if len(fs[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)}

from collections import defaultdict
from heapq import heappush,heappop
from fractions import Fraction
import time

def collapse(f):
    incident=defaultdict(set)
    for x in f:
        if x==0:continue
        z=x
        while z:
            bit=z&-z;z-=bit
            incident[x^bit].add(x)
    queue=[]
    for x,ys in incident.items():
        if x and len(ys)==1:heappush(queue,(-x.bit_count(),x))
    removed=set();pairs=[]
    while queue:
        _,x=heappop(queue)
        if x in removed or len(incident[x])!=1:continue
        y=next(iter(incident[x]))
        if y in removed:continue
        pairs.append((x,y))
        for z in (x,y):
            removed.add(z)
            m=z
            while m:
                bit=m&-m;m-=bit
                u=z^bit
                incident[u].discard(z)
                if u and len(incident[u])==1:
                    heappush(queue,(-u.bit_count(),u))
    return pairs,f-removed

def rank_Q(columns):
    pivots={}
    for col in columns:
        v=col
        while v:
            k=max(v)
            if k in pivots:
                q=pivots[k]
                a=v[k]/q[k]
                for j,b in q.items():
                    val=v.get(j,0)-a*b
                    if val:v[j]=val
                    elif j in v:del v[j]
            else:
                pivots[k]=v
                break
    return len(pivots)

def hom_Q(f):
    cells={k:sorted(x for x in f if x.bit_count()==k+1) for k in range(12)}
    ranks={}
    for k in range(1,12):
        index={x:i for i,x in enumerate(cells[k-1])}
        cols=[]
        for x in cells[k]:
            bits=[j for j in range(x.bit_length()) if x>>j&1]
            col={index[x^(1<<j)]:Fraction((-1)**i) for i,j in enumerate(bits)}
            cols.append(col)
        ranks[k]=rank_Q(cols)
    return {k:len(cells[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0) for k in range(12) if len(cells[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)}

edges=graph_edges(N)
pms=perfect_matchings(N,edges)
assert len(pms)==125
P=all_faces(pms)
pairs=conflict_graph(N,edges)
K,nbr=independent_faces(3*N,pairs)
assert K<=P
# Two exceptional perfect matchings not in K: alternating top/bottom patterns.
A=sum(1<<i for i in range(0,N,2))+sum(1<<(N+i) for i in range(1,N,2))
B=sum(1<<i for i in range(1,N,2))+sum(1<<(N+i) for i in range(0,N,2))
assert (pms-K)=={A,B} and A&B==0
assert P==K|all_faces([A,B])
assert all(x.bit_count()==N for x in pms)
for i in range(N):
    assert (nbr[i]&((1<<(N+i))))==0
    assert nbr[i]==nbr[N+i]  # paired horizontal-edge false twins
# Every g preserves P and K; distinct symmetries are checked exhaustively.
characters={}
for swap in range(2):
    for reflect in range(2):
        for rot in range(N):
            g=(swap,reflect,rot)
            perm=permutation(N,edges,rot, bool(reflect),bool(swap))
            assert len(set(perm))==len(edges)
            assert all(bitperm(f,perm) in pms for f in pms)
            assert all((min(perm[a],perm[b]),max(perm[a],perm[b])) in pairs for a,b in pairs)
            Lp=reduced_lefschetz(P,perm)
            Lk=reduced_lefschetz(K,perm)
            # Known cohomological dimensions: H_4(K)=2; H_4(P)=2 and H_3(P)=2.
            chi4=Lk
            chi3=Lk-Lp
            characters[g]=(chi3,chi4)
assert characters[(0,0,0)]==(2,2)
assert characters[(1,0,0)]==(0,2)
# Formula for conjugacy representatives; rotations +/-r, two reflection parities.
for sw in range(2):
    for ro in range(1,5):
        assert characters[(sw,0,ro)]==characters[(sw,0,N-ro)]
    for ro in range(N):
        assert characters[(sw,1,ro)]==characters[(sw,1,ro%2)]
print('n=',N,'graph_edges=',len(edges),'perfect_matchings=',len(pms),
      'faces_P=',len(P),'faces_K0=',len(K),'new_faces_from_2_exceptional_facets=',len(P-K))
print('relative_intersections=',[sum(1 for f in K if f&A==f),sum(1 for f in K if f&B==f)])
for name,complex_ in [('P',P),('K0',K)]:
    print('fvector_'+name+'=',[sum(1 for f in complex_ if f.bit_count()==j+1) for j in range(N+1)])
    print('mod2_reduced_betti_'+name+'=',homology_mod2(complex_))
for name, complex_, goal in [('P',P,{3:2,4:2}),('K0',K,{4:2})]:
    pairs_collapsed, residue=collapse(complex_)
    actual=hom_Q(residue)
    assert actual==goal
    print('exact_rational_reduced_betti_'+name+'=',actual,
          'certified_elementary_collapses=',len(pairs_collapsed),
          'residual_nonempty_faces=',len(residue)-1)
print('full_D10_times_C2_character_by_conjugacy_class:')
for sw in range(2):
    for desc,ref,rot,size in [('id',0,0,1),('r^5',0,5,1),
                              ('r^±1',0,1,2),('r^±2',0,2,2),
                              ('r^±3',0,3,2),('r^±4',0,4,2),
                              ('ref_even',1,0,5),('ref_odd',1,1,5)]:
        print(' swap=',sw,'class=',desc,'size=',size,'chi_H3=',characters[(sw,ref,rot)][0],
              'chi_H4=',characters[(sw,ref,rot)][1])
# Independently evaluate both traces via direct signed fixed-face enumeration for 10 sample elements.
for g in [(0,0,1),(0,0,5),(0,1,0),(0,1,1),(1,0,0),(1,0,2),(1,0,5),(1,1,0),(1,1,1)]:
    sw,ref,rot=g;perm=permutation(N,edges,rot,bool(ref),bool(sw))
    def signed_direct(faces):
        total=0
        for f in faces:
            m=bitperm(f,perm)
            if m!=f:continue
            bits=[i for i in range(3*N) if f>>i&1]
            p=[perm[i] for i in bits]
            inversions=sum(1 for a in range(len(p)) for b in range(a+1,len(p)) if p[a]>p[b])
            total-=(-1)**(len(bits)+inversions)
        return total
    assert signed_direct(P)==reduced_lefschetz(P,perm)
    assert signed_direct(K)==reduced_lefschetz(K,perm)
print('independent_signed_lefschetz_crosschecks=9_group_elements_x_2_complexes_passed')
print('ALL_CHECKS_PASSED')
