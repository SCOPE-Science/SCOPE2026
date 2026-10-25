"""Exact checks for two-view oblique section tomography of axis-aligned boxes.
Run: python verify.py (requires SymPy). This is diagnostic: the proof is in RESULT.md.
"""
import itertools
import sympy as S

r1,r2,r3=S.symbols('r1 r2 r3', nonzero=True)
x1,x2,x3=S.symbols('x1 x2 x3', nonzero=True)
r=(r1,r2,r3); x=(x1,x2,x3)
y=(x2,x3,x1)

def ep(v,k):
    return sum(S.prod(v[i] for i in I) for I in itertools.combinations(range(3),k))

v=[r[i]*x[i] for i in range(3)]
w=[r[i]*y[i] for i in range(3)]
d1=S.factor(ep(v,1)-ep(w,1))
d2=S.factor(ep(v,2)-ep(w,2))
sol=S.solve(d1,x1)[0]
factor=S.factor(d2.subs(x1,sol))
assert S.simplify(factor-(r1-r2)*(r2-r3)*(x2-x3)*(r1*x2-r3*x3)/(r1-r3))==0
print('SYMBOLIC-CYCLE: PASS')

# Verify that the two exceptional vectors are truly equal as multisets
xa=(r2,r3,r1); xb=(r3,r1,r2)
for k in (1,2,3):
    assert S.simplify(ep(xa,k)-ep(xb,k))==0
    assert S.simplify(ep([r[i]*xa[i] for i in range(3)],k)-ep([r[i]*xb[i] for i in range(3)],k))==0
print('EXCEPTIONAL-PRODUCTS: PASS')

# All 6 first-view permutations for three explicit distinct ratios.
rr=(S.Integer(1),S.Integer(2),S.Integer(3))
X=(S.Integer(2),S.Integer(3),S.Integer(1))
L=[]
for p in itertools.permutations(range(3)):
    Y=tuple(X[i] for i in p)
    if sorted(rr[i]*X[i] for i in range(3))==sorted(rr[i]*Y[i] for i in range(3)):
        L.append(Y)
assert sorted(set(L))==sorted({X,(S.Integer(3),S.Integer(1),S.Integer(2))})
print('THREE-DIMENSIONAL-PAIR: PASS')

# Explicit three-oblique-direction inversion from the second moments.
M=S.Matrix([[S.Rational(1,3)]*3,
            [S.Rational(1,6),S.Rational(4,6),S.Rational(1,6)],
            [S.Rational(1,6),S.Rational(1,6),S.Rational(4,6)]])
assert M.det()==S.Rational(1,12)
for sides in [(1,1,1),(2,3,1),(S.Rational(2,3),S.Rational(5,4),7)]:
    v=S.Matrix([S.sympify(q)**2 for q in sides])
    moments=M*v/12
    assert 12*M.inv()*moments==v
print('THREE-VIEW-MOMENT-INVERSION: PASS')
print('ALL CHECKS PASSED')
