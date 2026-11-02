"""Reproduce exact spectral and positivity checks for two-community Padé diffusion."""
from math import sqrt
import numpy as np
import sympy as sp


def laplacian(p, q, a, c, b):
    """Two-community Laplacian; within first weight a, second c, cross b."""
    n = p + q
    L = np.zeros((n, n), dtype=float)
    for i in range(p):
        for j in range(i + 1, p):
            L[i,i] += a; L[j,j] += a; L[i,j] -= a; L[j,i] -= a
    for i in range(p,n):
        for j in range(i + 1,n):
            L[i,i] += c; L[j,j] += c; L[i,j] -= c; L[j,i] -= c
    for i in range(p):
        for j in range(p,n):
            L[i,i] += b; L[j,j] += b; L[i,j] -= b; L[j,i] -= b
    return L


def pade(L,h):
    n=L.shape[0]
    Z=np.eye(n) + h*L/2 + h*h*(L@L)/12
    W=np.eye(n) - h*L/2 + h*h*(L@L)/12
    return np.linalg.solve(Z,W)


def three_off_diagonals(p,q,a,c,b,h):
    n=p+q; t=b*h; alpha=a/b; gamma=c/b
    ua=p*alpha+q; ub=q*gamma+p
    D=lambda z: 1+z/2+z*z/12
    f=lambda z: z/D(z)
    aa=t*(p*alpha +p*ua*t/2+ua*(n*n-q*ua)*t*t/12)/(p*D(ua*t)*D(n*t))
    bb=t*(q*gamma +q*ub*t/2+ub*(n*n-p*ub)*t*t/12)/(q*D(ub*t)*D(n*t))
    cross=f(n*t)/n
    return aa,bb,cross


def side_horizon(s,other,ratio,b):
    n=s+other
    if ratio <= (s+2*other)/other: return float('inf')
    u=s*ratio+other
    d=u*(other*u-n*n)/12
    v=s*u/2; z=s*ratio
    return (v+sqrt(v*v+4*d*z))/(2*d*b)


def horizon(p,q,a,c,b):
    return min(side_horizon(p,q,a/b,b),side_horizon(q,p,c/b,b))


def main():
    checks=0
    for p in range(2,9):
      for q in range(2,9):
        acrit=(p+2*q)/q; ccrit=(q+2*p)/p
        for ra,rc in ((0,0),(0.2,0.5),(1,1),(2,3),
                      (acrit,ccrit),(acrit+0.5,0.8),(1,ccrit+1),
                      (acrit+3,ccrit+2)):
          b=1.13; a=ra*b; c=rc*b
          L=laplacian(p,q,a,c,b)
          for h in (0.002,0.1,0.75,3.0,9.0,47.0):
            M=pade(L,h)
            aa,bb,cross=three_off_diagonals(p,q,a,c,b,h)
            err=max(abs(M[0,1]-aa),abs(M[p,p+1]-bb),abs(M[0,p]-cross))
            assert err<3e-9,(p,q,ra,rc,h,err)
            assert max(abs(M.sum(axis=1)-1))<3e-9
            assert min(np.linalg.eigvalsh(M))>0
            assert cross>0
            H=horizon(p,q,a,c,b)
            if h<H-1e-7:assert min(aa,bb)>-1e-12,(p,q,ra,rc,h,H,aa,bb)
            if h>H+1e-7:assert min(aa,bb)<0,(p,q,ra,rc,h,H,aa,bb)
            checks+=1
    print('direct_dense_matrix_cases',checks)
    # Verify class formula algebra and high-step critical law exactly for asymmetric groups.
    n,p,q=5,2,3
    ra,rc,t=sp.symbols('alpha gamma t',nonnegative=True)
    U=p*ra+q;V=q*rc+p
    D=lambda z: 1+z/sp.Integer(2)+z*z/sp.Integer(12)
    f=lambda z:z/D(z)
    raw_A=(n*f(U*t)-q*f(n*t))/(p*n)
    full_A=t*(p*ra+p*U*t/2+U*(n*n-q*U)*t*t/12)/(p*D(U*t)*D(n*t))
    raw_B=(n*f(V*t)-p*f(n*t))/(q*n)
    full_B=t*(q*rc+q*V*t/2+V*(n*n-p*V)*t*t/12)/(q*D(V*t)*D(n*t))
    assert sp.factor(raw_A-full_A)==0
    assert sp.factor(raw_B-full_B)==0
    assert sp.limit(t*t*full_A.subs(ra,sp.Rational(p+2*q,q)),t,sp.oo)==sp.Rational(72*q,n**4)
    assert sp.limit(t*t*full_B.subs(rc,sp.Rational(q+2*p,p)),t,sp.oo)==sp.Rational(72*p,n**4)
    print('two_symbolic_decompositions_and_critical_limits_OK')
    # Positive-root classification across two competing community horizons.
    brackets=0
    for p in range(2,11):
      for q in range(2,11):
        ra0=(p+2*q)/q; rc0=(q+2*p)/p
        for ra,rc in ((ra0+0.02,1),(1,rc0+0.03),(ra0+1,rc0+0.3)):
          H=horizon(p,q,ra,rc,1)
          for k in (0.1,0.5,0.999,1.001,2,100):
            aa,bb,_=three_off_diagonals(p,q,ra,rc,1,H*k)
            if k<1: assert min(aa,bb)>0
            if k>1: assert min(aa,bb)<0
            brackets+=1
    print('positive_horizon_brackets',brackets)
    # Exact worked example and exact critical high-step coefficient.
    H=horizon(2,2,4,1,1)
    assert abs(H-(15+sqrt(465))/10)<1.e-12
    for k in (0.5,1.001,5):
        M=pade(laplacian(2,2,4,1,1),H*k)
        assert (M[0,1]>0)==(k<1)
        assert M[2,3]>0
    print('worked_example_horizon',(15+sqrt(465))/10)
    # Normalized divergence of horizon above each critical class price.
    scaled=0
    for p,q in ((2,2),(3,4),(8,3)):
      for swapped in (False,True):
        P,Q=(q,p) if swapped else (p,q)
        r0=(P+2*Q)/Q
        for eps in (1.e-3,1.e-4,1.e-5):
          H=side_horizon(P,Q,r0+eps,1)
          assert abs(H*eps*Q/6-1)<0.01
          scaled+=1
    print('critical_divergence_checks',scaled)
    print('VERIFY_OK')

if __name__=='__main__':main()
