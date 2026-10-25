#!/usr/bin/env python3
"""Exact rational checks for abelian prime-power element-order moments."""
from fractions import Fraction
from itertools import product

def parts(n, mx=None):
    if n == 0:
        yield ()
        return
    for j in range(min(n, mx if mx is not None else n), 0, -1):
        for t in parts(n-j,j): yield (j,)+t

def psi(p,k, partition):
    if not partition: return 1
    L=max(partition)
    a=1
    result=1
    for j in range(1,L+1):
        b=p**sum(min(j,v) for v in partition)
        result+=(b-a)*p**(j*k)
        a=b
    return result

def formula(p,k,partition):
    n=sum(partition);l=partition[0];b=n-l
    if l<=b: return None
    H=partition[1:]
    c=Fraction((p-1)*p**k,p**(k+1)-1)
    d=Fraction(p**k-1,p**(k+1)-1)
    psiC_b=psi(p,k,(b,)) if b else 1
    psiCH=psi(p,k,((b,)+H) if b else H)
    E=p**b*d+psiCH-p**b*psiC_b
    return c/p**(b*k)+E/p**((k+1)*n),E

checks=0
for p in (2,3,5):
 for k in (1,2,3,4):
  for n in range(1,11):
   for z in parts(n):
    f=formula(p,k,z)
    if f is None:continue
    lhs=Fraction(psi(p,k,z),p**((k+1)*n))
    assert lhs==f[0],(p,k,z,lhs,f)
    assert f[1]>0
    checks+=1
    b=n-z[0]
    assert lhs>Fraction((p-1)*p**k,p**(k+1)-1)/p**(b*k)

for p in (2,3,5):
 for k in (1,2,3):
  for b in range(5):
   for l in (b+1,b+3,b+7):
    z=(l,)+(1,)*b
    n=l+b
    f=Fraction(psi(p,k,z),p**((k+1)*n))
    c=Fraction((p-1)*p**k,p**(k+1)-1)/p**(b*k)
    assert 0<f-c<=2*Fraction(p**((k+2)*b),p**((k+1)*n))
print('VERIFY_OK exact_partition_cases=', checks, ' and uniform error bounds')
