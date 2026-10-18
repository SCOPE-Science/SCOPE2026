#!/usr/bin/env python3
"""Symbolic check of a local Hopf normal-form identity for a specified quadratic flow.
Requires SymPy. Run: python3 check.py
"""
import sympy as S
I=S.I
s=S.symbols('s',positive=True,real=True)
rt=S.sqrt(3); D=121+3*s*s; w=2*rt*s
X,Y,Z,lam=S.symbols('X Y Z lam')
b,k=S.symbols('b k',positive=True,real=True)
state=S.Matrix([X,Y,Z])
flow=S.Matrix([12*(Y-X),-10*Y-X*Z,Y**2-b+k*X*Y])
E=S.Matrix([S.sqrt(b/(k+1)),S.sqrt(b/(k+1)),-10])
assert all(S.simplify(z)==0 for z in flow.subs(dict(zip(state,E))))
J=flow.jacobian(state).subs(dict(zip(state,E)))
poly=S.expand(J.charpoly(lam).as_expr())
expect=lam**3+22*lam**2+b*(k+2)/(k+1)*lam+24*b
assert S.simplify(poly-expect)==0
assert S.simplify((22*b*(k+2)/(k+1)-24*b)-2*b*(10-k)/(k+1))==0
assert S.expand(expect.subs(k,10)-(lam+22)*(lam**2+12*b/11))==0
# Real part of implicit eigenvalue derivative at the imaginary crossing.
cross=44*b/(121*(1936+48*s*s))
assert S.cancel(cross.subs(b,11*s*s)-11*s*s/(5324+132*s*s))==0
A=S.Matrix([[-12,12,0],[10,-10,-s],[10*s,12*s,0]])
q=S.Matrix([(3*s+11*rt*I)/D,(-5*s+rt*I*(s*s+22))/(2*D),1])
p=S.Matrix([5*rt*I/3,2*rt*I,1])
assert all(S.cancel(v)==0 for v in A*q-I*w*q)
assert all(S.cancel(v)==0 for v in A.T*p+I*w*p)
assert S.cancel((p.conjugate().T*q)[0]-2)==0
# Quadratic Hessian of the vector field, with k=10.
def B(v,t):
    return S.Matrix([0,-(v[0]*t[2]+v[2]*t[0]),2*v[1]*t[1]+10*(v[0]*t[1]+v[1]*t[0])])
qb=q.conjugate()
r1=S.Matrix([(s*s+132)/(44*s*D),(s*s+132)/(44*s*D),6/D])
assert all(S.cancel(v)==0 for v in A*r1-B(q,qb))
# A closed 2-by-2 elimination, independent of generic matrix inversion.
Bqq=B(q,q); C=1+I*w/6; P=-10+(10+2*I*w)*C; Q=-10-12*C
rx=(s*Bqq[2]-2*I*w*Bqq[1])/(s*s*Q-2*I*w*P)
r2=S.Matrix([rx,C*rx,(Bqq[1]-P*rx)/s])
assert all(S.cancel(v)==0 for v in (2*I*w*S.eye(3)-A)*r2-Bqq)
# q_z=1 and <p,q>=2; divide the adjoint vector by 2.
g21=(p.conjugate().T*(B(qb,r2)-2*B(q,r1)))[0]/2
l1=S.cancel((g21+S.conjugate(g21))/(4*w))
target=rt*s*(61*s*s+23364)/(96*D*D*(12*s*s+121))
assert S.cancel(l1-target)==0
assert l1.subs(s,S.Rational(1,2))>0
assert l1.subs(s,S.Integer(1))>0
assert l1.subs(s,S.Integer(3))>0
# Positivity at every s>0 follows directly from the positive factorization.
print('PASS: equilibrium, Jacobian spectrum, crossing and Hopf coefficient')
print('l1(b=100) =',target.subs(s,S.sqrt(S.Rational(100,11))).evalf(18))
