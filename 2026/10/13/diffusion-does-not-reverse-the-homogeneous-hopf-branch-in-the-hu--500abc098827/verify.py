#!/usr/bin/env python3
import sympy as sp

# Exact H1 witness.
sigma=sp.Integer(1)
a0=sp.Integer(4)
d1=sp.Integer(10)
d2=sp.Rational(1,5)
rho=sp.sqrt(a0*sigma)
mode_ratio=sp.simplify((rho-1)/(d2*rho))
assert mode_ratio == sp.Rational(5,2)

r1=sp.simplify((2*(rho-1)**2/a0 + d2*sp.sqrt(sigma/a0))/(((rho-1)/rho-d2)))
assert r1 == 2
assert d1 > r1

T1=sp.simplify(-(d1+d2) + (rho-1-sigma)/rho)
D1=sp.simplify(2*(rho-1)**2/a0 + d1*(d2-(rho-1)/rho) + d2*sp.sqrt(sigma/a0))
assert T1 == -sp.Rational(51,5)
assert D1 == -sp.Rational(12,5)

# Independent planar Hopf reconstruction at sigma=1, a=4.
x1,x2=sp.symbols('x1 x2', real=True)
u0=sp.Rational(1,2); v0=sp.Rational(1,4)
u=u0+x1; v=v0+x2
f=sp.expand(u*(1-u)-u*(1+4*v)*v)
g=sp.expand(u*(1+4*v)*v-v)
F=sp.Matrix([f,g])
vars=[x1,x2]
zero={x1:0,x2:0}
A=sp.simplify(F.jacobian(vars).subs(zero))
assert A == sp.Matrix([[-sp.Rational(1,2),-sp.Rational(3,2)],[sp.Rational(1,2),sp.Rational(1,2)]])
omega=sp.sqrt(A.det())
assert omega == sp.sqrt(2)/2

B=[[[sp.diff(F[i],vars[j],vars[k]).subs(zero) for k in range(2)] for j in range(2)] for i in range(2)]
C=[[[[sp.diff(F[i],vars[j],vars[k],vars[l]).subs(zero) for l in range(2)] for k in range(2)] for j in range(2)] for i in range(2)]
def Bfun(x,y):
    return sp.Matrix([sum(B[i][j][k]*x[j]*y[k] for j in range(2) for k in range(2)) for i in range(2)])
def Cfun(x,y,z):
    return sp.Matrix([sum(C[i][j][k][l]*x[j]*y[k]*z[l] for j in range(2) for k in range(2) for l in range(2)) for i in range(2)])
I=sp.I
q=(A-I*omega*sp.eye(2)).nullspace()[0]
praw=(A.T+I*omega*sp.eye(2)).nullspace()[0]
def inner(p,q):
    return (sp.conjugate(p).T*q)[0]
norm=sp.simplify(inner(praw,q))
p=sp.simplify(praw/sp.conjugate(norm))
assert sp.simplify(inner(p,q)-1)==0
qb=sp.conjugate(q)
term=Cfun(q,q,qb)-2*Bfun(q,A.inv()*Bfun(q,qb))+Bfun(qb,(2*I*omega*sp.eye(2)-A).inv()*Bfun(q,q))
l1=sp.simplify(sp.re(inner(p,term))/(2*omega))
assert l1 == -5*sp.sqrt(2)

# Crossing speed from the source trace formula for sigma=1:
a=sp.symbols('a', positive=True)
trace=(sp.sqrt(a)-2)/sp.sqrt(a)
beta=trace/2
cross=sp.simplify(sp.diff(beta,a).subs(a,4))
assert cross == sp.Rational(1,16)

print('VERIFY_OK')
print('mode_ratio',mode_ratio)
print('r1',r1)
print('T1',T1)
print('D1',D1)
print('l1',l1)
print('crossing_speed',cross)
