"""Standalone checks for the sharp simplex surface/interior second-moment gap.

The analytic inequalities and limiting sharpness are proved in RESULT.md;
these checks verify finite exact identities and examples, not infinite quantifiers.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 70


def C(d):
    return F(-d*d + 3*d + 2, d*d*(d+1)*(d+2))


def analytic_two_cluster(d, t):
    """Exact moments and areas computed for the explicit two-cluster family."""
    T = Decimal(t)
    A = (1 + T**4).sqrt()
    B = (d-2+T**2).sqrt()
    weights = [A, Decimal(1), T*B] + [T]*(d-2)
    total = sum(weights)
    p = [x/total for x in weights]
    V = [[Decimal(0)]*d for _ in range(d+1)]
    V[1][1] = T**2
    for j in range(2,d+1):
        V[j][0] = 1
        if j >= 3:
            V[j][j-1] = T
    g = [sum(v[k] for v in V)/(d+1) for k in range(d)]
    S = sum(sum((v[k]-g[k])**2 for k in range(d)) for v in V)
    surf_mean = [sum(p[i]*V[i][k] for i in range(d+1)) for k in range(d)]
    m2 = sum(((surf_mean[k]-g[k])/d)**2 for k in range(d))
    I = 2*S/Decimal((d+1)*(d+2))
    Bnd = 2*(S/Decimal(d*(d+1))-m2)
    return (Bnd-I)/S, p, S, I, Bnd


def rational_witness_d4():
    t=F(1,100)
    # The two large facets have rescaled areas sqrt(1+t^4)>=1, 1;
    # the other facets have rescaled areas t*(sqrt(2+t^2)+2)<=4t.
    assert F(2)+t*t < F(4)
    p_right_upper=2*t
    assert p_right_upper < F(3,5)
    # All boundary mean vector components are centered. Its first component is
    # (p_right - 3/5)/4, so square of its norm exceeds this exact bound.
    m2_lower=((F(3,5)-p_right_upper)/4)**2
    S=F(6,5)+F(8,5)*t*t+F(4,5)*t**4
    gap_upper=S/F(30)-2*m2_lower
    assert gap_upper < 0
    return gap_upper


def check():
    assert C(2)==F(1,12)
    assert C(3)==F(1,90)
    assert C(4)==-F(1,240)
    for d in range(2,15):
        assert (C(d)>0)==(d<=3)
        # The face areas from the explicit simplex are proportional to
        # sqrt(1+t^4), 1, t*sqrt(d-2+t^2), and d-2 copies of t.
        for exponent in (2,3,4,5):
            ratio,p,S,I,Bnd=analytic_two_cluster(d,Decimal(10)**(-exponent))
            assert abs(sum(p)-1)<Decimal('1e-60')
            assert ratio > Decimal(C(d).numerator)/Decimal(C(d).denominator)-Decimal('1e-56')
            if exponent==5:
                target=Decimal(C(d).numerator)/Decimal(C(d).denominator)
                assert abs(ratio-target)<Decimal('0.0001'),(d,ratio,target)
            assert S>0 and I>0 and Bnd>0
    bound=rational_witness_d4()
    ratio,p,S,I,Bnd=analytic_two_cluster(4,Decimal('0.01'))
    assert Bnd<I and (Bnd-I)<Decimal(bound.numerator)/Decimal(bound.denominator)
    print('PASS: 52 dimension/scale cases, sharp constants, limiting approach, and an exact-rational four-dimensional negative-gap certificate')
    print('dimension-four certified gap upper bound:',bound,'=',float(bound))
    print('dimension-four explicit witness: boundary squared distance',Bnd)
    print('dimension-four explicit witness: interior squared distance',I)
    print('dimension-four explicit witness: observed gap',Bnd-I)


if __name__=='__main__':
    check()
