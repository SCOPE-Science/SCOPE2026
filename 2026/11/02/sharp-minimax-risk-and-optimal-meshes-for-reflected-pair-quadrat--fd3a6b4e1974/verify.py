"""Exact-rational checks for convex-Lipschitz antithetic stratified quadrature.

Only Python standard library is required. All assertions are deterministic and exact.
"""
from fractions import Fraction as F
from random import Random


def rtheta(x):
    return min(x, 1-x)


def kernel(x, y):
    """Covariance of reflected local hinge pairs (no spatial scaling)."""
    a,b=sorted([rtheta(x),rtheta(y)])
    return a*a*b*(1-b)-a*a*a/3


def direct_covariance(theta_coefficients):
    """Integrate directly the piecewise-affine sum of local hinge pairs."""
    breaks={F(0),F(1)}
    for t, _ in theta_coefficients:
        breaks.add(t)
        breaks.add(1-t)
    xs=sorted(breaks)
    def value(u):
        return sum((c*(max(F(0),u-t)+max(F(0),1-u-t)) for t,c in theta_coefficients),F(0))
    e1=e2=F(0)
    for lo,hi in zip(xs, xs[1:]):
        vl,vh=value(lo),value(hi)
        dx=hi-lo
        e1+=dx*(vl+vh)/2
        e2+=dx*(vl*vl+vl*vh+vh*vh)/3
    return e2-e1*e1


def analytical_covariance(theta_coefficients):
    return sum((ci*cj*kernel(ti,tj) for ti,ci in theta_coefficients for tj,cj in theta_coefficients),F(0))


def test():
    count=0
    for m in range(0,51):
        t=F(m,100)
        expect=F(2,3)*t**3-t**4
        assert kernel(t,t)==expect
        assert kernel(t,t)<=F(1,48)
        count+=2
    # Direct moment integration against the closed covariance kernel.
    rng=Random(51403)
    for _ in range(1400):
        kk=rng.randrange(0,7)
        terms=[(F(rng.randrange(0,41),40),F(rng.randrange(0,11),10)) for j in range(kk)]
        exact=direct_covariance(terms)
        formula=analytical_covariance(terms)
        assert exact==formula, (terms,exact,formula)
        assert F(0)<=formula<=sum((c for _,c in terms),F(0))**2/F(48)
        count+=2
    # Arbitrary rational cell widths and independently localized curvature masses.
    for _ in range(600):
        n=rng.randrange(1,8)
        weights=[rng.randrange(1,10) for _ in range(n)]
        denom=sum(weights)
        hs=[F(w,denom) for w in weights]
        masses=[]
        full=F(0)
        for h in hs:
            terms=[(F(rng.randrange(0,21),20),F(rng.randrange(0,11),10)) for _ in range(rng.randrange(0,5))]
            masses.append(terms)
            full+=sum((c for _,c in terms),F(0))
        variance=sum((h**4*analytical_covariance(terms)/4 for h,terms in zip(hs,masses)),F(0))
        Lip=full/2
        assert variance <= Lip**2*max(hs)**4/48
        count+=1
    # Equality for one maximal cell and V-shaped 1-Lipschitz integrand.
    for n in range(1,21):
        hs=[F(1,n)]*n
        variance=hs[0]**4*analytical_covariance([(F(1,2),F(2))])/4
        assert variance == F(1,48*n**4)
        assert direct_covariance([(F(1,2),F(2))])==F(1,12)
        count+=2
    # Independent two-query measurement noise adds exactly v^2/2 * sum(h_i^2).
    for n in range(1,21):
        hs=[F(1,n)]*n
        noise=F(3,2)
        exact=noise*noise*sum((h*h for h in hs),F(0))/2
        assert exact==F(9,8*n)
        count+=1
    print('VERIFY_OK',count,'exact rational assertions')


if __name__=='__main__':
    test()
