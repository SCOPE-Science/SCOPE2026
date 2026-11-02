#!/usr/bin/env python3
"""Standalone symbolic and numerical diagnostics for the stated four-mode model."""
import math
import numpy as np
import sympy as sp

checks = 0

def require(cond, message):
    global checks
    assert bool(cond), message
    checks += 1

E, a, b, gamma = sp.symbols('E a b gamma', positive=True, real=True)
I = sp.I
H = sp.Matrix([[I*gamma,a,0,0], [a,0,b,0], [0,b,0,a], [0,0,a,-I*gamma]])
p = sp.expand((E*sp.eye(4)-H).det())
expected = E**4+(gamma**2-2*a**2-b**2)*E**2+a**4-b**2*gamma**2
require(sp.simplify(p-expected)==0,'characteristic determinant')
t, x = sp.symbols('t x', positive=True, real=True)
u = sp.symbols('u', real=True)
quad = u**2-(2*t+1-x)*u+(t**2-x)
disc = sp.discriminant(quad,u)
require(sp.expand(disc-((x-(2*t-1))**2+4*t*(2-t)))==0,'quadratic discriminant')
q = sp.symbols('q',positive=True,real=True)
xplus = 2*t-1+2*q
xminus = 2*t-1-2*q
require(sp.simplify(sp.expand((t**2-xplus)-(q-1)**2).subs(q**2,t*(t-2)))==0,'upper product identity')
require(sp.simplify(sp.expand((t**2-xminus)-(q+1)**2).subs(q**2,t*(t-2)))==0,'lower product identity')
require(sp.expand((2*t+1-xplus)-2*(1-q))==0,'upper trace identity')
require(sp.expand((2*t+1-xminus)-2*(1+q))==0,'lower trace identity')
require(sp.factor(p.subs({a:sp.sqrt(2),b:1,gamma:sp.sqrt(3)})-(E**2-1)**2)==0,'lower cusp exception polynomial')
tcrit = 1+sp.sqrt(2)
require(sp.simplify(p.subs({a:sp.sqrt(tcrit),b:1,gamma:tcrit})-E**4)==0,'upper critical exceptional polynomial')
require((H.subs({a:sp.sqrt(2),b:1,gamma:sp.sqrt(3)})-sp.eye(4)).rank()==3,'positive Jordan eigenspace at lower cusp')
require((H.subs({a:sp.sqrt(2),b:1,gamma:sp.sqrt(3)})+sp.eye(4)).rank()==3,'negative Jordan eigenspace at lower cusp')
Hcrit=H.subs({a:sp.sqrt(tcrit),b:1,gamma:tcrit})
require(Hcrit.rank()==3,'fourfold exceptional point has one eigenvector')
require((Hcrit**4).applyfunc(sp.simplify)==sp.zeros(4) and (Hcrit**3).applyfunc(sp.simplify)!=sp.zeros(4),'order-four nilpotency')

# Test actual eigenvalues of the original complex matrix independently of the scalar criterion.
def four_eigs(a0,b0,g0):
    z=np.array([[1j*g0,a0,0,0],[a0,0,b0,0],[0,b0,0,a0],[0,0,a0,-1j*g0]],dtype=complex)
    return np.linalg.eigvals(z)

def all_real_simple(a0,b0,g0):
    z=four_eigs(a0,b0,g0)
    return max(abs(z.imag))<5e-8 and min(abs(z[i]-z[j]) for i in range(4) for j in range(i+1,4))>1e-6

def nonreal(a0,b0,g0):
    return max(abs(z.imag) for z in four_eigs(a0,b0,g0))>1e-6

for t0 in np.linspace(2.003,1+math.sqrt(2)-0.003,37):
    qt=math.sqrt(t0*(t0-2))
    xm=2*t0-1-2*qt;xp=2*t0-1+2*qt
    for xx in (0, 0.2*xm, 0.8*xm):
        require(all_real_simple(math.sqrt(t0),1,math.sqrt(xx)),'first real interval')
    for frac in (0.25,0.5,0.75):
        require(nonreal(math.sqrt(t0),1,math.sqrt((1-frac)*xm+frac*xp)),'broken interval')
    for frac in (0.2,0.5,0.8):
        require(all_real_simple(math.sqrt(t0),1,math.sqrt((1-frac)*xp+frac*t0*t0)),'recovered interval')
    for xx in (t0*t0+0.08,t0*t0+1.0):
        require(nonreal(math.sqrt(t0),1,math.sqrt(xx)),'final nonreal interval')

for t0 in (0.02,0.1,0.5,1.0,1.8,1.999,2.0):
    for xx in (0,0.25*t0*t0,0.5*t0*t0):
        require(all_real_simple(math.sqrt(t0),1,math.sqrt(xx)),'single initial real phase')
    for xx in (1.1*t0*t0,2*t0*t0+1):
        require(nonreal(math.sqrt(t0),1,math.sqrt(xx)),'after initial real phase')

for t0 in (1+math.sqrt(2)+0.001,2.6,3.0,4,8,20):
    qt=math.sqrt(t0*(t0-2));xm=2*t0-1-2*qt;xp=2*t0-1+2*qt
    require(all_real_simple(math.sqrt(t0),1,math.sqrt(0.5*xm)),'prebreak high-coupling phase')
    require(nonreal(math.sqrt(t0),1,math.sqrt((xm+xp)/2)),'high-coupling discr broken')
    require(nonreal(math.sqrt(t0),1,math.sqrt(xp+1)),'post-discr phase remains nonreal')

C=(2-math.sqrt(3))/(2*math.sqrt(2)+1)
last=1.
for t0 in np.linspace(2+1e-7,1+math.sqrt(2)-1e-7,350):
    qt=math.sqrt(t0*(t0-2)); xp=2*t0-1+2*qt
    w=(t0-math.sqrt(xp))/(2*math.sqrt(t0)+1)
    require(0<w<C,'sharp nonattained normalized bound')
    require(w<last,'strict monotonicity samples')
    last=w
for eps in (1e-4,1e-5,1e-6,1e-7):
    t0=2+eps; qt=math.sqrt(t0*(t0-2));xm=2*t0-1-2*qt;xp=2*t0-1+2*qt
    J=2*math.sqrt(t0)+1
    w=(t0-math.sqrt(xp))/J
    broken=(math.sqrt(xp)-math.sqrt(xm))/J
    require(abs(w-C+broken/2)<2*broken**2,'linear Pareto-edge expansion')

print('PASS: %d symbolic and numerical diagnostic assertions' % checks)
