"""Independent finite checks of the Abel-family estimates; not a proof of global claims."""
import math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
T=2*math.pi

def integrate(a,r):
    def rhs(t,z):
        x,v=z
        A=a+math.cos(2*t); B=math.sin(t)
        return [B*x*x+A*x*x*x,(2*B*x+3*A*x*x)*v]
    def escape(t,z): return 10000-z[0]
    escape.terminal=True
    escape.direction=-1
    s=solve_ivp(rhs,(0,T),[r,1.0],rtol=2e-11,atol=2e-13,max_step=.015,events=escape)
    if s.status != 0: raise ValueError('trajectory escaped')
    return float(s.y[0,-1]-r),float(s.y[1,-1])

assert 0.125 - 2*(0.25)**2 == 0 # square-completion max; at y=1/4
for a in [-1.0,-0.8,-0.5]:
    for x0 in [0.05,0.1,0.3]:
        assert integrate(a,x0)[0] < 0
for a,lo,hi in [(-0.02,0.1,0.3),(-0.001,0.03,0.1)]:
    dlo,_=integrate(a,lo); dhi,_=integrate(a,hi)
    assert dlo<0<dhi
    root=brentq(lambda x: integrate(a,x)[0],lo,hi,xtol=1e-11)
    displacement,mult=integrate(a,root)
    assert abs(displacement)<1e-7 and mult>1
    print('parameter',a,'root',root,'multiplier',mult)
print('CHECKS_PASS')
