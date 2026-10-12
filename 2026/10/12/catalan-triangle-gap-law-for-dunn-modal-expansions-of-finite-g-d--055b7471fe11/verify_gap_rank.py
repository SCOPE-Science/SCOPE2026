from itertools import combinations_with_replacement
from math import comb
from fractions import Fraction

def cat(n):
    return comb(2*n,n)//(n+1)

def T(n,k):
    if k < 0 or k > n: return 0
    return comb(n+k,k) - (comb(n+k,k-1) if k else 0)

def formula(n):
    B=comb(2*n+1,n)
    return [B*T(n,k) for k in range(n+1)]

def brute(n):
    if n==0: return [1]
    N=n+1
    seqs=list(combinations_with_replacement(range(N+1),n))
    ans=[0]*(n+1)
    for b in seqs:
        for d in seqs:
            if all(b[i] <= d[i] for i in range(n)):
                ans[sum(b[i] < d[i] for i in range(n))]+=1
    return ans

def dp(n):
    if n==0: return [1]
    N=n+1
    states=[(a,b) for a in range(N+1) for b in range(a,N+1)]
    D={(a,b):[0]*(n+1) for a,b in states}
    for a,b in states:
        D[a,b][int(a<b)]=1
    for r in range(2,n+1):
        E={(a,b):[0]*(n+1) for a,b in states}
        for u,v in states:
            s=int(u<v)
            for a,b in states:
                if a<=u and b<=v:
                    for k,x in enumerate(D[a,b]):
                        if x and k+s<=n:
                            E[u,v][k+s]+=x
        D=E
    ans=[0]*(n+1)
    for vec in D.values():
        for k,x in enumerate(vec): ans[k]+=x
    return ans

checks=0
for n in range(0,6):
    assert brute(n)==formula(n)
    checks += len(formula(n))
for n in range(0,13):
    assert dp(n)==formula(n)
    checks += len(formula(n))
for n in range(0,51):
    row=formula(n)
    assert sum(row)==comb(2*n+1,n)*cat(n+1)
    assert sum(T(n,k) for k in range(n+1))==cat(n+1)
    if n:
        EJ=Fraction(sum((n-k)*T(n,k) for k in range(n+1)),cat(n+1))
        EF2=Fraction(sum((n-k)*(n-k-1)*T(n,k) for k in range(n+1)),cat(n+1))
        assert EJ==Fraction(2*n,n+3)
        assert EF2==Fraction(6*n*(n-1),(n+3)*(n+4))
        var=EF2+EJ-EJ*EJ
        assert var==Fraction(2*n*(n+1)*(2*n+3),(n+3)**2*(n+4))
        checks += 3
    checks += 2
print("ROWS", [formula(n) for n in range(1,6)])
print("VERIFY_OK", checks, "exact assertions/components")
