#!/usr/bin/env python3
"""Exact 4-dimensional binary evolution-algebra symmetry census.

Pure Python, Python 3.9+, no dependencies.  Matrices encoded in row-major order:
bit (4*i+j) is the coefficient of e_j in e_i^2.  All loops are finite.
"""
from collections import Counter
from itertools import permutations
from math import factorial
import json

N = 4
PERMS = tuple(permutations(range(N)))
ALL = tuple(range(1 << (N*N)))

def matrix_rank(m):
    rows = [(m >> (N*i)) & ((1<<N)-1) for i in range(N)]
    rank = 0
    for col in range(N):
        k = next((k for k in range(rank, N) if (rows[k]>>col)&1), None)
        if k is None:
            continue
        rows[rank], rows[k] = rows[k], rows[rank]
        for i in range(rank+1,N):
            if (rows[i]>>col)&1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank

def det_parity(m):
    # Independent of the row-reduction test: determinant expansion mod 2.
    v=0
    for p in PERMS:
        term=1
        for i in range(N):
            term &= (m >> (N*i+p[i])) & 1
        v ^= term
    return v

def strongly_connected(m):
    # Outgoing-neighbour reachability from every vertex.
    for source in range(N):
        reached = 1 << source
        while True:
            union = reached
            for i in range(N):
                if reached & (1 << i):
                    union |= (m >> (N*i)) & 15
            if reached == union:
                break
            reached = union
        if reached != 15:
            return False
    return True

def no_sink_set(m):
    # Independent connectivity criterion: every nonempty proper set
    # has at least one edge leaving it.
    for u in range(1, (1<<N)-1):
        out=0
        for i in range(N):
            if u & (1<<i):
                out |= (m >> (N*i)) & 15
        if out & ~u == 0:
            return False
    return True

def relabel(m,p):
    result=0
    for i in range(N):
        for j in range(N):
            if m & (1<<(4*i+j)):
                result |= 1 << (4*p[i]+p[j])
    return result

def perm_cycle_type(p):
    used=set(); lengths=[]
    for i in range(N):
        if i in used: continue
        j=i; k=0
        while j not in used:
            used.add(j); k+=1; j=p[j]
        lengths.append(k)
    return tuple(sorted(lengths))

def perm_order(p):
    current=tuple(range(N))
    for k in range(1,25):
        current=tuple(p[i] for i in current)
        if current==tuple(range(N)):
            return k
    raise AssertionError('invalid permutation')

def group_label(ix):
    k=len(ix)
    if k==1: return 'trivial'
    if k==2: return 'C2'
    if k==3: return 'C3'
    if k==4:
        return 'C4' if any(perm_order(PERMS[i])==4 for i in ix) else 'V4'
    if k==6: return 'S3'
    if k==8: return 'D8'
    if k==12: return 'A4'
    if k==24: return 'S4'
    raise AssertionError(f'unexpected subgroup size {k}')

EXPECTED_LABELLED={
    'trivial':11064,'C2':540,'C3':24,'C4':12,
    'V4':6,'S3':8,'D8':3,'S4':1
}
EXPECTED_CLASSES={
    'trivial':461,'C2':45,'C3':3,'C4':2,
    'V4':1,'S3':2,'D8':1,'S4':1
}
EXPECTED_FIXED={
    (1,1,1,1):11658,(1,1,2):72,(2,2):62,(1,3):9,(4,):6
}

# Method I: all matrices, Gaussian elimination, reachability, stabilizers
# and canonical-orbit representatives.
labelled=Counter(); orbit_classes=Counter(); examples={}
fixed_by_type=Counter(); all_invertible=0; all_invertible_orbits=0
simple_masks=[]
for mask in ALL:
    if matrix_rank(mask)<4:
        continue
    all_invertible+=1
    orbit_values=[relabel(mask,p) for p in PERMS]
    if mask==min(orbit_values):
        all_invertible_orbits+=1
    if not strongly_connected(mask):
        continue
    simple_masks.append(mask)
    stabilizer=tuple(i for i,im in enumerate(orbit_values) if im==mask)
    label=group_label(stabilizer)
    labelled[label]+=1
    if mask==min(orbit_values):
        orbit_classes[label]+=1
        examples.setdefault(label,mask)
    for i in stabilizer:
        fixed_by_type[perm_cycle_type(PERMS[i])]+=1

assert all_invertible==20160
assert all_invertible_orbits==908  # Wei--Zou 2023 all-perfect count.
assert sum(labelled.values())==11658
assert sum(orbit_classes.values())==516
assert dict(labelled)==EXPECTED_LABELLED
assert dict(orbit_classes)==EXPECTED_CLASSES
for cycle, nperm in [((1,1,1,1),1),((1,1,2),6),((2,2),3),((1,3),8),((4,),6)]:
    assert fixed_by_type[cycle]==nperm*EXPECTED_FIXED[cycle]

# Method II: enumerate matrices fixed under each conjugacy representative
# by choosing bits on the orbits of the induced action on 16 cells.
# Determine nonsingularity by determinant parity, and simplicity by the
# proper-sink-subset test, both independent of Method I.
def fixed_matrices(p):
    cell_orbits=[]; visited=set()
    for c in range(N*N):
        if c in visited:
            continue
        current=c; orbit=[]
        while current not in visited:
            visited.add(current);orbit.append(current)
            i,j=divmod(current,N)
            current=N*p[i]+p[j]
        cell_orbits.append(orbit)
    for bits in range(1 << len(cell_orbits)):
        m=0
        for k,orb in enumerate(cell_orbits):
            if bits & (1<<k):
                for c in orb: m|=1<<c
        yield m

fix_independent={}
for cyc in EXPECTED_FIXED:
    representative=next(p for p in PERMS if perm_cycle_type(p)==cyc)
    observed=sum(bool(det_parity(m)) and no_sink_set(m)
                 for m in fixed_matrices(representative))
    assert observed==EXPECTED_FIXED[cyc], (cyc,observed)
    fix_independent[','.join(map(str,cyc))]=observed

# Extra tests: the two independent predicates agree on the whole universe.
assert all((matrix_rank(m)==4)==bool(det_parity(m)) for m in ALL)
assert all(strongly_connected(m)==no_sink_set(m) for m in ALL)
assert (11658 + 6*72 + 3*62 + 8*9 + 6*6)//24 ==516

result={
 'status':'VERIFY_OK',
 'number_of_binary_4x4_matrices':65536,
 'number_of_invertible_matrices':all_invertible,
 'all_perfect_isomorphism_classes_known':all_invertible_orbits,
 'simple_labeled':len(simple_masks),
 'simple_isomorphism_classes':sum(orbit_classes.values()),
 'automorphism_group_labelled_counts':dict(sorted(labelled.items())),
 'automorphism_group_isomorphism_class_counts':dict(sorted(orbit_classes.items())),
 'symmetry_class_representatives_decimal':dict(sorted(examples.items())),
 'independent_fixed_matrices_per_representative':fix_independent,
 'proof_cross_checks':['rank/determinant parity all 65536',
   'reachability/no-sink-subset all 65536',
   'two distinct Burnside calculations',
   '908 all-perfect class count matches Wei-Zou (2023)']
}
print(json.dumps(result, indent=2, sort_keys=True))
