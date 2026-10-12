"""Exact certificate checker for binary order-eight orientable cycle maximum.
Python 3, standard library only. Every assertion is an exact integer/string test.
"""
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
N = 8
WIDTH = N - 1
VERTICES = 1 << WIDTH

def reversal(x, bits):
    return int(format(x, f"0{bits}b")[::-1], 2)

pairs = tuple(w for w in range(1 << N) if w < reversal(w, N))
assert len(pairs) == 120
pal_eight = tuple(w for w in range(1 << N) if w == reversal(w, N))
assert len(pal_eight) == 16

ports = defaultdict(list)
for i, w in enumerate(pairs):
    source, target = w >> 1, w & (VERTICES - 1)
    for end, v in enumerate((source, target)):
        vr = reversal(v, WIDTH)
        representative = min(v, vr)
        if v == vr:
            sign = None
        else:
            sign = (1 if v == representative else -1) * (1 if end == 0 else -1)
        ports[representative].append((2 * i + end, sign))

assert len(ports) == 72
pal_vertices = tuple(v for v in ports if v == reversal(v, WIDTH))
assert len(pal_vertices) == 16
assert sorted(len(ports[v]) for v in pal_vertices) == [1] * 2 + [2] * 14
for v in pal_vertices:
    entries = ports[v]
    if len(entries) == 2:
        ports[v] = [(entries[0][0], 1), (entries[1][0], -1)]
    else:
        ports[v] = [(entries[0][0], 1)]

edges = {}
for i in range(len(pairs)):
    edges[(2 * i, 2 * i + 1)] = 1
local_edges = 0
for v, entries in ports.items():
    plus = [pid for pid, s in entries if s == 1]
    minus = [pid for pid, s in entries if s == -1]
    for a in plus:
        for b in minus:
            e = tuple(sorted((a, b)))
            assert e not in edges, ("parallel omission and transition", v, e)
            edges[e] = 0
            local_edges += 1
assert len(edges) == 330 and local_edges == 210

# Verify the signed-incidence identity for BOTH orientations of every pair.
for i, w in enumerate(pairs):
    for selected in (w, reversal(w, N)):
        imbalance = [0] * VERTICES
        imbalance[selected >> 1] += 1
        imbalance[selected & (VERTICES - 1)] -= 1
        for v, entries in ports.items():
            if v == reversal(v, WIDTH):
                continue
            contribution = sum(s for pid, s in entries if pid // 2 == i)
            assert imbalance[v] - imbalance[reversal(v, WIDTH)] == contribution

# Exact dual feasible vector: sum = 28, every edge cost dominates its endpoints.
y = tuple(map(int, (ROOT / "DUAL.txt").read_text(encoding="ascii").split()))
assert len(y) == 2 * len(pairs) and sum(y) == 28
for (u, v), cost in edges.items():
    assert y[u] + y[v] <= cost, (u, v, y[u], y[v], cost)

# Verify the lower-bound witness by all 92 cyclic eight-windows.
word = (ROOT / "WITNESS.txt").read_text(encoding="ascii").strip()
assert len(word) == 92 and set(word) <= {"0", "1"}
windows = [int("".join(word[(i + j) % len(word)] for j in range(N)), 2)
           for i in range(len(word))]
assert len(windows) == len(set(windows)) == 92
assert all(w != reversal(w, N) for w in windows)
assert set(windows).isdisjoint({reversal(w, N) for w in windows})
assert len({min(w, reversal(w, N)) for w in windows}) == 92

# Distinct windows imply the period cannot be a proper divisor of 92.
assert all(any(word[i] != word[(i + d) % len(word)] for i in range(len(word)))
           for d in range(1, len(word)) if len(word) % d == 0)

print("VERIFY_OK order=8 pair_orbits=120 quotient_vertices=72 "+
      "ports=240 certificate_edges=330 dual_sum=28 "+
      "upper_bound=92 witness_period=92")
