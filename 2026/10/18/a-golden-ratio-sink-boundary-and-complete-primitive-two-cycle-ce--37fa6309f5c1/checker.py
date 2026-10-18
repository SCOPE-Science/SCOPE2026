"""Exact algebraic verification for the three-dimensional polynomial map period-two theorem.
Run: python checker.py
Python 3 and SymPy required. This checks identities and representative parameters;
the universal root and count arguments are proved in RESULT.md.
"""
from fractions import Fraction
import sympy as sp

T, U, V, a, b, c, y, s, lam = sp.symbols('T U V a b c y s lam', real=True)
checks = 0

def check(expr, expected=0):
    global checks
    difference=sp.simplify(sp.expand(expr - expected))
    valid=all(sp.simplify(e)==0 for e in difference) if isinstance(difference, sp.MatrixBase) else difference==0
    if not valid:
        raise AssertionError(f'identity failed: {expr} vs {expected}')
    checks += 1

# Two-cycle scalar reduction, difference and sum constraints.
G = lambda z, t: t*z+z**3
check(sp.expand((G(U,T)-V) - (G(V,T)-U)), (U-V)*(T+U**2+U*V+V**2+1))
check(sp.expand((G(U,T)-V) + (G(V,T)-U)), (U+V)*(T+U**2-U*V+V**2-1))
# Rescaling in the original three-dimensional map.
x,z = sp.symbols('x z')
F = lambda xx,yy,zz,aa,bb,cc: sp.Matrix([aa*yy**2,bb*yy*(1-zz),cc*(1-xx)])
K = a*b*c
P0 = sp.Matrix([a*V**2/K,U/sp.sqrt(K),c*(1-a*U**2/K)])
P1 = sp.Matrix([a*U**2/K,V/sp.sqrt(K),c*(1-a*V**2/K)])
# Use scaled coordinates as y=U/sqrt(K) so F(P0)[1]=G(U,b*(1-c))/sqrt(K).
check(sp.simplify(F(*P0,a,b,c)[1]*sp.sqrt(K)),G(U,b*(1-c)))
check(sp.simplify(F(*P1,a,b,c)[1]*sp.sqrt(K)),G(V,b*(1-c)))
for i in (0,2):
    check(sp.simplify(F(*P0,a,b,c)[i]),P1[i])
    check(sp.simplify(F(*P1,a,b,c)[i]),P0[i])

# General Jacobian and period-two determinant.
J = sp.Matrix([[0,2*a*y,0],[0,-1,-b*y],[-c,0,0]])
D = sp.diag(1,-1,1)
check(J.det(),2*a*b*c*y**2)
check(sp.expand((lam*sp.eye(3)-D*J).det()),lam**3-lam**2+2*a*b*c*y**2)
check(sp.simplify(D*J*D),J.subs(y,-y))

r = sp.symbols('r',positive=True)
check(sp.expand((lam+r)*(lam**2-(1+r)*lam+r*(1+r))),lam**3-lam**2+r**2*(1+r))
rc=(sp.sqrt(5)-1)/2
sc=rc/2
check(rc*(rc+1),1)
check(sc,(sp.sqrt(5)-1)/4)

# Explicit exact-radical representatives in all phase regions.
parameters = [sp.Rational(1,2),sp.Rational(0),sp.Rational(-1),
 sp.Rational(-9,8),sp.Rational(-5,4),sp.Rational(-3,2),
 sp.Rational(-2),sp.Rational(-5,2),sp.Rational(-3),sp.Rational(-4)]
for tval in parameters:
    bb=sp.Integer(1)
    cc=1-tval
    aa=1/cc
    kval=aa*bb*cc
    check(kval,1)
    cycle_pairs = []
    if tval < -1:
        v0=sp.sqrt(-tval-1)
        cycle_pairs.append((v0,-v0))
    if tval < -2:
        discriminant=sp.sqrt(tval**2-4)
        hi=sp.sqrt((-tval+discriminant)/2)
        lo=1/hi
        cycle_pairs.extend([(hi,-lo),(-hi,lo)])
    expected_count = 0 if tval>=-1 else (1 if tval>=-2 else 3)
    check(len(cycle_pairs),expected_count)
    for u,v in cycle_pairs:
        check(sp.simplify(G(u,tval)),v)
        check(sp.simplify(G(v,tval)),u)
        point0=sp.Matrix([aa*v**2,u,cc*(1-aa*u**2)])
        point1=sp.Matrix([aa*u**2,v,cc*(1-aa*v**2)])
        for i in range(3):
            check(sp.simplify(F(*point0,aa,bb,cc)[i]),point1[i])
            check(sp.simplify(F(*point1,aa,bb,cc)[i]),point0[i])
        # The Jacobian determinant product for any two-cycle is 4(u v)^2.
        JJ=lambda pp:sp.Matrix([[0,2*aa*pp[1],0],
               [0,bb*(1-pp[2]),-bb*pp[1]],[-cc,0,0]])
        return_matrix=JJ(point1)*JJ(point0)
        check(sp.simplify(return_matrix.det()),4*(u*v)**2)
        if sp.simplify(u+v) == 0:
            check(sp.simplify((lam*sp.eye(3)-D*JJ(point0)).det()),lam**3-lam**2+2*u**2)
        else:
            check(return_matrix.det(),4)
print(f'PASS: {checks} exact algebraic/radical identities; ten rational phase representatives.')
