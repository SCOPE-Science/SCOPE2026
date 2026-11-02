"""Reproduce symbolic identities and finite test cases for a Bernoulli stale-gradient recurrence.
Scientific scope: a scalar quadratic and independent zero/one-step gradient delays.
"""
from fractions import Fraction
from random import Random
import sympy as sp

q, z, noise_var = sp.symbols('q z noise_var', positive=True)
A0 = sp.Matrix([[1-z,0],[1,0]])
A1 = sp.Matrix([[1,-z],[1,0]])
b = q*z/(1+q*z)
P = sp.Matrix([[1,-b],[-b,q*z**2]])
delta = z*(q*z**2+z-2)/(1+q*z)
J = sp.diag(1,0)
T = (1-q)*A0.T*P*A0 + q*A1.T*P*A1
assert (T-P-delta*J).applyfunc(sp.factor) == sp.zeros(2)
assert sp.factor(P.det()-q*z**2*(1-q/(1+q*z)**2)) == 0
M = sp.Matrix([
    [(1-q)*(1-z)**2+q, -2*q*z,q*z**2],
    [1-(1-q)*z, -q*z, 0],
    [1,0,0]
])
assert sp.factor((sp.eye(3)-M).det()+z*(q*z*z+z-2)) == 0

# Mean-square stationary covariance for independent mean-zero additive perturbations.
# State moments are [E X_n^2, E X_n X_(n-1), E X_(n-1)^2].
stat = (sp.eye(3)-M).inv()*sp.Matrix([noise_var,0,0])
stationary_u = noise_var*(1+q*z)/(z*(2-z-q*z*z))
assert sp.factor(stat[0]-stationary_u)==0
assert sp.factor(stat[0]-stat[2])==0
assert sp.factor((sp.Matrix([[1,-2*b,q*z*z]]).dot(stat)-sp.Matrix([[1,-2*b,q*z*z]]).dot(M*stat+sp.Matrix([noise_var,0,0]))))==0

# Exact rational branch enumeration compares direct second moments with the moment recursion.
rng = Random(20261030)
cases = 0
for _ in range(480):
    Q = Fraction(rng.randrange(1,20),20)
    Z = Fraction(rng.randrange(1,31),12)
    x0 = Fraction(rng.randrange(-5,6),3)
    xm1 = Fraction(rng.randrange(-5,6),3)
    v = [(Fraction(1),x0,xm1)]
    B = Q*Z/(1+Q*Z)
    C = Q*Z*Z
    d = Z*(Q*Z*Z+Z-2)/(1+Q*Z)
    V=lambda x,y: x*x-2*B*x*y+C*y*y
    initial_v=V(x0,xm1)
    m0 = x0*x0
    for depth in range(1,7):
        w=[]
        for pr,x,y in v:
            w.append((pr*(1-Q),(1-Z)*x,x))
            w.append((pr*Q,x-Z*y,x))
        v=w
        value = sum(pr*V(x,y) for pr,x,y in v)
        new_m0 = sum(pr*x*x for pr,x,y in v)
        assert value-initial_v == d*m0
        initial_v=value
        m0 = new_m0
        cases+=1

# Additional exact identity check on full moment evolution for both stable and unstable choices.
for _ in range(90):
    Q=sp.Rational(rng.randrange(1,19),20)
    Z=sp.Rational(rng.randrange(1,19),10)
    X=sp.Rational(rng.randrange(-5,6),3)
    Y=sp.Rational(rng.randrange(-5,6),3)
    start=sp.Matrix([X*X,X*Y,Y*Y])
    mat=M.subs({q:Q,z:Z})
    p=sp.Matrix([[1,-2*b,q*z*z]]).subs({q:Q,z:Z})
    d=delta.subs({q:Q,z:Z})
    for k in range(7):
        nxt=mat*start
        assert sp.factor((p*nxt)[0]-(p*start)[0]-d*start[0])==0
        start=nxt
        cases+=1

# Numeric stationary covariance and mean-only blind-spot example.
for Q,Z in [(sp.Rational(1,2),sp.Rational(1,2)),(sp.Rational(1,2),sp.Rational(6,5)),(sp.Rational(4,5),sp.Rational(1,1))]:
    st=stat.subs({q:Q,z:Z,noise_var:sp.Rational(3,2)})
    assert all(k.is_finite for k in st)
    assert st[0] > 0
    assert (sp.Matrix([[1,-2*b,q*z*z]]).subs({q:Q,z:Z})*st)[0]>0

q0=sp.Rational(1,2);z0=sp.Rational(3,2)
assert q0*z0*z0+z0 > 2
mean=sp.Matrix([[1-(1-q0)*z0,-q0*z0],[1,0]])
assert mean.det()<1 and (1-mean.trace()+mean.det())>0 and (1+mean.trace()+mean.det())>0
print('PASS: symbolic Lyapunov identity, determinant, stationary variance; exact finite branch and moment tests:',cases)
