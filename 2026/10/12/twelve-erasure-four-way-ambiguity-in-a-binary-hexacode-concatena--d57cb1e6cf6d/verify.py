"""Exact erasure-ambiguity spectrum of an 18-symbol binary hexacode concatenation.
Run: python3 verify.py. Uses only Python's standard library.
"""
from itertools import combinations, product
from collections import Counter
from math import comb

# GF(4) = GF(2)[w]/(w*w+w+1), encoded 0, 1, w, w+1.
def mul(a,b):
    ans=0
    for i in range(2):
        if (b>>i)&1: ans ^= a<<i
    if ans & 8: ans ^= 0b1100
    if ans & 4: ans ^= 0b111
    return ans

def rank4(rows):
    rows=[list(r) for r in rows]
    h=len(rows); w=len(rows[0]) if rows else 0
    rank=0
    for c in range(w):
        p=next((i for i in range(rank,h) if rows[i][c]),None)
        if p is None: continue
        rows[rank],rows[p]=rows[p],rows[rank]
        piv=rows[rank][c]
        for i in range(rank+1,h):
            if rows[i][c]:
                scale=mul(rows[i][c],mul(piv,piv)) # inverse of nonzero pivot is its square
                for j in range(c,w): rows[i][j] ^= mul(scale,rows[rank][j])
        rank+=1
        if rank==h:break
    return rank

M=((1,2,2),(2,1,2),(2,2,1))
H=[tuple(1 if i==j else 0 for j in range(3)) + M[i] for i in range(3)]
# Every 3 columns are independent: a [6,3,4]_4 MDS code.
assert all(rank4([[H[i][j] for j in J] for i in range(3)])==3
           for J in combinations(range(6),3))
# Hermitian self-orthogonality of the row space.
for u in H:
    for v in H:
        s=0
        for a,b in zip(u,v):s ^= mul(a,mul(b,b))
        assert s==0

# H = [I | M]; C consists of (M*y,y), y in GF(4)^3.
# Inner [3,2,2]_2 image map uses even-weight triples.
INNER=(0b000,0b110,0b101,0b011)
words=[]
for y in product(range(4),repeat=3):
    x=tuple(mul(M[i][0],y[0]) ^ mul(M[i][1],y[1]) ^ mul(M[i][2],y[2]) for i in range(3))
    qword=x+y
    for r in H:
        c=0
        for a,b in zip(r,qword):c ^=mul(a,b)
        assert c==0
    words.append(sum(INNER[v]<<(3*j) for j,v in enumerate(qword)))
assert len(set(words))==64
assert all(words[a]^words[b]==words[a^b] for a in range(64) for b in range(64))
assert Counter(w.bit_count() for w in words)=={0:1,8:45,12:18}

# All binary two-dimensional subcodes: the nonzero vectors are {a,b,a+b}.
planes={frozenset((a,b,a^b)) for a,b in combinations(range(1,64),2)}
assert len(planes)==651
plane_wts=Counter(); minimal_supports={}
profiles=Counter()
for P in planes:
    support=0
    for a in P:support |=words[a]
    n=support.bit_count()
    plane_wts[n]+=1
    if n==12:
        assert support not in minimal_supports
        minimal_supports[support]=P
        profile=tuple(sorted((support>>(3*i)&7).bit_count() for i in range(6)
                             if (support>>(3*i)&7)))
        profiles[profile]+=1
assert plane_wts=={12:240,14:270,16:135,18:6}
assert profiles=={(3,3,3,3):15,(2,2,2,3,3):180,(2,2,2,2,2,2):45}
assert len(minimal_supports)==240

# Independently reconstruct a binary generator and compute the un-erased rank.
G=[words[1<<i] for i in range(6)]
col=[sum(((g>>j)&1)<<i for i,g in enumerate(G)) for j in range(18)]
def rank2(v):
    basis=[0]*6
    n=0
    for x in v:
        while x:
            i=x.bit_length()-1
            if basis[i]:x ^=basis[i]
            else:
                basis[i]=x
                n+=1
                break
    return n

hist=Counter();by_dim_support=Counter()
allmask=(1<<18)-1
for idx in combinations(range(18),12):
    E=sum(1<<i for i in idx)
    missing=allmask^E
    nullity=6-rank2(col[i] for i in range(18) if missing>>i&1)
    hist[nullity]+=1
    # Independent decoding dimension from full codeword list.
    q=sum((w & missing)==0 for w in words)
    assert q==(1<<nullity)
    if nullity==2:
        assert E in minimal_supports
assert hist=={0:9576,1:8748,2:240}
assert sum(hist.values())==comb(18,12)==18564
# Double count all nonzero words supported in 12 positions.
incidences=45*comb(10,4)+18
assert incidences==hist[1]+3*hist[2]==9468
# The three 12-support types count as 15 + 180 + 45.
assert (15*3+60*9+45*3)//3==240
print('weight_distribution',dict(Counter(w.bit_count() for w in words)))
print('minimal_two_space_profiles',dict(profiles))
print('twelve_erasure_nullity',dict(sorted(hist.items())))
print('VERIFY_OK')
