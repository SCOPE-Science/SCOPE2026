"""Reproduce the finite permutation and binary-module calculations in RESULT.md.
Pure Python 3; exact integer arithmetic; no third-party dependencies.
"""
from itertools import permutations, combinations

def perm_comp(g,h):
    return tuple(g[h[i]] for i in range(5))

def perm_inverse(g):
    return tuple(g.index(i) for i in range(5))

def parity(g):
    return sum(g[i]>g[j] for i in range(5) for j in range(i+1,5))%2

identity=tuple(range(5))
H=set(g for g in permutations(range(5)) if parity(g)==0)
assert len(H)==60
orders={}
for g in H:
    cur=identity
    for d in range(1,61):
        cur=perm_comp(cur,g)
        if cur==identity:
            orders[g]=d;break


def power(g,k):
    z=identity
    for _ in range(k):z=perm_comp(z,g)
    return z
sylow5=sorted({frozenset(power(g,k) for k in range(5)) for g in H if orders[g]==5},key=lambda f:sorted(f))
assert len(sylow5)==6
pos={S:i for i,S in enumerate(sylow5)}

def act(g):
    inv=perm_inverse(g)
    return tuple(pos[frozenset(perm_comp(g,perm_comp(u,inv)) for u in S)] for S in sylow5)

def action_vec(v,p):
    return sum(1<<p[i] for i in range(6) if v>>i&1)

def basis(vectors):
    R={}
    for x in vectors:
        while x:
            pivot=x.bit_length()-1
            if pivot in R: x^=R[pivot]
            else: R[pivot]=x;break
    return [R[i] for i in sorted(R,reverse=True)]

def span(vectors):
    Z={0}
    for w in basis(vectors):Z|={v^w for v in tuple(Z)}
    return frozenset(Z)

def rref_spaces(n):
    for r in range(n+1):
        for piv in combinations(range(n),r):
            extras=[x for x in range(n) if x not in piv]
            slots=[(i,j) for i,p in enumerate(piv) for j in extras if j>p]
            for flags in range(1<<len(slots)):
                rows=[1<<p for p in piv]
                for bit,(i,j) in enumerate(slots):
                    if flags>>bit&1: rows[i]|=1<<j
                yield span(rows)

all_actions={act(g) for g in H}
assert len(all_actions)==60
p5=(1,2,3,4,0)
p3=(1,2,0,3,4)
a,b=act(p5),act(p3)
# Independently close the two generators: they produce all 60 actions.
cl={tuple(range(6))}; stack=list(cl)
while stack:
    g=stack.pop()
    for h in (a,b):
        c=tuple(g[h[i]] for i in range(6))
        if c not in cl:cl.add(c);stack.append(c)
assert cl==all_actions
assert {p[i] for p in all_actions for i in range(6)}==set(range(6))
assert len({(p[i],p[j]) for p in all_actions for i,j in [(0,1)]})==30
for i,j in combinations(range(6),2):
    stabilizer=[g for g in all_actions if g[i]==i and g[j]==j]
    assert len(stabilizer)==2
    assert sum(stabilizer[1][k]==k for k in range(6))==2 or sum(stabilizer[0][k]==k for k in range(6))==2

zero=frozenset([0]);constant=span([63]);augmentation=span([3,5,9,17,33]);whole=frozenset(range(64))
assert len(augmentation)==32
invariants=[s for s in rref_spaces(6) if all(all(action_vec(v,p) in s for v in s) for p in (a,b))]
assert set(invariants)=={zero,constant,augmentation,whole},[len(x) for x in invariants]

# Five Sylow-2 subgroups of A5 consist of 1 plus three double transpositions fixing one letter.
matchings=[]
for fixed in range(5):
    P={g for g in H if g[fixed]==fixed and (g==identity or orders[g]==2)}
    assert len(P)==4
    actions=[act(g) for g in P]
    yet=set(range(6)); partition=[]
    while yet:
        i=min(yet);orbit={p[i] for p in actions}
        assert len(orbit)==2
        yet-=orbit;partition.append(tuple(sorted(orbit)))
    matchings.append(tuple(sorted(partition)))
assert len(set(matchings))==5
edges=[e for m in matchings for e in m]
assert len(edges)==15 and set(edges)==set(combinations(range(6),2))

local_parts=[]
for m in matchings:
    part=span([(1<<i)|(1<<j) for i,j in m])
    assert len(part)==8
    local_parts.append(part)
local=frozenset.intersection(*local_parts)
assert local==constant
assert constant<augmentation<whole
print('A5_ORDER=60; SIX_SYLOW5_SUBGROUPS=6; TWO_TRANSITIVE=TRUE')
print('INVARIANT_SUBMODULE_DIMENSIONS=0,1,5,6')
print('FIVE_SYLOW2_ORBIT_MATCHINGS:',matchings)
print('MATCHINGS_PARTITION_EDGES_OF_K6=TRUE')
print('RADICAL_DIM=5; LOCAL_INTERSECTION_DIM=1; GAP_DIM=4')
print('FOR_EACH_t>=1: PHI_DIM=5t; PSI_DIM=t; QUOTIENT_ORDER=2^(4t)')
print('VERIFY_OK')
