"""Exact symbolic verification for the transverse Veronese-cone identities."""
import sympy as sp

a,b,c,d=sp.symbols('a b c d')
x0=a*b**2; x1=b*c*d; x3=a*b*d; x4=b*c; x5=b
x6=b**2*d; x7=a*b+c**2*d
F1=x0**2+x1*x4*x7+x3*x4**2-x5**2*x7**2
F2=x0*x5+x1*x4-x5**2*x7
F3=x0*x1-x3*x4*x5
F4=x1**2+x3*x5**2-x6*x7
assert all(sp.expand(e)==0 for e in (F1,F2,F3,F4))

A,B,C,D,q,s=sp.symbols('A B C D q s', nonzero=True)
t=s**2
F1=A**2+q*B*C+t*C**2-q**2*D**2
F2=A*D+B*C-q*D**2
F3=A*B-t*C*D
U0=A/q
U1=s*C/q
U2=D-U0
U3=B/s-U1
minors=(U0*U2-U1**2, U0*U3-U1*U2, U1*U3-U2**2)
assert all(sp.factor(a-b)==0 for a,b in zip(minors,(F2/q-F1/q**2,F3/(q*s),2*F2/q-F1/q**2)))
r,z=sp.symbols('r z')
standard=(r**3,r**2*z,r*z**2,z**3)
u0,u1,u2,u3=sp.symbols('u0 u1 u2 u3')
assert all(sp.expand(f.subs({u0:r**3,u1:r**2*z,u2:r*z**2,u3:z**3}))==0 for f in (u0*u2-u1**2,u0*u3-u1*u2,u1*u3-u2**2))
print('VERIFY_OK')
