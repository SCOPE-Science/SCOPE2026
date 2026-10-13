"""Exact finite-field certificate for the seven-power Grassmannian color spectrum.

No external modules. Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations, permutations

POLY=0x43  # T^6+T+1 in binary

def mul(a,b):
    assert 0 <= a < 64 and 0 <= b < 64
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1
        a <<= 1
        if a&64: a ^= POLY
    return z

def power(a,n):
    r=1
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a); n>>=1
    return r

assert all(power(x,63)==1 for x in range(1,64))
assert len({power(x,7) for x in range(1,64)})==9
# Check field polynomial has no zero divisors (sufficient for this tiny field).
assert all(mul(a,b)!=0 for a in range(1,64) for b in range(1,64))

# Full RREF enumeration, pivots leading in each row (little-endian columns).
# RREF constraint: nonpivot/free entries in row i may occur only to right of pivot i.
spaces={}
for piv in combinations(range(6),3):
    free=[j for j in range(6) if j not in piv]
    pos=[(i,j) for i in range(3) for j in free if j>piv[i]]
    for mask in range(1<<len(pos)):
        v=[1<<j for j in piv]
        for t,(i,j) in enumerate(pos):
            if mask>>t&1: v[i] |= 1<<j
        elems=frozenset([0,v[0],v[1],v[2],v[0]^v[1],v[0]^v[2],v[1]^v[2],v[0]^v[1]^v[2]])
        assert len(elems)==8
        assert elems not in spaces
        spaces[elems]=tuple(v)
assert len(spaces)==1395

# Independent enumeration from all linearly independent unordered triples.
raw=set()
for a,b,c in combinations(range(1,64),3):
    elems=frozenset([0,a,b,c,a^b,a^c,b^c,a^b^c])
    if len(elems)==8: raw.add(elems)
assert raw == set(spaces)

# The 7th-power polarization gives the 3x3 Moore determinant.
def moore(v):
    out=0
    for p in permutations(range(3)):
        term=1
        for i in range(3):
            term=mul(term,power(v[p[i]],1<<i))
        out ^= term
    return out

sizes=Counter()
color_of={}
for U,basis in spaces.items():
    z=0
    for x in U: z ^= power(x,7)
    assert z==moore(basis), (basis,z,moore(basis))
    assert z!=0
    sizes[z]+=1
    color_of[U]=z
assert len(sizes)==63
H={power(x,7) for x in range(1,64)}
assert len(H)==9
assert H=={x for x in range(1,64) if power(x,9)==1}
assert Counter(sizes.values())=={21:54,29:9}, Counter(sizes.values())
assert {z for z,num in sizes.items() if num==29} == H
assert sum(sizes.values())==1395

# Structural orbit certificate under the free multiplicative action, except GF8.
remaining=set(spaces)
orbits=[]
while remaining:
    U=min(remaining,key=lambda s:tuple(sorted(s)))
    orbit={frozenset(mul(a,x) for x in U) for a in range(1,64)}
    assert orbit.issubset(spaces)
    assert orbit.issubset(remaining)
    remaining.difference_update(orbit)
    z=color_of[U]
    assert all(color_of[V] in {mul(h,z) for h in H} for V in orbit)
    orbits.append((len(orbit),z,U))
assert len(orbits)==23
assert Counter(m for m,z,u in orbits)=={63:22,9:1}
# Each generic 63-orbit deposits 7 spaces into each of the nine colors of a coset.
cosets=[]
left=set(range(1,64))
while left:
    r=min(left)
    cos={mul(r,h) for h in H}
    left-=cos
    cosets.append(cos)
assert len(cosets)==7
counts=[]
for cos in cosets:
    generic=sum(1 for size,z,U in orbits if size==63 and z in cos)
    exceptional=sum(1 for size,z,U in orbits if size==9 and z in cos)
    assert len({sizes[z] for z in cos})==1
    observed=sizes[min(cos)]
    assert observed == 7*generic+exceptional
    counts.append((min(cos),generic,exceptional,observed))
assert Counter((generic,exc,occ) for r,generic,exc,occ in counts)=={(4,1,29):1,(3,0,21):6}

# Adjacency proof check: equal-color 3-spaces do not share a 2-space.
# Every 2-space determines exactly [4 choose 1]_2 = 15 3-space superspaces.
line_to_colors={}
for U,z in color_of.items():
    for a,b in combinations(sorted(U - {0}),2):
        L=frozenset((0,a,b,a^b))
        assert len(L)==4
        line_to_colors.setdefault(L,set()).add(z)
assert len(line_to_colors)==651  # Gaussian binomial [6 choose 2]_2
assert all(len(colors)==15 for colors in line_to_colors.values())

print('FIELD: F2[t]/(t^6+t+1)')
print('THREE_SPACES',len(spaces))
print('MOORE_IDENTITY',len(spaces))
print('CLASS_SIZES',sorted(Counter(sizes.values()).items()))
print('NORM_ONE_CLASSES',len(H))
print('SCALAR_ORBITS',Counter(size for size,z,U in orbits))
print('ORBIT_COSSETS',sorted(counts))
print('TWO_SPACES',len(line_to_colors),'COLORS_PER_TWO_SPACE',15)
print('VERIFY_OK')
