"""Reproducible standard-library diagnostic checks for the kinetic blow-up clock.

The exhaustive statements are proved analytically in RESULT.md.  This script
only checks algebraic identities and representative finite numerical quadratures.
"""
from fractions import Fraction as Q
from math import exp, gamma, isclose, lgamma, pi


def small_beta(nu, phi, delta):
    """Power series for integral_0^delta t^(nu-1)(1-t)^(phi-1) dt."""
    coef = 1.0
    power = delta**nu
    ans = power / nu
    for j in range(1, 200):
        coef *= (j - phi) / j
        power *= delta
        term = coef * power / (nu + j)
        ans += term
        if abs(term) < 1e-17 * max(1., abs(ans)):
            return ans
    raise RuntimeError("series did not converge")


def incomplete_beta(phi, nu, z):
    return exp(lgamma(phi) + lgamma(nu) - lgamma(phi + nu)) - small_beta(nu, phi, 1-z)


def simpson_beta(phi, nu, z, n=20000):
    # Substitute t=z*u^(1/phi), removing the integrable singularity at zero.
    def f(u):
        return (1.0-z*u**(1.0/phi))**(nu-1.0)
    h = 1./n
    total = f(0.)+f(1.)
    for i in range(1,n):
        total += (4 if i%2 else 2)*f(i*h)
    return z**phi/phi * h*total/3.


cases=[(1,2,1),(1,10,100),(2,3,4),(1,20,80),(9,10,1)]
checks=0
for aa,bb,cc in cases:
    a,b,c=Q(aa),Q(bb),Q(cc)
    d=b-a; k=b+c; star=d/k; P=a/d
    nu=P+b/k; phi=c/k; gam=a+b*star
    assert k*nu*star==gam; checks+=1
    for scale in [Q(1,2),Q(2),Q(5)]:
        w=star*scale
        if w==star: continue
        derivative=P/w-nu/(w-star)
        assert derivative==-(a+b*w)/(k*w*(w-star)); checks+=1
        assert 1+w*derivative==(c*w-b)/(k*(w-star)); checks+=1
    ph=float(phi); nn=float(nu); x0=2.
    z=.5
    IB=incomplete_beta(ph,nn,z)
    direct=simpson_beta(ph,nn,z)
    assert abs(IB-direct)<max(2e-7*abs(IB),2e-10), (aa,bb,cc,IB,direct)
    checks+=1
    # The finite-part difference is computed stably as a beta tail.
    for diff in [.001,.0001]:
        w0=float(star)+diff
        z=float(star)/w0
        h=x0*diff**nn/w0**float(P)
        tail=small_beta(nn,ph,1-z)
        finite_part=-float(star)**(-ph)*tail/(float(k)*h)
        target=-1/(float(gam)*x0)
        assert abs((finite_part-target)*x0)<max(3*diff,1e-6), (aa,bb,cc,diff,finite_part,target)
        checks+=1
# The original source's equal-rate example has exponent 5/3, gamma=5/3.
a,b,c=Q(1),Q(2),Q(1)
star=Q(1,3); nu=Q(5,3); phi=Q(1,3)
assert Q(4,1)*Q(5,3)==Q(20,3)
A=float(star)**(float(nu)-1)*gamma(float(phi))*gamma(float(nu))/gamma(float(phi+nu))/3
A_explicit=4*pi/(3**(8/3)*3**.5)
assert isclose(A,A_explicit,rel_tol=1e-13)
checks+=1
print('VERIFIED',checks,'finite rational/analytic/numerical diagnostics')
