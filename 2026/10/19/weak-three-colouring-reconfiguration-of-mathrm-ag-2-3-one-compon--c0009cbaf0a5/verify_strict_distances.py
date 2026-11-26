"""Exact strict-endpoint distances in the labeled weak graph of AG(2,3)."""
from collections import Counter, deque
from itertools import combinations, product

P = list(product(range(3), repeat=2))
lines = [L for L in combinations(range(9), 3)
         if all(sum(P[i][k] for i in L) % 3 == 0 for k in (0, 1))]
assert len(lines) == 12
vertices = [''.join(w) for w in product('012', repeat=9)
            if all(len({w[i] for i in L}) > 1 for L in lines)]
strict = {w for w in vertices if all(len({w[i] for i in L}) == 2 for L in lines)}
assert len(strict) == 162
adj = {w: set() for w in vertices}
for i in range(9):
    buckets = {}
    for w in vertices:
        buckets.setdefault(w[:i] + w[i+1:], []).append(w)
    for c in buckets.values():
        for a, b in combinations(c, 2):
            adj[a].add(b)
            adj[b].add(a)
root = '001001112'
assert root in strict
dist = {root: 0}
todo = deque([root])
while todo:
    a = todo.popleft()
    for b in adj[a]:
        if b not in dist:
            dist[b] = dist[a] + 1
            todo.append(b)
assert strict <= dist.keys()
hist = Counter(dist[w] for w in strict if w != root)
assert hist == {4: 32, 5: 22, 6: 16, 7: 80, 8: 8, 9: 1, 10: 2}
far = {w for w in strict if dist[w] == 10}
assert far == {''.join(str((int(x)+k)%3) for x in root) for k in (1,2)}
print('distance, strict partners per root, unordered strict pairs')
for d, n in sorted(hist.items()):
    print(d, n, n*len(strict)//2)
print('strict partners at distance ten:', ', '.join(sorted(far)))
