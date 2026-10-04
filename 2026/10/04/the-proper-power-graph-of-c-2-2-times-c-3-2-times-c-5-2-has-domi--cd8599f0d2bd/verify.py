#!/usr/bin/env python3
from itertools import product
from time import perf_counter

SIZES=(3,4,6)


def all_partial(sizes):
    r=len(sizes)
    out=[]
    for mask in range(1,1<<r):
        inds=[i for i in range(r) if (mask>>i)&1]
        for vals in product(*[range(sizes[i]) for i in inds]):
            t=[-1]*r
            for i,v in zip(inds,vals):
                t[i]=v
            out.append(tuple(t))
    return out


def comparable(a,b):
    sa=[i for i,x in enumerate(a) if x!=-1]
    sb=[i for i,x in enumerate(b) if x!=-1]
    A=set(sa); B=set(sb)
    if A<=B:
        return all(a[i]==b[i] for i in sa)
    if B<=A:
        return all(a[i]==b[i] for i in sb)
    return False

V=all_partial(SIZES)
assert len(V)==(1+3)*(1+4)*(1+6)-1==139
N=len(V)
COV=[]
DOMS=[[] for _ in range(N)]
for j,s in enumerate(V):
    m=0
    for i,t in enumerate(V):
        if comparable(t,s):
            m |= 1<<i
            DOMS[i].append(j)
    COV.append(m)
ALL=(1<<N)-1

# Canonical 11-set: every atom except one distinguished value per coordinate,
# plus the full distinguished tuple.
witness=[]
for i,n in enumerate(SIZES):
    for a in range(n-1):
        t=[-1]*3; t[i]=a
        witness.append(V.index(tuple(t)))
witness.append(V.index((2,3,5)))
assert len(witness)==11
covered=0
for j in witness:
    covered |= COV[j]
assert covered==ALL

# Exact branch-and-bound decision for a dominating family of size <=10.
# Every branch selects a dominator of one uncovered target. Memoization and
# a rigorous maximum-new-coverage lower bound prune only impossible states.
seen=set(); nodes=0
start=perf_counter()

def dfs(uncovered,k):
    global nodes
    nodes += 1
    if uncovered==0:
        return True
    if k==0:
        return False
    maxcov=0
    for c in COV:
        z=(c & uncovered).bit_count()
        if z>maxcov: maxcov=z
    if (uncovered.bit_count()+maxcov-1)//maxcov > k:
        return False
    key=(uncovered,k)
    if key in seen:
        return False
    # Exact branching: choose an uncovered target with the fewest available
    # dominators, then try every such dominator.
    u=uncovered
    best=None
    while u:
        bit=u & -u
        i=bit.bit_length()-1
        u-=bit
        cand=[j for j in DOMS[i] if COV[j] & uncovered]
        if best is None or len(cand)<len(best):
            best=cand
            if len(best)==1:
                break
    best.sort(key=lambda j:(COV[j]&uncovered).bit_count(), reverse=True)
    for j in best:
        if dfs(uncovered & ~COV[j], k-1):
            return True
    seen.add(key)
    return False

assert dfs(ALL,10) is False
elapsed=perf_counter()-start

# The 899 actual nonidentity elements collapse exactly to these 139 generated
# cyclic subgroups because G=C2^2 x C3^2 x C5^2 has squarefree exponent 30.
# Number of order-p lines: 3,4,6; each nontrivial cyclic subgroup chooses a
# nonempty subset of the three primes and one line for every chosen prime.
assert 4*5*7-1==139
assert 4*9*25-1==899

print('VERIFY_OK')
print('group_order=900')
print('proper_power_vertices=899')
print('cyclic_subgroup_types=139')
print('dominating_witness_size=11')
print('no_dominating_family_size_10=true')
print(f'branch_nodes={nodes}')
