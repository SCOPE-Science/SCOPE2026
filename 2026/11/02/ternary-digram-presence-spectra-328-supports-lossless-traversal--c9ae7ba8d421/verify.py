"""Independent exhaustive checks for ternary 2-factor presence-support theorem.
Only standard Python 3 is needed. No external datasets are required.
"""
from itertools import product
from collections import defaultdict, Counter

Q=3
B=1<<(Q*Q)

def profile(word):
    mask=0
    for a,b in zip(word,word[1:]):
        mask |= 1<<(Q*a+b)
    return mask

# Enumerate all possible label-specific directed supports with DFS over states
# (support, final letter); every finite word is represented by a path here.
seen={(0,a) for a in range(Q)}
front=set(seen)
for _ in range(B*Q):
    nxt={(mask|(1<<(Q*a+b)),b) for mask,a in front for b in range(Q)}-seen
    if not nxt:
        break
    seen |= nxt
    front=nxt
else:
    raise AssertionError('Finite-state closure not reached')
feasible={mask for mask,a in seen}
assert len(feasible)==328
hist=Counter(mask.bit_count() for mask in feasible)
assert [hist.get(k,0) for k in range(10)]==[1,9,21,44,72,81,60,30,9,1]

# Independently enumerate every word of each length up to 10 and compare the
# full support set at maximal natural length, without using DFS state closure.
fixed={}
for n in range(1,11):
    profiles={profile(w) for w in product(range(Q),repeat=n)}
    fixed[n]=profiles
assert [len(fixed[n]) for n in range(1,11)]==[1,9,24,62,134,215,275,305,314,315]

# Independently compute shortest realization by breadth-first word enumeration.
first={}
for n in range(1,11):
    for m in fixed[n]:
        first.setdefault(m,n)
assert set(first)==feasible
assert all(first[m]==m.bit_count()+1 for m in feasible)

# A directed support contains a directed cycle if it contains a loop, a
# reciprocal pair, or a directed 3-cycle (the only alternatives for q=3).
def cyclic(m):
    if any(m&(1<<(Q*a+a)) for a in range(Q)):
        return True
    if any((m&(1<<(Q*a+b))) and (m&(1<<(Q*b+a)))
           for a in range(Q) for b in range(a+1,Q)):
        return True
    return any(all(m&(1<<(Q*x+y)) for x,y in [(a,b),(b,c),(c,a)])
               for a,b,c in product(range(Q),repeat=3)
               if len({a,b,c})==3)
acyclic={m for m in feasible if not cyclic(m)}
assert len(acyclic)==13
assert Counter(m.bit_count() for m in acyclic)=={0:1,1:6,2:6}
assert all(m not in fixed[10] for m in acyclic)
assert feasible-fixed[10]==acyclic

# Four-letter counterexample: must repeat a transition since balance is +/-2.
w=tuple(map(int,'02103101'))
support4={(a,b) for a,b in zip(w,w[1:])}
assert support4=={(0,2),(2,1),(1,0),(0,3),(3,1),(0,1)}
assert len(support4)==6 and len(w)==8
out=Counter(a for a,b in support4); inc=Counter(b for a,b in support4)
assert sorted(out[v]-inc[v] for v in range(4))==[-2,0,0,2]
print('PASS: 328 feasible ternary supports out of 512')
print('PASS: edge-count distribution', [hist.get(k,0) for k in range(10)])
print('PASS: every feasible support has shortest word length edges+1')
print('PASS: 13 acyclic supports = empty, six arcs, six directed paths')
print('PASS: at length 10 exactly 315 cyclic supports and none acyclic')
print('PASS: four-letter 6-arc support requires at least 7 edges; 8-letter word realizes it')
