"""Independent pure-Python critical-cycle check for Roman GP(n,2) labelings.

Four consecutive two-vertex column labels form a transfer state; the center
column's Roman conditions are verified when a fifth column is appended.
"""
from collections import deque

K = 9 ** 4
adj = [[] for _ in range(K)]
for s in range(K):
    a, r = divmod(s, 729)
    b, r = divmod(r, 81)
    c, d = divmod(r, 9)
    for e in range(9):
        outer = c // 3 != 0 or any(v == 2 for v in (b // 3, d // 3, c % 3))
        inner = c % 3 != 0 or any(v == 2 for v in (a % 3, e % 3, c // 3))
        if outer and inner:
            adj[s].append(((s % 729) * 9 + e, 7 * (e // 3 + e % 3) - 8))

# Label-correcting shortest potentials, with all initial distances zero.
h = [0] * K
queue = deque(range(K))
inq = [True] * K
updates = 0
while queue:
    s = queue.popleft()
    inq[s] = False
    for t, w in adj[s]:
        if h[t] > h[s] + w:
            h[t] = h[s] + w
            updates += 1
            if not inq[t]:
                queue.append(t)
                inq[t] = True
            assert updates < 1000000

G = [[] for _ in range(K)]
R = [[] for _ in range(K)]
for s in range(K):
    for t, w in adj[s]:
        z = w + h[s] - h[t]
        assert z >= 0
        if z == 0:
            G[s].append(t)
            R[t].append(s)

# Kosaraju with iterative depth-first traversal: no graph library required.
seen = [False] * K
order = []
for root in range(K):
    if seen[root]:
        continue
    stack = [(root, 0)]
    seen[root] = True
    while stack:
        x, j = stack[-1]
        if j == len(G[x]):
            order.append(x)
            stack.pop()
        else:
            stack[-1] = (x, j + 1)
            y = G[x][j]
            if not seen[y]:
                seen[y] = True
                stack.append((y, 0))

component = [-1] * K
sccs = []
for root in reversed(order):
    if component[root] != -1:
        continue
    cid = len(sccs)
    members = []
    todo = [root]
    component[root] = cid
    while todo:
        x = todo.pop()
        members.append(x)
        for y in R[x]:
            if component[y] == -1:
                component[y] = cid
                todo.append(y)
    sccs.append(members)

cyclic = []
for cid, members in enumerate(sccs):
    internal_arcs = sum(component[y] == cid for x in members for y in G[x])
    if len(members) > 1 or internal_arcs:
        cyclic.append((len(members), internal_arcs, members))

assert len(cyclic) == 1 and cyclic[0][:2] == (7, 7)
for x in cyclic[0][2]:
    assert sum(component[y] == component[x] for y in G[x]) == 1
    assert sum(component[y] == component[x] for y in R[x]) == 1

print('states', K)
print('arcs', sum(map(len, adj)))
print('h_min_max', min(h), max(h))
print('tight_arcs', sum(map(len, G)))
print('components', len(sccs))
print('cyclic_component_size_arcs', cyclic[0][:2])
print('PASS')
