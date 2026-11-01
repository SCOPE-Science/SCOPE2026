"""Reproducible finite character calculation for the seven-symbol Kneser neighborhood complex.
Run: python3 verify.py. Depends only on the Python standard library.
The topological concentration used to identify the character comes from
Nilakantan--Singh, arXiv:1802.05848, Theorem 1.3 (not established by this code).
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial

N = 7
vertices = tuple(combinations(range(N), 2))
idx = {v: i for i, v in enumerate(vertices)}
neighborhoods = [tuple(j for j, y in enumerate(vertices) if not set(x).intersection(y)) for x in vertices]
assert len(vertices) == 21 and all(len(x) == 10 for x in neighborhoods)
faces = set()
for neigh in neighborhoods:
    for bits in range(1, 1 << 10):
        faces.add(tuple(neigh[j] for j in range(10) if (bits >> j) & 1))
fvec = Counter(len(f)-1 for f in faces)
assert len(faces) == 17724
assert [fvec[d] for d in range(10)] == [21, 210, 1225, 3360, 4872, 4340, 2520, 945, 210, 21]

# Independent face count: each simplex is a simple labeled graph with no
# isolated vertices on r labels, for some 2<=r<=5.
independent = [0] * 10
for r in range(2, 6):
    for edges in range(1, comb(r, 2) + 1):
        covered = sum((-1)**j * comb(r, j) * comb(comb(r-j, 2), edges)
                      if edges <= comb(r-j, 2) else 0 for j in range(r+1))
        independent[edges - 1] += comb(N, r) * covered
assert independent == [fvec[d] for d in range(10)]
assert sum((-1)**d * fvec[d] for d in range(10)) == -28

def cycle_type(p):
    unseen = set(range(N))
    lengths = []
    while unseen:
        x = min(unseen)
        y, k = x, 0
        while y in unseen:
            unseen.remove(y)
            k += 1
            y = p[y]
        lengths.append(k)
    return tuple(sorted(lengths, reverse=True))

def parity(a):
    return -1 if sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1, len(a))) & 1 else 1

reps = {}
sizes = Counter()
for p in permutations(range(N)):
    t = cycle_type(p)
    reps.setdefault(t, p)
    sizes[t] += 1
assert len(reps) == 15 and sum(sizes.values()) == factorial(N)

rows = []
for typ, p in sorted(reps.items(), reverse=True):
    induced = [idx[tuple(sorted((p[a],p[b])))] for a,b in vertices]
    traces = [0]*10
    for face in faces:
        moved = [induced[z] for z in face]
        if set(moved) == set(face):
            traces[len(face)-1] += parity(moved)
    reduced_lefschetz = sum((-1)**d * traces[d] for d in range(10)) - 1
    char = -reduced_lefschetz
    f = typ.count(1)
    c2 = typ.count(2)
    sign = (-1)**(N - len(typ))
    model = sign * (f*f - 3*f + 1)
    # Each following character is sign-twisted, respectively,
    # S^(5,2) and exterior square of the standard S^(5,1,1).
    char_a = sign * (comb(f,2) + c2 - f)
    char_b = sign * (comb(f-1,2) - c2) if f >= 1 else sign * (1 - c2)
    # Polynomial continuation (f-1)(f-2)/2 also applies at f=0.
    char_b = sign * ((f-1)*(f-2)//2 - c2)
    assert char == model == char_a + char_b, (typ, char, model)
    rows.append((typ, sizes[typ], char, char_a, char_b))

def inner(i,j):
    numerator = sum(row[1]*row[i]*row[j] for row in rows)
    assert numerator % factorial(N) == 0
    return numerator // factorial(N)
assert inner(3,3) == inner(4,4) == 1
assert inner(3,4) == 0
assert sum(size*char for typ,size,char,a,b in rows) == 0
assert next(char for typ,size,char,a,b in rows if typ == (1,)*7) == 29
assert next(a for typ,size,char,a,b in rows if typ == (1,)*7) == 14
assert next(b for typ,size,char,a,b in rows if typ == (1,)*7) == 15
print('FACES',len(faces))
print('F_VECTOR',','.join(str(fvec[d]) for d in range(10)))
print('INDEPENDENT_F_VECTOR_CHECK_PASS')
print('CONJUGACY_CLASSES',len(rows))
for typ,size,char,a,b in rows:
    print('CLASS',','.join(map(str,typ)),size,char,a,b)
print('ORTHOGONAL_IRREDUCIBLE_CHARACTERS_14_PLUS_15_PASS')
print('FULL_GROUP_INVARIANTS_0_PASS')
print('NOTE_HOMOLOGY_CONCENTRATION_USES_NILAKANTAN_SINGH_2018_THEOREM_1_3')
print('ALL_CHECKS_PASS')
