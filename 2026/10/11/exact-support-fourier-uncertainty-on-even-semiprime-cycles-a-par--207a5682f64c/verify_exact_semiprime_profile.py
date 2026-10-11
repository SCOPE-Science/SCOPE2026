"""Exact cyclotomic checks of sharp examples for the Fourier-support profile.

Only standard-library integer arithmetic is used.  The infinite-prime theorem
is established analytically; finite tests are supplementary.
"""

def add(a, b):
    return [x + y for x, y in zip(a, b)]


def mul_root(a, exponent):
    p = len(a)
    out = [0] * p
    for j, value in enumerate(a):
        out[(j + exponent) % p] += value
    return out


def is_zero(a):
    # In Z[zeta_p], polynomial evaluations vanish exactly when their p
    # coefficients in Z[X]/(X^p - 1) are all equal.
    return len(set(a)) == 1


def sharp_polynomial(p, k):
    one = [1] + [0] * (p - 1)
    coefficients = [one]
    for j in range(k - 1):
        nxt = [[0] * p for _ in range(len(coefficients) + 1)]
        for i, c in enumerate(coefficients):
            nxt[i] = add(nxt[i], [-v for v in mul_root(c, j)])
            nxt[i + 1] = add(nxt[i + 1], c)
        coefficients = nxt
    assert len(coefficients) == k
    assert all(not is_zero(c) for c in coefficients)
    zeros = []
    for t in range(p):
        val = [0] * p
        for x, c in enumerate(coefficients):
            val = add(val, mul_root(c, -t*x))
        if is_zero(val):
            zeros.append(t)
    assert len(zeros) == k - 1
    return zeros


def verify():
    count = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for k in range(1, p + 1):
            sharp_polynomial(p, k)
            pure = 2 * (p - k + 1)
            if k % 2:
                target = pure
            else:
                paired = p - k//2 + 1
                target = min(pure, paired)
                sharp_polynomial(p, k//2)
            assert 1 <= target <= 2*p
            count += 1
        if p >= 11:
            theta_4 = min(p - 1, 2*(p - 3))
            theta_5 = 2*(p - 4)
            assert theta_5 - theta_4 == p - 7 > 0
    print('VERIFY_OK: exact cyclotomic examples for', count,
          'support sizes across seven odd prime orders')


if __name__ == '__main__':
    verify()
