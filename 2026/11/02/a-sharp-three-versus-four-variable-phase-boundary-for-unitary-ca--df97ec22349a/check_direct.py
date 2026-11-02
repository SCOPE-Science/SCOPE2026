"""Independent finite graph verification for unitary Cayley adjacency.

Only uses finite vertex enumeration and bitset adjacency; no theorem assumptions.
"""
from itertools import combinations, product
from math import gcd
import json


def prime_data(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            factors.append((d,e))
        d += 1
    if n > 1:
        factors.append((n,1))
    return factors


def e_c_counts(neigh):
    n = len(neigh)
    mask = (1 << n) - 1
    minimum = [n] * 4
    for a,b in combinations(range(n),2):
        available = mask & ~((1 << a) | (1 << b))
        both = neigh[a] & neigh[b] & available
        only_a = neigh[a] & ~neigh[b] & available
        only_b = ~neigh[a] & neigh[b] & available
        neither = ~neigh[a] & ~neigh[b] & available
        for i,bits in enumerate((neither,only_b,only_a,both)):
            minimum[i] = min(minimum[i], bits.bit_count())
    return minimum


def residue_graph(n):
    return [sum(1 << b for b in range(n) if gcd(a-b,n) == 1)
            for a in range(n)]


def product_graph(q):
    vertices = list(product(*(range(x) for x in q)))
    return [sum(1 << j for j,b in enumerate(vertices)
                if all(x!=y for x,y in zip(a,b))) for a in vertices]


# Check every modulus in a contiguous range, including nonsquarefree cases.
moduli = list(range(2,151))
mod_errors = []
mod_pass = []
critical_moduli = []
for n in moduli:
    p = prime_data(n)
    pred = len(p) >= 2 and p[0][0] >= 3 and all(e == 1 for _,e in p)
    minima = e_c_counts(residue_graph(n))
    actual = min(minima) >= 1
    if actual != pred:
        mod_errors.append((n,p,minima,pred))
    if actual:
        mod_pass.append(n)
        if min(minima) == 1:
            critical_moduli.append(n)
assert not mod_errors, mod_errors

# A second representation: categorical products on coordinate tuples.
profiles = [(3,3),(3,4),(3,5),(4,4),(3,3,3),(3,3,4),
            (3,4,4),(4,4,4),(3,3,3,3),(3,5,5),
            (2,3),(2,3,3),(3,),(4,)]
profile_errors = []
profile_results = []
for q in profiles:
    minima = e_c_counts(product_graph(q))
    actual = min(minima) > 0
    pred = len(q)>=2 and min(q)>=3
    critical = actual and min(minima)==1
    expected_critical = actual and ((len(q)==2 and 3 in q)
                                     or (len(q)>=3 and all(x==3 for x in q)))
    if (actual,critical)!=(pred,expected_critical):
        profile_errors.append((q,minima))
    profile_results.append([list(q),minima,critical])
assert not profile_errors, profile_errors
print(json.dumps({"moduli_checked":len(moduli),
                  "2ec_moduli":mod_pass,
                  "critical_2ec_moduli":critical_moduli,
                  "product_profiles_checked":len(profiles),
                  "product_results":profile_results,
                  "error_count":len(mod_errors)+len(profile_errors)},
                 sort_keys=True,separators=(',',':')))
