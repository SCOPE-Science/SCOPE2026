#!/usr/bin/env python3
import itertools, json, math
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text())

def rank(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv: y^=piv[p]
            else: piv[p]=y; break
    return len(piv)

def dot(a,b): return (a&b).bit_count()&1

def comps(n,k,p=()):
    if k==1:
        yield p+(n,); return
    for x in range(n+1): yield from comps(n-x,k-1,p+(x,))

def expand(m): return [c for c,z in enumerate(m) for _ in range(z)]
def weights(m): return [sum(m[c] for c in range(8) if dot(u,c)) for u in range(1,8)]

def local_d(cols,G):
    W={tuple(dot(u,cols[j]) for j in G) for u in range(8)}
    z=[sum(w) for w in W if any(w)]
    return min(z) if z else 99

def avail(cols):
    for i in range(8):
        hs=[]
        O=[j for j in range(8) if j!=i]
        for s in (1,2):
            for H in itertools.combinations(O,s):
                if local_d(cols,(i,)+H)>=2: hs.append(frozenset(H))
        if not any(a.isdisjoint(b) for a,b in itertools.combinations(hs,2)): return False
    return True

def apply(A,x):
    y=0
    for i,r in enumerate(A):
        if dot(r,x): y|=1<<i
    return y

GL=[A for A in itertools.product(range(8),repeat=3) if rank(A)==3]
assert len(GL)==168

def tm(m,A):
    z=[0]*8
    for c,n in enumerate(m): z[apply(A,c)]+=n
    return tuple(z)

valid=[]
for m in comps(8,8):
    cols=expand(m)
    if rank(cols)!=3: continue
    w=weights(m)
    if min(w)<4: continue
    if avail(cols): valid.append(m)

assert len(valid)==28
assert all(m[0]==0 for m in valid)
V=set(valid)
orbits=[]
while V:
    m=min(V); O={tm(m,A) for A in GL}&set(valid)
    orbits.append(O); V-=O
assert sorted(map(len,orbits))==[7,21]

SUB=set()
for a,b in itertools.combinations(range(1,8),2):
    S=frozenset((0,a,b,a^b))
    if len(S)==4: SUB.add(S)
assert len(SUB)==7

def mm(cols): return tuple(cols.count(c) for c in range(8))
def supp(m,S): return sum(m[c] for c in range(8) if any(dot(u,c) for u in S))

for info in CERT["classification"]["classes"]:
    m=mm(info["columns"]); assert m in set(valid)
    wd=Counter([0]+weights(m))
    assert dict(sorted(wd.items()))=={int(k):v for k,v in info["weight_distribution"].items()}
    sp=Counter(supp(m,S) for S in SUB)
    assert dict(sorted(sp.items()))=={int(k):v for k,v in info["two_dim_support_distribution"].items()}
    assert [min(weights(m)),min(sp),supp(m,set(range(8)))]==info["generalized_hamming_weights"]
    st=sum(tm(m,A)==m for A in GL); assert st==info["gl_stabilizer_order"]
    internal=math.prod(math.factorial(x) for x in m)
    assert st*internal==info["permutation_automorphism_order"]

source=mm([1,1,2,2,4,5,6,7])
assert len({tm(source,A) for A in GL})==21

had=(1,1,1,1,1,1,1,1)
assert min(weights(had))==4 and not avail(expand(had))
print("VERIFY_OK")
