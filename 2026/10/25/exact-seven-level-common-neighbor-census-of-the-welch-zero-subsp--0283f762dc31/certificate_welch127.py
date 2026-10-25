#!/usr/bin/env python3
"""Exact finite-field certificate for the Welch seven-space intersection graph."""
from collections import Counter
from itertools import combinations, product

N=7
Q=1<<N
POLY=0b10000011  # X^7 + X + 1, irreducible over F_2.

def mult(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1
        a<<=1
        if a&Q:a^=POLY
    return out

def power(a,e):
    r=1
    while e:
        if e&1:r=mult(r,a)
        a=mult(a,a)
        e>>=1
    return r

# Rabin irreducibility criterion for degree seven (the only prime divisor is 7).
def polynomial_mod(v, f):
    while v.bit_length() >= f.bit_length():
        v ^= f << (v.bit_length() - f.bit_length())
    return v

def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_mod(a, b)
    return a

def polynomial_square_mod(a, f):
    t = 0
    for i in range(a.bit_length()):
        if a & (1 << i):
            t ^= 1 << (2*i)
    return polynomial_mod(t, f)

assert polynomial_gcd(POLY, 0b110) == 1  # gcd(f, x^2-x)=1.
x = 0b10
for _ in range(7):
    x = polynomial_square_mod(x, POLY)
assert x == 0b10  # x^(2^7)=x mod f, so f is irreducible.
assert all(mult(a, power(a,126)) == 1 for a in range(1,Q))

def block(a,b,c):
    points=(a,b,c,a^b,a^c,b^c,a^b^c)
    return sum(1<<z for z in points)

# Two independent exhaustive descriptions of the Grassmannian Gr_2(7,3).
triple_masks=set()
for a,b,c in combinations(range(1,Q),3):
    if a^b==c:continue
    triple_masks.add(block(a,b,c))
assert len(triple_masks)==11811
rref_masks=set()
for piv in combinations(range(N),3):
    options=[]
    for p in piv:
        free=[j for j in range(p+1,N) if j not in piv]
        options.append([1<<p | sum((1<<j) for j,bit in zip(free,z) if bit)
                        for z in product([0,1],repeat=len(free))])
    for a,b,c in product(*options):
        rref_masks.add(block(a,b,c))
assert len(rref_masks)==11811 and rref_masks==triple_masks

W=[power(x,11) for x in range(Q)]
def welch_zero(mask):
    acc=0
    for x in range(1,Q):
        if mask>>x & 1:acc^=W[x]
    return acc==0
zeros={mask for mask in rref_masks if welch_zero(mask)}
assert len(zeros)==127

D=(1,2,3,8,9,10,11)
seed=sum(1<<a for a in D)
assert seed in zeros
orbit={sum(1<<mult(a,r) for a in D) for r in range(1,Q)}
assert len(orbit)==127 and orbit==zeros

# Multiplicative quotient (connection) set for the cyclic intersection graph.
R={mult(a,power(b,Q-2)) for a in D for b in D if a!=b}
assert len(R)==42 and 1 not in R

profile=Counter()
for t in range(2,Q):
    common=sum(mult(t,r) in R for r in R)
    profile[("edge" if t in R else "nonedge",common)]+=1
expected={("edge",15):28,("edge",21):14,
          ("nonedge",8):14,("nonedge",10):14,("nonedge",12):28,
          ("nonedge",14):14,("nonedge",16):14}
assert dict(profile)==expected,profile
assert sum(v for (state,k),v in profile.items() if state=='edge')==42
assert sum(v for (state,k),v in profile.items() if state=='nonedge')==84
triangle_count=sum(v*k for (state,k),v in profile.items() if state=='edge')*127//6
assert triangle_count==15113

# An independent check of the primary source's Kloosterman count formula.
def trace(a):
    x=a;s=a
    for _ in range(1,N):
        x=mult(x,x);s^=x
    assert s in (0,1)
    return s
signs=Counter(trace(u^power(u,Q-2)) for u in range(1,Q))
assert signs=={0:57,1:70}
Kl=signs[0]-signs[1]
assert Kl==-13
assert (Q-1)*(Q+1-3*Kl)//168==127
print('CERTIFICATE_OK gr_2_7_3=11811 zero_welch_planes=127 orbit=127 degree=42')
print('multiplier_codegrees',sorted(profile.items()))
print('unordered_pair_counts',sorted(((kind,common),127*count//2)
                                     for (kind,common),count in profile.items()))
print('triangles=15113 kloosterman=-13')
