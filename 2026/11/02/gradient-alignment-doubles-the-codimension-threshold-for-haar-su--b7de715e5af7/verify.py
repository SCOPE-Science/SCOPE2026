#!/usr/bin/env python3
"""Reproducible matrix-identity and rational-moment diagnostics for a Haar-subspace quadratic model.

Requires only Python 3 standard library. These finite tests do not prove tail limits.
"""
import math, random
from fractions import Fraction

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def transpose(A): return list(map(list,zip(*A)))
def solve(A,y):
    n=len(y); M=[list(map(float,r))+[float(yi)] for r,yi in zip(A,y)]
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(M[i][j])); M[j],M[p]=M[p],M[j]
        assert abs(M[j][j])>1e-13
        z=M[j][j]; M[j]=[t/z for t in M[j]]
        for i in range(n):
            if i==j:continue
            z=M[i][j]; M[i]=[t-z*s for t,s in zip(M[i],M[j])]
    return [r[-1] for r in M]

def frame(d,k,rng):
    cols=[]
    for _ in range(k):
        while True:
            x=[rng.gauss(0,1) for _ in range(d)]
            for q in cols:
                t=dot(x,q); x=[xi-t*qi for xi,qi in zip(x,q)]
            # reorthogonalize to control floating point errors
            for q in cols:
                t=dot(x,q); x=[xi-t*qi for xi,qi in zip(x,q)]
            t=norm(x)
            if t>1e-9: break
        cols.append([v/t for v in x])
    return cols

def step(cols,e,g,c=1.0,hessian=None):
    k=len(cols)
    if hessian is None:
        A=[[c*(dot(u,v)-dot(u,e)*dot(v,e)) for v in cols] for u in cols]
    else:
        A=[[sum(ui*sum(hij*vj for hij,vj in zip(row,v)) for ui,row in zip(u,hessian)) for v in cols] for u in cols]
    z=solve(A,[dot(u,g) for u in cols]); return [sum(zj*col[i] for zj,col in zip(z,cols)) for i in range(len(e))]

def closed_sq(cols,e,g,c=1):
    T=sum(dot(u,e)**2 for u in cols)
    gv=[dot(u,g) for u in cols]
    a=[dot(u,e) for u in cols]
    return (dot(gv,gv)+(2-T)*dot(a,gv)**2/(1-T)**2)/(c*c),T

def tests():
    rng=random.Random(12345)
    count=0
    for d,k in [(3,1),(4,2),(5,1),(5,3),(6,2),(8,3),(10,4)]:
        e=[1.0]+[0.0]*(d-1)
        for _ in range(125):
            cols=frame(d,k,rng)
            gs=[[1.0]+[0.]*(d-1), [0.,1.]+[0.]*(d-2), [0.2,0.8]+[0.]*(d-2)]
            for g in gs:
                s=step(cols,e,g,c=2)
                sq,T=closed_sq(cols,e,g,c=2)
                assert math.isclose(dot(s,s),sq,rel_tol=3e-8,abs_tol=2e-8), (d,k,g,T)
                if g==gs[0]:
                    val=math.sqrt(T)/(2*(1-T))
                    assert math.isclose(norm(s),val,rel_tol=1e-8,abs_tol=1e-8)
                if g==gs[1]:
                    assert sq>=0
                count+=1
    # Exact rational beta identities, not Monte Carlo estimators
    exact=0
    for d in range(4,26):
        for k in range(1,d):
            r=d-k
            if r>4:
                # E[T/(1-T)^2]=a(a+b-1)/[(b-1)(b-2)]
                a=Fraction(k,2); b=Fraction(r,2)
                x=a*(a+b-1)/((b-1)*(b-2))
                assert x==Fraction(k*(d-2),(r-2)*(r-4))
                exact+=1
            if r>2:
                x=Fraction(k,d)+Fraction(1,d-1)*(Fraction(d-2,r-2)-Fraction(r,d))
                assert x==Fraction(k*(r-1),(d-1)*(r-2))
                exact+=1
    # Anisotropic nullspace bounds and three-dimensional diagnostic
    for d,k in [(3,1),(5,2),(7,3),(9,4)]:
        e=[1.]+[0.]*(d-1)
        H=[[0.]*d for _ in range(d)]
        vals=[0.]+[1.25+i/(d-1) for i in range(1,d)]
        for i in range(d):H[i][i]=vals[i]
        mi=min(vals[1:]); ma=max(vals[1:])
        for _ in range(75):
            cols=frame(d,k,rng)
            T=sum(dot(u,e)**2 for u in cols)
            s=step(cols,e,e,hessian=H)
            low=math.sqrt(T)/(ma*(1-T)); high=math.sqrt(T)/(mi*(1-T))
            assert low-1e-8<=norm(s)<=high+1e-8
            count+=1
    print('PASS',count,'direct matrix/special-case/bound checks;',exact,'exact rational moment identities')

if __name__=='__main__': tests()
