"""Finite exact-arithmetic diagnostics for the centered Cantor-gap map.
The infinite theorem is proved analytically; these checks test identities and examples.
"""
from fractions import Fraction as F
from math import log, exp, log1p

def tail(j):
    return F(2,3)**j

def gap_bounds(k,r):
    a=F(1,3**k); b=F(1,r**k)
    return (a-b)/2, (a+b)/2

def target_mass_at_rational_epsilon(eps,r,max_k=140):
    # Exact mass if full inclusion/exclusion of every branch level is decidable
    p=F(0,1)
    for k in range(1,max_k+1):
        lo,hi=gap_bounds(k,r)
        if hi < eps: p += F(2**(k-1),3**k)
        elif lo >= eps: pass
        else: return None
    # Tail levels are automatically included whenever the high bound at max_k is below eps.
    assert gap_bounds(max_k,r)[1]<eps
    return p+tail(max_k)

def run():
    count=0
    for r in (4,5,7,11):
      for j in (12,17,24,30):
        # Choose three rational phases strictly inside (0,1), with epsilon= (c/2)3^-j.
        # c=1/2,2/3,5/6 are between 1/3 and 1.
        for c in (F(1,2),F(2,3),F(5,6)):
            eps=c*F(1,2*3**j)
            assert gap_bounds(j+1,r)[1]<eps<gap_bounds(j,r)[0]
            count+=2
            assert target_mass_at_rational_epsilon(eps,r)==tail(j)
            count+=1
        # Strict interior test on either side of the k=j midpoint, with margins exceeding branch radii
        rho=F(1,1)*(F(3,r)**j)
        ea=(1-2*rho)*F(1,2*3**j)
        eb=(1+2*rho)*F(1,2*3**j)
        assert ea>0
        assert target_mass_at_rational_epsilon(ea,r)==tail(j)
        assert target_mass_at_rational_epsilon(eb,r)==tail(j-1)
        count+=3
    # direct formula for ideal-model step function, with no irrational conversions in the exact arithmetic
    for j in range(4,35):
       for c in (F(1,2), F(2,3), F(5,6)):
          eps=c*F(1,2*3**j)
          # the ideal threshold k>=j+1 has geometric tail q^j
          assert tail(j)==sum((F(2**(k-1),3**k) for k in range(j+1,j+50)),F(0)) + tail(j+49)
          count+=1
    delta=log(1.5)/log(3)
    assert abs(3**(-delta)-2/3)<1e-14
    for f in (.2,.4,.8):
        R=2**delta*1.5**f
        for j in (25,60,100):
           eps=0.5*3**(-(j+f))
           ratio=(2/3)**j/eps**delta
           assert abs(ratio/R-1)<1e-12
           # exponential limit at the true geometric probability p, tested for rare levels
           p=(2/3)**j
           t=2.0
           assert abs(exp(int(t/(eps**delta))*log1p(-p)) - exp(-R*t)) < 2e-4
           count+=2
    print('PASS',count,'exact and floating finite diagnostics')
    print('delta',delta,'liminf',2**delta,'limsup',1.5*2**delta)
if __name__=='__main__': run()
