"""Reproduce exact identities and finite diagnostics for a two-compartment ODE integrator.

Requires Python 3.10+, SymPy and mpmath. Analytical limits are proved in RESULT.md,
not by the finite diagnostics performed here.
"""
import math
import sympy as sp
from mpmath import mp

checks = 0
r, s = sp.symbols('r s', positive=True)
d = 1/r - r
R = r * sp.exp(d*s)
# The formula obtained by explicitly forming the two-stage, one-sweep step.
pred_x = sp.exp(s*(r-1))
pred_y = r*sp.exp(s*(1/r-1))
source_x = sp.Rational(1,2)*s*((r-1) + (pred_y-pred_x)/pred_x)
source_y = sp.Rational(1,2)*s*((1/r-1) + (pred_x-pred_y)/pred_y)
closed_x = sp.Rational(1,2)*s*(r+R-2)
closed_y = sp.Rational(1,2)*s*(1/r+1/R-2)
for a,b in [(source_x,closed_x),(source_y,closed_y)]:
    assert sp.simplify(a-b) == 0
    checks += 1

# Exact Taylor coefficients for the total-mass difference at fixed positive r.
series_x = sp.series(sp.exp(closed_x),s,0,4).removeO().expand()
series_y = sp.series(r*sp.exp(closed_y),s,0,4).removeO().expand()
series_total = series_x + series_y
for power,target in [
    (0,1+r),
    (1,0),
    (2,0),
    (3,-(r-1)**4*(r+1)/(12*r**2)),
]:
    assert sp.simplify(series_total.coeff(s,power)-target) == 0
    checks += 1

# Predictor's leading mass surplus: strict Jensen for the full statement.
pred_series = sp.series(pred_x+r*sp.exp(s*(1/r-1)),s,0,3).removeO().expand()
assert sp.simplify(pred_series.coeff(s,2)-(r+1)*(r-1)**2/(2*r)) == 0
checks += 1

# Verify independently evaluated source-stage and closed-form endpoints numerically.
for x,y in [(2.0,1.0),(1.0,2.0),(3.0,7.0),(2.0,3.0),(9.0,1.0),(1.0,1.0)]:
    for rate in [0.5,1.0,1.75]:
        for h in [0.02,0.1,0.4,0.8]:
            z=rate*h
            px=x*math.exp(z*(y/x-1))
            py=y*math.exp(z*(x/y-1))
            direct_log_x=math.log(x)+0.5*h*(rate*(y-x)/x+rate*(py-px)/px)
            direct_log_y=math.log(y)+0.5*h*(rate*(x-y)/y+rate*(px-py)/py)
            rr=y/x
            Rr=rr*math.exp(z*(1/rr-rr))
            closed_log_x=math.log(x)+0.5*z*(rr+Rr-2)
            closed_log_y=math.log(y)+0.5*z*(1/rr+1/Rr-2)
            for a,b in [(direct_log_x,closed_log_x),(direct_log_y,closed_log_y)]:
                assert math.isclose(a,b,rel_tol=3e-13,abs_tol=3e-13)
                assert math.isfinite(a)
                checks+=2

mp.dps = 80
for rstr in ['0.1','0.25','0.5','0.8','1.2','2','10']:
    q=mp.mpf(rstr)
    # Small-step mass deficit after correction; predictor has mass surplus.
    z=mp.mpf('0.0001')
    P=q*mp.exp(z*(1/q-q))
    M=mp.exp(z*(q+P-2)/2)+q*mp.exp(z*(1/q+1/P-2)/2)
    Mp=mp.exp(z*(q-1))+q*mp.exp(z*(1/q-1))
    assert M < 1+q
    assert Mp > 1+q
    checks += 2
    # Large-step logarithmic growth: calculations in log space avoid overflow.
    qf=float(q)
    dd=abs(qf-1/qf)
    large_s=30/dd
    Rf=qf*math.exp(large_s*(1/qf-qf))
    ux=0.5*large_s*(qf+Rf-2)
    vy=math.log(qf)+0.5*large_s*(1/qf+1/Rf-2)
    big=max(ux,vy)
    logmass=big+math.log1p(math.exp(min(ux,vy)-big))
    value=(logmass-math.log(1+qf))/(large_s*math.exp(30))
    assert abs(value-0.5*min(qf,1/qf)) < 5e-10
    checks+=1

# Exact illustrative initial data (2,1), rate 1.
for z in [.1,.5,1.,2.]:
    direct_u=2*math.exp(z*math.exp(1.5*z)/4-3*z/4)
    direct_v=math.exp(z*math.exp(-1.5*z))
    Rf=.5*math.exp(1.5*z)
    u=2*math.exp(0.5*z*(.5+Rf-2))
    v=math.exp(0.5*z*(2+1/Rf-2))
    assert math.isclose(direct_u,u,rel_tol=1e-12)
    assert math.isclose(direct_v,v,rel_tol=1e-12)
    checks+=2

print('PASS: ', checks, 'symbolic and finite verification assertions')
