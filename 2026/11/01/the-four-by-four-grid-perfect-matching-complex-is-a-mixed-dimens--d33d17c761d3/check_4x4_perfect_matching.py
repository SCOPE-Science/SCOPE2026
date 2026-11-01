#!/usr/bin/env python3
"""Self-contained exact finite verification for the 4 by 4 perfect-matching complex.
Requires Python >= 3.9; no external libraries. Run: python check_4x4_perfect_matching.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import heapq

M = N = 4
TOGGLES = (21, 14, 0, 1, 23, 20, 12, 4)
TOP_CYCLE = (1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1)

def enum_edges():
    edges = []
    for r in range(M):
        for c in range(N):
            if r+1<M: edges.append((r*N+c, (r+1)*N+c))
            if c+1<N: edges.append((r*N+c, r*N+c+1))
    assert len(edges)==24
    return edges

def matchings(edges):
    incident = [[] for _ in range(M*N)]
    for j,(u,v) in enumerate(edges):
        incident[u].append((v,j)); incident[v].append((u,j))
    @lru_cache(None)
    def go(mask):
        if mask==0:return ((),)
        u=(mask & -mask).bit_length()-1
        out=[]
        for v,j in incident[u]:
            if (mask>>v)&1:
                for tail in go(mask ^ (1<<u) ^ (1<<v)):
                    out.append(tuple(sorted((j,)+tail)))
        return tuple(out)
    return go((1<<(M*N))-1)

def enumerate_faces(facets):
    f={0}
    for facet in facets:
        for k in range(len(facet)+1):
            for small in combinations(facet,k):
                f.add(sum(1<<j for j in small))
    return f

def bit_elements(mask):
    while mask:
        j=(mask&-mask).bit_length()-1
        yield j
        mask &= mask-1

def toggle_morse(faces):
    remaining=set(faces); pairs=[]
    for j in TOGGLES:
        a=1<<j; removed=set()
        for x in sorted(remaining):
            if not (x&a) and (x|a) in remaining:
                assert x not in removed and (x|a) not in removed
                pairs.append((x,x|a))
                removed.add(x); removed.add(x|a)
        remaining.difference_update(removed)
    assert len(remaining)==3
    assert Counter(x.bit_count()-1 for x in remaining)=={2:2,3:1}
    assert len(pairs)==(len(faces)-3)//2
    assert len({z for pair in pairs for z in pair})==len(faces)-3
    return remaining,pairs

def assert_acyclic(faces,pairs):
    upward=set(pairs)
    adj=defaultdict(list); indeg={x:0 for x in faces}
    incidences=0
    for upper in faces:
        for i in bit_elements(upper):
            lower=upper^(1<<i)
            assert lower in faces
            incidences+=1
            source,target=(lower,upper) if (lower,upper) in upward else (upper,lower)
            adj[source].append(target);indeg[target]+=1
    q=deque(x for x in faces if indeg[x]==0)
    seen=0
    while q:
        x=q.popleft();seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==len(faces),(seen,len(faces))
    return incidences

def greedy_free_collapse(faces):
    live=set(faces);live.remove(0)
    immediate={x:set() for x in live}
    for y in live:
        for i in bit_elements(y):
            x=y^(1<<i)
            if x in live:immediate[x].add(y)
    pq=[]
    def candidate(x):
        if x in live and len(immediate[x])==1:
            heapq.heappush(pq,(-x.bit_count(),x))
    for x in live:candidate(x)
    collapse_pairs=[]
    while pq:
        _,x=heapq.heappop(pq)
        if x not in live or len(immediate[x])!=1:continue
        y=next(iter(immediate[x]))
        assert y.bit_count()==x.bit_count()+1
        # A unique immediate coface is the unique coface in any dimension.
        assert not any((z!=y and z!=x and z&x==x) for z in live)
        collapse_pairs.append((x,y));live.remove(x);live.remove(y)
        for z in (x,y):
            for i in bit_elements(z):
                lower=z^(1<<i)
                if lower in live:
                    immediate[lower].discard(z)
                    candidate(lower)
    assert len(collapse_pairs)==2628
    assert Counter(x.bit_count()-1 for x in live)=={0:14,1:49,2:62,3:25}
    assert len(live)==150
    for x in live:
        for i in bit_elements(x):
            assert x.bit_count()==1 or x^(1<<i) in live
    return live,collapse_pairs

def boundary(faces,degree):
    higher=sorted(f for f in faces if f.bit_count()==degree+1)
    lower=sorted(f for f in faces if f.bit_count()==degree)
    pos={x:i for i,x in enumerate(lower)}
    cols=[]
    for f in higher:
        col=[]
        for j,i in enumerate(bit_elements(f)):
            col.append((pos[f^(1<<i)],1 if j%2==0 else -1))
        cols.append(col)
    return lower,higher,cols

def mod2_rank(cols,n_rows):
    pivots={}
    for col in cols:
        x=0
        for i,_ in col:x ^= 1<<i
        while x:
            top=x.bit_length()-1
            if top in pivots: x ^= pivots[top]
            else:
                pivots[top]=x
                break
    return len(pivots)

def rank_and_cycle_check(core):
    vertices,edges,d1=boundary(core,1)
    edges2,triangles,d2=boundary(core,2)
    triangles2,tetras,d3=boundary(core,3)
    assert edges==edges2 and triangles==triangles2
    for j,col in enumerate(d2):
        accumulation=Counter()
        for i,co in col:
            for r,co2 in d1[i]:accumulation[r]+=co*co2
        assert all(v==0 for v in accumulation.values())
    for j,col in enumerate(d3):
        accumulation=Counter()
        for i,co in col:
            for r,co2 in d2[i]:accumulation[r]+=co*co2
        assert all(v==0 for v in accumulation.values())
    rank1=mod2_rank(d1,len(vertices))
    rank2=mod2_rank(d2,len(edges))
    rank3=mod2_rank(d3,len(triangles))
    assert (rank1,rank2,rank3)==(13,36,24)
    assert len(d3)==len(TOP_CYCLE)==25
    sum_boundary=Counter()
    for z,col in zip(TOP_CYCLE,d3):
        for i,sign in col:sum_boundary[i]+=z*sign
    assert all(v==0 for v in sum_boundary.values())
    assert set(abs(v) for v in TOP_CYCLE)=={1}
    # Rank 24 over F2 gives rank at least 24 over Q; a nonzero
    # exact integral 3-cycle gives rank at most 24 over Q.
    assert len(d3)-rank3==1
    return (rank1,rank2,rank3),Counter({d:sum(x.bit_count()==d+1 for x in core) for d in range(4)})

def main():
    edges=enum_edges();facets=matchings(edges)
    assert len(facets)==36 and len(set(facets))==36
    assert all(len(t)==8 for t in facets)
    faces=enumerate_faces(facets)
    assert len(faces)==5407
    fv=tuple(sum(x.bit_count()==k for x in faces) for k in range(9))
    assert fv==(1,24,212,796,1516,1596,938,288,36)
    critical,pairs=toggle_morse(faces)
    incidences=assert_acyclic(faces,pairs)
    core,collapses=greedy_free_collapse(faces)
    ranks,core_vec=rank_and_cycle_check(core)
    print('facets=36; faces=5407; f_vector='+str(fv))
    print('toggle_order='+str(TOGGLES)+'; pairs='+str(len(pairs))+'; critical_dimensions=(2,2,3)')
    print('hasse_incidences='+str(incidences)+'; acyclicity=PASS')
    print('elementary_collapses='+str(len(collapses))+'; core_f_vector=(14,49,62,25)')
    print('core_boundary_mod2_ranks='+str(ranks)+'; nonzero_integer_3_cycle=PASS')
    print('MORSE_AND_EXACT_TOP_CYCLE_GRID_4X4_OK')

if __name__=='__main__':main()
