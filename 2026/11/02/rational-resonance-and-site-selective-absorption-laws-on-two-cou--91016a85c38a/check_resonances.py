#!/usr/bin/env python3
"""Independent finite linear-algebra and arithmetic checks for two-block hypercube capture."""
from fractions import Fraction
from math import comb, gcd
from itertools import product
import numpy as np

def kraw(n,k,r):
    return sum((-1)**j*comb(r,j)*comb(n-r,k-j) for j in range(max(0,k-(n-r)),min(k,r)+1))

def theoretical(a,b,rho):
    # rho=None signifies irrational relative coupling.
    groups={}
    for k in range(a+1):
        for l in range(b+1):
            e=(k,l) if rho is None else rho.denominator*k+rho.numerator*l
            groups.setdefault(e,[]).append((k,l))
    rank=len(groups)
    per_site={}
    for r in range(a+1):
        for s in range(b+1):
            total=Fraction(0)
            for gl in groups.values():
                num=sum(kraw(a,k,r)*kraw(b,l,s) for k,l in gl)
                den=sum(comb(a,k)*comb(b,l) for k,l in gl)
                total+=Fraction(num*num,2**(a+b)*den)
            per_site[(r,s)]=total
    return rank,per_site

def direct(a,b,rho):
    # Explicit Walsh spectral-projector matrix using orthonormal eigenvectors.
    d=a+b;N=1<<d
    V=np.array([[(-1)**((i&j).bit_count()) for j in range(N)] for i in range(N)],dtype=float)/N**.5
    energies=[]
    for j in range(N):
        k=(j&((1<<a)-1)).bit_count()
        l=(j>>a).bit_count()
        en=(k,l) if rho is None else rho.denominator*k+rho.numerator*l
        energies.append(en)
    vals=list(dict.fromkeys(energies))
    P=np.zeros((N,N))
    for x in vals:
        ix=[i for i, en in enumerate(energies) if en==x]
        sp=V[:,ix]@V[0,ix]
        P+=np.outer(sp,sp)/np.inner(sp,sp)
    return len(vals),np.diag(P)

def run():
    tests=0; sites=0; maxdiff=0
    for a in range(1,5):
      for b in range(1,5):
        choices=[None,Fraction(1,1),Fraction(1,2),Fraction(2,1),Fraction(2,3),Fraction(3,2),Fraction(3,4),Fraction(4,3),Fraction(7,5)]
        for rho in choices:
          expected_rank=(a+1)*(b+1)
          if rho is not None and rho.numerator<=a and rho.denominator<=b:
              expected_rank-=(a+1-rho.numerator)*(b+1-rho.denominator)
          r,formula=theoretical(a,b,rho)
          dr,vals=direct(a,b,rho)
          assert r==expected_rank==dr,(a,b,rho,r,dr,expected_rank)
          for j in range(1<<(a+b)):
            h1=(j&((1<<a)-1)).bit_count()
            h2=(j>>a).bit_count()
            dif=abs(float(formula[h1,h2])-vals[j]);maxdiff=max(maxdiff,dif)
            assert dif<1.e-12,(a,b,rho,j,dif)
            sites+=1
          # exactly four bright sites unless resonant (then two).
          full=sum(comb(a,h1)*comb(b,h2) for (h1,h2),v in formula.items() if v==1)
          expected_full=2 if rho is not None and rho.numerator<=a and rho.denominator<=b else 4
          assert full==expected_full,(a,b,rho,full,expected_full)
          tests+=1
    print('PASS direct Walsh-projector comparisons:',tests,'parameter cases,',sites,'sites, max discrepancy',format(maxdiff,'.3g'))
    print('PASS rank deficiency and all-site full-capture threshold for all tested cases')
    print('sample a=2 b=3:')
    for rho in [None,Fraction(1),Fraction(1,2),Fraction(2,1),Fraction(2,3),Fraction(7,5)]:
       rk,m=theoretical(2,3,rho)
       print('rho=',str(rho),'rank=',rk,'average=',f'{rk}/32','full-sites=',sum(comb(2,r)*comb(3,s) for (r,s),p in m.items() if p==1))
if __name__=='__main__': run()
