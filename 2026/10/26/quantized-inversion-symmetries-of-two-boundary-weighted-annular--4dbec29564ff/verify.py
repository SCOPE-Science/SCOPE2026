#!/usr/bin/env python3
"""Exact rational checks of annular weighted-composition identities at p=2."""
from fractions import Fraction as Q

def norm(coeff, r, wo, wi):
    return sum((abs(a)**2)*(wo+wi*r**(2*n)) for n,a in coeff.items())

def reciprocal(coeff, r, k, c2):
    # For theta=0 and |c|^2=c2; indices n -> k-n.
    return {k-n:a*r**n for n,a in coeff.items()}

def check(r,k):
    wo=Q(1);wi=r**(-k);c2=r**(-k)
    testsets=[{-4:Q(2),-1:Q(-3),0:Q(1),2:Q(5)},
              {-3:Q(3),1:Q(1),5:Q(-2)},
              {0:Q(1)}, {-6:Q(2),6:Q(3)}]
    for coeff in testsets:
        # T(z^n) = c*r^n*z^(k-n), so squared coefficient is c2*r^(2n)
        transformed=reciprocal(coeff,r,k,c2)
        lhs=norm(coeff,r,wo,wi)
        rhs=c2*norm(transformed,r,wo,wi)
        assert lhs==rhs,(r,k,coeff,lhs,rhs)
    return len(testsets)

count=sum(check(r,k) for r in (Q(1,2),Q(2,3),Q(3,5)) for k in (-3,1,4))
# Off-lattice example: r=1/2, wi/wo=3. Two necessary monomial equations fail for each candidate k.
r=Q(1,2);wo=Q(1);wi=Q(3)
for k in range(-12,13):
    assert not (wi/wo==r**(-k))
print('VERIFY_OK exact_laurent_cases=%d off_lattice_winding_candidates=25'%count)
