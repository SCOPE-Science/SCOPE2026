#!/usr/bin/env python3
"""Independent finite checks of a weighted graph spectral-gap allocation theorem.

No packages beyond the Python standard library are required.  These checks
illustrate the universal analytic proof; they do not replace it.
"""
import math
import random
from fractions import Fraction as F


def eigenvalues_sym(a):
    """Cyclic Jacobi rotations for a real symmetric matrix."""
    a=[list(map(float,r)) for r in a]
    n=len(a)
    for _ in range(65*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-12: break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=math.copysign(1.,tau)/(abs(tau)+math.sqrt(1+tau*tau))
        cs=1/math.sqrt(1+t*t); sn=t*cs
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.
        for k in range(n):
            if k not in (p,q):
                akp,akq=a[k][p],a[k][q]
                a[k][p]=a[p][k]=cs*akp-sn*akq
                a[k][q]=a[q][k]=sn*akp+cs*akq
    else:
        raise AssertionError('Jacobi iteration failed to converge')
    return sorted(a[i][i] for i in range(n))


def corona_gap(m,core_edges,core_w,leaf_w):
    mat=[[0.0]*(2*m) for _ in range(2*m)]
    for (i,j),w in zip(core_edges,core_w):
        for v in (i,j):mat[v][v]+=w
        mat[i][j]-=w;mat[j][i]-=w
    for i,w in enumerate(leaf_w):
        mat[i][i]+=w;mat[m+i][m+i]+=w
        mat[i][m+i]-=w;mat[m+i][i]-=w
    ev=eigenvalues_sym(mat)
    assert abs(ev[0])<1e-9
    return ev[1]


def optimum(m,d,lam,P,Q,B):
    c=d*P/(2*lam)
    D=2*c+Q+2*math.sqrt(c*Q)
    gap=B/(m*D)
    core=gap/lam*(2+math.sqrt(Q/c))
    leaf=gap*(1+math.sqrt(c/Q))
    return gap,core,leaf


def run():
    count=0
    # Exact rational algebra: b/t and (lambda*a)/t parameterized
    # by any positive rational s = sqrt(c/Q).
    for p in range(1,20):
        for q in range(1,14):
            s=F(p,q); c=s*s; Q=F(1)
            D=2*c+Q+2*s
            u=1+s; x=2+1/s
            assert c*x+Q*u==D
            assert x*(u-1)==2*u-1
            assert D==(1+s)**2+s*s
            count+=3
    # Independent symmetric eigensystem and randomized nonuniform candidates.
    rng=random.Random(14626031)
    for m in range(3,12):
        edges=[(i,(i+1)%m) for i in range(m)]
        lam=2-2*math.cos(2*math.pi/m)
        for P,Q,B in ((1.,1.,1.),(9.,0.7,2.),(.2,15.,1.),(0.01,0.07,0.8)):
            gap,a,b=optimum(m,2,lam,P,Q,B)
            got=corona_gap(m,edges,[a]*m,[b]*m)
            assert abs(got-gap)<1e-8*max(1.,gap), (m,P,Q,B,got,gap)
            assert abs(m*(P*a+Q*b)-B)<1e-9*max(1.,B)
            count+=2
            for _ in range(20):
                raw=[math.exp(rng.uniform(-3,3)) for j in range(2*m)]
                rawsum=P*sum(raw[:m])+Q*sum(raw[m:])
                weights=[B*v/rawsum for v in raw]
                g=corona_gap(m,edges,weights[:m],weights[m:])
                assert g<=gap+1e-8*max(1.,gap), (m,P,Q,B,gap,g)
                count+=1
    # General transitive cores: complete graphs and cubic cube (Q3).
    for m in range(3,9):
        edges=[(i,j) for i in range(m) for j in range(i+1,m)]
        P,Q,B=1.7,.4,5.
        gap,a,b=optimum(m,m-1,m,P,Q,B)
        assert abs(corona_gap(m,edges,[a]*len(edges),[b]*m)-gap)<1e-8
        count+=1
    m=8
    edges=[(i,j) for i in range(m) for j in range(i+1,m) if (i^j).bit_count()==1]
    gap,a,b=optimum(m,3,2,2.,.8,3.)
    assert abs(corona_gap(m,edges,[a]*len(edges),[b]*m)-gap)<1e-8
    count+=1
    # The three leading asymptotic constants for cycles (fixed B,P,Q).
    for m in (250,1000,4000):
        P,Q,B=2.,3.,5.
        lam=2-2*math.cos(2*math.pi/m)
        gap,a,b=optimum(m,2,lam,P,Q,B)
        assert abs(gap*m**3/(2*math.pi**2*B/P)-1)<.06
        assert abs(a*m/(B/P)-1)<.06
        assert abs(b*m*m/(math.pi*B/math.sqrt(P*Q))-1)<.06
        count+=3
    print('PASS: %d exact and independent spectral/budget checks'%count)

if __name__=='__main__':run()
