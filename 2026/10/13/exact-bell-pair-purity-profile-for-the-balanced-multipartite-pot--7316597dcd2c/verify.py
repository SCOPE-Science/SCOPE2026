from fractions import Fraction
from itertools import combinations
from math import comb

def coeff_poly(K, m):
    p=[1]
    for _ in range(K):
        q=[0]*(len(p)+2)
        for i,a in enumerate(p):
            q[i]+=a; q[i+1]+=a; q[i+2]+=a
        p=q
    return p[m]

def direct(K,m):
    total=Fraction(0,1)
    for A in combinations(range(2*K),m):
        s=set(A)
        singles=0
        for j in range(K):
            c=(2*j in s)+(2*j+1 in s)
            if c==1: singles+=1
        total += Fraction(1,2**singles)
    return total/Fraction(comb(2*K,m),1)

for K in range(1,9):
    for m in range(1,K+1):
        a=direct(K,m)
        b=Fraction(coeff_poly(K,m),comb(2*K,m))
        assert a==b,(K,m,a,b)
assert direct(2,2)==Fraction(1,2)
assert direct(3,3)==Fraction(7,20)
assert direct(4,4)==Fraction(19,70)
print('VERIFY_OK')
