"""Numerical supplement for sharp affine Bargmann--Fock vacuum stability.

Requirements: Python 3, scipy. Analytic proof is in RESULT.md; checks are
finite samples and do not certify statements for arbitrary parameters.
"""
from math import pi, sqrt, isfinite
from scipy.special import i0e, i1e

c = sqrt(pi) / 2
radii = [0., .001, .03, .3, 1., 3., 10., 30.]
tested = 0
for a in radii:
    for s in radii:
        if s == 0:
            m = a
        else:
            t = a*a / (2*s*s)
            m = (s*sqrt(pi)/2) * ((1+2*t)*i0e(t)+2*t*i1e(t))
        assert isfinite(m), (a, s, m)
        r = sqrt(a*a+s*s)
        upper1 = sqrt(a*a + c*c*s*s)
        upper2 = c*r+(1-c)*a
        eps = 5e-11 * max(1, r)
        assert m <= upper1+eps, (a,s,m,upper1)
        assert upper1 <= upper2+eps, (a,s,upper1,upper2)
        ph_dist2 = r*r + 1-2*a
        modulus_dist2 = r*r + 1-2*m
        bound = (1-c)*ph_dist2 + c*(r-1)**2
        assert modulus_dist2 >= bound-eps, (a,s,modulus_dist2,bound)
        if a == 0 or s == 0:
            assert abs(modulus_dist2-bound)<eps, (a,s,modulus_dist2,bound)
        elif 0.03 <= a/r <= 0.99:
            assert modulus_dist2 > bound+1e-13*max(1,r), (a,s,modulus_dist2,bound)
        tested += 1

# Direct first-Hermite extremizer, F(z)=z_1, normalized in any dimension.
first_order_modulus2 = 2-2*c
first_order_phase2 = 2
C = sqrt(first_order_phase2/first_order_modulus2)
assert abs(C-1/sqrt(1-c))<1e-13
print('PASS: grid points:', tested)
print('sharp coefficient c =', format(c,'.16f'))
print('sharp Lipschitz C =', format(C,'.16f'))
print('equality: a=0 or s=0 on tested grid')
