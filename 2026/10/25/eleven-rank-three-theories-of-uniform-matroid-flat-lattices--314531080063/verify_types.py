"""Exact three-round first-order types of uniform-matroid flat lattices.

The mathematical uniformity argument is in RESULT.md; this program evaluates
its Venn-cell recurrence exactly and checks representative and sampled cases.
"""
from itertools import product
from math import comb


def relation(a,b,c):
    if a == b == c: return 0
    if c == a: return 1
    if c == b: return 2
    return 3


def statuses(s):
    if s == 0: return [(0,0)]
    out=[(0,0),(s,2)]
    if s >= 2:out.append((1,1))
    return out


def pair_type(n,r,a,b,c):
    cells=(c,a-c,b-c,n-a-b+c)
    mask=0
    for states in product(*(statuses(s) for s in cells)):
        x=[p[0] for p in states]
        if sum(x)>=r:continue
        c_sub_a=(x[2]==x[3]==0)
        a_sub_c=(x[0]==cells[0] and x[1]==cells[1])
        c_sub_b=(x[1]==x[3]==0)
        b_sub_c=(x[0]==cells[0] and x[2]==cells[2])
        ca=0 if c_sub_a and a_sub_c else 1 if c_sub_a else 2 if a_sub_c else 3
        cb=0 if c_sub_b and b_sub_c else 1 if c_sub_b else 2 if b_sub_c else 3
        mask |= 1<<(4*ca+cb)
    mask |= 1 << (4*(0 if a==n else 2) + (0 if b==n else 2))
    return relation(a,b,c),mask


def pointed(n,r,a):
    return frozenset(pair_type(n,r,a,b,c)
       for b in list(range(r))+[n]
       for c in range(max(0,a+b-n),min(a,b)+1))


def complete_type(n,r):
    return frozenset(pointed(n,r,a) for a in list(range(r))+[n])


def label(row):
    return ' '.join(f'{k}:{m:04x}' for k,m in sorted(row))


def run():
    # Exact canonical table, representatives chosen within the original family.
    representatives=[(1,1)]
    for r in range(2,7):representatives.extend(((r,r),(r+1,r)))
    theories={complete_type(n,r):i for i,(n,r) in enumerate(representatives)}
    assert len(theories)==11
    max_flats=max(1+sum(comb(n,j) for j in range(r)) for n,r in representatives)
    assert max_flats==121
    for n in range(1,26):
        for r in range(1,n+1):
            key=complete_type(n,r)
            assert key in theories,(n,r,'unexpected type')
            expected=0 if r==1 else 2*(min(r,6)-2)+1+(n>r)
            assert theories[key]==expected,(n,r,expected,theories[key])
    print('EXACT_ORBITS_OK n=1..25 classes=11 rank_saturation=6')
    for boolean,n,r in [(True,6,6),(False,7,6)]:
        for name,a in [('bottom',0),('atom',1),('second',2),('middle',3),('co-second',4),('coatom',5),('top',n)]:
            print(('BOOLEAN' if boolean else 'TRUNCATED'),name,label(pointed(n,r,a)))
    print('SHARP_REPRESENTATIVE_OK n=7 r=6 flats=121')
    print('VERIFY_OK')

if __name__=='__main__':run()
