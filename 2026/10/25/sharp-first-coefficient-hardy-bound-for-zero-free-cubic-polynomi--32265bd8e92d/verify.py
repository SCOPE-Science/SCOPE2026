"""Exact rational Bernstein certificates for a sharp zero-free cubic coefficient inequality.

Requires only Python 3 standard library. No floating-point decisions.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def mon(dim, idx):
    t = [0] * dim
    t[idx] = 1
    return {tuple(t): Q(1)}


def scalar(dim, value):
    return {tuple([0] * dim): Q(value)}


def add(p, q):
    out = dict(p)
    for term, val in q.items():
        out[term] = out.get(term, Q(0)) + val
    return {t: v for t, v in out.items() if v}


def neg(p):
    return {t: -v for t, v in p.items()}


def sub(p, q):
    return add(p, neg(q))


def mul(p, q):
    out = {}
    for t, v in p.items():
        for s, w in q.items():
            k = tuple(x + y for x, y in zip(t, s))
            out[k] = out.get(k, Q(0)) + v*w
    return {t: v for t, v in out.items() if v}


def scale(p, c):
    return {t: v*Q(c) for t, v in p.items() if v*c}


def pow2(p):
    return mul(p, p)


def sum_poly(*ps):
    out = {}
    for p in ps:
        out = add(out, p)
    return out


def bernstein_coeff(poly, boxes, degree):
    """Exact tensor Bernstein coefficients after affine substitution on boxes."""
    dim = len(boxes)
    N = degree + 1
    # Power-to-Bernstein conversion on [L,U].
    table = {}
    for axis, (lo, hi) in enumerate(boxes):
        high_power = max(k[axis] for k in poly)
        for exponent in range(high_power+1):
            table[(axis, exponent)] = [
                sum((Q(comb(exponent, j) * comb(i, j), comb(degree, j))
                     * lo**(exponent-j) * (hi-lo)**j
                     for j in range(min(i, exponent)+1)), Q(0))
                for i in range(N)]
    out = []
    for indices in product(range(N), repeat=dim):
        s = Q(0)
        for exponents, coefficient in poly.items():
            term = coefficient
            for axis in range(dim):
                term *= table[(axis, exponents[axis])][indices[axis]]
            s += term
        out.append((indices, s))
    return out


def certify(poly, boxes, degree, label, expected_zeros=0):
    coeffs = bernstein_coeff(poly, boxes, degree)
    assert all(c >= 0 for _, c in coeffs), (label, min(coeffs, key=lambda z:z[1]))
    zero = [idx for idx, c in coeffs if c == 0]
    assert len(zero) == expected_zeros, (label, zero)
    minimum = min(c for _,c in coeffs)
    print(label, 'degree', degree, 'min', minimum, 'zero_count', len(zero))
    return zero


def make_phase_lower_bound(signs):
    x,y,z=[mon(3,j) for j in range(3)]
    one=scalar(3,1)
    a,b,c=pow2(x),pow2(y),pow2(z)
    pair=sum_poly(mul(a,b),mul(a,c),mul(b,c))
    F=add(scale(sum_poly(one,pair,mul(mul(a,b),c)),7),scale(sum_poly(a,b,c),-3))
    rs=[x,y,z]
    for k in range(3):
        i,j=[idx for idx in range(3) if idx!=k]
        # -2 sgn(7 r_k^2-3) r_i r_j
        piece=mul(mul(rs[i],rs[j]),sub(scale(pow2(rs[k]),7),scalar(3,3)))
        F=sub(F,scale(piece,2*signs[k]))
    return F


def make_discriminant():
    u,v=mon(2,0),mon(2,1)
    one=scalar(2,1)
    a=sub(one,u);b=sub(one,v)
    p=add(a,b); q=mul(a,b)
    A=sub(scale(add(pow2(p),pow2(q)),7),scalar(2,3))
    C=sub(scale(add(one,pow2(q)),7),scale(pow2(p),3))
    B=mul(p,sub(scalar(2,3),scale(q,7)))
    return sub(mul(A,C),pow2(B))


def main():
    lo=(Q(0),Q(2,3));hi=(Q(13,20),Q(1))
    for case in (0,1,3):
        signs=[1]*case+[-1]*(3-case)
        boxes=[hi]*case+[lo]*(3-case)
        certify(make_phase_lower_bound(signs),boxes,4,'phase_case_'+str(case))
    # The two-high case reduces to a quadratic in the third modulus.
    # A(c+B/A)^2 + (AC-B^2)/A.  A>=7*(13/10)^2-3>0.
    zeros=certify(make_discriminant(), [(Q(0),Q(7,20))]*2,
                  8,'two_high_discriminant',expected_zeros=1)
    assert zeros == [(0,0)]
    # Verify the equality polynomial directly: (1+z)^2(1-z/4).
    coeffs=[Q(1),Q(7,4),Q(1,2),Q(-1,4)]
    norm2=sum(t*t for t in coeffs)
    assert norm2==Q(35,8)
    assert coeffs[1]**2/norm2 == Q(7,10)
    # Boundary roots at z=-1 (double), last zero at z=4.
    # Strict certificate cases and uniqueness of the 2-high zero imply
    # equality only up to scalar and rotations of the variable.
    print('CHECK_OK')

if __name__=='__main__':
    main()
