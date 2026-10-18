#!/usr/bin/env python3
"""Exact closed-point calculation from the complete genus-four F2 zeta census.

Input DATA.b64 encodes the 620 distinct (N1,N2,N3,N4) tuples from
X. Xarles, Censusforgenus4curvesoverF2, ListCurvesGenus4p2.txt.
No network access or third-party Python modules are required.
"""
from base64 import b64decode
from collections import Counter
from pathlib import Path

b=b64decode(Path(__file__).with_name('DATA.b64').read_text().strip(), validate=True)
assert len(b)==2480
rows=[tuple(b[4*i:4*i+4]) for i in range(620)]
assert len(set(rows))==620 and rows==sorted(rows)

def n6_from_L(row):
    s=[0]+[2**n+1-row[n-1] for n in range(1,5)]
    c=[1]
    for n in range(1,5):
        numerator=-(s[n]+sum(c[j]*s[n-j] for j in range(1,n)))
        assert numerator%n==0
        c.append(numerator//n)
    c.extend([2*c[3],4*c[2],8*c[1],16])
    for n in (5,6):
        s.append(-(n*c[n]+sum(c[j]*s[n-j] for j in range(1,n))))
    return 65-s[6],c,s

def n6_from_real_roots(c):
    # L(T)=T^4 h(T^{-1}+2T), h(U)=U^4+a1 U^3+...+a4.
    a1=c[1]; a2=c[2]-8; a3=c[3]-6*a1; a4=c[4]-24-4*a2
    a=[1,a1,a2,a3,a4]
    t=[4]
    for n in range(1,7):
        if n<=4:
            t.append(-(sum(a[j]*t[n-j] for j in range(1,n))+n*a[n]))
        else:
            t.append(-sum(a[j]*t[n-j] for j in range(1,5)))
    return 65-(t[6]-12*t[4]+36*t[2]-64)

freq=Counter(); minimizers=[]
for i,row in enumerate(rows):
    n6,c,s=n6_from_L(row)
    assert n6==n6_from_real_roots(c)
    numerator=n6-row[2]-row[1]+row[0]
    assert numerator%6==0
    b6=numerator//6
    assert b6>=0
    freq[b6]+=1
    if b6<=1: minimizers.append((i,row,n6,b6,tuple(c)))
assert min(freq)==1 and freq[1]==1
assert minimizers==[(360,(3,9,9,45),21,1,(1,0,2,0,9,0,8,0,16))]
assert sum(freq.values())==620
print('B6 histogram:',sorted(freq.items()))
print('Unique sharp N-vector / N6 / Weil L:', minimizers)

# Independent arithmetic check of the known genus-four extremal DS curve:
# y^2+y=x^9+x^5+1; its sole F2 and F32 point is infinity.
MOD=0b100101  # irreducible z^5+z^2+1

def mul(x,y):
    ans=0
    while y:
        if y&1: ans^=x
        y//=2; x<<=1
        if x&32: x^=MOD
    return ans

def power(x,n):
    ans=1
    while n:
        if n&1: ans=mul(ans,x)
        x=mul(x,x);n//=2
    return ans

assert len({power(2,i) for i in range(31)})==31

def trace(x,n):
    acc=0
    for _ in range(n): acc^=x;x=mul(x,x)
    return acc
for n in (1,5):
    field=range(2**n) if n==5 else range(2)
    # For n=1 the field is the literal {0,1}; for n=5 all binary 5-tuples.
    affine=0
    for x in field:
        v=power(x,9)^power(x,5)^1
        if trace(v,n)==0: affine+=2
    assert affine==0
    print('C(F_2^%d):'%n,affine+1)

# The genus-four global universal step: B7>0 by Weil and Bn>0 for n>=8
# by Aubry-Haloui-Lachaud's strict bound used in Aubry-Herbaut-Monaldi.
assert 126**2 > 2*72**2  # N7-N1 >=126-72*sqrt(2)>0
assert (2**2-1)**2 >= 2*4  # for every n>=8, (2^(n/4)-1)^2 >=2g
print('VERIFIED: rho(2,4)=6; sharp B6=1 in one isogeny class.')
