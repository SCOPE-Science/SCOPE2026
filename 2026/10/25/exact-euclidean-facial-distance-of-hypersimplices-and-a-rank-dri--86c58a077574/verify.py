#!/usr/bin/env python3
"""Exact face-orbit and independent small-dimensional convex checks for hypersimplex facial distance."""
from fractions import Fraction as F
from math import comb, floor
from itertools import combinations

def square_face(n,k,a,b):
    r=n-a-b
    assert 0<=a<=n-k-1 and 0<=b<=k-1 and a+b>0 and 2<=r
    H=n*(a+b)-(a-b)**2
    # Squared optimum and exactly feasible single-violation mixing parameter.
    if a==0: u=F(0); v=F(1)
    elif b==0: u=F(1); v=F(0)
    else:
        u=F(a*(r+2*b),H)
        v=F(b*(r+2*a),H)
    assert u+v==1 and 0<=u<=1 and 0<=v<=1
    d= (u*u/F(a) if a else 0) + (v*v/F(b) if b else 0) + (u-v)**2/F(r)
    assert d==F(n,H),(n,k,a,b,d,F(n,H))
    kp=k-b
    assert 1<=kp<=r-1
    # Uniform one-violation vertices yield the stated residual average.
    gamma=(u*F(kp-1,r) + v*F(kp+1,r))
    assert gamma==F(kp+v-u,r)
    return H

def predicted_H(n,k):
    t=min(k,n-k)
    if n<=4*t:
        return n*(n-2)-(n-2*t)**2
    return (n*n)//4 + 2*n*(t-1)

def verify_orbits():
    n_cases=0
    orbits=0
    for n in range(4,34):
        for k in range(2,n-1):
            values=[]
            for a in range(n-k):
                for b in range(k):
                    if a+b:
                        values.append(square_face(n,k,a,b)); orbits+=1
            optimum=max(values)
            theoretical=predicted_H(n,k)
            assert optimum==theoretical,(n,k,optimum,theoretical)
            vertex_den=k*(n-k)
            assert optimum>vertex_den,(n,k,optimum,vertex_den)
            # All optimizing orbit types, inclusive of the tie at n=4t+1.
            max_pairs={(a,b) for a in range(n-k) for b in range(k)
                       if a+b and n*(a+b)-(a-b)**2==optimum}
            t=min(k,n-k)
            if k<=n//2:
                if n<=4*t: expected={(n-t-1,t-1)}
                elif n%2==0: expected={(t-1+n//2,t-1)}
                else: expected={(t-1+n//2,t-1),(t+n//2,t-1)}
            else:
                if n<=4*t: expected={(t-1,n-t-1)}
                elif n%2==0: expected={(t-1,t-1+n//2)}
                else: expected={(t-1,t-1+n//2),(t-1,t+n//2)}
            assert max_pairs==expected,(n,k,max_pairs,expected)
            n_cases+=1
    return n_cases,orbits

def small_vertex_checks():
    cases=0
    # Construct weighted mixtures of explicitly enumerated vertices to check
    # that the exact orbit witness lies in the complement convex hull.
    for n in range(4,9):
        for k in range(2,n-1):
            vertices=[set(c) for c in combinations(range(n),k)]
            for a in range(n-k):
                for b in range(k):
                    if a+b==0:continue
                    A=set(range(a)); B=set(range(a,a+b)); R=set(range(a+b,n))
                    kp=k-b
                    typesA=[V for V in vertices if len(V&A)==1 and len(B-V)==0]
                    typesB=[V for V in vertices if len(V&A)==0 and len(B-V)==1]
                    assert bool(typesA)==bool(a) and bool(typesB)==bool(b)
                    H=n*(a+b)-(a-b)**2
                    if a==0:u=F(0)
                    elif b==0:u=F(1)
                    else:u=F(a*(n-a-b+2*b),H)
                    # Mixtures of true complement vertices, not relaxation.
                    mixture=[]
                    if a: mixture.extend((u/F(len(typesA)),V) for V in typesA)
                    if b: mixture.extend(((1-u)/F(len(typesB)),V) for V in typesB)
                    assert sum((w for w,V in mixture),F(0))==1
                    y=[sum((w for w,V in mixture if i in V),F(0)) for i in range(n)]
                    x=[F(0)]*a+[F(1)]*b+[F(kp,n-a-b)]*(n-a-b)
                    sq=sum((v-w)**2 for v,w in zip(x,y))
                    assert sq==F(n,H),(n,k,a,b,sq,F(n,H))
                    assert all(V not in [set(c) for c in combinations(R,kp)] for V in [])
                    cases+=1
    return cases

def numeric_qp_checks():
    # Independent vertex-enumeration convex quadratic programs (optional SciPy).
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        return 'SCIPY_NOT_INSTALLED'
    checks=0
    for n,k,a,b in [(4,2,1,1),(5,2,2,1),(6,2,3,1),(6,3,2,2),
                     (7,2,4,1),(7,3,3,2),(8,2,5,1),(8,3,4,2)]:
        V=np.array([tuple(int(i in c) for i in range(n)) for c in combinations(range(n),k)],dtype=float)
        mask=np.array([all(V[j,i]==0 for i in range(a)) and all(V[j,i]==1 for i in range(a,a+b)) for j in range(len(V))])
        X=V[mask];Y=V[~mask]
        nx,ny=len(X),len(Y)
        def func(w):
            z=w[:nx]@X-w[nx:]@Y
            return z@z
        def jac(w):
            z=w[:nx]@X-w[nx:]@Y
            return np.concatenate((2*X@z,-2*Y@z))
        constraint=[{'type':'eq','fun':lambda w,p=nx:sum(w[:p])-1,'jac':lambda w,p=nx:np.array([1.]*p+[0.]*ny)},
                    {'type':'eq','fun':lambda w,p=nx:sum(w[p:])-1,'jac':lambda w,p=nx:np.array([0.]*p+[1.]*ny)}]
        start=np.r_[np.ones(nx)/nx,np.ones(ny)/ny]
        result=minimize(func,start,jac=jac,constraints=constraint,bounds=[(0,None)]*(nx+ny),method='SLSQP',
                        options={'ftol':1e-12,'maxiter':800})
        assert result.success,(n,k,a,b,result.message)
        expected=float(F(n,n*(a+b)-(a-b)**2))
        assert abs(result.fun-expected)<2e-7,(n,k,a,b,result.fun,expected)
        checks+=1
    return checks

if __name__=='__main__':
    a,b=verify_orbits(); c=small_vertex_checks(); q=numeric_qp_checks()
    print(f'EXACT_OK rank_cases={a} face_orbits={b} explicit_complement_mixtures={c} independent_vertex_QP={q}')
