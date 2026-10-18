#!/usr/bin/env python3
"""Reconstruct the Heawood matching-complex homology and GL(3,2) character.
Requires only Python 3 standard library. All enumerations are exhaustive.
"""
from collections import Counter, defaultdict
from itertools import product

V = tuple(range(1, 8))
parity = lambda x: x.bit_count() & 1
EDGES = tuple((p, a) for p in V for a in V if parity(p & a) == 0)
assert len(EDGES) == 21
assert all(sum(1 for p,a in EDGES if p==v)==3 for v in V)
assert all(sum(1 for p,a in EDGES if a==v)==3 for v in V)
assert all(sum(1 for p,a in EDGES if p==u and (parity(v&a)==0))==1 for u in V for v in V if u<v)

# Every face is a partial bijection between the point and line sets.
FACES = [0]
for i,(p,a) in enumerate(EDGES):
    FACES += [f|(1<<i) for f in FACES
              if all(not ((f>>j)&1) or (pp!=p and aa!=a)
                     for j,(pp,aa) in enumerate(EDGES))]
FACE_SET = set(FACES)
assert len(FACES)==len(FACE_SET)==3462
FCOUNTS=Counter(f.bit_count() for f in FACES)
assert tuple(FCOUNTS[k] for k in range(8)) == (1,21,168,644,1218,1050,336,24)

# Exact simplicial boundary ranks over F_2. Dimensions 1 through 6.
BY_SIZE={k: sorted(f for f in FACES if f.bit_count()==k) for k in range(8)}
def boundary_rank(k):
    base={f:i for i,f in enumerate(BY_SIZE[k-1])}
    pivots={}
    for f in BY_SIZE[k]:
        x=0
        for j in range(21):
            if f&(1<<j):
                x ^= 1<<base[f^(1<<j)]
        while x:
            p=x.bit_length()-1
            if p in pivots: x^=pivots[p]
            else: pivots[p]=x; break
    return len(pivots)
RANKS=tuple(boundary_rank(k) for k in range(2,8))
assert RANKS == (20,148,496,722,312,24),RANKS

# GL(3,2) acts on the seven nonzero vectors of F_2^3, and the seven
# nonzero covectors contragrediently. For each B, compute its edge action.
def apply(B,x):
    return (B[0] if x&1 else 0) ^ (B[1] if x&2 else 0) ^ (B[2] if x&4 else 0)
BASIS=(1,2,4)
MATRICES=[b for b in product(V,repeat=3)
          if len({apply(b,x) for x in V})==7]
assert len(MATRICES)==168
INDEX={e:i for i,e in enumerate(EDGES)}
GROUP=[]
EPERMS=[]
for B in MATRICES:
    points={p:apply(B,p) for p in V}
    lines={a:next(ap for ap in V
                  if all(parity(apply(B,x)&ap)==parity(x&a) for x in BASIS))
           for a in V}
    gp=tuple(points[p] for p in V)
    ep=tuple(INDEX[(points[p],lines[a])] for p,a in EDGES)
    assert len(set(ep))==21
    GROUP.append(gp);EPERMS.append(ep)
assert len(set(GROUP))==168

ID=tuple(V)
def compose(g,h):
    return tuple(g[h[i]-1] for i in range(7))
def perm_order(g):
    t=ID
    for k in range(1,169):
        t=compose(g,t)
        if t==ID:return k
    raise AssertionError('not finite order dividing 168')
def inverse(g):
    a=[None]*7
    for i,v in enumerate(g):a[v-1]=i+1
    return tuple(a)

# Direct oriented fixed-face calculation (without orbit shortcuts).
def sign_images(indices):
    return -1 if sum(x>y for i,x in enumerate(indices)
                     for y in indices[i+1:])%2 else 1

def direct_trace(ep):
    s=-1  # reduced Lefschetz = ordinary Lefschetz - 1
    for face in FACES:
        if face==0:continue
        chosen=[i for i in range(21) if face>>i&1]
        img=[ep[i] for i in chosen]
        if set(img)==set(chosen):
            s+=(-1)**(len(chosen)-1)*sign_images(img)
    return s

# Orbital matching polynomial at -1 is an independent character algorithm.
def orbital_trace(ep):
    seen=set();viable=[]
    for i in range(21):
        if i in seen:continue
        orbit=[];j=i
        while j not in seen:
            seen.add(j);orbit.append(j);j=ep[j]
        es=[EDGES[j] for j in orbit]
        if len({p for p,a in es})==len(es) and len({a for p,a in es})==len(es):
            viable.append((set(p for p,a in es),set(a for p,a in es)))
    def rec(i,P,L):
        if i==len(viable):return 1
        n=rec(i+1,P,L)
        ps,ls=viable[i]
        if not (ps&P or ls&L):n-=rec(i+1,P|ps,L|ls)
        return n
    return -rec(0,set(),set())

assert Counter(perm_order(g) for g in GROUP)=={1:1,2:21,3:56,4:42,7:48}
CHARS={}
for g,ep in zip(GROUP,EPERMS):
    a=direct_trace(ep)
    b=orbital_trace(ep)
    assert a==b,(g,a,b)
    CHARS[g]=a
char_by_order=defaultdict(set)
for g in GROUP: char_by_order[perm_order(g)].add(CHARS[g])
assert dict(char_by_order)=={1:{16},2:{0},3:{1},4:{0},7:{2}},char_by_order

# Eight Sylow-7 subgroups: each of 48 order-7 elements occurs in one
# subgroup of size 7, so there are exactly 8. Compute the conjugation action.
subgroups=set()
for g in GROUP:
    if perm_order(g)!=7:continue
    h=ID;S=[]
    for i in range(7):
        S.append(h);h=compose(g,h)
    subgroups.add(frozenset(S))
assert len(subgroups)==8
PI={}
for g in GROUP:
    gi=inverse(g)
    PI[g]=sum(1 for S in subgroups
              if frozenset(compose(compose(g,h),gi) for h in S)==S)
pi_by_order=defaultdict(set)
for g in GROUP:pi_by_order[perm_order(g)].add(PI[g])
assert dict(pi_by_order)=={1:{8},2:{0},3:{2},4:{0},7:{1}},pi_by_order

# Real character inner product and multiplicities of 1, the 7-dimensional
# augmentation subrepresentation of the Sylow-7 permutation module, and
# the 8-dimensional residual module.
def inner(a,b):
    numer=sum(a[g]*b[g] for g in GROUP)
    assert numer%168==0,(numer,a,b)
    return numer//168
ONE={g:1 for g in GROUP}
SEVEN={g:PI[g]-1 for g in GROUP}
EIGHT={g:CHARS[g]-PI[g] for g in GROUP}
assert CHARS[ID]==16
assert inner(SEVEN,SEVEN)==inner(EIGHT,EIGHT)==1
assert inner(ONE,SEVEN)==inner(ONE,EIGHT)==inner(SEVEN,EIGHT)==0
assert inner(CHARS,ONE)==inner(CHARS,SEVEN)==inner(CHARS,EIGHT)==1
assert all(CHARS[g]==ONE[g]+SEVEN[g]+EIGHT[g] for g in GROUP)
print('VERIFY_OK faces=3462 f_vector=(21,168,644,1218,1050,336,24)',
      'boundary_ranks=',RANKS,
      'group=168 order_classes={1:1,2:21,3:56,4:42,7:48}',
      'chi={1:16,2:0,3:1,4:0,7:2}',
      'sylow7_perm={1:8,2:0,3:2,4:0,7:1}',
      'representation=1+7+8')
