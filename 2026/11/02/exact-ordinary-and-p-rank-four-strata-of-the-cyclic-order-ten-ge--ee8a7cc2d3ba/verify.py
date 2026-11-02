"""Exact finite-field checks for cyclic genus-six quintic Cartier strata.

Python 3 standard library only.  Finite examples check the formulas; the
manuscript's universal theorem is justified by its mathematical proof.
"""
from math import comb


def trim(a):
    a = a[:]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def sub(a, b, p):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % p
    for i, x in enumerate(b):
        out[i] = (out[i] - x) % p
    return trim(out)


def derivative(a, p):
    return trim([(i * a[i]) % p for i in range(1, len(a))] or [0])


def rem(a, b, p):
    a, b = trim(a), trim(b)
    assert b != [0]
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        c = a[-1] * inv % p
        shift = len(a) - len(b)
        for j, z in enumerate(b):
            a[shift + j] = (a[shift + j] - c*z) % p
        a = trim(a)
    return a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return a


def scalar_same(a, b, p):
    a, b = trim(a), trim(b)
    if a == [0] or b == [0] or len(a) != len(b):
        return False
    nonzero = next(i for i, x in enumerate(b) if x)
    ratio = a[nonzero] * pow(b[nonzero], -1, p) % p
    return ratio != 0 and all(x == ratio*y % p for x, y in zip(a, b))


def choose(a, b, p):
    return comb(a, b) % p if 0 <= b <= a else 0


def coefficient(a, exponent, p):
    """[x^exponent] (x(x^2-1)(x^2-lambda))^a."""
    if exponent < a or (exponent - a) % 2:
        return [0]
    m = (exponent - a) // 2
    if m > 2*a:
        return [0]
    out = [0] * (a + 1)
    sign = (-1) ** (2*a - m)
    for j in range(max(0, m - a), min(a, m) + 1):
        power = a - m + j
        out[power] = (sign * choose(a, j, p) * choose(a, m-j, p)) % p
    return trim(out)


def binomial_one_minus(power, p):
    return trim([(-1)**j * choose(power, j, p) % p for j in range(power+1)])


def qq(n, p):
    return trim([choose(4*n, j, p) * choose(4*n, 3*n-j, p) % p for j in range(3*n+1)])


def eval_poly(a, x, p):
    v = 0
    for c in a[::-1]:
        v = (v*x+c) % p
    return v


def check_prime(p):
    assert p > 13 and p % 10 == 1
    n = (p-1)//10
    q = qq(n, p)
    assert len(q) == 3*n+1 and eval_poly(q, 0, p) and eval_poly(q, 1, p)
    assert len(gcd(q, derivative(q, p), p)) == 1
    assert all(q[j] == q[3*n-j] for j in range(3*n+1))
    assert (eval_poly(q, -1, p) == 0) == (n % 2 == 1)
    b2 = coefficient(4*n, p-1, p)
    target2 = [0]*n + q
    assert scalar_same(b2, target2, p)
    b311 = coefficient(6*n, p-1, p)
    target311 = [0]*(4*n) + binomial_one_minus(2*n, p)
    assert scalar_same(b311, target311, p)
    b322 = coefficient(6*n, 2*p-2, p)
    target322 = mul(binomial_one_minus(2*n, p), q, p)
    assert scalar_same(b322, target322, p)
    b4 = [[coefficient(8*n, h*p-k, p) for k in (1, 2, 3)]
          for h in (1, 2, 3)]
    assert all(b4[h][k] == [0] for h,k in ((0,1),(1,0),(1,2),(2,1)))
    det2 = sub(mul(b4[0][0], b4[2][2], p), mul(b4[0][2], b4[2][0], p), p)
    det = mul(det2, b4[1][1], p)
    target4 = [0]*(9*n) + binomial_one_minus(12*n,p)
    assert scalar_same(det, target4, p)
    print('checked p =', p, 'n =', n, 'rank-drop parameters =', 3*n,
          'cyclic-10 isomorphism classes =', (3*n)//2)


if __name__ == '__main__':
    for p in (31, 41, 61, 71, 101):
        check_prime(p)
    print('VERIFY_OK')
