#!/usr/bin/env python3
from itertools import product

def chain_imp(a, b, n):
    return n - 1 if a <= b else b

def check_farl_chain(f, g, n):
    for x in range(n):
        if f[x] > x:
            return False
        for y in range(n):
            if ((g[x] <= y) != (x <= f[y])):
                return False
            if f[chain_imp(g[x], y, n)] != chain_imp(g[x], f[y], n):
                return False
            if f[max(g[x], y)] != max(g[x], f[y]):
                return False
            if g[min(x, g[y])] != min(g[x], g[y]):
                return False
    return True

def check_mon_chain(f, g, n):
    for x in range(n):
        if chain_imp(f[x], x, n) != n - 1:
            return False
        if g[x] != min(g[x], g[x]):
            return False
        for y in range(n):
            if f[chain_imp(x, f[y], n)] != chain_imp(g[x], f[y], n):
                return False
            if f[chain_imp(f[x], y, n)] != chain_imp(f[x], f[y], n):
                return False
            if f[max(x, g[y])] != max(f[x], g[y]):
                return False
    return True

def rounding_pair(F, n):
    F = sorted(F)
    f = tuple(max(z for z in F if z <= x) for x in range(n))
    g = tuple(min(z for z in F if z >= x) for x in range(n))
    return f, g

# Full pair enumeration through n=4.
for n in range(2, 5):
    farl = set()
    mon = set()
    vals = range(n)
    for f in product(vals, repeat=n):
        for g in product(vals, repeat=n):
            if check_farl_chain(f, g, n):
                farl.add((tuple(f), tuple(g)))
            if check_mon_chain(f, g, n):
                mon.add((tuple(f), tuple(g)))
    expected = {
        rounding_pair(
            {0, n - 1} | {i for i in range(1, n - 1) if (mask >> (i - 1)) & 1},
            n
        )
        for mask in range(1 << (n - 2))
    }
    assert farl == mon == expected

# Exhaust all possible f through n=6; a right adjoint has at most one left adjoint.
for n in range(2, 7):
    found = set()
    for f in product(range(n), repeat=n):
        g = []
        possible = True
        for x in range(n):
            ys = [y for y in range(n) if x <= f[y]]
            if not ys:
                possible = False
                break
            g.append(min(ys))
        if possible:
            g = tuple(g)
            if check_farl_chain(f, g, n):
                found.add((tuple(f), g))
    expected = {
        rounding_pair(
            {0, n - 1} | {i for i in range(1, n - 1) if (mask >> (i - 1)) & 1},
            n
        )
        for mask in range(1 << (n - 2))
    }
    assert found == expected
    assert len(found) == 2 ** (n - 2)

# Constructive check through n=12.
for n in range(2, 13):
    pairs = set()
    for mask in range(1 << (n - 2)):
        F = {0, n - 1} | {i for i in range(1, n - 1) if (mask >> (i - 1)) & 1}
        f, g = rounding_pair(F, n)
        assert check_farl_chain(f, g, n)
        assert check_mon_chain(f, g, n)
        pairs.add((f, g))
    assert len(pairs) == 2 ** (n - 2)

# Non-chain test: G2 x G2, represented by bit pairs.
elts = [(0,0), (0,1), (1,0), (1,1)]
idx = {x:i for i,x in enumerate(elts)}

def leq(a,b):
    return a[0] <= b[0] and a[1] <= b[1]

def meet(a,b):
    return (min(a[0],b[0]), min(a[1],b[1]))

def join(a,b):
    return (max(a[0],b[0]), max(a[1],b[1]))

def imp(a,b):
    return (1 if a[0] <= b[0] else b[0],
            1 if a[1] <= b[1] else b[1])

def check_farl_prod(f, g):
    F = lambda x: elts[f[idx[x]]]
    G = lambda x: elts[g[idx[x]]]
    for x in elts:
        if not leq(F(x), x):
            return False
        for y in elts:
            if (leq(G(x), y) != leq(x, F(y))):
                return False
            if F(imp(G(x), y)) != imp(G(x), F(y)):
                return False
            if F(join(G(x), y)) != join(G(x), F(y)):
                return False
            if G(meet(x, G(y))) != meet(G(x), G(y)):
                return False
    return True

def check_mon_prod(f, g):
    F = lambda x: elts[f[idx[x]]]
    G = lambda x: elts[g[idx[x]]]
    one = (1,1)
    for x in elts:
        if imp(F(x), x) != one:
            return False
        if G(meet(x,x)) != meet(G(x),G(x)):
            return False
        for y in elts:
            if F(imp(x, F(y))) != imp(G(x), F(y)):
                return False
            if F(imp(F(x), y)) != imp(F(x), F(y)):
                return False
            if F(join(x, G(y))) != join(F(x), G(y)):
                return False
    return True

farl = set()
mon = set()
for f in product(range(4), repeat=4):
    for g in product(range(4), repeat=4):
        if check_farl_prod(f,g):
            farl.add((f,g))
        if check_mon_prod(f,g):
            mon.add((f,g))
assert farl == mon
assert farl

print("CHAIN_COUNTS", [2 ** (n - 2) for n in range(2, 8)])
print("PRODUCT_G2xG2_COUNT", len(farl))
print("VERIFY_OK")
