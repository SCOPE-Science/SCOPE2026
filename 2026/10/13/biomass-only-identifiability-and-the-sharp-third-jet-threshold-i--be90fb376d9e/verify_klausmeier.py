#!/usr/bin/env python3
"""Exact symbolic checks for one-output Klausmeier inverse identities.
Only standard Python and SymPy are required; no observations or external data.
Run: python verify_klausmeier.py
"""
import sympy as s

u, w, a, m, eps, b = s.symbols('u w a m eps b', positive=True)
y, yp, ypp, yppp = s.symbols('y yp ypp yppp', real=True)
f = u*u*w - m*u
g = a - (1+u*u)*w
lie = lambda expression: s.factor(s.diff(expression,u)*f+s.diff(expression,w)*g)
L1=lie(f)
L2=lie(L1)

B = y + 1/y - yp/y**2
A = ypp/y**2 - 2*yp**2/y**3 + (1+y**2)*yp/y**2
Bdot=s.diff(B,y)*yp+s.diff(B,yp)*ypp
Adot=s.diff(A,y)*yp+s.diff(A,yp)*ypp+s.diff(A,ypp)*yppp

subs={y:u,yp:f,ypp:L1,yppp:L2}
for name,expr in [
 ('input-output identity', A+m*B-a),
 ('derivative identity', Adot+m*Bdot),
 ('recovered initial water', (yp+m*y)/y**2-w),
]:
 assert s.factor(expr.subs(subs))==0, name

# The algebraic obstruction to an entire nonconstant trajectory with B=b.
pf = u**3-b*u**2+u
exprA=s.factor(s.diff(pf/u**2,u)*pf+(1+u**2)*pf/u**2)
assert s.factor(exprA-2*u*(u*u-b*u+1))==0
assert s.diff(exprA,u)!=0

# Every second-order jet admits a parameter perturbation and a positive nearby state.
A0=s.factor(A.subs({y:u,yp:f,ypp:L1}))
B0=s.factor(B.subs({y:u,yp:f,ypp:L1}))
mp=m+eps
wp=w+eps/u
ap=a+eps*B0
assert s.factor(u*u*wp-mp*u-f)==0
fp=u*u*wp-mp*u
gp=ap-(1+u*u)*wp
next2=s.factor(s.diff(fp,u)*fp+s.diff(fp,w)*gp)
# fp uses w, m too; instead derive the second derivative using the new model's symbolic state.
W,M,AA=s.symbols('W M AA')
f_new=u*u*W-M*u
g_new=AA-(1+u*u)*W
second_new=s.diff(f_new,u)*f_new+s.diff(f_new,W)*g_new
assert s.factor(second_new.subs({W:wp,M:mp,AA:ap})-L1)==0

# Reconstruction from a third jet at nonsingular observation times.
B1=s.factor(Bdot.subs(subs))
third_new=s.diff(second_new,u)*f_new+s.diff(second_new,W)*g_new
third_difference=s.factor(third_new.subs({W:wp,M:mp,AA:ap})-L2)
assert s.factor(third_difference+eps*u**2*B1)==0
A1=s.factor(Adot.subs(subs))
assert s.factor(A1+m*B1)==0
points=[(s.Rational(2),s.Rational(1,2),s.Rational(3,2),s.Rational(1,2)),
        (s.Rational(6),s.Rational(1),s.Rational(2),s.Rational(1)),
        (s.Rational(3),s.Rational(3,4),s.Rational(5,4),s.Rational(4,3)),
        (s.Rational(7,3),s.Rational(2,3),s.Rational(2),s.Rational(2,3))]
regular=0
for av,mv,uv,wv in points:
 st={a:av,m:mv,u:uv,w:wv}
 if B1.subs(st):
  assert s.cancel(-A1.subs(st)/B1.subs(st))==mv
  assert s.cancel(A0.subs(st)+mv*B0.subs(st))==av
  regular+=1

# Third-order singularity is not equivalent to a stationary solution.
singular={a:s.Integer(6),m:s.Integer(1),u:s.Integer(2),w:s.Integer(1)}
assert f.subs(singular)==2
assert B1.subs(singular)==0
assert lie(B1).subs(singular)==20

# Positive equilibria have w=m/u and a=m(u+1/u).
assert s.factor(f.subs({w:m/u}))==0
assert s.factor(g.subs({w:m/u,a:m*(u+1/u)}))==0
print('VERIFY_OK input_output=1 derivative_identity=1 no_constant_B_transients=1 two_jet_nonidentifiability=1 regular_three_jet_points=%d singular_nonstationary=1 positive_equilibrium_family=1' % regular)
