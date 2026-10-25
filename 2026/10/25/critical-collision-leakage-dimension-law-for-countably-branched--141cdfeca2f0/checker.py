"""Independent finite-arithmetic and numerical diagnostics for the stated dimension law.

Standard Python 3 only. These calculations do not constitute the infinite-system proof.
"""
from fractions import Fraction
from math import isfinite


def zeta(s):
    if s <= 1:
        raise ValueError('s must exceed 1')
    N = 64
    total = sum(k ** (-s) for k in range(1, N))
    total += N ** (1 - s) / (s - 1) + .5 * N ** (-s)
    # Euler-Maclaurin terms B_{2j}/(2j)! times rising factorial.
    terms = [(1 / 12, 1), (-1 / 720, 3), (1 / 30240, 5), (-1 / 1209600, 7)]
    for coefficient, power in terms:
        rising = 1.0
        for k in range(power):
            rising *= s + k
        total += coefficient * rising * N ** (-s - power)
    return total


def no_repeat_sum(q, s, eta):
    c = (1 - eta) / zeta(q)
    z = 0.0
    for k in range(1, 160):
        term = ((-1) ** (k + 1)) * (c ** (k * s)) * zeta(q * k * s)
        z += term
        if k >= 8 and abs(term) < 1e-15:
            break
    return z


def solve_root(func, q):
    left = 1 / q + (1 - 1 / q) / 100000
    right = 1.0
    assert func(left) > 1 and func(right) < 1
    for _ in range(90):
        mid = (left + right) / 2
        if func(mid) > 1:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def exact_matrix_identity():
    # For B_ij=w_j (j != i) and v_i=(lambda+w_i)^-1,
    # Bv - lambda v must be independent of i, equal to T(lambda)-1.
    for ws in ([Fraction(1, 3), Fraction(1, 5)],
               [Fraction(1, 8), Fraction(1, 7), Fraction(1, 9)],
               [Fraction(1, 4), Fraction(1, 11), Fraction(1, 23), Fraction(1, 31)]):
        for lam in (Fraction(2, 5), Fraction(1), Fraction(7, 4)):
            v = [1 / (lam + w) for w in ws]
            target = sum(w * vi for w, vi in zip(ws, v)) - 1
            for i in range(len(ws)):
                residual = sum(ws[j] * v[j] for j in range(len(ws)) if j != i) - lam * v[i]
                assert residual == target
    return True


def main():
    assert exact_matrix_identity()
    print('EXACT_PERRON_IDENTITY_PASS')
    previous_cubic_ratio = -1
    previous_penalty_ratio = -1
    for delta in (0.1, 0.05, 0.025, 0.0125, 0.00625):
        q = 1 + delta
        S2 = zeta(2 * q) / zeta(q) ** 2
        eta = S2 / (1 + S2)
        c = (1 - eta) / zeta(q)
        unrestricted = solve_root(lambda s: c ** s * zeta(q * s), q)
        distinct = solve_root(lambda s: no_repeat_sum(q, s, eta), q)
        assert 1 / q < distinct < unrestricted < 1
        ratio = (unrestricted - distinct) / (delta * S2)
        cubic = (1 - distinct) / delta ** 3
        assert isfinite(ratio) and isfinite(cubic)
        assert previous_penalty_ratio < ratio < 1.05
        assert previous_cubic_ratio < cubic < 3.4
        previous_penalty_ratio, previous_cubic_ratio = ratio, cubic
        print(f'delta={delta:.5f}; dim_unrestricted={unrestricted:.12f}; '
              f'dim_distinct={distinct:.12f}; normalized_penalty={ratio:.8f}; '
              f'cubic_coefficient={cubic:.8f}')
    print('NUMERICAL_DIAGNOSTICS_PASS')


if __name__ == '__main__':
    main()
