#!/usr/bin/env python3
import itertools

MOD={2:0b111,3:0b1011,4:0b10011}

def mul(a,b,M):
    r=0; mod=MOD[M]
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a&(1<<M): a^=mod
    return r&((1<<M)-1)

def power(a,n,M):
    r=1
    while n:
        if n&1: r=mul(r,a,M)
        a=mul(a,a,M); n//=2
    return r

def inverses(M):
    q=1<<M; inv=[0]*q
    for a in range(1,q):
        inv[a]=power(a,q-2,M)
        assert mul(a,inv[a],M)==1
    return inv

def rank_bits(xs):
    piv={}
    for x in xs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv: y^=piv[p]
            else: piv[p]=y; break
    return len(piv)

def frames(M,s):
    for tup in itertools.permutations(range(1,1<<M),s):
        if rank_bits(tup)==s: yield tup

def image(v,imgs):
    z=0
    for j,b in enumerate(imgs):
        if (v>>j)&1: z^=b
    return z

def syndrome(c,cols):
    z=0
    for i,h in enumerate(cols):
        if (c>>i)&1: z^=h
    return z

def formula(M,s):
    z=1<<M
    for j in range(s): z*=((1<<M)-(1<<j))
    return z

def check(cols,s,M):
    n=len(cols)
    assert rank_bits(cols)==s
    assert all(cols) and len(set(cols))==n
    inv=inverses(M)
    base=[syndrome(c,cols)==0 for c in range(1<<n)]
    reps=0
    for imgs in frames(M,s):
        b=[image(h,imgs) for h in cols]
        assert all(b) and len(set(b))==n
        for beta in range(1<<M):
            alpha=[beta^inv[x] for x in b]
            assert beta not in alpha and len(set(alpha))==n
            for c in range(1<<n):
                z=0
                for i,bi in enumerate(b):
                    if (c>>i)&1: z^=bi
                assert (z==0)==base[c]
            reps+=1
    assert reps==formula(M,s)
    return reps

assert check([1,2,3],2,2)==24
assert check([1,2,3],2,3)==336
assert check([1,2,3,4,5,6,7],3,3)==1344
assert check([1,2,3,4,5,6],3,3)==1344

inj4=sum(1 for _ in frames(4,3))
assert inj4==15*14*12
assert 16*inj4==40320

print("VERIFY_OK")
