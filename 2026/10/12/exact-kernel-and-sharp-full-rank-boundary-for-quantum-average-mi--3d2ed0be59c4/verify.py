#!/usr/bin/env python3
"""Verify double-star adjacency quantum-average-mixing formulas.
Requires Python 3, sympy and numpy. All exact tests use sympy rationals/radicals.
No external downloads, and no dependence on other files.
"""
import itertools
import numpy as np
import sympy as s

def adjacency(p, q, engine=s):
    n = p+q+2
    A=s.zeros(n) if engine is s else np.zeros((n,n))
    x,y=p,p+1
    for i in range(p):
        A[i,x]=A[x,i]=1
    A[x,y]=A[y,x]=1
    for k in range(q):
        i=p+2+k
        A[i,y]=A[y,i]=1
    return A

def predicted_nullity(p,q):
    if p==q==1:return 2
    if p==q==2:return 3
    if p==q:return 1
    return (p<=2)+(q<=2)

def kernel_vectors(p,q,engine=s):
    n=p+q+2
    def v(mapping):
        out=s.zeros(n,1) if engine is s else np.zeros(n)
        for k,x in mapping.items():out[k]=x
        return out
    x,y=p,p+1
    out=[]
    if p==2:out.append(v({0:1,1:-1}))
    if q==2:out.append(v({p+2:1,p+3:-1}))
    if p==q:out.append(v({x:1,y:-1}))
    if p==q==1:out.append(v({0:1,p+2:-1}))
    if p==1 and q>=2:out.append(v({0:q-1,x:-q,y:1}))
    if q==1 and p>=2:out.append(v({p+2:p-1,y:-p,x:1}))
    return out

def w_formula(p,q):
    D=s.sqrt((p+q+1)**2-4*p*q)
    u=(p+q+1+D)/2;v=(p+q+1-D)/2
    out=[]
    for mu,a,b in [(u,(u-q)/(2*D),(u-p)/(2*D)),(v,(q-v)/(2*D),(p-v)/(2*D))]:
        w=s.Matrix([a/mu]*p+[a,b]+[b/mu]*q)
        out.append((mu,w,a,b))
    return out

def zero_projector(p,q):
    n=p+q+2; E=s.zeros(n)
    for k,size in [(0,p),(p+2,q)]:
        for i in range(size):
            for j in range(size):
                E[k+i,k+j]=s.KroneckerDelta(i,j)-s.Rational(1,size)
    return E

def mixing_formula(p,q):
    E=zero_projector(p,q)
    M=E.multiply_elementwise(E)
    for mu,w,a,b in w_formula(p,q):
        M+=2*w*w.T
    return M

def mixing_projectors(p,q):
    A=adjacency(p,q)
    E0=zero_projector(p,q)
    W=w_formula(p,q)
    n=p+q+2; I=s.eye(n); A2=A*A
    res=E0.multiply_elementwise(E0)
    for j,(mu,_,_,_) in enumerate(W):
        other=W[1-j][0]
        P=A2*(A2-other*I)/(mu*(mu-other))
        B=A*P
        res+=(P.multiply_elementwise(P)+B.multiply_elementwise(B)/mu)/2
    return res

def independent_numeric(p,q):
    A=np.array(adjacency(p,q), dtype=float)
    vals,V=np.linalg.eigh(A)
    M=np.zeros_like(A)
    i=0
    while i<len(vals):
        j=i+1
        while j<len(vals) and abs(vals[j]-vals[i])<1e-8:j+=1
        P=V[:,i:j]@V[:,i:j].T
        M+=P*P
        i=j
    return M

def mixing_formula_float(p,q):
    D=np.sqrt((p+q+1)**2-4*p*q)
    mup=(p+q+1+D)/2
    mum=(p+q+1-D)/2
    E=np.array(zero_projector(p,q),dtype=float)
    M=E*E
    for mu,a,b in [(mup,(mup-q)/(2*D),(mup-p)/(2*D)),(mum,(q-mum)/(2*D),(p-mum)/(2*D))]:
        w=np.array([a/mu]*p+[a,b]+[b/mu]*q)
        M+=2*np.outer(w,w)
    return M

def main():
    n_exact=0;n_entries=0
    # Small exact projector identities (not an enumeration proof).
    for p,q in [(1,1),(1,2),(2,2),(2,3)]:
        M=mixing_formula(p,q)
        W=mixing_projectors(p,q)
        n=p+q+2
        samples={(0,0),(0,p),(p,p),(p,p+1),(p+1,p+1),(n-1,n-1)}
        for i,j in samples:
            assert s.simplify(M[i,j]-W[i,j])==0,(p,q,i,j)
            n_entries+=1
        for v in kernel_vectors(p,q):
            assert all(s.simplify(w)==0 for w in M*v),(p,q,'kernel')
        assert len(kernel_vectors(p,q))==predicted_nullity(p,q)
        n_exact+=1
    n_float=0;max_diff=0.0;max_res=0.0
    for p in range(1,13):
        for q in range(1,13):
            Mi=independent_numeric(p,q)
            M=mixing_formula_float(p,q)
            err=np.max(np.abs(M-Mi));max_diff=max(max_diff,float(err))
            assert err<1e-9,(p,q,err)
            N=p+q+2
            assert np.linalg.matrix_rank(Mi,tol=1e-8)==N-predicted_nullity(p,q),(p,q,'floating-rank')
            K=kernel_vectors(p,q,engine=np)
            for v in K:
                err=np.max(np.abs(Mi@v));max_res=max(max_res,float(err))
                assert err<1e-9,(p,q,'floating-kernel')
            if K:assert np.linalg.matrix_rank(np.stack(K,axis=1))==len(K)
            n_float+=1
    assert s.factor((s.Symbol('u')-s.Symbol('q'))*(s.Symbol('p')-s.Symbol('v'))-(s.Symbol('q')-s.Symbol('v'))*(s.Symbol('u')-s.Symbol('p'))-(s.Symbol('p')-s.Symbol('q'))*(s.Symbol('u')-s.Symbol('v')))==0
    print(f'VERIFY_OK exact_cases={n_exact} exact_projector_samples={n_entries} independent_numeric_cases={n_float} max_matrix_error={max_diff:.3g} max_kernel_residual={max_res:.3g} double_star_2_2_rank={6-predicted_nullity(2,2)}/6 full_rank_3_4={9-predicted_nullity(3,4)}/9')
if __name__=='__main__':main()
