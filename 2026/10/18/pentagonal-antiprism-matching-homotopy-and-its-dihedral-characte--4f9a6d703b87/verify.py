#!/usr/bin/env python3
"""Exact finite verification for the pentagonal-antiprism matching complex.

Requires Python 3.10+ and NumPy. No network or external data is used.
Run: python verify.py
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
import numpy as np

N = 10
EDGES = sorted({tuple(sorted((i, (i+d) % N))) for i in range(N) for d in (1,2)})
EDGE_INDEX = {e: i for i,e in enumerate(EDGES)}
CARDINALITY_FACES = {k: [t for t in combinations(range(20), k)
                  if len({v for j in t for v in EDGES[j]}) == 2*k]
                     for k in range(1,6)}
FACES = {0} | {sum(1 << j for j in t)
                for tuples in CARDINALITY_FACES.values() for t in tuples}
ORDER = (1,17,10,14,16,6,0,8,5,13,12,7,2,15,9,3,18,19,4,11)
assert len(EDGES)==20 and len(FACES)==708
assert [len(CARDINALITY_FACES[k]) for k in range(1,6)] == [20,130,310,225,22]


def boundary(mask):
    indices = [j for j in range(20) if mask & (1<<j)]
    return [(mask ^ (1<<j), (-1)**i) for i,j in enumerate(indices)]

remaining = set(FACES)
up, down = {}, {}
for j in ORDER:
    bit = 1 << j
    for small in sorted(remaining):
        large = small | bit
        if not small & bit and large in remaining:
            remaining.remove(small)
            remaining.remove(large)
            up[small] = large
            down[large] = small
crit = {d: sorted(s for s in remaining if s.bit_count()-1==d) for d in range(4)}
assert len(up)==len(down)==347
assert [len(crit[d]) for d in (0,1,2,3)] == [0,0,5,9]
assert 0 not in remaining
assert crit[2] == [16672,16897,16904,20481,32897]
assert crit[3] == [34840,67720,264324,266276,266372,270624,270864,532768,557584]

# Verify that the reversed matching edges produce no cycle in the Hasse graph.
forward = {s: [] for s in FACES}
for upper in FACES:
    for lower, _ in boundary(upper):
        if up.get(lower)==upper:
            forward[upper].append(lower)
        else:
            forward[lower].append(upper)
state = {}

def dfs(s):
    assert state.get(s,0) != 1, 'directed cycle in matching'
    if state.get(s,0)==2: return
    state[s]=1
    for t in forward[s]: dfs(t)
    state[s]=2
for face in FACES: dfs(face)

@lru_cache(None)
def project(s):
    """Algebraic-Morse projection, preserving the oriented critical basis."""
    if s in remaining: return {s: 1}
    if s in down: return {}
    upper = up[s]
    terms = boundary(upper)
    pivot = dict(terms)[s]
    out = defaultdict(int)
    for lower, coeff in terms:
        if lower==s: continue
        for c, v in project(lower).items(): out[c] -= pivot*coeff*v
    return {c:v for c,v in out.items() if v}

critical_2 = crit[2]
critical_3 = crit[3]
MORSE = np.zeros((5,9), dtype=np.int64)
for col, high in enumerate(critical_3):
    out = defaultdict(int)
    for low, coeff in boundary(high):
        for c,v in project(low).items(): out[c]+=coeff*v
    for c,v in out.items(): MORSE[critical_2.index(c),col]=v
expected = np.zeros((5,9),dtype=np.int64)
expected[0,5:8] = [1,-1,1]
expected[1,5:8] = [1,-1,1]
assert np.array_equal(MORSE,expected)
assert np.linalg.matrix_rank(MORSE)==1
# The degree is primitive because a unit coefficient occurs.
assert int(np.gcd.reduce(MORSE.ravel()))==1


def transformed(k, reflection, t):
    transformed_indices = []
    for j in t:
        a,b = EDGES[j]
        a = ((-a if reflection else a)+k) % N
        b = ((-b if reflection else b)+k) % N
        transformed_indices.append(EDGE_INDEX[tuple(sorted((a,b)))])
    inv = sum(transformed_indices[i]>transformed_indices[j]
              for i in range(len(t)) for j in range(i+1,len(t)))
    return tuple(sorted(transformed_indices)),(-1)**inv


def rank_basis_and_left_inverse(p):
    faces2 = CARDINALITY_FACES[3]  # degree 2: 310 matchings
    faces3 = CARDINALITY_FACES[4]  # degree 3: 225 matchings
    ix = {t:i for i,t in enumerate(faces2)}
    mat = np.zeros((len(faces2),len(faces3)),dtype=np.int64)
    for j,t in enumerate(faces3):
        for i in range(4):
            mat[ix[t[:i]+t[i+1:]],j] = 1 if i%2==0 else p-1
    # Exact independent columns and their pivot coordinates in GF(p).
    piv,pc,pr={},[],[]
    for j in range(mat.shape[1]):
        v=mat[:,j].copy()
        for i,u in piv.items():
            if v[i]:v=(v-v[i]*u)%p
        nonzero=np.flatnonzero(v)
        if len(nonzero):
            i=int(nonzero[0]);piv[i]=v*pow(int(v[i]),-1,p)%p
            pc.append(j);pr.append(i)
    assert len(pc)==195
    B=mat[:,pc]
    P=B[pr,:]
    aug=np.concatenate((P,np.eye(len(pc),dtype=np.int64)),axis=1)
    for j in range(len(pc)):
        pivot=next(k for k in range(j,len(pc)) if aug[k,j])
        aug[[j,pivot]]=aug[[pivot,j]]
        aug[j]=aug[j]*pow(int(aug[j,j]),-1,p)%p
        rows=np.flatnonzero(aug[:,j]);rows=rows[rows!=j]
        for row in rows:
            aug[row]=(aug[row]-aug[row,j]*aug[j])%p
    Q=aug[:,len(pc):]
    assert np.array_equal(Q@P%p,np.eye(len(pc),dtype=np.int64))
    return B,pr,Q


def characters(p):
    B,pr,Q=rank_basis_and_left_inverse(p)
    faces2=CARDINALITY_FACES[3]
    idx={t:i for i,t in enumerate(faces2)}
    chars={}
    for reflection in (False,True):
        for k in range(N):
            chain=[]
            for card in range(1,6):
                chain.append(sum(sgn for t in CARDINALITY_FACES[card]
                             for new,sgn in [transformed(k,reflection,t)] if new==t))
            preimage={}
            for i,t in enumerate(faces2):
                new,sgn=transformed(k,reflection,t)
                preimage[idx[new]]=(i,sgn)
            transformed_pivot_rows=np.vstack([
                B[preimage[row][0],:]*preimage[row][1]%p for row in pr])
            image_trace=int(np.sum(Q.T*transformed_pivot_rows)%p)
            h2=(chain[2]-chain[1]+chain[0]-1-image_trace)%p
            h3=(chain[3]-image_trace-chain[4])%p
            lift=lambda a:a if a<p//2 else a-p
            chars[(reflection,k)]=(lift(h2),lift(h3))
    return chars

# Repeating over two independent characteristics catches arithmetic mistakes;
# absolute trace bounds 4 and 8 give unique integral lifts from either prime.
char101=characters(101)
char103=characters(103)
assert char101==char103
expected_chars={}
for refl in (False,True):
    for k in range(N):
        if not refl:
            h2=4 if k%2==0 else 0
            h3=(8 if k==0 else 6 if k==5 else 3 if k%2==0 else 1)
        else:
            h2=0 if k%2==0 else -4
            h3=2 if k%2==0 else 4
        expected_chars[(refl,k)]=(h2,h3)
assert char101==expected_chars
# Lefschetz identity independently reconstructs the alternating trace on
# reduced chains for all symmetries.
for (refl,k),(h2,h3) in char101.items():
    ct=sum((-1)**(card-1)*sum(s for t in CARDINALITY_FACES[card]
                for new,s in [transformed(k,refl,t)] if new==t)
           for card in range(1,6))-1
    assert ct == h2-h3,(refl,k,ct,h2-h3)
print('PASS: 708 augmented faces, 347 acyclic pairs, exact Morse matrix,')
print('      integral sphere-wedge homotopy, D10 characters modulo 101 and 103.')
for kind in (False,True):
    print('reflections' if kind else 'rotations',
          [char101[(kind,k)] for k in range(N)])
