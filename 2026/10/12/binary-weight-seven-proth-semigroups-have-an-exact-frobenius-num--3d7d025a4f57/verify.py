"""Independent finite checks for an exact Proth-semigroup Frobenius formula.

Run: python3 verify.py  (standard library only)
The computations support, but do not replace, the unrestricted proof.
"""
from heapq import heappop, heappush


def residue_shortest_paths(k, n):
    a = k * (1 << n) + 1
    # The finite minimal-generator range is indices 0,...,n+bit_length(k)-1.
    gens = [k * (1 << (n + i)) + 1
            for i in range(1, n + k.bit_length())]
    edges = [(g % a, g) for g in gens]
    dist = [None] * a
    dist[0] = 0
    todo = [(0, 0)]
    while todo:
        d, u = heappop(todo)
        if d != dist[u]:
            continue
        for step, cost in edges:
            v = (u + step) % a
            nd = d + cost
            if dist[v] is None or nd < dist[v]:
                dist[v] = nd
                heappush(todo, (nd, v))
    assert all(x is not None for x in dist)
    return dist


def powers_for_t_and_c(t, c):
    assert t % 2 == 0
    v = t // 2
    exps = [j for j in range(v.bit_length()) if v >> j & 1]
    assert len(exps) <= c <= v
    while len(exps) < c:
        at = next(i for i, exponent in enumerate(exps) if exponent > 0)
        z = exps.pop(at)
        exps.extend((z - 1, z - 1))
    assert sum(1 << e for e in exps) == v
    return [e + 1 for e in exps]


def constructed_witness(a, u):
    if u == 0:
        return 0, []
    if u <= (a + 1) // 2:
        t = 2 * u
    elif u <= a - 7:
        t = a + 1
    elif u <= a - 5:
        t = a + 3
    elif u == a - 4:
        t = a + 5
    else:
        t = a + 7
    c = t - u
    assert (t // 2).bit_count() <= c <= t // 2
    return a * t - u, t, c


def run():
    checks = 0
    sample_pairs = [(127,7),(127,8),(127,9),(127,10),(191,8),(223,8),(319,9)]
    for k, n in sample_pairs:
        a = k * (1 << n) + 1
        target = a * (a + 5) + 3
        shortest = residue_shortest_paths(k, n)
        assert max(shortest) - a == target
        assert shortest.index(max(shortest)) == 3
        assert shortest.count(max(shortest)) == 1
        assert shortest[3] == a * (a + 6) + 3
        print(f"k={k} n={n} multiplicity={a} Frobenius={target} maximizing_residue=3")
        for u in range(a):
            w, t, c = constructed_witness(a, u) if u else (0, 0, 0)
            assert w <= target + a
            assert w % a == (-u) % a
            if c <= 150 and u in {1, 2, 3, 11, (a + 1)//2, a-7, a-6, a-5, a-4, a-3, a-2, a-1}: 
                exps = powers_for_t_and_c(t, c)
                assert sum(k * (1 << (n + i)) + 1 for i in exps) == w
            checks += 1
    bitweight_parameters = 0
    for k, n in [(127, j) for j in range(7, 60)] + [(191,8),(223,8),(319,9)]:
        a = k * (1 << n) + 1
        assert k.bit_count() == 7 and k < (1 << n)
        for offset, expected in [(-1, 7), (1, 8), (3, 8), (5, 9), (7, 8)]:
            assert ((a + offset) // 2).bit_count() == expected
        bitweight_parameters += 1
    print(f"constructive_witness_residues_checked={checks}")
    print(f"binary_weight_parameter_values_checked={bitweight_parameters}")
    print("finite_computation_does_not_prove_infinite_statement=True")
    print("VERIFY_OK")

if __name__ == "__main__":
    run()
