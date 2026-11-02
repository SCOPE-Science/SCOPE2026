"""Standalone reproducibility checks for an affine-forced quadratic flow's local Hopf family.
Only scientific formulas and numerical support are recorded; no infinite proof is inferred from numerics.
"""
import sympy as s
b=s.symbols('b',positive=True,real=True)
i=s.I
A=s.Matrix([[0,1,0],[-1,0,0],[0,0,-b]])
q=s.Matrix([1,i,0]); qb=s.conjugate(q)
p=s.Matrix([1,i,0])/2

def B(u,v):
    return s.Matrix([0, u[1]*v[2]+u[2]*v[1], -5*(u[0]*v[1]+u[1]*v[0])+u[0]*v[2]+u[2]*v[0]])
assert s.simplify((A*q-i*q).norm())==0
assert s.simplify(s.conjugate(p).dot(q)-1)==0
assert B(q,q)==s.Matrix([0,0,-10*i])
assert B(q,qb)==s.zeros(3,1)
h20=s.simplify((2*i*s.eye(3)-A).inv()*B(q,q))
G=s.factor(s.simplify(s.conjugate(p).dot(B(qb,h20))))
assert s.simplify(G-5*i/(b+2*i))==0
l1=s.simplify(s.re(G)/2)
assert s.simplify(l1-5/(b*b+4))==0
print('G21=',G,'l1=',l1)

# Independently verify Poincare-Lindstedt resonance with real Fourier harmonics.
th,R=s.symbols('th R',real=True)
x1=R*s.cos(th); y1=-R*s.sin(th)
z2=-1/b+ s.Rational(5,2)*R**2*(b*s.sin(2*th)-2*s.cos(2*th))/(b*b+4)
assert s.trigsimp(s.diff(z2,th)+b*z2+1+5*x1*y1)==0
forcing=s.expand_trig(y1*z2)
fund_s=s.simplify(s.integrate(forcing*s.sin(th),(th,0,2*s.pi))/s.pi)
fund_c=s.simplify(s.integrate(forcing*s.cos(th),(th,0,2*s.pi))/s.pi)
expected_s=R/b-5*R**3/(2*(b*b+4))
expected_c=-5*b*R**3/(4*(b*b+4))
assert s.simplify(fund_s-expected_s)==0
assert s.simplify(fund_c-expected_c)==0
r2=2*(b*b+4)/(5*b)
omega2=s.simplify(s.cancel(-fund_c/(2*R)).subs(R**2,r2))
assert omega2==s.Rational(1,4)
print('amplitude_squared_over_minus_alpha=',r2,'frequency_coefficient=',omega2)

# Numerical checks of actual nontrivial periodic orbits, which are repelling in the radial direction.
from scipy.integrate import solve_ivp
from scipy.optimize import root
import numpy as np

def flow(t,s0,alpha,b0):
    x,y,z=s0
    return np.array([y,-x+y*z,alpha-b0*z-5*x*y+x*z])

def solve_cycle(alpha,b0):
    amp=np.sqrt(-2*alpha*(b0*b0+4)/(5*b0))
    period=2*np.pi*(1+alpha/4)
    z0=alpha/b0-5*amp**2/(b0*b0+4)
    def residual(v):
        x,z,T=v
        if T<=1: return np.array([50+x,50+z,50+T])
        sol=solve_ivp(flow,(0,T),[x,0,z],args=(alpha,b0),method='DOP853',rtol=1e-11,atol=1e-13)
        return sol.y[:,-1]-np.array([x,0,z])
    sol=root(residual,[amp,z0,period],tol=1e-11)
    if not sol.success and np.linalg.norm(residual(sol.x))>1e-8: raise RuntimeError((alpha,b0,sol.message,sol.x,residual(sol.x)))
    x,z,T=sol.x
    assert x>0 and abs(x)>amp/2
    print('numeric', 'b=',b0,'alpha=',alpha,'x_at_max=',f'{x:.9g}','predicted_sqrt_amplitude=',f'{amp:.9g}','period=',f'{T:.11g}','predicted_period=',f'{period:.11g}','residual=',f'{np.linalg.norm(residual(sol.x)):.2g}')

for b0 in [0.5,1.0,2.0]:
    for alpha in [-0.005,-0.0025]: solve_cycle(alpha,b0)
print('VERIFICATION PASSED')
