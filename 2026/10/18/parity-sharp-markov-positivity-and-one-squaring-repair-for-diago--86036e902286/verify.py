"""Exact reproducibility checks for Padé positivity on reset generators.

Requires Python 3 and SymPy. Every matrix identity is evaluated with exact rationals.
The proof for arbitrary dimensions and Padé degrees is in RESULT.md.
"""
from math import factorial
import sympy as S

Z = S.symbols('z', nonnegative=True)
checks = 0

def check(condition, description):
    global checks
    if condition is not True and condition != S.true:
        raise AssertionError(description)
    checks += 1


def pade_polynomial(m, x):
    return S.expand(sum(S.Rational(factorial(2*m-j)*factorial(m),
                  factorial(2*m)*factorial(m-j)*factorial(j))*x**j
                  for j in range(m+1)))

# Coefficients and the gamma-integral expansion for every tested degree.
for m in range(1, 10):
    p=pade_polynomial(m,Z)
    from_integral=S.expand(sum(S.binomial(m,j)*S.factorial(2*m-j)/S.factorial(2*m)*Z**j for j in range(m+1)))
    check(S.expand(p-from_integral)==0, f'integral coefficients m={m}')
    check(S.expand(p.subs(Z,0))==1, f'normalization m={m}')
    check(S.expand(p.subs(Z,-Z))==pade_polynomial(m,-Z), f'parity m={m}')
    check(S.sign(S.LC(S.Poly(p,Z)))==1, f'leading coefficient m={m}')

# The cubic threshold and strict derivative for the 3-stage Gauss method.
p3=pade_polynomial(3,Z)
r3=p3.subs(Z,-Z)/p3
num=S.factor(S.cancel(S.diff(r3,Z)*p3**2))
check(S.simplify(num+(Z**4-30*Z**2+600)/600)==0,'exact third-order diagonal Padé derivative')
check(S.expand(Z**4-30*Z**2+600-((Z**2-15)**2+375))==0, 'positive quartic factorization')
for n in range(3,12):
    fn=S.expand(120*((n-1)*p3.subs(Z,-Z)+p3))
    target=120*n-60*(n-2)*Z+12*n*Z**2-(n-2)*Z**3
    check(S.expand(fn-target)==0,f'complete graph cubic n={n}')

# Full rational matrix-function formulas and each squaring level.
pis=( (S.Rational(1,2),S.Rational(1,2)),
      (S.Rational(1,3),S.Rational(1,3),S.Rational(1,3)),
      (S.Rational(1,2),S.Rational(1,3),S.Rational(1,6)),
      (S.Rational(1,10),S.Rational(2,10),S.Rational(3,10),S.Rational(4,10)))
for weights in pis:
    n=len(weights)
    e=S.ones(n,1)
    Pi=e*S.Matrix([weights])
    I=S.eye(n)
    Q=Pi-I
    check(Pi*Pi==Pi,f'idempotent for {weights}')
    for m in range(1,7):
        for z in (S.Rational(1,2), S.Rational(3), S.Rational(12)):
            for sq in (0,1,2):
                argument=z/S.Integer(2)**sq
                # Functional calculus via explicit matrix polynomial and inversion.
                def poly_at_matrix(x):
                    return sum((S.Rational(factorial(2*m-j)*factorial(m),
                       factorial(2*m)*factorial(m-j)*factorial(j))*x**j for j in range(m+1)),S.zeros(n))
                num=poly_at_matrix(argument*Q)
                den=poly_at_matrix(-argument*Q)
                out=(den.inv()*num)**(2**sq)
                r=pade_polynomial(m,-argument)/pade_polynomial(m,argument)
                target=Pi+(r**(2**sq))*(I-Pi)
                check(out==target,f'exact functional calculus n={n} m={m} z={z} sq={sq}')
                check(out*S.ones(n,1)==S.ones(n,1),f'row sum n={n} m={m} z={z} sq={sq}')
                if sq>=1 or m%2==0 or weights==(S.Rational(1,2),S.Rational(1,2)):
                    check(all(x>=0 for x in out),f'entrywise positivity n={n} m={m} z={z} sq={sq}')

# Examples forcing negativity for every odd degree, without assuming a uniform threshold.
for m in (1,3,5,7,9):
    p=pade_polynomial(m,Z)
    r=S.limit(p.subs(Z,-Z)/p,Z,S.oo)
    check(r==-1,f'odd stiff limit m={m}')
for m in (2,4,6,8):
    p=pade_polynomial(m,Z)
    r=S.limit(p.subs(Z,-Z)/p,Z,S.oo)
    check(r==1,f'even stiff limit m={m}')
print(f'VERIFIED: {checks} exact symbolic/matrix checks')
