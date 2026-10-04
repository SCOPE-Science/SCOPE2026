#!/usr/bin/env python3
from fractions import Fraction as Q


def poly_eval(coeffs, x):
    y = Q(0)
    for c in reversed(coeffs):
        y = y * x + Q(c)
    return y


def mean_poly(L, s):
    # M_{L,s}(r)=sum_{j=1}^L (j-s) r^(j-1)
    return [j - s for j in range(1, L + 1)]


def half_poly(L, s):
    # H_{L,s}(r)=sum_{j=0}^{s-1}r^j-sum_{j=s}^{L-1}r^j.
    return [1 if j < s else -1 for j in range(L)]


def root_bracket(L, s, steps=140):
    coeffs = mean_poly(L, s)
    lo, hi = Q(0), Q(4)
    flo, fhi = poly_eval(coeffs, lo), poly_eval(coeffs, hi)
    assert flo < 0 < fhi, (L, s, flo, fhi)
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = poly_eval(coeffs, mid)
        if fm == 0:
            return mid, mid
        if fm < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def sign_certificate(L, s):
    lo, hi = root_bracket(L, s)
    hcoeffs = half_poly(L, s)
    if lo == hi:
        h = poly_eval(hcoeffs, lo)
        return h, h, lo, hi
    mid = (lo + hi) / 2
    hmid = poly_eval(hcoeffs, mid)
    # Uniform exact derivative bound on [lo,hi].
    deriv_bound = Q(0)
    for j in range(1, L):
        deriv_bound += j * hi ** (j - 1)
    err = (hi - lo) / 2 * deriv_bound
    return hmid - err, hmid + err, lo, hi


def decimal(q, digits=16):
    # display only; all certification above is exact rational arithmetic
    return f"{float(q):.{digits}g}"


def main():
    checked = []
    for L in range(3, 8):
        for s in range(2, L):
            hlo, hhi, rlo, rhi = sign_certificate(L, s)
            assert hlo > 0, (L, s, hlo, hhi)
            checked.append((L, s, rlo, rhi, hlo, hhi, "+"))

    # Eight-point witness: unique positive r making the mean equal to 6.
    hlo, hhi, rlo, rhi = sign_certificate(8, 6)
    assert hhi < 0, (8, 6, hlo, hhi)
    checked.append((8, 6, rlo, rhi, hlo, hhi, "-"))

    # Verify the displayed witness polynomial coefficients exactly.
    assert mean_poly(8, 6) == [-5, -4, -3, -2, -1, 0, 1, 2]
    assert half_poly(8, 6) == [1, 1, 1, 1, 1, 1, -1, -1]

    # Print a compact replay table. The sign column certifies F(s)-1/2.
    print("L s r_lo r_hi sign")
    for L, s, rlo, rhi, hlo, hhi, sign in checked:
        print(L, s, decimal(rlo), decimal(rhi), sign)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
