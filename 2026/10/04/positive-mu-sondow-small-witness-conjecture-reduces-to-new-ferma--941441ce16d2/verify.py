#!/usr/bin/env python3

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d; e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

def is_prime(n):
    return n>=2 and len(factor(n))==1 and factor(n)[0]==(n,1)

def v2(n):
    v=0
    while n%2==0:
        n//=2; v+=1
    return v

def is_power_two(n):
    return n>0 and (n & (n-1))==0

def is_mu_sondow(n, mu):
    for p,e in factor(n):
        if (n//p + mu) % (p**e) != 0:
            return False
    return True

def smallest_prime_factor(n):
    return factor(n)[0][0]

def constructive_witness(mu):
    if mu>=3 and mu%2==1:
        return 2
    if mu>=2 and mu%2==0 and not is_power_two(mu):
        return 2**(v2(mu)+1)
    if is_power_two(mu) and not is_prime(mu+1):
        return smallest_prime_factor(mu+1)
    return None

assert is_mu_sondow(145,256) and 145<=256
assert is_mu_sondow(627,65536) and 627<=65536

# Regression check of the constructive cases.
for mu in range(3,50001):
    n=constructive_witness(mu)
    if n is not None:
        assert 2<=n<=mu, (mu,n)
        assert is_mu_sondow(n,mu), (mu,n)

# Regression check of the classical Fermat-exponent factorization pattern.
for v in range(1,25):
    if is_prime(2**v+1):
        assert is_power_two(v), v

print('VERIFY_OK')
