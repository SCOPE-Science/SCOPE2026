#!/usr/bin/env python3
import sympy as sp

a11,a12,a21,sigma = sp.symbols("a11 a12 a21 sigma", nonzero=True, real=True)
mu1 = sigma**2/(2*a21)
mu2 = -a11*sigma**2/(2*a12*a21)
A = sp.Matrix([[a11,a12],[a21,0]])
mu = sp.Matrix([mu1,mu2])
force = sp.Matrix([0,-sigma**2/2])
assert sp.simplify(A*mu+force) == sp.zeros(2,1)

S11 = a12*sigma**2/(2*a11*a21)
S12 = -sigma**2/(2*a21)
S22 = (a11**2-a12*a21)*sigma**2/(2*a11*a12*a21)
Sigma = sp.Matrix([[S11,S12],[S12,S22]])
Q = sp.Matrix([[0,0],[0,sigma**2]])
assert sp.simplify(A*Sigma+Sigma*A.T+Q) == sp.zeros(2,2)

S,x,Sstar,xstar = sp.symbols("S x Sstar xstar", positive=True)
Y = sp.log(S/Sstar)
Z = sp.log(x/xstar)
J = sp.Matrix([Y,Z]).jacobian([S,x])
assert sp.simplify(J.det()-1/(S*x)) == 0

S0v=sp.Integer(4); Dv=sp.Integer(2); mv=sp.Integer(3); av=sp.Integer(1)
Ssv = Dv*av/(mv-Dv); xsv = S0v-Ssv
assert Ssv == 2 and xsv == 2
a11v = sp.simplify(-Dv*(Ssv**2+av*S0v)/((av+Ssv)*Ssv))
a12v = sp.simplify(-mv*xsv/(av+Ssv))
a21v = sp.simplify(mv*av*Ssv/(av+Ssv)**2)
assert a11v == -sp.Rational(8,3)
assert a12v == -2
assert a21v == sp.Rational(2,3)

subs = {a11:a11v,a12:a12v,a21:a21v}
muv = sp.simplify(mu.subs(subs))
Sigmav = sp.simplify(Sigma.subs(subs))
assert muv == sp.Matrix([3*sigma**2/4,-sigma**2])
assert Sigmav == sigma**2*sp.Matrix([[sp.Rational(9,16),-sp.Rational(3,4)],[-sp.Rational(3,4),sp.Rational(19,16)]])
assert sp.simplify(Sigmav.det()-sp.Rational(27,256)*sigma**4) == 0

vz = sp.Rational(19,16)*sigma**2
muz = -sigma**2
mode = sp.simplify(2*sp.exp(muz-vz))
mean = sp.simplify(2*sp.exp(muz+vz/2))
Vx = sp.simplify(sp.exp(vz)-1)
Sxstat = sp.simplify(sp.exp(3*vz)-3*sp.exp(vz)+2)
assert mode == 2*sp.exp(-sp.Rational(35,16)*sigma**2)
assert mean == 2*sp.exp(-sp.Rational(13,32)*sigma**2)

sigv=sp.Rational(15,100)
print("VERIFY_OK")
print("source_mu", muv)
print("source_covariance", Sigmav)
print("mode_sigma_0_15", sp.N(mode.subs(sigma,sigv),16))
print("mean_sigma_0_15", sp.N(mean.subs(sigma,sigv),16))
print("normalized_variance_sigma_0_15", sp.N(Vx.subs(sigma,sigv),16))
print("skewness_statistic_sigma_0_15", sp.N(Sxstat.subs(sigma,sigv),16))
