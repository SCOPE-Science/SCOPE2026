#!/usr/bin/env python3
"""Exact polynomial and two-cell weak-form verification (SymPy required)."""
import math
import sympy as S

z = S.symbols("z", positive=True)
X, Y = S.symbols("X Y", real=True)
checks = 0

def check(v):
    global checks
    assert v
    checks += 1

# Assemble the period-two upwind DG operator from cell-average and slope tests.
F = S.zeros(4)
G = S.zeros(4)
for j in range(2):
    left = (j - 1) % 2
    F[2*j, 2*j] = -1
    F[2*j, 2*j+1] = -1
    F[2*j, 2*left] = 1
    F[2*j, 2*left+1] = 1
    F[2*j+1, 2*j] = 3
    F[2*j+1, 2*j+1] = -3
    F[2*j+1, 2*left] = -3
    F[2*j+1, 2*left+1] = -3
    G[2*j, 2*j+1] = -2

# Any two-stage order-two tableau has b1+b2=1 and b2*a21=1/2.
full_step = S.eye(4) + z*F + S.Rational(1,2)*z*z*F*G
alternating = S.Matrix([X, Y, -X, -Y])
M = S.Matrix([[1-2*z, -2*z+2*z*z], [6*z, 1-6*z*z]])
pair = M*S.Matrix([X,Y])
target = S.Matrix([pair[0],pair[1],-pair[0],-pair[1]])
for entry in full_step*alternating-target:
    check(S.simplify(entry) == 0)

W = S.diag(1, S.Rational(1,3))
Q = S.simplify(W - M.T*W*M)
Q_exp = S.Matrix([[4*z*(1-4*z),2*z*z*(8*z-3)],
                  [2*z*z*(8*z-3),8*z*z*z*(1-2*z)]])
for entry in Q-Q_exp:
    check(S.simplify(entry) == 0)
check(S.factor(Q.det()) == -4*z**4)
T = 4*z-16*z**2+24*z**3-48*z**4
check(S.simplify(S.trace(W.inv()*Q)-T) == 0)
check(S.simplify((W.inv()*Q).det()+12*z**4) == 0)

# An exact rational energy-increase example at Courant number one tenth.
v = S.Matrix([S.Rational(3,20), 1])
check(S.simplify((v.T*Q.subs(z,S.Rational(1,10))*v)[0] + S.Rational(7,5000)) == 0)
check(S.simplify((M.subs(z,S.Rational(1,10))*v).T*W*(M.subs(z,S.Rational(1,10))*v))[0] > (v.T*W*v)[0])

for n in range(1,501):
    nu = S.Rational(n,247)
    check(Q.subs(z,nu).det() < 0)
    t = float(T.subs(z,nu))
    gain = 1.0 + (math.sqrt(t*t + 48*float(nu)**4) - t)/2
    qf = W.inv()*Q.subs(z,nu)
    eig = sorted(float(S.re(e)) for e in qf.eigenvals().keys())
    check(eig[0] < 0 < eig[1])
    check(math.isclose(gain, 1-eig[0], rel_tol=1e-10, abs_tol=1e-10))

# Rationalized closed form yields an exact leading coefficient.
check(S.limit(24/(S.sqrt((T/z)**2+48*z*z)+T/z), z, 0, dir='+') == 3)

print(f"VERIFICATION_OK: {checks} independent algebraic and finite-domain checks")
