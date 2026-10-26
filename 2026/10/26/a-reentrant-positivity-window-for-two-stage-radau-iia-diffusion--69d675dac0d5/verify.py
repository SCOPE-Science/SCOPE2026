"""Exact checks for Radau IIA diffusion on square rook graphs.
Run: python verify.py (requires SymPy >=1.12).
"""
import sympy as S
from fractions import Fraction
x,q=S.symbols('x q', positive=True)
R=lambda t:(6-2*t)/(t*t+4*t+6)
den=(x*x+4*x+6)*(2*x*x+4*x+3)
D=2*x**4+(18-4*q-2*q*q)*x**3+(18+18*q-5*q*q)*x*x+36*q*x+18*q*q
F=2*x**3+(18-2*q)*x**2+(18+9*q)*x+18*q
assert S.simplify(1+2*(q-1)*R(x)+(q-1)**2*R(2*x)-D/den)==0
assert S.simplify(1+(q-2)*R(x)-(q-1)*R(2*x)-x*F/den)==0
assert S.simplify(1-2*R(x)+R(2*x)-2*x*x*(x*x+9*x+9)/den)==0
assert S.factor(D.subs(q,3)- (2*x*x*(x-3)**2+9*x*x+108*x+162))==0
assert S.factor(D.subs(x,q)+q*q*(2*q**3+7*q*q-36*q-72))==0
assert S.factor(D.subs(x,6)+594*(q*q-12))==0
assert S.factor(F-(2*x*(x*x+9*x+9)+q*(2*x+3)*(6-x)))==0
assert S.simplify(2*(x*x+9*x+9)-(2*x+3)*(x-6)-(27*x+36))==0
assert S.factor(S.limit(D/q**2,q,S.oo)+(2*x-3)*(x*x+4*x+6))==0
# Separate direct rational functional calculus, not derived from spectral projectors.
count=0
for size,steps in [(2,[S.Rational(1,4),1,2,7]),(3,[S.Rational(1,3),1,4,9]),(4,[S.Rational(1,8),1,2,7]),(5,[S.Rational(1,10),1,2]),(6,[S.Rational(1,12),1])]:
    n=size*size
    adjacency=S.zeros(n)
    for u in range(n):
        i,j=divmod(u,size)
        for v in range(n):
            if u==v:continue
            k,l=divmod(v,size)
            if (i==k) != (j==l):adjacency[u,v]=1
    L=2*(size-1)*S.eye(n)-adjacency
    eye=S.eye(n)
    for h in steps:
        transition=(6*eye+4*h*L+h*h*L*L).inv()*(6*eye-2*h*L)
        xx=size*h
        for u in range(n):
            i,j=divmod(u,size)
            assert sum(transition[u,v] for v in range(n)) == 1
            for v in range(n):
                k,l=divmod(v,size)
                if u==v: numerator=D.subs({q:size,x:xx})
                elif (i==k) or (j==l):numerator=xx*F.subs({q:size,x:xx})
                else:numerator=2*xx*xx*(xx*xx+9*xx+9)
                expected=numerator/(size*size*den.subs(x,xx))
                assert S.cancel(transition[u,v]-expected)==0,(size,h,u,v)
                count+=1
# Rigorous exact examples and sharp crossover at q=4.
assert S.factor(D.subs({q:4,x:4})/(16*den.subs(x,4)))==-S.Rational(4,323)
for size in range(4,31):
    assert D.subs({q:size,x:size}) < 0
print('VERIFY_OK: 7 polynomial identities; exact R(L) entry replay',count,'entries; q=4 witness -4/323; 27 exact q-witnesses')
