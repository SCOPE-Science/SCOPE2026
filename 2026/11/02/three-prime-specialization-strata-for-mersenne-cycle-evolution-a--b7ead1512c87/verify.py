#!/usr/bin/env python3
"""Reproduce finite-field counts for cyclic evolution-algebra arithmetic strata."""
from math import gcd

def prime(p):
    return p >= 2 and all(p%d for d in range(2,int(p**0.5)+1))

def predicted(n,p):
    L=(1<<n)-1
    g=gcd(L,p-1)
    residue=pow(2,(p-1)//g,p)==1
    return (g if residue else 0), (n*g if residue else g)

def actual(n,p):
    c=[1]*(n-1)+[2]
    count_idem=0
    for a in range(1,p):
        x=[a]
        for i in range(n-1):
            x.append((x[-1]*x[-1])%p)
        if all(x[(i+1)%n] == (x[i]*x[i]*c[i])%p for i in range(n)):
            count_idem+=1
    aut=0
    # monomial forms with shifts s; solve product-preservation equations exactly
    for s in range(n):
        for a in range(1,p):
            v=[a]
            for i in range(n-1):
                v.append((v[-1]**2 * c[(i+s)%n] * pow(c[i],-1,p))%p)
            if all((c[i]*v[(i+1)%n]- v[i]*v[i]*c[(i+s)%n])%p==0 for i in range(n)):
                aut+=1
    return count_idem,aut

if __name__=='__main__':
    total=0
    for n in (3,5,7):
        assert prime((1<<n)-1)
        for p in (q for q in range(3,152,2) if prime(q)):
            a=actual(n,p)
            b=predicted(n,p)
            assert a==b,(n,p,a,b)
            total+=1
    for n,p in ((3,631),(5,683),(7,78233)):
        assert actual(n,p)==predicted(n,p)==((1<<n)-1,n*((1<<n)-1)),(n,p)
    print('VERIFY_OK exhaustive_prime_field_cases=',total,'high_residue_cases=3')
