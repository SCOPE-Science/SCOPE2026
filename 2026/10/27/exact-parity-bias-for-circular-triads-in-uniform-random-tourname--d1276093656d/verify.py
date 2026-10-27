"""Exact standalone checks for the circular-triad parity formula.

Pure Python 3, standard library only. Exhaustive checks use independent
arc-pattern counting; symbolic checks use integer Gaussian arithmetic.
"""
from itertools import combinations
from math import comb


def integer_gaussian_pow(a, b, n):
    r = (1, 0)
    for _ in range(n):
        r = (r[0] * a - r[1] * b, r[0] * b + r[1] * a)
    return r


def symbolic_check():
    checks = 0
    for n in range(2, 101):
        m = comb(n, 2)
        c = comb(n, 3)
        re, im = integer_gaussian_pow(1, -1, n)
        phase = [(re, im), (-im, re), (-re, -im), (im, -re)][m % 4]
        # E[(-1)^T] = signed / 2^n, and the numerator is 2 * real(phase).
        signed = 2 * phase[0] * (-1 if c % 2 else 1)
        assert signed == 2 ** (n - ((n - 1) // 2))
        checks += 1
    return checks


def exhaustive_check():
    checks = 0
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        edge_index = {e: idx for idx, e in enumerate(edges)}
        triple_edges = [tuple(edge_index[e] for e in [(a, b), (b, c), (a, c)])
                        for a, b, c in combinations(range(n), 3)]
        even = odd = 0
        for bits in range(1 << len(edges)):
            outdegree = [0] * n
            for idx, (u, v) in enumerate(edges):
                if bits & (1 << idx):
                    outdegree[v] += 1
                else:
                    outdegree[u] += 1
            triads = comb(n, 3) - sum(comb(d, 2) for d in outdegree)
            triads_direct = sum(((bits >> ab) & 1, (bits >> bc) & 1,
                                 (bits >> ac) & 1) in {(0, 0, 1), (1, 1, 0)}
                                for ab, bc, ac in triple_edges)
            assert triads == triads_direct
            assert 0 <= triads <= comb(n, 3)
            checks += 1
            if triads % 2:
                odd += 1
            else:
                even += 1
        delta = even - odd
        assert delta == (1 << (len(edges) - ((n - 1) // 2)))
        print(f"n={n}: even={even} odd={odd} difference={delta}")
    return checks


if __name__ == "__main__":
    c1 = symbolic_check()
    c2 = exhaustive_check()
    print(f"VERIFY_OK symbolic={c1} exhaustive={c2}")
