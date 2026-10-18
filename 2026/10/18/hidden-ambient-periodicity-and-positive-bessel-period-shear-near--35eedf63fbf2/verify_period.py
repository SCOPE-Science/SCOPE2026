"""Independent numerical diagnostics for the quadratic-cylinder period-shear theorem.

Dependencies: Python 3, NumPy, SciPy. These tests do not replace the proof.
"""
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import iv
from scipy.integrate import solve_ivp, quad

NODES, WEIGHTS = leggauss(240)

def roots(h, a, c):
    lam = c/a
    q = lambda x: 1.0-x*x+h*np.exp(lam*x)
    left = brentq(q, -1.2, -0.8, xtol=1e-14)
    right = brentq(q, 0.8, 1.2, xtol=1e-14)
    return left,right

def period(h, a, c):
    lo,hi = roots(h,a,c)
    theta = pi*(NODES+1)/2
    x = (lo+hi)/2+(hi-lo)*np.cos(theta)/2
    q = 1-x*x+h*np.exp((c/a)*x)
    w = (hi-lo)*np.sin(theta)/(2*a*np.sqrt(q))
    return (pi/2)*np.dot(WEIGHTS,w)

def first_integrals(x,y,z,a,c,b3,b5,b6):
    h = np.exp(-(c/a)*x)*(x*x+z*z-1)
    B = b6/(2*a)
    v = quad(lambda u: np.exp(-B*u)*(b3+b5*u)/(2*a),0,x,epsabs=2e-13)[0]
    j = np.exp(-B*x)*y-v
    return h,j

cases = [(1.,.3),(1.,1.2),(1.,-1.5),(.8,.72),(1.3,-.8)]
for a,c in cases:
    predicted=pi*c*iv(1,c/a)/(2*a*a)
    assert predicted>0
    assert abs(period(0.,a,c)-pi/a)<1e-8
    step=2e-4
    measured=(period(step,a,c)-period(-step,a,c))/(2*step)
    assert abs(measured-predicted)<5e-5, (a,c,predicted,measured)
    print(f'a={a} c={c}: exact Tprime={predicted:.12g}, finite diff={measured:.12g}')

periods=[period(h,1.,1.2) for h in [-.02,-.01,0,.01,.02]]
assert all(x<y for x,y in zip(periods,periods[1:])),periods

a,c,b3,b5,b6=1.3,.7,1.0,-.4,.5
h=.02
_,right=roots(h,a,c)
y0=.2
T=period(h,a,c)
H0,J0=first_integrals(right,y0,0.,a,c,b3,b5,b6)
assert abs(H0-h)<1e-12

def field(t,v):
    x,y,z=v
    return [2*a*z,z*(b3+b5*x+b6*y),c*(x*x+z*z-1)-2*a*x]
sol=solve_ivp(field,[0,T],[right,y0,0],rtol=1e-11,atol=1e-12,dense_output=True)
assert sol.success
assert np.max(np.abs(sol.y[:,-1]-[right,y0,0])) <2e-8
for u in np.linspace(0,T,15):
    x,y,z=sol.sol(u)
    Hu,Ju=first_integrals(x,y,z,a,c,b3,b5,b6)
    assert abs(Hu-H0)<2e-8
    assert abs(Ju-J0)<2e-8
print('PASS: analytic-frequency diagnostics, monotonic sample, orbital return, two conserved quantities.')
