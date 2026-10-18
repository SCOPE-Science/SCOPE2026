"""Exhaustive exact-arithmetic certificate for the binary16 stochastic logistic map.

Only Python's standard library is needed. Probabilistic transitions correspond
solely to a single stochastic rounding of the exact real expression 4*x*(1-x).
Both adjacent rounding outputs have positive probability when the value is
strictly between two binary16 numbers. Includes gradual underflow.
"""
from fractions import Fraction
from bisect import bisect_left
from collections import deque, Counter
from hashlib import sha256
import struct

N = 0x3c01                       # 0x0000 through 0x3c00: +0 to +1
A = 0x3a00                       # encoding of 3/4

def binary16(code):
    """Decode nonnegative half bits 0x0000..0x3c00 exactly, no floats."""
    assert 0 <= code <= 0x3c00
    exponent = code >> 10
    fraction = code & 1023
    if exponent == 0:
        return Fraction(fraction, 1 << 24)
    return Fraction(1024 + fraction, 1 << (25-exponent))

values = [binary16(i) for i in range(N)]
assert len(values) == N and values[0] == 0 and values[A] == Fraction(3,4)
assert values[-1] == 1 and all(a < b for a,b in zip(values,values[1:]))
adj = []
edge_stream = bytearray()
for u,x in enumerate(values):
    y = 4*x*(1-x)               # exactly rational, never floating-point
    h = bisect_left(values,y)
    assert 0 <= h < N
    if values[h] == y:
        targets = (h,)
    else:
        assert h > 0 and values[h-1] < y < values[h]
        targets = (h-1,h)
        p = (y-values[h-1])/(values[h]-values[h-1])
        assert 0 < p < 1        # each arc has strictly positive probability
    adj.append(targets)
    edge_stream.extend(struct.pack('>HB',u,len(targets)))
    for v in targets:
        edge_stream.extend(struct.pack('>H',v))
assert len(adj) == N
assert sum(map(len,adj)) == 30623
assert adj[0] == (0,) and adj[A] == (A,)
assert adj[0x3400] == (A,)         # 1/4 maps exactly to 3/4

rev = [[] for _ in range(N)]
for u,outs in enumerate(adj):
    for v in outs:
        rev[v].append(u)

def ancestors(target):
    found = {target}
    work = [target]
    for v in work:
        for u in rev[v]:
            if u not in found:
                found.add(u)
                work.append(u)
    return found

r0 = ancestors(0)
rA = ancestors(A)
assert (len(r0),len(rA),len(r0&rA),len(r0-rA),len(rA-r0)) == (15359,46,44,15315,2)
assert rA-r0 == {0x3400, A}

# Iterative Kosaraju: exact complete SCC check, independent of graph libraries.
visited = bytearray(N)
postorder = []
for root in range(N):
    if visited[root]:
        continue
    visited[root] = 1
    stack = [(root,0)]
    while stack:
        u,k = stack[-1]
        if k == len(adj[u]):
            postorder.append(u)
            stack.pop()
        else:
            stack[-1] = (u,k+1)
            v = adj[u][k]
            if not visited[v]:
                visited[v] = 1
                stack.append((v,0))
assert len(postorder) == N
comp = [-1]*N
sizes = []
for root in reversed(postorder):
    if comp[root] != -1:
        continue
    idx = len(sizes)
    todo = [root]
    comp[root] = idx
    size = 0
    while todo:
        u = todo.pop()
        size += 1
        for v in rev[u]:
            if comp[v] == -1:
                comp[v] = idx
                todo.append(v)
    sizes.append(size)
assert sum(sizes) == N
outgoing = [False]*len(sizes)
for u,outs in enumerate(adj):
    for v in outs:
        if comp[u] != comp[v]:
            outgoing[comp[u]] = True
bottom = {i for i,hasout in enumerate(outgoing) if not hasout}
assert bottom == {comp[0],comp[A]}
assert sizes[comp[0]] == sizes[comp[A]] == 1
assert len(sizes) == 13616
assert max(sizes) == 1746

# A further independently reproducible directed-graph feature.
distance = [-1]*N
Q = deque([0,A])
distance[0] = distance[A] = 0
while Q:
    v = Q.popleft()
    for u in rev[v]:
        if distance[u] == -1:
            distance[u] = distance[v]+1
            Q.append(u)
assert all(d >= 0 for d in distance)
assert max(distance) == 23
assert Counter(distance)[23] == 7

print('states',N)
print('edges',sum(map(len,adj)))
print('bottom_scc',[(len(sizes),sizes[comp[0]],sizes[comp[A]])])
print('reach_zero',len(r0),'reach_three_quarters',len(rA))
print('both',len(r0&rA),'only_zero',len(r0-rA),'only_three_quarters',len(rA-r0))
print('max_shortest_absorption_path',max(distance),'state_count_at_max',distance.count(23))
print('transition_sha256',sha256(edge_stream).hexdigest())
print('PASS: exhaustive binary16 Markov transition and recurrent-class certificate')
