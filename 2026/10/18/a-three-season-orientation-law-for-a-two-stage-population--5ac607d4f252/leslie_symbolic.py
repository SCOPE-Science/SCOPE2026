"""Exact algebraic verification of the three-season two-stage projection identity.
Run: python3 leslie_symbolic.py   (requires sympy)
"""
import sympy as S

a = S.symbols('a1 a2 a3')
s = S.symbols('s1 s2 s3')
b = S.symbols('b', positive=True)
M = [S.Matrix([[0,b],[s[i],a[i]]]) for i in range(3)]
A = M[0]*M[1]*M[2]
B = M[0]*M[2]*M[1]
area = S.det(S.Matrix([[1,a[i],s[i]] for i in range(3)]))
assert S.factor(S.trace(A)-S.trace(B)-b*area)==0
assert S.factor(S.det(A)+b**3*s[0]*s[1]*s[2])==0
assert S.factor(S.det(B)+b**3*s[0]*s[1]*s[2])==0
c123=a[0]*s[1]+a[1]*s[2]+a[2]*s[0]
c132=a[0]*s[2]+a[1]*s[0]+a[2]*s[1]
assert S.factor(S.trace(A)-a[0]*a[1]*a[2]-b*c123)==0
assert S.factor(S.trace(B)-a[0]*a[1]*a[2]-b*c132)==0
v={a[0]:S.Rational(1,4),a[1]:S.Rational(1,2),a[2]:S.Rational(3,4),
   s[0]:S.Rational(1,4),s[1]:S.Rational(3,4),s[2]:S.Rational(1,4),b:S.Rational(4,3)}
assert S.trace(A).subs(v)==S.Rational(73,96)
assert S.trace(B).subs(v)==S.Rational(35,32)
assert S.det(A).subs(v)==-S.Rational(1,9)
assert S.det(B).subs(v)==-S.Rational(1,9)
assert S.det(S.eye(2)-A).subs(v)==S.Rational(37,288)
assert S.det(S.eye(2)-B).subs(v)==-S.Rational(59,288)
print('PASS: symbolic oriented-area identity, common determinant, exact persistence flip.')
