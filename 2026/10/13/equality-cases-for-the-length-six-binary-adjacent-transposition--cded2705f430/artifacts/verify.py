#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque, Counter

N=6
WORDS=tuple(range(1<<N))

def bits(x):
    return tuple((x>>(N-1-i))&1 for i in range(N))

def wordstr(x):
    return ''.join(map(str,bits(x)))

def weight(x):
    return x.bit_count()

def swap_adj(x,i):
    b=list(bits(x)); b[i],b[i+1]=b[i+1],b[i]
    y=0
    for v in b: y=(y<<1)|v
    return y

def ball(x):
    return frozenset([x]+[swap_adj(x,i) for i in range(N-1)])

BALL={x:ball(x) for x in WORDS}
LAYERS={k:tuple(x for x in WORDS if weight(x)==k) for k in range(N+1)}

def compatible_ball(x,y):
    return BALL[x].isdisjoint(BALL[y])

def token_neighbors(x):
    return frozenset(swap_adj(x,i) for i in range(N-1) if swap_adj(x,i)!=x)

# Independent graph-distance construction inside each weight layer.
DIST={}
for k,V in LAYERS.items():
    Vset=set(V)
    for s in V:
        d={s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for v in token_neighbors(u):
                assert v in Vset
                if v not in d:
                    d[v]=d[u]+1; q.append(v)
        for t in V: DIST[(s,t)]=d.get(t,10**9)
for k,V in LAYERS.items():
    for x,y in combinations(V,2):
        assert compatible_ball(x,y) == (DIST[(x,y)]>=3)

TARGET=(1,2,4,6,4,2,1)
EXPECTED_COUNTS=(1,6,14,1,14,6,1)
layer_opt=[]
for k,(t,exp) in enumerate(zip(TARGET,EXPECTED_COUNTS)):
    V=LAYERS[k]
    goods=[]
    for S in combinations(V,t):
        if all(compatible_ball(x,y) for x,y in combinations(S,2)):
            goods.append(tuple(S))
    assert len(goods)==exp,(k,len(goods),exp)
    if t+1<=len(V):
        bigger=0
        for S in combinations(V,t+1):
            if all(compatible_ball(x,y) for x,y in combinations(S,2)):
                bigger+=1
        assert bigger==0,(k,bigger)
    layer_opt.append(tuple(goods))

# Since adjacent transpositions preserve weight, balls from distinct weights are disjoint.
for x,y in combinations(WORDS,2):
    if weight(x)!=weight(y):
        assert BALL[x].isdisjoint(BALL[y])

assert sum(TARGET)==20
expected_total=1
for z in EXPECTED_COUNTS: expected_total*=z
assert expected_total==7056

maxima=[]
for choices in product(*layer_opt):
    C=frozenset(x for S in choices for x in S)
    assert len(C)==20
    assert all(compatible_ball(x,y) for x,y in combinations(C,2))
    maxima.append(C)
assert len(maxima)==7056 and len(set(maxima))==7056

middle=tuple(sorted(layer_opt[3][0]))
expected_middle=tuple(int(s,2) for s in ['000111','001110','011100','100011','110001','111000'])
assert middle==expected_middle

# Natural channel symmetries: complement and reversal.
def comp(x): return x^((1<<N)-1)
def rev(x): return int(wordstr(x)[::-1],2)
def act(C,c,r):
    out=set()
    for x in C:
        y=comp(x) if c else x
        y=rev(y) if r else y
        out.add(y)
    return frozenset(out)
G=[(0,0),(1,0),(0,1),(1,1)]
Mset=set(maxima)
for C in maxima:
    for g in G: assert act(C,*g) in Mset
seen=set(); orbit_sizes=[]
for C in maxima:
    if C in seen: continue
    O={act(C,*g) for g in G}
    seen |= O; orbit_sizes.append(len(O))
assert len(seen)==7056
os=Counter(orbit_sizes)
assert os==Counter({4:1720,2:86,1:4}),os
fixed={g:sum(act(C,*g)==C for C in maxima) for g in G}
assert fixed[(0,0)]==7056
assert fixed[(1,0)]==84
assert fixed[(0,1)]==16
assert fixed[(1,1)]==84

# Secondary reproducible profile: number of received words covered by each maximum.
coverage=Counter(len(set().union(*(BALL[x] for x in C))) for C in maxima)
expected_cov={46:1,47:12,48:62,49:200,50:479,51:880,52:1280,53:1464,54:1311,55:868,56:394,57:96,58:9}
assert dict(sorted(coverage.items()))==expected_cov,coverage

print('VERIFY_OK',
      'vertices=64',
      'maximum=20',
      'labeled_maxima=7056',
      'layer_sizes='+','.join(map(str,TARGET)),
      'layer_optima='+','.join(map(str,EXPECTED_COUNTS)),
      'middle='+','.join(wordstr(x) for x in middle),
      'natural_group=4',
      'orbits=1810',
      'orbit_sizes=1x4,2x86,4x1720',
      'fixed_complement=84',
      'fixed_reversal=16',
      'fixed_complement_reversal=84')
print('COVERAGE',','.join(f'{k}:{v}' for k,v in sorted(coverage.items())))
