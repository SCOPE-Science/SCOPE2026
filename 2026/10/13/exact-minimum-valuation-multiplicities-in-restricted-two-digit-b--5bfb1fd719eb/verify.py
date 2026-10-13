#!/usr/bin/env python3
"""Exact integer checks for minimal valuations of restricted binomial rows."""
from math import comb


def valuation_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


def valuation_binomial(N, k, p):
    return valuation_factorial(N, p) - valuation_factorial(k, p) - valuation_factorial(N-k, p)


def digit_sum(n, p):
    out = 0
    while n:
        out += n % p
        n //= p
    return out


def valuation_by_digit_sums(N, k, p):
    return (digit_sum(k, p) + digit_sum(N-k, p) - digit_sum(N, p)) // (p-1)


def expected_count(p, m, s, t):
    assert p >= 2 and m >= 3 and (p+1) % m == 0
    assert s >= 0 and t > s and (t-s) % 2 == 1
    assert p**s + p**t > m
    if p > m:
        h = (p+1)//m - 1
        return h * (1 + 2*(s >= 1) if t == s+1 else 2*(1+(s>=1)))
    if t == s+1:
        return (p-1)*(1 if s == 1 else 3)
    return (p-1)*(2 if s == 0 else 3 if s == 1 else 5)


def structural_candidates(p, m, s, t):
    gap = t-s
    N = p**s + p**t
    candidates = set()
    if p > m:
        if s >= 1:
            for d in range(1,p):
                for e in (0,1):
                    candidates.add(d*p**(s-1) + e*p**t)
        if gap == 1:
            for d in range(2,p):
                candidates.add(d*p**s)
        else:
            for d in range(1,p):
                for e in (0,1):
                    candidates.add(d*p**(t-1) + e*p**s)
    else:
        if s >= 2:
            for d in range(1,p):
                for c in range(p):
                    for e in (0,1):
                        candidates.add(d*p**(s-2)+c*p**(s-1)+e*p**t)
        if gap == 1:
            if s >= 1:
                for d in range(1,p):
                    for c in range(1,p):
                        candidates.add(d*p**(s-1) + c*p**s)
        else:
            for d in range(1,p):
                for c in range(p):
                    for e in (0,1):
                        candidates.add(d*p**(t-2)+c*p**(t-1)+e*p**s)
            if s >= 1:
                for d in range(1,p):
                    for e in range(1,p):
                        candidates.add(d*p**(s-1)+e*p**(t-1))
    return {k for k in candidates if 0 < k < N and k % m == 0}


def is_prime(n):
    if n < 2: return False
    for j in range(2,int(n**0.5)+1):
        if n%j == 0:return False
    return True


def run():
    exhaustive_cases = 0
    checked_coefficients = 0
    candidate_checks = 0
    largest_n = 0
    signature_examples = []
    for p in [2,3,5,7,11,13,17,19,23]:
        assert is_prime(p)
        for m in range(3,p+2):
            if (p+1)%m: continue
            for s in range(0,6):
                for gap in (1,3,5,7):
                    t = s+gap
                    N = p**s+p**t
                    if N<=m: continue
                    pred = expected_count(p,m,s,t)
                    candidates = structural_candidates(p,m,s,t)
                    if len(candidates)!=pred:
                        raise AssertionError(('candidate-count',p,m,s,t,pred,len(candidates)))
                    needle = 1 if p>m else 2
                    for k in candidates:
                        if valuation_binomial(N,k,p)!=needle:
                            raise AssertionError(('candidate-valuation',p,m,s,t,k))
                    candidate_checks += len(candidates)
                    if N>35000: continue
                    actual = []
                    for k in range(m,N,m):
                        v1 = valuation_binomial(N,k,p)
                        v2 = valuation_by_digit_sums(N,k,p)
                        if v1 != v2:
                            raise AssertionError(('independent-valuations',p,m,s,t,k,v1,v2))
                        if v1<needle:raise AssertionError(('lower-valuation',p,m,s,t,k,v1))
                        if v1==needle:actual.append(k)
                        checked_coefficients += 1
                    if set(actual)!=candidates:
                        raise AssertionError(('exact-support',p,m,s,t,set(actual)^candidates))
                    assert len(actual)==pred
                    exhaustive_cases+=1
                    largest_n=max(largest_n,N)
                    if (p,m,s,t) in [(2,3,1,2),(2,3,0,3),(3,4,2,5),(5,3,1,4),(11,3,1,2)]:
                        signature_examples.append([p,m,s,t,N,pred])
    # Direct integer binomial check, independent of digit/Legendre implementations.
    direct_comb_checks = 0
    for p,m,s,t in [(2,3,1,4),(3,4,2,3),(5,3,1,2),(7,4,1,2)]:
        N=p**s+p**t
        for k in range(m,N,m):
            x=comb(N,k)
            v=0
            while x%p==0:
                x//=p
                v+=1
            assert v==valuation_binomial(N,k,p)
            direct_comb_checks+=1
    print('exact integer checks: PASS')
    print('exhaustive parameter cases:',exhaustive_cases)
    print('exhaustively evaluated binomial coefficients:',checked_coefficients)
    print('constructive witnesses checked:',candidate_checks)
    print('independent direct-binomial checks:',direct_comb_checks)
    print('largest exhaustively checked N:',largest_n)
    print('sample (p,m,s,t,N,count):',signature_examples)

if __name__=='__main__':run()
