"""Exact certificates for the signed Fano-incidence Ising energy moments.

Run with Python 3.10+; no external packages are required.
All loops range over complete, explicitly bounded finite sets.
"""
from collections import Counter, defaultdict, deque
from math import comb

LINES = ((0, 1, 3), (0, 2, 5), (0, 4, 6),
         (1, 2, 4), (1, 5, 6), (2, 3, 6), (3, 4, 5))
EDGES = tuple(sorted((p, 7 + j) for j, line in enumerate(LINES) for p in line))
N, M = 14, 21
assert len(EDGES) == M and len(set(EDGES)) == M
assert set(tuple(sorted((a, b))) for line in LINES for a in line
           for b in line if a < b) == {(a, b) for a in range(7) for b in range(a + 1, 7)}
assert all(sum(p in line for line in LINES) == 3 for p in range(7))

# A deterministic breadth-first spanning tree on the connected incidence graph.
adj = [[] for _ in range(N)]
for e, (u, v) in enumerate(EDGES):
    adj[u].append((v, e)); adj[v].append((u, e))
tree = []
seen, queue = {0}, deque([0])
while queue:
    u = queue.popleft()
    for v, e in adj[u]:
        if v not in seen:
            seen.add(v); tree.append(e); queue.append(v)
assert len(seen) == N and len(tree) == N - 1
chords = sorted(set(range(M)) - set(tree))
assert len(chords) == 8
T = [[] for _ in range(N)]
for e in tree:
    u, v = EDGES[e]; T[u].append((v, e)); T[v].append((u, e))

def tree_path_mask(start, finish):
    todo = deque([(start, 0)]); visited = {start}
    while todo:
        u, path = todo.popleft()
        if u == finish:
            return path
        for v, e in T[u]:
            if v not in visited:
                visited.add(v); todo.append((v, path ^ (1 << e)))
    raise AssertionError('tree disconnected')

fundamental = [(1 << e) ^ tree_path_mask(*EDGES[e]) for e in chords]
even_subgraphs = []
for subset in range(256):
    mask = 0
    for j, fundamental_mask in enumerate(fundamental):
        if (subset >> j) & 1:
            mask ^= fundamental_mask
    even_subgraphs.append(mask)
assert len(set(even_subgraphs)) == 256
for mask in even_subgraphs:
    assert all(sum((mask >> e) & 1 for _, e in adj[v]) % 2 == 0 for v in range(N))
assert Counter(x.bit_count() for x in even_subgraphs) == {0: 1, 6: 28, 8: 21, 10: 84, 12: 98, 14: 24}

# Every cut is represented once upon fixing the spin at vertex zero.
cut_masks = []
for spin_bits in range(1 << (N - 1)):
    spin = spin_bits << 1
    cut_masks.append(sum(1 << e for e, (u, v) in enumerate(EDGES)
                         if ((spin >> u) ^ (spin >> v)) & 1))
assert len(set(cut_masks)) == 1 << 13

# Krawtchouk transform: independent reconstruction of the cut-coset
# weight distribution from the complete, 256-element even-cycle space.
weights = (0, 6, 8, 10, 12, 14)
def krawtchouk(degree, weight):
    return sum((-1)**j * comb(weight, j) * comb(M-weight, degree-j)
               for j in range(max(0, degree-(M-weight)), min(weight, degree)+1))
K = {(f, w): krawtchouk(f, w) for f in range(M + 1) for w in weights}

classes = defaultdict(list)
dos_classes = defaultdict(set)
for signature in range(256):
    # Switching makes all tree edges positive; remaining eight signs are free.
    negative = sum((1 << e) for j, e in enumerate(chords) if (signature >> j) & 1)
    frequencies = [0] * (M + 1)
    for cut in cut_masks:
        frequencies[(cut ^ negative).bit_count()] += 1
    assert sum(frequencies) == (1 << 13)
    L = next(f for f, count in enumerate(frequencies) if count)
    signed_cycles = Counter()
    for even in even_subgraphs:
        signed_cycles[even.bit_count()] += 1 - 2 * ((negative & even).bit_count() % 2)
    c6, c8 = signed_cycles[6], signed_cycles[8]
    for f in range(M + 1):
        numerator = sum(signed_cycles[w] * K[f, w] for w in weights)
        assert numerator % 256 == 0
        assert frequencies[f] == numerator // 256
    moments = [sum(count * (2*f-M)**k for f, count in enumerate(frequencies)) // (1 << 13)
               for k in range(9)]
    assert all(sum(count * (2*f-M)**k for f, count in enumerate(frequencies)) % (1 << 13) == 0
               for k in range(9))
    assert moments[0] == 1 and moments[2] == 21 and moments[4] == 1281
    assert all(moments[k] == 0 for k in (1, 3, 5, 7))
    assert moments[6] == 126021 + 720*c6
    assert moments[8] == 16784481 + 20160*(2*c8 + 17*c6)
    classes[(c6, c8, L)].append(signature)
    dos_classes[(c6, c8)].add(tuple(frequencies))

EXPECTED = {
    (-8, 9, 3): 28,
    (-4, -3, 3): 56,
    (0, -7, 3): 24,
    (0, 1, 2): 84,
    (4, -3, 2): 42,
    (12, 5, 1): 21,
    (28, 21, 0): 1,
}
assert {k: len(v) for k, v in classes.items()} == EXPECTED
assert len(dos_classes) == 7 and all(len(D) == 1 for D in dos_classes.values())
assert len({next(iter(D)) for D in dos_classes.values()}) == 7
assert len({L for (c6,c8,L) in classes if c6 == 0}) == 2
assert len({L for (c6,c8,L) in classes if (c6,c8) == (0,1)}) == 1
assert len({L for (c6,c8,L) in classes if (c6,c8) == (0,-7)}) == 1
print('VERIFY_OK 256_signatures 8192_spin_cuts 256_even_subgraphs 7_DOS_types cutoff_8')
for (c6, c8, L), members in sorted(classes.items()):
    print('c6=%3d c8=%3d frustration=%d signatures=%3d' % (c6,c8,L,len(members)))
