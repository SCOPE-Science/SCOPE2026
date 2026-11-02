#!/usr/bin/env python3
"""Finite-field check of the Chevalley B2 positive-root nilradical commuting-tuple formulas.

Independent checks enumerate coordinate tuples, evaluate original Lie brackets,
and compare with the determinantal component membership and point-count formulas.
No third-party packages are needed.
"""
from itertools import product

class Field:
    def __init__(self, q):
        self.q = q
        if q in (2, 3, 5, 7):
            self.p = q
            self.add = lambda a, b: (a+b) % q
            self.mul = lambda a, b: (a*b) % q
            self.neg = lambda a: (-a) % q
        elif q == 4:
            self.p = 2
            self.add = lambda a, b: a ^ b
            def mult(a, b):
                r = 0
                for i in range(2):
                    for j in range(2):
                        if (a >> i) & 1 and (b >> j) & 1:
                            r ^= 1 << (i+j)
                # t^2 = t+1
                if r & 4: r ^= 7
                return r
            self.mul = mult
            self.neg = lambda a: a
        elif q == 9:
            self.p = 3
            self.add = lambda a,b: ((a%3+b%3)%3)+3*((a//3+b//3)%3)
            def mult(a,b):
                a0,a1=a%3,a//3; b0,b1=b%3,b//3
                # t^2 = -1 (irreducible over F3)
                return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
            self.mul = mult
            self.neg = lambda a: ((-a%3)%3)+3*((-(a//3))%3)
        else:
            raise ValueError(q)
    def diffprod(self, a,b,c,d):
        return self.add(self.mul(a,d), self.neg(self.mul(b,c)))

def prediction(q,m):
    if q%2==0:
        return q**(2*m)*(1+(q+1)*(q**m-1))
    return q**(3*m)+q**(m+2)*(q**m-1)

def check_reduced(q,m):
    F=Field(q); add,mul=F.add,F.mul
    vectors=list(product(range(q),repeat=m))
    zeros=(0,)*m
    count=0; singular=0
    for a in vectors:
        for b in vectors:
            for c in vectors:
                ab=all(F.diffprod(a[i],b[i],a[j],b[j])==0 for i in range(m) for j in range(i+1,m))
                ac=all(F.diffprod(a[i],c[i],a[j],c[j])==0 for i in range(m) for j in range(i+1,m))
                commutes=ab and (F.p==2 or ac)
                if F.p==2:
                    rankl=ab
                    assert commutes==rankl
                    if commutes and a==zeros and b==zeros: singular+=1
                else:
                    rank3=ab and ac and all(F.diffprod(b[i],c[i],b[j],c[j])==0 for i in range(m) for j in range(i+1,m))
                    component=(a==zeros or rank3)
                    assert commutes==component, (q,m,a,b,c)
                    if commutes and a==zeros and rank3: singular+=1
                count+=int(commutes)
    N=count*q**m
    assert N==prediction(q,m), (q,m,N,prediction(q,m))
    S=singular*q**m
    expectS=(q**(2*m) if F.p==2 else q**m*(1+(q+1)*(q**m-1)))
    assert S==expectS, (q,m,S,expectS)
    return N,S

def check_full(q):
    F=Field(q)
    # Full coefficient tuples (a_i,b_i,c_i,d_i) for two Lie elements.
    n=0
    for a,b,c,d,a2,b2,c2,d2 in product(range(q),repeat=8):
        b1=F.diffprod(a,b,a2,b2)
        b2val=F.mul(F.add(1,1),F.diffprod(a,c,a2,c2))
        if b1==0 and b2val==0: n+=1
    assert n==prediction(q,2), (q,n,prediction(q,2))
    return n

def main():
    print('Original bracket constants: [e1,e2]=e3; [e1,e3]=2e4')
    cases=[(2,2),(3,2),(4,2),(5,2),(7,2),(9,2),(2,3),(3,3),(4,3),(2,4)]
    for q,m in cases:
        N,S=check_reduced(q,m)
        print(f'q={q} m={m} N={N} singular={S} OK')
    for q in (2,3,4,5):
        print(f'full_pair q={q} N={check_full(q)} OK')
    print('B2_BAD_PRIME_COMMUTING_TUPLES_OK 10_REDUCED 4_FULL')

if __name__=='__main__':main()
