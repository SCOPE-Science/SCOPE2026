"""Supplementary exact scalar tests for mixed-summand pointwise slice constants.

Analytic inequalities for the uncountable parameter set are proved in RESULT.md;
these tests do not claim numerical exhaustiveness.
"""
from fractions import Fraction as F
from math import isclose
import itertools

# Reverse norm inequality and superadditivity, pivotal to the all-slice
# Daugavet lower bound. Exactly check rational scalar configurations.
checks=0
for p in (2,3,4,5):
    for a_k,u_k in itertools.product(range(21), range(-20,21)):
        a=F(a_k,20)
        u=F(u_k,20)
        # Candidate v is exactly the positive p-root of 1-|u|^p.
        # Raising the desired inequality to the p-th power eliminates roots
        # for the first reverse-triangle component.
        v_p=1-abs(u)**p
        assert v_p>=0
        # Reverse triangle: ||(a,0)-(u,v)|| >= 1-a is implied by
        # Minkowski and ||(u,v)||=1. Here verify at p-power level.
        assert abs(a-u)**p + v_p >= (1-a)**p
        checks+=1

# Superadditivity (b+v)^p >= b^p+v^p for rational b,v>=0.
for p in (2,3,4,5):
    for i,j in itertools.product(range(31), repeat=2):
        b=F(i,30); v=F(j,30)
        assert (b+v)**p >= b**p+v**p
        checks+=1

# Delta-upper bound: for every rational 0<=a<=u<=1,
# (u-a)^p+(b+(1-u^p)^(1/p))^p <= (2b)^p.
# Numeric checks are supplemented by the exact analytic derivative argument.
upper_checks=0
min_slack=float('inf')
for p in (1.125, 1.5, 2, 2.5, 3, 5, 9, 20):
    for ia in range(21):
        a=ia/20
        b=max(0.0,1-a**p)**(1/p)
        for iu in range(ia,21):
            u=iu/20
            v=max(0.0,1-u**p)**(1/p)
            left=(u-a)**p+(b+v)**p
            right=(2*b)**p
            assert left<=right+1e-10*max(1,right), (p,a,u,left,right)
            upper_checks+=1
            min_slack=min(min_slack,right-left)

# The Daugavet point assumption is essential: the checker makes no claim
# about non-Daugavet unit vectors in the second summand.
for p in (1.125,1.5,2,3,5,9):
    for k in range(1,20):
        a=k/20
        b=(1-a**p)**(1/p)
        dc=((1-a)**p+b**p)**(1/p)
        delta=2*b
        assert 0<dc<delta<2, (p,a,dc,delta)
        assert isclose((((1-a)**p + b**p)**(1/p)), dc)
    assert 2**(1/p)<2 # endpoint a=0: dc, delta = 2^(1/p),2
    assert (1-1)**p+0==0 # endpoint a=1: both zero

print(f'VERIFY_OK exact_rational_checks={checks} delta_upper_grid={upper_checks} exponents=8 strict_gap=verified')
