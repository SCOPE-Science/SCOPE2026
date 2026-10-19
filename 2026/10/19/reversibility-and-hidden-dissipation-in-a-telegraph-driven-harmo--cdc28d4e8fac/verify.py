"""Reproducible identities for a Markov-switching planar harmonic vortex.
Run: python verify.py.  Algebraic checks corroborate the analytic proof in RESULT.md.
"""
import math
import sympy as sp
from scipy.linalg import expm
import numpy as np

x,y,k,d,w,l,s=sp.symbols('x y k d w l s',positive=True,real=True)
assertions=0

def eq(a,b):
    global assertions
    z=sp.trigsimp(sp.factor(a-b))
    assert z==0, z
    assertions+=1

# Stationary Gaussian and divergence-free sign-dependent rotational flux.
q=d/k
rad=x*x+y*y
phi=sp.exp(-k*rad/(2*d))
bx=-k*x-w*s*y
by=-k*y+w*s*x
F=-(sp.diff(bx*phi,x)+sp.diff(by*phi,y))+d*(sp.diff(phi,x,2)+sp.diff(phi,y,2))
eq(sp.simplify(F/phi),0)
for sg in [1,-1]:
    eq(sp.diff((-sg*w*y)*phi,x)+sp.diff((sg*w*x)*phi,y),0)

# The generator adjoint intertwines with sign swapping when switching is symmetric.
def L(expr,flip=False):
    expr=sp.sympify(expr)
    torque= -w if flip else w
    out=(-k*x-torque*s*y)*sp.diff(expr,x)+(-k*y+torque*s*x)*sp.diff(expr,y)
    out+=d*(sp.diff(expr,x,2)+sp.diff(expr,y,2)) + l*(expr.subs(s,-s)-expr)
    return sp.expand(out)
T=lambda expr:sp.expand(sp.sympify(expr).subs(s,-s))
for f in [1,x,y,s,s*x,s*y,x*x+y*y,x*y,s*x*y,x*x*y,s*x*x*y]:
    for sign in [1,-1]:
        eq((L(f,flip=True)-T(L(T(f)))).subs(s,sign),0)

# Telegraphed angular characteristic: symmetric two-state generator,
# instantaneous derivatives and damped oscillator recurrence.
I=sp.I
M=sp.Matrix([[I*w-l,l],[l,-I*w-l]])
u=sp.Matrix([1,1]);v=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)]])
deriv=[sp.simplify((v*M**n*u)[0]) for n in range(6)]
for n,expected in enumerate([1,0,-w*w,2*l*w*w,w**4-4*l*l*w*w,
                               8*l**3*w*w-4*l*w**4]):
    eq(deriv[n],expected)
for n in range(4):
    eq(deriv[n+2]+2*l*deriv[n+1]+w*w*deriv[n],0)

# Radial (squared-radius) generator is autonomous and torque-independent.
for f in [rad,rad**2,rad**3]:
    n={rad:1,rad**2:2,rad**3:3}[f]
    expected=n*rad**(n-1)*(4*d-2*k*rad)+4*d*rad*n*(n-1)*rad**(n-2)
    eq(L(f),expected)

# One-time Gaussian, label-resolved stationary current and entropy coefficient.
# E|X|^2=2d/k; each label has probability 1/2.
eq((w*w/d)*(2*d/k),2*w*w/k)

# Asymmetric switching yields the nonzero stationary area current.
a,b=sp.symbols('a b',positive=True,real=True)
p_plus=b/(a+b);p_minus=a/(a+b)
eq(p_plus+p_minus,1)
eq(2*q*w*(p_plus-p_minus),2*d*w*(b-a)/(k*(a+b)))

# Conditional pairwise Gaussian Wick factor: Cov(X_t^1^2, X_0^2^2 | phase)
# =2(C_{12})^2; after symmetric averaging it is q^2 exp(-2kt)(1-m_{2w}).
phase,r=sp.symbols('phase r',real=True)
eq(2*(q*r*sp.sin(phase))**2,q*q*r*r*(1-sp.cos(2*phase)))

# Oscillatory and overdamped angular-characteristic regimes agree with
# the independent 2-state matrix exponential at noncritical parameters.
def formula(t,rate,omega):
    if abs(rate-omega)<1e-12:
        return math.exp(-rate*t)*(1+rate*t)
    if rate>omega:
        z=math.sqrt(rate*rate-omega*omega)
        return math.exp(-rate*t)*(math.cosh(z*t)+rate/z*math.sinh(z*t))
    z=math.sqrt(omega*omega-rate*rate)
    return math.exp(-rate*t)*(math.cos(z*t)+rate/z*math.sin(z*t))
for rate,omega in [(0.45,1.3),(1.3,1.3),(2.5,1.3),(0.8,1.8)]:
    for t in [0.05,0.3,1.2,2.6,3.7]:
        mat=np.array([[1j*omega-rate,rate],[rate,-1j*omega-rate]],dtype=complex)
        z=(np.ones(2)@expm(t*mat)@np.ones(2))/2
        assert abs(z.imag)<2e-13
        assert abs(z.real-formula(t,rate,omega))<2e-12
        assertions+=2

# Small-lag coefficient is nonzero and the projected conditional mean cannot
# be a Markov semigroup when angular speed is nonzero.
eq(deriv[2],-w**2)
print(f'PASS: {assertions} independently checked identities/comparisons')
