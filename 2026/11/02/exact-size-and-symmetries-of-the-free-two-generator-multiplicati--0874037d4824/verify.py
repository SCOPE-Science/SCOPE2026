#!/usr/bin/env python3
"""Exact finite congruence computation for a two-generator constant-free semiring.

Use Python 3 standard library only. No untrusted inputs or network accesses.
The parameters exhaust *all* polynomial representatives, not a sample.
"""
from collections import Counter, deque

WORDS = ("a", "b", "ab", "ba", "aba", "bab")

def simplify(word):
    while True:
        old = word
        for a, b in (("aa", "a"), ("bb", "b"), ("abab", "ab"), ("baba", "ba")):
            word = word.replace(a, b)
        if word == old:
            return word

INDEX = {w:i for i,w in enumerate(WORDS)}
BAND = [[INDEX[simplify(u+v)] for v in WORDS] for u in WORDS]
assert all(BAND[i][i] == i for i in range(6))
assert all(BAND[BAND[i][j]][k] == BAND[i][BAND[j][k]]
           for i in range(6) for j in range(6) for k in range(6))

# Coefficients: 0=absent, 1=one copy, 2=positive even, 3=odd >=3.
ADD = ((0,1,2,3),(1,2,3,2),(2,3,2,3),(3,2,3,2))
DIGITS = [tuple((n >> (2*i)) & 3 for i in range(6)) for n in range(4096)]

def code(d):
    return sum(c << (2*i) for i,c in enumerate(d))

def plus(p,q):
    return code([ADD[x][y] for x,y in zip(DIGITS[p],DIGITS[q])])

def product(p,q):
    z = [0]*6
    for i,x in enumerate(DIGITS[p]):
        if x:
            for j,y in enumerate(DIGITS[q]):
                if y:
                    k = x*y
                    z[BAND[i][j]] = ADD[z[BAND[i][j]]][1 if k==1 else 2 if k%2==0 else 3]
    return code(z)

# The least congruence containing (p,p*p) for each of the 4095 elements:
# addition by six basis monomials and left/right multiplication by a,b
# form a complete list of unary contexts, via distributivity.
parent = list(range(4096)); sizes = [1]*4096

def root(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

queue = deque((p,product(p,p)) for p in range(1,4096))
add_generators = [1 << (2*i) for i in range(6)]
mul_generators = [1, 4]
merges = 0; processed = 0
while queue:
    p,q = queue.popleft(); processed += 1
    x,y = root(p),root(q)
    if x == y:
        continue
    if sizes[x] < sizes[y]: x,y = y,x
    parent[y] = x; sizes[x] += sizes[y]; merges += 1
    for g in add_generators:
        queue.append((plus(p,g),plus(q,g)))
    for g in mul_generators:
        queue.append((product(p,g),product(q,g)))
        queue.append((product(g,p),product(g,q)))

blocks={}
for p in range(1,4096):
    blocks.setdefault(root(p),[]).append(p)
assert len(blocks) == 94 and merges == 4095-94
assert all(root(product(p,p))==root(p) for p in range(1,4096))
# Explicitly ensure the equivalence is stable under the generating contexts.
for block in blocks.values():
    representative = block[0]
    for p in block:
        for g in add_generators:
            assert root(plus(p,g)) == root(plus(representative,g))
        for g in mul_generators:
            assert root(product(p,g)) == root(product(representative,g))
            assert root(product(g,p)) == root(product(g,representative))

reps = [v[0] for v in blocks.values()]
labels = {root(p):i for i,p in enumerate(reps)}
L = len(reps)
addition = [[labels[root(plus(p,q))] for q in reps] for p in reps]
multiplication = [[labels[root(product(p,q))] for q in reps] for p in reps]
a = labels[root(1)]; b = labels[root(4)]
assert a != b
# Exhaustive, independent quotient axioms: every triple of 94 elements.
for i in range(L):
    assert multiplication[i][i] == i
    for j in range(L):
        assert addition[i][j] == addition[j][i]
        for k in range(L):
            assert addition[addition[i][j]][k] == addition[i][addition[j][k]]
            assert multiplication[multiplication[i][j]][k] == multiplication[i][multiplication[j][k]]
            assert multiplication[i][addition[j][k]] == addition[multiplication[i][j]][multiplication[i][k]]
            assert multiplication[addition[i][j]][k] == addition[multiplication[i][k]][multiplication[j][k]]

def generated_size(x,y):
    seen = {x,y}; frontier = [x,y]
    while frontier:
        w = frontier.pop()
        for z in tuple(seen):
            for t in (addition[w][z], multiplication[w][z], multiplication[z][w]):
                if t not in seen:
                    seen.add(t); frontier.append(t)
                    if len(seen) == L:
                        return L
    return len(seen)

assert generated_size(a,b) == 94
ordered_generating_pairs = [(i,j) for i in range(L) for j in range(L) if generated_size(i,j)==L]
assert len(ordered_generating_pairs)==2
assert set(ordered_generating_pairs)=={(a,b),(b,a)}

print('BAND_SIZE=6 FORMAL_POLYNOMIALS=4095')
print('CONGRUENCE_MERGES=',merges,'CONGRUENCE_CLASSES=',len(blocks),'PROCESSED_PAIRS=',processed)
print('QUOTIENT_SEMIRING_AXIOMS=PASS for all 94^3 triples')
print('GENERATING_ORDERED_PAIRS=',len(ordered_generating_pairs),'AUTOMORPHISM_GROUP_ORDER=2')
print('CLASS_SIZE_HISTOGRAM=',sorted(Counter(map(len,blocks.values())).items()))
print('VERIFY_OK')

# Separate supporting comparison: if multiplication is additionally commutative,
# the free multiplicative band has the three words a,b,ab. This is a different
# quotient universe and is not used to obtain the noncommutative count above.
CB = ((0,2,2),(2,1,2),(2,2,2))
CD = [tuple((p >> (2*i)) & 3 for i in range(3)) for p in range(64)]
def cenc(z):
    return sum(c << (2*i) for i,c in enumerate(z))
def cplus(p,q):
    return cenc([ADD[x][y] for x,y in zip(CD[p],CD[q])])
def cprod(p,q):
    z = [0,0,0]
    for i,x in enumerate(CD[p]):
        for j,y in enumerate(CD[q]):
            t=x*y
            if t: z[CB[i][j]]=ADD[z[CB[i][j]]][1 if t==1 else 2 if t%2==0 else 3]
    return cenc(z)
cp=list(range(64)); cq=deque((p,cprod(p,p)) for p in range(1,64))
def cr(x):
    while cp[x]!=x:
        cp[x]=cp[cp[x]];x=cp[x]
    return x
while cq:
    x,y=cq.popleft();rx,ry=cr(x),cr(y)
    if rx==ry:continue
    cp[ry]=rx
    for g in (1,4,16):cq.append((cplus(x,g),cplus(y,g)))
    for g in (1,4):
        cq.append((cprod(x,g),cprod(y,g)))
        cq.append((cprod(g,x),cprod(g,y)))
assert len({cr(x) for x in range(1,64)})==39
print('COMMUTATIVE_RANK_TWO_CLASSES=39; different subvariety; PASS')
