from itertools import product
from collections import Counter

Q = range(3)
WORDS = list(product(Q, repeat=4))
INDEX = {w:i for i,w in enumerate(WORDS)}
N = len(WORDS)

def pair_distance(x,y):
    return sum((x[i], x[(i+1)%4]) != (y[i], y[(i+1)%4]) for i in range(4))

ADJ = [set() for _ in range(N)]
for i,x in enumerate(WORDS):
    for j in range(i+1,N):
        if pair_distance(x, WORDS[j]) >= 4:
            ADJ[i].add(j)
            ADJ[j].add(i)

hist = Counter()
maxima = []
nodes = 0

def bronk(R,P,X):
    global nodes
    nodes += 1
    if not P and not X:
        hist[len(R)] += 1
        if len(R) == 9:
            maxima.append(tuple(sorted(R)))
        return
    U = P | X
    if U:
        u = max(U, key=lambda v: len(P & ADJ[v]))
        cand = list(P - ADJ[u])
    else:
        cand = list(P)
    for v in cand:
        bronk(R+[v], P & ADJ[v], X & ADJ[v])
        P.remove(v)
        X.add(v)

bronk([], set(range(N)), set())
maxima = sorted(set(maxima))
assert hist == Counter({6:1296, 7:28512, 9:8784}), hist
assert len(maxima) == 8784
assert max(hist) == 9

# Affine two-flats in F_3^4.
def is_affine(code):
    vecs = [WORDS[i] for i in code]
    base = vecs[0]
    D = {tuple((a-b)%3 for a,b in zip(v,base)) for v in vecs}
    if len(D) != 9 or (0,0,0,0) not in D:
        return False
    for u in D:
        for v in D:
            if tuple((a+b)%3 for a,b in zip(u,v)) not in D:
                return False
    return True

affine_count = sum(is_affine(C) for C in maxima)
assert affine_count == 252

# Generators for (S_3)^4 semidirect D_8: two transpositions in each
# coordinate, one cycle rotation, and one reflection.
gens = []
for c in range(4):
    for a,b in ((0,1),(1,2)):
        mp=[]
        for w in WORDS:
            z=list(w)
            if z[c] == a:
                z[c] = b
            elif z[c] == b:
                z[c] = a
            mp.append(INDEX[tuple(z)])
        gens.append(tuple(mp))
for coordperm in ((1,2,3,0),(0,3,2,1)):
    gens.append(tuple(INDEX[tuple(w[j] for j in coordperm)] for w in WORDS))

def act(code, mp):
    return tuple(sorted(mp[v] for v in code))

maxset = set(maxima)
seen = set()
orbits=[]
for C in maxima:
    if C in seen:
        continue
    seen.add(C)
    stack=[C]
    orb=[]
    while stack:
        X=stack.pop()
        orb.append(X)
        for mp in gens:
            Y=act(X,mp)
            assert Y in maxset
            if Y not in seen:
                seen.add(Y)
                stack.append(Y)
    orbits.append(orb)

orbit_sizes = sorted(len(o) for o in orbits)
assert orbit_sizes == [36,72,144,324,432,648,648,1296,1296,1296,2592]
affine_orbits = sorted(len(o) for o in orbits if all(is_affine(C) for C in o))
assert affine_orbits == [36,72,144]
assert sum(orbit_sizes) == 8784
assert sum(affine_orbits) == 252

# Explicit nonlinear maximum witness and a closure failure.
witness_words = [
    (0,0,0,0),(0,1,0,1),(0,2,0,2),
    (1,0,1,0),(1,1,2,2),(1,2,2,1),
    (2,0,2,0),(2,1,1,2),(2,2,1,1)
]
witness = tuple(sorted(INDEX[w] for w in witness_words))
assert witness in maxset
assert not is_affine(witness)
assert pair_distance((1,1,2,2),(1,2,2,1)) == 4
assert tuple((a+b)%3 for a,b in zip((1,1,2,2),(1,2,2,1))) == (2,0,1,0)
assert (2,0,1,0) not in witness_words

print(
    "VERIFY_OK "
    f"vertices={N} edges={sum(len(a) for a in ADJ)//2} "
    f"maximal_cliques={sum(hist.values())} histogram=6:{hist[6]},7:{hist[7]},9:{hist[9]} "
    f"maximum=9 labeled_maxima={len(maxima)} affine_maxima={affine_count} "
    "orbits=11 orbit_sizes=36,72,144,324,432,648,648,1296,1296,1296,2592 "
    "affine_orbits=36,72,144"
)
