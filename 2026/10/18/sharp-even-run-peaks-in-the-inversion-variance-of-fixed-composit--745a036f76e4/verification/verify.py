"""Exact reproducibility checks for inversion dispersion at fixed binary run count.

All arithmetic is exact; no external libraries are needed. Finite checks
support, but do not replace, the general composition-moment proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb

checks = 0

def equal(got, expected, label):
    global checks
    assert got == expected, (label, got, expected)
    checks += 1

def formula_even(m, n, k):
    assert 1 <= k <= min(m, n)
    N, P = m + n, m * n
    return F(P * ((k+2)*(2*P-(k-1)*N)+k*(k-1)), 12*k*(k+1))

def formula_odd(m, n, k):
    assert 1 <= k <= min(m, n) and m+n > 2*k
    N, P = m+n, m*n
    return F(P, 12*(k+1)) * (
        2*P-k*(N-1)-1+F(N*N-8*P+2*k*N, N-2*k))

def formula(m, n, r):
    if r % 2 == 0:
        return formula_even(m, n, r//2)
    return formula_odd(m, n, (r-1)//2)

def exact_moments(m, n):
    N = m+n
    buckets = defaultdict(list)
    for positions in combinations(range(N), m):
        ones = set(positions)
        seq = [int(i in ones) for i in range(N)]
        runs = 1+sum(seq[i]!=seq[i-1] for i in range(1,N))
        count_ones = 0
        inv = 0
        for x in seq:
            if x: count_ones += 1
            else: inv += count_ones
        buckets[runs].append(inv)
    for r, vals in buckets.items():
        t = len(vals)
        mean = F(sum(vals),t)
        var = F(sum(x*x for x in vals),t) - mean**2
        equal(mean,F(m*n,2),(m,n,r,'conditional mean'))
        equal(var,formula(m,n,r),(m,n,r,'conditional variance'))
        if r%2==0:
            k=r//2
            equal(t,2*comb(m-1,k-1)*comb(n-1,k-1),(m,n,r,'even count'))
        else:
            k=(r-1)//2
            def c(a,b): return comb(a,b) if 0 <= b <= a else 0
            expected = c(m-1,k)*c(n-1,k-1)+c(m-1,k-1)*c(n-1,k)
            equal(t,expected,(m,n,r,'odd count'))
    return buckets

for m in range(1,9):
    for n in range(1,9):
        buckets = exact_moments(m,n)
        feasible = sorted(buckets)
        for r in feasible:
            if r%2==0 and r+1 in buckets:
                assert formula(m,n,r)>formula(m,n,r+1)
                checks+=1
            if r%2==0 and r-1 in buckets:
                assert formula(m,n,r)>formula(m,n,r-1)
                checks+=1
            if r%2==0 and r+2 in buckets:
                assert formula(m,n,r)>formula(m,n,r+2)
                checks+=1

# Symbolic-free, exact reconstruction of the variance from uniform compositions.
def matrix_variance(m,n,r,s,start_one):
    C = [[int(i<=j if start_one else i<j)
          for j in range(s)] for i in range(r)]
    T = sum(map(sum,C))
    rows = [sum(row) for row in C]
    cols = [sum(C[i][j] for i in range(r)) for j in range(s)]
    ca = F(m*(m-r),r*(r+1))
    cb = F(n*(n-s),s*(s+1))
    trow = sum((F(v)-F(T,r))**2 for v in rows)
    tcol = sum((F(v)-F(T,s))**2 for v in cols)
    q = sum((F(C[i][j])-F(rows[i],s)-F(cols[j],r)+F(T,r*s))**2
            for i in range(r) for j in range(s))
    mu = F(m*n*T,r*s)
    v = F(n*n,s*s)*ca*trow+F(m*m,r*r)*cb*tcol+ca*cb*q
    return mu,v

for m in range(1,24):
    for n in range(1,24):
        for k in range(1,min(m,n)+1):
            mu1,v1 = matrix_variance(m,n,k,k,True)
            mu0,v0 = matrix_variance(m,n,k,k,False)
            mean = (mu1+mu0)/2
            var = (v1+v0)/2 + ((mu1-mu0)/2)**2
            equal(mean,F(m*n,2),(m,n,k,'even mean, matrix'))
            equal(var,formula_even(m,n,k),(m,n,k,'even matrix'))
            if m+n > 2*k:
                mu1,v1 = matrix_variance(m,n,k+1,k,True)
                mu0,v0 = matrix_variance(m,n,k,k+1,False)
                a,b = m-k,n-k
                mean = F((a*mu1+b*mu0),a+b)
                var = F(a,a+b)*(v1+(mu1-mean)**2)+F(b,a+b)*(v0+(mu0-mean)**2)
                equal(mean,F(m*n,2),(m,n,k,'odd mean, matrix'))
                equal(var,formula_odd(m,n,k),(m,n,k,'odd matrix'))

for m in range(1,40):
    for n in range(1,40):
        N,P=m+n,m*n
        for k in range(1,min(m,n)+1):
            if N>2*k:
                difference= F(N*P*(2*P-N*(k-1)-2*k),6*k*(N-2*k)*(k+1))
                equal(formula_even(m,n,k)-formula_odd(m,n,k),difference,(m,n,k,'right parity gap'))
                assert difference>0
                checks+=1
            if k>=2:
                a,b=m-k,n-k
                num=(a*a*b+a*b*b+(4*k+6)*a*b+(k*k+4*k+3)*(a+b)+2*(k+1)**2)
                difference=F(P*num,6*k*(k+1)*(a+b+2))
                equal(formula_even(m,n,k)-formula_odd(m,n,k-1),difference,(m,n,k,'left parity gap'))
                assert difference>0
                checks+=1
            if k<min(m,n):
                difference=F(P*(2*N+P*k+4*P-k),6*k*(k+1)*(k+2))
                equal(formula_even(m,n,k)-formula_even(m,n,k+1),difference,(m,n,k,'even monotonicity'))
                assert difference>0
                checks+=1

print(f'{checks} exact assertions passed')
