#!/usr/bin/env python3
"""Exact finite checks of coordinate-incidence graph Vietoris--Rips collapses."""
from collections import deque, Counter
from itertools import product, combinations
from math import comb

def faces_by_f(d):
    xcoords=list(product((-1,1), repeat=d))
    vx=len(xcoords); N=vx+2*d
    faces=set()
    # Cube-only cliques avoid opposite pairs, exactly 3^(2^(d-1)) faces incl empty.
    neg_index={xcoords.index(tuple(-u for u in x)) for x in xcoords}
    paired=[]
    for i,x in enumerate(xcoords):
        j=xcoords.index(tuple(-u for u in x))
        if i<j:paired.append((i,j))
    assert len(paired)==2**(d-1)
    for state in product((0,1,2), repeat=len(paired)):
        fs=frozenset(paired[k][choice-1] for k,choice in enumerate(state) if choice)
        faces.add(fs)
    xonly_count=len(faces)-1
    matching_by_F=[]
    for k in range(1,d+1):
        for axes in combinations(range(d), k):
            for signs in product((-1,1), repeat=k):
                F=frozenset(vx+2*i+(s==1) for i,s in zip(axes,signs))
                free=[i for i,x in enumerate(xcoords) if all(x[a]==s for a,s in zip(axes,signs))]
                distinguished=next(i for i in free if all(xcoords[i][a]==1 for a in range(d) if a not in axes))
                assert len(free)==2**(d-k)
                for state in product((0,1), repeat=len(free)):
                    U=frozenset(free[i] for i,p in enumerate(state) if p)
                    faces.add(F|U)
                matching_by_F.append((k, F, tuple(free), distinguished))
    full_r2=set(faces)
    pairs=0
    matching_by_F.sort(key=lambda z:-z[0])
    for k,F,free,star in matching_by_F:
        remaining=tuple(i for i in free if i!=star)
        subsets=[]
        for st in product((0,1),repeat=len(remaining)):
            subsets.append(frozenset(remaining[i] for i,p in enumerate(st) if p))
        subsets.sort(key=lambda U:-len(U))
        for U in subsets:
            low=F|U; high=low|{star}
            assert low in faces and high in faces,(d,k,low,high)
            # A face is elementary free exactly when the ONLY currently present immediate coface is high.
            immediate=[low|{t} for t in range(N) if t not in low and low|{t} in faces]
            assert immediate==[high],(d,k,low,len(immediate),immediate)
            faces.remove(low);faces.remove(high);pairs+=1
    # exactly the antipodal free-choice cross-polytope join remains
    assert len(faces)==3**(2**(d-1))
    assert all(not any({i,j}<=fs for i,j in paired) and all(t<vx for t in fs) for fs in faces)
    expected_pairs=sum(comb(d,k)*2**k*2**(2**(d-k)-1) for k in range(1,d+1))
    assert pairs==expected_pairs
    print(f'd={d}, vertices={N}, edges={d*2**d}, complex2_faces={xonly_count + 2*pairs}, collapse_pairs={pairs}, remaining_nonempty_faces={len(faces)-1}, scale2_sphere_dimension={2**(d-1)-1}, scale3_sphere_dimension={2**(d-1)+d-1}, scale3_nonempty_faces={3**(2**(d-1)+d)-1}',flush=True)
    adj=[set() for _ in range(N)]
    for i,x in enumerate(xcoords):
        for a in range(d):
            t=vx+2*a+(x[a]==1)
            adj[i].add(t); adj[t].add(i)
    ds=[]
    for v in range(N):
        dist={v:0}; q=deque([v])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w]=dist[u]+1; q.append(w)
        assert len(dist)==N
        ds.append(dist)
    expected_distance_counts={
        1:d*2**d,
        2:comb(2**d,2)-2**(d-1)+comb(2*d,2)-d,
        3:d*2**d,
        4:2**(d-1)+d,
    }
    actual_distance_counts=Counter(ds[i][j] for i in range(N) for j in range(i+1,N))
    assert actual_distance_counts==expected_distance_counts,(actual_distance_counts,expected_distance_counts)
    if d==3:
        # Independent brute-force clique generation, no use of compatible-facet formula.
        exhaustive2=set()
        exhaustive3=set()
        for mask in range(1<<N):
            ss=frozenset(i for i in range(N) if mask&(1<<i))
            if all(ds[i][j]<=2 for i,j in combinations(ss,2)):
                exhaustive2.add(ss)
            if all(ds[i][j]<=3 for i,j in combinations(ss,2)):
                exhaustive3.add(ss)
        assert exhaustive2==full_r2
        assert len(exhaustive3)==3**(2**(d-1)+d)
        print('d=3 independently enumerated all graph-metric cliques at scales 2 and 3.',flush=True)
    print(f'd={d} complete BFS distance profile: {dict(sorted(actual_distance_counts.items()))}',flush=True)
    return pairs

if __name__=='__main__':
    assert faces_by_f(3)==80
    assert faces_by_f(4)==1296
    print('PASS: exact verified pairwise free-face removal and face-count certificates.')
