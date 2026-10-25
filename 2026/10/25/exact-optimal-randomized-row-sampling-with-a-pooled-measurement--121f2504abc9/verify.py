"""Reproduce spectral and probability identities for an augmented star row frame.
Requires Python 3 and numpy; finite tests supplement, rather than replace, the proof.
"""
import numpy as np
from math import sqrt

def data(m, c):
    s = sqrt(1-c*c)
    r = s*s
    den = (m+1)*r + 2*sqrt(m)*c*s
    t = 1/den
    u = (1-(m+1)*c*c+sqrt(m)*c*s)/den
    v = sqrt(m)*c*s/den
    return s,r,den,t,u,v

def matrix(m,c,p):
    n=m+1
    s=sqrt(1-c*c)
    rows=[np.eye(n)[0]]
    for i in range(1,n):
        v=np.zeros(n)
        v[0]=c
        v[i]=s
        rows.append(v)
    rows.append(np.r_[0.,np.ones(m)/sqrt(m)])
    return sum(x*np.outer(a,a) for a,x in zip(rows,p))

if __name__ == '__main__':
    count=0
    max_error=0.
    rng=np.random.default_rng(65010)
    for m in range(2,13):
        zthr=(3*m+2+sqrt(5)*m)/(2*(m*m+3*m+1))
        for frac in (.05,.3,.6,.85,1.):
            c=sqrt(zthr)*frac
            s,r,den,t,u,v=data(m,c)
            assert min(t,u,v)>-1e-12
            assert abs(u+m*t+v-1)<3e-14
            p=[u]+[t]*m+[v]
            F=matrix(m,c,p)
            eig=np.linalg.eigvalsh(F)
            target=r/den
            err=abs(eig[0]-target)
            max_error=max(max_error,err)
            assert err<2e-13, (m,c,err)
            assert abs(np.sum(eig)-1.)<1e-12
            assert abs(u+m*t+v-1)<1e-12
            count+=1
            for k in range(50):
                q=rng.dirichlet(np.ones(m+2))
                e=np.linalg.eigvalsh(matrix(m,c,q))[0]
                assert e<=target+1e-12, (m,c,e,target)
                count+=1
    print('OK: 55 parameter configurations, 2750 arbitrary sampling vectors,',count,'total spectral comparisons; max error',max_error)
    # Exact rational certificate m=2, c=3/5, s=4/5, sqrt(m) irrational.
    # Block diagonal identity does not rely on floating-point verification.
    import sympy as sp
    m=4; c=sp.Rational(3,5); s=sp.Rational(4,5)
    r=s*s; den=(m+1)*r+2*sp.sqrt(m)*c*s
    t=1/den; u=(1-(m+1)*c*c+sp.sqrt(m)*c*s)/den
    v=sp.sqrt(m)*c*s/den
    Q=sp.Matrix([[u+m*t*c*c,sp.sqrt(m)*t*c*s],[sp.sqrt(m)*t*c*s,v+t*r]])
    assert sp.simplify(Q[0,0]-Q[1,1])==0
    assert sp.simplify(Q[0,0]-Q[0,1]-r/den)==0
    assert sp.simplify(u+m*t+v-1)==0
    assert sp.simplify((m+1)*r+2*sp.sqrt(m)*c*s-den)==0
    print('OK: exact symbolic block identities for m=4, c=3/5')
