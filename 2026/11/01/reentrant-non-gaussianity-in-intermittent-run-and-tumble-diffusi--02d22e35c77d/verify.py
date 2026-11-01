#!/usr/bin/env python3
"""Exact algebra and independent finite-time moment-semigroup checks for an intermittent-motion model."""
import sympy as sp
import numpy as np
from scipy.linalg import expm

b,c,d,k,s,L=sp.symbols('b c d k s L', positive=True)
Q=sp.Matrix([[-1-b,1,b],[1,-1-b,b],[c/2,c/2,-c]])
# An additive displacement with +/- unit drift and passive diffusivity d.
M=Q+sp.diag(k,-k,d*k*k)
F=sp.expand((M-L*sp.eye(3)).det())
x=sp.symbols('x')
F_formula=((c+b*(b+2)*d)*x-d*x*x-(b+2)*(b+c)*L +
           (1+2*(b+1)*d)*x*L-(2+2*b+c)*L**2+d*x*L**2-L**3)
assert sp.simplify(F.subs(k*k,x)-F_formula)==0
l2=(c+b*(b+2)*d)/((b+2)*(b+c))
P=b*(b+2)**3*d**2-b*(b+2)*(4+3*b+c)*d +(2*b+b*b-b*c-c*c)
l4=c*P/((b+2)**3*(b+c)**3)
assert sp.factor(sp.expand(F_formula.subs(L,l2*x+l4*x*x)).coeff(x,1))==0
assert sp.factor(sp.expand(F_formula.subs(L,l2*x+l4*x*x)).coeff(x,2))==0
assert sp.factor(sp.discriminant(P,d)-b*(b+2)**2*(b+c)**2*(8+5*b))==0
Dm=(4+3*b+c-(b+c)*sp.sqrt((8+5*b)/b))/(2*(b+2)**2)
Dp=(4+3*b+c+(b+c)*sp.sqrt((8+5*b)/b))/(2*(b+2)**2)
assert sp.simplify(sp.factor(P.subs(d,Dm)))==0
assert sp.simplify(sp.factor(P.subs(d,Dp)))==0
assert sp.factor(sp.diff(l4,d,2)/2 - b*c/(b+c)**3)==0
Krate=sp.factor(6*l4/l2**2)
assert sp.factor(Krate.subs({b:1,c:1}) - (27*d*d-24*d+1)/(3*d+1)**2)==0
assert sp.factor(Dm.subs({b:1,c:1})-(4-sp.sqrt(13))/9)==0
assert sp.factor(Dp.subs({b:1,c:1})-(4+sp.sqrt(13))/9)==0

# Independent stationary occupation-time variance gives the leading d^2 coefficient.
# For the passive indicator I(t), its stationary autocovariance is bc/(b+c)^2 exp(-(b+c)t).
# Thus Var(integral I) / t tends to 2bc/(b+c)^3 and the Gaussian mixture's
# fourth cumulant coefficient in d^2 is 12*(2bc/(b+c)^3) = 24bc/(b+c)^3.
assert sp.factor((24*sp.diff(l4,d,2)/2)-24*b*c/(b+c)**3)==0

# Independent transform: the published scalar renewal propagator and Markov resolvent agree.
z=sp.symbols('z')
B=z*sp.eye(3)-Q-sp.diag(sp.I*k,-sp.I*k,-d*k*k)
init=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2),0]])
resolvent=sp.factor((init*B.inv()*sp.ones(3,1))[0])
renewal=(z+b+2)*(z+b+c+d*k*k)/(((z+b)*(z+b+2)+k*k)*(z+c+d*k*k)-b*c*(z+b+2))
assert sp.factor(resolvent-renewal)==0
# Verify the exact equal-rate published Eq. (55)/(66).
r=sp.symbols('r')
eq55=(r+z+2)*(d*k*k+2*r+z)/(d*k*k*(k*k+(r+z)*(r+z+2))+k*k*(r+z)+z*(r+z+2)*(2*r+z))
assert sp.factor(renewal.subs({b:r,c:r})-eq55)==0

# Independently propagate the first four finite-time raw moments with forward generator.
def finite_moments(B,C,D,t):
    Qv=np.array([[-1-B,1,B],[1,-1-B,B],[C/2,C/2,-C]],float)
    mat=np.zeros((15,15),float)
    vv=np.diag([1.,-1.,0.]); dd=np.diag([0.,0.,D])
    for n in range(5):
        mat[n*3:n*3+3,n*3:n*3+3]=Qv.T
        if n>=1: mat[n*3:n*3+3,(n-1)*3:(n-1)*3+3] = n*vv
        if n>=2: mat[n*3:n*3+3,(n-2)*3:(n-2)*3+3] = n*(n-1)*dd
    start=np.zeros(15)
    start[:3]=[C/(2*(B+C)),C/(2*(B+C)),B/(B+C)]
    end=expm(mat*t)@start
    moments=[sum(end[n*3:n*3+3]) for n in range(5)]
    var=moments[2]-moments[1]**2
    fourth=moments[4]-4*moments[1]*moments[3]+6*moments[1]**2*moments[2]-3*moments[1]**4
    return var, fourth/var**2-3

checks=0
for B,C,Ds in [(1.,1.,[0.0,0.02,0.2,0.5,1.0,3.0]),(0.4,1.1,[0.,.1,.3,2.]),(2.3,0.5,[0.,.1,.4,1.])]:
    for D in Ds:
        theo=float(sp.N(l2.subs({b:B,c:C,d:D})))
        coef=float(sp.N(Krate.subs({b:B,c:C,d:D})))
        for t in (15.,45.,100.):
            var,kurt=finite_moments(B,C,D,t)
            assert np.isfinite(var+kurt)
            assert abs(var/(2*t)-theo)<max(.08, .08*theo)
            # Finite-time approach to coefficient; bound explicitly pre-asymptotic correction.
            if t==100.: assert abs(t*kurt-coef)<max(1.5,.25*abs(coef)+.3)
            checks+=1
print('PASS: symbolic determinant, coefficient, discriminant, roots, exact renewal transform and',checks,'finite-time semigroup checks')
for D in (0.0,0.02,.2,.5,1.0):
    var,ku=finite_moments(1.,1.,D,100.)
    print('b=c=1, D=',D,'100*t kurt=',100*ku,'asymptote=',float(Krate.subs({b:1,c:1,d:D})))
