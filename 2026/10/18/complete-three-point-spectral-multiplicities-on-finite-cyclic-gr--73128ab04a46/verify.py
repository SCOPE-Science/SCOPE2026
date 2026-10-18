"""Exact, finite verification for three-frequency cyclic spectral-pair counts.

Run with Python 3: python verify.py
The general theorem is proved by CRT and the root-of-unity rigidity lemma;
these finite checks are tests, not substitutes for that proof.
"""
from itertools import combinations
from math import comb


def factor(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            b = 0
            while n % p == 0:
                n //= p
                b += 1
            ans.append((p, b))
        p += 1
    if n > 1:
        ans.append((n, 1))
    return ans


def vp(x, p, b):
    if x == 0:
        return b
    ans = 0
    while ans < b and x % p == 0:
        ans += 1
        x //= p
    return ans


def predicted_count(N, R):
    a = 0
    q = N
    while q % 3 == 0:
        q //= 3
        a += 1
    if not a:
        return 0, None
    pairdiff = [(R[i] - R[j]) % N for i in range(3) for j in range(i)]
    vals3 = [vp(x, 3, a) for x in pairdiff]
    if len(set(vals3)) != 1 or vals3[0] == a:
        return 0, None
    r = vals3[0]
    value = 3 ** (a + 2 * r - 1)
    ks = []
    for p, b in factor(q):
        k = min(vp(x, p, b) for x in pairdiff)
        ks.append((p, b, k))
        value *= p ** (b + 2 * k)
    return value, (r, tuple(ks))


def predicted_total(N):
    a = 0
    q = N
    while q % 3 == 0:
        q //= 3
        a += 1
    if not a:
        return 0
    result = a * 3 ** (4*a-4) * q**2
    for p, b in factor(q):
        result *= p ** (2*b-2)*(p*p+b*(p*p-1))
    return result


def directly_is_hadamard(N, R, C):
    if N % 3:
        return False
    d1, d2 = R[1] - R[0], R[2] - R[0]
    e1, e2 = C[1] - C[0], C[2] - C[0]
    x = ((d1 * e1) % N, (d1 * e2) % N,
         (d2 * e1) % N, (d2 * e2) % N)
    t = N // 3
    return x == (t, 2*t, 2*t, t) or x == (2*t, t, t, 2*t)


def predicted_histogram(N):
    a = 0
    m = N
    while m % 3 == 0:
        m //= 3
        a += 1
    if not a:
        return {0:comb(N,3)}
    outcome = {}
    for r in range(a):
        d = {3**(a+2*r-1): 3**(3*a-2*r-3)}
        for p,b in factor(m):
            nxt = {}
            for value, multiplicity in d.items():
                for k in range(b+1):
                    ways = p**b if k==b else p**(3*b-2*k)-p**(3*b-2*k-2)
                    v = value * p**(b+2*k)
                    nxt[v] = nxt.get(v,0) + multiplicity * ways
            d=nxt
        for v,c in d.items():
            outcome[v] = outcome.get(v,0)+c
    zero=comb(N,3)-sum(outcome.values())
    if zero:
        outcome[0]=zero
    return outcome


def check_N(N):
    triples = list(combinations(range(N),3))
    hist = {}
    total_direct = 0
    for R in triples:
        predicted, _ = predicted_count(N,R)
        direct = sum(directly_is_hadamard(N,R,C) for C in triples)
        assert predicted == direct, (N,R,predicted,direct)
        total_direct += direct
        hist[direct] = hist.get(direct,0)+1
    assert total_direct == predicted_total(N), (N,total_direct,predicted_total(N))
    assert hist == predicted_histogram(N), (N,hist,predicted_histogram(N))
    print(f'N={N:2d} rows={len(triples):4d} spectral_pairs={total_direct:8d} distinct_multiplicities={len(hist)}')


if __name__ == '__main__':
    for n in (3,4,6,8,9,10,12,15,18,21,24):
        check_N(n)
    print('ALL EXACT CHECKS PASSED')
