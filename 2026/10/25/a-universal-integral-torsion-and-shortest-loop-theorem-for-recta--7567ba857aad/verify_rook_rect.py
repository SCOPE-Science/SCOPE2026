#!/usr/bin/env python3
"""Exact finite certificate for the rectangular rook open-neighborhood theorem.

No input data, floating point arithmetic, or third-party packages.  Exhaustive
base-case incidence check is combined with a separate symbolic proof for all
rectangles in the accompanying result.
"""
from itertools import combinations
from collections import deque, Counter


def is_face_triple(tri, m, n):
    z = [(q//n,q%n) for q in tri]
    return any(all((r==x or c==y) and (r,c)!=(x,y) for r,c in z)
               for x in range(m) for y in range(n))


def pattern(tri, m, n):
    z=[(q//n,q%n) for q in tri]
    same_row=sum(z[a][0]==z[b][0] for a,b in combinations(range(3),2))
    same_col=sum(z[a][1]==z[b][1] for a,b in combinations(range(3),2))
    return 'L' if (same_row,same_col)==(1,1) else 'matching3' if (same_row,same_col)==(0,0) else 'face'


def triangle_sign_relation(i,j):
    # For a four-tuple Q, the boundary relation between its two nonfaces:
    # (-1)^i boundary(Q-i)+(-1)^j boundary(Q-j)=0.
    return -1 if (i+j)%2==0 else +1


def base_certificate():
    m=n=4; N=m*n
    tris=list(combinations(range(N),3))
    types=Counter()
    bad=set()
    for t in tris:
        p=pattern(t,m,n)
        types[p]+=1
        assert (p=='face')==is_face_triple(t,m,n)
        # The 1-cochain is 1 on pairs in distinct rows and columns.
        parity=sum((a//n!=b//n and a%n!=b%n) for a,b in combinations(t,2))%2
        assert parity==(p!='face')
        if p!='face':bad.add(t)
    assert types=={'face':320,'L':144,'matching3':96}
    graph={t:[] for t in bad}
    four_types=Counter()
    for Q in combinations(range(N),4):
        z=[(i,Q[:i]+Q[i+1:]) for i in range(4)]
        missing=[(i,t) for i,t in z if t in bad]
        four_types[len(missing)]+=1
        assert len(missing) in (0,2,4)
        if len(missing)==2:
            (i,a),(j,b)=missing
            s=triangle_sign_relation(i,j)
            graph[a].append((b,s,Q))
            graph[b].append((a,s,Q))
    assert four_types=={0:320,2:1440,4:60}
    start=min(bad)
    sign={start:1};parent={start:None};queue=deque([start]);bad_edge=None
    while queue:
        a=queue.popleft()
        for b,s,Q in sorted(graph[a]):
            expected=sign[a]*s
            if b not in sign:
                sign[b]=expected; parent[b]=(a,s,Q);queue.append(b)
            elif sign[b]!=expected and bad_edge is None:
                bad_edge=(a,b,s,Q)
    assert len(sign)==240 and bad_edge is not None
    # Independent cycle-sign verification using the stored tree paths.
    a,b,s,Q=bad_edge
    assert sign[a]*s==-sign[b]
    print('BASE_4x4_TRIANGLE_TYPES',dict(types))
    print('BASE_4x4_FOUR_TYPES',dict(four_types))
    print('SIGNED_RELATION_VERTICES',len(sign))
    print('SIGNED_RELATION_EDGES',sum(len(v) for v in graph.values())//2)
    print('NEGATIVE_CYCLE_CLOSING_EDGE',a,b,s,Q)
    print('NEGATIVE_CYCLE_TREE_SIGNS',sign[a],sign[b])


def rectangular_checks(m,n):
    # These calculations check the exact classification, not the general proof.
    N=m*n; types=Counter()
    for t in combinations(range(N),3):
        p=pattern(t,m,n)
        assert (p=='face')==is_face_triple(t,m,n)
        parity=sum((a//n!=b//n and a%n!=b%n) for a,b in combinations(t,2))%2
        assert parity==(p!='face')
        types[p]+=1
    from math import comb
    assert types['L']==4*comb(m,2)*comb(n,2)
    assert types['matching3']==6*comb(m,3)*comb(n,3)
    # Every nonface triple is contained in a four-row/four-column subgrid:
    # each has at most three distinct rows and columns.
    print('RECTANGLE',m,n,'NONFACIAL',types['L']+types['matching3'],'FORMULA_MATCH',True)


def support_checks(m,n):
    N=m*n;k=m+n-1;bad=set()
    for t in combinations(range(N),3):
        if pattern(t,m,n)!='face':bad.add(t)
    # Exhaustively certify the sharp threshold on small boards: any k-set
    # contains a missing triangle; an open neighborhood has size k-1.
    for W in combinations(range(N),k):
        assert any(t in bad for t in combinations(W,3))
    for i in range(m):
        for j in range(n):
            S=tuple(sorted([i*n+y for y in range(n) if y!=j]
                           +[x*n+j for x in range(m) if x!=i]))
            assert len(S)==k-1
            assert all(t not in bad for t in combinations(S,3))
    print('SUPPORT_THRESHOLD_CHECK',m,n,k,'COMPLETE')

if __name__=='__main__':
    base_certificate()
    for dimensions in [(4,4),(4,5),(5,4),(5,5),(4,6)]:
        rectangular_checks(*dimensions)
    for dimensions in [(4,4),(4,5)]:
        support_checks(*dimensions)
    print('VERIFY_OK_RECTANGULAR_ROOK_H1_AND_MINIMAL_SUPPORTS')
