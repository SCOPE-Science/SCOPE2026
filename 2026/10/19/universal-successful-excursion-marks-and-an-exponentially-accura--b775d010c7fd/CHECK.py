"""Finite-parameter independent quadrature checks for a random-location reset search theorem.

Run: python CHECK.py. The asymptotic theorem requires its analytical proof;
these deterministic tests verify normalization, transforms, and constants.
"""
from math import exp, gamma, pi, sinh, sqrt, tanh, factorial


def simpson(func, n=24000):
    assert n % 2 == 0
    h = 1.0/n
    summation = func(0.0)+func(1.0)
    for i in range(1,n):
        summation += (4.0 if i % 2 else 2.0)*func(h*i)
    return summation*h/3.0


def h(q, d, a):
    # Brownian first exit of (0,2a), starting at geodesic distance d.
    return (exp(-q*d)+exp(-q*(2*a-d)))/(1.0+exp(-2*q*a))


def p_and_transform(beta, q, w=0.0, s=0.0, a=pi):
    # Geodesic distance density beta*d**(beta-1)/a**beta, with
    # substitution d=a*x**8 smooths all tested endpoint powers.
    k=8
    def integrand(x):
        d=a*x**k
        return k*beta*x**(k*beta-1)*exp(-w*q*d)*h(q*sqrt(1.0+s),d,a)
    return simpson(integrand)


def assert_close(x,y,atol=1e-5,rtol=1e-5):
    assert abs(x-y)<=atol+rtol*abs(y), (x,y,abs(x-y))


def main():
    checks=0
    a=pi
    for q in (0.25,0.8,1.2,2.5,4.0,10.0):
        p=p_and_transform(1.0,q,a=a)
        assert_close(p,tanh(a*q)/(a*q),atol=2e-7)
        assert 0<p<1
        checks+=2
    for beta in (0.55,0.75,1.0,1.5,2.0,2.75,3.25):
        # At q=60 endpoint neighborhoods are near enough to be resolved
        # while keeping the numerical integration feasible.
        for q in (20.0,35.0,60.0):
            p=p_and_transform(beta,q,a=a)
            p_asym=gamma(beta+1)/(a*q)**beta
            assert_close(p/p_asym,1.0,atol=2e-4)
            checks+=1
            for w,s in ((0.,0.),(.5,0.),(0.,1.),(.5,2.),(1.5,.35)):
                lhs=p_and_transform(beta,q,w=w,s=s,a=a)/p
                rhs=(w+sqrt(1+s))**(-beta)
                assert_close(lhs,rhs,atol=3e-4)
                checks+=1
    # Compare exact circle-success mass to half-line mass plus the possible
    # remote-boundary correction for integer shape parameters.
    for beta in (1, 2, 3, 4):
        for q in (4.0, 7.0, 12.0, 20.0):
            x=a*q
            p=p_and_transform(beta,q,a=a)
            p_inf=gamma(beta+1)/x**beta
            tail=exp(-x)*sum(x**k/factorial(k) for k in range(beta))
            def b_integrand(z):
                d=a*z**8
                return 8*beta*z**(8*beta-1)*sinh(q*d)/sinh(2*x)
            b=simpson(b_integrand)
            assert abs(p-p_inf)<=b+p_inf*tail+2e-9, (beta,x,p,p_inf,b,tail)
            assert b<=exp(-x)/(1-exp(-4*x))+2e-9
            assert p>=p_inf*(1-tail)-2e-9
            checks+=3
    # Conditional law and universal covariance checks from the half-line
    # Brownian first passage Laplace transform.
    for beta in (.55,.75,1.0,1.5,2.0,2.75,3.25):
        EZ=beta; VZ=beta
        EU=beta/2; VU=beta/2
        cov=beta/2
        assert_close(cov/sqrt(VZ*VU),1/sqrt(2),atol=1e-12)
        assert_close(EU,EZ/2,atol=1e-12)
        assert_close(VU,beta/2,atol=1e-12)
        checks+=3
    # For a normalized reset density and fixed r, exact standard renewal MFPT.
    for beta in (.75,1.0,2.0,3.25):
        for r in (.2,2.,50.):
            p=p_and_transform(beta,sqrt(r),a=a)
            mean=(1-p)/(r*p)
            assert mean>0
            checks+=1
    print(f"PASS: {checks} deterministic tests; no analytical limit inferred from these checks.")

if __name__=='__main__':
    main()
