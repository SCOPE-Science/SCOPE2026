#!/usr/bin/env python3
"""Exact independent finite enumeration of the common-shift-gcd-four stratum."""
from math import gcd, isqrt

def prime(n):
    if n < 2:
        return False
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            return False
    return True

def divs(n):
    low, high = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]

def parametrized(p):
    seen = set()
    for a in range(1, p):
        for z in divs((p + 1) * (p + a)):
            q = z - 1
            if q <= p or not prime(q):
                continue
            M = p * q - 1
            if M % a:
                continue
            r = M // a - 1
            if r <= q or not prime(r):
                continue
            if (q*r-1) % (p+1) == 0 and (p*r-1) % (q+1) == 0:
                seen.add((p,q,r))
    return seen

def direct(p):
    seen = set()
    for q in range(p+1, 2*p*p+p-1):
        if not prime(q):
            continue
        for d in divs(p*q-1):
            r = d-1
            if r<=q or not prime(r):
                continue
            n=p*q*r
            if all((n+1)%(z+1)==0 for z in (p,q,r)):
                seen.add((p,q,r))
    return seen

def main():
    ps=[4*a-1 for a in range(1,11) if prime(4*a-1)]
    assert ps==[3,7,11,19,23,31]
    answers=[]
    table=[]
    for p in ps:
        got=parametrized(p)
        assert got==direct(p),('mismatched algorithms',p,got ^ direct(p))
        four=sorted(t for t in got if gcd(gcd(t[0]+1,t[1]+1),t[2]+1)==4)
        answers.extend(four)
        table.append((p,len(got),len(four)))
    expect=[(3,7,19),(7,19,43),(11,31,67),(19,83,787),(23,67,139)]
    assert sorted(answers)==expect,answers
    assert all(prime(z) for row in answers for z in row)
    print('VERIFY_OK:',len(ps),'possible smallest primes; full direct/parametrized agreement; table',table)
    print('COMPLETE_G4_TRIPLES:', sorted(answers))
    print('NUMBERS:',[p*q*r for p,q,r in sorted(answers)])
if __name__=='__main__':
    main()
