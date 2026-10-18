"""Independent spectrum and algebra checks for fastest mixing on complete-graph coronas.

Run: python verify.py  (requires NumPy and SymPy).
Finite checks complement, but do not replace, the analytic all-orders proof.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp


def parameters(m):
    assert isinstance(m, int) and m >= 3
    s = math.sqrt(m * (m-1))
    d = 5*m*m - 8*m + 4
    p = (m*m + (m-2)*s)/d
    q = (1-p)/(m-1)
    mu = 2*((m-2)*(m-1)+m*s)/d
    return p,q,mu


def matrix(m,p,q):
    t = 2*m
    W = np.zeros((t,t),dtype=float)
    for i in range(m):
        W[i,m+i] = W[m+i,i] = p
        for j in range(i):
            W[i,j] = W[j,i] = q
    for i in range(t):
        W[i,i] = 1-float(np.sum(W[i]))
    return W


def slem(W):
    eig = np.linalg.eigvalsh(W)
    return max(abs(float(eig[0])),abs(float(eig[-2])))


m = sp.symbols('m',integer=True,positive=True)
c = m/(2*(m-1))
a = 1-c
d = 5*m*m-8*m+4
z = sp.sqrt(m*(m-1))
p = (m*m+(m-2)*z)/d
mu = 2*((m-2)*(m-1)+m*z)/d
assert sp.simplify(sp.radsimp(mu-(a+sp.sqrt(2*c**3))/(1+c*c))) == 0
assert sp.simplify(sp.radsimp(p-(1-(1-a*mu)/(2*c)))) == 0
assert sp.simplify((1+c*c)*mu**2-2*a*mu+1-2*c) == 0
symbolic_checks = 3

for M in range(3,61):
    P,Q,U=parameters(M)
    assert 0 < P < 1 and Q > 0 and U < 1
    W = matrix(M,P,Q)
    assert np.min(W)>=-2e-14 and np.max(np.abs(np.sum(W,axis=1)-1))<2e-14
    assert np.linalg.norm(W-W.T,ord=np.inf)<1e-14
    # Direct dense matrices independent of the spectral-block derivation.
    assert abs(slem(W)-U)<4e-12,(M,slem(W),U)
    eig=np.linalg.eigvalsh(W)
    assert np.sum(abs(eig-U)<1e-10)>=M-1
    # The calculated positive spectral branch bounds every other nontrivial eigenvalue.
    a_=1-M*Q/2-P
    eplus=a_+math.hypot(P,M*Q/2)
    eminus=a_-math.hypot(P,M*Q/2)
    assert abs(eplus-U)<3e-13
    assert abs(1-2*P)<=U+4e-13 and abs(eminus)<=U+4e-13

# Noninvariant feasible matrices: each tested objective is bounded by the theorem.
rng=np.random.default_rng(7819)
random_tests=0
for M in range(3,11):
    base=matrix(M,*parameters(M)[:2])
    opt=parameters(M)[2]
    for _ in range(50):
        E=rng.uniform(0,1,(2*M,2*M))
        E=(E+E.T)/2
        W=np.zeros_like(E)
        for i in range(2*M):
            for j in range(i):
                if base[i,j]>0:
                    W[i,j]=W[j,i]=E[i,j]
        W*=0.99/max(1,np.max(np.sum(W,axis=1)))
        for i in range(2*M):
            W[i,i]=1-np.sum(W[i])
        assert np.min(W)>=-1e-14
        assert slem(W)>=opt-1e-11
        random_tests+=1

print('VERIFY_OK', 'symbolic_identities',symbolic_checks,
      'full_dense_orders',58, 'random_feasible_matrices',random_tests)
