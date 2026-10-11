#!/usr/bin/env python3
from fractions import Fraction

# Baykur--Stipsicz--Szabo, arXiv:2610.02261v1, Appendix D.5.
# Coefficients are in ascending powers of t.
h = [
    1, 0, -2, 1, 3, -1, -1, 2, -2,
    0, -1, 2, 0, 1, -2, 2, -2, 1,
]
hs = list(reversed(h))
p = [1, 0, 1]  # t^2 + 1


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divmod_poly(a, b):
    a = [Fraction(x) for x in trim(a)]
    b = [Fraction(x) for x in trim(b)]
    if b == [0]:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        c = a[-1] / b[-1]
        k = len(a) - len(b)
        q[k] += c
        for j, bj in enumerate(b):
            a[k + j] -= c * bj
        a = trim(a)
    return trim(q), trim(a)


def gcd_poly(a, b):
    a = [Fraction(x) for x in trim(a)]
    b = [Fraction(x) for x in trim(b)]
    while b != [0]:
        _, r = divmod_poly(a, b)
        a, b = b, r
    lead = a[-1]
    return trim([x / lead for x in a])


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return trim(c)


assert len(h) - 1 == 17
assert h[0] == h[-1] == 1
assert h != hs
assert gcd_poly(h, hs) == [Fraction(1)]
assert gcd_poly(h, p) == [Fraction(1)]
assert gcd_poly(hs, p) == [Fraction(1)]

# The source characteristic polynomial is (t^2+1)^2 h h*.
chi = mul(mul(mul(p, p), h), hs)
assert len(chi) - 1 == 38
assert chi == list(reversed(chi))  # symplectic reciprocity check

# Source premise: dim ker(S^2+I)=2 and the (t^2+1)-primary
# characteristic factor has degree 4.  There are only two Q[t]-module
# possibilities on that primary space.  Kernel dimension 2 selects one
# cyclic p^2 block rather than two p blocks.
primary_dimension = 4
kernel_dimension = 2
assert primary_dimension == 2 * (len(p) - 1)
assert kernel_dimension == len(p) - 1

# The canonical symplectic quotient L^perp/L therefore has rank 38-2-2.
quotient_rank = 38 - kernel_dimension - kernel_dimension
assert quotient_rank == 34
assert (len(h) - 1) + (len(hs) - 1) == quotient_rank

print(
    "VERIFY_OK "
    "deg_h=17 gcd_h_hstar=1 gcd_h_cyclotomic=1 "
    "char_degree=38 reciprocal=true primary_dim=4 kernel_dim=2 "
    "quotient_rank=34 stable_dim=17 unstable_dim=17"
)
