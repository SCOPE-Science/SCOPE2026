#!/usr/bin/env python3
"""Finite and exact checks for the blocking-cubic classification over GF(3).
Standard-library Python; run: python3 verify.py
"""
from itertools import product, combinations
from collections import Counter

F = 3
monomials = [(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),
             (1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]

def normalize(v):
    u=next(t for t in v if t)
    c=pow(u,-1,F)
    return tuple(c*t%F for t in v)

points = sorted({normalize(v) for v in product(range(F), repeat=3)
                 if any(v)})
assert len(points)==13
lines = [sum(1<<i for i,(x,y,z) in enumerate(points)
             if (a*x+b*y+c*z)%F==0)
         for a,b,c in points]
assert len(set(lines))==13 and all(v.bit_count()==4 for v in lines)


def blocked(mask):
    return all(mask & line for line in lines)

minimal = []
for mask in range(1,1<<13):
    if blocked(mask) and all(not blocked(mask^(1<<i))
                             for i in range(13) if (mask>>i)&1):
        minimal.append(mask)
assert Counter(m.bit_count() for m in minimal)=={4:13,6:234}

triangles=set()
for a,b,c in combinations(lines,3):
    if a&b&c:
        continue
    vertices=(a&b)|(a&c)|(b&c)
    six=(a|b|c)&~vertices
    assert six.bit_count()==6
    triangles.add(six)
assert len(triangles)==234
assert set(minimal)==triangles|set(lines)

base = {(0,1,1),(0,1,2),(1,0,1),(1,0,2),(1,1,0),(1,2,0)}
base_mask=sum(1<<i for i,p in enumerate(points) if p in base)
assert base_mask in triangles

# Coordinate functions A,B,C,G from the proof, using the chosen monomial order.
def pencil(A,B,C,G):
    return (A,-B,-C,-A,G,-A,B,-C,-B,C)

def evaluations(w):
    return tuple(sum(k*pow(x,a,F)*pow(y,b,F)*pow(z,c,F)
                     for k,(a,b,c) in zip(w,monomials))%F
                 for x,y,z in points)

canonical=[]
for a,b,c,g in product(range(F),repeat=4):
    if not any((a,b,c,g)):
        continue
    if next(x for x in (a,b,c,g) if x)!=1:
        continue
    vals=evaluations(pencil(a,b,c,g))
    mask=sum(1<<i for i,v in enumerate(vals) if not v)
    assert mask&base_mask==base_mask
    if mask==base_mask:
        canonical.append((a,b,c,g))
    else:
        assert any(mask&l==l for l in lines)
assert len(canonical)==4
assert set(canonical)=={(1,1,1,1),(1,1,2,2),
                       (1,2,1,2),(1,2,2,1)}

# Independent full-coefficient census: any polynomial vanishing on all four
# rational points of a line has that line as an actual polynomial factor,
# because its degree is three and the four points are pairwise distinct.
rows=[tuple(pow(x,a,F)*pow(y,b,F)*pow(z,c,F)
            for a,b,c in monomials) for x,y,z in points]
count_form=count_block=count_noline=0
point_hist=Counter()
for w in product(range(3),repeat=10):
    if not any(w) or next(x for x in w if x)!=1:
        continue
    count_form+=1
    mask=0
    for i,row in enumerate(rows):
        if sum(a*b for a,b in zip(w,row))%3==0:
            mask|=1<<i
    if not blocked(mask):
        continue
    count_block+=1
    if not any(mask&l==l for l in lines):
        count_noline+=1
        point_hist[mask.bit_count()]+=1
assert (count_form,count_block,count_noline)==(29524,4940,936)
assert point_hist=={6:936}
assert 234*4==936
# Cardinality of PGL_3(F3) = [(27-1)(27-3)(27-9)]/(3-1).
group_order=(27-1)*(27-3)*(27-9)//2
assert group_order==5616 and group_order//936==6
print('13 points and lines; 234 vertexless triangles; 40 pencil forms;')
print('4 smooth-candidate forms on each triangle; 29524 normalized cubics;')
print('4940 blocking cubics; exactly 936 without a rational line factor;')
print('all 936 have six rational points; stabilizer order six: PASS')
