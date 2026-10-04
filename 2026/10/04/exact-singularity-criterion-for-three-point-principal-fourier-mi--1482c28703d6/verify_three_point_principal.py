#!/usr/bin/env python3
from math import gcd

MAX_N = 120

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def div_exact_monic(num, den):
    num = num[:]
    den = trim(den[:])
    assert den[-1] == 1
    if len(num) < len(den):
        raise AssertionError('nondivisible')
    q = [0] * (len(num) - len(den) + 1)
    while len(num) >= len(den):
        k = len(num) - len(den)
        c = num[-1]
        q[k] = c
        if c:
            for i, d in enumerate(den):
                num[i+k] -= c*d
        trim(num)
    if any(num):
        raise AssertionError(('nonzero remainder', num, den))
    return trim(q)

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def cyclotomics(M):
    phis = {1: [-1, 1]}
    for n in range(2, M+1):
        p = [-1] + [0]*(n-1) + [1]
        for d in divisors(n):
            if d < n:
                p = div_exact_monic(p, phis[d])
        phis[n] = p
    return phis

def power_remainders(phi, N):
    d = len(phi)-1
    rem = []
    v = [0]*d
    v[0] = 1
    rem.append(tuple(v))
    for _ in range(1, N):
        w = [0]*d
        top = v[-1]
        for i in range(d-1, 0, -1):
            w[i] = v[i-1]
        if top:
            # x^d = -sum_{i<d} phi[i] x^i
            for i in range(d):
                w[i] -= top*phi[i]
        v = w
        rem.append(tuple(v))
    return rem

def determinant_zero_exact(N, a, b, rem):
    d = len(rem[0])
    acc = [0]*d
    terms = [
        ((a*a+b*b) % N, 1),
        ((a*b) % N, 2),
        ((a*a) % N, -1),
        ((b*b) % N, -1),
        ((2*a*b) % N, -1),
    ]
    for e,c in terms:
        r = rem[e]
        for i in range(d):
            acc[i] += c*r[i]
    return all(v == 0 for v in acc)

def criterion(N, a, b):
    return (
        ((a*a) % N == 0 and (a*b) % N == 0)
        or ((b*b) % N == 0 and (a*b) % N == 0)
        or (((b-a)*(b-a)) % N == 0 and (a*(b-a)) % N == 0)
    )

def symmetric_criterion(N, pts):
    x,y,z = pts
    triples = [(x,y,z),(x,z,y),(y,z,x)]
    return any(((u-v)*(u-v)) % N == 0 and ((u-v)*(u-w)) % N == 0
               for u,v,w in triples)

def order_coset_criterion(N, pts):
    x,y,z = pts
    triples = [(x,y,z),(x,z,y),(y,z,x)]
    for u,v,w in triples:
        d = (u-v) % N
        q = N // gcd(N, d)
        if N % (q*q) == 0 and (u-w) % q == 0:
            return True
    return False

def main():
    phis = cyclotomics(MAX_N)
    pairs = 0
    singular = 0
    squarefree_n = 0
    for N in range(3, MAX_N+1):
        rem = power_remainders(phis[N], N)
        # Sanity: x^N-1 vanishes modulo Phi_N by construction; x^0..x^(N-1) reps suffice.
        sf = all(N % (p*p) for p in range(2, int(N**0.5)+1))
        if sf:
            squarefree_n += 1
        for a in range(1, N):
            for b in range(a+1, N):
                pairs += 1
                dz = determinant_zero_exact(N,a,b,rem)
                cr = criterion(N,a,b)
                sr = symmetric_criterion(N,(0,a,b))
                oc = order_coset_criterion(N,(0,a,b))
                if cr != sr or cr != oc:
                    raise AssertionError(('criterion equivalence mismatch',N,a,b,cr,sr,oc))
                if dz != cr:
                    raise AssertionError(('determinant mismatch',N,a,b,dz,cr))
                if dz:
                    singular += 1
                    if sf:
                        raise AssertionError(('squarefree singularity',N,a,b))
    print('MAX_N', MAX_N)
    print('NORMALIZED_TRIPLES', pairs)
    print('SINGULAR_NORMALIZED_TRIPLES', singular)
    print('SQUAREFREE_MODULI', squarefree_n)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
