from collections import defaultdict
from itertools import combinations
import math, random

random.seed(2705)

def collision_type(A):
    reps=defaultdict(list)
    for i,a in enumerate(A):
        for j in range(i,len(A)):
            reps[a+A[j]].append((i,j))
    bad=[v for v in reps.values() if len(v)>1]
    if len(bad)!=1 or len(bad[0])!=2:
        return None
    (i,j),(k,l)=bad[0]
    if len({i,j,k,l})==4:
        return 'parallelogram'
    if (i==j) ^ (k==l):
        return 'three_term_progression'
    return None

def moment4(A,c):
    sums=defaultdict(complex)
    for i,a in enumerate(A):
        for j,b in enumerate(A):
            sums[a+b] += c[i]*c[j]
    return sum(abs(z)**2 for z in sums.values())

def ratio(A,c):
    s=sum(abs(z)**2 for z in c)
    return moment4(A,c)/(s*s)

# Exact witnesses.
A=[0,1,4,5]
assert collision_type(A)=='parallelogram'
assert abs(ratio(A,[1,1,1,1])-9/4) < 1e-14
A=[0,1,2,10]
assert collision_type(A)=='three_term_progression'
assert abs(ratio(A,[math.sqrt(2),math.sqrt(3),math.sqrt(2),0])-15/7) < 1e-14

# Exhaustive support census in a bounded integer window, followed by
# deterministic random coefficient stress tests for every detected support.
counts={'parallelogram':0,'three_term_progression':0}
worst={'parallelogram':0.0,'three_term_progression':0.0}
checked=0
for m in range(3,7):
    for A in combinations(range(12),m):
        typ=collision_type(A)
        if typ is None:
            continue
        counts[typ]+=1
        target=9/4 if typ=='parallelogram' else 15/7
        for _ in range(4):
            c=[complex(random.uniform(-1,1),random.uniform(-1,1)) for _ in A]
            q=ratio(A,c)
            worst[typ]=max(worst[typ],q)
            assert q <= target + 2e-12, (A,typ,q,target)
            checked += 1

print('supports',counts)
print('random_checks',checked)
print('worst',worst)
print('VERIFY_OK')
