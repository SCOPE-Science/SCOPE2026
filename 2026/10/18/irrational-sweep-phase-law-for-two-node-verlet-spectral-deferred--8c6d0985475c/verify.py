#!/usr/bin/env python3
"""Algebraic and separately implemented numerical checks for two-node Verlet-SDC harmonic stability.

Requires SymPy and mpmath. The density theorem itself is proved analytically.
"""
import sympy as S
import mpmath as mp

R = S.sqrt(3)
z, t = S.symbols('z t')
nodes = [S.Integer(0), (3-R)/6, (3+R)/6]
weights = S.Matrix([[0, S.Rational(1,2), S.Rational(1,2)]])
one = S.ones(3, 1)
assert nodes[1] < nodes[2]

basis = [S.prod((t-nodes[j])/(nodes[i]-nodes[j])
                for j in (1, 2) if j != i) for i in (1, 2)]
Q = S.zeros(3)
for i in (1, 2):
    for j in (1, 2):
        Q[i, j] = S.simplify(S.integrate(basis[j-1], (t, 0, nodes[i])))
Q_expected = S.Matrix([[0, 0, 0],
                       [0, S.Rational(1,4), S.Rational(1,4)-R/6],
                       [0, S.Rational(1,4)+R/6, S.Rational(1,4)]])
assert S.simplify(Q-Q_expected) == S.zeros(3)
E, I = S.zeros(3), S.zeros(3)
for i in (1, 2):
    for j in range(i):
        E[i, j] = nodes[j+1]-nodes[j]
    for j in range(1, i+1):
        I[i, j] = nodes[j]-nodes[j-1]
T = (E+I)/2
Xpre = E*T + E.multiply_elementwise(E)/2
C = Q*Q-Xpre
H = S.simplify(C[1:3, 1:3])
H_expected = S.Matrix([[S.Rational(1,24), S.Rational(1,8)-R/12],
                       [S.Rational(1,24), S.Rational(1,24)]])
assert S.simplify(H-H_expected) == S.zeros(2)
assert S.simplify(S.trace(H)-S.Rational(1,12)) == 0
assert S.simplify(H.det()-(R-1)/288) == 0
assert S.simplify(S.trace(H)**2/(2*H.det())-1-(R-1)/2) == 0

c = S.Matrix([nodes[1], nodes[2]])
q = S.Matrix([[S.Rational(1,2), S.Rational(1,2)]])
a = [S.simplify((-1)**k*(q*H**k*c)[0]) for k in range(13)]
assert a[0] == S.Rational(1,2)
assert S.simplify(a[1]+S.Rational(1,24)-R/72) == 0
assert S.simplify(a[2]-S.Rational(1,192)+5*R/1728) == 0
assert [S.sign(S.N(x,80)) for x in a[1:9]] == [-1,1,1,-1,1,-1,1,1]

w = S.Matrix([[1,0]]*3)
v = S.Matrix([[0,1]]*3)
base = S.Matrix([[1,1],[0,1]])
Pade_a = 1-z/12
Pade_den = Pade_a**2+z/4
R_pade = S.Matrix([[(Pade_a**2-z/4)/Pade_den,Pade_a/Pade_den],
                  [-z*Pade_a/Pade_den,(Pade_a**2-z/4)/Pade_den]])
exact_stage = (S.eye(3)+z*Q*Q).inv()*(w+Q*v)
R_coll = base - z*S.Matrix.vstack(weights*Q*exact_stage, weights*exact_stage)
assert S.simplify(R_coll-R_pade)==S.zeros(2)
assert S.simplify(R_coll.det()-1)==0

stage = w
for k in range(1,7):
    stage = S.simplify((S.eye(3)+z*Xpre).inv()*(w+Q*v-z*C*stage))
    step = base-z*S.Matrix.vstack(weights*Q*stage, weights*stage)
    determinant = S.Poly(S.expand(S.simplify(step.det()-1)), z, extension=R)
    for j in range(k+1):
        assert S.simplify(determinant.coeff_monomial(z**j))==0, (k, j)
    assert S.simplify(determinant.coeff_monomial(z**(k+1))-a[k])==0, k
    assert S.simplify(S.expand(S.trace(step)).coeff(z,1)+1)==0, k

# Second implementation of the stage recurrence at high precision: solve
# the strictly lower-triangular sweep directly, rather than using its inverse.
mp.mp.dps = 90
def M(A):
    return mp.matrix([[mp.mpf(str(S.N(A[i,j],94))) for j in range(A.cols)]
                      for i in range(A.rows)])
QM, XM, CM, oneM, qM = map(M, (Q,Xpre,C,one,weights))
assert abs(mp.det(M(H)) - mp.mpf(str(S.N((R-1)/288,90)))) < mp.mpf('1e-78')
for k in range(1,10):
    zz = mp.mpf('0.03')
    Z = mp.eye(3)+zz*XM
    cols=[]
    for init in ((mp.mpf(1),mp.mpf(0)),(mp.mpf(0),mp.mpf(1))):
        x0,w0=init
        rhs0=oneM*x0+QM*oneM*w0
        old=oneM*x0
        for sweep in range(k):
            rhs=rhs0-zz*CM*old
            curr=mp.matrix(3,1)
            for i in range(3):
                curr[i]=(rhs[i]-sum(Z[i,j]*curr[j] for j in range(i)))/Z[i,i]
            old=curr
        x1=x0+w0-zz*(qM*QM*old)[0]
        w1=w0-zz*(qM*old)[0]
        cols.append((x1,w1))
    B = mp.matrix([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]])
    defect=mp.det(B)-1
    leading=mp.mpf(str(S.N(a[k],90)))*zz**(k+1)
    assert mp.sign(defect)==mp.sign(leading), (k,defect,leading)
    assert abs(defect/leading-1) < mp.mpf('0.3'), (k,defect,leading)
print('PASS: quadrature, Verlet matrices, complex compression, Gauss collocation,')
print('six determinant-leading identities, and nine independent high-precision sweeps')
print('Leading defect signs k=1..9:', [str(S.sign(S.N(t,60))) for t in a[1:10]])
