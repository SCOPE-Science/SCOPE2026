#!/usr/bin/env python3
from itertools import product
from collections import Counter

Q = 3
COLS = [
(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),(0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1),
(1,0,2,0,0,0),(1,0,1,0,0,0),(0,0,0,0,1,2),(0,0,0,0,1,1),(0,1,0,2,0,0),(0,1,0,1,0,0),
(1,1,1,2,2,0),(0,1,2,1,1,1),(1,0,2,1,1,2),(1,2,0,0,0,1),(1,0,0,1,2,2),(1,2,2,2,0,1),
(0,1,2,2,1,2),(1,1,2,0,0,1),(1,2,1,2,1,0),(1,0,1,1,1,1),(0,1,2,0,2,1),(0,0,1,2,1,0),(0,0,0,1,2,2),
]

def rank_mod3(rows):
    a=[list(x) for x in rows if any(y % 3 for y in x)]
    if not a:
        return 0
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c] % 3),None)
        if p is None:
            continue
        a[r],a[p]=a[p],a[r]
        inv=1 if a[r][c] % 3 == 1 else 2
        a[r]=[(inv*x)%3 for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c] % 3:
                f=a[i][c] % 3
                a[i]=[(a[i][j]-f*a[r][j])%3 for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def normalize(v):
    v=tuple(x%3 for x in v)
    for x in v:
        if x:
            inv=1 if x==1 else 2
            return tuple((inv*y)%3 for y in v)
    raise ValueError('zero vector')

def codeword(u):
    return tuple(sum(u[i]*c[i] for i in range(6))%3 for c in COLS)

assert len(COLS)==25 and len(set(COLS))==25
assert all(normalize(c)==c for c in COLS)
assert rank_mod3(COLS)==6
messages=list(product(range(3),repeat=6))
code=[codeword(u) for u in messages]
assert len(set(code))==729

nonzero=[(u,c) for u,c in zip(messages,code) if any(u)]
weights=Counter(sum(x!=0 for x in c) for _,c in nonzero)
assert dict(sorted(weights.items())) == {11:6,12:34,13:46,14:52,15:82,16:82,17:106,18:126,19:142,20:52}

projective=[]
for u,c in nonzero:
    if normalize(u)==u:
        support=frozenset(i for i,x in enumerate(c) if x)
        projective.append((u,support))
assert len(projective)==364
for i,(_,s) in enumerate(projective):
    for _,t in projective[i+1:]:
        assert not s <= t and not t <= s

# Direct trifference check after translating a triple so its third word is zero.
# In F_3, a scalar-dependent pair is necessarily y=2x; otherwise an independent
# pair must have a coordinate containing the two distinct nonzero symbols.
for ai in range(1,len(messages)):
    x=messages[ai]; cx=code[ai]
    for bi in range(ai+1,len(messages)):
        y=messages[bi]; cy=code[bi]
        if all(y[j] == (2*x[j])%3 for j in range(6)):
            assert any(cx[k] for k in range(25))
        else:
            assert any(cx[k] and cy[k] and cx[k]!=cy[k] for k in range(25))

normals=[u for u in messages[1:] if normalize(u)==u]
assert len(normals)==364
intersection_sizes=Counter(); intersection_ranks=Counter()
for a in normals:
    pts=[c for c in COLS if sum(a[i]*c[i] for i in range(6))%3==0]
    r=rank_mod3(pts)
    intersection_sizes[len(pts)]+=1
    intersection_ranks[r]+=1
    assert r==5

print('rank=6')
print('projective_columns=25')
print('codewords=729')
print('minimum_distance=11')
print('weight_distribution='+repr(dict(sorted(weights.items()))))
print('projective_supports=364; pairwise_incomparable=yes')
print('trifference_pairs_checked=264628')
print('hyperplanes_checked=364')
print('hyperplane_intersection_size_distribution='+repr(dict(sorted(intersection_sizes.items()))))
print('hyperplane_rank_distribution='+repr(dict(sorted(intersection_ranks.items()))))
print('VERIFY_OK')
