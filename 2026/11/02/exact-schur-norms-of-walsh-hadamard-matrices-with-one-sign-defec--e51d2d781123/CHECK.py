#!/usr/bin/env python3
"""Reproduce finite checks for a one-sign-defect Walsh Schur multiplier.
Requires Python >=3.10 and the standard library only.
The proof in RESULT.md, not finite calculations, establishes the theorem.
"""
import math
import random


def walsh_defect(n):
    assert n >= 2 and n & (n-1) == 0
    m = [[1 if ((i & j).bit_count() % 2 == 0) else -1
          for j in range(n)] for i in range(n)]
    m[0][0] = -1
    return m


def eigs_sym(a, tol=1e-13):
    """Jacobi eigenvalue algorithm for a small real symmetric matrix."""
    n = len(a)
    a = [row[:] for row in a]
    for iteration in range(100*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),
                key=lambda z: abs(a[z[0]][z[1]]))
        if abs(a[p][q]) < tol:
            return [a[i][i] for i in range(n)]
        app,aqq,apq = a[p][p],a[q][q],a[p][q]
        tau=(aqq-app)/(2*apq)
        t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t)
        s=t*c
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k != p and k != q:
                akp,akq=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*akp-s*akq
                a[k][q]=a[q][k]=s*akp+c*akq
    raise AssertionError('Jacobi solver did not converge')


def trace_norm_weighted(m, p, q):
    # Nuclear norm of diag(sqrt(p)) M diag(sqrt(q)); real matrices.
    n=len(m)
    g=[[sum(math.sqrt(p[i]*p[j])*m[i][k]*m[j][k]*q[k]
            for k in range(n)) for j in range(n)] for i in range(n)]
    return sum(math.sqrt(v) if v>1e-12 else 0.0 for v in eigs_sym(g))


def formula(n,t):
    return ((n-2)*math.sqrt(n)+math.sqrt(t*t+(4*n-6)*t+1))/(t+n-1)


def optimum(n):
    return 2*math.sqrt(n*(n+2))-(2*n+1)


def run():
    checks=0
    rng=random.Random(62173)
    for n in (2,4,8,16):
        m=walsh_defect(n)
        # Exact integer Walsh-orthogonality and balanced nonzero rows.
        h=[row[:] for row in m]
        h[0][0]=1
        for i in range(n):
            for j in range(n):
                assert sum(h[i][k]*h[j][k] for k in range(n)) == (n if i==j else 0)
                checks+=1
        for i in range(1,n):
            assert sum(h[i][1:])==-1
            checks+=1
        if n==2:
            assert abs(formula(n,optimum(n))-1)<1e-12
            checks+=1
        for t in (0.0,0.12,0.4,0.75,1.0,1.7,5.0):
            b=1/(t+n-1)
            p=[t*b]+[b]*(n-1)
            observed=trace_norm_weighted(m,p,p)
            assert abs(observed-formula(n,t)) <= 2e-10, (n,t,observed,formula(n,t))
            checks+=1
        if n>=4:
            t=optimum(n)
            f=formula(n,t)
            assert 0<t<1
            assert f>1 and f<math.sqrt(n)
            checks+=3
            for dx in (-0.5,-0.1,-0.01,0.01,0.1,0.5,1.0,2.0):
                assert f+1e-12 >= formula(n,max(0.0,t+dx))
                checks+=1
            for _ in range(40):
                p=[rng.expovariate(1) for _ in range(n)]
                q=[rng.expovariate(1) for _ in range(n)]
                p=[v/sum(p) for v in p]
                q=[v/sum(q) for v in q]
                got=trace_norm_weighted(m,p,q)
                assert got <= f+5e-10, (n,got,f)
                checks+=1
    for n in (32,64,128,256,1024,4096):
        t=optimum(n)
        assert 0<t<1
        assert 0<math.sqrt(n)-formula(n,t)<2/n**1.5
        checks+=2
    print('CHECK_OK exact-orthogonality-and-numerical-tests=%d'%checks)
    for n in (4,8,16,32,64):
        print('order=%d weight_ratio=%.12g schur_norm=%.12g deficit=%.12g'%
              (n,optimum(n),formula(n,optimum(n)),math.sqrt(n)-formula(n,optimum(n))))

if __name__=='__main__':
    run()
