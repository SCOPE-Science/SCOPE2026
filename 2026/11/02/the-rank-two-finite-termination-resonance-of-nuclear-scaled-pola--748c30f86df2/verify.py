"""Standalone arithmetic and matrix checks for the nuclear-scaled polar iteration theorem.

Use: python verify.py (requires numpy for dense matrix tests).
Finite tests are corroboration, not a substitute for the theorem's proof.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np

checks = 0

def checked(condition, message):
    global checks
    assert bool(condition), message
    checks += 1


def singular_step(values, t):
    values = tuple(F(v) for v in values)
    shift = F(t) * sum(values)
    return tuple(abs(v - shift) for v in values)

# Exact exhaustive rational rank-two checks, independent of matrix SVD.
for a, b in product(range(1, 41), repeat=2):
    x = (F(a), F(b))
    y = singular_step(x, F(1,2))
    z = singular_step(y, F(1,2))
    checked(z == (0,0), f"rank-two termination failed: {x}")
    checked(y[0] == y[1] == F(abs(a-b),2), f"equalization failed: {x}")

# Nonterminating two-level rays in every rank from three through twenty.
for r in range(3,21):
    s0 = (F(1),)*(r-1) + (F(r-1),)
    s = s0
    c = F(r-2,r)
    for k in range(1,13):
        s = singular_step(s,F(1,r))
        checked(s == tuple(c**k*v for v in s0),f"rank {r}, k {k} ray failed")
        checked(all(v>0 for v in s),f"rank {r}, k {k}: vanished")

# All-equal spectrum obstructs every nonresonant step. Include stable and
# unstable rational choices, plus the rank-one exact solution.
for r in range(1,15):
    for t in [F(1,7),F(1,2),F(3,4),F(4,3)]:
        if t != F(1,r):
            s=(F(1),)*r
            for k in range(1,8):
                s=singular_step(s,t)
                checked(s == (abs(1-r*t)**k,)*r,f"equal spectrum r={r} t={t} k={k}")
                checked(all(v != 0 for v in s),f"nonresonance failure r={r} t={t}")
checked(singular_step((F(9),),F(1,1))==(0,),"rank-one termination")

# Matrix SVD tests: rectangular full-rank-two matrices with arbitrary
# singular-vector orientations; no diagonal simplification used here.
rng = np.random.default_rng(20261025)
for m,n in [(2,2),(2,4),(4,2),(3,5),(5,3),(7,8)]:
    for trial in range(500):
        L,_ = np.linalg.qr(rng.standard_normal((m,2)))
        R,_ = np.linalg.qr(rng.standard_normal((n,2)))
        s = np.array([np.exp(rng.uniform(-2,2)),np.exp(rng.uniform(-2,2))])
        X=L@np.diag(s)@R.T
        Y=X
        for _ in range(2):
            u,sv,vh=np.linalg.svd(Y,full_matrices=False)
            mask=sv > 1.e-11 * max(1.,sv[0])
            Y=Y-0.5*sv[mask].sum()*(u[:,mask]@vh[mask,:])
        checked(np.linalg.norm(Y,'fro') < 2.e-10*np.linalg.norm(X,'fro'),"dense rank-two mismatch")

# Discontinuity example: rank-raising perturbation of diag(3,1,0).
E0=np.diag([3.,1.,0.]); P0=np.diag([1.,-1.,0.]);
for e in [1e-2,1e-4,1e-6,1e-8]:
    E=np.diag([3.,1.,e]); S=4+e
    P=np.diag([3-S/2,1-S/2,e-S/2])
    checked(np.linalg.norm(P-P0,'fro')>1.9,"rank-raising discontinuity")
    checked(abs(np.linalg.norm(P-P0,'fro')-2)<0.01,"limit discontinuity")

# Exact-line-search (rank-adaptive) first-step discontinuity at rank two.
# E0 = diag(3,1,0), Eeps = diag(3,1,eps), with t=1/r.
for q in [F(1,100), F(1,10**4), F(1,10**6)]:
    E0_1=(F(1),F(-1),F(0))
    S=F(4)+q
    Ee_1=(F(3)-S/3,F(1)-S/3,q-S/3)
    delta_sq=sum((a-b)**2 for a,b in zip(Ee_1,E0_1))
    checked(abs(float(delta_sq)-8/3)<0.1,'rank-adaptive finite discontinuity')
checked(F(2,3)**2+F(2,3)**2+F(-4,3)**2==F(8,3),
        'exact rank-adaptive discontinuity squared norm')

print(f"PASS: {checks} independent finite arithmetic/matrix checks")
