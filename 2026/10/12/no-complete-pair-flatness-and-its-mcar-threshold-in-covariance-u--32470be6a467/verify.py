"""Reproduce the flatness, full-rank witness, ridge identity, and MCAR mask probability."""
import math
import numpy as np
from numpy.linalg import inv, matrix_rank, eigvalsh

def covariance(x):
    x=np.asarray(x,dtype=float)
    centered=x-x.mean(axis=0)
    return centered.T@centered/(len(x)-1)

def active_pairs(mask):
    return [(i,j) for i in range(len(mask)) for j in range(i+1,len(mask))
            if mask[i] or mask[j]]

def objective(x,pairs,ridge=0.0):
    p=x.shape[1]
    W=inv(covariance(x)+ridge*np.eye(p))
    return sum(float((x[i]-x[j])@W@(x[i]-x[j])) for i,j in pairs)

n,p=6,2
base=np.array([[0.,1.],[2.,0.],[0.,2.],[4.,0.],[0.,4.],[5.,0.]])
missing=[(0,),(1,),(0,),(1,),(0,),(1,)]
pairs=active_pairs([bool(m) for m in missing])
assert len(pairs)==n*(n-1)//2
B=[]
for i,j in pairs:
    for dim in range(p):
        row=np.zeros(n)
        if dim in missing[i]: row[i]+=1
        if dim in missing[j]: row[j]-=1
        B.append(row)
assert matrix_rank(np.array(B))==n
first=base.copy()
for dim in range(p):
    flag=np.array([dim in m for m in missing])
    first[flag,dim]=first[~flag,dim].mean()
assert np.linalg.det(covariance(first))>1e-9

completions=[]
for imputed in ([0.5,3.5,8.0,4.2,1.5,-1.4],
                [7.0,-4.0,2.0,3.3,-2.0,9.5]):
    x=base.copy()
    x[range(n),[m[0] for m in missing]]=imputed
    completions.append(x)
assert not np.allclose(completions[0],completions[1])
for x in completions:
    S=covariance(x)
    assert np.linalg.det(S)>1e-9
    assert abs(objective(x,pairs)-n*(n-1)*p)<1e-9
    for ridge in (0.03,0.4):
        expected=n*(n-1)*sum(z/(z+ridge) for z in eigvalsh(S))
        assert abs(objective(x,pairs,ridge)-expected)<1e-9

N,dimension,q=1599,45,0.2
r=(1-q)**dimension
flat_prob=(1-r)**N+N*r*(1-r)**(N-1)
assert abs(flat_prob-0.9976857362296532)<1e-12

# In the critical dimension window, the exact binomial formula approaches
# the Poisson zero-or-one probability with mean lambda=N*(1-q)^dimension.
for N,dimension in ((10000,80),(10000,41),(10000,20)):
    r=(1-q)**dimension
    lam=N*r
    prob=(1-r)**N+N*r*(1-r)**(N-1)
    assert 0.0<=prob<=1.0
    if lam<0.01: assert prob>0.999
    if lam>100: assert prob<0.00001

print('CHECKS_PASS')
print('n',n,'p',p,'missing_variables',len(missing),'rank_linear_design',matrix_rank(np.array(B)))
print('nonlinear_objective_constant',n*(n-1)*p)
print('mcar_flat_pair_mask_probability',format(flat_prob,'.16f'))
