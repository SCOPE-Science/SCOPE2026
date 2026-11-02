"""Numerical and exact finite checks for a weighted Möbius-ladder design theorem.
Standard-library only. Infinite parameter assertions are proved in RESULT.md.
"""
from fractions import Fraction
from math import acosh, tanh, sinh, sqrt, isclose, log
from random import Random


def chebyshev(m,x):
    a,b=1,x
    if m==0: return a
    for _ in range(2,m+1): a,b=b,2*x*b-a
    return b


def determinant_integer(M):
    a=[list(row) for row in M]
    n=len(a); old=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if r is None: return 0
            a[k],a[r]=a[r],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%old==0
                a[i][j]=num//old
        for i in range(k+1,n): a[i][k]=0
        old=pivot
    return sign*a[-1][-1]


def graph_laplacian(m,cycle_weights,rung_weights):
    n=2*m
    L=[[0 for _ in range(n)] for _ in range(n)]
    for i,w in enumerate(cycle_weights):
        j=(i+1)%n
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for i,w in enumerate(rung_weights):
        j=i+m
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    return L


def logdet_float(A):
    a=[list(map(float,row)) for row in A]
    n=len(a); s=0.
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]))
        if abs(a[pivot][k])<1e-14:return float('-inf')
        a[k],a[pivot]=a[pivot],a[k]
        v=a[k][k]
        if v<=0:return float('-inf')
        s+=log(v)
        for i in range(k+1,n):
            z=a[i][k]/v
            for j in range(k+1,n):a[i][j]-=z*a[k][j]
    return s


def difference(m,q,t):
    if t==0: return (m*m-(2*m-1)*q)/2
    u=acosh(1+t)
    return m*tanh(m*u/2)/sqrt(t*(t+2))-(2*m-1)*q/(2+q*t)


def optimal_ratio(m,q):
    assert m>=2 and q>0
    if q>=m*m/(2*m-1):return 0.
    lo,hi=0.,1.
    while difference(m,q,hi)>0:hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if difference(m,q,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def test():
    count=0
    # Independent exact integer matrix-tree determinants versus Chebyshev formula.
    for m in range(2,8):
        for a in (1,2,3):
            for b in (0,1,2,3):
                L=graph_laplacian(m,[a]*(2*m),[b]*m)
                actual=determinant_integer([row[:-1] for row in L[:-1]])
                pred=m*Fraction(a)**(2*m-1)*(chebyshev(m,1+Fraction(b,a))+1)
                assert actual==pred,(m,a,b,actual,pred)
                count+=1
    rng=Random(240617)
    # Compare optimum with independent non-symmetric, budget-normalized allocations.
    for m in range(2,8):
        for q in (0.2,1.,2.,m*m/(2*m-1),2*m):
            B=1.
            t=optimal_ratio(m,q)
            a=B/(m*(2+q*t)); b=t*a
            cand=logdet_float([row[:-1] for row in graph_laplacian(m,[a]*(2*m),[b]*m)[:-1]])
            assert abs(difference(m,q,0))<1e-12 if q==m*m/(2*m-1) else True
            if t>1e-10:
                assert abs(difference(m,q,t))<1e-8,(m,q,t,difference(m,q,t))
                count+=1
            for trial in range(24):
                edge=[rng.expovariate(1) for _ in range(3*m)]
                norm=sum(edge[:2*m])+q*sum(edge[2*m:])
                c=[x/norm for x in edge[:2*m]]
                d=[x/norm for x in edge[2*m:]]
                z=logdet_float([row[:-1] for row in graph_laplacian(m,c,d)[:-1]])
                assert cand>=z-2e-10,(m,q,t,cand,z)
                count+=1
    # Two independent asymptotic regimes (not a substitute for analysis).
    for q in (.2,.5,1.,3.):
        limiting=2*(1-2*q+sqrt((2*q-1)**2+3))/(3*q)
        assert abs(optimal_ratio(5000,q)/limiting-1)<0.004
        count+=1
    for alpha in (.12,.25,.4):
        lo,hi=1e-9,50.
        for _ in range(100):
            s=(lo+hi)/2
            if tanh(s/2)/s>alpha:lo=s
            else:hi=s
        s=(lo+hi)/2
        r=optimal_ratio(8000,alpha*8000)
        assert abs(8000**2*r/(s*s/2)-1)<0.003,(alpha,r,s)
        count+=1
    print(f'PASS exact determinants, unrestricted competitor comparisons, asymptotics: {count} assertions')

if __name__=='__main__':test()
