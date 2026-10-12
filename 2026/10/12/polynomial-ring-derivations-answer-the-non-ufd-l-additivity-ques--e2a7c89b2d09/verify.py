#!/usr/bin/env python3
from itertools import product

def add(z, w):
    return (z[0] + w[0], z[1] + w[1])

def mul(z, w):
    # (a+b*s)(c+d*s), s^2=-5
    a, b = z
    c, d = w
    return (a*c - 5*b*d, a*d + b*c)

def scale(k, z):
    return (k*z[0], k*z[1])

def norm(z):
    a, b = z
    return a*a + 5*b*b

ZERO = (0, 0)
ONE = (1, 0)
S = (0, 1)

def trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == ZERO:
        q.pop()
    return tuple(q)

def padd(p, q):
    n = max(len(p), len(q))
    out = []
    for i in range(n):
        a = p[i] if i < len(p) else ZERO
        b = q[i] if i < len(q) else ZERO
        out.append(add(a, b))
    return trim(out)

def pmul(p, q):
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] = add(out[i+j], mul(a, b))
    return trim(out)

def deriv(p):
    if len(p) <= 1:
        return (ZERO,)
    return trim(tuple(scale(i, p[i]) for i in range(1, len(p))))

def main():
    two = (2, 0)
    three = (3, 0)
    one_plus_s = (1, 1)
    one_minus_s = (1, -1)
    six = (6, 0)

    assert mul(two, three) == six
    assert mul(one_plus_s, one_minus_s) == six
    assert norm(two) == 4
    assert norm(three) == 9
    assert norm(one_plus_s) == 6
    assert norm(one_minus_s) == 6

    # Exact size reduction: if a^2+5b^2 <= 3, then b=0.
    # Check the remaining integer squares explicitly.
    for target in (2, 3):
        assert all(a*a != target for a in range(-2, 3))
    units = [(a, b) for a in range(-2, 3) for b in range(-1, 2) if norm((a,b)) == 1]
    assert units == [(-1, 0), (1, 0)]

    coeffs = [(-1,0), (0,0), (1,0), (0,1), (0,-1)]
    polys = [trim(p) for p in product(coeffs, repeat=3)]
    # Deduplicate after trimming.
    polys = list(dict.fromkeys(polys))
    checks = 0
    for f in polys:
        for g in polys:
            lhs = deriv(pmul(f, g))
            rhs = padd(pmul(deriv(f), g), pmul(f, deriv(g)))
            assert lhs == rhs
            checks += 1

    # Nonzero witness.
    X = (ZERO, ONE)
    assert deriv(X) == (ONE,)

    print("VERIFY_OK")
    print("explicit_factorization_checks=2")
    print("norm_obstruction_targets=2")
    print("polynomial_product_rule_checks=" + str(checks))

if __name__ == "__main__":
    main()
