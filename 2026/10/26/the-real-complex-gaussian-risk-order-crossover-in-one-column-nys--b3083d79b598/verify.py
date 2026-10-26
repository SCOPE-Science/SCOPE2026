"""Reproducible numerical diagnostics for a two-dimensional Nyström residual law.
Analytical universal statements are proved in RESULT.md, not by these tests.
Python 3 standard library only.
"""
import math
import random


def formulas(a, b):
    assert a > b > 0
    return (math.sqrt(a*b),a*b*math.log(a/b)/(a-b),
            (a+b)*math.sqrt(a*b)/2,a*b,2*a*b/(a+b))


def quantiles(a,b,p):
    assert a > b > 0 and 0 <= p <= 1
    return (a*b/(b+(a-b)*math.cos(math.pi*p/2)**2),
            a*b/(a-(a-b)*p))


def integrate(f, n=100000):
    h=1/n
    return h*(.5*(f(0)+f(1))+sum(f(j*h) for j in range(1,n)))


def test_integrals():
    for a,b in [(9.,1.),(16.,.25),(1.1,1.),(4.,2.)]:
        er,ec,er2,ec2,m=formulas(a,b)
        r=lambda t:a*b/(a*math.cos(math.pi*t/2)**2+b*math.sin(math.pi*t/2)**2)
        c=lambda t:a*b/(b+(a-b)*t)
        assert abs(integrate(r)-er) < 1e-7 * max(1,er)
        assert abs(integrate(c)-ec) < 1e-7 * max(1,ec)
        assert abs(integrate(lambda t:r(t)**2)-er2) < 1e-6 * max(1,er2)
        assert abs(integrate(lambda t:c(t)**2)-ec2) < 1e-6 * max(1,ec2)
        assert abs(quantiles(a,b,.5)[0]-m) < 1e-12
        assert abs(quantiles(a,b,.5)[1]-m) < 1e-12
        for p in [.02,.10,.30,.70,.90,.98]:
            x,y=quantiles(a,b,p)
            assert (x<y) if p<.5 else (x>y)
        assert er>ec


def direct_matrix_residual(a,b,theta,z1,z2):
    # Orthogonal eigenvector rotation, with complex probe coordinates.
    ct,st=math.cos(theta),math.sin(theta)
    # Eigen-coordinates of probe, hence invariant trace residual.
    u=ct*z1+st*z2
    v=-st*z1+ct*z2
    den=a*abs(u)**2+b*abs(v)**2
    tr=a+b-(a*a*abs(u)**2+b*b*abs(v)**2)/den
    return tr,a*b*(abs(u)**2+abs(v)**2)/den


def test_matrix_identity():
    rng=random.Random(10220)
    for _ in range(2000):
        a,b=9.,1.
        z1=complex(rng.gauss(0,1),rng.gauss(0,1))
        z2=complex(rng.gauss(0,1),rng.gauss(0,1))
        t=rng.uniform(-math.pi,math.pi)
        x,y=direct_matrix_residual(a,b,t,z1,z2)
        assert abs(x-y)<1e-11


def test_convex_risk():
    a,b=25.,1.
    q_r=lambda p:quantiles(a,b,p)[0]
    q_c=lambda p:quantiles(a,b,p)[1]
    # Smooth convex increasing utilities: powers and stop-loss functions.
    for f in [lambda z:z,lambda z:z*z,lambda z:z**3,
              lambda z:max(z-2,0),lambda z:max(z-7,0),
              lambda z:max(z-14,0)]:
        assert integrate(lambda p:f(q_r(p))) >= integrate(lambda p:f(q_c(p)))-1e-6


if __name__=='__main__':
    test_integrals()
    test_matrix_identity()
    test_convex_risk()
    print('VERIFY_OK: 4 quadrature pairs, 2000 matrix trace identities, convex-risk tests')
