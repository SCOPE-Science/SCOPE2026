"""Reproducible checks for cumulants of two stationary fluctuating-interaction dimers.

Requires numpy, scipy, and sympy. Runs direct finite-grid conditional-variance
checks independently of the continuous-time ordered-cumulant integration.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

checks = 0

def assert_close(actual, expected, rtol=1e-5, atol=1e-10):
    global checks
    if not math.isclose(float(actual), float(expected), rel_tol=rtol, abs_tol=atol):
        raise AssertionError((actual, expected, rtol))
    checks += 1


def assert_true(expr):
    global checks
    assert bool(expr)
    checks += 1


def finite_cumulant(t, mu, nu, pvar, yvar, driver):
    """Exact ordered four-point kernel followed by numerical integration."""
    assert driver in ('gaussian', 'telegraph')
    def v_integral(u):
        maxv = t-u
        def integrand(v):
            if driver == 'gaussian':
                f = (math.exp(-2*nu*v)+math.exp(-2*mu*v)
                     +math.exp(-2*(mu+nu)*v))
            else:
                f = math.exp(-2*nu*v)-math.exp(-2*(mu+nu)*v)
            return (t-u-v)*f
        return quad(integrand, 0, maxv, epsabs=3e-12, epsrel=3e-12)[0]
    out = quad(lambda u: u*math.exp(-(mu+nu)*u)*v_integral(u),
               0, t, epsabs=2e-11, epsrel=2e-11)[0]
    return 3*pvar**2*yvar**2*out


def finite_cumulant_discretized(t, mu, nu, pvar, yvar, driver, n):
    """Independent conditional-Gaussian-variance calculation on a midpoint grid."""
    times=(np.arange(n)+0.5)*t/n
    ky=yvar*np.exp(-nu*np.abs(times[:,None]-times[None,:]))
    kp=pvar*np.exp(-mu*np.abs(times[:,None]-times[None,:]))
    if driver=='gaussian':
        return 3/8*(t/n)**4*np.trace((ky@kp)@(ky@kp))
    pair_i=np.repeat(np.arange(n),n)
    pair_j=np.tile(np.arange(n),n)
    ts=np.stack(np.broadcast_arrays(times[pair_i][:,None],times[pair_j][:,None],
                                    times[pair_i][None,:],times[pair_j][None,:]))
    ts.sort(axis=0)
    e4=pvar**2*np.exp(-mu*((ts[1]-ts[0])+(ts[3]-ts[2])))
    epair=pvar*np.exp(-mu*np.abs(times[pair_i]-times[pair_j]))
    cv=e4-epair[:,None]*epair[None,:]
    weights=ky[pair_i,pair_j]
    return 3/16*(t/n)**4*np.dot(weights,cv@weights)


def rate(mu,nu,pvar,yvar,driver):
    pref=1.5*pvar**2*yvar**2/(nu*(mu+nu)**3)
    return pref*((mu**2+3*mu*nu+nu**2)/mu if driver=='gaussian' else mu)


def ordered_cumulant(t,mu,nu,pvar,yvar,driver):
    """Full moment/cumulant pairings at four times (independent of gap formulas)."""
    a=np.array(t)
    assert len(a)==4
    p=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    def corr(i,j,r): return math.exp(-r*abs(a[i]-a[j]))
    def wick(r):return sum(math.prod(corr(*edge,r) for edge in pairing) for pairing in p)
    y4=yvar**2*wick(nu)
    if driver=='gaussian':
        ps4=pvar**2*wick(mu)
    else:
        ts=sorted(a)
        ps4=pvar**2*math.exp(-mu*(ts[1]-ts[0]+ts[3]-ts[2]))
    gaussian_reductions= sum(math.prod(pvar*yvar*corr(*edge,mu)*corr(*edge,nu)
                                     for edge in pairing) for pairing in p)
    return ps4*y4-gaussian_reductions


if __name__=='__main__':
    m,n=sp.symbols('m n', positive=True)
    # Count all label-orderings without using a fourth-cumulant shortcut.
    pairing_psi=((0,1),(2,3));pairing_y=((0,2),(1,3))
    integral=0
    for order in itertools.permutations(range(4)):
        coeff=[]
        for k in (1,2,3):
            seen=set(order[:k])
            crosses=lambda pair: sum((i in seen)!=(j in seen) for i,j in pair)
            coeff.append(m*crosses(pairing_psi)+n*crosses(pairing_y))
        integral+=1/sp.prod(coeff)
    assert_true(sp.simplify(integral-4*(m*m+3*m*n+n*n)/(m*n*(m+n)**3))==0)
    for mu,nu,pvar,yvar in [(1.3,.7,1.5,.8),(.6,2.4,4.,.5), (3.,1.9,.7,2.)]:
        t=1.65
        # Reconstruct four-variable cumulants at unrelated deterministic times.
        for gaps in [(0.11,.3,.5),(.4,.02,.8),(1.2,.7,.04)]:
            a,b,c=gaps
            ts=[0,a,a+b,a+b+c]
            A=math.exp(-(mu+nu)*(a+c))
            fg=2*pvar*pvar*yvar*yvar*A*(
                math.exp(-2*nu*b)+math.exp(-2*mu*b)+math.exp(-2*(mu+nu)*b))
            ft=2*pvar*pvar*yvar*yvar*A*(
                math.exp(-2*nu*b)-math.exp(-2*(mu+nu)*b))
            assert_close(ordered_cumulant(ts,mu,nu,pvar,yvar,'gaussian'),fg,rtol=1e-10)
            assert_close(ordered_cumulant(ts,mu,nu,pvar,yvar,'telegraph'),ft,rtol=1e-10)
            assert_true(fg>ft>0)
        cg=finite_cumulant(t,mu,nu,pvar,yvar,'gaussian')
        ct=finite_cumulant(t,mu,nu,pvar,yvar,'telegraph')
        assert_true(cg>ct>0)
        # Different operator-theoretic and Markov-chain Wick routes converge to
        # the same continuous-time value when the discrete grid is refined.
        for driver,exact in [('gaussian',cg),('telegraph',ct)]:
            c28=finite_cumulant_discretized(t,mu,nu,pvar,yvar,driver,28)
            c42=finite_cumulant_discretized(t,mu,nu,pvar,yvar,driver,42)
            assert_true(abs(c42-exact)<abs(c28-exact))
            assert_close(c42,exact,rtol=.014)
        rg=rate(mu,nu,pvar,yvar,'gaussian')
        rt=rate(mu,nu,pvar,yvar,'telegraph')
        assert_close(rg/rt,1+3*nu/mu+(nu/mu)**2)
        assert_true(rg>rt>0)
        # An independent gap-factorization yields the same asymptotic integral.
        a=mu+nu
        ig=3*pvar*pvar*yvar*yvar/a**2*(1/(2*nu)+1/(2*mu)+1/(2*a))
        it=3*pvar*pvar*yvar*yvar/a**2*(1/(2*nu)-1/(2*a))
        assert_close(ig,rg)
        assert_close(it,rt)
        # Full mean-square displacement agrees for both drivers.
        Dx=1.2
        var=Dx*t+pvar*yvar/(2*a*a)*(a*t+math.exp(-a*t)-1)
        var_direct=Dx*t+(pvar*yvar/2)*quad(lambda s:(t-s)*math.exp(-a*s),0,t)[0]
        assert_close(var,var_direct)
        entropy=pvar*yvar/(2*Dx)
        assert_true(entropy>0)
        print('rates mu,nu=',mu,nu,'OU,tele=',rg,rt,'ratio=',rg/rt,
              'finite κ4=',cg,ct, 'entropy=',entropy)
    print(f'PASS: {checks} independent analytic and discretized checks')
