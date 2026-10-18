"""Exact rational and independent integral checks for the spacing-exceedance theorem.

Run: python3 verify.py
Uses the Python standard library. No external data or packages.
"""
from fractions import Fraction as F
from math import comb


def plus(x):
    return max(F(0), x)


def harmonic(m):
    return sum((F(1, j) for j in range(1, m + 1)), F(0))


def gap_survival(m, b):
    """P(max(Y)-Y_1 > b), by labeled-subset simplex volumes."""
    return sum(((-1)**(k+1) * comb(m-1, k) * plus(1-k*b)**(m-1) / (k+1)
                for k in range(1, m)), F(0))


def stoploss(m, b):
    """E[(b - (max(Y)-Y_1))_+] from the integrated gap survival."""
    return b - sum(((-1)**(k+1) * F(comb(m-1, k), m*k*(k+1))
                    * (1 - plus(1-k*b)**m) for k in range(1, m)), F(0))


def joint_cdf_integrated(m, t):
    """Independent inclusion-exclusion for E[M 1{Y_1>t}]."""
    mass = (1-t)**(m-1)
    integral = F(m-1, m)*(1-t)**m
    integral += sum(((-1)**k * F(comb(m-1,k), m*k*(k+1))
                     * plus(1-(k+1)*t)**m for k in range(1,m)),F(0))
    return mass-integral


def covariance_formula(m, t):
    b=t/(1-t)
    return m*(1-t)**m*(stoploss(m,b) - b*harmonic(m)/m)


def covariance_independent(m, t):
    return m*(joint_cdf_integrated(m,t) - (1-t)**(m-1)*harmonic(m)/m)


def check():
    checks=0
    for m in range(2, 13):
        assert gap_survival(m,F(0)) == F(m-1,m)
        checks+=1
        assert gap_survival(m,F(1)) == 0
        checks+=1
        for j in range(1,29):
            t=F(j,30)
            assert covariance_formula(m,t) == covariance_independent(m,t), (m,t)
            checks+=1
            if t >= F(1,2) and m>=3:
                assert covariance_formula(m,t)>0, (m,t)
                checks+=1
        # Given the same m, the stoploss ratio crosses H_m/m only once;
        # check sample rational points against its monotonicity.
        last = F(0)
        for j in range(1,51):
            b=F(j,50)
            ratio=stoploss(m,b)/b
            assert ratio>last, (m,b,last,ratio)
            last=ratio
            checks+=1
    # The m=2 threshold is b=1, or t=1/2.
    assert stoploss(2,F(1)) == harmonic(2)/2
    checks+=1
    assert covariance_formula(2,F(1,3)) < 0
    checks+=1
    assert covariance_formula(2,F(2,3)) > 0
    checks+=1
    # For m=3, b>1/2 root solves 18b^2-6b^3+1-11b=0.
    for b in [F(1,2), F(2,3), F(3,4), F(4,5)]:
        polynomial=18*b*b-6*b*b*b+1-11*b
        assert 18*(stoploss(3,b)-b*harmonic(3)/3) == polynomial
        checks+=1
    # Rational exact-covariance sign bracket for selected dimensions.
    brackets={3:(F(40,100),F(42,100)),4:(F(34,100),F(35,100)),
              5:(F(29,100),F(31,100)),8:(F(21,100),F(22,100)),
              10:(F(18,100),F(19,100))}
    for m,(low,high) in brackets.items():
        assert covariance_formula(m,low)<0
        assert covariance_formula(m,high)>0
        checks+=2
    # Independent grid enumeration of the simplex is only illustrative, not a proof.
    # Exact rational identities above cover a broad range of dimensions and thresholds.
    print(f"PASS: {checks} exact rational assertions")

if __name__ == '__main__':
    check()
