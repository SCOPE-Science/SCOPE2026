#!/usr/bin/env python3
"""Independent finite-state tests of stationary maxima in a distinct-panel q-voter process."""
from fractions import Fraction
from math import comb
import sympy as sp

n,m,z,k=sp.symbols('n m z k', integer=True)
F=(2*m-n)*(n+z)*(n+z-1) - (n+1)*(2*m-n+z-1)*(2*m-n+z-2)
assert sp.expand(F-(2*m-2*n-1)*(-2*m*n-2*m+n*n+n+z*z-3*z+2))==0
assert sp.expand(F.subs(n,m-1-k)-(2*k+1)*(k*(k+1)-m*(m+1)+(z-1)*(z-2)))==0

def stationary_weights(m,z,replacement=False):
    # Obtain exact stationary ratios directly from the one-step update rule.
    S=2*m
    values=[Fraction(1)]
    for j in range(S):
        if replacement:
            ratio=Fraction(S-j,j+1)*Fraction((j+z)**2,(S-j+z-1)**2)
        else:
            ratio=Fraction(S-j,j+1)*Fraction((j+z)*(j+z-1),(S-j+z-1)*(S-j+z-2))
        values.append(values[-1]*ratio)
    return [v/sum(values) for v in values]

def predicted(m,z):
    # Fully exact formula inferred from the algebraic sign identity.
    Delta=m*(m+1)-(z-1)*(z-2)
    if Delta<0: return [m]
    if Delta==0: return [m-1,m,m+1]
    for kk in range(1,m):
        if kk*(kk+1)==Delta:
            return [m-kk-1,m-kk,m+kk,m+kk+1]
    kk=next((j for j in range(1,m) if j*(j+1)>Delta),m)
    return [m-kk,m+kk]

trials=0
for mm in range(1,16):
    for zz in range(2,mm+12):
        p=stationary_weights(mm,zz)
        modes=[i for i,v in enumerate(p) if v==max(p)]
        assert modes==predicted(mm,zz),(mm,zz,modes,predicted(mm,zz))
        assert sum(p)==1
        assert all(p[j]==p[2*mm-j] for j in range(mm+1))
        trials+=1

# Directly count two-person samples without repetition for all small population states.
for mm in range(1,5):
  for zz in range(2,7):
    N=2*mm+2*zz;S=2*mm
    for j in range(S+1):
      plus_population=j+zz
      minus_population=S-j+zz
      # For each susceptible B agent, other A agents form precisely this many pairs.
      plus_pairs=comb(plus_population,2)
      minus_pairs=comb(minus_population,2)
      den=comb(N-1,2)
      up=Fraction(S-j,N)*Fraction(plus_pairs,den)
      down=Fraction(j,N)*Fraction(minus_pairs,den)
      if j<S:
        assert up>0
      if j>0:
        assert down>0
      if j<S:
        p=stationary_weights(mm,zz)
        assert p[j]*up==p[j+1]*Fraction(j+1,N)*Fraction(comb(S-j-1+zz,2),den)
      trials+=1

# Negative Pell instances, including two beyond the smallest examples.
x,y=1,1
pell=[]
for exponent in range(3,12,2):
    # exact power of 1+sqrt(2)
    x,y=1,0
    for i in range(exponent): x,y=x+2*y,x+y
    assert x*x-2*y*y==-1
    mm=(x-1)//2; a=(y-1)//2; zz=a+2
    assert mm> a>=2
    target=[mm-a-1,mm-a,mm+a,mm+a+1]
    assert predicted(mm,zz)==target
    if exponent<=7:
      p=stationary_weights(mm,zz)
      assert [i for i,v in enumerate(p) if v==max(p)]==target
      pr=stationary_weights(mm,zz,replacement=True)
      assert [i for i,v in enumerate(pr) if v==max(pr)]==[mm-a,mm+a]
    pell.append((exponent,mm,zz,target))

print('PASS: symbolic polynomial identities; %d rational distribution and rate checks; Pell examples %s' % (trials,pell))
