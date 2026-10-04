#!/usr/bin/env python3
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter

# Exact arithmetic in Q(zeta_8)=Q[z]/(z^4+1).
ZERO=(Q(0),Q(0),Q(0),Q(0)); ONE=(Q(1),Q(0),Q(0),Q(0)); Z=(Q(0),Q(1),Q(0),Q(0))

def sub(a,b): return tuple(a[i]-b[i] for i in range(4))
def mul(a,b):
    c=[Q(0)]*7
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: c[i+j]+=x*y
    for d in range(6,3,-1):
        if c[d]: c[d-4]-=c[d]
    return tuple(c[:4])

def _inverse(a):
    cols=[]; p=ONE
    for _ in range(4): cols.append(mul(a,p)); p=mul(p,Z)
    A=[[cols[c][r] for c in range(4)]+[Q(1 if r==0 else 0)] for r in range(4)]
    for c in range(4):
        p=next(r for r in range(c,4) if A[r][c])
        A[c],A[p]=A[p],A[c]
        q=A[c][c]; A[c]=[x/q for x in A[c]]
        for r in range(4):
            if r!=c and A[r][c]:
                q=A[r][c]; A[r]=[A[r][j]-q*A[c][j] for j in range(5)]
    out=tuple(A[r][4] for r in range(4))
    assert mul(a,out)==ONE
    return out

@lru_cache(None)
def inv(a): return _inverse(a)

POW=[ONE]
for _ in range(7): POW.append(mul(POW[-1],Z))
assert mul(POW[4],ONE)==(-ONE[0],ZERO[1],ZERO[2],ZERO[3])

def bitset(mask): return [i for i in range(8) if (mask>>i)&1]
def rank(rows,cols):
    A=[[POW[(r*c)%8] for c in cols] for r in rows]
    m=len(A); n=len(cols); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]!=ZERO),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        pinv=inv(A[rr][c])
        for i in range(rr+1,m):
            if A[i][c]!=ZERO:
                fac=mul(A[i][c],pinv)
                for j in range(c,n): A[i][j]=sub(A[i][j],mul(fac,A[rr][j]))
        rr+=1
        if rr==m: break
    return rr

RANK={}
for rm in range(256):
    rows=bitset(rm)
    for cm in range(256): RANK[(rm,cm)]=rank(rows,bitset(cm))
assert RANK[(255,255)]==8

def realizable(S,T):
    # Variables are the coefficients on exact time support S. Rows in ZT force
    # Fourier coefficients outside T to vanish.
    ZT=(~T)&255
    r=RANK[(ZT,S)]
    s=S.bit_count()
    if r>=s: return False
    # No input coordinate functional may vanish on the kernel.
    for j in bitset(S):
        if RANK[(ZT,S & ~(1<<j))] != r: return False
    # No desired Fourier coordinate functional may vanish on the kernel.
    for t in bitset(T):
        if RANK[(ZT | (1<<t),S)] != r+1: return False
    return True

INC=[[0]*9 for _ in range(9)]
REAL=[]
for S in range(1,256):
    for T in range(1,256):
        if realizable(S,T):
            INC[S.bit_count()][T.bit_count()]+=1
            REAL.append((S,T))
EXPECTED_INC=[
[0,0,0,0,0,0,0,8],
[0,0,0,8,0,32,128,28],
[0,0,0,32,0,1056,384,56],
[0,8,32,148,2176,1736,544,70],
[0,0,0,2176,2816,1536,448,56],
[0,32,1056,1736,1536,784,224,28],
[0,128,384,544,448,224,64,8],
[8,28,56,70,56,28,8,1],
]
assert [INC[k][1:] for k in range(1,9)]==EXPECTED_INC
assert len(REAL)==20929
assert all(INC[k][l]==INC[l][k] for k in range(1,9) for l in range(1,9))

UNITS=(1,3,5,7)
def shift(mask,a):
    out=0
    for x in bitset(mask): out |= 1<<((x+a)%8)
    return out
def dil(mask,u):
    out=0
    for x in bitset(mask): out |= 1<<((u*x)%8)
    return out
def affine(pair,a,b,u):
    S,T=pair
    # u^{-1}=u for every unit modulo 8.
    return shift(dil(S,u),a), shift(dil(T,u),b)
def negate(mask):
    out=0
    for x in bitset(mask): out |= 1<<((-x)%8)
    return out
def fourier_swap(pair):
    S,T=pair
    return T,negate(S)

REALSET=set(REAL)
seen=set(); AFF=[]
for p in REAL:
    if p in seen: continue
    orb={affine(p,a,b,u) for a in range(8) for b in range(8) for u in UNITS}
    assert orb <= REALSET
    seen |= orb; AFF.append(orb)
assert len(seen)==20929 and len(AFF)==205
assert Counter(map(len,AFF))==Counter({128:72,256:34,64:30,8:22,16:19,32:18,4:7,2:2,1:1})

seen=set(); EXT=[]
for p in REAL:
    if p in seen: continue
    orb=set()
    for q in (p,fourier_swap(p)):
        orb.update(affine(q,a,b,u) for a in range(8) for b in range(8) for u in UNITS)
    assert orb <= REALSET
    seen |= orb; EXT.append(orb)
assert len(seen)==20929 and len(EXT)==108
assert Counter(map(len,EXT))==Counter({256:34,512:17,128:17,64:13,16:12,32:9,8:3,4:2,1:1})

print('RANK_TABLE',len(RANK))
print('REALIZABLE_SUPPORT_PAIRS',len(REAL))
print('INCIDENCE_MATRIX')
for row in EXPECTED_INC: print(*row)
print('AFFINE_ORBITS',len(AFF),dict(sorted(Counter(map(len,AFF)).items())))
print('FOURIER_EXTENDED_ORBITS',len(EXT),dict(sorted(Counter(map(len,EXT)).items())))
print('VERIFY_OK')
