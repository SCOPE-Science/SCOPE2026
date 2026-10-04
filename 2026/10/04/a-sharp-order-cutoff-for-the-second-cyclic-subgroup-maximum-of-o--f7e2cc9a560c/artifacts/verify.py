from itertools import product
from math import gcd

def M(p, n):
    num = 2*p**(n-1) - p**(n-2) + p - 2
    assert num % (p-1) == 0
    return num // (p-1)

def wreath_formula(p):
    num = p**(p-2)*(3*p*p - 3*p + 1) + p - 2
    assert num % (p-1) == 0
    return num // (p-1)

def addv(a, b, p):
    return tuple((x+y) % p for x,y in zip(a,b))

def shift(v, j):
    n = len(v)
    j %= n
    if j == 0:
        return v
    return v[-j:] + v[:-j]

def mul_wreath(x, y, p):
    v, i = x
    w, j = y
    return (addv(v, shift(w, i), p), (i+j) % p)

def identity_wreath(p):
    return ((0,)*p, 0)

def order_wreath(g, p):
    e = identity_wreath(p)
    x = e
    for k in range(1, p*p + 1):
        x = mul_wreath(x, g, p)
        if x == e:
            return k
    raise AssertionError("order bound failed")

def phi_prime_power_order(o, p):
    if o == 1:
        return 1
    if o == p:
        return p-1
    if o == p*p:
        return p*(p-1)
    raise AssertionError((p,o))

def brute_wreath(p):
    vecs = list(product(range(p), repeat=p))
    counts = {1:0, p:0, p*p:0}
    cyclic_weight_num = 0
    for v in vecs:
        for j in range(p):
            o = order_wreath((v,j), p)
            counts[o] += 1
    assert sum(counts.values()) == p**(p+1)
    # Number of cyclic subgroups from element orders.
    c = 1 + counts[p]//(p-1) + counts[p*p]//(p*(p-1))
    assert counts[p] % (p-1) == 0
    assert counts[p*p] % (p*(p-1)) == 0
    return counts, c

def order_mod_tuple(x, mods):
    o = 1
    for a,m in zip(x,mods):
        if a == 0:
            oi = 1
        else:
            oi = m // gcd(a,m)
        # lcm
        o = o*oi//gcd(o,oi)
    return o

def brute_abelian_equality(p,n):
    mods = (p*p,) + (p,)*(n-2)
    counts = {}
    for x in product(*[range(m) for m in mods]):
        o = order_mod_tuple(x,mods)
        counts[o] = counts.get(o,0)+1
    assert set(counts) <= {1,p,p*p}
    c = 1 + counts.get(p,0)//(p-1) + counts.get(p*p,0)//(p*(p-1))
    return c

# Symbolic-integer algebra checks over a broad numerical range.
for p in (3,5,7,11,13):
    for n in range(3, min(p+3, 9)):
        assert M(p,n) == (2*p**(n-1) - p**(n-2) + p - 2)//(p-1)
    diff = wreath_formula(p) - M(p,p+1)
    assert diff == p**(p-2)*(p-1)
    assert diff > 0

# Equality examples.
for p,n in ((3,3),(3,4),(5,3),(5,4)):
    assert brute_abelian_equality(p,n) == M(p,n), (p,n)

# Direct full wreath enumerations.  p=5 has 15625 elements.
for p in (3,5):
    counts,c = brute_wreath(p)
    expected_solutions = p**(p-1)*(2*p-1)
    assert counts[1] + counts[p] == expected_solutions, (p,counts)
    assert counts[p*p] == p**(p+1)-expected_solutions, (p,counts)
    assert c == wreath_formula(p), (p,c,wreath_formula(p))
    assert c == M(p,p+1) + p**(p-2)*(p-1)
    if p == 3:
        assert c == 29
    if p == 5:
        assert c == 1907

print("VERIFY_OK")
