#!/usr/bin/env python3
from pathlib import Path
import json,itertools,collections

ROOT=Path(__file__).resolve().parent.parent
C=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
MOD=0b1011

def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a&8:a^=MOD
    return r&7

def vec(x,y):return x|(y<<3)
def dot(a,b):return (a&b).bit_count()&1

E={}
for lam in range(8):
    E[lam]={vec(x,mul(lam,x)) for x in range(8)}
E[8]={vec(0,x) for x in range(8)}

def orth(S):
    return {v for v in range(64) if all(dot(v,x)==0 for x in S)}
ED={k:orth(S) for k,S in E.items()}
assert all(len(S)==8 for S in ED.values())

def subspaces(n,d):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv) for c in range(p+1,n) if c not in P]
        for vals in itertools.product((0,1),repeat=len(free)):
            B=[1<<p for p in piv]
            for (i,c),v in zip(free,vals):
                if v:B[i]|=1<<c
            yield B

SUB={d:list(subspaces(7,d)) for d in range(1,8)}
assert {str(d):len(SUB[d]) for d in SUB}==C["subspace_counts"]

expected={int(d):{int(k):v for k,v in spec.items()} for d,spec in C["support_spectra"].items()}
gh_expected=tuple(C["generalized_hamming_weights"])

def rows_for(pair,a):
    union=E[pair[0]]|E[pair[1]]
    f=[1 if x and x in union else 0 for x in range(64)]
    coords=list(range(1,64))+[x for x in range(1,64) if dot(a,x)]
    assert len(coords)==95
    rows=[]
    for ri in range(7):
        z=0
        for j,x in enumerate(coords):
            b=f[x] if ri==0 else ((x>>(ri-1))&1)
            if b:z|=1<<j
        rows.append(z)
    return rows

classes=set()
instances=0
for pair in itertools.combinations(range(9),2):
    U=ED[pair[0]]|ED[pair[1]]
    outside=[a for a in range(1,64) if a not in U]
    assert len(outside)==49
    for a in outside:
        rows=rows_for(pair,a)
        words=[0]*128
        for u in range(128):
            z=0
            for i in range(7):
                if (u>>i)&1:z^=rows[i]
            words[u]=z
        specs={}
        gh=[]
        for d in range(1,8):
            ctr=collections.Counter()
            for B in SUB[d]:
                z=0
                for u in B:z|=words[u]
                ctr[z.bit_count()]+=1
            specs[d]=dict(sorted(ctr.items()))
            gh.append(min(ctr))
        assert tuple(gh)==gh_expected
        assert specs==expected
        key=(tuple(gh),tuple((d,tuple(specs[d].items())) for d in range(1,8)))
        classes.add(key)
        instances+=1

assert instances==C["instances_checked"]==1764
assert len(classes)==1
assert C["subcode_instances_checked"]==instances*sum(len(SUB[d]) for d in SUB)
assert expected[1]=={22:1,42:12,46:36,48:62,54:3,58:12,64:1}
print("VERIFY_OK")
