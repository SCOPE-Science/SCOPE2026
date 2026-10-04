#!/usr/bin/env python3
from itertools import combinations

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def div_exact(a, b):
    a = a[:]
    b = trim(b[:])
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        assert b[-1] in (1, -1)
        c = a[-1] // b[-1]
        k = len(a) - len(b)
        q[k] = c
        for i, bi in enumerate(b):
            a[i+k] -= c * bi
        trim(a)
    assert not any(a)
    return trim(q)

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def cyclotomics(nmax):
    phi = {}
    for n in range(1, nmax+1):
        p = [-1] + [0] * (n-1) + [1]
        for d in divisors(n):
            if d != n:
                p = div_exact(p, phi[d])
        phi[n] = p
    return phi

def rem_mod(p, m):
    p = trim(p[:])
    m = trim(m[:])
    while len(p) >= len(m):
        c = p[-1] // m[-1]
        k = len(p) - len(m)
        for i, mi in enumerate(m):
            p[i+k] -= c * mi
        trim(p)
    return tuple(p)

def add_vecs(vecs):
    L = max((len(v) for v in vecs), default=1)
    s = [0] * L
    for v in vecs:
        for i, x in enumerate(v):
            s[i] += x
    while len(s) > 1 and s[-1] == 0:
        s.pop()
    return tuple(s)

def add_poly(A, B, scale=1):
    C = dict(A)
    for e, c in B.items():
        C[e] = C.get(e, 0) + scale*c
        if C[e] == 0:
            del C[e]
    return C

def mul_poly(A, B):
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(ea[i] + eb[i] for i in range(4))
            C[e] = C.get(e, 0) + ca*cb
    return {e:c for e,c in C.items() if c}

def var(i, power=1):
    e = [0]*4
    e[i] = power
    return {tuple(e):1}

def sign_perm(p):
    inv = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv % 2 else 1

def perms(xs):
    if not xs:
        yield ()
    else:
        for i, x in enumerate(xs):
            for q in perms(xs[:i] + xs[i+1:]):
                yield (x,) + q

# Exact generalized-Vandermonde factorization for row exponents 0,1,2,4.
exps = (0,1,2,4)
D = {}
for p in perms((0,1,2,3)):
    mon = {(0,0,0,0):sign_perm(p)}
    for row, col in enumerate(p):
        mon = mul_poly(mon, var(col, exps[row]))
    D = add_poly(D, mon)
V = {(0,0,0,0):1}
for i in range(4):
    for j in range(i+1,4):
        V = mul_poly(V, add_poly(var(j), var(i), scale=-1))
S = {}
for i in range(4):
    S = add_poly(S, var(i))
assert D == mul_poly(V, S)

# Exact root-of-unity check: a polynomial vanishes at a primitive Nth root
# exactly when its remainder modulo the integer cyclotomic polynomial Phi_N is zero.
Nmax = 40
phi = cyclotomics(Nmax)
total = 0
singular = 0
for N in range(5, Nmax+1):
    reps = []
    for c in range(N):
        p = [0] * (c+1)
        p[c] = 1
        reps.append(rem_mod(p, phi[N]))
    count = 0
    for C in combinations(range(N), 4):
        total += 1
        zsum = add_vecs([reps[c] for c in C])
        iszero = all(x == 0 for x in zsum)
        if N % 2:
            predicted = False
        else:
            h = N//2
            residues = {c % h for c in C}
            predicted = len(residues) == 2 and all(sum(d % h == r for d in C) == 2 for r in residues)
        assert iszero == predicted, (N, C, iszero, predicted)
        if iszero:
            count += 1
            singular += 1
    expected = 0 if N % 2 else (N//2)*(N//2-1)//2
    assert count == expected, (N, count, expected)

print(f'VERIFY_OK N_max={Nmax} subsets={total} singular={singular} determinant_identity=exact')
