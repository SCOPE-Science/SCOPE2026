from itertools import product
from math import prod

def add_A(x, z, mods):
    return tuple((a+b) % m for a,b,m in zip(x,z,mods))

def neg_A(x, mods):
    return tuple((-a) % m for a,m in zip(x,mods))

def elements_A(mods):
    return [tuple(v) for v in product(*[range(m) for m in mods])]

def zero_A(mods):
    return tuple(0 for _ in mods)

def mul_dic(x, z, mods, y):
    a,e = x
    b,f = z
    term = b if e == 0 else neg_A(b, mods)
    c = add_A(a, term, mods)
    if e and f:
        c = add_A(c, y, mods)
    return (c, e ^ f)

def cyclic_subgroup(elements, identity, mul, g):
    H = {identity}
    x = identity
    while True:
        x = mul(x, g)
        if x in H:
            break
        H.add(x)
    return frozenset(H)

def all_cyclic_subgroups(elements, identity, mul):
    return list({cyclic_subgroup(elements, identity, mul, g) for g in elements})

def hasse_edges(subgroups):
    E = set()
    for H in subgroups:
        for K in subgroups:
            if len(H) >= len(K) or not H < K:
                continue
            if not any(len(H) < len(L) < len(K) and H < L < K for L in subgroups):
                E.add((H,K))
    return E

def edge_count_A(mods):
    els = elements_A(mods)
    z = zero_A(mods)
    subs = all_cyclic_subgroups(els, z, lambda a,b: add_A(a,b,mods))
    return len(hasse_edges(subs))

def edge_count_dic(mods, y):
    A = elements_A(mods)
    els = [(a,e) for a in A for e in (0,1)]
    z = (zero_A(mods),0)
    subs = all_cyclic_subgroups(els, z, lambda a,b: mul_dic(a,b,mods,y))
    return len(hasse_edges(subs)), subs

def factorint(n):
    f = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            f[p] = f.get(p,0) + 1
            n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        f[n] = f.get(n,0) + 1
    return f

def ecyc(n):
    exps = list(factorint(n).values())
    if not exps:
        return 0
    ans = 0
    for i,a in enumerate(exps):
        term = a
        for j,b in enumerate(exps):
            if i != j:
                term *= (b+1)
        ans += term
    return ans

def tau(n):
    ans = 1
    for a in factorint(n).values():
        ans *= a+1
    return ans

tests = [
    ((2,), (1,)),
    ((4,), (2,)),
    ((6,), (3,)),
    ((8,), (4,)),
    ((2,2), (1,0)),
    ((2,2), (1,1)),
    ((2,4), (1,0)),
    ((2,4), (0,2)),
    ((2,6), (1,0)),
    ((4,4), (2,0)),
    ((4,4), (2,2)),
]

for mods,y in tests:
    m = prod(mods)
    eA = edge_count_A(mods)
    eG, subs = edge_count_dic(mods,y)
    assert eG == eA + m//2, (mods,y,eG,eA,m)
    assert eG >= ecyc(2*m), (mods,y,eG,ecyc(2*m))
    if eG == ecyc(2*m):
        assert mods in ((2,), (6,)), (mods,y)

for s in range(1, 402, 2):
    f = tau(s) + ecyc(s)
    assert f <= s, (s,f)
    if f == s:
        assert s in (1,3), (s,f)

for m in range(2, 402, 2):
    d = ecyc(m) + m//2 - ecyc(2*m)
    assert d >= 0, (m,d)
    if d == 0:
        assert m in (2,6), (m,d)

print("VERIFY_OK")
