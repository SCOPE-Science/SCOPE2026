"""Reproducible identities and numerical checks for H4 inner linear approximants."""
import sympy as s
import numpy as np
from scipy.optimize import minimize

a,b,u,v=s.symbols('a b u v', real=True)
F=1+4*(a*a+b*b)+a**4+4*a*a*b*b+b**4-4*u*a-4*u*a*(a*a+2*b*b)-4*v*a*a*b+2*u*u*a*a
assert s.expand(s.diff(F,b)/4-(b*(2+2*a*a+b*b-4*u*a)-v*a*a))==0
assert s.expand(s.diff(F,a).subs(a,1) - (1-u)*(2*(1-u)*(5+u)+8*(b-(1+u)/2)**2)-8*b*(1-u*u-v))==0
print('symbolic b-stationarity and a=1 derivative factor: PASS')
z=np.exp(2j*np.pi*np.arange(8192)/8192)
U=.5; R=1/3
G1=(R+z)/(1+R*z)
G2=(R+z*z)/(1+R*z*z)
I1=(U+z*G1)/(1+U*z*G1)
I2=(U+z*G2)/(1+U*z*G2)
assert np.max(np.abs(abs(I1)-1)) < 1e-12
assert np.max(np.abs(abs(I2)-1)) < 1e-12
for aa,bb in [(0.13,0.09),(0.28,0.05),(0.4,-0.2),(0.1+0.2j,0.2-0.13j)]:
 p=aa+bb*z
 actual1=np.mean(abs(1-I1*p)**4)
 actual2=np.mean(abs(1-I2*p)**4)
 predicted=(1+4*(abs(aa)**2+abs(bb)**2)+abs(aa)**4+4*abs(aa*bb)**2+abs(bb)**4
 -4*(U*aa).real-4*(U*aa*(abs(aa)**2+2*abs(bb)**2)+(1-U*U)*R*aa*aa*np.conj(bb)).real
 +2*(U*U*aa*aa).real)
 assert abs(actual1-predicted)<1e-11
 assert abs(actual2-predicted)<1e-11
print('two distinct inner functions, identical first jets, quartic formula: PASS')
for U in [0.2,0.5,0.7,0.85,0.93]:
 V=1-U*U
 expr=s.lambdify((a,b,u,v),F,'numpy')
 opt=minimize(lambda t:expr(t[0],t[1],U,V),[U/2,0.02],method='BFGS',tol=1e-12)
 aa,bb=opt.x
 assert 0<bb<aa*aa/2 and 0<aa<1 and aa/bb>2
 print(f'Blaschke input u={U:.2f}: root={aa/bb:.5f}')
print('Numerics illustrate, do not prove, the infinite-family theorem.')
