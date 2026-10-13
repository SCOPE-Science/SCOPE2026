"""Exact finite checks for edge--triangle moments in uniform chord diagrams.

Only the Python standard library is needed. Enumeration is exhaustive for the
small labeled subdiagrams used in the proof; whole-diagram checks are finite
cross-checks of the general formulas, not proofs for unbounded chord counts.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def words(m):
    """Every word on m letters, each appearing twice, exactly once."""
    def fill(remaining, pairs):
        if not remaining:
            yield tuple(pairs)
            return
        for pair in combinations(remaining, 2):
            rest = tuple(x for x in remaining if x not in pair)
            yield from fill(rest, pairs + (pair,))
    return fill(tuple(range(2*m)), ())


def crossing(a, b):
    left, right = a
    c, d = b
    return (left < c < right) != (left < d < right)


def clique3(a, b, c):
    return crossing(a, b) and crossing(a, c) and crossing(b, c)


def local_table():
    total = [0, 0, 0, 0, 0, 0]
    cases = [0, 0, 0, 0, 0, 0]
    for pairs in words(2):
        total[0] += 1
        cases[0] += crossing(pairs[0], pairs[1])
    for p in words(3):
        a, b, c = p
        total[1] += 1
        cases[1] += crossing(a, b) and crossing(a, c)
        total[2] += 1
        cases[2] += clique3(a, b, c)
    for p in words(4):
        a, b, c, d = p
        total[3] += 1
        cases[3] += clique3(a, b, c) and crossing(a, d)
        total[4] += 1
        cases[4] += clique3(a, b, c) and clique3(a, b, d)
    for p in words(5):
        a, b, c, d, e = p
        total[5] += 1
        cases[5] += clique3(a, b, c) and clique3(a, d, e)
    expected = [Q(1, 3), Q(2, 15), Q(1, 15),
                Q(1, 35), Q(1, 63), Q(2, 315)]
    assert [Q(c, t) for c, t in zip(cases, total)] == expected
    assert total == [6, 90, 90, 2520, 2520, 113400]
    assert cases == [2, 12, 6, 72, 40, 720]
    return total, cases


def matchings(remaining):
    """Every perfect matching of a specified ordered endpoint set."""
    if not remaining:
        yield ()
        return
    first = remaining[0]
    for j in range(1, len(remaining)):
        pair = (first, remaining[j])
        rest = remaining[1:j] + remaining[j + 1:]
        for smaller in matchings(rest):
            yield (pair,) + smaller


def formulas(n):
    mu_e = Q(comb(n, 2), 3)
    mu_t = Q(comb(n, 3), 15)
    var_e = Q(n * (n-1) * (n+3), 45)
    var_t = comb(n, 3) * (Q(14, 225) + Q(6 * (n-3), 175)
                               + Q((n-3)*(n-4), 350))
    cov = Q(n * (n-1) * (n-2) * (n+4), 315)
    return mu_e, mu_t, var_e, var_t, cov


def global_replay(n):
    count = sx = st = sxx = stt = sxt = 0
    for arcs in matchings(tuple(range(2*n))):
        adj = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                adj[i][j] = adj[j][i] = crossing(arcs[i], arcs[j])
        x = sum(adj[i][j] for i in range(n) for j in range(i + 1, n))
        t = sum(adj[i][j] and adj[i][k] and adj[j][k]
                for i in range(n) for j in range(i + 1, n)
                for k in range(j + 1, n))
        count += 1
        sx += x
        st += t
        sxx += x*x
        stt += t*t
        sxt += x*t
    ex, et = Q(sx, count), Q(st, count)
    measured = (ex, et, Q(sxx, count)-ex*ex,
                Q(stt, count)-et*et, Q(sxt, count)-ex*et)
    expected = formulas(n)
    assert measured == expected, (n, measured, expected)
    return count


def main():
    total, cases = local_table()
    print('LOCAL_OK total=' + repr(total) + ' favorable=' + repr(cases))
    for n in range(3, 8):
        count = global_replay(n)
        print('MOMENTS_OK n=%d matchings=%d' % (n, count))
    for n in range(3, 100):
        ex, et, vx, vt, c = formulas(n)
        assert vx > 0 and vt > 0 and c > 0
        r2 = c*c/(vx*vt)
        assert 0 < r2 < 1
    print('VERIFY_OK exact_local=6 whole_sizes=5 parameter_checks=97 asymptotic_r2=20/21')


if __name__ == '__main__':
    main()
