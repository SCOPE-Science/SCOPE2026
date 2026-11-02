"""Independent finite checks for the sharp sign-sketch negative-step law.

Only Python standard-library dependencies. Finite checks supplement the proof.
"""
import itertools
import math
from fractions import Fraction
from math import comb


def threshold(kappa):
    return 2 * math.sqrt(kappa) / (1 + kappa)


def sharp_probability(k, kappa):
    chi = threshold(kappa)
    return sum(comb(k, j) for j in range(k + 1)
               if 2*j-k < -k*chi-1e-12) / (2**k)


def negative_count(k, a, L, x, y):
    result = 0
    for bits in itertools.product((-1, 1), repeat=k):
        cross = sum(bits)
        numer = k*(a*x*x+L*y*y)+(a+L)*cross*x*y
        denom = k*(a*a*x*x+L*L*y*y)+2*a*L*cross*x*y
        # If the sketched search vector vanishes, the minimal-norm coefficient is zero.
        if denom != 0 and numer < 0:
            result += 1
    return Fraction(result, 2**k)

# Every sign row has four equally likely possibilities, but its product
# is a fair Rademacher variable. Enumerating products is exact.
checks=0
for k in range(1, 9):
    for K in (Fraction(2), Fraction(4), Fraction(16), Fraction(64), Fraction(400)):
        # AM-GM extremizer has irrational x in general; pick K square.
        if math.isqrt(K.numerator)**2 == K.numerator:
            x=Fraction(math.isqrt(K.numerator)); y=Fraction(1)
            p=negative_count(k,Fraction(1),K,x,y)
            assert abs(float(p)-sharp_probability(k,float(K)))<1e-12,(k,K,p)
            checks+=1
        # No other rational tested direction has greater risk.
        limit=sharp_probability(k,float(K))
        for x,y in ((1,1),(1,2),(2,1),(3,1),(1,3),(-2,1),(5,2),(7,4)):
            p=negative_count(k,Fraction(1),K,Fraction(x),Fraction(y))
            assert float(p)<=limit+1e-13,(k,K,x,y,p,limit)
            checks+=1

# Demonstrate the strict endpoint of the k=3 phase transition.
Kcrit=(3+2*math.sqrt(2))**2
assert abs(threshold(Kcrit)-1/3)<1e-14
assert sharp_probability(3,Kcrit*(1-1e-8))==1/8
assert sharp_probability(3,Kcrit*(1+1e-8))==1/2
# All k have a persistent probability 2^-k from the all-opposite-sign event.
for k in range(1, 17):
    assert sharp_probability(k,1+1e-4)>=2**(-k)-1e-14

print('PASS:',checks,'exact-rational enumeration comparisons;'
      ' critical k=3 phase jump; 16 persistent-tail checks')
