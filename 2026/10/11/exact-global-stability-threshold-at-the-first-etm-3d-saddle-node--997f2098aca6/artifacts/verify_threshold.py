from sympy import symbols, Matrix, diag, factor, discriminant, count_roots, oo, Rational, gcd

rho,a,x = symbols('rho a x', real=True)
A = Matrix([[-2,-rho,0],[1,-1,rho],[0,rho,-5]])
W = diag(a,1,2-a)
M = (W*A + A.T*W)/2
F = 3*a**3*rho**2 + 2*a**2*rho**2 - 10*a**2*rho - 40*a**2 - 18*a*rho**2 + 20*a*rho + 85*a - 10
P = 594*rho**8 - 2076*rho**7 - 5948*rho**6 + 20050*rho**5 + 25505*rho**4 - 66100*rho**3 - 63325*rho**2 + 77500*rho + 75000
Q = 8*x**4 + 8*rho*x**3 + (-6*rho**2+10*rho+35)*x**2 + (-4*rho**3+5*rho**2+15*rho)*x + 2*rho**4-5*rho**3-20*rho**2+25*rho+50

assert factor(M.det() + F/4) == 0
assert factor(discriminant(F,a) - 120*P) == 0
assert factor(discriminant(Q,x) - 12000*P) == 0
assert factor(F.subs(a,0) + 10) == 0
assert factor(F.subs(a,2) + 4*rho**2) == 0
assert count_roots(P,0,oo) == 2
I1=(Rational(2188758,10**6),Rational(2188759,10**6))
I2=(Rational(3355161,10**6),Rational(3355162,10**6))
assert count_roots(P,*I1) == 1
assert count_roots(P,*I2) == 1
assert count_roots(F.subs(rho,1),0,2) == 2
assert count_roots(F.subs(rho,Rational(5,2)),0,2) == 0
assert count_roots(F.subs(rho,4),0,2) == 0
assert count_roots(Q.subs(rho,1),-oo,oo) == 0
assert count_roots(Q.subs(rho,Rational(5,2)),-oo,oo) == 2
assert count_roots(Q.subs(rho,4),-oo,oo) == 4
assert gcd(P, factor(Q.subs(x,0))) == 1

# Cubic cancellation for a general symmetric weight matrix.
p11,p22,p33,p12,p13,p23 = symbols('p11 p22 p33 p12 p13 p23')
Ws = Matrix([[p11,p12,p13],[p12,p22,p23],[p13,p23,p33]])
N = Matrix([symbols('y')*symbols('z'), -2*symbols('x')*symbols('z'), symbols('x')*symbols('y')])
xx,yy,zz=symbols('x y z')
N = Matrix([yy*zz,-2*xx*zz,xx*yy])
vec=Matrix([xx,yy,zz])
C=factor((vec.T*Ws*N)[0])
expected = p13*xx**2*yy - 2*p12*xx**2*zz + p23*xx*yy**2 + (p11-2*p22+p33)*xx*yy*zz - 2*p23*xx*zz**2 + p12*yy**2*zz + p13*yy*zz**2
assert factor(C-expected)==0

print('ALL_VERIFY_OK')
print('positive roots of P: exactly 2')
print('rho_1 in (2.188758, 2.188759); rho_2 in (3.355161, 3.355162)')
print('F(a,rho) roots in (0,2): 2 at rho=1, 0 at rho=5/2 and rho=4')
print('Q(x,rho) real roots: 0 at rho=1, 2 at rho=5/2, 4 at rho=4')
print('disc_a F = 120 P; disc_x Q = 12000 P')
