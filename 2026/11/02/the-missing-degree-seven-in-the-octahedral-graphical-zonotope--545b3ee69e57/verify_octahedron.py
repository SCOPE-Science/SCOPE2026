#!/usr/bin/env python3
"""Exhaustive certificate for acyclic orientation flip degrees of the octahedral graph."""
from itertools import permutations, product
from collections import Counter

V=tuple(range(6))
part=lambda u:u//2
E=tuple((u,v) for u in V for v in range(u+1,6) if part(u)!=part(v))
assert len(E)==12

# Every acyclic orientation has a topological ordering; every order is acyclic.
def orientation(order):
    pos={v:i for i,v in enumerate(order)}
    return sum((pos[u]<pos[v])<<i for i,(u,v) in enumerate(E))
O={orientation(p) for p in permutations(V)}
assert len(O)==426

def degree(a):
    return sum((a^(1<<i)) in O for i in range(12))
assert Counter(degree(a) for a in O)==Counter({5:288,6:120,8:18})
assert sum(degree(a) for a in O)==2304

# The entire automorphism group of K_{2,2,2} permutes the three independent
# vertex pairs and independently swaps the endpoints within each pair.
perms=[]
for order in permutations(range(3)):
    for bits in product(range(2),repeat=3):
        p=tuple(2*order[j//2]+(j%2 ^ bits[j//2]) for j in V)
        perms.append(p)
assert len(set(perms))==48
edge_index={e:i for i,e in enumerate(E)}

def action(a,p):
    x=0
    for i,(u,v) in enumerate(E):
        pu,pv=p[u],p[v]
        j=edge_index[tuple(sorted((pu,pv)))]
        x|=(((a>>i)&1) ^ (pu>pv))<<j
    return x

seen=set(); orbits=[]
for a in sorted(O):
    if a in seen:continue
    orbit={action(a,p) for p in perms}
    assert orbit<=O and all(degree(x)==degree(a) for x in orbit)
    assert not seen.intersection(orbit)
    seen.update(orbit)
    orbits.append((a,len(orbit),degree(a)))
assert seen==O and len(orbits)==15
assert Counter({5:sum(size for _,size,d in orbits if d==5),
                6:sum(size for _,size,d in orbits if d==6),
                8:sum(size for _,size,d in orbits if d==8)})==Counter({5:288,6:120,8:18})
print('OCTAHEDRON_ACYCLIC_ORBITS_PASS')
print('vertex_orbits',orbits)
print('reversible_degree_polynomial','288*t^5+120*t^6+18*t^8')
