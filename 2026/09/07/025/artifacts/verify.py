import itertools
# Verified verifier: rebuild PG(2,4) from scratch, check regularity, recompute M(8,8) both sides, check comparison bounds, check degree-sequence lemma.
def f4_mul(a,b):
    if a==0 or b==0: return 0
    if a==1: return b
    if b==1: return a
    if a==2 and b==2: return 3
    if a==3 and b==3: return 2
    return 1
def f4_add(a,b): return a^b
def canon(v):
    for c in v:
        if c!=0:
            inv=[None,1,3,2][c]
            return tuple(f4_mul(x,inv) for x in v)
pts=[]; seen=set()
for x in range(4):
    for y in range(4):
        for z in range(4):
            if x==y==z==0: continue
            c=canon((x,y,z))
            if c not in seen: seen.add(c); pts.append(c)
assert len(pts)==21
pidx={p:i for i,p in enumerate(pts)}
lines=list(pts)
def dot(n,p):
    s=0
    for a,b in zip(n,p): s=f4_add(s,f4_mul(a,b))
    return s
def pop(m): return bin(m).count('1')
linemask=[]; ptmask=[]
for n in lines:
    m=0
    for p,i in pidx.items():
        if dot(n,p)==0: m|=(1<<i)
    linemask.append(m)
    assert pop(m)==5
for i,p in enumerate(pts):
    m=0
    for j,n in enumerate(lines):
        if dot(n,p)==0: m|=(1<<j)
    ptmask.append(m)
    assert pop(m)==5
k=8; best=0; cnt=0; ex=None
for P in itertools.combinations(range(21),k):
    pm=0
    for i in P: pm|=(1<<i)
    s=sum(sorted([pop(pm&lm) for lm in linemask],reverse=True)[:k])
    if s>best: best=s; cnt=1; ex=P
    elif s==best: cnt+=1
assert best==24 and cnt==7560, (best,cnt)
best2=0; cnt2=0
for L in itertools.combinations(range(21),k):
    lm=0
    for j in L: lm|=(1<<j)
    s=sum(sorted([pop(lm&pm) for pm in ptmask],reverse=True)[:k])
    if s>best2: best2=s; cnt2=1
    elif s==best2: cnt2+=1
assert best2==24 and cnt2==7560, (best2,cnt2)
# comparison bounds: EML d|P||L|/N + lam*sqrt(|P||L|), d=5,N=21,lam=2; KST (n+sqrt(n^2+4nm(m-1)))/2
import math
eml=5*64/21+2*8; kst=(8+math.sqrt(64+4*8*8*7))/2
assert abs(eml-31.2380952381)<1e-6
assert abs(kst-25.5406597569)<1e-6
# degree-sequence lemma
sols=[]
def rec(rem,parts,lo,cur):
    if parts==1:
        if rem>=lo: sols.append(tuple(cur+[rem]))
        return
    for v in range(lo,rem+1):
        if rem-v<0: break
        rec(rem-v,parts-1,v,cur+[v])
rec(25,8,0,[])
filt=sorted([s for s in sols if 79<=sum(v*v for v in s)<=81])
assert filt==[(2,3,3,3,3,3,4,4),(3,3,3,3,3,3,3,4)], filt
# pair-disjointness identity: two pts determine unique line -> sum C(r_l,2)<=C(8,2)
# exhibit 24 configuration
P=(0,1,2,5,6,13,16,18); L=(0,1,4,5,6,10,17,20)
pm=sum(1<<i for i in P)
assert sum(pop(pm&linemask[j]) for j in L)==24
assert sorted(pop(pm&linemask[j]) for j in L)==[3]*8
print("ALL CHECKS PASS: M(8,8)=24, counts 7560/7560, lemma ok, example ok")
