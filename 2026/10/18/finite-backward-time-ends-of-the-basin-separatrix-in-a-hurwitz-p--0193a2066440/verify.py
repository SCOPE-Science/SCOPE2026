"""Reproducible algebra checks and finite trajectory stress tests for the stated planar field.
The numerical tests are not a proof of finite-time singularity or global basin geometry.
"""
from fractions import Fraction as F
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp

r,z,mu=S.symbols('r z mu',real=True)
P=21*r**4-125*r**2+400*z**2+100
u=-mu*r*P/21
v=-z-r**2/10
J=S.Matrix([u,v]).jacobian([r,z])
assert S.simplify(S.trace(J)-(-1-mu*(5*(r**2-S.Rational(25,14))**2+S.Rational(400,21)*z**2-S.Rational(6575,588))))==0
assert S.simplify(P.subs(z,-r*r/10)-25*(r*r-1)*(r*r-4))==0
assert S.simplify(S.det(J.subs({r:1,z:S.Rational(-1,10)})) + S.Rational(150,21)*mu)==0
assert S.simplify(S.det(J.subs({r:2,z:S.Rational(-2,5)})) - S.Rational(600,21)*mu)==0
assert S.simplify(S.trace(J.subs({r:2,z:S.Rational(-2,5)})) +1 + S.Rational(344,21)*mu)==0
assert S.simplify(P.subs(z,0)-(r*r-5)*(21*r*r-20))==0
assert S.simplify(J[0,0].subs({r:1,z:S.Rational(-1,10)})- S.Rational(166,21)*mu)==0
assert S.simplify(J[0,1].subs({r:1,z:S.Rational(-1,10)})-S.Rational(80,21)*mu)==0

completed=0
for m in [0.001,0.02,0.07,0.089]:
    D=np.array(J.subs({r:1,z:-S.Rational(1,10),mu:m})).astype(float)
    evals, evecs=np.linalg.eig(D)
    stable=evecs[:,int(np.argmin(evals.real))].real
    stable/=np.linalg.norm(stable)
    for sign in [-1,1]:
        def rhs(t,Y):
            R,Z=Y
            return [-m*R/21*(21*R**4-125*R*R+400*Z*Z+100),-Z-R*R/10]
        def radius100(t,Y): return Y[0]-100
        radius100.terminal=True; radius100.direction=0
        sol=solve_ivp(rhs,(0,-100000),np.array([1.,-.1])+sign*1.e-7*stable,
                      rtol=2e-9,atol=1e-11,max_step=1,events=radius100)
        assert sol.status==1 and abs(sol.y[0,-1]-100)<1e-3,(m,sign,sol.message,sol.y[:,-1])
        assert np.all(sol.y[0]>0)
        completed+=1
print('VERIFY_OK: symbolic divergence/equilibrium/Jacobian/factorization checks; stable-branch backward-radius crosses 100 in',completed,'noncertifying integrations')
