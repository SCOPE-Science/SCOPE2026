"""Exact cubic-coset triple-pattern verification for primes below 900.

All computations use Python integer arithmetic, with no external packages.
Two independent cubical-coset label constructions are cross-checked.
"""
from itertools import product
from math import isqrt

ALL = set(product(range(3), repeat=3))

def primes_below(n):
    sieve = bytearray(b'\x01') * n
    sieve[0:2] = b'\x00\x00'
    for i in range(2, isqrt(n - 1) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = b'\x00' * len(sieve[i*i:n:i])
    return [i for i in range(n) if sieve[i]]

def distinct_prime_factors(n):
    facts = []
    q = 2
    while q*q <= n:
        if n % q == 0:
            facts.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1: facts.append(n)
    return facts

def root_labels(p):
    facs = distinct_prime_factors(p-1)
    g = next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in facs))
    labels = [-1] * p
    z = 1
    for e in range(p-1):
        assert labels[z] == -1
        labels[z] = e%3
        z = z*g%p
    assert z == 1 and labels[0] == -1
    return labels

def cube_labels(p):
    C = {pow(i,3,p) for i in range(1,p)}
    h = next(i for i in range(2,p) if i not in C)
    sets = [C, {h*i%p for i in C}, {h*h*i%p for i in C}]
    assert len(sets[0]) == (p-1)//3
    assert not (sets[0]&sets[1] or sets[1]&sets[2] or sets[0]&sets[2])
    labels = [-1]*p
    for e,values in enumerate(sets):
        for i in values: labels[i] = e
    assert sum(i>=0 for i in labels)==p-1
    return labels

def patterns(a,p):
    return {(a[x],a[x+1],a[x+2]) for x in range(1,p-2)}

def main():
    checked=0; failures={}; odd_prefix=[]
    for p in primes_below(900):
        if p%3 != 1: continue
        a,b = root_labels(p),cube_labels(p)
        # labels 1 and 2 can interchange, but label 0 always agrees
        assert a==b or all((u == 0 and v == 0) or (u in (1,2) and v==3-u) or (u==-1 and v==-1) for u,v in zip(a,b))
        pat=patterns(a,p)
        assert pat==patterns(b,p) or pat=={tuple((0 if v==0 else 3-v) for v in s) for s in patterns(b,p)}
        missing=ALL-pat
        checked += 1
        if missing:
            failures[p]=sorted(missing)
        if p in (151,163,283,307):
            odd_prefix.append((p,len(pat),sorted(missing)))
    assert sorted(failures)==[7,13,19,31,37,43,61,67,79,127,151,163,283]
    assert failures[283]==[(0,0,0)]
    assert all(not failures.get(p) for p in primes_below(900) if p>=307 and p%3==1)
    assert 900-28*isqrt(900)-27>0
    print('VERIFY_OK: exact cubic-coset search for',checked,'primes < 900 (p ≡ 1 mod 3)')
    print('Exceptions:',[(p,len(m)) for p,m in failures.items()])
    print('Boundary:',odd_prefix)
    print('Weil lower-bound at p=900:',900-28*900**0.5-27)
if __name__=='__main__': main()
