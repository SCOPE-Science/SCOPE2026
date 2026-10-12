#!/usr/bin/env python3
import itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# F4 encoding: 0,1,w,w^2 with w^2=w+1.
def add(a,b): return a^b
def mul(a,b):
    if a==0 or b==0: return 0
    e={1:0,2:1,3:2}; r={0:1,1:2,2:3}
    return r[(e[a]+e[b])%3]
def conj(a): return mul(a,a)

PTS=[(1,0),(0,1),(1,1),(1,2),(1,3)]

def det2(a,b,c,d):
    return add(mul(a,d),mul(b,c))

def gram_det(m):
    g=[[0,0],[0,0]]
    for count,(x,y) in zip(m,PTS):
        if count%2:
            g[0][0]=add(g[0][0],mul(x,conj(x)))
            g[0][1]=add(g[0][1],mul(x,conj(y)))
            g[1][0]=add(g[1][0],mul(y,conj(x)))
            g[1][1]=add(g[1][1],mul(y,conj(y)))
    return det2(g[0][0],g[0][1],g[1][0],g[1][1])

# Direct parity check.
for bits in itertools.product((0,1),repeat=5):
    t=sum(bits)
    expected=((t*(t-1)//2)%2)
    assert (gram_det(bits)!=0)==bool(expected)

# GL(2,4) and induced projective permutations.
def norm_projective(v):
    x,y=v
    z=x if x else y
    # invert nonzero z by z^2 because z^3=1.
    zi=conj(z)
    return (mul(x,zi),mul(y,zi))

pt_index={p:i for i,p in enumerate(PTS)}
perms=set()
for a,b,c,d in itertools.product(range(4),repeat=4):
    if det2(a,b,c,d)==0: continue
    p=[]
    for x,y in PTS:
        z=(add(mul(a,x),mul(b,y)), add(mul(c,x),mul(d,y)))
        p.append(pt_index[norm_projective(z)])
    perms.add(tuple(p))
assert len(perms)==CERT["verification"]["projective_group_size"]==60

def transform(m):
    return tuple(x+1 if x%2==0 else x-1 for x in m)

for p in perms:
    for bits in itertools.product((0,1),repeat=5):
        pb=tuple(bits[p[i]] for i in range(5))
        assert transform(pb)==tuple(transform(bits)[p[i]] for i in range(5))

def comps5(n):
    for a in range(n+1):
      for b in range(n-a+1):
       for c in range(n-a-b+1):
        for d in range(n-a-b-c+1):
         yield (a,b,c,d,n-a-b-c-d)

def canon(m):
    return min(tuple(m[p[i]] for i in range(5)) for p in perms)

def distance(m):
    return sum(m)-max(m)

def lcd_orbits(n, min_distance=None):
    out=set()
    for m in comps5(n):
        if gram_det(m)==0: continue
        # Nonsingular Gram already implies dimension two.
        if min_distance is not None and distance(m)<min_distance: continue
        out.add(canon(m))
    return out

for n in CERT["verification"]["even_lengths"]:
    left=lcd_orbits(n)
    right=lcd_orbits(n+1,min_distance=2)

    image={canon(transform(m)) for m in left}
    assert image==right

    for m in left:
        z=transform(m)
        assert sum(z)==n+1
        assert sum(x%2 for x in z)==3
        assert gram_det(z)!=0
        assert distance(z)>=2
        assert transform(z)==m

    for m in right:
        z=transform(m)
        assert sum(z)==n
        assert sum(x%2 for x in z)==2
        assert gram_det(z)!=0
        assert transform(z)==m

    assert len(left)==len(right)

print("VERIFY_OK")
