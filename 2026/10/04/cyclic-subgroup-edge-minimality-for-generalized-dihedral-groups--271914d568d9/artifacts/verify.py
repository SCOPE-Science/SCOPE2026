from itertools import product
from math import prod

def add_A(x, y, mods):
    return tuple((a+b) % m for a,b,m in zip(x,y,mods))

def neg_A(x, mods):
    return tuple((-a) % m for a,m in zip(x,mods))

def mul_dih(x, y, mods):
    a,e = x
    b,f = y
    if e:
        b = neg_A(b, mods)
    return (add_A(a,b,mods), (e+f) & 1)

def identity_A(mods):
    return tuple(0 for _ in mods)

def elements_A(mods):
    return [tuple(x) for x in product(*[range(m) for m in mods])]

def elements_dih(mods):
    return [(a,e) for a in elements_A(mods) for e in (0,1)]

def cyclic_subgroup(elements, identity, mul, g):
    seen = {identity}
    x = identity
    while True:
        x = mul(x, g)
        if x in seen:
            break
        seen.add(x)
    return frozenset(seen)

def all_cyclic_subgroups(elements, identity, mul):
    return sorted(
        {cyclic_subgroup(elements, identity, mul, g) for g in elements},
        key=lambda s: (len(s), tuple(sorted(map(str,s))))
    )

def hasse_edge_count(subgroups):
    e = 0
    for i,H in enumerate(subgroups):
        for K in subgroups[i+1:]:
            if len(H) >= len(K) or not H < K:
                continue
            covered = True
            for L in subgroups:
                if len(H) < len(L) < len(K) and H < L and L < K:
                    covered = False
                    break
            if covered:
                e += 1
    return e

def edge_count_A(mods):
    els = elements_A(mods)
    z = identity_A(mods)
    return hasse_edge_count(
        all_cyclic_subgroups(els, z, lambda x,y: add_A(x,y,mods))
    )

def edge_count_dih(mods):
    els = elements_dih(mods)
    z = (identity_A(mods),0)
    return hasse_edge_count(
        all_cyclic_subgroups(els, z, lambda x,y: mul_dih(x,y,mods))
    )

def edge_count_cyclic(n):
    return edge_count_A((n,))

def tau(n):
    ans = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            ans *= a+1
        p += 1 if p == 2 else 2
    if n > 1:
        ans *= 2
    return ans

tests = [
    (3,), (5,), (7,), (9,), (11,),
    (3,3), (3,5), (3,7), (5,5),
    (3,3,3), (9,3)
]

for mods in tests:
    m = prod(mods)
    eA = edge_count_A(mods)
    eG = edge_count_dih(mods)
    eC = edge_count_cyclic(2*m)
    assert eG == eA + m, (mods, eG, eA+m)
    assert eG >= eC, (mods, eG, eC)
    if eG == eC:
        assert mods == (3,), (mods, eG, eC)

for m in range(3, 302, 2):
    em = edge_count_cyclic(m)
    assert tau(m) + em <= m, (m, tau(m), em)
    if tau(m) + em == m:
        assert m == 3, m

print("VERIFY_OK")
