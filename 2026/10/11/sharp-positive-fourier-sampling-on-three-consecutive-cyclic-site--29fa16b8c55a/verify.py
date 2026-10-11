"""Numerical corroboration of positive quadrature on cyclic roots of unity.

Requires numpy and scipy.  Finite checks do not replace the proof.
"""
from itertools import combinations
from math import cos, pi, gcd
import numpy as np
from scipy.optimize import linprog


def expected(N):
    return 3 if N % 3 == 0 else 4 if N % 2 == 0 else 5


def root(N, j):
    return np.exp(2j * pi * j / N)


def moments(N, inds, weights):
    return np.array([sum(float(w) * root(N, int(j))**k for j, w in zip(inds, weights))
                     for k in (0, 1, 2)], dtype=complex)


def closed_rule(N):
    if N % 3 == 0:
        return [0, N//3, 2*N//3], np.ones(3)/3
    if N % 2 == 0:
        k=N//4
        c=cos(2*pi*k/N)
        d=cos(4*pi*k/N)
        t=1/(2*(1-d))
        return [0,k,N-k,N//2], np.array([-t*(c+d),t,t,t*(c-d)])
    P=np.column_stack([np.ones(N),np.cos(2*pi*np.arange(N)/N),
                       np.sin(2*pi*np.arange(N)/N),
                       np.cos(4*pi*np.arange(N)/N),
                       np.sin(4*pi*np.arange(N)/N)])
    b=np.array([1.,0.,0.,0.,0.])
    r=linprog(np.linspace(0,1,N),A_eq=P.T,b_eq=b,bounds=(0,None),method='highs')
    assert r.success, (N,r.message)
    I=np.flatnonzero(r.x>1e-9)
    return I.tolist(),r.x[I]


def lagrange_weights(N, inds):
    z=[root(N,j) for j in inds]
    ws=[]
    for i, zi in enumerate(z):
        other=[z[j] for j in range(5) if j != i]
        e2=sum(a*b for a,b in combinations(other,2))
        denom=np.prod([zi-z[j] for j in range(5) if j!=i])
        ws.append((zi**2*e2)/denom)
    return np.array(ws,complex)


n_moments=0
n_distinct=0
n_no_four=0
for N in range(3,80):
    inds, ws=closed_rule(N)
    assert len(inds) == expected(N), (N,inds)
    assert len(inds) == len(set(inds)), (N,inds)
    assert np.min(ws)>1e-9, (N,inds,ws)
    assert np.max(abs(moments(N,inds,ws)-[1,0,0])) < 1e-9, (N,inds,ws)
    n_moments += 3
    n_distinct += len(inds)
    if len(inds)==5:
        other=lagrange_weights(N,inds)
        assert np.max(abs(other.imag)) < 1e-8 and np.max(abs(other.real-ws)) < 1e-8, (N,inds,other,ws)

for N in range(5,38):
    if gcd(N,6)!=1:
        continue
    zz=[root(N,i) for i in range(N)]
    for quad in combinations(zz,4):
        e2=sum(a*b for a,b in combinations(quad,2))
        assert abs(e2)>1e-8, (N,quad,e2)
        n_no_four+=1

print('VERIFY_OK')
print('cyclic_orders',77,'moment_identities',n_moments,'rule_nodes',n_distinct)
print('five_node_lagrange_checks',sum(expected(N)==5 for N in range(3,80)))
print('four_node_nonexistence_checks',n_no_four)
print('sample_N',[(N,closed_rule(N)[0],np.round(closed_rule(N)[1],8).tolist()) for N in (5,7,8,10,11,14,25)])
