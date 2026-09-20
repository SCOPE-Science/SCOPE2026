#!/usr/bin/env python3

def primes_lt(n):
    out=[]
    for x in range(2,n):
        ok=True
        d=2
        while d*d<=x:
            if x%d==0:
                ok=False
                break
            d+=1
        if ok:
            out.append(x)
    return out

def sigma_k_prime_power(p,a,k):
    return sum(p**(k*j) for j in range(a+1))

hits=[]
checked=0
for k in range(2,9):
    for a in range(1,9):
        A=sigma_k_prime_power(2,a,k)
        for b in range(1,9):
            for p in primes_lt(500):
                if p==2:
                    continue
                B=sigma_k_prime_power(p,b,k)
                numerator=(2**(a*k))*(p**(b*k))*(a+1)*(b+1)
                checked+=1
                if numerator%(A*B)==0:
                    hits.append((k,a,p,b,numerator//(A*B)))
print(f"checked={checked}")
print(f"hits={len(hits)}")
if hits:
    print(hits)
