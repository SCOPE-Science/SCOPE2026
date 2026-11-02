#!/usr/bin/env python3
"""Exact finite census of quadratic-conic-free points in PG(2, GF(64)).

Field encoding: GF(2)[t]/(t^6+t+1), elements bitpacked 0..63.
All loops have explicit finite bounds: 4096 affine points, 63 conics,
512 candidate binary matrices, and at most 168 automorphisms per orbit.
"""
from collections import Counter

MOD = 0b1000011

def mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= MOD
    return r

def power(a, k):
    r = 1
    while k:
        if k & 1:
            r = mul(r, a)
        a = mul(a, a)
        k >>= 1
    return r

def poly_rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def poly_gcd(a, b):
    while b:
        a, b = b, poly_rem(a, b)
    return a

def poly_power_x_mod(n):
    x = 2
    for _ in range(n):
        x = poly_rem(mul_poly(x, x), MOD)
    return x

def mul_poly(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return r

def rank_bit_vectors(vectors):
    pivots = [0]*6
    for vec in vectors:
        while vec:
            i = vec.bit_length()-1
            if pivots[i]:
                vec ^= pivots[i]
            else:
                pivots[i] = vec
                break
    return sum(z != 0 for z in pivots)

assert poly_power_x_mod(6) == 2
assert poly_gcd(MOD, poly_power_x_mod(2) ^ 2) == 1
assert poly_gcd(MOD, poly_power_x_mod(3) ^ 2) == 1
assert all(mul(power(a, 62), a)==1 for a in range(1, 64))

# Two independent criteria: binary rank and vanishing of any of 63 F2 conics.
def quadratic_values(a,b):
    return (1, a, b, mul(a,a), mul(a,b), mul(b,b))

def lies_on_binary_conic(vals):
    for mask in range(1,64):
        value=0
        for i in range(6):
            if mask & (1<<i):
                value ^= vals[i]
        if value==0:
            return True
    return False

good=set()
ranks=Counter()
for a in range(64):
    for b in range(64):
        vals = quadratic_values(a,b)
        rank = rank_bit_vectors(vals)
        ranks[rank]+=1
        no_conic=not lies_on_binary_conic(vals)
        assert (rank==6)==no_conic
        if no_conic:
            good.add((a,b))
assert ranks == {1:4, 2:12, 3:384, 5:2352, 6:1344}, ranks
assert len(good)==1344
assert (2,16) in good and quadratic_values(2,16)==(1,2,16,4,32,12)
# No point at infinity can qualify: the nonzero F2 conic X_0 X_1=0 contains it.
assert all(lies_on_binary_conic((0,0,0,1,b,mul(b,b))) for b in range(64))

# Enumerate GL(3,F2): every projective transformation over F2 is one of these.
def rank3(rows):
    pivots=[0,0,0]
    for r in rows:
        while r:
            i=r.bit_length()-1
            if pivots[i]:r^=pivots[i]
            else:pivots[i]=r;break
    return sum(z!=0 for z in pivots)
matrices=[(i & 7,(i>>3)&7,(i>>6)&7) for i in range(512)
          if rank3((i&7,(i>>3)&7,(i>>6)&7))==3]
assert len(matrices)==168

def action(A, p):
    v=(1,p[0],p[1])
    w=[]
    for row in A:
        z=0
        for i in range(3):
            if row & (1<<i):z^=v[i]
        w.append(z)
    assert w[0] != 0
    scale=power(w[0],62)
    return (mul(w[1],scale),mul(w[2],scale))

remaining=good.copy()
orbits=[]
while remaining:
    rep=min(remaining)
    orbit={action(A,rep) for A in matrices}
    assert len(orbit)==168, (rep,len(orbit))
    assert orbit<=remaining
    remaining-=orbit
    orbits.append((rep,orbit))
reps=[p for p,o in orbits]
assert reps == [(2,16),(2,20),(2,24),(2,40),(2,44),(2,48),(4,24),(4,50)]
assert len(orbits)==8
labels={point:j for j,(_,orbit) in enumerate(orbits) for point in orbit}
frob=[labels[(mul(p[0],p[0]),mul(p[1],p[1]))] for p in reps]
assert frob==[5,6,3,7,1,0,2,4],frob
seen=set();cycles=[]
for i in range(8):
    if i not in seen:
        cycle=[];j=i
        while j not in seen:
            seen.add(j);cycle.append(j);j=frob[j]
        assert j==i
        cycles.append(cycle)
assert cycles==[[0,5],[1,6,2,3,7,4]],cycles
# Every good point has a full 6-element Frobenius orbit.
assert all(len({(power(a,2**k),power(b,2**k)) for k in range(6)})==6 for a,b in good)
assert len(good)//6==224
print('F64_QUADRATIC_ORBIT_CENSUS_PASS')
print('good=1344, frobenius_sextuples=224, GL3_orbits=8*168')
print('reps=',reps)
print('frobenius_orbit_cycles=',cycles,'combined_orbit_sizes=',[336,1008])
print('affine_rank_spectrum=',dict(sorted(ranks.items())))
