"""Finite-section and algebraic checks for a one-spike shift tensor law.

Requires numpy and scipy. Finite checks corroborate, but do not prove,
infinite-dimensional essential-spectrum claims.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal

checks = 0


def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1


def edges(a, n):
    if n < 2:
        return np.zeros(0)
    b = np.full(n-1, 0.5)
    if n == 2:
        b[0] = a*a/2
    else:
        b[0] = b[-1] = a/2
    return b


def folded(a, n, parity):
    assert parity in (+1, -1)
    b = edges(a,n)
    r=n//2
    if n % 2 == 0:
        if r==0:
            return np.zeros(0),np.zeros(0)
        d=np.zeros(r)
        d[-1]=parity*b[r-1]
        return d,b[:r-1].copy()
    if parity < 0:
        return np.zeros(r), b[:max(0,r-1)].copy()
    d=np.zeros(r+1)
    e=np.zeros(r)
    if r > 0:
        e[:r-1]=b[:r-1]
        e[-1]=math.sqrt(2)*b[r-1]
    return d,e


def eigs(a,n,parity):
    d,e=folded(a,n,parity)
    if len(d)==0: return np.zeros(0)
    if len(d)==1: return d.copy()
    return eigh_tridiagonal(d,e,eigvals_only=True)


def full_matrix(a,n):
    b=edges(a,n)
    mat=np.zeros((n,n))
    for j,w in enumerate(b):
        mat[j,j+1]=mat[j+1,j]=w
    return mat


def parity_basis(n,parity):
    vectors=[]
    for j in range(n//2):
        v=np.zeros(n)
        v[j]=1/math.sqrt(2)
        v[n-1-j]=parity/math.sqrt(2)
        vectors.append(v)
    if parity==1 and n%2:
        v=np.zeros(n)
        v[n//2]=1.0
        vectors.append(v)
    if not vectors: return np.zeros((n,0))
    return np.stack(vectors,axis=1)


for a in (0.5,1,1.3,math.sqrt(2),1.6,2.0,3.0):
    for n in range(1,40):
        matrix=full_matrix(a,n)
        for parity in (1,-1):
            U=parity_basis(n,parity)
            d,e=folded(a,n,parity)
            J=np.diag(d)+np.diag(e,1)+np.diag(e,-1)
            check(np.allclose(U.T@U,np.eye(U.shape[1]),atol=1e-13),
                  f'parity orthogonality {a,n,parity}')
            check(np.allclose(matrix@U,U@J,atol=1e-13),
                  f'invariant folded section {a,n,parity}')
            check(np.allclose(np.linalg.eigvalsh(J),eigs(a,n,parity),atol=1e-12),
                  f'folded spectrum {a,n,parity}')
            # The Weyl band is uniformly bounded by 1 below or at threshold.
            if a <= math.sqrt(2) and n >= 4:
                check(max(abs(eigs(a,n,parity)),default=0) <= 1+1e-11,
                      f'no spurious exterior eigenvalue {a,n,parity}')
        same=np.sort(np.concatenate((eigs(a,n,1),eigs(a,n,-1))))
        check(np.allclose(same,np.linalg.eigvalsh(matrix),atol=1e-12),
              f'full spectrum parity decomposition {a,n}')

for a,n,tolerance in ((1.5,1200,0.0005),(1.6,500,1e-6),
                      (2.0,200,1e-9),(3.0,100,1e-10)):
    expected=a*a/(2*math.sqrt(a*a-1))
    for parity in (1,-1):
        vals=eigs(a,n,parity)
        check(abs(vals[-1]-expected)<tolerance,f'positive detached edge {a,n,parity}')
        check(abs(vals[0]+expected)<tolerance,f'negative detached edge {a,n,parity}')
    rho=1/math.sqrt(a*a-1)
    u0=a/(2*expected)
    values=[u0]+[rho**(i-1) for i in range(1,40)]
    lhs=[(a/2)*values[1]]
    for i in range(1,39):
        lhs.append(((a if i==1 else 1)/2)*values[i-1]+values[i+1]/2)
    for j,actual in enumerate(lhs):
        check(abs(actual-expected*values[j])<1e-10,f'half-line eigenvector {a,j}')

print(f'PASS: {checks} deterministic finite and recurrence assertions')
print('These tests are finite-dimensional corroboration, not an infinite proof.')
