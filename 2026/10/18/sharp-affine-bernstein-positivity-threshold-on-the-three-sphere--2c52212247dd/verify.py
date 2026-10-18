"""Exact rational checks for affine Bernstein preservation on the three-sphere.

Run: python3 verify.py
Only the Python standard library is required. Finite checks corroborate the
separate proof of the all-degree statements; they are not its replacement.
"""
from fractions import Fraction as F
from math import comb, factorial


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def mul(p, q):
    v = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            v[i+j] += a*b
    return trim(v)


def scale(p, c):
    return trim([c*a for a in p])


def evaluate(p, x):
    v = F(0)
    for a in reversed(p):
        v = v*x+a
    return v


def u(m):
    if m == 0:
        return [F(1)]
    p0, p1 = [F(1)], [F(0), F(2)]
    for _ in range(1, m):
        p0, p1 = p1, add(mul([0, 2], p1), scale(p0, -1))
    return p1


def r(m):
    return scale(u(m), F(1, m+1))


def bernstein(m, n):
    p, q = [F(0)], r(m)
    for j in range(n+1):
        b = [F(1)]
        for _ in range(j):
            b = mul(b, [F(1,2), F(1,2)])
        for _ in range(n-j):
            b = mul(b, [F(1,2), F(-1,2)])
        p = add(p, scale(b, comb(n, j)*evaluate(q, F(2*j-n, n))))
    return p


def coeffs_in_r_basis(poly, n):
    left = poly[:]
    co = [F(0)]*(n+1)
    for k in range(n, -1, -1):
        top = left[k] if k < len(left) else F(0)
        if not top:
            continue
        bk = r(k)
        co[k] = top/bk[k]
        left = add(left, scale(bk, -co[k]))
    assert all(v == 0 for v in left)
    return co


def exact_check():
    count = 0
    for n in range(1, 5):
        for m in range(121):
            c = coeffs_in_r_basis(bernstein(m, n), n)
            assert all(v >= 0 for v in c), (n, m, c)
            assert sum(c) == 1
            count += 1

    # The complete degree-four formula, checked independently from the nodes.
    for m in range(121):
        N = m + 1
        A = evaluate(r(m), F(1, 2))
        B = evaluate(r(m), F(0))
        c = coeffs_in_r_basis(bernstein(m, 4), 4)
        if m % 2:
            expected = [F(0), F(3,4) + A/2, F(0), F(1,4)-A/2, F(0)]
        else:
            expected = [(21+28*A+15*B)/64, F(0),
                        (81-36*A-45*B)/128, F(0),
                        F(5,128)*(1-4*A+3*B)]
        assert c == expected, (m, c, expected)
        count += 1

    # A finite check of the general negative top coefficient, not an all-n proof.
    for n in range(5, 26):
        c = coeffs_in_r_basis(bernstein(n+2, n), n)
        predicted = F(factorial(n), n**n)*F((n+1)**2*(4-n), 3*n*(n+3))
        assert c[n] == predicted and predicted < 0
        count += 1

    assert coeffs_in_r_basis(bernstein(4, 4), 4) == [F(23,80), 0, F(99,160), 0, F(3,32)]
    assert coeffs_in_r_basis(bernstein(6, 4), 4) == [F(5,14), 0, F(9,14), 0, 0]
    print(f'VERIFY_OK {count} exact rational basis/coefficients comparisons; n=1..4, m=0..120; n=5..25 top obstructions')


if __name__ == '__main__':
    exact_check()
