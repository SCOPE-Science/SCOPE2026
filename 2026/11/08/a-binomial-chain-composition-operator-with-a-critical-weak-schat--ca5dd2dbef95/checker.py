"""Independent finite arithmetic checks of the binomial-chain monomial composition model.
This finite code corroborates, but does not replace, the analytic arguments.
"""
from fractions import Fraction
from math import factorial, comb

def r(j,k): return Fraction(k+1,j+k+1)
def d(j,k):
    prev=Fraction(k,j+k) if k else Fraction(0)
    return r(j,k)**2-prev**2

def count(Q):
    n=0
    # d(j,k)<=2/(j+k), so j+k>=2Q cannot contribute
    for j in range(1,2*Q,2):
        for k in range(max(0,2*Q-j)):
            lhs=Q*j*(j*(2*k+1)+2*k*(k+1))
            rhs=(j+k)**2*(j+k+1)**2
            n+=(lhs>rhs)
    return n

checks=0
for j in range(1,35,2):
    for k in range(0,45):
        x=d(j,k)
        assert x>0
        assert x==Fraction(j*(j*(2*k+1)+2*k*(k+1)),(j+k)**2*(j+k+1)**2)
        assert x <= Fraction(2,j+k)
        assert r(j,k) > (Fraction(k,j+k) if k else 0)
        m=Fraction(factorial(k)*factorial(j),factorial(j+k))**2
        mp=Fraction(factorial(k+1)*factorial(j),factorial(j+k+1))**2
        assert mp/m==r(j,k)**2
        checks+=5
for Q in (100,200,500,1000):
    n=count(Q)
    scaled=Fraction(n,Q*Q)
    assert abs(float(scaled)-1/30)<.0015
    print('Q',Q,'N(1/Q)',n,'scaled',float(scaled))
    checks+=1
print('DYADIC_BINOMIAL_CHECK_OK',checks,'exact assertions')
