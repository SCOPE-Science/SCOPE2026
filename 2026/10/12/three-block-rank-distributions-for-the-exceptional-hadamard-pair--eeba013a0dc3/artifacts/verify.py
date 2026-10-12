#!/usr/bin/env python3
import itertools, collections, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def rank_bits(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y^=piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

# ---------- H^{1,1,1}: local function spaces from the source ----------
# basis: eps,a,b,c,d,e,ad,bd
E,A,B,C,D,E2,AD,BD=[1<<i for i in range(8)]
VA=[
    [E,A,B,D],
    [A,D,E^E2,B^AD],
    [A,D,B,E^C],
    [A,D,B,E^C^E2^BD],
]
singleA=collections.Counter(rank_bits(v) for v in VA)
pairA=collections.Counter()
triA=collections.Counter()
for I in itertools.combinations(range(4),2):
    pairA[rank_bits(sum((VA[i] for i in I),[]))]+=1
for I in itertools.combinations(range(4),3):
    triA[rank_bits(sum((VA[i] for i in I),[]))]+=1
assert singleA=={4:4}
assert pairA=={5:3,6:3}
assert triA=={6:1,7:3}
assert rank_bits(sum(VA,[]))==8

# ---------- Hbar^{2,0,0}: direct Z8/Carlet reconstruction ----------
def phi3(u):
    u0=(u>>0)&1
    u1=(u>>1)&1
    u2=(u>>2)&1
    out=[]
    for h0,h1 in ((0,0),(0,1),(1,0),(1,1)):
        out.append(u2 ^ (u0&h0) ^ (u1&h1))
    return out

code=[]
for x1 in range(8):
    for x2 in range(8):
        bits=[]
        for j in range(8):
            bits.extend(phi3((x1+x2*j)%8))
        z=0
        for i,b in enumerate(bits):
            if b:z|=1<<i
        code.append(z)
assert len(set(code))==64
assert collections.Counter(x.bit_count() for x in code)=={0:1,16:62,32:1}
assert rank_bits(code)==8

# Coordinates are (j,h0,h1), with Gray order used above.
blocks={}
idx=0
for j in range(8):
    for h0,h1 in ((0,0),(0,1),(1,0),(1,1)):
        lab=(j%2,h0^h1)
        blocks.setdefault(lab,[]).append(idx)
        idx+=1
assert len(blocks)==4 and all(len(v)==8 for v in blocks.values())

labels=sorted(blocks)
def puncture_rank(coord_ids):
    rows=[]
    for word in code:
        z=0
        for k,c in enumerate(coord_ids):
            if (word>>c)&1:z|=1<<k
        rows.append(z)
    return rank_bits(rows)

singleB=collections.Counter()
pairB=collections.Counter()
triB=collections.Counter()
for I in itertools.combinations(range(4),1):
    coords=sum((blocks[labels[i]] for i in I),[])
    singleB[puncture_rank(coords)]+=1
for I in itertools.combinations(range(4),2):
    coords=sum((blocks[labels[i]] for i in I),[])
    pairB[puncture_rank(coords)]+=1
for I in itertools.combinations(range(4),3):
    coords=sum((blocks[labels[i]] for i in I),[])
    triB[puncture_rank(coords)]+=1
assert singleB=={4:4}
assert pairB=={5:2,7:4}
assert triB=={8:4}
assert puncture_rank(list(range(32)))==8

# ---------- Recurrences and closed forms ----------
def pA(m):
    return {5:5*4**m-2**(m+1), 6:3*4**m}
def pB(m):
    return {5:4*4**m-2**(m+1), 7:4**(m+1)}
def tA(m):
    return {6:(14*8**m-15*4**m+4*2**m)//3,
            7:6*8**m-3*4**m}
def tB(m):
    return {6:(8*8**m-12*4**m+4*2**m)//3,
            8:8*8**m-4*4**m}

PA=collections.Counter({5:3,6:3})
PB=collections.Counter({5:2,7:4})
TA=collections.Counter({6:1,7:3})
TB=collections.Counter({8:4})
b=4
for m in range(11):
    assert dict(PA)=={k:v for k,v in pA(m).items() if v}
    assert dict(PB)=={k:v for k,v in pB(m).items() if v}
    assert dict(TA)=={k:v for k,v in tA(m).items() if v}
    assert dict(TB)=={k:v for k,v in tB(m).items() if v}
    assert sum(PA.values())==math.comb(b,2)
    assert sum(PB.values())==math.comb(b,2)
    assert sum(TA.values())==math.comb(b,3)
    assert sum(TB.values())==math.comb(b,3)
    if m==10:
        break
    PA2=collections.Counter({5:b})
    PB2=collections.Counter({5:b})
    for j,n in PA.items(): PA2[j]+=4*n
    for j,n in PB.items(): PB2[j]+=4*n
    TA2=collections.Counter()
    TB2=collections.Counter()
    for j,n in TA.items(): TA2[j]+=8*n
    for j,n in TB.items(): TB2[j]+=8*n
    for j,n in PA.items(): TA2[j+1]+=4*n
    for j,n in PB.items(): TB2[j+1]+=4*n
    PA,PB,TA,TB=PA2,PB2,TA2,TB2
    b*=2

# certificate base-data consistency
assert CERT["base_t5"]["A_pairs"]=={"5":3,"6":3}
assert CERT["base_t5"]["A_triples"]=={"6":1,"7":3}
assert CERT["base_t5"]["B_pairs"]=={"5":2,"7":4}
assert CERT["base_t5"]["B_triples"]=={"8":4}

print("VERIFY_OK")
