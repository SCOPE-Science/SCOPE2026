"""Supplementary numerical and exact-arithmetic checks of rank-one scaling formulas.

Run: python verify.py. Finite tests supplement the analytic theorem, not certify its quantified scope.
"""
import itertools
import math
import numpy as np
from scipy.optimize import minimize
import sympy as sp


def formula(u):
    u = np.asarray(u, dtype=float)
    q = u*u
    S = float(np.sum(q))
    p = np.ones(len(q))
    if S == 0:
        return 1.0, p
    k = int(np.argmax(q))
    M = q[k]; R = S-M
    if M <= R:
        return 1+S,p
    p[k] = (1+M)/(1+R)
    rho = math.sqrt(M*R/((1+M)*(1+R)))
    return (1+rho)/(1-rho),p


def condition(u,p):
    n=len(u)
    A=np.eye(n)+np.outer(u,u)
    B=A/np.sqrt(np.outer(p,p))
    e=np.linalg.eigvalsh(B)
    return float(e[-1]/e[0])

# Test arbitrary real signs, equal/unequal, zero, no-dominant/dominant/boundary.
cases = [
    [0,0], [1,0], [1,1], [2,1], [1,1,1],
    [math.sqrt(2),1,1], [math.sqrt(3),1,1],
    [math.sqrt(7),1,1,1,1,1], [.5,-1,1,1],
    [-3,1,1], [math.sqrt(7),-2,math.sqrt(3)],
    [2,-1,-1,0], [.1,0.2,.3,.4,.5]
]
rng=np.random.default_rng(20261024)
for n in range(2,13):
    for j in range(12):
        u = rng.normal(size=n)*np.exp(rng.uniform(-1,1,size=n))
        cases.append(u)

trial_count=0
max_formula_error=0.0
min_random_margin=1e99
for a in cases:
    u=np.asarray(a,dtype=float)
    value,p=formula(u)
    observed=condition(u,p)
    max_formula_error=max(max_formula_error, abs(value-observed))
    assert np.isclose(value,observed,rtol=1e-10,atol=1e-10), (u,value,observed)
    for j in range(40):
        trial=np.exp(rng.uniform(-2,2,size=len(u)))
        c=condition(u,trial)
        min_random_margin=min(min_random_margin,c-value)
        assert c>=value-1e-9,(u,trial,c,value)
        trial_count+=1

# Numerical optimization against the separately evaluated spectral objective.
num_optimized=0
max_opt_gap=0.0
for u in cases[2:25]:
    u=np.asarray(u,dtype=float)
    n=len(u)
    target,p=formula(u)
    def fun(z):return math.log(condition(u,np.exp(np.r_[0.0,z])))
    opt=minimize(fun,np.log(p[1:]/p[0]),method='Nelder-Mead',
                 options={'maxiter':1500,'xatol':1e-10,'fatol':1e-10})
    kval=math.exp(opt.fun)
    max_opt_gap=max(max_opt_gap,abs(kval-target))
    assert np.isclose(kval,target,rtol=1e-7,atol=1e-8)
    num_optimized+=1

# Exact non-dominant dual witness: q=[1,1,1], unit vectors at angles 0,120,240.
u=sp.ones(3,1)
z=sp.Matrix([[1,0],[-sp.Rational(1,2),sp.sqrt(3)/2],
             [-sp.Rational(1,2),-sp.sqrt(3)/2]])
H=z*z.T/3
A=sp.eye(3)+u*u.T
assert sp.simplify(H*u)==sp.zeros(3,1)
assert H.trace()==1 and H.diagonal()==sp.Matrix([[sp.Rational(1,3)]*3])
assert sp.simplify(A*H-H)==sp.zeros(3)
assert all(v>=0 for v in H.eigenvals())
# Exact dominant witness q=[9,1,1]: scaled two-plane eigenvalues.
u=sp.Matrix([3,1,1]); P=sp.diag(sp.Rational(10,3),1,1)
A=sp.eye(3)+u*u.T
B=sp.diag(*[sp.sqrt(1/x) for x in P.diagonal()]) * A * sp.diag(*[sp.sqrt(1/x) for x in P.diagonal()])
eigs=B.eigenvals();r=sp.sqrt(sp.Rational(3,5))
assert eigs == {1:1, 3*(1+r):1,3*(1-r):1}, eigs

# Exact Jacobi-worse-than-identity example.
u=sp.Matrix([sp.Rational(1,2),1,1,1])
A=sp.eye(4)+u*u.T
P=sp.diag(*A.diagonal())
B=sp.diag(*[sp.sqrt(1/x) for x in P.diagonal()]) * A * sp.diag(*[sp.sqrt(1/x) for x in P.diagonal()])
eigs=B.eigenvals()
expected={sp.Rational(1,2):2,(3+sp.sqrt(sp.Rational(11,5)))/2:1,(3-sp.sqrt(sp.Rational(11,5)))/2:1}
assert eigs==expected,(eigs,expected)
assert (3+sp.sqrt(sp.Rational(11,5))) > sp.Rational(17,4)

print('FORMULA_EIGENVALUE_TESTS',len(cases))
print('MAX_FORMULA_ABSOLUTE_ERROR',format(max_formula_error,'.3g'))
print('ASYMMETRIC_RANDOM_PRECONDITIONERS',trial_count)
print('MIN_RANDOM_GAP_FROM_THEOREM',format(min_random_margin,'.12g'))
print('SEPARATE_NELDER_MEAD_OPTIMIZATIONS',num_optimized)
print('MAX_OPTIMIZATION_ABSOLUTE_GAP',format(max_opt_gap,'.3g'))
print('EXACT_POLYGON_DUAL_CERTIFICATE','PASS')
print('EXACT_DOMINANT_SPECTRUM','PASS')
print('EXACT_JACOBI_WORSE_EXAMPLE','PASS')
