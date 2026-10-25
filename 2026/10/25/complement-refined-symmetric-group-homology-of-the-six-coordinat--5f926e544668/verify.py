#!/usr/bin/env python3
"""Exact finite verification of Rips homology characters on rank 2/4 subsets of six coordinates.
Uses only the Python standard library.  All tests reconstruct the complex from its metric."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial

N = 6
universe = frozenset(range(N))
vertices = [frozenset(x) for k in (2, 4) for x in combinations(range(N), k)]
vid = {v: i for i, v in enumerate(vertices)}
assert len(vertices) == 30
neighbors = [0] * 30
for i in range(30):
    for j in range(i + 1, 30):
        if len(vertices[i] ^ vertices[j]) <= 2:
            neighbors[i] |= 1 << j
            neighbors[j] |= 1 << i
faces = defaultdict(list)
def enumerate_faces(prefix, candidates):
    if prefix:
        faces[len(prefix)-1].append(tuple(prefix))
    while candidates:
        mask = candidates & -candidates
        j = mask.bit_length() - 1
        candidates ^= mask
        enumerate_faces(prefix + [j], candidates & neighbors[j])
enumerate_faces([], (1 << 30) - 1)
fvector = tuple(len(faces[i]) for i in range(6))
assert fvector == (30, 210, 520, 480, 132, 20), fvector
assert sum((-1)**i * fvector[i] for i in range(6)) == -28
print('EXHAUSTIVE_SCALE_TWO_F_VECTOR', fvector)

# Independent mod-2 rank check: sparse columns encoded as Python bitsets.
def rank2(cols):
    basis = {}
    for v in cols:
        while v:
            pivot = v.bit_length() - 1
            if pivot in basis:
                v ^= basis[pivot]
            else:
                basis[pivot] = v
                break
    return len(basis)
ranks = []
for d in range(1, 6):
    index = {x: i for i, x in enumerate(faces[d-1])}
    cols = []
    for simplex in faces[d]:
        w = 0
        for j in range(len(simplex)):
            w ^= 1 << index[simplex[:j] + simplex[j+1:]]
        cols.append(w)
    ranks.append(rank2(cols))
assert ranks == [29, 181, 339, 112, 20], ranks
betti = [fvector[0]-ranks[0]] + [fvector[i] - ranks[i-1] - ranks[i] for i in range(1,5)] + [fvector[5]-ranks[4]]
assert betti == [1,0,0,29,0,0], betti
print('MOD_TWO_BOUNDARY_RANKS', ranks, 'BETTI',betti)

cycle_reps = {}
for p in permutations(range(N)):
    seen = set()
    cycles = []
    for i in range(N):
        if i in seen:
            continue
        k, j = 0, i
        while j not in seen:
            seen.add(j)
            j = p[j]
            k += 1
        cycles.append(k)
    typ = tuple(sorted(cycles, reverse=True))
    cycle_reps.setdefault(typ, p)
assert len(cycle_reps) == 11

def signed_trace_on_chains(p, complement):
    vmap = []
    for v in vertices:
        image = frozenset(p[i] for i in v)
        if complement:
            image = universe - image
        vmap.append(vid[image])
    result = 0
    for d, simplices in faces.items():
        for sigma in simplices:
            transformed = [vmap[v] for v in sigma]
            if set(transformed) != set(sigma):
                continue
            sorted_s = sorted(sigma)
            pi = [sorted_s.index(v) for v in transformed]
            inv = sum(pi[i] > pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))
            result += (-1)**(d+inv)
    return 1-result    # H_3 trace, as all other reduced rational homology vanishes

traces = {e: {c: signed_trace_on_chains(p,e) for c,p in cycle_reps.items()} for e in (0,1)}
expected0 = {(1,1,1,1,1,1):29,(2,1,1,1,1):-11,(2,2,1,1):1,(2,2,2):1,(3,1,1,1):5,(3,2,1):1,(3,3):-1,(4,1,1):-1,(4,2):-1,(5,1):-1,(6,):1}
expected1 = {(1,1,1,1,1,1):1,(2,1,1,1,1):1,(2,2,1,1):-3,(2,2,2):5,(3,1,1,1):1,(3,2,1):1,(3,3):1,(4,1,1):-1,(4,2):-1,(5,1):1,(6,):-1}
assert traces[0] == expected0 and traces[1] == expected1
# Every group element, not just representatives.
all_cases = 0
for p in permutations(range(N)):
    seen = set(); lengths=[]
    for i in range(N):
        if i not in seen:
            x = i; s=0
            while x not in seen:
                seen.add(x);x=p[x];s+=1
            lengths.append(s)
    typ=tuple(sorted(lengths,reverse=True))
    for comp in (0,1):
        assert signed_trace_on_chains(p,comp) == traces[comp][typ]
        all_cases += 1
assert all_cases == 1440
print('ALL_JOINT_GROUP_TRACES', all_cases)

# Self-contained Murnaghan--Nakayama: rim strips and character table.
def partitions(n, maximum=None):
    if not n:
        yield ()
    else:
        for k in range(min(n, maximum if maximum is not None else n),0,-1):
            for rest in partitions(n-k,k):
                yield (k,)+rest

def diagram(shape):
    return frozenset((r,c) for r,length in enumerate(shape) for c in range(length))

@lru_cache(None)
def rim_removals(lam,k):
    source=diagram(lam);out=[]
    for nu in partitions(sum(lam)-k):
        rem=source-diagram(nu)
        if len(rem)!=k or not diagram(nu)<=source:continue
        visited=set();todo={next(iter(rem))}
        while todo:
            x=todo.pop()
            if x in visited: continue
            visited.add(x)
            r,c=x
            todo.update(y for y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)) if y in rem and y not in visited)
        if visited!=rem:continue
        if any((r+1,c) in rem and (r,c+1) in rem and (r+1,c+1) in rem for r,c in rem):continue
        out.append((nu,(-1)**(len({r for r,c in rem})-1)))
    return out

@lru_cache(None)
def character(lam,cycle):
    if not cycle:return int(not lam)
    return sum(sign*character(smaller,cycle[1:]) for smaller,sign in rim_removals(lam,cycle[0]))

def centralizer(cycle):
    out=1
    for k,v in Counter(cycle).items():out *= k**v * factorial(v)
    return out

results={}
for lam in partitions(N):
    a=sum((factorial(N)//centralizer(c)) * character(lam,c)*traces[0][c] for c in traces[0])
    b=sum((factorial(N)//centralizer(c)) * character(lam,c)*traces[1][c] for c in traces[1])
    assert a%factorial(N)==0 and b%factorial(N)==0
    a//=factorial(N);b//=factorial(N)
    assert (a+b)%2==0 and (a-b)%2==0
    results[lam]=((a+b)//2,(a-b)//2)
expected = {(3,1,1,1):(1,0),(2,2,1,1):(0,1),(2,1,1,1,1):(1,1)}
assert {lam:v for lam,v in results.items() if v!=(0,0)}==expected
assert sum(chi for lam,(plus,minus) in results.items() for chi in (plus,minus))==4
print('S6_TIMES_C2_DECOMPOSITION',expected)

# At scale four, the only missing edges are the 15 complement pairs.
pairs=set()
for i in range(30):
    for j in range(i+1,30):
        if len(vertices[i]^vertices[j])>4:
            assert vertices[j]==universe-vertices[i]
            pairs.add((i,j))
assert len(pairs)==15
# A coordinate transposition exchanges precisely 4 of the 15 antipodal axes.
transposition=(1,0,2,3,4,5)
axes=[v for v in vertices if len(v)==2]
perm=[axes.index(frozenset(transposition[i] for i in v)) for v in axes]
assert sum(perm[i]>perm[j] for i in range(15) for j in range(i+1,15))%2==0
print('SCALE_FOUR_CROSS_POLYTOPE',15,'ANTIPODAL_PAIRS')
print('REPRODUCIBLE_RIPS_S6_C2_CHARACTER_PASS')
