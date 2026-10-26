"""Reproducible exact checks for a binary-quartic discriminant in characteristic 3.
Requires SymPy. Finite-field points support, but do not replace, the geometric proof.
"""
import itertools
import sympy as sp
A,B,C,D,E,x,s,t,u,v=sp.symbols('A B C D E x s t u v')
vs=(A,B,C,D,E)
f=A*x**4+B*x**3+C*x**2+D*x+E
P=lambda g:sp.Poly(sp.expand(g),*vs, modulus=3).as_expr()
Delta=P(sp.discriminant(f,x))
assert Delta==P((A*E-B*D)**3 +C**2*(A*E-B*D)**2 - C**3*(A*D**2+B**2*E)+A*E*C**4)
J=[P(sp.diff(Delta,z)) for z in vs]
# Triple-root locus L^3 M is the quadric C=0, AE-BD=0.
trip=(s**3*u,s**3*v,0,t**3*u,t**3*v)
assert sp.Poly(Delta.subs(dict(zip(vs,trip)), simultaneous=True),s,t,u,v,modulus=3).is_zero
for j in J:
    assert sp.Poly(j.subs(dict(zip(vs,trip)), simultaneous=True),s,t,u,v,modulus=3).is_zero
# Squares q^2 of quadratic forms form the second singular component.
square=(s**2,2*s*t,t**2+2*s*u,2*t*u,u**2)
assert sp.Poly(Delta.subs(dict(zip(vs,square)), simultaneous=True),s,t,u,modulus=3).is_zero
for j in J:
    assert sp.Poly(j.subs(dict(zip(vs,square)), simultaneous=True),s,t,u,modulus=3).is_zero
sqC=sp.Poly(square[2],s,t,u,modulus=3).as_expr()
sqU=sp.Poly((A*E-B*D).subs(dict(zip(vs,square)), simultaneous=True),s,t,u,modulus=3).as_expr()
assert sqC==t**2-s*u
assert sp.Poly(sqU+s*u*(t**2-s*u),s,t,u,modulus=3).is_zero

# P^4(F3) exhaustive point-support equality.
def prj(points):
    out=set()
    for v in points:
        if not any(v):continue
        k=next(z for z in v if z)
        out.add(tuple((z*pow(k,-1,3))%3 for z in v))
    return out
F3=range(3)
P4=prj(itertools.product(F3,repeat=5))
def eval3(expr, values):return int(expr.subs(dict(zip(vs,values))))%3
sing={p for p in P4 if eval3(Delta,p)==0 and all(eval3(j,p)==0 for j in J)}
Q={p for p in P4 if p[2]==0 and (p[0]*p[4]-p[1]*p[3])%3==0}
V=prj(tuple(int(g.subs({s:S,t:T,u:U}))%3 for g in square) for S,T,U in itertools.product(F3,repeat=3))
assert sing==Q|V, (len(sing),len(Q),len(V),len(sing-(Q|V)),len((Q|V)-sing))
print('PASS: modular quartic discriminant, complete derivatives, triple-root quadric, square locus, scheme intersection, exhaustive P4(F3) singular support.')
print('F3 count:',len(P4),'singular',len(sing),'quadric',len(Q),'squares',len(V),'intersection',len(Q&V))
