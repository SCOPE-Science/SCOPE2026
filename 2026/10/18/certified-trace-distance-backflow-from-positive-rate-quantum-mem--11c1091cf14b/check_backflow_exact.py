"""Exact rational certificate for trace-distance backflow at positive reset rate.
Only Python 3 standard library. Every inequality uses Fraction.
"""
from fractions import Fraction as F
from math import factorial

A=(F(25,29),F(10,29))

def mul(u,v):
    return (u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def sqabs(z):
    return z[0]**2+z[1]**2

def partial(t,N=80):
    z=(-F(t),-F(5*t,2))
    term=(F(1),F(0))
    summation=term
    for n in range(1,N):
        term=mul(term,mul((A[0]+n-1,A[1]),z))
        term=(term[0]/(n*n),term[1]/(n*n))
        summation=(summation[0]+term[0],summation[1]+term[1])
    return summation

# Since |A|<1 and |z|<11, nth Kummer term <=11^n/n!.
# The sum of all terms from n=80 onward is at most B.
B=F(81*11**80,70*factorial(80))
assert 725 < 29*29  # |A|<1
assert 116 < 121 # |z|^2 <=116<121 for t in [3,4]
assert B<F(1,10000000000)
P3=partial(3)
P4=partial(4)
# Use triangle inequality and B<1/10000.
# The two squared-norm claims are exact rational arithmetic.
assert F(17,10000)<sqabs(P3)<F(18,10000)
assert sqabs(P3)<(F(1,20)-F(1,10000))**2
assert F(119,10000)<sqabs(P4)<F(120,10000)
assert sqabs(P4)>(F(1,10)+F(1,10000))**2
# Thus |f(3)|<1/20, |f(4)|>1/10, by the series tail bound.
print('CERTIFIED: |M(a;1;-3(1+5i/2))| < 1/20')
print('CERTIFIED: |M(a;1;-4(1+5i/2))| > 1/10')
assert F(1,20)-7*F(1,200)==F(3,200)
print('CERTIFIED: trace-distance backflow > 1/20 at gap ratio 5/2')
print('CERTIFIED: backflow > 3/200 on the gap-ratio band [499/200, 501/200]')
print('tail_bound < 1/10^10:', B<F(1,10**10))
print('approximate squared moduli',float(sqabs(P3)),float(sqabs(P4)))
