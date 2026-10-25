"""Reproducibility checks for cost-weighted D-optimal crown-network allocation.

Python >=3.10 standard library only. These finite checks complement, not replace,
the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, log
import random


def laplacian(n, w):
    size = 2*n
    L = [[F(0) for _ in range(size)] for __ in range(size)]
    for i in range(n):
        for j in range(n):
            c = F(w[i*n+j]); u=i; v=n+j
            L[u][u] += c; L[v][v] += c
            L[u][v] -= c; L[v][u] -= c
    return [row[:-1] for row in L[:-1]]


def fraction_det(A):
    a=[row[:] for row in A]
    d=F(1)
    for k in range(len(a)):
        p=next((i for i in range(k,len(a)) if a[i][k]),None)
        if p is None: return F(0)
        if p!=k:
            a[k],a[p]=a[p],a[k];d=-d
        piv=a[k][k]; d*=piv
        for i in range(k+1,len(a)):
            r=a[i][k]/piv
            if not r:continue
            for j in range(k+1,len(a)):
                a[i][j]-=r*a[k][j]
            a[i][k]=0
    return d


def inverse(A):
    n=len(A)
    a=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if a[i][k])
        if p!=k:a[k],a[p]=a[p],a[k]
        piv=a[k][k]
        a[k]=[x/piv for x in a[k]]
        for i in range(n):
            if i==k:continue
            r=a[i][k]
            if r:a[i]=[a[i][j]-r*a[k][j] for j in range(2*n)]
    return [row[n:] for row in a]


def resistance(inv, u, v, anchor):
    if u==anchor: return inv[v][v]
    if v==anchor: return inv[u][u]
    return inv[u][u]+inv[v][v]-2*inv[u][v]


def candidate(n, cost, B=1):
    tau0=n*(2*n-3)/((n-2)*(2*n-1))
    if cost>=tau0:
        return 0., B/(n*(n-1))
    z=(n-2*cost*(n-1)+sqrt(n*(n+2*cost**2-2*cost)))/(2*cost)
    b=B/(n*(cost*z+n-1))
    return z*b, b


def logdet_float(n, weights):
    N=2*n-1
    A=[[0.0]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            c=float(weights[i*n+j]); u=i; v=n+j
            if u<N: A[u][u]+=c
            if v<N: A[v][v]+=c
            if u<N and v<N: A[u][v]-=c; A[v][u]-=c
    ans=0.0
    for i in range(N):
        s=A[i][i]-sum(A[i][k]**2 for k in range(i))
        if s<=0: return float('-inf')
        diag=sqrt(s); A[i][i]=diag;ans+=2*log(diag)
        for j in range(i+1,N):
            A[j][i]=(A[j][i]-sum(A[j][k]*A[i][k] for k in range(i)))/diag
    return ans


def run():
    exact=0
    for n in range(3,9):
        for a,b in [(F(0),F(1)),(F(1),F(1)),(F(2),F(3)),(F(5,3),F(2,7))]:
            w=[a if i==j else b for i in range(n) for j in range(n)]
            actual=fraction_det(laplacian(n,w))
            expected=n**(n-2)*b**(n-1)*(a+(n-1)*b)*(2*a+(n-2)*b)**(n-1)
            assert actual==expected,(n,a,b,actual,expected)
            exact+=1
    print('exact_weighted_matrix_tree_determinants',exact)
    res=0
    for n in range(3,9):
        b=F(1,2)
        w=[F(0) if i==j else b for i in range(n) for j in range(n)]
        inv=inverse(laplacian(n,w)); anchor=2*n-1
        Rm=resistance(inv,0,n,anchor)
        Rb=resistance(inv,0,n+1,anchor)
        expected_m=F(2*n-3,(n-1)*(n-2))*1/b
        expected_b=F(2*n-1,n*(n-1))*1/b
        assert Rm==expected_m and Rb==expected_b
        assert Rm/Rb==F(n*(2*n-3),(n-2)*(2*n-1))
        res+=3
    print('exact_crown_resistance_and_price_ratio_checks',res)
    cases=0; comps=0
    rng=random.Random(360047)
    for n in range(3,10):
        tc=n*(2*n-3)/((n-2)*(2*n-1))
        for cost in [F(1,3),F(1),F(9,10)*F(n*(2*n-3),(n-2)*(2*n-1)), F(n*(2*n-3),(n-2)*(2*n-1)), F(11,10)*F(n*(2*n-3),(n-2)*(2*n-1)), F(5)]:
            t=float(cost)
            a,b=candidate(n,t)
            assert a>=-1e-13 and b>0
            assert abs(n*t*a+n*(n-1)*b-1)<5e-12
            wstar=[a if i==j else b for i in range(n) for j in range(n)]
            optimum=logdet_float(n,wstar)
            norm=n*t*a+n*(n-1)*b
            for _ in range(105):
                free=[max(1e-8,rng.expovariate(1)) for _ in range(n*n)]
                scale=sum((t if i==j else 1)*free[i*n+j] for i in range(n) for j in range(n))
                w=[u/scale for u in free]
                value=logdet_float(n,w)
                assert value <= optimum+1e-7,(n,t,value,optimum)
                comps+=1
            cases+=1
    print('numerical_parameter_cases',cases)
    print('independent_random_feasible_comparisons',comps)
    for n in range(3,101):
        tc=n*(2*n-3)/((n-2)*(2*n-1))
        assert tc>1
        a,b=candidate(n,tc)
        assert abs(a)<1e-10
        aa,bb=candidate(n,1.0)
        assert abs(aa-bb)<2e-12
    print('budget_and_threshold_boundary_checks',98*2)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':run()
