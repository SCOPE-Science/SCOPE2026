"""Reproducibility checks for the weak-drive exponential Duffing lift.

Finite symbolic checks supplement, but do not replace, the proof of global
attraction or the analytical perturbation expansion.
"""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

x, y, B, e, t, a = s.symbols('x y B e t a', real=True)
V = y**2 / 2 + 3*x*x/4 + B*x**4/4 + x*y/2
Dx = y
Dy = -y-x-B*x**3+e*s.cos(t)
assert s.simplify(s.diff(V,x)*Dx+s.diff(V,y)*Dy + (y*y+x*x+B*x**4)/2-e*(y+x/2)*s.cos(t)) == 0
W, v, r = s.symbols('W v r', real=True)
Q = v**2/2+s.Rational(3,4)*W**2+v*W/2
assert s.simplify(s.diff(Q,W)*v+s.diff(Q,v)*(-v-W-r*W)+(v*v+W*W)/2+r*W*(v+W/2)) == 0
L=lambda f: s.expand(s.diff(f,t,2)+s.diff(f,t)+f)
u=B*(s.Rational(3,4)*s.cos(t)-s.Rational(2,73)*s.sin(3*t)-s.Rational(3,292)*s.cos(3*t))
assert s.trigsimp(L(u)+B*s.sin(t)**3).expand(trig=True).simplify()==0
assert s.integrate(s.sin(t)*u,(t,0,2*s.pi)).simplify()==0
assert s.integrate(s.sin(t)**2,(t,0,2*s.pi))==s.pi
assert s.integrate(s.sin(t)**4,(t,0,2*s.pi))==3*s.pi/4
print('Exact algebraic assertions: PASS')

# A numerical supplementary check of the asymptotic drift and its sign.
# The reference periodic solution is obtained by shooting; tests do not
# constitute proof of uniqueness or asymptotic error orders.
period=2*np.pi
for cubic in (0.0, 1.0, 5.0):
 for forcing in ((0.005,0.015,0.03) if cubic<=1 else (0.005,0.015,0.025)):
  def fun(time,state):
   xx, yy=state
   return [yy,-yy-xx-cubic*xx**3+forcing*np.cos(time)]
  def period_map(state, dense=False):
   sol=solve_ivp(fun,(0,period),state,rtol=3e-11,atol=1e-13,dense_output=dense)
   return sol if dense else sol.y[:,-1]
  solroot=root(lambda state: period_map(state)-state,[0,forcing],tol=1e-11)
  assert np.linalg.norm(period_map(solroot.x)-solroot.x)<1e-9
  sol=period_map(solroot.x,True)
  times=np.linspace(0,period,4001)
  xx=sol.sol(times)[0]
  assert np.max(np.abs(xx[:2001]+xx[2000:]))<1e-7
  for beta in (-2.0,0.0,1.0,3.0):
   drift=np.trapezoid(xx*np.exp(beta*xx),times)/period
   approx=beta*forcing**2/2+beta**3*forcing**4/16
   if beta==0: assert abs(drift)<1e-9
   else:
    assert drift*beta>0
    assert abs(drift-approx) < 40*forcing**6 * max(1.0,abs(beta)**5)*max(1.0,cubic**2)
print('Numerical one-period checks: PASS')
