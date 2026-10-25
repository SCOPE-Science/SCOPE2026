"""Finite-state verification of a stationary four-spin identity in a three-temperature Glauber chain."""
from fractions import Fraction
from itertools import product
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve

def stationary(n, gamma):
    Q=lil_matrix((1<<n, 1<<n), dtype=float)
    for z in range(1<<n):
        spins=[1 if z>>i &1 else -1 for i in range(n)]
        for i in range(n):
            rate=1-gamma[i]*spins[i]*(spins[(i-1)%n]+spins[(i+1)%n])/2
            assert rate>0
            zz=z^(1<<i)
            Q[z,zz]+=rate
            Q[z,z]-=rate
    A=Q.T.tolil()
    A[0,:]=1
    rhs=np.zeros(1<<n)
    rhs[0]=1
    p=spsolve(A.tocsr(),rhs)
    assert np.min(p)>0 and abs(sum(p)-1)<1e-9
    assert np.max(abs(Q.T@p))<1e-9
    return p

def expectation(p, subset):
    n=int(round(np.log2(len(p))))
    out=0.0
    for z,w in enumerate(p):
        v=1
        for i in subset: v*=1 if z>>i&1 else -1
        out+=v*w
    return out

a=Fraction(1,2);b=Fraction(1,3); D=16-a*b
v={"01":4*a/D,"02":a*b/D,"03":Fraction(0),"12":4*(a+b)/D,"13":a*b/D,"23":4*b/D,"0123":a*b/D}
v["defect"] = v["0123"] - v["01"]*v["23"]
v["kappa4"] = v["defect"] - v["02"]*v["13"] - v["03"]*v["12"]
print('Exact rational identities',v)
assert v['defect']==Fraction(-1,9025)
assert v['kappa4']==Fraction(-2,9025)
for n in (6,9):
    gamma=[float((0,a,b)[i%3]) for i in range(n)]
    p=stationary(n,gamma)
    for key,val in v.items():
        if not key.isdigit():continue
        got=expectation(p,tuple(map(int,key)))
        assert abs(got-float(val))<3e-11,(n,key,got,val)
    print(f'finite ring n={n}: stationary residual and seven analytic observables PASS')
for n in (6,9):
    gamma=[(1e-6,0.5,1/3)[i%3] for i in range(n)]
    p=stationary(n,gamma)
    four=expectation(p,(0,1,2,3))
    pair=expectation(p,(0,1))*expectation(p,(2,3))
    defect=four-pair
    assert defect <= -1/9025+16e-6 + 2e-10,(n,defect)
    assert defect<0,(n,defect)
    print(f'finite ring n={n}: three distinct finite bath parameters, strict negative defect {defect:.12f} PASS')
print('All assertions passed')