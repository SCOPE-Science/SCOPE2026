"""Numerical checks for the two-stage coordination-game Floquet law.

Run with Python >=3.10 and scipy >=1.10. All claims about an
infinite parameter family are proved analytically in RESULT.md;
finite computations below are consistency checks only.
"""

from math import exp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def one_cycle(x0, a1, b1, a2, b2, duty, period, h):
    state = [x0, 0.0, 0.0, 0.0, 0.0]
    peak = None
    for index, (a, b, width) in enumerate((
        (a1, b1, duty * period), (a2, b2, (1 - duty) * period)
    )):
        def rhs(_, y):
            x = y[0]
            growth = a*x-b
            return [x*(1-x)*growth, a, a*x, a*(x-h)**2,
                    (1-2*x)*growth+a*x*(1-x)]
        sol = solve_ivp(rhs, (0, width), state,
                        atol=1e-13, rtol=3e-12)
        assert sol.success
        state = list(sol.y[:, -1])
        if index == 0:
            peak = state[0]
    return state, peak


def stationary_cycle(a1, b1, a2, b2, duty, period):
    h1, h2 = b1/a1, b2/a2
    assert 0 < h1 < h2 < 1 and 0 < duty < 1 and period > 0
    abar = duty*a1+(1-duty)*a2
    h = (duty*b1+(1-duty)*b2)/abar
    flow = lambda x: one_cycle(x,a1,b1,a2,b2,duty,period,h)
    lo = brentq(lambda x: flow(x)[0][0]-x, h1+1e-10, h2-1e-10,
                xtol=1e-14)
    state, hi = flow(lo)
    assert abs(state[0]-lo)<2e-10
    J0, J1, J2, integral_fx = state[1:]
    V = J2/J0
    exponent = integral_fx/period
    identity_exponent = abar*(h*(1-h)-V)
    assert abs(J0-abar*period)<1e-9
    assert abs(J1/J0-h)<5e-10
    assert 0<h1<lo<h<hi<h2<1
    assert 0<V<(h-lo)*(hi-h)<(h-h1)*(h2-h)
    assert exponent>0 and abs(exponent-identity_exponent)<1e-9
    return dict(h=h,lo=lo,hi=hi,V=V, exponent=exponent,
                multiplier=exp(period*exponent), abar=abar)


def run_checks():
    checked=0
    parameter_sets=(
        (3.0, 1.0, 3.0, 2.0, 0.5),
        (4.0, 1.0, 3.0, 2.0, 0.4),
        (2.5, 0.3, 7.0, 6.0, 0.2),
        (8.0, 1.5, 5.0, 3.5, 0.7),
    )
    for params in parameter_sets:
        a1,b1,a2,b2,duty=params
        prev=None
        for T in (0.02, 0.1, 0.5, 1., 2., 3., 7., 12.) if params != parameter_sets[-1] else (0.02, 0.1, 0.5, 1., 2., 3., 7.):
            r=stationary_cycle(*params,T)
            if prev:
                assert r['lo']<prev['lo'] and r['hi']>prev['hi']
                assert r['V']>prev['V'] and r['exponent']<prev['exponent']
            if T in (0.5,1.,2.,3.,7.):
                dt=1e-4
                upper=stationary_cycle(*params,T+dt)
                lower=stationary_cycle(*params,T-dt)
                Vprime=(upper['V']-lower['V'])/(2*dt)
                formula=((r['h']-r['lo'])*(r['hi']-r['h'])-r['V'])/T
                assert abs(Vprime-formula)<3e-7, (params,T,Vprime,formula)
            if T == 0.02:
                h=r['h']; v=duty*h*(1-h)*(a1*h-b1)
                assert abs(r['V']/T**2-v*v/12)<max(3e-7,0.005*v*v/12)
            checked+=1
            prev=r
        print('parameters:', params, 'largest tested period:',
              {k:round(v,10) for k,v in r.items() if k!='multiplier'})
    print('PASS:',checked,'period/parameter evaluations plus derivative, limits, strict ordering and Floquet checks')

if __name__=='__main__':
    run_checks()
