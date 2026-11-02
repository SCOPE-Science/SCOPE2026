"""Reproducible numerical checks for the powered-distance theorem of edge-subdivided bicliques.

Uses Python 3, numpy and scipy. The analytical argument, not this finite test,
proves the all-parameter theorem.
"""
import math
from collections import deque
import numpy as np
from scipy.linalg import eigvalsh
from scipy.optimize import brentq


def graph_distances(m, n):
    """Reconstruct graph independently of the formula by BFS."""
    assert 2 <= m and 2 <= n
    # First m are A vertices, next n are B, remaining mn represent all original edges.
    N = m + n + m*n
    adj = [[] for _ in range(N)]
    for i in range(m):
        for j in range(n):
            k = m+n+i*n+j
            for h in (i, m+j):
                adj[h].append(k)
                adj[k].append(h)
    D = np.zeros((N, N), dtype=float)
    for v in range(N):
        d = [-1]*N
        d[v] = 0
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if d[y] == -1:
                    d[y] = d[x]+1
                    queue.append(y)
        assert -1 not in d
        D[v] = d
    return D


def analytic_distances(m, n):
    N=m+n+m*n
    D=np.zeros((N,N))
    for i in range(N):
        for j in range(i):
            if i<m and j<m: d=4
            elif m<=i<m+n and m<=j<m+n: d=4
            elif (i<m and m<=j<m+n) or (j<m and m<=i<m+n): d=2
            elif i>=m+n and j>=m+n:
                x,y=divmod(i-m-n,n);z,w=divmod(j-m-n,n)
                d=2 if x==z or y==w else 4
            else:
                e=i if i>=m+n else j
                v=j if i>=m+n else i
                x,y=divmod(e-m-n,n)
                d=1 if (v<m and x==v) or (m<=v<m+n and y==v-m) else 3
            D[i,j]=D[j,i]=d
    return D


def global_matrix(m,n,p):
    b=2.0**p; a=b*b; c=3.0**p
    sig=1/m+1/n; tau=1/(m*n); delta=1/m-1/n
    K=(a*(2-sig)-2*b)/4
    J=delta*(a/2+1-c)
    R=a*((6-5*sig)/4+tau)+b*(0.5+sig-2*tau)-2*c-(1-c)*sig
    return np.array([[K,J/2],[J/2,R]])


def threshold(m,n):
    cap=math.log2(2/(2-1/m-1/n))
    if m==n: return cap
    f=lambda p:np.linalg.det(global_matrix(m,n,p))
    # f(0)>0 and f(cap)<0 by the theorem. Avoid p=0 as optimization bound.
    assert f(0)>0 and f(cap)<0
    return brentq(f,0,cap,xtol=2e-14)


def critical_vector(m,n,p):
    H=global_matrix(m,n,p)
    if m==n:
        s,w=1.,0.
    else:
        w=1.;s=-H[0,1]/H[0,0]
    u=(s-w)/2;v=(-s-w)/2
    return np.r_[np.full(m,u/m),np.full(n,v/n),np.full(m*n,w/(m*n))]


def centered_eigs(D,p):
    N=len(D)
    # Orthonormal zero-sum basis from a Householder transformation.
    w=np.ones(N)/np.sqrt(N); e=np.zeros(N); e[-1]=1.
    v=w-e; v=v/np.linalg.norm(v)
    U=np.eye(N)-2*np.outer(v,v)
    B=U[:,:-1]
    assert np.linalg.norm(B.T@np.ones(N))<1e-10
    return eigvalsh(B.T@(D**p)@B)


def run():
    tested=0
    pairs=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(2,8),(3,7)]
    for m,n in pairs:
        D=graph_distances(m,n)
        assert np.array_equal(D,analytic_distances(m,n))
        tested+=1
        p0=threshold(m,n)
        pk=math.log2(2/(2-1/m-1/n))
        if (m,n)!=(2,2):
            if m==n: assert abs(p0-pk)<2e-12
            else: assert 0<p0<pk-1e-5
        else: assert abs(p0-1)<2e-12
        for p in [0.01,p0/2,p0,max(p0+0.01,1.02)]:
            ev=centered_eigs(D,p)
            if p<p0-1e-10: assert ev[-1]<-1e-7,(m,n,p,ev[-1])
            elif p>p0+1e-10: assert ev[-1]>1e-7,(m,n,p,ev[-1])
            else:
                dim=3 if (m,n)==(2,2) else 1
                assert sum(abs(ev)<4e-8)==dim,(m,n,ev[-5:])
                assert ev[-dim-1]<-1e-5,(m,n,ev[-dim-1])
            tested+=1
        if (m,n)!=(2,2):
            x=critical_vector(m,n,p0)
            assert abs(x.sum())<3e-13
            assert abs(x@(D**p0)@x)<2e-10,(m,n)
            tested+=1
    for m in [2,3,4,5,8]:
        coef=(1+1/m)/((4-1/m)*math.log(2)-2*math.log(3))
        assert coef>0
        for n in [1000,4000,16000]:
            pp=threshold(m,n)
            # The asymptotic residual multiplied by n^2 remains bounded.
            assert abs(pp-coef/n)*n*n<15000,(m,n,pp,coef)
            tested+=1
    print('CHECK_OK',tested,'assertion groups; exact BFS distances, full centered spectra, kernel vectors and asymptotics')

if __name__=='__main__':run()
