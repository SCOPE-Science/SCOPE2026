from sympy import Matrix, Rational, sqrt, I, symbols, factor, discriminant, diff, re, simplify, conjugate, eye, expand

a = symbols("a", positive=True, real=True)
lam = symbols("lam")
x,y,z = symbols("x y z", real=True)
f = Matrix([-a*x+y*z, a*x-x*z, -a*z+x**2+a])
J = f.jacobian([x,y,z])

# Equilibria and characteristic polynomials.
E0={x:0,y:0,z:1}
r=sqrt(a*(a-1))
Ep={x:r,y:r,z:a}
assert all(simplify(v.subs(E0))==0 for v in f)
assert all(simplify(v.subs(Ep))==0 for v in f)
p0=factor(J.subs(E0).charpoly(lam).as_expr())
pm=factor(J.subs(Ep).charpoly(lam).as_expr())
assert expand(p0-(lam+a)*(lam**2+a*lam+1-a))==0
assert expand(pm-(lam**3+2*a*lam**2+a*(2-a)*lam+2*a**2*(a-1)))==0

# Hopf factorization, crossing speed, and cubic discriminant.
a0=Rational(3,2); omega=sqrt(3)/2
assert factor(pm.subs(a,a0)) == (lam+3)*(4*lam**2+3)/4
dlda=simplify(-diff(pm,a)/diff(pm,lam))
assert simplify(re(dlda.subs({a:a0,lam:I*omega}))-Rational(6,13))==0
assert factor(discriminant(pm,lam)) == -4*a**3*(a-1)*(59*a**2-55*a-8)

# First Lyapunov coefficient in the standard Kuznetsov convention.
A=Matrix([[-a0,a0,sqrt(3)/2],[0,0,-sqrt(3)/2],[sqrt(3),0,-a0]])
q=(A-I*omega*eye(3)).nullspace()[0]
p=(A.T+I*omega*eye(3)).nullspace()[0]
inn=(conjugate(p).T*q)[0]
p=simplify(p/conjugate(inn))
assert simplify((conjugate(p).T*q)[0]-1)==0

def B(u,v):
    return Matrix([u[1]*v[2]+u[2]*v[1], -(u[0]*v[2]+u[2]*v[0]), 2*u[0]*v[0]])
qb=conjugate(q)
g21=simplify((conjugate(p).T*(-2*B(q,A.inv()*B(q,qb)) + B(qb,(2*I*omega*eye(3)-A).inv()*B(q,q))))[0])
l1=simplify(re(g21)/(2*omega))
assert simplify(l1 + 2*sqrt(3)/3)==0

# Exact scalar filter identity used for the global half-space statement.
w=symbols('w', real=True)
zdot=-a*z+x**2+a
assert simplify(zdot + a*(z-1) - x**2)==0

print('p0 =', p0)
print('pm =', pm)
print('crossing_speed =', Rational(6,13))
print('first_lyapunov_coefficient =', l1)
print('VERIFY_OK')
