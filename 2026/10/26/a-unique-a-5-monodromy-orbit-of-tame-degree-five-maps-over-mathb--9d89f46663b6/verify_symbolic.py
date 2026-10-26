#!/usr/bin/env python3
"""Exact symbolic independent verification of all tame degree-five maps over F2.
Only the standard library is used. Bit i represents coefficient of x**i.
"""
from collections import Counter
from math import comb

D = 5

def degree(p): return p.bit_length()-1

def product(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

def remainder(a,b):
    assert b
    while a and degree(a)>=degree(b): a^=b << (degree(a)-degree(b))
    return a

def gcd(a,b):
    while b:a,b=b,remainder(a,b)
    return a

def hasse(a,k):
    return sum((1 << (j-k)) for j in range(k,D+1)
               if (a>>j)&1 and (comb(j,k)&1))

def irreducible(h):
    d=degree(h)
    return d>=1 and all(remainder(h,g) for k in range(1,d//2+1)
                         for g in range(1<<k,(1<<(k+1))))

IRR=[h for d in range(1,5) for h in range(1<<d,1<<(d+1)) if irreducible(h)]
assert IRR==[2,3,7,11,13,19,25,31],IRR
# With a coprime degree-5 pair, the Wronskian is a nonzero polynomial
# in x**2 of degree <=8. Every finite ramification point therefore
# has minimal polynomial of degree <=4, exhaustively represented by IRR.

def ram_types(a,b):
    T=[product(hasse(a,k),b)^product(hasse(b,k),a) for k in range(1,D+1)]
    assert T[0] and all(not ((T[0]>>j)&1) for j in range(1,degree(T[0])+1,2))
    ram=[]
    for h in IRR:
        if remainder(T[0],h):continue
        e=next(k for k in range(1,D+1) if remainder(T[k-1],h))
        assert e>1
        ram.extend([e]*degree(h))
    # Infinity, local coordinate z=Z/X.
    top_a=(a>>D)&1;top_b=(b>>D)&1
    e_inf=next(k for k in range(1,D+1)
               if (((a>>(D-k))&1)*top_b)^(((b>>(D-k))&1)*top_a))
    ram.append(e_inf)
    return ram

MAPS={(a,b) for a in range(64) for b in range(1,64)
      if (a|b)&32 and gcd(a,b)==1}
assert len(MAPS)==1536,len(MAPS)
TAME={(a,b) for a,b in MAPS if all(e%2 for e in ram_types(a,b))}
assert len(TAME)==60,len(TAME)
PAT=Counter(tuple(sorted(e for e in ram_types(a,b) if e>1)) for a,b in TAME)
assert PAT==Counter({(3,3,3,3):36,(5,5):24}),PAT

# Complete left-right action by the six binary Möbius transforms.
GL=[(a,b,c,d) for a in range(2) for b in range(2)
    for c in range(2) for d in range(2) if (a*d ^ b*c)==1]
assert len(GL)==6

def transform_form(mask,mat):
    A,B,C,E=mat
    out=0
    for n in range(6):
        if not (mask>>n)&1: continue
        term=1
        for p,q in [(A,B)]*n+[(C,E)]*(D-n):
            term=((term<<1) if p else 0) ^ (term if q else 0)
        out ^= term
    return out

def image(pair,pre,post):
    a,b=pair
    a,b=transform_form(a,pre),transform_form(b,pre)
    u,v,w,z=post
    return ((a if u else 0)^(b if v else 0),
            (a if w else 0)^(b if z else 0))

unseen=set(TAME);ORBIT=[]
while unseen:
    representative=min(unseen)
    orb={image(representative,g,h) for g in GL for h in GL}
    assert orb <= TAME
    unseen-=orb
    ORBIT.append((len(orb),min(orb),tuple(sorted(set(ram_types(*representative))-{1}))))
ORBIT.sort()
assert ORBIT==[(6,(19,33),(5,)),(18,(1,32),(5,)),(36,(7,41),(3,))],ORBIT
assert sum(e for e,_,_ in ORBIT)==60

if __name__=='__main__':
    print('ALL_DEGREE5_PAIRS',len(MAPS))
    print('IRREDUCIBLES_DEGREE_1_TO_4',IRR)
    print('TAME_MAPS',len(TAME))
    print('RAMIFICATION_PROFILES',sorted(PAT.items()))
    print('LEFT_RIGHT_ORBITS',ORBIT)
    print('TAME_PAIR_MASKS',','.join('%d:%d'%p for p in sorted(TAME)))
    print('VERIFY_OK')
