#!/usr/bin/env python3
"""Exact reproducibility checks for the planar positive-quadrant cutoff."""
import sympy as s

x,y,M,r=s.symbols('x y M r', positive=True)
F=s.Matrix([x*x/(x+M)-x*y, r*y*(1-y/x)])
D=1/(x*y*y)
div=s.simplify(s.diff(D*F[0],x)+s.diff(D*F[1],y))
assert s.simplify(div-(M*x/(x+M)**2-r)/(x*y*y))==0
assert s.expand((x+M)**2-4*M*x-(x-M)**2)==0

mu=s.Rational(1,2); rr=s.Rational(1,4); a=1-mu
E={x:a,y:a,M:mu,r:rr}
J=s.simplify(F.jacobian([x,y]).subs(E))
assert J==s.Matrix([[s.Rational(1,4),-s.Rational(1,2)],[s.Rational(1,4),-s.Rational(1,4)]])
w=s.Rational(1,4)
q=s.Matrix([1,(1-s.I)/2]); p=s.Matrix([(1+s.I)/2,-s.I]); qb=s.conjugate(q)
assert s.simplify(J*q-s.I*w*q)==s.zeros(2,1)
assert s.simplify(J.T*p+s.I*w*p)==s.zeros(2,1)
assert s.simplify(s.conjugate(p).dot(q))==1
assert s.simplify(J.det()-s.Rational(1,16))==0
var_r=s.symbols('var_r',positive=True)
Jvar=s.simplify(F.jacobian([x,y]).subs({x:a,y:a,M:mu,r:var_r}))
assert s.simplify(s.trace(Jvar)-(s.Rational(1,4)-var_r))==0
assert s.diff(s.trace(Jvar)/2,var_r)==-s.Rational(1,2)

def B(u,v):
    return s.Matrix([s.simplify(sum(s.diff(F[k],(x,y)[i],(x,y)[j]).subs(E)*u[i]*v[j]
         for i in range(2) for j in range(2))) for k in range(2)])
def C(u,v,z):
    return s.Matrix([s.simplify(sum(s.diff(F[k],(x,y)[i],(x,y)[j],(x,y)[l]).subs(E)*u[i]*v[j]*z[l]
         for i in range(2) for j in range(2) for l in range(2))) for k in range(2)])
G=C(q,q,qb)-2*B(q,J.inv()*B(q,qb))+B(qb,(2*s.I*w*s.eye(2)-J).inv()*B(q,q))
g21=s.simplify(s.conjugate(p).dot(G))
assert g21==-s.Rational(1,4)-s.Rational(5,12)*s.I, g21
assert s.simplify(s.re(g21)/(2*w))==-s.Rational(1,2)
print('PASS: exact Dulac divergence, sharp square bound, critical spectrum, transversality, and Hopf cubic coefficient')
