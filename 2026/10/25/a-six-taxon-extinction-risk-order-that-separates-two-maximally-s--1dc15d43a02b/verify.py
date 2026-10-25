"""Exact finite checks for rooted six-tip extinction-risk shape theorem.
Run: python verify.py [certificate.json]
Uses only the Python standard library; the analytical proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import Counter
import json, sys

LEAF = ()

def key(t):
    return (0,) if t == LEAF else (1, size(t), repr(t))

def size(t):
    return 1 if t == LEAF else size(t[0]) + size(t[1])

def shape(a,b):
    return tuple(sorted((a,b),key=key))

def all_shapes(n, cache={}):
    if n==1: return (LEAF,)
    if n in cache: return cache[n]
    out = {}
    for k in range(1,n):
        for a in all_shapes(k):
            for b in all_shapes(n-k):
                t=shape(a,b)
                out[repr(t)] = t
    cache[n] = tuple(out.values())
    return cache[n]

def clades(t):
    """Descending clade sizes, omitting the root and all singleton leaves."""
    if t == LEAF: return []
    out=[]
    for child in t:
        if child != LEAF:
            out.append(size(child))
            out.extend(clades(child))
    return out

def depths(t,d=0):
    if t==LEAF: return [d]
    return depths(t[0],d+1)+depths(t[1],d+1)

# Coefficients of the six ranked clade polynomials in ascending order.
RANKED = [
    {2:1,3:1,4:1,5:1},
    {2:2,4:1,5:1},
    {2:2,3:1,5:1},
    {2:2,3:1,4:1},
    {2:2,3:2},
    {2:3,4:1},
]
GAPS = [
    {2:1,3:-1},
    {3:1,4:-1},
    {4:1,5:-1},
    {3:1,4:-1},
    {2:1,3:-2,4:1},
]

def poly_diff(a,b):
    return {k:a.get(k,0)-b.get(k,0) for k in set(a)|set(b) if a.get(k,0)!=b.get(k,0)}

shapes=all_shapes(6)
assert len(shapes)==6
found={}
for t in shapes:
    c=Counter(clades(t))
    assert sum(c.values())==4
    v={k:c[k] for k in c}
    assert tuple(sorted(v.items())) not in found
    found[tuple(sorted(v.items()))]=t
assert set(found)==set(tuple(sorted(v.items())) for v in RANKED)
for a,b,gap in zip(RANKED,RANKED[1:],GAPS):
    assert poly_diff(b,a)==gap

# F maximum for 4/5 tips and six-tip root configuration check.
assert len(all_shapes(4))==2 and len(all_shapes(5))==3
for n,winning in ((4,{2:2}),(5,{2:2,3:1})):
    assert any(dict(Counter(clades(t)))==winning for t in all_shapes(n))
    for q in (Q(1,7),Q(1,3),Q(1,2),Q(4,5)):
        score=lambda d:sum(v*q**k for k,v in d.items())
        assert all(score(winning)>score(dict(Counter(clades(t)))) for t in all_shapes(n) if dict(Counter(clades(t)))!=winning)

# The 5th and 6th polynomials are respectively 3+3 and 2+4 balanced.
E=found[tuple(sorted(RANKED[4].items()))]
F=found[tuple(sorted(RANKED[5].items()))]
assert sorted(depths(E))==sorted(depths(F))==[2,2,3,3,3,3]
assert poly_diff(RANKED[5],RANKED[4])=={2:1,3:-2,4:1}

# Canonical extinction outcomes for every leaf set; each shape is unlabeled,
# but its six leaves receive deterministic left-to-right indexes.
def clade_leaf_masks(t):
    cnt=[0]; masks=[]
    def rec(node):
        if node==LEAF:
            x=1<<cnt[0];cnt[0]+=1; masks.append(x);return x
        x=rec(node[0])|rec(node[1]);masks.append(x);return x
    rec(t)
    assert cnt[0]==6 and len(masks)==11 # 6 leaves + 5 internal vertices
    return masks[:-1] # exclude root: 10 unit edges

def score(t, extinct_mask):
    return sum(int((c&extinct_mask)==c) for c in clade_leaf_masks(t))

checks=0
for t in shapes:
    c=dict(Counter(clades(t)))
    for q,theta in product((Q(1,5),Q(1,3),Q(1,2),Q(4,5)),(Q(1,4),Q(3,5),Q(1,1))):
        independent=Q(0)
        for mask in range(64):
            k=mask.bit_count()
            independent += score(t,mask)*q**k*(1-q)**(6-k)
            checks += 1
        full=score(t,63);empty=score(t,0)
        shared=q*full+(1-q)*empty
        mixture=(1-theta)*independent+theta*shared
        eq_ind=6*q+sum(v*q**k for k,v in c.items())
        eq_excess=theta*(4*q-sum(v*q**k for k,v in c.items()))
        assert independent==eq_ind and full==10 and empty==0
        assert shared==10*q and mixture-independent==eq_excess
        checks+=4

# Independent full rational comparison for selected positions.
for q in (Q(1,10),Q(1,3),Q(1,2),Q(7,8),Q(99,100)):
    Fs=[sum(v*q**k for k,v in r.items()) for r in RANKED]
    assert all(y>x for x,y in zip(Fs,Fs[1:]))
    assert Fs[-1]-Fs[-2]==q*q*(1-q)*(1-q)
    checks+=6

out={
    'schema_version':1,
    'checks':'six rooted binary shapes, exact clade polynomials, adjacent difference identities, all 64 extinction states for each shape, exact conservation of 6-leaf Sackin depths, 4/5-tip first-size checks',
    'rooted_six_shapes':len(shapes),
    'rational_state_checks':checks,
    'q_values':['1/5','1/3','1/2','4/5'],
    'theta_values':['1/4','3/5','1'],
    'ordered_clade_polynomials':[
       {str(k):v for k,v in sorted(r.items())} for r in RANKED
    ],
    'status':'verified',
    'limits':'Exact finite rational checks corroborate but do not replace the symbolic all-q all-theta argument.'
}
blob=(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
if len(sys.argv)>1:
    with open(sys.argv[1],'wb') as f:f.write(blob)
else: sys.stdout.buffer.write(blob)
