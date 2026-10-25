#!/usr/bin/env python3
"""Independent, deterministic finite verification of the open 4x4 knight complex.
Python 3.9+ standard library only. All claims refer to ordinary (nonperiodic) knight moves.
"""
from collections import Counter, deque

V = tuple((r, c) for r in range(4) for c in range(4))
N = len(V)
ADJ = tuple(sum(1 << j for j, (u, v) in enumerate(V)
                if sorted((abs(r-u), abs(c-v))) == [1, 2])
            for r, c in V)
assert N == 16 and sum(x.bit_count() for x in ADJ)//2 == 24

# Induction on the least set bit verifies the independent-set predicate.
ok = bytearray(1 << N)
ok[0] = 1
faces = []
by_degree = [[] for _ in range(8)]
for mask in range(1, 1 << N):
    bit = mask & -mask
    i = bit.bit_length() - 1
    smaller = mask ^ bit
    if ok[smaller] and not (ADJ[i] & smaller):
        ok[mask] = 1
        faces.append(mask)
        by_degree[mask.bit_count()-1].append(mask)
assert [len(F) for F in by_degree] == [16,96,276,412,340,170,48,6]
assert len(faces) == 1364

# Sequential, explicitly specified partial matchings on unmatched simplices.
pivots = [13,9,0,8,7,4,15,2,11,3,1,10,6,5,12,14]
unmatched = set(faces)
match = {}
for v in pivots:
    bit = 1 << v
    for lower in faces:
        upper = lower | bit
        if not (lower & bit) and lower in unmatched and upper in unmatched:
            unmatched.remove(lower)
            unmatched.remove(upper)
            match[lower] = upper
assert len(match) == 679
assert len(unmatched) == 6
critical = sorted(unmatched, key=lambda k:(k.bit_count(),k))
assert Counter(k.bit_count()-1 for k in critical) == {0:1,3:5}

# Independently certify that ALL cover relations in the 1364-face poset
# become an acyclic digraph after reversing precisely the matched covers.
face_index = {mask:i for i,mask in enumerate(faces)}
indeg = [0] * len(faces)
out = [[] for _ in faces]
num_covers = 0
for upper in faces:
    if upper.bit_count() == 1:
        continue
    remaining = upper
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        lower = upper ^ bit
        if match.get(lower) == upper:
            src, dst = face_index[lower], face_index[upper]
        else:
            src, dst = face_index[upper], face_index[lower]
        out[src].append(dst)
        indeg[dst] += 1
        num_covers += 1
queue = deque(i for i,x in enumerate(indeg) if x==0)
visited = 0
while queue:
    i = queue.popleft(); visited += 1
    for j in out[i]:
        indeg[j] -= 1
        if indeg[j] == 0: queue.append(j)
assert visited == len(faces), (visited,len(faces))

# Independent cross-check using boundary ranks over F_2. This does not
# substitute for the integral/topological Morse argument.
ranks = [0]
for dim in range(1, len(by_degree)):
    lower_index = {face:i for i,face in enumerate(by_degree[dim-1])}
    basis = {}
    for face in by_degree[dim]:
        column = 0
        rest = face
        while rest:
            bit = rest & -rest
            rest ^= bit
            column ^= 1 << lower_index[face ^ bit]
        while column:
            pivot = column.bit_length()-1
            if pivot in basis:
                column ^= basis[pivot]
            else:
                basis[pivot] = column
                break
    ranks.append(len(basis))
assert ranks == [0,15,81,195,212,128,42,6]
reduced_betti = [len(F)-ranks[i]-(ranks[i+1] if i+1<len(ranks) else 0)
                 for i,F in enumerate(by_degree)]
reduced_betti[0] -= 1
assert reduced_betti == [0,0,0,5,0,0,0,0]

# The geometric dihedral group acts on oriented faces.
def rotate(x):
    r,c=x
    return (c,3-r)
def reflect(x):
    r,c=x
    return (r,3-c)
def sign(word):
    return -1 if sum(word[i]>word[j] for i in range(len(word))
                     for j in range(i+1,len(word)))%2 else 1

def lefschetz(permutation):
    acc=0
    for face in faces:
        vertices=[i for i in range(N) if (face>>i)&1]
        image=[permutation[i] for i in vertices]
        if set(vertices)==set(image):
            acc += (-1)**(len(vertices)-1) * sign(image)
    return acc
characters = {}
for k in range(4):
    for e in range(2):
        permutation=[]
        for x in V:
            y=reflect(x) if e else x
            for _ in range(k): y=rotate(y)
            permutation.append(V.index(y))
        assert sorted(permutation)==list(range(N))
        assert all((ADJ[i]>>j)&1 == (ADJ[permutation[i]]>>permutation[j])&1
                   for i in range(N) for j in range(N))
        # L(g)=tr(H_0)-tr(H_3)=1-tr(H_3), for the proven wedge.
        characters[(k,e)] = 1-lefschetz(permutation)
assert characters == {
    (0,0):5, (1,0):-1, (2,0):1, (3,0):-1,
    (0,1):3, (1,1):-1, (2,1):3, (3,1):-1
}
# The decomposition is one trivial, two one-dimensional r=-1,s=+1,
# and one standard two-dimensional rotation/reflection representation.
for (k,e),ch in characters.items():
    trivial=1
    twist=2*(-1 if k%2 else 1) # reflection eigenvalue +1
    standard= (2 if k%4==0 else -2 if k%4==2 else 0) if e==0 else 0
    assert ch == trivial+twist+standard

for n in (1,2,3):
    small = [(r,c) for r in range(n) for c in range(n)]
    assert any(all(sorted((abs(r-u),abs(c-v))) != [1,2]
                   for u,v in small if (r,c)!=(u,v)) for r,c in small)

print('F_VECTOR 16 96 276 412 340 170 48 6')
print('MATCH_PAIRS',len(match),'CRITICAL_MASKS',critical,
      'CRITICAL_DIMS',[x.bit_count()-1 for x in critical])
print('HASSE_COVERS',num_covers,'ACYCLIC_VERTICES',visited)
print('MOD2_BOUNDARY_RANKS',ranks,'REDUCED_BETTI',reduced_betti)
print('D4_CHARACTER_r^k_s^e',sorted(characters.items()))
print('D4_REPRESENTATION trivial + 2*(r=-1,s=+1) + standard_2d')
print('SQUARE_N_LE_3 contractible_by_isolated_vertex')
print('HOMOTOPY_KNIGHTS4 wedge_of_five_3_spheres')
print('VERIFY_OK_OPEN_KNIGHTS4_HOMOTOPY_D4_CHARACTER')
