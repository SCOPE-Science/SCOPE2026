#!/usr/bin/env python3
"""Integral discrete Morse certificate for the binary rank-four cap complex."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

PIVOT_ORDER=(11,13,10,12,6,0,1,8,14,9,5,7,3,2,4)
N=15

def vertices(mask):
    return [v for v in range(1,N+1) if mask & (1<<(v-1))]

def is_cap(mask):
    vs=vertices(mask)
    return all(not (mask & (1<<((a^b)-1))) for a,b in combinations(vs,2))

faces={s:s.bit_count()-1 for s in range(1,1<<N) if is_cap(s)}
assert len(faces)==3048
fv=tuple(Counter(faces.values())[i] for i in range(8))
assert fv==(15,105,420,945,1008,420,120,15)

# At each pivot, pair *all* still-unmatched faces with their pivot extensions.
remaining=set(faces)
matching=[]
for pivot in PIVOT_ORDER:
    bit=1<<pivot
    for lower in sorted(remaining):
        upper=lower|bit
        if lower in remaining and lower&bit==0 and upper in remaining:
            assert faces[upper]==faces[lower]+1
            remaining.remove(lower)
            remaining.remove(upper)
            matching.append((lower,upper))
assert len(matching)==1484
assert len(remaining)==80
assert Counter(faces[s] for s in remaining)=={0:1,3:1,4:78}

# Every edge of the Hasse diagram is directed downward, EXCEPT a matching
# pair, directed upwards.  A topological sort certifies no directed cycles.
matched=set(matching)
nexts=defaultdict(list)
indegree={s:0 for s in faces}
for upper in faces:
    for vertex in vertices(upper):
        lower=upper^(1<<(vertex-1))
        if lower not in faces:
            assert lower==0
            continue
        u,v=(lower,upper) if (lower,upper) in matched else (upper,lower)
        nexts[u].append(v);indegree[v]+=1
queue=deque(x for x in faces if indegree[x]==0)
visited=0
while queue:
    x=queue.popleft(); visited+=1
    for y in nexts[x]:
        indegree[y]-=1
        if indegree[y]==0:queue.append(y)
assert visited==len(faces),f'directed cycle: visited {visited}'

# Compute the integer Morse differential via the acyclic gradient-path
# recursion.  Of dimension three there is exactly one critical cell.
critical3=next(s for s in remaining if faces[s]==3)
critical4=sorted(s for s in remaining if faces[s]==4)
lower_to_upper={a:b for a,b in matching if faces[a]==3}
upper3={b for a,b in matching if faces[b]==3}

# Facet signs use increasing order of vertex labels.
def facets(upper):
    for i,v in enumerate(vertices(upper)):
        yield upper^(1<<(v-1)),(-1 if i%2 else 1)

active=set()
@lru_cache(None)
def projection(face):
    if face==critical3:return 1
    if face in upper3:return 0
    assert face in lower_to_upper,(face, faces[face])
    if face in active:raise AssertionError('gradient cycle')
    active.add(face)
    upper=lower_to_upper[face]
    fac=dict(facets(upper)); unit=fac[face]
    assert abs(unit)==1
    val=-sum(sign*projection(other) for other,sign in fac.items() if other!=face)//unit
    active.remove(face)
    return val

coefficients=[]
for upper in critical4:
    coefficient=sum(sign*projection(lower) for lower,sign in facets(upper))
    coefficients.append(coefficient)
print('face vector:',fv)
print('Morse matching pairs:',len(matching))
print('acyclic Hasse nodes:',visited)
print('critical dimensions:',dict(sorted(Counter(faces[s] for s in remaining).items())))
print('critical dimension-3 simplex:',vertices(critical3))
print('Morse boundary distribution:',dict(sorted(Counter(coefficients).items())))
from math import gcd
from functools import reduce
boundary_gcd=reduce(gcd,(abs(x) for x in coefficients),0)
print('Morse boundary gcd:',boundary_gcd)
print('reduced integral H3: Z/%s' % boundary_gcd)
print('reduced integral H4: Z^%s' % (len(critical4)-1))
assert boundary_gcd==2
print('ALL_CHECKS_PASS')
