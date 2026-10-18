#!/usr/bin/env python3
"""Finite replay for an ordinary three-cut homotopy theorem on Mobius ladders.

All tests are exact combinatorial checks. The uniform infinite proof is in RESULT.md.
Run: python3 VERIFY.py
"""
from itertools import combinations
from collections import deque


def ladder(n):
    N = 2*n
    edges = {tuple(sorted((i, (i+1)%N))) for i in range(N)}
    edges.update((i,i+n) for i in range(n))
    adj = [set() for _ in range(N)]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    return adj


def connected_triple(t, adj):
    return sum(b in adj[a] for a,b in combinations(t,2)) >= 2


def face_data(n):
    adj=ladder(n); N=2*n
    triangles={tuple(t) for t in combinations(range(N),3) if connected_triple(t,adj)}
    tetra={tuple(t) for t in combinations(range(N),4) if all(tuple(q) in triangles for q in combinations(t,3))}
    return adj, triangles, tetra


def rank_mod2(columns):
    piv={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x
                break
            x ^= piv[j]
    return len(piv)


def boundary_rank(faces, lowers):
    lookup={x:i for i,x in enumerate(lowers)}
    return rank_mod2([sum(1<<lookup[sub] for sub in combinations(face,len(face)-1)) for face in faces])


def verify_collapse(n):
    N=2*n
    adj, triangles, tetra=face_data(n)
    all_tetra={tuple(sorted((i,(i+1)%N,(i+n)%N,(i+n+1)%N))) for i in range(n)}
    assert tetra==all_tetra, ('tetrahedral face classification',n, tetra^all_tetra)
    assert len(triangles)==6*n
    faces={1:{(i,) for i in range(N)},
           2:set(combinations(range(N),2)),
           3:set(triangles),4:set(tetra)}
    count=0
    def collapse(high,low):
        nonlocal count
        high=tuple(sorted(high)); low=tuple(sorted(low))
        assert len(high)==len(low)+1, (n,high,low)
        assert high in faces[len(high)] and low in faces[len(low)], (n,high,low)
        cofaces=[]
        for k in range(len(low)+1,5):
            cofaces += [f for f in faces[k] if set(low).issubset(f)]
        assert cofaces==[high], ('not free', n,low,cofaces)
        faces[len(high)].remove(high)
        faces[len(low)].remove(low)
        count+=1
    for i in range(n):
        a=i; b=(i+1)%N; c=(i+n)%N; d=(i+n+1)%N
        collapse((a,b,c,d),(a,b,c))
    for j in range(N):
        collapse(((j)%N,(j+1)%N,(j+2)%N),(j%N,(j+2)%N))
    for i in range(n):
        a=i;b=(i+1)%N;c=(i+n)%N;d=(i+n+1)%N
        collapse((b,c,d),(b,c))
        collapse((a,b,d),(a,b))
        collapse((a,c,d),(a,d))
    assert count==6*n and not faces[3] and not faces[4]
    assert len(faces[2])==N*(N-1)//2-5*n
    remain=faces[2]
    graph=[set() for _ in range(N)]
    for a,b in remain: graph[a].add(b); graph[b].add(a)
    seen={0}; queue=deque([0])
    while queue:
        for k in graph[queue.popleft()]:
            if k not in seen:
                seen.add(k);queue.append(k)
    assert len(seen)==N
    beta=len(remain)-N+1
    assert beta==2*n*n-8*n+1
    return beta


def verify_dual_homology(n):
    # An independent mod-two calculation of the ordinary cut complex, not its dual.
    N=2*n;adj=ladder(n)
    disconnected={t for t in combinations(range(N),3) if not connected_triple(t,adj)}
    # A face is in the cut complex iff a disconnected triple lies in its complement.
    faces_by_size={k:[] for k in range(1,N-2)}
    for k in range(1,N-2):
        for t in combinations(range(N),k):
            comp=set(range(N))-set(t)
            if any(set(q).issubset(comp) for q in disconnected):
                faces_by_size[k].append(t)
    assert faces_by_size[N-3], n
    prev_rank=0
    betti={}
    for k in range(1,N-2):
        curr=boundary_rank(faces_by_size[k+1],faces_by_size[k]) if k+1<N-2 else 0
        if k==1:
            # rank of reduced boundary C0->Z
            rank_prev=1
        else:
            rank_prev=prev_rank
        betti[k-1]=len(faces_by_size[k])-rank_prev-curr
        prev_rank=curr
    expected=2*n*n-8*n+1
    assert {d:b for d,b in betti.items() if b}=={N-4:expected},(n,betti)
    return sum(map(len,faces_by_size.values()))


def main():
    print('Mobius ladder ordinary three-cut verification')
    for n in range(4,41):
        b=verify_collapse(n)
        if n <= 6:
            face_count=verify_dual_homology(n)
            print(f'n={n}: collapses={6*n}, spheres={b}, exact mod-two cut faces={face_count}')
        elif n in (7,8,12,20,40):
            print(f'n={n}: collapses={6*n}, spheres={b}')
    print('VERIFY_OK: 37 exact Alexander-dual collapses and 3 independent full cut-complex homology checks')

if __name__=='__main__': main()
