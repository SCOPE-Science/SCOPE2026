"""M4 common data: edges, minimal covers, orbit types. Importable by other scripts."""
import itertools

n = 11
V = list(range(5))
U = list(range(5, 10))
W = 10

edges = set()
for i in range(5):
    a, b = i, (i + 1) % 5
    edges.add((min(a, b), max(a, b)))
for j in range(5):
    u = 5 + j
    for vv in ((j - 1) % 5, (j + 1) % 5):
        edges.add((min(u, vv), max(u, vv)))
for i in range(5):
    edges.add((5 + i, 10))
EDGES = sorted(edges)
assert len(EDGES) == 20

adj = {v: set() for v in range(n)}
for a, b in EDGES:
    adj[a].add(b)
    adj[b].add(a)

# maximal independent sets -> minimal covers
_maximal_ind = []
for mask in range(1 << n):
    S = {v for v in range(n) if mask & (1 << v)}
    if any(a in S and b in S for a, b in EDGES):
        continue
    if all(v in S or (adj[v] & S) for v in range(n)):
        _maximal_ind.append(S)

COVERS = sorted([sorted(set(range(n)) - S) for S in _maximal_ind])
assert len(COVERS) == 16
# verify minimality: no cover strictly contains another... each must be minimal
for i, C in enumerate(COVERS):
    Cset = set(C)
    for v in C:
        assert any(a not in Cset or b not in Cset for a, b in EDGES if v in (a, b)) or True
    # check: removing any vertex breaks cover property
    for v in C:
        rest = Cset - {v}
        assert any(a not in rest and b not in rest for a, b in EDGES), f"not minimal: {C} minus {v}"


def ctype(C):
    Cset = set(C)
    return (len([v for v in Cset if v < 5]),
            len([v for v in Cset if 5 <= v < 10]),
            1 if 10 in Cset else 0)


if __name__ == "__main__":
    for C in COVERS:
        print(ctype(C), C)
