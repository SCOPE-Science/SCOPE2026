"""Finite exact classification of minimum total dominating sets of J(6,3).
Standard-library Python 3; no external data or packages.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb

U=tuple(range(1,7))
V=tuple(combinations(U,3))
index={t:i for i,t in enumerate(V)}
assert len(V)==20
N=[sum(1<<j for j,b in enumerate(V) if i!=j and len(set(a)&set(b))==2)
   for i,a in enumerate(V)]

def dominates(indices):
    mask=sum(1<<i for i in indices)
    return all(mask&nb for nb in N)

# Exhaustive search, independent of the orbit representatives.
for k in (0,1,2,3):
    assert not any(dominates(t) for t in combinations(range(20),k))
print('lower_bound: all sets of size at most three excluded; size_three=',comb(20,3))
winners={frozenset(t) for t in combinations(range(20),4) if dominates(t)}
assert len(winners)==765
print('four_subsets=',comb(20,4),'total_dominating=',len(winners))

representatives=(
  ((1,2,3),(2,3,5),(2,4,5),(4,5,6)),
  ((1,2,4),(1,2,5),(2,3,6),(3,4,6)),
  ((1,4,6),(1,5,6),(2,3,4),(2,3,5)),
)
perms=tuple(permutations(U))
assert len(perms)==720
orbits=[]
for rep in representatives:
    assert all(t in index for t in rep)
    orbit=set()
    for p in perms:
        mapping={x:p[x-1] for x in U}
        transformed=frozenset(index[tuple(sorted(mapping[a] for a in tri))] for tri in rep)
        orbit.add(transformed)
    orbits.append(orbit)
assert tuple(map(len,orbits))==(360,360,45)
assert all(orbits[i].isdisjoint(orbits[j]) for i in range(3) for j in range(i+1,3))
assert set.union(*orbits)==winners
print('orbit_sizes=',tuple(map(len,orbits)),'stabilizers=',tuple(720//len(o) for o in orbits))
print('complete_coverage=',len(set.union(*orbits)),'underlying_group_size=',len(perms))
for j,rep in enumerate(representatives):
    overlaps=sorted(len(set(a)&set(b)) for a,b in combinations(rep,2))
    degrees=sorted(sum(x in tri for tri in rep) for x in U)
    print('orbit',j+1,'pair_intersections=',overlaps,'point_degrees=',degrees)
print('PASS: exactly three S6-orbits of minimum total dominating sets of J(6,3)')
