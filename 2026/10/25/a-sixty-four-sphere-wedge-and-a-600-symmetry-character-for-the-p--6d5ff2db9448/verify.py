#!/usr/bin/env python3
"""Self-contained exact finite verification for the Paley-25 flag complex."""
from collections import Counter, defaultdict, deque
from itertools import combinations

P = 5
NVERT = 25

def xy(z):
    return divmod(z, P)

def mul(x, y):
    a, b = xy(x)
    c, d = xy(y)
    return P*((a*c+2*b*d)%P)+(a*d+b*c)%P

def add(x, y):
    a,b=xy(x); c,d=xy(y)
    return P*((a+c)%P)+(b+d)%P

def sub(x, y):
    a,b=xy(x); c,d=xy(y)
    return P*((a-c)%P)+(b-d)%P

SQUARES = {mul(x, x) for x in range(1, NVERT)}
assert SQUARES == {5, 10, 15, 20, 6, 12, 18, 24, 9, 13, 17, 21}
NEIGHBORS = [set(y for y in range(NVERT) if y != x and sub(x, y) in SQUARES)
             for x in range(NVERT)]
assert {len(A) for A in NEIGHBORS} == {12}
assert all((len(NEIGHBORS[x] & NEIGHBORS[y]) == (5 if y in NEIGHBORS[x] else 6))
           for x in range(NVERT) for y in range(x+1, NVERT))

LEVEL = {1: [(x,) for x in range(NVERT)]}
while True:
    prev = LEVEL[max(LEVEL)]
    nxt = [face + (v,) for face in prev for v in range(face[-1]+1, NVERT)
           if all(v in NEIGHBORS[x] for x in face)]
    if not nxt: break
    LEVEL[len(nxt[0])] = nxt
assert {k:len(v) for k,v in LEVEL.items()} == {1:25, 2:150, 3:250, 4:75, 5:15}
ALLFACES = set().union(*[set(v) for v in LEVEL.values()])
assert len(ALLFACES) == 515

# An explicit legal elementary-collapse sequence: each chosen proper face
# currently has a unique codimension-one coface, hence its upper interval
# consists of the matched pair alone in the relevant maximal dimension.
remaining = set(ALLFACES)
collapse_steps = []
for d, expected in [(4,15),(3,60)]:
    count = 0
    while True:
        facets = defaultdict(list)
        for face in remaining:
            if len(face) == d+1:
                for subface in combinations(face,d):
                    facets[subface].append(face)
        eligible = sorted((subface, cofaces[0])
                          for subface,cofaces in facets.items()
                          if len(cofaces)==1 and subface in remaining)
        if not eligible: break
        low,high = eligible[0]
        assert len(high)==len(low)+1 and set(low).issubset(high)
        assert all(not (set(low).issubset(other) and other!=high)
                   for other in remaining if len(other)>len(low))
        remaining.remove(low); remaining.remove(high)
        collapse_steps.append((low,high))
        count += 1
    assert count == expected, (d,count)
assert Counter(len(f) for f in remaining) == Counter({1:25,2:150,3:190})

# Fundamental group presentation: contract a spanning tree, record triangle
# attaching words, and perform only exact Tietze eliminations. Every letter
# occurs at most once in each chosen pivot relator, so solving is legal.
tree = set(); reached = {0}; queue = deque([0])
while queue:
    v = queue.popleft()
    for u in sorted(NEIGHBORS[v]):
        if u not in reached:
            reached.add(u)
            tree.add(tuple(sorted((u,v))))
            queue.append(u)
assert len(reached)==25 and len(tree)==24
edges = [e for e in LEVEL[2] if e not in tree]
gen = {e:i+1 for i,e in enumerate(edges)}
assert len(gen)==126

def letter(a,b):
    edge = tuple(sorted((a,b)))
    if edge in tree: return 0
    return gen[edge] if a<b else -gen[edge]

def free_reduce(word):
    stack=[]
    for w in word:
        if not w: continue
        if stack and stack[-1]==-w: stack.pop()
        else: stack.append(w)
    return stack

def cyclic_reduce(word):
    word=free_reduce(word)
    while len(word)>1 and word[0]==-word[-1]:
        word=word[1:-1]
    return word

relators = [cyclic_reduce([letter(a,b),letter(b,c),letter(c,a)])
            for (a,b,c) in LEVEL[3]]
