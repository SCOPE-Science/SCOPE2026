"""Exact finite binary-polynomial enumeration of tame degree-2, 4 and 6 maps.
Run with Python 3.10+. No third-party dependencies.
"""
from collections import Counter
from itertools import product
from math import comb

def deg(a): return a.bit_length()-1

def rem(a,b):
    d=deg(b)
    while a and deg(a)>=d: a ^= b << (deg(a)-d)
    return a

def mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        a <<=1; b>>=1
    return r

def gcd(a,b):
    while b: a,b=b,rem(a,b)
    return a

def hasse(a,j):
    return sum(((comb(i,j)&1) & (a>>i&1)) << (i-j) for i in range(j,deg(a)+1))

def reverse(a,d):
    return sum((a>>i&1) << (d-i) for i in range(d+1))

def irreducibles_to(n):
    primes=[]
    for p in range(2,1<<(n+1)):
        h=deg(p)
        if all(rem(p,q) for q in primes if deg(q)<=h//2): primes.append(p)
    return primes

IRR = irreducibles_to(10)

def ramification(A,B,d):
    jets=[mul(hasse(A,j),B)^mul(A,hasse(B,j)) for j in range(d+1)]
    if jets[1]==0: return None
    profile=[]
    for p in IRR:
        if deg(p)>2*d-2: break
        if rem(jets[1],p): continue
        e=next(j for j in range(2,d+1) if rem(jets[j],p))
        profile.append((deg(p),e,p))
    A0,B0=reverse(A,d),reverse(B,d)
    jets0=[mul(hasse(A0,j),B0)^mul(A0,hasse(B0,j)) for j in range(d+1)]
    e_inf=next(j for j in range(1,d+1) if jets0[j]&1)
    if e_inf>1: profile.append((1,e_inf,0))
    return tuple(sorted(profile))

def enumerate_maps(d):
    count=0; tame=[]; signatures=Counter()
    for A in range(1<<(d+1)):
        for B in range(1<<(d+1)):
            if not ((A|B)>>d&1) or gcd(A,B)!=1: continue
            count+=1
            prof=ramification(A,B,d)
            if prof is not None and all(e&1 for _,e,_ in prof):
                tame.append((A,B))
                signatures[tuple(sorted((k,e) for k,e,_ in prof))]+=1
    return count,tame,signatures

def lin_matrices():
    return [(a,b,c,d) for a,b,c,d in product((0,1),repeat=4) if (a*d-b*c)&1]

def binpow(a,b,n):
    r=1
    for _ in range(n):
        z=0
        for i in range(deg(r)+1):
            if r>>i&1:
                if b:z^=1<<i
                if a:z^=1<<(i+1)
        r=z
    return r

def source_substitute(F,d,m):
    a,b,c,e=m
    PX=[binpow(a,b,j) for j in range(d+1)]
    QZ=[binpow(c,e,j) for j in range(d+1)]
    z=0
    for i in range(d+1):
        if F>>i&1: z^=mul(PX[i],QZ[d-i])
    return z

def orbit(pair,d):
    z=set()
    mats=lin_matrices()
    for m in mats:
        A=source_substitute(pair[0],d,m)
        B=source_substitute(pair[1],d,m)
        for p,q,r,s in mats:
            z.add((p*A^q*B,r*A^s*B))
    return z

if __name__=='__main__':
    expected={2:(24,0),4:(384,0),6:(6144,72)}
    for d in (2,4,6):
        count,tame,signatures=enumerate_maps(d)
        assert (count,len(tame))==expected[d], (d,count,len(tame))
        print('degree',d,'all_maps',count,'tame',len(tame),'profiles',dict(signatures))
        if d==6:
            assert set(tame)==orbit((2,73),6)|orbit((2,105),6)
            assert len(orbit((2,73),6))==len(orbit((2,105),6))==36
            assert not (orbit((2,73),6)&orbit((2,105),6))
            assert signatures=={((1,3),(1,5),(2,3)):72}
            print('degree 6: two disjoint orbits of size 36, representatives x/(x^6+x^3+1) and x/(x^6+x^5+x^3+1)')
            open('tame_d6_pairs.txt','w',encoding='utf-8').write(''.join(f'{a} {b}\n' for a,b in sorted(tame)))
    print('PASS')
