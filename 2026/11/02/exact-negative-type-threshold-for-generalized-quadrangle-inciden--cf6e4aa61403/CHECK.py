"""Reproducible supplementary checks for generalized-quadrangle distance kernels.

Python 3 standard library only. All-parameter statements require the analytic
proof in RESULT.md; finite numerical tests here are not infinite certificates.
"""
from collections import deque
from math import log2, sqrt


def coefficients(s, t):
    r, k = t + 1, s + 1
    return (s*r*r + t*k*k,
            s*t*(s*r + t*k),
            2*k*r*s*t,
            2*k*r)


def P(s, t, p):
    a, b, c, d = coefficients(s, t)
    return a * 2.0**p + b * 4.0**p - c * 3.0**p - d


def root(s, t):
    lo, hi = 0.0, log2(1.0 + 1.0/max(s, t))
    assert P(s, t, lo) < 0 < P(s, t, hi)
    for _ in range(70):
        mid = (lo+hi)/2
        if P(s, t, mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def symplectic(u, v):
    x = [(u >> j) & 1 for j in range(4)]
    y = [(v >> j) & 1 for j in range(4)]
    return (x[0]*y[1]+x[1]*y[0]+x[2]*y[3]+x[3]*y[2]) % 2


def gq22():
    pts = tuple(range(1, 16))
    lines = sorted({tuple(sorted((u,v,u^v)))
                    for u in pts for v in pts
                    if u != v and symplectic(u,v)==0})
    assert len(lines)==15
    assert all(sum(p in L for L in lines)==3 for p in pts)
    assert all(len(L)==3 for L in lines)
    for p in pts:
        for L in lines:
            if p not in L:
                assert sum(symplectic(p,q)==0 for q in L)==1
    edges = [[] for _ in range(30)]
    for i,p in enumerate(pts):
        for j,L in enumerate(lines):
            if p in L:
                edges[i].append(j+15)
                edges[j+15].append(i)
    dist = []
    for a in range(30):
        ds=[-1]*30
        ds[a]=0
        todo=deque([a])
        while todo:
            u=todo.popleft()
            for v in edges[u]:
                if ds[v]<0:
                    ds[v]=ds[u]+1
                    todo.append(v)
        assert min(ds)==0 and max(ds)==4
        dist.append(ds)
    for a in range(30):
        for b in range(30):
            assert dist[a][b]==dist[b][a]
            if a==b:
                assert dist[a][b]==0
            elif a<15 and b<15:
                assert dist[a][b]==(2 if symplectic(pts[a],pts[b])==0 else 4)
            elif a>=15 and b>=15:
                assert dist[a][b]==(2 if set(lines[a-15]) & set(lines[b-15]) else 4)
            else:
                pi=a if a<15 else b
                li=b-15 if a<15 else a-15
                assert dist[a][b]==(1 if pts[pi] in lines[li] else 3)
    return dist


def contrast_q(dist, p):
    z=[1/15]*15+[-1/15]*15
    return sum(z[i]*z[j]*dist[i][j]**p
               for i in range(30) for j in range(30) if i!=j)


def check():
    assertions=0
    for s in range(2, 31):
        for t in range(2, 31):
            A,B,C,D=coefficients(s,t)
            assert (A+B-C-D)==-(s+t+2)
            assertions+=1
            assert 2*B-C==2*s*t*(s*t-1)
            assertions+=1
            assert 5*(A+2*B)-8*C == (4*s*s*t*t-s*s*t-s*t*t+4*s*t+5*s+5*t)
            assertions+=1
            u,v=min(s,t),max(s,t)
            A2,B2,C2,D2=coefficients(u,v)
            x=1/v
            lower=A2*(1+x)+B2*(1+x)**2-C2*(1+1.6*x+0.5*x*x)-D2
            target=(u+1)*(4*u-5)*(v+1)/5
            assert abs(lower-target)<1e-7*max(1,target)
            assertions+=1
            alpha=root(s,t)
            assert 0<alpha<log2(1+1/max(s,t))<1
            a,b,c=2**alpha,3**alpha,4**alpha
            u1=(s-1)*a-s*c
            u2=(t-1)*a-t*c
            determinant=u1*u2-(s+t)*(b-1)**2
            assert u1<0 and u2<0 and determinant>0
            assert t*c-(t+1)*a<0 and s*c-(s+1)*a<0
            assert P(s,t,max(0,alpha-1e-5))<0<P(s,t,alpha+1e-5)
            assertions+=1
    dist=gq22()
    alpha=root(2,2)
    assert abs(alpha-0.34578472347643)<1e-11
    assertions+=1
    for p in [0, 0.1, alpha-1e-3, alpha, alpha+1e-3, 0.5, 1.0]:
        # q is P/(k*r*(st+1)), for s=t=2 the denominator is 45.
        assert abs(contrast_q(dist,p)-P(2,2,p)/45)<1e-9
        assertions+=1
    print('GQ_NEGATIVE_TYPE_CHECK_OK',assertions, 'sample_alpha',format(alpha,'.14f'))


if __name__=='__main__':
    check()
