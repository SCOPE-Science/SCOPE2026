import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from m4_data import EDGES, n

# Independent stdlib-only re-verification of odd_packing_cert.txt:
# rebuild adjacency from the edge list printed in the file, BFS-test every
# listed nonbipartite set, and confirm the list is EXACTLY the set of all
# nonbipartite subsets (recount from scratch) with zero disjoint pairs.
import ast

cert = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'odd_packing_cert.txt')
lines = open(cert).read().splitlines()
edges = ast.literal_eval(lines[0].split('M4 edges: ', 1)[1])
assert sorted(map(tuple, edges)) == sorted(EDGES), 'edge list mismatch'
adj = {v: set() for v in range(n)}
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)


def is_bipartite(vs):
    S = set(vs)
    color = {}
    for s in vs:
        if s in color:
            continue
        color[s] = 0
        stack = [s]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if u not in S:
                    continue
                if u not in color:
                    color[u] = color[v] ^ 1
                    stack.append(u)
                elif color[u] == color[v]:
                    return False
    return True


listed = [ast.literal_eval(l.split('N ', 1)[1]) for l in lines if l.startswith('N ')]
assert all(not is_bipartite(vs) for vs in listed), 'listed set is bipartite!'
full = []
for mask in range(1 << n):
    vs = sorted(v for v in range(n) if mask & (1 << v))
    if not is_bipartite(vs):
        full.append(vs)
assert sorted(map(tuple, listed)) == sorted(map(tuple, full)), 'list incomplete'
for i in range(len(full)):
    Si = set(full[i])
    for j in range(i + 1, len(full)):
        assert not Si.isdisjoint(full[j]), 'disjoint pair exists'
print('odd-packing certificate verified: %d nonbipartite sets, 0 disjoint pairs' % len(full))
