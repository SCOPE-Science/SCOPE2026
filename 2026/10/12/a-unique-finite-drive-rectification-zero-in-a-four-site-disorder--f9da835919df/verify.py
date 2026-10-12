"""Exact sixteen-state stationary-current certificate for a four-site exclusion chain.

Requires SymPy. Running prints VERIFY_OK on completion.
"""
import sympy as S
from fractions import Fraction

x = S.symbols('x')
q = [S.Integer(1), S.Rational(1, 4), S.Rational(1, 2), S.Integer(1)]
left, right = (1 + x) / 2, (1 - x) / 2
states = [tuple((i >> j) & 1 for j in range(4)) for i in range(16)]
position = {a: i for i, a in enumerate(states)}
Q = S.zeros(16)
for i, a in enumerate(states):
    destinations = []
    t = list(a)
    t[0] = 1-a[0]
    destinations.append((tuple(t), left if not a[0] else 1-left))
    t = list(a)
    t[3] = 1-a[3]
    destinations.append((tuple(t), right if not a[3] else 1-right))
    for j in range(3):
        if a[j] != a[j+1]:
            t = list(a)
            t[j], t[j+1] = t[j+1], t[j]
            destinations.append((tuple(t), q[j] if a[j] else q[j+1]))
    for b, rate in destinations:
        Q[i, position[b]] += rate
        Q[i, i] -= rate
assert all(S.expand(sum(Q[i,j] for j in range(16))) == 0 for i in range(16))
A = Q.T
A[15, :] = S.ones(1, 16)
rhs = S.zeros(16, 1)
rhs[15] = 1
stationary = A.inv() * rhs
assert S.simplify(sum(stationary)-1)==0
assert all(S.simplify(v)==0 for v in Q.T*stationary)
current = sum(stationary[i] * (q[1] if a[1] else -q[2]) for i,a in enumerate(states) if a[1]!=a[2])/2
D = 900*x**6 + 7884*x**5 -326323*x**4-2101164*x**3-478618*x**2+30025544*x+285870765
N = 13777968 +1394687*x+351342*x**2-6089*x**3-1014*x**4
formula = x*N/D
assert S.cancel(current-formula) == 0
z = S.symbols('z')
P=2514276*z**4-1658361577*z**3+207843423093*z**2+15992346284053*z-14990744789037
symmetry=2*x*x*P.subs(z,x*x)/(D*D.subs(x,-x))
assert S.cancel(formula+formula.subs(x,-x)-symmetry)==0
assert P.subs(z,0)<0<P.subs(z,1)
assert 15992346284053-3*1658361577>0
assert 285870765-(7884+326323+2101164+478618+30025544)>0
assert S.factor(symmetry.subs(x,S.Rational(1,2)))==S.Rational(-2788493690453,41358464106269436)
assert S.factor(symmetry.subs(x,S.Rational(99,100)))==S.Rational(2742563650189250089505856910104,127791761309188514069321932127433175)
for a in states:
    i=position[a]
    expected=S.prod((S.Rational(1,2) if j in (0,3) else (S.Rational(4,5) if j==1 else S.Rational(2,3))) if a[j] else (S.Rational(1,2) if j in (0,3) else (S.Rational(1,5) if j==1 else S.Rational(1,3))) for j in range(4))
    assert S.simplify(stationary[i].subs(x,0)-expected)==0
print('VERIFY_OK')
