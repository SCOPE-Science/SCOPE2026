"""Independent finite-state checks for the Bernoulli--Laplace fixed-time profile.

All finite equalities use exact fractions. Numerical TV checks are diagnostics,
not substitutes for the asymptotic proof. Python 3.10+, standard library only.
"""
from fractions import Fraction
from math import comb, sqrt, erf

checks = 0

def check(ok, label):
    global checks
    assert ok, label
    checks += 1

def hg(n, reds, k):
    denom = comb(n, k)
    return {j: Fraction(comb(reds, j) * comb(n-reds, k-j), denom)
            for j in range(max(0, k-(n-reds)), min(k, reds)+1)}

def matrix(n,k):
    rows=[]
    for x in range(n+1):
        a,b=hg(n,x,k),hg(n,n-x,k)
        row=[Fraction(0) for _ in range(n+1)]
        for j,p in a.items():
            for h,q in b.items():
                row[x-j+h]+=p*q
        rows.append(row)
    return rows

def mean(v): return sum(i*p for i,p in enumerate(v))
def variance(v):
    mu=mean(v)
    return sum((i-mu)**2*p for i,p in enumerate(v))

def tv(v,w):return sum(abs(a-b) for a,b in zip(v,w))/2

def stationary(n):
    den=comb(2*n,n)
    return [Fraction(comb(n,j)**2,den) for j in range(n+1)]

for n in (4,6,8,10,12):
    for k in range(1,n):
        p=matrix(n,k); pi=stationary(n)
        check(sum(pi)==1, f'pi norm {n,k}')
        for x in range(n+1):
            check(sum(p[x])==1,f'row norm {n,k,x}')
            check(mean(p[x])==Fraction(n,2)+Fraction(n-2*k,n)*(Fraction(x)-Fraction(n,2)),f'mean {n,k,x}')
            check(variance(p[x])==Fraction(2*k*(n-k)*x*(n-x),n*n*(n-1)),f'variance {n,k,x}')
            for y in range(n+1):
                check(pi[x]*p[x][y]==pi[y]*p[y][x],f'detailed balance {n,k,x,y}')
        for y in range(n+1):
            check(sum(pi[x]*p[x][y] for x in range(n+1))==pi[y],f'stationarity {n,k,y}')
        if k==n//2:
            check(p[0][n//2]==1,f'deterministic first step {n}')
            two=[sum(p[0][z]*p[z][y] for z in range(n+1)) for y in range(n+1)]
            check(0<tv(two,pi)<tv(p[0],pi),f'decrease in two steps {n}')

# Numeric probability kernels with exact-ratio hypergeometric masses at larger sizes.
# We deliberately do not infer limit theorems from these finite tests.
def flt_row(n,k,x):
    l,r=hg(n,x,k),hg(n,n-x,k)
    ans=[0.0]*(n+1)
    for i,pi in l.items():
        for j,pj in r.items(): ans[x-i+j]+=float(pi)*float(pj)
    return ans

def float_stationary(n):
    den=comb(2*n,n)
    return [comb(n,j)**2/den for j in range(n+1)]

def float_step(v,n,k):
    result=[0.0]*(n+1)
    for x,w in enumerate(v):
        if w<1e-15: continue
        row=flt_row(n,k,x)
        for y,p in enumerate(row): result[y]+=w*p
    return result

def float_tv(a,b):return 0.5*sum(abs(x-y) for x,y in zip(a,b))

for n in (20,32,48,64,80):
    for delta in (0,1,2,3):
        k=n//2+delta
        pi=float_stationary(n)
        v=[0.0]*(n+1);v[0]=1.0
        v=float_step(v,n,k)
        check(abs(sum(v)-1)<1e-10,f'float normalization {n,k}')
        v=float_step(v,n,k)
        assert 0 <= float_tv(v,pi) <= 1
        if delta==0:
            check(float_tv(v,pi)<0.032,f'half-swap 2-step TV {n}')
            if n==80:print('diagnostic n=80 half-swap two-step TV',float_tv(v,pi))

print('PASS: exact finite assertions and numeric diagnostics:',checks)
