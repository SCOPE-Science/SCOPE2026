"""Exact-arithmetic checks for two-leader pinning on finite paths.

Python 3 standard library only. The infinite-size proof is analytical,
not inferred from any finite collection of cases.
"""
from fractions import Fraction as Q
from itertools import combinations


def balanced_tail_value(n, d, gain):
    """Exact trace of the grounded inverse at optimum fixed separation."""
    z = n - 1 - d
    a = z // 2
    b = z - a
    t = a * (a + 1) + b * (b + 1)
    gain = Q(gain)
    return ((6 * n + (6 * t + 6 * d * n) * gain
            + (3 * d * t + d * (d * d - 1)) * gain**2)
            / (6 * gain * (d * gain + 2)))


def coeffs(n, d):
    z = n - 1 - d
    a = z // 2
    b = z - a
    t = a * (a + 1) + b * (b + 1)
    return (6 * n, 6 * t + 6 * d * n, 3 * d * t + d * (d * d - 1))


def difference_numerator(n, d, e):
    """F(n,d)-F(n,e) = (q0+q1*g+q2*g²)/[6(d*g+2)(e*g+2)]."""
    a0, a1, a2 = coeffs(n, d)
    b0, b1, b2 = coeffs(n, e)
    return (2 * (a1-b1)+e*a0-d*b0,
            2*(a2-b2)+e*a1-d*b1,
            e*a2-d*b2)


def strictly_positive_quadratic_on_positive_axis(q):
    a, b, c = q
    if a >= 0 and b >= 0 and c >= 0 and (a or b or c):
        return True
    if a > 0 and c > 0 and b < 0 and b*b < 4*a*c:
        return True
    return False


def solve_rational_system(A, b):
    n = len(b)
    mat = [[Q(v) for v in A[i]] + [Q(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if mat[i][j])
        mat[pivot], mat[j] = mat[j], mat[pivot]
        k = mat[j][j]
        mat[j] = [v / k for v in mat[j]]
        for i in range(n):
            if i != j:
                v = mat[i][j]
                if v:
                    mat[i] = [mat[i][h] - v*mat[j][h] for h in range(n+1)]
    return [mat[i][-1] for i in range(n)]


def direct_trace(n, a, b, gain):
    mat = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        mat[i][i] += 1
        mat[i+1][i+1] += 1
        mat[i][i+1] -= 1
        mat[i+1][i] -= 1
    mat[a][a] += gain
    mat[b][b] += gain
    total = Q(0)
    for j in range(n):
        rhs = [Q(1) if i == j else Q(0) for i in range(n)]
        total += solve_rational_system(mat, rhs)[j]
    return total


def check():
    # Every omitted separation has a candidate which dominates for ALL gains.
    candidates = {3: (2,), 4: (3,), 5: (2, 3),
                  6: (3,), 7: (4,), 8: (5,),
                  9: (4, 5, 6), 10: (5, 6, 7)}
    dominance = 0
    for n, active in candidates.items():
        for d in range(1, n):
            if d in active:
                continue
            assert any(strictly_positive_quadratic_on_positive_axis(
                difference_numerator(n, d, e)) for e in active), (n, d)
            dominance += 1

    # All exact quadratic differences defining the critical phase transitions.
    assert difference_numerator(10, 5, 6) == (-12, 84, 30)
    assert difference_numerator(10, 6, 7) == (-12, 60, -42)
    assert difference_numerator(10, 5, 7) == (-24, 144, 0)
    assert difference_numerator(9, 4, 5) == (-6, 96, 60)
    assert difference_numerator(9, 5, 6) == (-6, 84, 30)
    assert difference_numerator(9, 4, 6) == (-12, 180, 96)
    assert difference_numerator(5, 2, 3) == (-6, 24, 6)

    # Exact inverse for every placement at several rational gains.
    inverse_checks = 0
    for n in range(3, 11):
        for a, b in combinations(range(n), 2):
            d = b-a
            for gain in (Q(1,10), Q(1,2), Q(1), Q(2)):
                z = n-1-d
                t = (a*(a+1)+(n-1-b)*(n-b))
                rho = Q(d*gain+1, gain*(d*gain+2))
                interior = ((d+1)*(d*(d-1)*gain**2+6*d*gain+6)
                            / (6*gain*(d*gain+2)))
                expected = Q(t,2) + z*rho + interior
                assert direct_trace(n,a,b,gain) == expected
                assert expected >= balanced_tail_value(n,d,gain)
                inverse_checks += 1

    # Confirm the infinite-family formulas on a broad exact sample.
    # This is NOT the proof for arbitrary m; proof is symbolic in RESULT.md.
    family_checks = 0
    for m in range(2, 61):
        n = 5*m
        for gain, best_d in ((1, 3*m+1), (2, 3*m)):
            best = balanced_tail_value(n, best_d, gain)
            assert all(best < balanced_tail_value(n, d, gain)
                       for d in range(1, n) if d != best_d)
            family_checks += 1
    print('VERIFY_OK', 'dominance_certificates=',dominance,
          'exact_inverse_checks=',inverse_checks,
          'family_sample_cases=',family_checks)


if __name__ == '__main__':
    check()
