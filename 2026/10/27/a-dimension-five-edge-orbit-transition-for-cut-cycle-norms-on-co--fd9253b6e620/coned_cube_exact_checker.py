"""Exact checks for cut/cycle projections of an unweighted hypercube with one apex.
Run with Python 3 and SymPy.  All comparisons use rational arithmetic.
"""
from fractions import Fraction as F
from math import comb
import sympy as S


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def radial_green(n, distance):
    # Walsh-resolvent expansion for (I+L(Q_n))^{-1}.
    val = F(0)
    for j in range(n + 1):
        a = sum((-1)**s * binom(distance, s) * binom(n-distance, j-s)
                for s in range(distance + 1))
        val += F(a, (1 << n) * (2*j + 1))
    return val


def exact_predictions(n):
    r0 = sum((F(comb(n, j), (1 << n) * (2*j + 1)) for j in range(n+1)), F(0))
    h0 = F(1, n) * (1-r0)
    qc_spoke = F(n+3, 3)
    qc_cube = F(6*n+14, 15)
    pc_spoke = 1+qc_spoke-2*r0
    pc_cube = 1+qc_cube-4*h0
    return r0, h0, qc_spoke, qc_cube, pc_spoke, pc_cube


def full_graph_checks(n):
    # Independent grounded graph Laplacian: the apex is grounded.
    N=1<<n
    edges=[(u, u^(1<<j)) for u in range(N) for j in range(n) if u < (u^(1<<j))]
    edges += [(u,N) for u in range(N)]
    L=S.zeros(N)
    for u,v in edges:
        if v == N:
            L[u,u]+=1
        else:
            L[u,u]+=1; L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    column_rhs=S.zeros(N, 2)
    column_rhs[0,0]=1
    column_rhs[0,1]=1; column_rhs[1,1]=-1
    X=L.inv()*column_rhs
    result=[]
    for typ,(u,v) in enumerate(((0,N),(0,1))):
        V={a:X[a,typ] for a in range(N)}
        V[N]=S.Integer(0)
        col=[abs(V[a]-V[b]) for a,b in edges]
        qc=sum(col)
        diag=abs(V[u]-V[v])
        pc=1+qc-2*diag
        result.append((F(qc),F(pc),F(diag)))
    return result,len(edges)


def check():
    spectral = 0
    for n in range(1,31):
        r0,h0,qs,qc,ps,pc=exact_predictions(n)
        r=[radial_green(n,j) for j in range(n+1)]
        h=[r[j]-r[j+1] for j in range(n)]
        assert r[0]==r0 and (n==1 or h[0]==h0)
        assert all(v>0 for v in r)
        assert all(t>0 for t in h)
        assert all(h[j]>h[j+1] for j in range(n-1))
        spoke_abs = 1+sum(binom(n,j)*(n-j)*h[j] for j in range(n))
        cube_abs=4*sum(binom(n-1,j)*h[j] for j in range(n)) + 2*sum(binom(n-1,j)*(n-1-j)*(h[j]-h[j+1]) for j in range(n-1))
        assert spoke_abs==qs and cube_abs==qc
        assert (qc>qs if n>1 else qc==qs)
        if n in (2,3,4): assert ps>pc
        if n>=5: assert pc>ps
        spectral+=1
    grounded=0; graph_edges=0
    for n in range(2,7):
        got,count=full_graph_checks(n)
        r0,h0,qs,qc,ps,pc=exact_predictions(n)
        assert got[0]==(qs,ps,r0), (n,got[0],(qs,ps,r0))
        assert got[1]==(qc,pc,2*h0), (n,got[1],(qc,pc,2*h0))
        grounded+=1; graph_edges+=count
    print('CONED_CUBE_HODGE_EXACT_OK spectral_dimensions=%d grounded_dimensions=%d grounded_graph_edges=%d' % (spectral,grounded,graph_edges))

if __name__ == '__main__':
    check()
