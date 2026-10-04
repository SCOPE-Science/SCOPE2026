#!/usr/bin/env python3
from itertools import product, combinations

Q = (0, 1, 2)  # stands for 0, 1/2, 1

def gimp(a, b):
    return 2 if a <= b else b

def modal_value(kind, R, v, S):
    vals = []
    for u in S:
        if kind == "box":
            vals.append(gimp(R[u], v[u]))
        else:
            vals.append(min(R[u], v[u]))
    return min(vals) if kind == "box" else max(vals)

def witness_set(kind, R, v):
    S = tuple(range(len(R)))
    z = modal_value(kind, R, v, S)
    return {u for u in S if (
        gimp(R[u], v[u]) if kind == "box" else min(R[u], v[u])
    ) == z}

case_count = 0
for n in range(1, 4):
    worlds = tuple(range(n))
    root = 0
    subsets = []
    for mask in range(1 << n):
        S = {u for u in worlds if (mask >> u) & 1}
        if root in S:
            subsets.append(S)

    specs = []
    for kind in ("box", "diamond"):
        for v in product(Q, repeat=n):
            specs.append((kind, v))

    for R in product(Q, repeat=n):
        # Test pairs, including repeated modalities, so overlapping/equal edges occur.
        for spec1 in specs:
            for spec2 in specs:
                pair = (spec1, spec2)
                full_vals = [
                    modal_value(kind, R, v, worlds)
                    for kind, v in pair
                ]
                edges = [
                    witness_set(kind, R, v)
                    for kind, v in pair
                ]
                assert all(edges)

                for S in subsets:
                    restricted = [
                        modal_value(kind, R, v, tuple(sorted(S)))
                        for kind, v in pair
                    ]
                    preserved = restricted == full_vals
                    hits = all(S & E for E in edges)
                    assert preserved == hits, (n, R, pair, S, full_vals, restricted, edges)
                    case_count += 1

# Sharpness family.
for m in range(1, 13):
    # Worlds: 0=root, i=witness for p_i.
    n = m + 1
    R = [0] * n
    for i in range(1, n):
        R[i] = 2

    diamond_vals = []
    edges = []
    for i in range(1, n):
        v = [0] * n
        v[i] = 2
        z = modal_value("diamond", R, v, range(n))
        E = witness_set("diamond", R, v)
        assert z == 2
        assert E == {i}
        diamond_vals.append(z)
        edges.append(E)

    # Gödel conjunction is minimum.
    assert min(diamond_vals) == 2

    for omitted in range(1, n):
        S = [u for u in range(n) if u != omitted]
        vals = []
        for i in range(1, n):
            v = [0] * n
            v[i] = 2
            vals.append(modal_value("diamond", R, v, S))
        assert min(vals) == 0

print("HITTING_CASES", case_count)
print("SHARP_M_MAX", 12)
print("VERIFY_OK")
