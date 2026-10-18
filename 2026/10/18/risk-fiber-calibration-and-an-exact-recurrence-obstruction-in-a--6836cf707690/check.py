"""Exact arithmetic consistency checks for the ecological feedback moment theorem.

Checks are finite algebraic tests; the analytic invariant-measure proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb


def f(p, q, x):
    return comb(p + q, p) * x**p * (1-x)**q


def envelope(p, q, x):
    d = p + q - 1
    a = Q(p - 1, d)
    b = Q(p, d)
    if p > 1 and x < a:
        return (x/a)*f(p, q, a)
    if q > 1 and x > b:
        return ((1-x)/(1-b))*f(p, q, b)
    return f(p, q, x)


def curvature_polynomial(p, q, x):
    n = p + q
    return n*(n-1)*x*x - 2*p*(n-1)*x + p*(p-1)


def check_envelopes():
    cases = 0
    for p in range(1, 15):
        for q in range(1, 15):
            d = p+q-1
            a,b = Q(p-1,d),Q(p,d)
            assert a <= b
            assert curvature_polynomial(p,q,a) <= 0
            assert curvature_polynomial(p,q,b) <= 0
            for j in range(61):
                x=Q(j,60)
                assert envelope(p,q,x) >= f(p,q,x)
                if 0<j<60:
                    before=envelope(p,q,Q(j-1,60))
                    after=envelope(p,q,Q(j+1,60))
                    assert 2*envelope(p,q,x) >= before+after
                cases += 1
    return cases


def check_logarithmic_identities():
    checks=0
    for i in range(1,9):
        x,r=Q(i,12),Q(9-i,12)
        cost=Q(1,10)+Q(i,35)
        beta,alpha=Q(2,25),Q(1,2)
        B=Q(1)
        m1,m2=Q(1),Q(9)
        t1,t2,t3,t4=Q(1),Q(1),Q(1),Q(8)
        F=f(2,2,x)
        xd=x*(1-x)*(B*F*r-cost)
        rd=r*(1-r)*(m1-(m1+m2)*x)
        cd=(alpha-cost)*(cost-beta)*(t1-(t1+t2)*x-t4+(t3+t4)*r)
        assert xd/(x*(1-x)) == B*F*r-cost
        assert rd/(r*(1-r)) == (m1+m2)*(Q(1,10)-x)
        assert rd/(1-r) == (m1+m2)*r*(Q(1,10)-x)
        assert (alpha-beta)*cd/((cost-beta)*(alpha-cost)) == (alpha-beta)*(t1-t4-(t1+t2)*x+(t3+t4)*r)
        checks+=4
    return checks


def check_example():
    chi,eta=Q(1,10),Q(4,5)
    beta,alpha,B=Q(2,25),Q(1,2),Q(1)
    assert eta == ((Q(1)+Q(1))*chi-Q(1)+Q(8))/(Q(1)+Q(8))
    h=envelope(2,2,chi)
    assert h == Q(4,45)
    assert B*eta*h == Q(16,225)
    assert beta == Q(18,225)>B*eta*h
    assert f(2,2,Q(1,2)) == Q(3,8)
    assert eta*f(2,2,Q(1,2))==Q(3,10)
    # Unrestricted two-mean coupling: masses 3/10, 1/2, 1/5.
    atoms=[(Q(1,3),Q(1),Q(3,10)),(Q(0),Q(1),Q(1,2)),(Q(0),Q(0),Q(1,5))]
    assert sum(w for x,r,w in atoms)==1
    assert sum(w*x for x,r,w in atoms)==chi
    assert sum(w*r for x,r,w in atoms)==eta
    assert sum(w*r*f(2,2,x) for x,r,w in atoms)==Q(4,45)
    assert sum(w*r*x for x,r,w in atoms)==Q(1,10)!=chi*eta
    # Fiber-calibrated abstract optimizer: risk constant eta;
    # x=1/3 with probability 3/10 and x=0 otherwise.
    assert Q(3,10)*Q(1,3)==chi
    assert eta*Q(3,10)*f(2,2,Q(1,3))==eta*h
    return 12


if __name__ == '__main__':
    n=check_envelopes()+check_logarithmic_identities()+check_example()
    print(f'VERIFY_OK {n} exact arithmetic comparisons')
