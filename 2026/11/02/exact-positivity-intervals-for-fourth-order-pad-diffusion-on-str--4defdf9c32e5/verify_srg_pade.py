#!/usr/bin/env python3
"""Exact finite-instance verification for [2/2] Pade diffusion on strongly regular graphs.
This checks examples only; the all-graph theorem is proved in RESULT.md.
Python 3 standard library, deterministic exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt


def graph_triangular(n):
    vs=list(combinations(range(n),2))
    return [[int(i!=j and len(set(a)&set(b))==1) for j,b in enumerate(vs)] for i,a in enumerate(vs)]

def graph_rook(n):
    vs=list(product(range(n),repeat=2))
    return [[int(i!=j and (a[0]==b[0] or a[1]==b[1])) for j,b in enumerate(vs)] for i,a in enumerate(vs)]

def graph_kneser(n):
    vs=list(combinations(range(n),2))
    return [[int(i!=j and set(a).isdisjoint(b)) for j,b in enumerate(vs)] for i,a in enumerate(vs)]

def graph_paley(p):
    residues={j*j%p for j in range(1,p)}
    assert p%4==1 and len(residues)==(p-1)//2
    return [[int(i!=j and (i-j)%p in residues) for j in range(p)] for i in range(p)]

def graph_complement(a):
    n=len(a)
    return [[int(i!=j and a[i][j]==0) for j in range(n)] for i in range(n)]

def parameters(a):
    n=len(a); k=sum(a[0]); ls=set(); ms=set()
    assert 0<k<n-1
    for i in range(n):
        assert sum(a[i])==k and a[i][i]==0
        for j in range(i+1,n):
            assert a[i][j]==a[j][i]
            c=sum(a[i][h]*a[j][h] for h in range(n))
            (ls if a[i][j] else ms).add(c)
    assert len(ls)==len(ms)==1, (n,k,ls,ms)
    lam=ls.pop(); mu=ms.pop()
    assert mu>0
    assert k*(k-lam-1)==(n-k-1)*mu
    return n,k,lam,mu

def mul(a,b):
    n=len(a); return [[sum((a[i][z]*b[z][j] for z in range(n)),F(0)) for j in range(n)] for i in range(n)]

def linear_solve(a,b):
    n=len(a); width=len(b[0]); x=[[F(v) for v in ar+br] for ar,br in zip(a,b)]
    for j in range(n):
        pivot=next((k for k in range(j,n) if x[k][j]),None)
        assert pivot is not None
        x[j],x[pivot]=x[pivot],x[j]
        f=x[j][j]; x[j]=[v/f for v in x[j]]
        for i in range(n):
            if i==j: continue
            f=x[i][j]
            if f: x[i]=[u-f*v for u,v in zip(x[i],x[j])]
    return [row[n:] for row in x]

def verify(a,t):
    n,k,lam,mu=parameters(a)
    S=2*k-lam+mu
    delta=n-S
    # Eigenvalues q1,q2 are roots of X^2-SX+mu*n (both >0).
    # Compute their denominator product with symmetric polynomials only.
    # D(q1t)D(q2t) = 1 + S*t/2 + ... ; derive by direct polynomial product below.
    t=F(t)
    s=F(S); pr=F(mu*n)
    # Symmetric reductions: q1^2+q2^2=s^2-2pr, q1^2 q2+q1 q2^2=pr*s
    # NOTE t^2 coefficient: (q1^2+q2^2)/12+q1q2/4=(s^2+pr)/12
    den=F(1)+s*t/2+(s*s+pr)*t*t/12+pr*s*t**3/24+pr*pr*t**4/144
    adj=t*(1+F(mu)*t/2+F(mu)*(S-n)*t*t/12)/den
    non=F(mu)*t*t*(F(1,2)+s*t/12)/den
    L=[[F(k if i==j else -a[i][j]) for j in range(n)] for i in range(n)]
    L2=mul(L,L)
    D=[[F(int(i==j))+t*L[i][j]/2+t*t*L2[i][j]/12 for j in range(n)] for i in range(n)]
    N=[[F(int(i==j))-t*L[i][j]/2+t*t*L2[i][j]/12 for j in range(n)] for i in range(n)]
    P=linear_solve(D,N)
    comparisons=0
    for i in range(n):
        assert sum(P[i])==1
        assert P[i][i]>0
        for j in range(n):
            if i==j:continue
            expected=adj if a[i][j] else non
            assert P[i][j]==expected,(n,k,lam,mu,t,i,j,P[i][j],expected)
            comparisons+=1
    if delta>0:
        poly=1+F(mu)*t/2-F(mu)*delta*t*t/12
        assert (adj>=0)==(poly>=0)
    else:assert adj>=0
    assert non>0 if t>0 else non==0
    return comparisons

def main():
    cases={
        'Petersen':graph_kneser(5),
        'Paley5':graph_paley(5),
        'Paley13':graph_paley(13),
        'Triangular4':graph_triangular(4),
        'Triangular5':graph_triangular(5),
        'Triangular6':graph_triangular(6),
        'Triangular7':graph_triangular(7),
        'Rook3':graph_rook(3),
        'Rook4':graph_rook(4),
        'ComplementTriangular7':graph_complement(graph_triangular(7)),
    }
    times=[F(1,5),F(1),F(3),F(4),F(100)]
    count=0
    for name,a in cases.items():
        v,k,lam,mu=parameters(a); S=2*k-lam+mu
        if name != 'Triangular4':
            assert parameters(graph_complement(a))[0]==v
        checks=sum(verify(a,t) for t in times)
        count+=checks
        print(name, 'srg', (v,k,lam,mu),'S-v=',S-v,'comparisons=',checks, flush=True)
    print('VERIFY_OK', len(cases),'graph instances;', len(cases)*len(times),'exact rational matrices;',count,'entry comparisons', flush=True)

if __name__=='__main__':main()
