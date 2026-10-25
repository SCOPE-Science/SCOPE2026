"""Self-contained finite witness and exhaustive small-order certificate.
All edges have length one; distances along the realized tree are intrinsic.
Python 3 standard library only. Run: python verify_tree_distance.py
"""
from collections import Counter, deque
from itertools import product, combinations
from heapq import heapify, heappop, heappush

WITNESS_A = ((1,0),(1,2),(1,4),(0,5),(0,8),(2,3),(5,6),(5,7))
WITNESS_B = ((1,0),(1,2),(0,4),(0,6),(0,8),(2,3),(4,5),(6,7))
EXPECTED = ((0,10),(1,10),(2,6),(3,2))
EXPECTED_COUNTS = {2:1, 3:1, 4:2, 5:3, 6:6, 7:11, 8:23}

def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for a,b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        adj[a].append(b)
        adj[b].append(a)
    assert len(edges) == n - 1
    return adj

def edge_distance_histogram(n, edges):
    adj = adjacency(n, edges)
    dist = [[-1]*n for _ in range(n)]
    for start in range(n):
        dist[start][start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[start][v] == -1:
                    dist[start][v] = dist[start][u] + 1
                    queue.append(v)
        assert all(d >= 0 for d in dist[start])
    counts = Counter()
    for e,f in combinations(edges,2):
        k = min(dist[a][b] for a in e for b in f)
        counts[k] += 1
    return tuple(sorted(counts.items()))

def canonical_tree(n, edges):
    adj = adjacency(n,edges)
    if n == 1:
        return '()'
    degrees = [len(neigh) for neigh in adj]
    leaves = deque(i for i,d in enumerate(degrees) if d == 1)
    remaining = n
    while remaining > 2:
        size = len(leaves)
        remaining -= size
        for _ in range(size):
            u = leaves.popleft()
            degrees[u] = 0
            for v in adj[u]:
                if degrees[v]:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        leaves.append(v)
    centers = tuple(leaves)
    assert len(centers) in (1,2)
    def rooted(u,parent):
        return '('+''.join(sorted(rooted(v,u) for v in adj[u] if v != parent))+')'
    if len(centers) == 1:
        return rooted(centers[0],-1)
    a,b = centers
    return '['+''.join(sorted((rooted(a,b),rooted(b,a))))+']'

def prufer_tree(n, sequence):
    deg = [1] * n
    for x in sequence:
        deg[x] += 1
    leaves = [i for i,d in enumerate(deg) if d==1]
    heapify(leaves)
    edges=[]
    for x in sequence:
        y=heappop(leaves)
        edges.append((x,y))
        deg[x] -=1
        deg[y] -=1
        if deg[x] == 1:
            heappush(leaves,x)
    assert len(leaves)==2
    edges.append((heappop(leaves),heappop(leaves)))
    return tuple(edges)

def check_minimality():
    print('Exhaustive labeled Prufer trees:')
    for n in range(2,9):
        seen={}
        for sequence in product(range(n),repeat=n-2):
            edges=prufer_tree(n,sequence)
            signature=edge_distance_histogram(n,edges)
            canonical=canonical_tree(n,edges)
            first=seen.setdefault(signature,canonical)
            assert first==canonical, ('collision below nine vertices',n,signature)
        assert len(set(seen.values()))==EXPECTED_COUNTS[n]
        print('n=%d labeled=%d nonisomorphic=%d signatures=%d collision=none'%
              (n,n**(n-2),len(set(seen.values())),len(seen)))

def check_witness():
    a=edge_distance_histogram(9,WITNESS_A)
    b=edge_distance_histogram(9,WITNESS_B)
    assert a == b == EXPECTED
    degrees=lambda edges:tuple(sorted(len(x) for x in adjacency(9,edges)))
    da,db=degrees(WITNESS_A),degrees(WITNESS_B)
    assert da != db
    assert canonical_tree(9,WITNESS_A)!=canonical_tree(9,WITNESS_B)
    print('A degree sequence',da)
    print('B degree sequence',db)
    print('common edge-pair separation counts',a)
    # Pair-distance density on the realized metric tree:
    # (8*2*(1-t)_+ + 2*sum_{k=0}^3 a_k*g(t-k))/8^2,
    # g(s)=s for 0<=s<=1, 2-s for 1<=s<=2, zero else.
    # On intervals [0,1], [1,2], [2,4], [4,5], this equals
    # (4+t)/16, 5/16, (9-2*t)/16, (5-t)/16 respectively.
    # Verify each polynomial piece at three rational interior positions.
    from fractions import Fraction as F
    def g(s):
        return s if 0<=s<=1 else (2-s if 1<s<=2 else F(0))
    def density(t):
        same=16*(1-t) if t<=1 else 0
        different=2*sum(count*g(t-k) for k,count in EXPECTED)
        return (same+different)/64
    for lo,hi,expression in [
        (0,1,lambda t:(4+t)/16),
        (1,2,lambda t:F(5,16)),
        (2,4,lambda t:(9-2*t)/16),
        (4,5,lambda t:(5-t)/16),
    ]:
        for num in (1,2,3):
            t=F(lo)+(F(hi-lo)*num)/4
            assert density(t)==expression(t), (lo,hi,t)
    print('exact density intervals independently checked')

if __name__=='__main__':
    check_witness()
    check_minimality()
    print('CERTIFICATE_OK')
