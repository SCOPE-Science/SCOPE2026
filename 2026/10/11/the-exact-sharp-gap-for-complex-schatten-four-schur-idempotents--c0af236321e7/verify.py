#!/usr/bin/env python3
"""Reproducibility checks for the exact Schatten-four Schur-idempotent gap."""
import itertools
import math
import random
from fractions import Fraction


def fourth_power_schatten(a, z, w, b):
    square_sum = abs(a)**2 + abs(z)**2 + abs(w)**2 + abs(b)**2
    determinant = a * b - z * w
    value = square_sum**2 - 2 * abs(determinant)**2
    return max(0.0, value)


def poly_gap(t):
    return t * (3 * t + 4) / ((1 + t)**4 * (t*t + 4*t + 2))


def positive_root():
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        f = mid**3 + 4*mid*mid + 3*mid - 1
        if f > 0: hi = mid
        else: lo = mid
    return (lo + hi) / 2


def polynomial_identity_checks():
    # Degrees <= 12 make 27 integer evaluations sufficient for identity.
    checks = 0
    for b in range(-13, 14):
        a = -b**3 - 2*b
        n = a**4 + 4*a*a + 2
        d = a**4 + b**4 + 4*(a*a+b*b+a*b) + 2
        assert d == (1+b*b)**4 * (b**4+4*b*b+2)
        assert n-d == b*b*(3*b*b+4)
        checks += 2
    return checks


def classification_checks():
    checks=0
    for rows, cols in ((2,2),(2,3),(3,3)):
        for flat in itertools.product((0,1),repeat=rows*cols):
            m = [flat[i*cols:(i+1)*cols] for i in range(rows)]
            triangle = False
            for i in range(rows):
                for j in range(i+1,rows):
                    si = {k for k in range(cols) if m[i][k]}
                    sj = {k for k in range(cols) if m[j][k]}
                    if si & sj and si!=sj:
                        triangle=True
            classes={}
            for i in range(rows):
                supp=tuple(j for j in range(cols) if m[i][j])
                if supp:classes.setdefault(supp,[]).append(i)
            row_sets=list(classes.keys())
            disjoint=all(not(set(x)&set(y)) for i,x in enumerate(row_sets) for y in row_sets[i+1:])
            assert triangle != disjoint
            checks+=1
    return checks


def random_checks(kappa):
    rng=random.Random(2404713)
    checks=0
    for _ in range(25000):
        vals=[complex(rng.uniform(-2,2), rng.uniform(-2,2)) for _ in range(4)]
        a,z,w,b=vals
        before=fourth_power_schatten(a,z,w,b)
        after=fourth_power_schatten(a,z,w,0)
        assert after <= (kappa**4 + 2e-12)*before + 1e-10, (before,after)
        checks+=1
    return checks


def main():
    exact=polynomial_identity_checks()
    binary=classification_checks()
    tau=positive_root()
    assert abs(tau**3+4*tau*tau+3*tau-1)<1e-14
    kappa=(1+poly_gap(tau))**0.25
    b=math.sqrt(tau)
    a=-b**3-2*b
    witness=(fourth_power_schatten(a,1,1,0)/fourth_power_schatten(a,1,1,b))**0.25
    assert abs(witness-kappa)<1e-12
    random_count=random_checks(kappa)
    print('VERIFY_OK exact_polynomial=%d triangle_patterns=%d random_complex=%d witness=1 kappa=%.13f tau=%.13f' % (exact,binary,random_count,kappa,tau))

if __name__=='__main__':
    main()
