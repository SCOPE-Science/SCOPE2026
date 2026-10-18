#!/usr/bin/env python3
"""Exact-rational finite-state checks for integrated occupation noise on a cycle.
Only Python's standard library is required.
"""
from fractions import Fraction as F


def solve(a, b):
    n=len(b)
    aug=[[F(z) for z in row]+[F(rhs)] for row,rhs in zip(a,b)]
    for k in range(n):
        piv=next(i for i in range(k,n) if aug[i][k])
        aug[k],aug[piv]=aug[piv],aug[k]
        c=aug[k][k]
        aug[k]=[x/c for x in aug[k]]
        for i in range(n):
            if i==k: continue
            c=aug[i][k]
            if c:
                aug[i]=[x-c*y for x,y in zip(aug[i],aug[k])]
    return [row[-1] for row in aug]


def verify(n,m):
    assert n>=3 and 1<=m<n
    a,b=m,n-m
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        L[i][i]-=2
        L[i][(i+1)%n]+=1
        L[i][(i-1)%n]+=1
    f=[F(int(i<m))-F(m,n) for i in range(n)]
    # Fix additive Poisson-gauge u_0=0, checking every equation.
    A=[[-L[i][j] for j in range(1,n)] for i in range(1,n)]
    u=[F(0)]+solve(A,f[1:])
    assert all(sum(-L[i][j]*u[j] for j in range(n))==f[i] for i in range(n))
    d=[u[(i+1)%n]-u[i] for i in range(n)]
    formula=[F(b*(a-2*(i+1)),2*n) if i<a else
             F(a*(2*i-n-a+2),2*n) for i in range(n)]
    assert d==formula, (n,m,d,formula)
    edge=[F(2,n)*s*s for s in d]
    variance=sum(edge)
    expected=F(a*b*(a*b+2),6*n*n)
    assert variance==expected,(n,m,variance,expected)
    # Independent spectral/Poisson covariance identity:
    covariance=F(2,n)*sum(f[i]*u[i] for i in range(n))
    assert covariance==expected,(n,m,covariance,expected)
    border=edge[a-1]+edge[n-1]
    assert border==F((a*b)**2,n**3)
    fraction=border/variance
    assert fraction==F(6*a*b,n*(a*b+2))
    # Boundary edges are the unique top two squared gradients.
    large=sorted(range(n),key=lambda i:edge[i],reverse=True)[:2]
    assert set(large)=={a-1,n-1}
    assert all(edge[i]<edge[a-1] for i in range(n) if i not in (a-1,n-1))
    # Sharp finite graph noise budget bound for all 1 <= K <= n.
    for k in range(1,n+1):
        best=sum(sorted(edge,reverse=True)[:k])/variance
        assert best<=F(3*k*a*b,n*(a*b+2))
    # Uniform-in-m finite-size expansion of the boundary ratio.
    assert F(6,n)-fraction==F(12,n*(a*b+2))
    return len(edge)


if __name__=='__main__':
    instances=0
    edges=0
    for n in range(3,21):
        for m in range(1,n):
            edges+=verify(n,m)
            instances+=1
    # Cases with larger n checked using direct arithmetic gradients (no linear solve).
    for n in (25,32,50,100,257,1024):
        for m in (1,2,n//3,n//2,n-1):
            a,b=m,n-m
            d=[F(b*(a-2*(i+1)),2*n) if i<a else F(a*(2*i-n-a+2),2*n) for i in range(n)]
            var=F(2,n)*sum(z*z for z in d)
            assert var==F(a*b*(a*b+2),6*n*n)
            assert d[a-1]==-F(a*b,2*n) and d[n-1]==F(a*b,2*n)
            instances+=1; edges+=n
    print(f'PASS: {instances} exact instances; {edges} rational edge weights;')
    print('Poisson equations, covariance variance, edge allocation, optimal two-edge capture, all budgets, uniform asymptotic residual checked.')

# The checks below solve the full interacting configuration-space Poisson
# equation, independently of the single-walker reduction above.
from itertools import combinations

def verify_exclusion(n, k, m, rate=1):
    r=F(rate); a,b=m,n-m
    states=[sum(1<<i for i in sites) for sites in combinations(range(n),k)]
    pos={mask:i for i,mask in enumerate(states)}
    sz=len(states)
    L=[[F(0) for j in range(sz)] for i in range(sz)]
    for s,mask in enumerate(states):
        for i in range(n):
            j=(i+1)%n
            if bool(mask & (1<<i)) != bool(mask & (1<<j)):
                swapped=mask^(1<<i)^(1<<j)
                L[s][pos[swapped]]+=r
                L[s][s]-=r
    f=[F((mask&((1<<m)-1)).bit_count())-F(k*m,n) for mask in states]
    A=[[-L[i][j] for j in range(1,sz)] for i in range(1,sz)]
    u=[F(0)]+solve(A,f[1:])
    assert all(sum(-L[i][j]*u[j] for j in range(sz))==f[i] for i in range(sz))
    variance=F(2,sz)*sum(f[i]*u[i] for i in range(sz))
    expected=F(k*(n-k)*a*b*(a*b+2),6*rate*n*n*(n-1))
    assert variance==expected,(n,k,m,rate,variance,expected)
    edges=[F(0) for _ in range(n)]
    for s,mask in enumerate(states):
        for i in range(n):
            j=(i+1)%n
            if bool(mask & (1<<i)) != bool(mask & (1<<j)):
                other=pos[mask^(1<<i)^(1<<j)]
                edges[i]+=r*(u[other]-u[s])**2/F(sz)
    assert sum(edges)==variance
    # Independent formula for the stationary quadratic variation per edge.
    d=[F(b*(a-2*(i+1)),2*n) if i<a else F(a*(2*i-n-a+2),2*n) for i in range(n)]
    assert edges==[F(2*k*(n-k),rate*n*(n-1))*v*v for v in d]
    assert (edges[m-1]+edges[n-1])/variance==F(6*a*b,n*(a*b+2))
    return sz

if __name__=='__main__':
    full=0; states_count=0
    for n in range(3,8):
        for k in range(1,n):
            for m in range(1,n):
                states_count+=verify_exclusion(n,k,m,1)
                full+=1
    for n,k,m,r in [(8,2,3,2),(8,3,4,1),(7,3,2,3),(6,2,3,5)]:
        states_count+=verify_exclusion(n,k,m,r)
        full+=1
    print(f'PASS: {full} full-interacting SSEP Poisson generator comparisons; {states_count} configurations checked.')
