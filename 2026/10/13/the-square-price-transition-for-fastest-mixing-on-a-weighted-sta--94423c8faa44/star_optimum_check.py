"""Exact algebraic checks for the distinguished-edge weighted-star optimum.

Requires SymPy. Run: python star_optimum_check.py
"""
from fractions import Fraction
import sympy as S

m,t,z,h = S.symbols('m t z h', positive=True)
r=z*(m-z)/(m+1-2*z)
N=z*(m+1-2*z)
D=(m-1)*(m+1-2*z)+t*z*(m-z)
assert S.simplify(S.diff(N/D,z)*D**2 - (m-1)*((m+1-2*z)**2-t*z**2))==0
zopt=(m+1)/(h+2)
B=m*h**2+2*(m-1)*(h+1)
assert S.simplify((N/D).subs({z:zopt,t:h*h})-(m+1)/B)==0
assert S.simplify((1/(m-1+t*r)).subs({z:zopt,t:h*h})-(h+2)/B)==0
assert S.simplify((r/(m-1+t*r)).subs({z:zopt,t:h*h})-(m*(h+1)-1)/(h*B))==0

def lap(weights):
    k=len(weights)
    A=S.zeros(k+1)
    for j,w in enumerate(weights,1):
        A[0,0]+=w
        A[0,j]-=w
        A[j,0]-=w
        A[j,j]+=w
    return A

x=S.Symbol('x')
cases=0
for k in range(3,9):
    for u,w in [(S.Rational(1,3),S.Rational(1,5)),
                (S.Rational(4,13),S.Rational(4,13)),
                (S.Rational(2,7),S.Rational(6,7))]:
        char=S.factor(lap([w]+[u]*(k-1)).charpoly(x).as_expr())
        expected=x*(x-u)**(k-2)*(x*x-(2*w+k*u)*x+(k+1)*w*u)
        assert S.expand(char-expected)==0
        cases+=1
# Exact Schur-complement Fiedler inequalities for randomly asymmetric feasible weights.
for k in range(3,8):
    for ht in range(1,k+4):
        tval=S.Integer(ht*ht)
        if ht<=k-1:
            wval=uval=S.Rational(1,k-1+ht*ht)
            val=uval
        else:
            den=k*ht*ht+2*(k-1)*(ht+1)
            wval=S.Rational(k*(ht+1)-1,ht*den)
            uval=S.Rational(ht+2,den)
            val=S.Rational(k+1,den)
        assert S.simplify(tval*wval+(k-1)*uval-1)==0
        # Exact PSD in the centered subspace via principal minors of L - lambda P.
        M=lap([wval]+[uval]*(k-1));P=S.eye(k+1)-S.ones(k+1)/(k+1)
        F=M-val*P
        assert all(S.det(F.extract(rows,rows))>=0 for q in range(1,k+2)
                   for rows in __import__('itertools').combinations(range(k+1),q))
        # Perturb two ordinary edges without changing the budget.
        d=uval/S.Integer(5)
        v=[wval,uval+d,uval-d]+[uval]*(k-3)
        Mp=lap(v)
        Fp=Mp-val*P
        # Strictly suboptimal means at least one negative principal minor on centered space.
        assert any(S.det(Fp.extract(rows,rows))<0 for q in range(1,k+2)
                   for rows in __import__('itertools').combinations(range(k+1),q))
        cases+=1
print('VERIFY_OK',cases,'exact cases')
