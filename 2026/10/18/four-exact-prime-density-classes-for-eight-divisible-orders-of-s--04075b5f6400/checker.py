#!/usr/bin/env python3
"""Exact finite arithmetic checks for prime-order divisibility on split cubics."""
from fractions import Fraction
from math import isqrt
from itertools import product


def relations(alpha, beta, gamma):
    """All exponent triples whose radical product is a rational square."""
    def square(n):
        return isqrt(n)**2 == n
    return tuple(k for k in range(8) if square(
        alpha**(k & 1) * beta**((k >> 1) & 1) * gamma**((k >> 2) & 1)))


def good(a,b,c,m):
    return (m*a == 1 and m*c == 1) or (a == 1 and m*b == 1) or (c == 1 and b == 1)


def density_for_relations(R):
    permitted = []
    for a,b,c in product((-1,1),repeat=3):
        if all(a**(k&1)*b**((k>>1)&1)*c**((k>>2)&1)==1 for k in R):
            permitted.append((a,b,c))
    n = sum(good(a,b,c,m) for a,b,c in permitted for m in (-1,1))
    return Fraction(n,2*len(permitted)),len(permitted),n

subspaces = []
for mask in range(256):
    S = frozenset(i for i in range(8) if mask&(1<<i))
    if 0 in S and all((i^j) in S for i in S for j in S):
        subspaces.append(tuple(sorted(S)))
assert len(subspaces) == 16
found=set()
for S in subspaces:
    den,npairs,n = density_for_relations(S)
    assert npairs*len(S)==8
    found.add(den)
    print('relations=',','.join(str(k) for k in S),'admissible_ABC=',npairs,
          'successful_ABCm=',n,'density=',den)
assert found == {Fraction(1,2),Fraction(5,8),Fraction(3,4),Fraction(1,1)}

curves = [(2,2,Fraction(1,2)),(2,3,Fraction(5,8)),
          (1,2,Fraction(3,4)),(9,16,Fraction(1,1)),
          (952,72,Fraction(3,4))]
for a,b,expected in curves:
    R=relations(a,b,a+b)
    den,_,_=density_for_relations(R)
    assert den==expected, (a,b,R,den,expected)
    print('curve_gaps=',a,b,'relations=',R,'exact_density=',den)

# Exhaustive direct comparison of point counting and 2-descent criterion
# for each good odd prime <= 1031, for each curve.
def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

for a,b,_ in curves:
    checks=0
    for p in range(3,1032,2):
        if not isprime(p) or (a*b*(a+b))%p==0:continue
        leg=lambda z: 0 if z%p==0 else (1 if pow(z%p,(p-1)//2,p)==1 else -1)
        r=(0,a,a+b)
        pred = any(leg(r[i]-r[j])==1 and leg(r[i]-r[k])==1
                   for i,j,k in ((0,1,2),(1,0,2),(2,0,1)))
        order = p+1+sum(leg((x-r[0])*(x-r[1])*(x-r[2])) for x in range(p))
        assert (order%8==0)==pred, (p,a,b,order,pred)
        checks+=1
    print('curve_gaps=',a,b,'good_primes_checked=',checks)
print('CERTIFICATE_OK')
