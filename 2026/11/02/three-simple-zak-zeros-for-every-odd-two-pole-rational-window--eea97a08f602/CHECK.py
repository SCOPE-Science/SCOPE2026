"""Reproduce the algebraic identities underlying the two-pole Zak zero theorem.

Requires Python 3 and sympy. This is an auxiliary finite symbolic check;
parameter-uniform inequalities are proved in the accompanying manuscript.
"""
import sympy as sp
q,r,u,v,z=sp.symbols('q r u v z',nonzero=True,real=True)
S=u/(1-q*z)-v/(1-r*z)-q/(u*(z-q))+r/(v*(z-r))
D=(1-q*z)*(1-r*z)*(z-q)*(z-r)
N=sp.cancel(u*v*D*S)
assert sp.simplify(N-u*v*D*S)==0
assert sp.degree(N,z)==3
R=sp.factor(sp.resultant(N,sp.expand(z**3*N.subs(z,1/z)),z))
A=(u-v)*(q*r-u*v)+(q*v-r*u)*(1-u*v)
B=(u-v)*(q*r-u*v)-(q*v-r*u)*(1-u*v)
C=r*(1+v**2)*(q**2+u**2)-q*(1+u**2)*(r**2+v**2)
expected=-u**2*v**2*(q-1)*(q+1)*(q-r)**2*(r-1)*(r+1)*(q*r-1)**2*A*B*C**2
assert sp.factor(R-expected)==0
w,t=sp.symbols('w t',positive=True)
Nmid=sp.factor(N.subs({q:w**2,r:t**2,u:w,v:t}))
Mmid=t*w*(t-w)*(z-1)*(t*w-1)*(t*w*(z**2+1)+((1+w**2)*(1+t**2)+2*t*w)*z)
assert sp.expand(Nmid-Mmid)==0
Nedge=sp.factor(N.subs({u:1,v:1}))
assert sp.factor(Nedge + z*(q-r)*(z-1)*(z+1)*(q*r-1))==0
Sz=sp.diff(S,z)
# All three spatial Zak derivatives have positive real values for 0<r<q<1.
assert sp.factor(Sz.subs({z:1,u:1,v:1})+2*(q-r)*(q*r-1)/((q-1)**2*(r-1)**2))==0
assert sp.factor(Sz.subs({z:-1,u:1,v:1})+2*(q-r)*(q*r-1)/((q+1)**2*(r+1)**2))==0
assert sp.factor(Sz.subs({z:1,q:w**2,r:t**2,u:w,v:t})-(t-w)*(t*w-1)*((1+w**2)*(1+t**2)+4*t*w)/((1-t**2)**2*(1-w**2)**2))==0
# Discrete Zak sum versus its Fourier-series representation at interior points.
import math, cmath
for a,b,x,xi in [(0.24,0.31,0.23,0.31),(0.35,1.8,0.12,0.58),(1,2,0.27,0.47)]:
 g=lambda y:y/((y*y+a*a)*(y*y+b*b))
 direct=sum(g(x-m)*cmath.exp(2j*math.pi*m*xi) for m in range(-800,801))
 q0=math.exp(-2*math.pi*a);r0=math.exp(-2*math.pi*b)
 u0=q0**xi;v0=r0**xi;z0=cmath.exp(2j*math.pi*x)
 s0=u0/(1-q0*z0)-v0/(1-r0*z0)-q0/(u0*(z0-q0))+r0/(v0*(z0-r0))
 fourier=-1j*math.pi/(b*b-a*a)*cmath.exp(2j*math.pi*x*xi)*s0
 assert abs(direct-fourier)<4e-6,(a,b,x,xi,direct,fourier)
print('PASS: symbolic resultant, midpoint and edge factors, spatial derivatives, and 3 direct Zak tests')
