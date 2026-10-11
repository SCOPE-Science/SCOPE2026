#!/usr/bin/env python3
"""Exact finite tests for polynomial cellular-automaton boundary classification.

The universal statement is proved separately; this program checks representative
finite cases, the explicit periodic obstruction, and the p-adic inverse procedure.
Requires Python >= 3.9; standard library only.
"""
from itertools import product
from math import gcd
from random import Random

checks = 0

def ck(assertion):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError('exact-arithmetic test %d failed' % checks)

def factors(d):
    n = d
    output = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                e += 1
                n //= p
            output.append((p, e))
        p += 1
    if n > 1:
        output.append((n, 1))
    return output

def radical(d):
    z = 1
    for p, _ in factors(d):
        z *= p
    return z

def admissible(d, c):
    r = radical(d)
    return gcd(c[5], d) == 1 and all(c[i] % r == 0 for i in range(4)) and c[4]*c[6] % r == 0

def local(a, b, z, c, d):
    return (c[0]*a*b*z + c[1]*a*b + c[2]*a*z + c[3]*b*z
            + c[4]*a + c[5]*b + c[6]*z + c[7]) % d

def periodic(x, c, d):
    n = len(x)
    return tuple(local(x[(i-1)%n], x[i], x[(i+1)%n], c, d)
                 for i in range(n))

def null_boundary(x, c, d):
    n = len(x)
    return tuple(local(x[i-1] if i else 0, x[i],
                       x[i+1] if i+1<n else 0, c, d)
                 for i in range(n))

def crt(remainders, bases, d):
    val = 0
    for a, m in zip(remainders, bases):
        q = d // m
        val += a * q * pow(q, -1, m)
    return val % d

def inverse_periodic(y, c, d):
    n = len(y)
    factors_d = factors(d)
    bases = [p**e for p, e in factors_d]
    components = []
    for p, e in factors_d:
        invb = pow(c[5], -1, p)
        x = [((v-c[7])*invb) % p for v in y]
        for k in range(1, e):
            t = p**k
            m = p**(k+1)
            y_next = []
            for i in range(n):
                fx = local(x[(i-1)%n], x[i], x[(i+1)%n], c, m)
                difference = (y[i]-fx) % m
                ck(difference % t == 0)
                digit = ((difference//t)*invb) % p
                y_next.append(x[i]+t*digit)
            x = y_next
        components.append(x)
    return tuple(crt([x[i] for x in components], bases, d) for i in range(n))

def collision_witness(d, c):
    for p, e in factors(d):
        a, b = c[4]%p, c[5]%p
        z = c[6]%p
        if a == 0 and z == 0:
            continue
        ck(a*z % p == 0)
        lam = (-a * pow(b, -1, p)) % p if a else (-b * pow(z, -1, p)) % p
        ck(lam != 0)
        order = 1
        while pow(lam, order, p) != 1:
            order += 1
        ck(order <= p-1)
        witness = tuple((d//p)*pow(lam, i, p) % d for i in range(order))
        ck(any(witness))
        ck(periodic(witness, c, d) == periodic((0,)*order, c, d))
        return True
    return False

rng = Random(1812026)

# All 2-state admissible rules, and all 4-state admissible coefficient
# combinations, checked for injectivity on null-boundary rings of size <= 3.
for d in (2, 4):
    r = radical(d)
    multi = list(range(0, d, r))
    for c0, c1, c2, c3 in product(multi, repeat=4):
        for a, b, z, t in product(range(d), repeat=4):
            c = (c0, c1, c2, c3, a, b, z, t)
            if not admissible(d, c):
                continue
            for n in (1, 2, 3):
                images = {null_boundary(x, c, d) for x in product(range(d), repeat=n)}
                ck(len(images) == d**n)
            if d == 2 or (c0,c1,c2,c3) == (0,0,0,0):
                ck(collision_witness(d,c) == (a%r != 0 or z%r != 0))

# Composite prime power and mixed-prime samples with genuinely nonlinear rules.
for d in (6, 8, 9, 12, 16, 18):
    r = radical(d)
    for rep in range(70):
        c = tuple(r*rng.randrange((d-1)//r+1) % d for _ in range(4))
        a = rng.randrange(d)
        b = rng.choice([u for u in range(d) if gcd(u,d)==1])
        z_candidates = [v for v in range(d) if a*v%r == 0]
        z = rng.choice(z_candidates)
        t = rng.randrange(d)
        c += (a,b,z,t)
        ck(admissible(d,c))
        whether = any(a%p or z%p for p,e in factors(d))
        ck(collision_witness(d,c) == whether)
        if not whether:
            for n in (1,2,3,7):
                for s in range(8):
                    x = tuple(rng.randrange(d) for _ in range(n))
                    y = periodic(x,c,d)
                    ck(inverse_periodic(y,c,d) == x)
        if d <= 9:
            for n in (1,2,3):
                if d**n <= 729:
                    vals = {null_boundary(x,c,d) for x in product(range(d),repeat=n)}
                    ck(len(vals)==d**n)

# The sharpness example F(x)_i = x_i + rad(d) x_(i-1).
for d in (2, 4, 8, 9, 12, 16, 18, 36):
    r = radical(d)
    c = (0,0,0,0,r%d,1,0,0)
    emax = max(e for p,e in factors(d))
    N = 2*emax + 5
    v = [0]*N
    v[0] = 1
    out = inverse_periodic(v,c,d)
    ck(out[(emax-1)%N] % d == (-r)**(emax-1)%d)
    ck(out[(emax-1)%N] != 0)

print('VERIFIED',checks,'exact finite assertions')
