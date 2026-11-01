"""Independent numerical checks for Gaussian surface measure of translated boxes.

Run: python3 verify.py. Uses only the Python 3 standard library.
Numerical tests corroborate, but do not replace, the analytic proof.
"""
import math
import random

SQRT2PI = math.sqrt(2.0 * math.pi)


def phi(x):
    return math.exp(-0.5 * x * x) / SQRT2PI


def Phi(x):
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def q(a, t=0.0):
    return Phi(t + a) - Phi(t - a)


def factors(halfwidths):
    C = math.prod(q(v) for v in halfwidths[1:])
    L = sum(2.0 * phi(v) / q(v) for v in halfwidths[1:])
    return C, L


def gauss_boundary(halfwidths, t):
    a = halfwidths[0]
    C, L = factors(halfwidths)
    return C * (phi(t-a) + phi(t+a) + L*q(a, t))


def gauss_boundary_derivative(halfwidths, t):
    a = halfwidths[0]
    C, L = factors(halfwidths)
    return 2*C*phi(a)*math.exp(-0.5*t*t)*((a-L)*math.sinh(a*t)-t*math.cosh(a*t))


def optimal_translation(halfwidths):
    a = halfwidths[0]
    _, L = factors(halfwidths)
    if a*(a-L) <= 1:
        return 0.0
    lo, hi = 0.0, a-L
    def f(t):
        if t == 0.0:
            return a*(a-L)-1.0
        z=a*t
        ratio=1.0-z*z/3.0+2.0*z**4/15.0 if abs(z)<1e-3 else math.tanh(z)/z
        return a*(a-L)*ratio-1.0
    assert f(lo) > 0 and f(hi) <= 1e-15
    if f(hi) == 0.0:
        return hi
    for _ in range(100):
        m = 0.5*(lo+hi)
        if f(m)>0:
            lo=m
        else:
            hi=m
    return 0.5*(lo+hi)


def simpson(func, u, v, N=96):
    h=(v-u)/N
    return h/3*(func(u)+func(v)+4*sum(func(u+(2*k+1)*h) for k in range(N//2))
                +2*sum(func(u+2*k*h) for k in range(1,N//2)))


def direct_facet_quadrature(halfwidths,t):
    """Numerically integrate the full density on every boundary face."""
    centers=[t]+[0.0]*(len(halfwidths)-1)
    area=0.0
    for j in range(len(halfwidths)):
        other=[k for k in range(len(halfwidths)) if k!=j]
        for sign in (-1,1):
            x_j=centers[j]+sign*halfwidths[j]
            density=phi(x_j)
            if len(other)==1:
                k=other[0]
                face=simpson(lambda x: density*phi(x),
                             centers[k]-halfwidths[k],centers[k]+halfwidths[k])
            else:
                k,l=other
                face=simpson(lambda x: simpson(lambda y: density*phi(x)*phi(y),
                                  centers[l]-halfwidths[l],centers[l]+halfwidths[l]),
                             centers[k]-halfwidths[k],centers[k]+halfwidths[k])
            area+=face
    return area


def near(x,y,tol=1e-8):
    assert abs(x-y) <= tol*max(1.0, abs(x),abs(y)), (x,y)


def main():
    tests=0
    samples=[(0.8,0.6),(1.1,6.0),(2.3,3.4,1.2),(1.0,1.0,1.0),(3.0,5.0,5.0)]
    for widths in samples:
        for t in (0.0,0.15,0.45,1.1,2.25):
            near(gauss_boundary(widths,t), direct_facet_quadrature(widths,t),2e-8)
            tests+=1
    rng=random.Random(8194)
    for _ in range(280):
        dim=rng.randint(2,9)
        widths=[rng.uniform(0.3,5.0) for _ in range(dim)]
        a=widths[0]
        C,L=factors(widths)
        crit=(L+math.sqrt(L*L+4.0))/2
        assert (a*(a-L)>1) == (a>crit)
        tests+=1
        tstar=optimal_translation(widths)
        if tstar==0:
            assert all(gauss_boundary(widths,t)<gauss_boundary(widths,0)
                       for t in (0.02,0.1,0.5,1.4,3.0))
            tests+=5
        else:
            assert 0<tstar<=a-L
            near(gauss_boundary_derivative(widths,tstar),0,1e-9)
            assert gauss_boundary(widths,tstar)>gauss_boundary(widths,0)
            for frac in (0.12,0.35,0.7):
                assert gauss_boundary_derivative(widths,tstar*frac)>0
                tests+=1
            for frac in (1.15,1.4,2.0):
                assert gauss_boundary_derivative(widths,tstar*frac)<0
                tests+=1
            tests+=2
        for t in (0.12,0.3,0.8):
            h=1e-5
            numeric=(gauss_boundary(widths,t+h)-gauss_boundary(widths,t-h))/(2*h)
            near(numeric,gauss_boundary_derivative(widths,t),1e-8)
            tests+=1
    # Critical quartic coefficient, sqrt-bifurcation, and quadratic peak gain.
    b=2.0
    L=2*phi(b)/q(b)
    ac=(L+math.sqrt(L*L+4))/2
    C=q(b)
    for t in (0.03,0.02,0.01):
        loss=gauss_boundary((ac,b),0)-gauss_boundary((ac,b),t)
        limit=C*phi(ac)*ac*ac/6
        assert abs(loss/t**4/limit-1)<2e-3
        tests+=1
    for epsilon in (0.015,0.005,0.002):
        a=ac+epsilon
        delta=a*(a-L)-1
        root=optimal_translation((a,b))
        peak=gauss_boundary((a,b),root)-gauss_boundary((a,b),0)
        assert abs(root/(math.sqrt(3*delta)/ac)-1)<0.013
        assert abs(peak/(1.5*C*phi(ac)*delta**2/ac**2)-1)<0.049
        tests+=2
    print('PASS: %d checks; Gaussian facets, derivative, global phases, and critical scaling.'%tests)

if __name__=='__main__':
    main()
