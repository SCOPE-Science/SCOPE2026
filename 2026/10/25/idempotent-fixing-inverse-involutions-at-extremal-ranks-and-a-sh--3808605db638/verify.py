"""Standalone finite checks for inverse matchings of isotone transformation monoids.
Only the standard library is needed.  Infinite families are proved in RESULT.md.
"""
from itertools import combinations
from math import comb
from pathlib import Path

BASE = Path(__file__).resolve().parent

def multiply(f, g):
    # (f o g)(x)
    return tuple(f[y-1] for y in g)

def is_inverse(f, g):
    return multiply(multiply(f, g), f) == f and multiply(multiply(g, f), g) == g

def rk(f):
    return len(set(f))

def mat_rank2(n, a, b, c):
    assert 1 <= a < n and 1 <= b < c <= n
    return tuple(b if i <= a else c for i in range(1, n+1))

def rank2_tau(a, b, c):
    if a < b:
        return (c-1, a, b)
    if a >= c:
        return (b, c, a+1)
    return (a, b, c)

def mat_corank1(n, a, b):
    assert 1 <= a < n and 1 <= b <= n
    image = [v for v in range(1, n+1) if v != b]
    return tuple(image[i - 1 if i <= a else i - 2] for i in range(1, n+1))

def corank1_tau(a,b):
    if b<a:
        return (b,a+1)
    if b>a+1:
        return (b-1,a)
    return (a,b)

def mat_rank3_n5(code):
    cuts, image = code.split('|')
    assert len(cuts) == 2 and len(image) == 3
    aa = tuple(int(x) for x in cuts)
    bb = tuple(int(x) for x in image)
    assert 1 <= aa[0] < aa[1] <= 4 and 1 <= bb[0] < bb[1] < bb[2] <= 5
    return tuple(bb[0] if x <= aa[0] else bb[1] if x <= aa[1] else bb[2] for x in range(1,6))

checks = 0
for n in range(3, 13):
    seen2 = set(); seen1 = set()
    fixed2 = 0; fixed1 = 0
    for a in range(1,n):
        for b in range(1,n+1):
            for c in range(b+1,n+1):
                x=(a,b,c); y=rank2_tau(*x)
                assert rank2_tau(*y)==x and is_inverse(mat_rank2(n,*x), mat_rank2(n,*y))
                assert (x==y)==(mat_rank2(n,*x)==multiply(mat_rank2(n,*x),mat_rank2(n,*x)))
                fixed2+=(x==y); seen2.add(x); checks+=1
            x=(a,b); y=corank1_tau(*x)
            assert corank1_tau(*y)==x and is_inverse(mat_corank1(n,*x), mat_corank1(n,*y))
            assert (x==y)==(mat_corank1(n,*x)==multiply(mat_corank1(n,*x),mat_corank1(n,*x)))
            fixed1+=(x==y); seen1.add(x); checks+=1
    assert len(seen2) == (n-1)*comb(n,2)
    assert fixed2 == comb(n+1,3)
    assert (len(seen2)-fixed2)//2 == comb(n,3)
    assert len(seen1)==n*(n-1) and fixed1==2*(n-1)
    assert (len(seen1)-fixed1)//2==comb(n-1,2)

# The first fixed-idempotent obstruction at rank three of O_5.
all_keys = [f'{a}{b}|{i}{j}{k}' for a,b in combinations(range(1,5),2)
                                   for i,j,k in combinations(range(1,6),3)]
all_maps = {key:mat_rank3_n5(key) for key in all_keys}
assert len(all_maps)==60
idem = {code for code,f in all_maps.items() if multiply(f,f)==f}
assert len(idem)==21 and comb(7,5)==21
pairs = []
for row in (BASE/'certificate_rank3_n5.txt').read_text(encoding='utf-8').splitlines():
    if not row or row.startswith('#'): continue
    a,b = row.split(); pairs.append((a,b))
assert len(pairs)==20
moved = [c for p in pairs for c in p]
assert len(set(moved))==40 and all(c in all_maps for c in moved)
assert all(is_inverse(all_maps[a],all_maps[b]) for a,b in pairs)
fixed = set(all_maps)-set(moved)
assert len(fixed)==20 and fixed <= idem
assert len(idem-set(fixed))==1
assert idem-set(fixed)=={'12|124'}
print('VERIFY_OK', 'individual_extremal_checks=',checks,
      'rank_three_pairs=',len(pairs), 'fixed_idempotents=',len(fixed),
      'moved_idempotents=',len(idem-set(fixed)))
