#!/usr/bin/env python3
"""Exact independent coset and support-count verification for length-12 binary codes."""
from collections import Counter
from itertools import permutations
from hashlib import sha256

N = 6
COLS = (1,2,4,3,5,6)
H = [sum(((c>>j)&1)<<i for i,c in enumerate(COLS)) for j in range(3)]
U = frozenset(v for v in range(1<<N) if all((v&row).bit_count()%2 == 0 for row in H))
assert len(U)==8 and Counter(v.bit_count() for v in U)=={0:1,3:4,4:3}

def permword(v, p):
    return sum(((v>>i)&1)<<p[i] for i in range(N))

def doubled(core):
    return frozenset(v|(v<<6) for v in core)

def canonical_cosets(core):
    d = doubled(core)
    seen = set()
    for x in range(4096):
        if x in seen: continue
        coset = frozenset(x^y for y in d)
        seen.update(coset)
        yield (min(coset),coset)
    assert len(seen)==4096

all_cores={frozenset(permword(v,p) for v in U) for p in permutations(range(N))}
assert len(all_cores)==30
DU={w for w in range(64) if all((w&v).bit_count()%2==0 for v in U)}
assert Counter(w.bit_count() for w in DU)==Counter({0:1,3:4,4:3})
dual_triples={w for w in DU if w.bit_count()==3}
assert len(dual_triples)==4

# Independent symbolic classification by pair differences t=a xor b.
def category(x):
    a=x&63;b=x>>6;t=a^b
    q=t.bit_count()
    if q==6:return 6
    if q==5:return 5
    if q==3 and ((63^t) in dual_triples):
        I=63^t
        if (a&I).bit_count()%2:return 5   # parity of U|I is even
    return 0

hist=Counter(); hist_ref=None; code_sets=set(); examples={}
for core in sorted(all_cores, key=lambda v:tuple(sorted(v))):
    d=doubled(core)
    spec=Counter()
    for rep,coset in canonical_cosets(core):
        if rep==0: continue
        mind=min(y.bit_count() for y in coset)
        if core==U:
            hist[mind]+=1
            assert (category(rep)!=0)==(mind>=5), (rep,mind,category(rep))
        if mind<5:continue
        words=d|coset
        assert len(words)==16
        weight=tuple(sorted(Counter(y.bit_count() for y in words).items()))
        spec[weight]+=1
        code_sets.add(tuple(sorted(words)))
        examples.setdefault(weight,tuple(sorted(words)))
    assert sum(spec.values())==72
    if hist_ref is None: hist_ref=spec
    else: assert spec==hist_ref

assert hist=={1:12,2:66,3:180,4:181,5:64,6:8}
assert len(code_sets)==2160
expected={
 tuple(sorted([(0,1),(5,4),(6,4),(7,4),(8,3)])):48,
 tuple(sorted([(0,1),(5,6),(6,4),(8,3),(9,2)])):16,
 tuple(sorted([(0,1),(6,12),(8,3)])):8,
}
assert hist_ref==expected,(hist_ref,expected)
assert sum(m for w,m in hist_ref.items() if min(y for y,n in w if y>0)==6)==8
assert sum(1 for c in code_sets if min(z.bit_count() for z in c if z)!=6)==1920

# Verify punctured U covering radius 1 for each of the six 5-coordinate sets.
for j in range(6):
    mask=63^(1<<j)
    projections={v&mask for v in U}
    assert len(projections)==8
    assert all(min(((a^v)&mask).bit_count() for v in projections)<=1 for a in range(64))

# Check codimension-one projections on any four coordinates and two-coordinate surjections.
for I in range(64):
    if I.bit_count()==4:
        assert len({v&I for v in U})==8
    if I.bit_count()==2:
        assert len({v&I for v in U})==4

# Distinct U are uniquely C intersect diagonal, confirming distinctness after multiplying by 30.
for c in code_sets:
    kernel={w&63 for w in c if (w&63)==(w>>6)}
    assert frozenset(kernel) in all_cores and len(kernel)==8

record=';'.join(','.join(str(a) for a in c) for c in sorted(code_sets))
print('DIAGONAL_D5_VERIFY_OK')
print('core',','.join(map(str,sorted(U))))
print('dual_weight3_supports',','.join(str(v) for v in sorted(dual_triples)))
print('coset_min_spectrum',dict(sorted(hist.items())))
print('per_core_spectra',[(dict(w),count) for w,count in sorted(hist_ref.items())])
print('total_codes',len(code_sets),'d6',240,'d5',1920)
print('all_code_list_sha256',sha256(record.encode('ascii')).hexdigest())
