"""Finite numerical diagnostics only, not a proof."""
from math import log
from scipy.integrate import solve_ivp

X0=1.0
for b in (1.0,0.0,-1.0):
    def rhs(x,y): return [(x**5/y[0]) + b*x**3]
    outcomes=[]
    for y0 in (1.0,2.0):
        sol=solve_ivp(rhs,(X0,40.0),[y0],rtol=2e-11,atol=1e-11,max_step=.05)
        assert sol.success
        y=sol.y[0,-1]
        if b>0:
            finite_part=y-b*40**4/4-2*40**2/b+32*log(40)/b**3
            outcomes.append((y,finite_part))
        elif b==0:outcomes.append((y,y*y-40**6/3))
        else:outcomes.append((y,y-40**2))
    print('b',b,'at x=40:',outcomes)
    if b>0:assert outcomes[1][1]>outcomes[0][1]
    elif b==0:assert abs(outcomes[0][1]-(1-1/3))<1e-4
    else:assert abs(outcomes[0][1]+2)<.02
print('NUMERICAL_PROBE_OK')
