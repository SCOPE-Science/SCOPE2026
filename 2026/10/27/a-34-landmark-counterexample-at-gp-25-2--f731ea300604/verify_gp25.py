"""Exact finite verification of the strong metric dimension of GP(25,2).

All data are defined from the standard generalized Petersen adjacency rule.
No numerical optimization software, graph library, or external data are used.
"""
from collections import deque
from itertools import combinations

N = 25
V = range(2 * N)
adj = [set() for _ in V]
def link(a, b):
    assert a != b
    adj[a].add(b)
    adj[b].add(a)

for i in range(N):
    link(i, (i + 1) % N)
    link(i, N + i)
    link(N + i, N + ((i + 2) % N))
assert len({tuple(sorted((a,b))) for a in V for b in adj[a]}) == 75
assert all(len(adj[i]) == 3 for i in V)

def distances_bfs(start):
    dist = [-1] * (2*N)
    dist[start] = 0
    q = deque([start])
    while q:
        a = q.popleft()
        for b in adj[a]:
            if dist[b] < 0:
                dist[b] = dist[a] + 1
                q.append(b)
    assert all(d >= 0 for d in dist)
    return dist

D = [distances_bfs(s) for s in V]
# Independent all-pairs calculation by relaxation, not the BFS recursion.
F = [[0 if i==j else (1 if j in adj[i] else 99) for j in V] for i in V]
for k in V:
    for i in V:
        for j in V:
            if F[i][k] + F[k][j] < F[i][j]:
                F[i][j] = F[i][k] + F[k][j]
assert F == D
assert [D[0][j] for j in range(13)] == [0,1,2,3,4,5,5,6,6,7,7,8,8]
assert [D[N][N+j] for j in range(13)] == [0,3,1,4,2,5,3,6,4,7,5,7,6]
assert [D[0][N+j] for j in range(13)] == [1,2,2,3,3,4,4,5,5,6,6,7,7]

# Mutually maximally distant: neither endpoint has a neighbor farther
# from the opposite endpoint.
def mmd(a, b):
    return (all(D[x][b] <= D[a][b] for x in adj[a]) and
            all(D[a][y] <= D[a][b] for y in adj[b]))
H = [{b for b in V if a != b and mmd(a,b)} for a in V]
assert all((a in H[b]) == (b in H[a]) for a in V for b in V)
O = {5,7,9,11,12}
I = {9,11}
def cdiff(i,j):
    t=(i-j) % N
    return min(t, N-t)
for a,b in combinations(V,2):
    want = (a<N and b<N and cdiff(a,b) in O) or (a>=N and b>=N and cdiff(a-N,b-N) in I)
    assert (b in H[a]) == want, (a,b)
assert sum(len(x) for x in H)//2 == 175

# Outer-index bound: translate a chosen independent-set vertex to u_0.
# All other indices then lie in A, which partitions into five cliques.
A={j for j in range(1,N) if j not in H[0]}
cliques=[(1,6,19),(2,15,22),(3,8,21),(4,17,24),(10,23)]
assert A == set().union(*map(set,cliques))
assert sum(map(len,cliques)) == len(A) == 14
for C in cliques:
    assert all(b in H[a] for a,b in combinations(C,2))
# Therefore an independent outer subset has size at most 1+5=6.

# Inner-index bound: five vertex-disjoint 5-cycles cover all 25 indices.
base=(0,9,18,2,11)
cycles=[tuple((x+5*t)%N for x in base) for t in range(5)]
assert set().union(*map(set,cycles)) == set(range(N))
assert sum(map(len,cycles)) == N
for C in cycles:
    assert len(set(C)) == 5
    assert all(N+C[(t+1)%5] in H[N+C[t]] for t in range(5))
# Each such 5-cycle contributes at most 2 independent inner vertices.

U={0,2,4,6,8,10}
W={i for i in range(N) if i%5 in (0,3)}
assert len(U)==6 and len(W)==10
omitted=U | {N+i for i in W}
assert len(omitted)==16
assert all(b not in H[a] for a,b in combinations(sorted(omitted),2))
S=set(V)-omitted
assert len(S)==34

# Directly verify every unordered pair has a shortest-path betweenness
# witness inside S, independently of the strong-resolving-graph theorem.
for a,b in combinations(V,2):
    assert any(D[a][w] == D[a][b]+D[b][w] or
               D[b][w] == D[a][b]+D[a][w] for w in S), (a,b)

print('VERIFY_OK')
print('vertices=50 edges=75; strong_resolving_edges=175 (outer=125 inner=50 mixed=0)')
print('outer clique partition=5 groups; outer independence upper bound=6')
print('inner disjoint pentagons=5; inner independence upper bound=10')
print('independent omitted vertices=16; direct strong resolution=1225 pairs')
print('strong_metric_dimension_GP_25_2=34')
