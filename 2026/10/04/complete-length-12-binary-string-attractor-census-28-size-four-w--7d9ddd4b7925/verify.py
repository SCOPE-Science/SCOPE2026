from itertools import product, combinations
from collections import Counter

EXPECTED_DIST={1:2,2:1332,3:2734,4:28}
EXPECTED_REPS=['000100101011','000100101110','000100110101','000100110111','000101100111','000110100111','001011110100','010011000101','011110100001']
EXPECTED_ORBIT_SIZES=[4,4,4,2,4,2,2,4,2]

def masks(n,r):
    for c in combinations(range(n),r):
        m=0
        for i in c:m|=1<<i
        yield m

def gamma_a(w,limit=4):
    n=len(w); occ={}
    for i in range(n):
        m=0
        for j in range(i,n):
            m|=1<<j
            occ.setdefault(w[i:j+1],[]).append(m)
    for r in range(1,min(limit,n)+1):
        for S in masks(n,r):
            if all(any(S & m for m in ms) for ms in occ.values()):
                return r
    return limit+1

def gamma_b(w,limit=4):
    n=len(w)
    universe={w[i:j] for i in range(n) for j in range(i+1,n+1)}
    for r in range(1,min(limit,n)+1):
        for P in combinations(range(n),r):
            hit=set()
            for i in range(n):
                for j in range(i+1,n+1):
                    if any(i<=p<j for p in P): hit.add(w[i:j])
            if hit==universe:return r
    return limit+1

def complement(w): return ''.join('1' if c=='0' else '0' for c in w)
def orbit(w): return {w,w[::-1],complement(w),complement(w)[::-1]}
def canon(w): return min(orbit(w))

# Direct-definition engine A proves the first occurrence and the entire length-12 census.
for n in range(1,12):
    assert max(gamma_a(''.join(x)) for x in product('01',repeat=n))<=3
cnt=Counter(); ext=[]
for x in product('01',repeat=12):
    w=''.join(x); g=gamma_a(w); cnt[g]+=1
    if g==4: ext.append(w)
assert dict(sorted(cnt.items()))==EXPECTED_DIST
assert len(ext)==28

# Independent engine B encodes an attractor by the union of all substrings touched by its positions.
cnt_b=Counter(gamma_b(''.join(x)) for x in product('01',repeat=12))
assert dict(sorted(cnt_b.items()))==EXPECTED_DIST

classes={}
for w in ext: classes.setdefault(canon(w),set()).add(w)
assert sorted(classes)==EXPECTED_REPS
assert [len(classes[r]) for r in EXPECTED_REPS]==EXPECTED_ORBIT_SIZES
for r in EXPECTED_REPS:
    assert classes[r]==orbit(r)
print('distribution',dict(sorted(cnt.items())))
print('extremizers',len(ext))
print('orbit_representatives',','.join(EXPECTED_REPS))
print('orbit_sizes',EXPECTED_ORBIT_SIZES)
print('VERIFY_OK')
