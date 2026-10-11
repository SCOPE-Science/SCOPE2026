import sympy as sp
x,r=sp.symbols('x r', real=True)
p=8*r**3-6*r-1
A=sp.Rational(2,3)*(2*r**2-2*r-1)
B=sp.Rational(8,9)*(r**2-r-1)
C=-sp.Rational(1,9)*(4*r**2-4*r-7)
T4=8*x**4-8*x**2+1
T5=16*x**5-20*x**3+5*x
Q=sp.expand(1+A*x+B*T4+C*T5)
D=sp.Rational(9,2)*(8*r**2-6*r-1)
R=32*r*(3*r-2)*x**2-128*r*(r-1)*x+4*r*(16*r-15)
err=sp.expand(D*Q-(x+1)*(x-r)**2*R)
# identity is modulo p(r)=0
rem=sp.rem(sp.Poly(err,r),sp.Poly(p,r)).as_expr()
assert sp.expand(rem)==0
# A cubic identity modulo p
remA=sp.rem(sp.Poly(3*A**3-3*A-1,r),sp.Poly(p,r)).as_expr()
assert sp.expand(remA)==0
# contact and derivative identities modulo p
for expr in [Q.subs(x,-1),Q.subs(x,r),sp.diff(Q,x).subs(x,r)]:
    rr=sp.rem(sp.Poly(sp.expand(expr),r),sp.Poly(p,r)).as_expr()
    assert sp.expand(rr)==0
# discriminant of residual quadratic modulo p
qa=32*r*(3*r-2); qb=-128*r*(r-1); qc=4*r*(16*r-15)
disc=sp.expand(qb**2-4*qa*qc)
disc_red=sp.factor(sp.rem(sp.Poly(disc,r),sp.Poly(p,r)).as_expr())
assert sp.expand(disc_red + 64*(80*r**2-62*r-13)) == 0
# identify the intended real root and positivity signs numerically
roots=sorted([complex(z) for z in sp.nroots(p)],key=lambda z:z.real)
rv=roots[0].real
assert -1 < rv < -sp.Rational(3,4)
Av=float(A.subs(r,rv)); Bv=float(B.subs(r,rv)); Cv=float(C.subs(r,rv))
assert 1.13 < Av < 1.14
assert float(D.subs(r,rv))>0
assert float(qa.subs(r,rv))>0
assert float((80*r**2-62*r-13).subs(r,rv))>0
print(f'VERIFY_OK r={rv:.15f} A={Av:.15f} B={Bv:.15f} C={Cv:.15f} cubic=3A^3-3A-1 factor_mod_p=1')
