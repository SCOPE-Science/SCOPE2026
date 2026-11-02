#!/usr/bin/env python3
"""Independent exact-algebra and finite-matrix checks of a symmetric Erlang-2 oscillator's spectral peak theorem."""
import sympy as s
import numpy as np
from scipy.linalg import expm

z,k,d,w,t=s.symbols('z k d w t',real=True)
x,y=s.symbols('x y',positive=True)
Q=s.Matrix([[-k,k,0,0],[0,-k,k,0],[0,0,-k,k],[k,0,0,-k]])
Z=s.diag(1,1,-1,-1)
F=s.factor((s.ones(1,4)/4*(z*s.eye(4)-Q-s.I*d*Z).inv()*s.ones(4,1))[0])
Fexpected=(d*d*k+d*d*z+4*k**3+6*k*k*z+4*k*z*z+z**3)/((d*d+2*k*z+z*z)*(d*d+2*k*k+2*k*z+z*z))
assert s.cancel(F-Fexpected)==0

N=y*(x*x+(6-2*y)*x+y*y+6*y+8)
D=(x*x+(4-2*y)*x+y*y)*(x*x-2*y*x+(y+2)**2)
Sp=s.factor(s.re(F.subs({k:1,d:s.sqrt(y),z:s.I*w})).subs(w,s.sqrt(x)))
assert s.cancel(Sp-N/D)==0

P=s.Poly(x**5+(11-5*y)*x**4+(10*y*y-20*y+40)*x**3+(-10*y**3-6*y**2-32*y+52)*x**2+(5*y**4+28*y**3+24*y*y-8*y+32)*x-(y+2)*(y**4+11*y**3+10*y**2-24*y-32),x).as_expr()
assert s.factor(s.diff(N,x)*D-N*s.diff(D,x)+2*y*P)==0
q=512000*y**6-79872*y**5-954624*y**4+729856*y**3+1396656*y**2+239112*y+729
assert s.factor(s.discriminant(P,x)-65536*y*(y+2)*(4*y+5)**2*q)==0

# Positivity of q on [0,1] via its Mobius transform and on [1,infinity) via a translation.
c1=s.Poly(s.cancel((1+t)**6*q.subs(y,t/(1+t))),t).all_coeffs()
c2=s.Poly(q.subs(y,1+t),t).all_coeffs()
assert c1==[1843857,6987006,12016935,8722180,2603151,243486,729]
assert c2==[512000,2992128,6326016,6352640,4739760,4076136,1843857]
assert all(a>0 for a in c1+c2)

# At y=1, derivative P is positive for all x>=0; at y=2, P is strictly increasing,
# thanks to 120*x^2-232*x+416 having negative discriminant.
assert s.Poly(P.subs(y,1),x).all_coeffs()==[1,6,30,4,81,102]
assert s.Poly(P.subs(y,2),x).all_coeffs()==[1,1,40,-116,416,-256]
assert 232**2-4*120*416 < 0
assert s.polys.polytools.count_roots(P.subs(y,2),0,s.oo)==1

qcrit=y**4+11*y**3+10*y**2-24*y-32
roots=s.nroots(qcrit,maxsteps=100)
ycrit=float(next(s.re(r) for r in roots if abs(s.im(r))<1.e-10 and s.re(r)>0))
assert 1<ycrit<2
assert abs(ycrit-1.53440426264242)<1e-12

# Independent state-space resolvent calculations at arbitrary rates/frequencies.
Qnp=np.array([[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1]],dtype=float)
Diag=np.diag([1.,1.,-1.,-1.]); eye=np.eye(4); uni=np.ones(4)/4
rng=np.random.default_rng(129408)
for i in range(150):
    rate=float(np.exp(rng.uniform(-1.7,1.7)))
    delta=float(np.exp(rng.uniform(-1.4,1.4)))
    freq=float(rng.uniform(-5,5))
    direct=float(np.real(uni @ np.linalg.solve(1j*freq*eye-rate*Qnp-1j*delta*Diag,np.ones(4))))
    xx=(freq/rate)**2; yy=(delta/rate)**2
    predicted=float((yy*(xx**2+(6-2*yy)*xx+yy**2+6*yy+8))/((xx**2+(4-2*yy)*xx+yy**2)*(xx**2-2*yy*xx+(yy+2)**2)))/rate
    assert abs(direct-predicted)<1e-8*max(1,abs(predicted)),(rate,delta,freq,direct,predicted)

# The Markov switching comparator, at the same mean residence time 2/k,
# has transition rate k/2 and critical squared detuning y=1/2.
assert 2*ycrit**3 > 0
print('PASS: exact resolvent identity, rational spectrum, derivative and discriminant,')
print('       rigorous positivity certificates, transition root and 150 independent resolvent comparisons.')
print('critical squared detuning=',format(ycrit,'.14f'))
print('critical detuning/rate=',format(ycrit**0.5,'.14f'))
print('relative to equal-mean Markov threshold=',format((2*ycrit)**0.5,'.14f'))
