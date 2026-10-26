#!/usr/bin/env python3
"""Independent finite-extension enumeration of tame degree-five covers of P1/F2.
Pointwise local Taylor expansions over F16 and F8, and a chart at infinity.
"""
from collections import Counter
from math import comb
DEG=5

class Field:
    def __init__(self,n,modulus):
        self.size=1<<n
        self.times=[[0]*self.size for _ in range(self.size)]
        for a in range(self.size):
            for b in range(self.size):
                x,y,z=a,b,0
                while y:
                    if y&1:z^=x
                    x<<=1
                    if x&self.size:x^=modulus
                    y>>=1
                self.times[a][b]=z
        self.power=[[1]*(DEG+1) for _ in range(self.size)]
        for a in range(self.size):
            for i in range(1,DEG+1):
                self.power[a][i]=self.times[self.power[a][i-1]][a]

    def evaluate(self,polynomial,x):
        value=0
        for j in range(DEG+1):
            if polynomial>>j&1:value^=self.power[x][j]
        return value

    def order(self,a,b,x):
        av=self.evaluate(a,x);bv=self.evaluate(b,x)
        assert av or bv
        for k in range(1,DEG+1):
            ak=bk=0
            for j in range(k,DEG+1):
                if comb(j,k)&1:
                    if a>>j&1:ak^=self.power[x][j-k]
                    if b>>j&1:bk^=self.power[x][j-k]
            if self.times[ak][bv]^self.times[bk][av]:return k
        raise AssertionError('Coprime degree-five forms require finite order')

F16=Field(4,0b10011) # x^4+x+1
F8=Field(3,0b1011) # x^3+x+1

def mod(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

def rel_prime(a,b):
    while b:a,b=b,mod(a,b)
    return a==1

def ramification(a,b):
    orders=[F16.order(a,b,x) for x in range(16)]
    orders += [F8.order(a,b,x) for x in range(2,8)]
    la,lb=(a>>5)&1,(b>>5)&1
    assert la or lb
    orders.append(next(k for k in range(1,6)
                       if (((a>>(5-k))&1)*lb)^(((b>>(5-k))&1)*la)))
    return orders

DEGREE5=[(a,b) for a in range(64) for b in range(1,64)
         if (a|b)&32 and rel_prime(a,b)]
assert len(DEGREE5)==1536
TAME=[p for p in DEGREE5 if all(e%2 for e in ramification(*p))]
assert len(TAME)==60,len(TAME)
profiles=Counter(tuple(sorted(x for x in ramification(*p) if x>1)) for p in TAME)
# F16 and F8 share only the two points over F2, which are excluded in the F8 list.
assert profiles==Counter({(3,3,3,3):36,(5,5):24}),profiles
if __name__=='__main__':
    print('ALL_DEGREE5_PAIRS',len(DEGREE5))
    print('F16_MODULUS',0b10011,'F8_MODULUS',0b1011)
    print('TAME_MAPS',len(TAME))
    print('RAMIFICATION_PROFILES',sorted(profiles.items()))
    print('PAIR_MASKS',','.join('%d:%d'%p for p in TAME))
    print('VERIFY_OK')
