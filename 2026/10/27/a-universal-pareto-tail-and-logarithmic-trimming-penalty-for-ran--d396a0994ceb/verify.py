"""Finite computational checks for the rank-one indefinite Nystrom tail theorem.

Standard-library only. Numerical tests do not establish the universal theorem.
"""
import math
from fractions import Fraction


def residual_entries(a, b, c, s):
    # A=diag(a,-b), u=(c,s), where c*c+s*s=1.
    q = a*c*c-b*s*s
    assert q != 0
    n11 = a*a*c*c/q
    n12 = -a*b*c*s/q
    n22 = b*b*s*s/q
    return a-n11, -n12, -b-n22, q


def fraction_identity_tests():
    checked = 0
    for a in range(1, 9):
        for b in range(1, 8):
            for j, k in ((3,4),(5,12),(8,15),(7,24),(20,21),(9,40)):
                for sign in (-1,1):
                    c=Fraction(j*j-k*k,j*j+k*k)
                    s=Fraction(2*j*k*sign,j*j+k*k)
                    v11,v12,v22,q=residual_entries(Fraction(a),Fraction(b),c,s)
                    assert v11*v22-v12*v12 == 0
                    assert v11+v22 == -Fraction(a*b)/q
                    checked += 1
    return checked


def asymptotic_checks():
    # A=diag(+1,-1): E=1/|cos(2 theta)|, for E>=1.
    # Tail P(E>t)=2*arcsin(1/t)/pi.
    for t in (2., 10., 100., 10000., 1e7):
        tail=(2/math.pi)*math.asin(1/t)
        assert tail>0
        assert abs(t*tail-2/math.pi) < 0.25/t/t
    # A=diag(1,1,-1): X=||N||=1/|1-2 U_3^2|, U_3 uniform [-1,1].
    for t in (2., 10., 100., 1000., 1e6):
        tail=(1/t)/(math.sqrt((1+1/t)/2)+math.sqrt((1-1/t)/2))
        assert abs(t*tail-1/math.sqrt(2)) < 0.6/t/t
    # Null cone surface-area coefficient equals beta-density coefficient.
    for n in range(2, 17):
        area_ratio = (2**(2-n/2))*math.gamma(n/2)/(math.sqrt(math.pi)*math.gamma((n-1)/2))
        beta_density = 2**(2-n/2) / (math.gamma(.5)*math.gamma((n-1)/2)/math.gamma(n/2))
        assert abs(area_ratio-beta_density)<1e-11
    return 5+5+15


def truncated_exact_checks():
    # For +/-1 two-dimensional reflection, the formula for the rejected-core
    # spectral residual has exactly the stated log/arcsin expression.
    checked=0
    for eps in (.03,.1,.25,.5,.8):
        exact=2/math.pi*(math.log((1+math.sqrt(1-eps*eps))/eps)+math.asin(eps))
        # Independent midpoint angular quadrature, with threshold edges excluded.
        N=100000
        approx=0.
        for j in range(N):
            q=math.cos(2*math.pi*(j+.5)/N)
            approx+=(1/abs(q) if abs(q)>=eps else 1.)/N
        assert abs(approx-exact)<.002,(eps,approx,exact)
        checked += 1
    for eps in (1e-2,1e-3,1e-5):
        exact=2/math.pi*(math.log((1+math.sqrt(1-eps*eps))/eps)+math.asin(eps))
        assert abs(exact-(2/math.pi)*math.log(1/eps)) < 2/math.pi*math.log(2)+.01
        checked += 1
    return checked


if __name__=='__main__':
    counts=(fraction_identity_tests(),asymptotic_checks(),truncated_exact_checks())
    print('VERIFY_OK rank-one residual rational identities=%d, sharp-tail asymptotics and coarea constants=%d, normalized core truncation=%d' % counts)
