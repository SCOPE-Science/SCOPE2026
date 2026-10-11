#!/usr/bin/env python3
import math
import numpy as np

def constant_diagonal_basis(B, c=None, tol=1e-11):
    B=np.array(B,dtype=float)
    n=B.shape[0]
    if c is None:
        c=np.trace(B)/n
    if n==1:
        return np.ones((1,1))
    vals,vecs=np.linalg.eigh(B)
    if np.max(np.abs(vals-c)) < tol:
        return np.eye(n)
    lo=np.where(vals <= c+tol)[0][0]
    hi=np.where(vals >= c-tol)[0][-1]
    # Prefer a genuinely straddling pair if available.
    lo_candidates=np.where(vals <= c+tol)[0]
    hi_candidates=np.where(vals >= c-tol)[0]
    lo=lo_candidates[0]
    hi=hi_candidates[-1]
    if abs(vals[hi]-vals[lo]) < tol:
        q=vecs[:,0]
    else:
        s2=(c-vals[lo])/(vals[hi]-vals[lo])
        s2=min(1.0,max(0.0,s2))
        q=math.sqrt(1-s2)*vecs[:,lo]+math.sqrt(s2)*vecs[:,hi]
        q=q/np.linalg.norm(q)

    # Deterministic orthonormal basis for q-perp from QR.
    M=np.eye(n)-np.outer(q,q)
    cols=[]
    for j in range(n):
        v=M[:,j].copy()
        for u in cols:
            v-=np.dot(u,v)*u
        nv=np.linalg.norm(v)
        if nv>1e-9:
            cols.append(v/nv)
        if len(cols)==n-1:
            break
    N=np.column_stack(cols)
    B2=N.T@B@N
    Q2=constant_diagonal_basis(B2,c,tol)
    Q=np.column_stack([q,N@Q2])
    return Q

def vol_parallel(A,Q):
    ell=[np.linalg.norm(A@Q[:,k]) for k in range(Q.shape[1])]
    return (2.0**Q.shape[1])*math.prod(ell),ell

def vol_cross(ell):
    n=len(ell)
    return (2.0**n)/(math.factorial(n)*math.prod(ell))

rng=np.random.default_rng(20261007)
cases=0
for n in range(2,8):
    raw=np.arange(1,n+1,dtype=float)**1.35 + 0.17
    raw=raw/np.linalg.norm(raw)
    A=np.diag(raw)
    B=A@A
    detA=float(np.linalg.det(A))
    lower=(2.0**n)*detA
    upper=(2.0**n)*(n**(-n/2))

    # Principal-axis minimum.
    Ve,ell_e=vol_parallel(A,np.eye(n))
    assert abs(Ve-lower) < 2e-11*max(1.0,lower)

    # Constant-diagonal maximum, constructed independently.
    Qc=constant_diagonal_basis(B,1.0/n)
    assert np.max(np.abs(Qc.T@Qc-np.eye(n))) < 2e-9
    diag=np.diag(Qc.T@B@Qc)
    assert np.max(np.abs(diag-1.0/n)) < 3e-9, (n,diag)
    Vc,ell_c=vol_parallel(A,Qc)
    assert abs(Vc-upper) < 2e-8*max(1.0,upper), (n,Vc,upper)

    # Polar endpoint and constant-product checks.
    Ce=vol_cross(ell_e)
    Cc=vol_cross(ell_c)
    assert abs(Ve*Ce-(4.0**n)/math.factorial(n)) < 2e-9
    assert abs(Vc*Cc-(4.0**n)/math.factorial(n)) < 2e-9
    cross_lower=(2.0**n)*(n**(n/2))/math.factorial(n)
    cross_upper=(2.0**n)/(math.factorial(n)*detA)
    assert abs(Cc-cross_lower) < 2e-8*max(1.0,cross_lower)
    assert abs(Ce-cross_upper) < 2e-8*max(1.0,cross_upper)

    # Independent random frames satisfy the sharp bounds.
    for _ in range(40):
        M=rng.normal(size=(n,n))
        Q,R=np.linalg.qr(M)
        Q=Q@np.diag(np.sign(np.diag(R)))
        V,ell=vol_parallel(A,Q)
        assert lower-3e-10 <= V <= upper+3e-10, (n,V,lower,upper)
        C=vol_cross(ell)
        assert cross_lower-3e-9 <= C <= cross_upper+3e-9
        assert abs(V*C-(4.0**n)/math.factorial(n)) < 3e-9
    cases+=1

print(f"VERIFY_OK fuss-volume-spectrum dimensions=2..7 cases={cases} constant_diagonal=yes polar_product=yes")
