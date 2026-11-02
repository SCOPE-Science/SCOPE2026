"""Reproducibility checks for a scalar, Bernoulli-compressed error-control recurrence.

Requires Python 3, sympy, and numpy. All matrices and update rules are defined below.
Exact symbolic identities, rational finite-horizon comparisons, and numerical spectral
sanity checks are independently evaluated. Numerical checks are not infinite proofs.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S
import numpy as np

q, s = S.symbols('q s', positive=True)
A0 = S.Matrix([[1, 0, -s], [1, 1, -1], [0, 0, 1]])
A1 = S.Matrix([[1-s, -s, 0], [0, 0, 0], [1, 1, 0]])
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
bases = []
for i,j in pairs:
    B = S.zeros(3)
    B[i,j] = 1
    B[j,i] = 1
    bases.append(B)
def coordinate_vector(B):
    return S.Matrix([B[i,j] for i,j in pairs])
M = S.Matrix.hstack(*[coordinate_vector(S.expand((1-q)*A0*B*A0.T + q*A1*B*A1.T)) for B in bases])
assert S.factor((S.eye(6)-M).det() - s*q*q*((q-1)*s*s +(7*q-8)*s+6*q-4)) == 0
print('Exact 6x6 second-moment determinant: PASS')

F0 = S.Matrix([[1,-1],[0,1]])
F1 = S.Matrix([[0,0],[1,0]])
P = S.Matrix([[2*q*q,2*q*(q-1)], [2*q*(q-1),2*q*q-3*q+2]]) / (q*(3*q-2))
assert S.simplify(P - (1-q)*F0.T*P*F0 - q*F1.T*P*F1 - S.eye(2)) == S.zeros(2)
assert S.simplify(P.det() - 2*q/(3*q-2)**2)==0
print('Internal-system strict Lyapunov identity and determinant: PASS')

# Verify each case for small horizons by rational path enumeration, independent of M.
def direct(V,c,step):
    x,e,h=V
    if c==0:
        return (x-step*h, e+x-h, h)
    return ((1-step)*x-step*e, F(0), x+e)
def mat_power_moment(prob,step,t):
    Mr = M.subs({q:S.Rational(prob.numerator,prob.denominator),s:S.Rational(step.numerator,step.denominator)})
    state = S.Matrix([1,0,1])
    v=coordinate_vector(state*state.T)
    return Mr**t *v
checks=0
for prob,step in [(F(1,2),F(1,10)),(F(3,4),F(1,10)),(F(3,4),F(1,5)),(F(9,10),F(1,2))]:
    for t in range(7):
        trial = S.zeros(3,3)
        for path in product([0,1],repeat=t):
            z=(F(1),F(0),F(1));weight=F(1)
            for c in path:
                z=direct(z,c,step)
                weight*= prob if c else 1-prob
            zv=S.Matrix([S.Rational(y.numerator,y.denominator) for y in z])
            trial+=S.Rational(weight.numerator,weight.denominator)*(zv*zv.T)
        assert coordinate_vector(trial) == mat_power_moment(prob,step,t)
        checks+=1
print(f'Exact path enumeration versus moment transfer: PASS ({checks} full covariance identities)')

# Strictly internal spectral checks over natural rational parameter points.
for prob,step,stable in [(.5,.01,False),(.5,1.,False),(2./3.,.001,False),(.75,.1,True),(.75,.2,False),(.9,.5,True),(.9,1.,False),(.99,1.,True)]:
    Mn=np.array(M.subs({q:prob,s:step}),float)
    rho=max(abs(np.linalg.eigvals(Mn)))
    assert (rho<1.) == stable,(prob,step,rho)
    print(f'q={prob:.6f}, step={step:.4f}: spectral radius={rho:.10f}; expected stable={stable}')

# Positive root formula, including continuous limit at q=1.
for prob in [S.Rational(7,10),S.Rational(3,4),S.Rational(9,10),S.Rational(99,100),S.Integer(1)]:
    a=1-prob; b=8-7*prob; c=6*prob-4
    critical=2*c/(b+S.sqrt(b*b+4*a*c))
    assert S.simplify(a*critical*critical+b*critical-c)==0
assert S.simplify(2*(6*S.Integer(1)-4)/(8-7+S.sqrt((8-7)**2)))==2
print('Critical-root identity and uncompressed endpoint: PASS')

# The exact invariant-subspace and isolated-eigenvalue calculations used in the proof.
N = A0-S.eye(3)
assert N**3 == S.zeros(3) and N**2 != S.zeros(3) and N.rank()==2
u=S.Matrix([0,1,0]); assert (A1*u)[2] == 1
v=S.Matrix([1,0,1])
primal_square = S.expand((1-q)*(A0*v)[0]**2+q*(A1*v)[0]**2)
assert S.simplify(primal_square-(1-s)**2)==0
assert S.diff(primal_square,s).subs(s,0)==-2
crit=(S.sqrt(129)-11)/2
assert S.simplify((S.eye(6)-M).det().subs({q:S.Rational(3,4),s:crit}))==0
print('Single Jordan chain, irreducibility witness, slow derivative and exact boundary: PASS')
print('ALL CHECKS PASSED')
