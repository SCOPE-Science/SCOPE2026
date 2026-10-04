#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter

PAIR_CACHE={n:list(combinations(range(n),2)) for n in range(1,7)}

def outmasks(n,bits):
    out=[0]*n
    for k,(i,j) in enumerate(PAIR_CACHE[n]):
        if (bits>>k)&1:
            out[i]|=1<<j
        else:
            out[j]|=1<<i
    return out

def covers(out,y,x,S):
    return ((out[y]>>x)&1)==1 and (out[x]&S)&~(out[y]&S)==0

def uc_cover(out,S):
    U=0
    xs=S
    while xs:
        q=xs&-xs; x=q.bit_length()-1; xs^=q
        ys=S&~q; covered=False
        while ys:
            r=ys&-ys; y=r.bit_length()-1; ys^=r
            if covers(out,y,x,S):
                covered=True; break
        if not covered:
            U|=q
    return U

def uc_twostep(out,S):
    U=0
    xs=S
    while xs:
        q=xs&-xs; x=q.bit_length()-1; xs^=q
        reach=q | (out[x]&S)
        ys=out[x]&S
        while ys:
            r=ys&-ys; y=r.bit_length()-1; ys^=r
            reach |= out[y]&S
        if reach==S:
            U|=q
    return U

def ucinf_cover(out,n):
    S=(1<<n)-1
    while True:
        T=uc_cover(out,S)
        if T==S:return S
        S=T

def ucinf_twostep(out,n):
    S=(1<<n)-1
    while True:
        T=uc_twostep(out,S)
        if T==S:return S
        S=T

def is_covering_set(out,B,n):
    # Internal stability: all members are uncovered in the induced tournament.
    if uc_cover(out,B)!=B:return False
    full=(1<<n)-1
    rem=full^B
    while rem:
        q=rem&-rem; rem^=q
        # External stability: the added outsider is covered in B union {x}.
        if uc_cover(out,B|q)&q:
            return False
    return True

def is_externally_stable(out,B,n):
    full=(1<<n)-1
    rem=full^B
    while rem:
        q=rem&-rem; rem^=q
        if uc_cover(out,B|q)&q:return False
    return True

def mc_full(out,n):
    stable=[B for B in range(1,1<<n) if is_covering_set(out,B,n)]
    mins=[B for B in stable if not any(C!=B and (C&B)==C for C in stable)]
    assert len(mins)==1
    return mins[0]

def mc_external(out,n):
    # In tournaments, Dutta/Laslier's standard theorem says the unique
    # inclusion-minimal externally stable set is already internally stable.
    stable=[B for B in range(1,1<<n) if is_externally_stable(out,B,n)]
    mins=[B for B in stable if not any(C!=B and (C&B)==C for C in stable)]
    assert len(mins)==1
    B=mins[0]
    assert uc_cover(out,B)==B
    return B

def permute_bits(n,bits,p):
    idx={e:k for k,e in enumerate(PAIR_CACHE[n])}
    out=0
    for k,(i,j) in enumerate(PAIR_CACHE[n]):
        w=i if (bits>>k)&1 else j
        l=j if w==i else i
        W,L=p[w],p[l]
        a,b=sorted((W,L))
        if W==a:
            out |= 1<<idx[(a,b)]
    return out

def canonical6(bits):
    return min(permute_bits(6,bits,p) for p in permutations(range(6)))

def bitset(S,n):
    return frozenset(i for i in range(n) if (S>>i)&1)

hist={}; diff={}; strict=[]
for n in range(1,7):
    H=Counter(); d=0
    for bits in range(1<<(n*(n-1)//2)):
        out=outmasks(n,bits)
        U1=ucinf_cover(out,n)
        U2=ucinf_twostep(out,n)
        assert U1==U2
        M1=mc_full(out,n)
        M2=mc_external(out,n)
        assert M1==M2
        assert (M1 & ~U1)==0
        H[(M1.bit_count(),U1.bit_count(),M1==U1)] += 1
        if M1!=U1:
            d+=1
            if n==6: strict.append(bits)
    hist[n]=H; diff[n]=d

assert diff=={1:0,2:0,3:0,4:0,5:0,6:240}
assert hist[5]==Counter({(3,3,True):640,(1,1,True):320,(5,5,True):64})
assert hist[6]==Counter({
    (3,3,True):20240,
    (1,1,True):6144,
    (5,5,True):4704,
    (6,6,True):1440,
    (3,6,False):240,
})
classes=Counter(canonical6(bits) for bits in strict)
assert classes==Counter({1332:240})

# Canonical representative and its symmetry/structure.
bits=1332; out=outmasks(6,bits)
M=mc_full(out,6); U=ucinf_cover(out,6); UC=uc_cover(out,(1<<6)-1)
assert bitset(M,6)==frozenset({1,4,5})
assert bitset(U,6)==frozenset(range(6))
assert UC==(1<<6)-1
assert tuple(sorted(x.bit_count() for x in out))==(2,2,2,3,3,3)
assert tuple(i for i in range(6) if out[i].bit_count()==3)==(1,4,5)
assert bitset(M,6)==frozenset(i for i in range(6) if out[i].bit_count()==3)

autos=[p for p in permutations(range(6)) if permute_bits(6,bits,p)==bits]
assert len(autos)==3
assert {p[0] for p in autos}=={0,2,3}
assert {p[1] for p in autos}=={1,4,5}

# Each outside vertex is covered by exactly one MC member when adjoined.
coverers={}
for x in (0,2,3):
    S=M | (1<<x)
    cs=[y for y in (1,4,5) if covers(out,y,x,S)]
    coverers[x]=tuple(cs)
assert coverers=={0:(1,),2:(5,),3:(4,)}

print('VERIFY_OK')
for n in range(1,7):
    print('n',n,'total',1<<(n*(n-1)//2),'diff',diff[n],'hist',dict(hist[n]))
print('n6_probability','240/32768 = 15/2048')
print('n6_classes',dict(classes))
print('canonical_bits',1332)
print('canonical_MC',sorted(bitset(M,6)))
print('canonical_UCinf',sorted(bitset(U,6)))
print('canonical_UC',sorted(bitset(UC,6)))
print('outdegrees',[x.bit_count() for x in out])
print('automorphism_group_order',len(autos))
print('external_coverers',coverers)