assert len(relators)==250
pivots=[]
while True:
    possibilities=[]
    for j,r in enumerate(relators):
        freq=Counter(abs(k) for k in r)
        possibilities.extend((len(r),j,x) for x,count in freq.items() if count==1)
    if not possibilities: break
    _,j,x = min(possibilities)
    r=relators[j]
    i=next(i for i,a in enumerate(r) if abs(a)==x)
    replacement = ([-v for v in reversed(r[i+1:]+r[:i])]
                   if r[i]==x else r[i+1:]+r[:i])
    assert all(abs(v)!=x for v in replacement)
    for k,w in enumerate(relators):
        if j==k: continue
        substituted=[]
        for a in w:
            if a==x: substituted.extend(replacement)
            elif a==-x: substituted.extend(-v for v in reversed(replacement))
            else: substituted.append(a)
        relators[k]=cyclic_reduce(substituted)
    relators[j]=[]
    pivots.append((j,x,tuple(replacement)))
assert len(pivots)==126
assert set(x for j,x,w in pivots) == set(gen.values())
assert all(not word for word in relators)

# Optional independent mod-two chain ranks, not used to infer integral facts.
def gf2_rank(rows):
    piv={}
    for row in rows:
        while row:
            j=row.bit_length()-1
            if j in piv: row^=piv[j]
            else:
                piv[j]=row
                break
    return len(piv)

def boundary_rank(k):
    lower = {f:i for i,f in enumerate(LEVEL[k-1])}
    columns = []
    for face in LEVEL[k]:
        vec = 0
        for smaller in combinations(face,k-1):
            vec ^= 1<<lower[smaller]
        columns.append(vec)
    return gf2_rank(columns)
assert [boundary_rank(k) for k in (2,3,4,5)] == [24,126,60,15]

# The natural semiaffine group has 25*12*2=600 distinct graph automorphisms.
def frob(x):
    a,b=xy(x)
    return P*a + (-b)%P

def permutation(u,b,e):
    return tuple(add(mul(u,frob(x) if e else x),b) for x in range(NVERT))

def perm_sign(values):
    inversions=sum(values[i]>values[j] for i in range(len(values))
                   for j in range(i+1,len(values)))
    return -1 if inversions%2 else 1

def h2_trace(p):
    # Reduced simplicial Lefschetz formula, H_0=1, H_2 only positive homology.
    result = -1
    for dim,faces in LEVEL.items():
        coeff = (-1)**(dim-1)
        for face in faces:
            image = [p[x] for x in face]
            if tuple(sorted(image))==face:
                result += coeff*perm_sign(image)
    return result

character = Counter()
by_frob = Counter()
actions=set()
for e in (0,1):
    for u in sorted(SQUARES):
        for b in range(25):
            p=permutation(u,b,e)
            assert p not in actions
            actions.add(p)
            assert all(((p[j] in NEIGHBORS[p[i]]) == (j in NEIGHBORS[i]))
                       for i in range(NVERT) for j in range(i+1,NVERT))
            chi = h2_trace(p)
            character[chi] += 1
            by_frob[(e,chi)] += 1
assert len(actions)==600
assert character == Counter({0:450,-1:72,4:62,-16:15,64:1})
assert by_frob == Counter({(0,0):225,(0,4):62,(0,-1):12,(0,64):1,
                           (1,0):225,(1,-1):60,(1,-16):15})
trans_ch = Counter(h2_trace(permutation(5,b,0)) for b in range(25))
assert trans_ch == Counter({4:12,-1:12,64:1})
assert all(h2_trace(permutation(5,b,0)) == (64 if b==0 else 4 if b in SQUARES else -1)
           for b in range(25))
assert sum(trace*count for trace,count in character.items()) == 0

print('FIELD_SQUARE_DIRECTIONS', sorted(SQUARES))
print('FACE_VECTOR', [len(LEVEL[k]) for k in range(1,6)])
print('COLLAPSES_4_3', 15, 60, 'REMAINING_2_COMPLEX', (25,150,190))
print('FUNDAMENTAL_GROUP_GENERATORS_ELIMINATED', len(pivots), 'FINAL_RELATORS_NONTRIVIAL', sum(bool(r) for r in relators))
print('MOD_TWO_BOUNDARY_RANKS', [boundary_rank(k) for k in (2,3,4,5)])
print('INTEGRAL_HOMOTOPY', 'wedge of 64 two-spheres')
print('SEMIAFFINE_GROUP_ORDER', len(actions), 'H2_CHARACTER_HISTOGRAM', sorted(character.items()))
print('TRANSLATION_CHARACTER', sorted(trans_ch.items()), 'FULL_GROUP_H2_INVARIANTS', 0)
print('VERIFY_OK_PALEY25_FLAG_HOMOTOPY_SEMIAFFINE_CHARACTER')
