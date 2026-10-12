#!/usr/bin/env python3
"""Exact integer checks of prime-power gamma full periods and parity moments.
No external dependencies or claims of exhaustive verification of unbounded parameters.
"""
import json
from math import gcd


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def order(b,m):
    if gcd(b,m) != 1:
        raise ValueError('base must be a unit')
    v=b%m; t=1
    while v!=1:
        v=v*b%m; t+=1
    return t


def gamma_from_inverse(m,c):
    return int(pow(c,-1,m) % 2 == 0)


def gamma_direct(m,c):
    assert m%2==1 and m>=3 and c>=2 and gcd(m,c)==1
    T=(m-1)*(c-1)//2
    hits=[]
    for epsilon in (0,1):
        for y in range(m):
            r=T-epsilon-c*y
            if r>=0 and r%m==0:
                hits.append(epsilon)
    assert len(hits)==1, (m,c,hits)
    return hits[0]


def least_period(seq):
    n=len(seq)
    for d in range(1,n+1):
        if n%d==0 and all(seq[i]==seq[(i+d)%n] for i in range(n)):
            return d
    assert False


def main():
    count_cases=0; checked_positions=0; moments=0; primitive_bases=0; diophantine_checks=0
    exemplars=[]
    for p in range(3,51,2):
        if not isprime(p): continue
        e=1; m=p
        while m<=1500:
            n=m-m//p
            E=[u for u in range(2,m,2) if u%p]
            S=sum(E)
            assert 4*S == (p-1)*(p**(2*e-1)+1), (p,e,m,S)
            assert gcd(S,m)==1
            moments+=1
            bases=[b for b in range(2,min(m+2,32)) if gcd(b,m)==1 and order(b,m)==n]
            for b in bases:
                seq=[gamma_from_inverse(m,pow(b,i,m)) for i in range(1,n+1)]
                assert least_period(seq)==n, (p,e,b,seq)
                assert sum(seq)==n//2
                assert all(seq[i+n//2] == 1-seq[i] for i in range(n//2))
                primitive_bases+=1
                checked_positions+=n
                if len(exemplars)<6: exemplars.append({'p':p,'e':e,'base':b,'period':n,'ones':sum(seq)})
            count_cases+=1
            e+=1; m*=p
    for a in range(3,27,2):
        for b in range(2,9):
            if gcd(a,b)>1:continue
            for i in range(1,6):
                c=b**i
                if c>200000:continue
                assert gamma_direct(a,c)==gamma_from_inverse(a,c),(a,b,i)
                diophantine_checks+=1
    assert order(2,49)==21 and order(3,49)==42
    assert least_period([gamma_from_inverse(49,pow(3,i,49)) for i in range(1,43)])==42
    assert order(3,121)==5
    x=[gamma_from_inverse(121,pow(3,i,121)) for i in range(1,6)]
    assert least_period(x)==1 and set(x)=={0}
    result={'prime_power_moduli':count_cases, 'verified_even_unit_moments':moments,
            'primitive_base_cases':primitive_bases,'binary_sequence_positions_checked':checked_positions,
            'direct_Diophantine_solvability_checks':diophantine_checks,
            'nonprimitive_counterexample':{'modulus':121,'base':3,'order':5,'gamma_least_period':1},
            'non_dyadic_example':{'modulus':49,'order_of_2':21,'primitive_base':3,'full_gamma_period':42},
            'sample_cases':exemplars,'outcome':'PASS'}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
