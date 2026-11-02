#!/usr/bin/env python3
"""Exact checks and illustrative trajectories for a sinusoidal jerk flow.

Requirements: Python 3.10+, SymPy, NumPy, SciPy.
No finite computation substitutes for the global LaSalle or Hopf arguments.
"""
import math
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

x, y, z, a, b, c, d = s.symbols('x y z a b c d', real=True, positive=True)
P = -(1+b**2/a)*y**2/2 - b*y*z-a*z**2/2+c*y*s.sin(d*x)-b*c*s.cos(d*x)/d
v = s.Matrix([y,a*z,-y-b*z+c*s.sin(d*x)])
assert s.simplify(sum(s.diff(P,t)*v[i] for i,t in enumerate((x,y,z)))
                  -(b+c*d*s.cos(d*x))*y*y)==0
Q = s.Matrix([[1+b*b/a,b],[b,a]])
assert s.factor(Q.det()) == a
w=s.sqrt(a)
A=s.Matrix([[0,1,0],[0,0,a],[-b,-1,-b]])
right=s.Matrix([1,s.I*w,-1])
left3=(-a-s.I*b*w)/(2*(a+b*b))
left=s.Matrix([s.I*b/w,(b+s.I*w)/a,1])*left3
assert s.simplify(A*right-s.I*w*right)==s.zeros(3,1)
assert s.simplify(left.T*A-s.I*w*left.T)==s.zeros(1,3)
assert s.simplify((left.T*right)[0]-1)==0
linear=(a+s.I*b*w)/(2*(a+b*b))
cubic=s.simplify((b*d*d/2)*left3)
assert s.simplify(s.re(cubic)+a*b*d*d/(4*(a+b*b)))==0
assert s.simplify(s.re(linear)-a/(2*(a+b*b)))==0
r2=s.simplify(-s.re(linear)/s.re(cubic))
assert s.simplify(r2-2/(b*d*d))==0
assert s.simplify(s.im(linear)+s.im(cubic)*r2)==0

# Forward integration tests: stable nearby Hopf cycle and subcritical equilibrium.
A0,B0,D0=2.,0.6,2.
center=math.pi/D0
for mu in [0.012,0.018]:
    C0=(B0+mu)/D0
    fun=lambda t,u:[u[1],A0*u[2],-u[1]-B0*u[2]+C0*math.sin(D0*u[0])]
    sol=solve_ivp(fun,(0,1200),[center+0.13,0,0],rtol=1e-8,atol=1e-10,max_step=0.25)
    assert sol.success
    tail=sol.t>1030
    measured=np.max(np.abs(sol.y[0,tail]-center))
    expected=math.sqrt(8*mu/(B0*D0**2))
    assert abs(measured/expected-1)<0.03,(mu,measured,expected)
    peaks,_=find_peaks(sol.y[0]); peaks=peaks[sol.t[peaks]>1030]
    observed=float(np.mean(np.diff(sol.t[peaks])))
    assert abs(observed-2*math.pi/math.sqrt(A0))<0.002,(mu,observed)
for C0 in [0.15,0.25]:
    fun=lambda t,u:[u[1],A0*u[2],-u[1]-B0*u[2]+C0*math.sin(D0*u[0])]
    sol=solve_ivp(fun,(0,250),[center+0.25,0.02,0],rtol=1e-8,atol=1e-10,max_step=.25)
    assert sol.success and np.linalg.norm(sol.y[:,-1]-np.array([center,0,0]))<0.08
print('PASS: exact Lyapunov derivative, positive-definite quadratic part, Hopf normal form, first-order frequency cancellation, illustrative trajectories')
