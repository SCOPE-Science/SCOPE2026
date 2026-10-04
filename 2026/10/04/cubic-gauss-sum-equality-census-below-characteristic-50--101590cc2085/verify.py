#!/usr/bin/env python3
import math
from collections import defaultdict

PRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]
EXPECTED = {
    11: [
        [(95,855,1045),(285,475,1235),(665,)],
    ],
    23: [
        [(869,7821,9559),(2607,4345,11297),(6083,)],
    ],
    37: [
        [(3618,32562,39798),(10854,18090,47034),(25326,)],
        [(1206,30150,44622),(15678,22914,37386)],
        [(5427,34371,48843),(19899,27135,41607)],
        [(6030,20502,49446),(13266,27738,34974)],
        [(1809,16281,45225),(9045,23517,30753)],
    ],
}

def ds3(x,p):
    return x % p + (x // p) % p + x // (p*p)

def nu3(x,p,fact):
    return fact[x % p] * fact[(x // p) % p] * fact[x // (p*p)] % p

def orbit(c,p,n):
    out=[]
    x=c
    while x not in out:
        out.append(x)
        x=(x*p) % n
    return tuple(sorted(out))

def normalized_classes(classes):
    return sorted([tuple(sorted(tuple(o) for o in cls)) for cls in classes])

def classify(p):
    n=p**3-1
    fact=[math.factorial(i) % p for i in range(p)]
    units=[u for u in range(1,n) if math.gcd(u,n)==1]
    # A separating subset gives a rigorous coarse partition: any true equality
    # must survive every tested unit. Remaining multi-orbit cells are then
    # checked against every unit modulo n.
    probes=list(dict.fromkeys(units[:20] + [units[(j*len(units))//21] for j in range(1,21)]))
    groups=defaultdict(list)
    for c in range(n):
        key=[nu3(c,p,fact)]
        key.extend(ds3((u*c)%n,p) for u in probes)
        groups[tuple(key)].append(c)
    candidates=[]
    for cs in groups.values():
        if len({orbit(c,p,n) for c in cs}) > 1:
            candidates.append(cs)
    exact=[]
    for cs in candidates:
        refined=defaultdict(list)
        for c in cs:
            vec=bytes(ds3((u*c)%n,p) for u in units)
            refined[(nu3(c,p,fact),vec)].append(c)
        for sub in refined.values():
            ors=sorted({orbit(c,p,n) for c in sub})
            if len(ors)>1:
                exact.append(ors)
    return n, len(units), probes, exact

total_chars=0
total_units=0
observed={}
for p in PRIMES:
    n,phi,probes,classes=classify(p)
    total_chars += n
    total_units += phi
    if classes:
        observed[p]=classes
    exp=EXPECTED.get(p,[])
    assert normalized_classes(classes) == normalized_classes(exp), (p,classes,exp)

# Structural checks for the new p=37 phenomena.
n=37**3-1
assert n==50652
# Orders represented by each p=37 equality class.
orders=[]
for cls in EXPECTED[37]:
    orders.append([n//math.gcd(n,orb[0]) for orb in cls])
assert orders == [[14,14,2],[42,42],[28,28],[42,42],[28,28]]
# The order-28 representatives have non-midpoint digit sums, so they are not
# in the midpoint pure-sum situation of Proposition 2.13 of the source paper.
mid=3*(37-1)//2
assert mid==54
assert [ds3(c,37) for c in (1809,9045,5427,19899)] == [45,45,63,63]
# Evans' order-14 family applies at p=11,23,37 because 2 lies in <p> mod 7.
for p in (11,23,37):
    seen={1}
    x=p%7
    while x not in seen:
        seen.add(x); x=(x*p)%7
    assert 2 in seen

print(
    'VERIFY_OK '
    f'primes={len(PRIMES)} total_characters={total_chars} '
    f'exceptional_primes={sorted(observed)} '
    f'p37_classes={len(observed[37])} '
    f'p37_orders={orders} order28_digits=[45,45,63,63]'
)
