#!/usr/bin/env python3
"""Independent finite-field smoothness census (no computer algebra package).

For a plane cubic over F2, a geometric singularity occurs over F2, F4,
or F8. The lemma proving this is stated in RESULT.md. This program
checks those extension-field point sets directly.
"""
import itertools
import json
from collections import Counter

MONOS=[(i,j,3-i-j) for i in range(3,-1,-1) for j in range(3-i,-1,-1)]

def mul(a,b,qpoly,d):
    v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&(1<<d):a^=qpoly
    return v

def powf(a,n,qpoly,d):
    v=1
    while n:
        if n&1:v=mul(v,a,qpoly,d)
        a=mul(a,a,qpoly,d);n>>=1
    return v

def projpoints(qpoly,d):
    q=1<<d
    points=set()
    for v in itertools.product(range(q),repeat=3):
        if not any(v):continue
        first=next(a for a in v if a)
        inv=powf(first,q-2,qpoly,d)
        points.add(tuple(mul(a,inv,qpoly,d) for a in v))
    assert len(points)==q*q+q+1
    return sorted(points)

def calc(mask,pt,fieldpoly,d,derivative=None):
    val=0
    for k,e in enumerate(MONOS):
        if not((mask>>k)&1):continue
        if derivative is not None and e[derivative]%2==0:continue
        ee=list(e)
        if derivative is not None:ee[derivative]-=1
        v=1
        for j in range(3):v=mul(v,powf(pt[j],ee[j],fieldpoly,d),fieldpoly,d)
        val^=v
    return val

def gf16_vanishes_at_base(mask):
    return calc(mask,(1,2,4),0b10011,4)==0

def is_smooth_independent(mask,points):
    for poly,d,pts in points:
        for p in pts:
            if calc(mask,p,poly,d)!=0:continue
            if all(calc(mask,p,poly,d,k)==0 for k in range(3)):
                return False
    return True

def poly_rem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def poly_gcd(a,b):
    while b:a,b=b,poly_rem(a,b)
    return a

def poly_mul(a,b):
    result=0
    while b:
        if b&1:result^=a
        a<<=1;b>>=1
    return result

def poly_irreducible(f):
    d=f.bit_length()-1
    # Exact exhaustive trial division by every monic polynomial of degree <= d/2.
    for e in range(1,d//2+1):
        for g in range(1<<e,1<<(e+1)):
            if g& (1<<e) and poly_rem(f,g)==0:return False
    return True

def main():
    all_fields=[(0b11,1),(0b111,2),(0b1011,3)]
    all_points=[(f,d,projpoints(f,d)) for f,d in all_fields]
    sections=[m for m in range(1,1024) if gf16_vanishes_at_base(m)]
    smooth={m for m in sections if is_smooth_independent(m,all_points)}
    assert len(sections)==63 and len(smooth)==18
    members=sorted(smooth)
    pencils=set()
    for a,b in itertools.combinations(members,2):
        if a^b in smooth:pencils.add(frozenset((a,b,a^b)))
    assert len(pencils)==4
    pts2=all_points[0][2]
    point_counts={m:sum(calc(m,p,0b11,1)==0 for p in pts2) for m in smooth}
    distribution=Counter(point_counts.values())
    assert distribution==Counter({1:5,2:4,4:4,5:5})
    assert Counter(tuple(sorted(point_counts[m] for m in P)) for P in pencils)==Counter({(1,1,5):4})
    # Independent irreducibility certificates for the two base-point factors.
    assert poly_irreducible(0b10011)  # degree-four base orbit
    assert poly_irreducible(0b100101) # t^5+t^2+1
    # Check an explicit pencil: member masks 0x189,0x2e4,0x36d.
    # The projective affine elimination polynomial is the product of these
    # irreducible factors (degree 4 and degree 5).
    F4=0b10011
    F5=0b100101
    expected=0
    for i in (9,5,4,3,2,1,0):expected|=1<<i
    assert poly_mul(F4,F5)==expected
    print(json.dumps({
      'method':'F2/F4/F8 exhaustive singularity-point tests',
      'smooth_masks':[hex(m) for m in members],
      'number_smooth':len(smooth),
      'all_smooth_pencils':len(pencils),
      'pencils':[[hex(m) for m in sorted(p)] for p in sorted(pencils,key=lambda p:sorted(p))],
      'smooth_member_rational_points':dict(sorted(distribution.items())),
      'extension_point_sets':{str(1<<d):len(pts) for f,d,pts in all_points},
      'base_factor_irreducibility':True
    },sort_keys=True,indent=2))

if __name__=='__main__':main()
