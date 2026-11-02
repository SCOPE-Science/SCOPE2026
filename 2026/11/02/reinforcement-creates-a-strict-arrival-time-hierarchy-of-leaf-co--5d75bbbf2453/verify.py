#!/usr/bin/env python3
"""Exact checks for root-attachment/leaf dependence in affine recursive trees.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import factorial

CHECKS = 0

def eq(x, y, where):
    global CHECKS
    CHECKS += 1
    if x != y:
        raise AssertionError(f'{where}: got {x}, expected {y}')

def strict(x, y, where):
    global CHECKS
    CHECKS += 1
    if not x > y:
        raise AssertionError(f'{where}: {x} is not > {y}')

def exact_formula(a, n):
    """Return exact theoretical covariance and attachment contributions."""
    a = F(a)
    s = lambda k: (a+1)*k-a
    r = {2: a+1}
    h = {2: F(1)}
    for k in range(2, n):
        r[k+1] = r[k]*(1+a/s(k))
        h[k+1] = h[k]*(1+(a-1)/s(k))
    cov = {k: (r[k]-(a+1)*h[k])/(a+2) for k in range(2,n+1)}
    contributions = {}
    for j in range(3,n+1):
        w = (a*cov[j-1]+r[j-1]/(a+2))/s(j-1)
        for k in range(j,n):
            w *= 1-1/s(k)
        contributions[j] = w
    return cov[n], contributions, r, h

def enumerate_moments(a, n):
    """Independent direct enumeration of every increasing parent history."""
    a = F(a)
    sums = [F(0)]*(3+n)
    leaves = [F(0)]*(n+1)
    parents = [0]*(n+1)
    degree = [0]*(n+1)
    histories = 0
    def visit(k, p):
        nonlocal histories
        if k>n:
            histories += 1
            d = degree[1]
            leaf = sum(degree[x]==0 for x in range(1,n+1))
            sums[0] += p
            sums[1] += p*d
            sums[2] += p*leaf
            sums[3] += p*d*leaf
            for j in range(3,n+1):
                if parents[j]==1:
                    sums[j+1] += p
                    leaves[j] += p*leaf
            return
        s = (a+1)*(k-1)-a
        for u in range(1,k):
            q = p*(1+a*degree[u])/s
            degree[u] += 1
            parents[k]=u
            visit(k+1,q)
            degree[u] -= 1
    visit(2,F(1))
    eq(histories,factorial(n-1),('history count',a,n))
    eq(sums[0],F(1),('mass',a,n))
    ecov=sums[3]-sums[1]*sums[2]
    w={j:leaves[j]-sums[j+1]*sums[2] for j in range(3,n+1)}
    return ecov,w,sums[2]

def main():
    for a in (F(0),F(1,2),F(1),F(2)):
        for n in range(2,9):
            cov, w, r, h = exact_formula(a,n)
            actual, wa, leaf_mean = enumerate_moments(a,n)
            eq(actual,cov,('covariance',a,n))
            eq(leaf_mean,((a+1)*n-a)/(a+2),('leaf mean',a,n))
            eq(sum(w.values()),cov,('sum of arrival contributions',a,n))
            for j in w:
                eq(w[j],wa[j],('arrival contribution',a,n,j))
                strict(w[j],0,('strict positive arrival covariance',a,n,j))
                if j<n:
                    sj=(a+1)*j-a
                    sp=(a+1)*(j-1)-a
                    q=F(1)
                    for t in range(j+1,n):
                        st=(a+1)*t-a
                        q*=1-F(1,1)/st
                    expected_gap=q*a*(a+1)*h[j-1]/((a+2)*sp*sj)
                    eq(w[j+1]-w[j],expected_gap,('exact gap',a,n,j))
                    if a == 0:
                        eq(w[j+1],w[j],('equal contributions in zero reinforcement',a,n,j))
                    else:
                        strict(w[j+1],w[j],('strict increasing contributions',a,n,j))
    for a in (F(0),F(1,2),F(1),F(2),F(7)):
        for n in range(2,60):
            c, w, r, h=exact_formula(a,n)
            eq(sum(w.values()),c,('symbolic telescoping',a,n))
            if n>=3:
                strict(c,F(0),('positive final covariance',a,n))
            else:
                eq(c,F(0),('deterministic initial covariance',a,n))
            if a==0 and n>=3:
                for v in w.values():
                    eq(v,F(1,2*(n-1)),('classical equal-share identity',a,n))
            if a==1:
                from math import comb
                eq(r[n],F(4**(n-1),comb(2*n-2,n-1)),('plane recursive root expectation',n))
                eq(h[n],F(1),('plane recursive h',n))
    print('PASS:', CHECKS, 'exact assertions, including complete parent-history enumeration for n<=8.')

if __name__=='__main__':
    main()
