"""Integer-arithmetic cross-checks for the isolated-edge/triangle covariance theorem.

Run with Python 3.10 or newer: python CHECK.py
No third-party packages are required.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def formula(n, m):
    """Returns (E[S], E[T], E[ST], Cov(S,T)) in G(n,m)."""
    N = choose(n, 2)
    M = choose(n - 2, 2)
    den = choose(N, m)
    si = Fraction(N * choose(M, m - 1), den)
    tr = Fraction(choose(n, 3) * choose(N - 3, m - 3), den)
    st = Fraction(N * choose(n - 2, 3) * choose(M - 3, m - 4), den)
    return si, tr, st, st - si * tr


def direct_enumeration(n):
    edges = tuple(combinations(range(n), 2))
    edge_bits = {e: 1 << i for i, e in enumerate(edges)}
    tri_masks = [edge_bits[(a, b)] | edge_bits[(a, c)] | edge_bits[(b, c)]
                 for a, b, c in combinations(range(n), 3)]
    counts = [0] * (len(edges) + 1)
    ss = [0] * (len(edges) + 1)
    tt = [0] * (len(edges) + 1)
    st = [0] * (len(edges) + 1)
    for mask in range(1 << len(edges)):
        m = mask.bit_count()
        deg = [0] * n
        chosen = []
        for j, (a, b) in enumerate(edges):
            if (mask >> j) & 1:
                deg[a] += 1
                deg[b] += 1
                chosen.append((a, b))
        s = sum(deg[a] == deg[b] == 1 for a, b in chosen)
        t = sum((mask & tm) == tm for tm in tri_masks)
        counts[m] += 1
        ss[m] += s
        tt[m] += t
        st[m] += s * t
    checked = 0
    for m in range(len(edges) + 1):
        exact = (Fraction(ss[m], counts[m]),
                 Fraction(tt[m], counts[m]),
                 Fraction(st[m], counts[m]))
        expected = formula(n, m)
        assert exact == expected[:3], (n, m, exact, expected)
        assert exact[2] - exact[0] * exact[1] == expected[3]
        checked += 4
    return checked


def sign_prediction(n, m):
    M = choose(n - 2, 2)
    if n < 5 or m < 3 or m > M + 1:
        return 0
    return 1 if m >= (n + 3) // 2 else -1


def analytic_cross_checks():
    total = 0
    for n in range(2, 55):
        N = choose(n, 2)
        M = choose(n - 2, 2)
        test_m = set(range(0, min(N, 24) + 1))
        test_m.update((N, N - 1, N // 2, M + 1, M + 2,
                       (n + 3) // 2 - 1, (n + 3) // 2,
                       (n + 3) // 2 + 1))
        for m in sorted(x for x in test_m if 0 <= x <= N):
            es, et, est, cv = formula(n, m)
            assert (cv > 0) - (cv < 0) == sign_prediction(n, m), (n, m, cv)
            total += 1
            if n >= 5 and 3 <= m <= M + 1:
                # A second conditional-law expression, from the conditional-moment representation.
                KN = Fraction((n + 1) * (n*n - n - 4),
                              (n - 1) * (n*n - 5*n + 2))
                assert cv == es * et * (KN * Fraction(m - 3, m) - 1)
                total += 1
                # The critical point lies strictly between successive integers.
                threshold = Fraction(3 * (n + 1) * (n*n - n - 4),
                                     2 * (3*n*n - 6*n - 1))
                if n % 2:
                    assert Fraction(n + 1, 2) < threshold < Fraction(n + 3, 2)
                else:
                    assert Fraction(n, 2) < threshold < Fraction(n + 2, 2)
                total += 1
    return total


def main():
    checks = sum(direct_enumeration(n) for n in range(2, 7))
    checks += analytic_cross_checks()
    print('PASS:', checks, 'exact assertion checks,',
          'including exhaustive enumeration of all graphs on up to six labeled vertices.')


if __name__ == '__main__':
    main()
