#!/usr/bin/env python3
from itertools import product
from collections import Counter

def factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

def primitive_root(p):
    phi = p-1
    fac = factors(phi)
    for g in range(2,p):
        if all(pow(g, phi//r, p) != 1 for r in fac):
            return g
    raise AssertionError("no primitive root")

def rank_mod(A,p):
    A = [[x % p for x in row] for row in A]
    r = 0
    nrow = len(A)
    ncol = len(A[0]) if A else 0
    for c in range(ncol):
        piv = next((i for i in range(r,nrow) if A[i][c] % p), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p-2, p)
        A[r] = [(x*inv) % p for x in A[r]]
        for i in range(nrow):
            if i != r and A[i][c] % p:
                f = A[i][c] % p
                A[i] = [(a-f*b) % p for a,b in zip(A[i],A[r])]
        r += 1
        if r == nrow:
            break
    return r

def hull_dim_direct(q,k,eta):
    n = 2*k
    assert (q-1) % n == 0
    root = pow(primitive_root(q), (q-1)//n, q)
    alpha = [pow(root,j,q) for j in range(n)]
    V = [[pow(a,e,q) for a in alpha] for e in range(n)]

    G = []
    for i in range(1,k+1):
        e = k+i-1
        G.append([(V[i-1][j] + eta[i-1]*V[e][j]) % q for j in range(n)])

    H = []
    for m in range(1,k+1):
        i = k+1-m
        e2 = (n-i+1) % n
        H.append([(V[m][j] - eta[i-1]*V[e2][j]) % q for j in range(n)])

    return n-rank_mod(G+H,q)

def hull_dim_formula(q,k,eta):
    h = 1 if (eta[0]*eta[0] + 1) % q == 0 else 0
    for i in range(2,k+1):
        j = k+2-i
        if (eta[i-1] + eta[j-1]) % q == 0:
            h += 1
    return h

def predicted_hist(q,k):
    rq = 2 if q % 4 == 1 else 0
    p = (k-1)//2
    f = 1 if k % 2 == 0 else 0
    # polynomial as Counter degree -> coefficient
    P = Counter({0:q-1-rq, 1:rq})
    pair = Counter({0:(q-1)*(q-2), 2:q-1})
    for _ in range(p):
        Q = Counter()
        for a,ca in P.items():
            for b,cb in pair.items():
                Q[a+b] += ca*cb
        P = Q
    if f:
        P = Counter({d:c*(q-1) for d,c in P.items()})
    return P

expected = {
    (13,3): Counter({0:1320,1:264,2:120,3:24}),
    (19,3): Counter({0:5508,2:324}),
    (17,4): Counter({0:53760,1:7680,2:3584,3:512}),
}

for q,k in expected:
    observed = Counter()
    for eta in product(range(1,q), repeat=k):
        hd = hull_dim_direct(q,k,eta)
        assert hd == hull_dim_formula(q,k,eta)
        observed[hd] += 1
    assert observed == predicted_hist(q,k)
    assert observed == expected[(q,k)]
    assert sum(observed.values()) == (q-1)**k

print("VERIFY_OK")
