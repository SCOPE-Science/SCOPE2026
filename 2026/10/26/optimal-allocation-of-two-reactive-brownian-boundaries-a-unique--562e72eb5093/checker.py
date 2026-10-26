"""Independent reproducibility checks for a two-reactive-endpoint Brownian interval.

No external dependencies; run with: python checker.py
"""
from math import sqrt
from random import Random


def mean_formula(y, s, t):
    assert 0 <= y <= 1 and s > 0 and 0 <= t <= s
    return -y*y/2 + (1+(s-t)/2)*(1+t*y)/(s+t*(s-t))


def derivative_numerator(y, s, t):
    return (y-.5)*t*t+(s*(1-y)+2)*t+s*((s+2)*y-(s+3))/2


def optimal(y, s):
    a, b = 0., s
    for _ in range(80):
        m = (a+b)/2
        if derivative_numerator(y, s, m) < 0:
            a = m
        else:
            b = m
    return (a+b)/2


def independent_fd_bvp(y, s, t, n=128):
    """Thomas solver for -u''=1, center-derivative Robin boundaries.

    Ghost elimination gives a tridiagonal system.  For quadratic solutions
    both the interior and boundary stencils are exact, not approximate.
    """
    h = 1./n
    lo, hi = t, s-t
    below = [-1.]*(n+1)
    diag = [2.]*(n+1)
    above = [-1.]*(n+1)
    rhs = [h*h]*(n+1)
    diag[0] = 2+2*h*lo
    above[0] = -2.
    below[n] = -2.
    diag[n] = 2+2*h*hi
    below[0] = 0.
    above[n] = 0.
    for i in range(1,n+1):
        q = below[i]/diag[i-1]
        diag[i] -= q*above[i-1]
        rhs[i] -= q*rhs[i-1]
    u = [0.]*(n+1)
    u[n] = rhs[n]/diag[n]
    for i in range(n-1,-1,-1):
        u[i] = (rhs[i]-above[i]*u[i+1])/diag[i]
    j=int(y*n)
    dy=y*n-j
    if j==n:
        return u[n]
    # Exact quadratic interpolation between adjacent grid points requires
    # the known curvature -1; interpolating the quadratic, not the grid line.
    return (1-dy)*u[j]+dy*u[j+1]+h*h*dy*(1-dy)/2


def golden_min(y,s):
    # Optimization uses function evaluations only; not its derivative.
    a,b=0.,s
    gr=(sqrt(5)-1)/2
    c=b-gr*(b-a)
    d=a+gr*(b-a)
    fc=mean_formula(y,s,c)
    fd=mean_formula(y,s,d)
    for _ in range(110):
        if fc<fd:
            b,d,fd=d,c,fc
            c=b-gr*(b-a)
            fc=mean_formula(y,s,c)
        else:
            a,c,fc=c,d,fd
            d=a+gr*(b-a)
            fd=mean_formula(y,s,d)
    return (a+b)/2


def run():
    rng=Random(910751)
    max_bvp=0.
    max_opt_obj=0.
    for k in range(50):
        s=10**rng.uniform(-1.2,1.5)
        y=rng.uniform(0,1)
        t=s*rng.uniform(.01,.99)
        expected=mean_formula(y,s,t)
        measured=independent_fd_bvp(y,s,t)
        err=abs(expected-measured)
        max_bvp=max(max_bvp,err)
        assert err<3e-10, ('BVP',k,s,y,t,err)
        tstar=optimal(y,s)
        assert 0<tstar<s
        assert abs(derivative_numerator(y,s,tstar))<1e-9*(1+s*s)
        alt=golden_min(y,s)
        loss=mean_formula(y,s,tstar)-mean_formula(y,s,alt)
        max_opt_obj=max(max_opt_obj,abs(loss))
        assert loss<3e-11,('minimum',k,s,y,loss)
        assert mean_formula(y,s,tstar)<min(mean_formula(y,s,0),mean_formula(y,s,s))
    for y in (0.,.05,.25,.5,.7,.95,1.):
        ss=(1e-6,1e-4,.01,1.,1e2,1e5)
        pp=[optimal(y,s)/s for s in ss]
        pweak=.75-.5*y
        assert abs(pp[0]-pweak)<2e-5,(y,pp[0],pweak)
        if y<.5:
            assert all(pp[i]<=pp[i+1]+1e-9 for i in range(len(pp)-1)),(y,pp)
        if y>.5:
            assert all(pp[i]>=pp[i+1]-1e-9 for i in range(len(pp)-1)),(y,pp)
        if 0<y<1:
            pstrong=sqrt(1-y)/(sqrt(1-y)+sqrt(y))
            assert abs(pp[-1]-pstrong)<2e-3,(y,pp[-1],pstrong)
        if y==.5:
            assert all(abs(v-.5)<1e-8 for v in pp)
    print('PASS: 50 exact-form vs independent Robin finite-difference BVP checks')
    print('PASS: 50 function-only minimizations vs derivative-root optimizers')
    print('PASS: seven weak/strong budget asymptotic and monotonicity tests')
    print('maximum BVP discrepancy:',max_bvp)
    print('maximum optimized objective discrepancy:',max_opt_obj)

if __name__=='__main__':
    run()
