"""Exact symbolic verification of a sampling-moment stability frontier.

Run: python verify.py   (requires SymPy)
All assertions use exact rational arithmetic; no numerical eigenvalue
calculation is used as proof.
"""
import sympy as sp

h, m4 = sp.symbols('h m4', real=True)
p = sp.Rational(4, 3)
d = sp.Integer(1)
A = sp.Matrix([[1-p*h*h/2, h-d*h*h/2], [-p*h, 1-d*h]])
H = [sp.Rational(j, 10) for j in (1, 5, 9, 13, 17)]
w_low = [sp.Rational(j, 40) for j in (7, 12, 2, 12, 7)]
w_high = [sp.Rational(j, 40) for j in (9, 4, 14, 4, 9)]
base = [sp.Matrix([[1, 0],[0, 0]]), sp.Matrix([[0, 1],[1, 0]]), sp.Matrix([[0, 0],[0, 1]])]

def cov_map(weights):
    columns = []
    for X in base:
        Y = sum((w*A.subs(h, hj)*X*A.subs(h, hj).T
                 for hj, w in zip(H, weights)), sp.zeros(2))
        columns.append(sp.Matrix((Y[0,0], Y[0,1], Y[1,1])))
    return sp.Matrix.hstack(*columns)

def raw_moments(weights):
    return [sum((w*hj**j for w, hj in zip(weights, H)), sp.S.Zero)
            for j in range(5)]

ml, mu = raw_moments(w_low), raw_moments(w_high)
assert ml[:4] == mu[:4] == [1, sp.Rational(9,10), sp.Rational(113,100), sp.Rational(1593,1000)]
assert ml[4] == sp.Rational(118501, 50000)
assert mu[4] == sp.Rational(120037, 50000)
assert all(w > 0 for w in w_low + w_high)
assert sum(w_low) == sum(w_high) == 1

Sl = cov_map(w_low)
Su = cov_map(w_high)
S = sp.Matrix([[4*m4/9-sp.Rational(38,75), 2*m4/3-sp.Rational(727,500), m4/4-sp.Rational(463,1000)],
               [sp.Rational(27,125), -sp.Rational(9,250), sp.Rational(3,2000)],
               [sp.Rational(452,225), sp.Rational(46,75), sp.Rational(33,100)]])
assert Sl == S.subs(m4, ml[4])
assert Su == S.subs(m4, mu[4])
assert sp.simplify((sp.eye(3) - S).det() - sp.Rational(24,25)*(sp.Rational(642421,270000)-m4)) == 0
assert sp.Rational(118501,50000) < sp.Rational(642421,270000) < sp.Rational(120037,50000)
assert sp.factor((sp.eye(3) - Sl).det()) == sp.Rational(6289,703125)
assert sp.factor((sp.eye(3) - Su).det()) == -sp.Rational(14447,703125)

P = sp.Matrix([[sp.Rational(8175625,25156), sp.Rational(3909625,100624)],
               [sp.Rational(3909625,100624), sp.Rational(25955165,402496)]])
assert P[0,0] > 0 and P.det() == sp.Rational(2590980634375,133226176) > 0
assert P - sum((w * A.subs(h,hj).T * P * A.subs(h,hj)
                 for hj,w in zip(H,w_low)), sp.zeros(2)) == sp.eye(2)

# For *arbitrary* positive gains, the coefficient of h^4 in
# A(h) X A(h)^T is (1/4)e1 (p,d) X (p,d)^T e1^T.
pp, dd, x, y, z = sp.symbols('p d x y z', real=True)
Ab = sp.Matrix([[1-pp*h*h/2, h-dd*h*h/2],[-pp*h,1-dd*h]])
X = sp.Matrix([[x,y],[y,z]])
quad = sp.expand( (sp.Matrix([[pp,dd]])*X*sp.Matrix([[pp],[dd]]))[0]/4 )
coef = (Ab*X*Ab.T).applyfunc(lambda a: sp.expand(a).coeff(h,4))
assert coef == sp.Matrix([[quad,0],[0,0]])

print('All exact moment identities, covariance matrices, Lyapunov certificate,')
print('spectral boundary determinant, and universal fourth-order coefficient verified.')
print('Threshold:', sp.Rational(642421,270000))
print('Lower/higher fourth moments:', ml[4], mu[4])
