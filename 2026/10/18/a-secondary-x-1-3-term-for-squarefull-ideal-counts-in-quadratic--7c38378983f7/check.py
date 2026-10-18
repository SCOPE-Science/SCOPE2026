"""Finite coefficient checks for squarefull ideals in the Gaussian integers.
All calculations use exact integer arithmetic and Python's standard library.
The tests are illustrations, not a proof of an asymptotic formula.
"""
from math import isqrt


def primes_up_to(n):
    isprime = [True] * (n + 1)
    isprime[:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if isprime[p]:
            for k in range(p*p, n+1, p):
                isprime[k] = False
    return [p for p in range(2,n+1) if isprime[p]]


def ordinary_ideal_prefix(n):
    # zeta_{Q(i)}(s) = zeta(s) L(s,chi_{-4}).
    a = [0] * (n+1)
    for d in range(1,n+1,2):
        chi = 1 if d % 4 == 1 else -1
        for m in range(d,n+1,d):
            a[m] += chi
    totals = [0] * (n+1)
    for m in range(1,n+1):
        totals[m] = totals[m-1] + a[m]
    return totals


def squarefree_ideal_norm_coefficients(n):
    b = [0] * (n+1)
    b[1] = 1
    for p in primes_up_to(n):
        if p == 2:
            local = [(p,1)]
        elif p % 4 == 1:
            local = [(p,2),(p*p,1)]
        else:
            local = [(p*p,1)]
        nxt = b[:]
        for m in range(1,n+1):
            if b[m]:
                for factor,weight in local:
                    if m*factor <= n:
                        nxt[m*factor] += weight*b[m]
        b = nxt
    return b


def direct_squarefull_ideal_coefficients(n):
    spf = list(range(n+1))
    for p in range(2,isqrt(n)+1):
        if spf[p] == p:
            for k in range(p*p,n+1,p):
                if spf[k] == k:
                    spf[k] = p
    result=[0]*(n+1)
    result[1]=1
    for m in range(2,n+1):
        temp=m
        coefficient=1
        while temp>1:
            p=spf[temp]
            k=0
            while temp%p==0:
                temp//=p
                k+=1
            if p==2:
                local = int(k>=2)
            elif p%4==1:
                local = 0 if k==1 else (1 if k==0 else max(2,k-1))
            else:
                local = int(k>=4 and k%2==0)
            coefficient *= local
        result[m]=coefficient
    return result


def count_via_square_cube(x, prefix, squarefree):
    total=0
    for b in range(1,len(squarefree)):
        if b*b*b>x:
            break
        total += squarefree[b]*prefix[isqrt(x//(b*b*b))]
    return total


def verify():
    limit=200000
    prefix=ordinary_ideal_prefix(isqrt(limit))
    squarefree=squarefree_ideal_norm_coefficients(100)
    direct=direct_squarefull_ideal_coefficients(limit)
    cumulative=0
    for n in range(1,limit+1):
        cumulative+=direct[n]
        if n in (100,1000,10000,50000,200000):
            counted=count_via_square_cube(n,prefix,squarefree)
            assert counted == cumulative,(n,counted,cumulative)
            print('bound',n,'squarefull_gaussian_ideals',counted)
    print('Exact comparisons passed at five bounds; no asymptotic conclusion is inferred from these finite tests.')

if __name__=='__main__':
    verify()
