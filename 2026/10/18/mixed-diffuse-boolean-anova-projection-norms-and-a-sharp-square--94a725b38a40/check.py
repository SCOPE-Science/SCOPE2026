#!/usr/bin/env python3
"""Independent finite checks for mixed continuous/Boolean ANOVA endpoint constants.

This verification script uses only Python's standard library; numerical limits
are checked at finite resolution, not treated as proofs.
"""
from fractions import Fraction
from itertools import product
from math import comb

def predicted(m, n, k):
    assert m >= 0 and n >= 0 and 0 <= k < m+n
    total=Fraction(0)
    for j in range(min(m,k)+1):
        avg=Fraction(0)
        for z in product([-1,1],repeat=n):
            e=[1]+[0]*n
            for val in z:
                for ell in range(n,0,-1):e[ell]+=val*e[ell-1]
            value=0
            for h in range(k-j+1):
                if h>m-j:continue
                sign=(-1)**h*comb(m-j,h)
                value+=sign*sum(e[ell] for ell in range(min(n,k-j-h)+1))
            avg+=abs(value)
        total+=comb(m,j)*avg/(2**n)
    return total

def finite_row(m,n,k,p):
    """Independent full Walsh-kernel row computation at atom probabilities p."""
    total=Fraction(0)
    for y in product((0,1),repeat=m+n):
        mass=Fraction(1)
        z=[]
        for i,yi in enumerate(y):
            pi=p if i<m else Fraction(1,2)
            mass*=pi if yi==1 else 1-pi
            xi=1 if i<m else 0
            z.append((int(yi==xi)/pi if xi==1 else int(yi==xi)/(1-pi))-1)
        e=[Fraction(1)]+[Fraction(0)]*k
        for zi in z:
            for j in range(k,0,-1):e[j]+=zi*e[j-1]
        total+=mass*abs(sum(e))
    return total

def run():
    count=0
    for m in range(5):
        for n in range(7):
            d=m+n
            for k in range(d):
                formula=predicted(m,n,k)
                if m==0:
                    assert formula==finite_row(m,n,k,Fraction(1,2))
                else:
                    v1=finite_row(m,n,k,Fraction(1,100))
                    v2=finite_row(m,n,k,Fraction(1,100000))
                    assert abs(v2-formula) <= abs(v1-formula)+Fraction(1,500000), (m,n,k,formula,v1,v2)
                    assert abs(v2-formula)<Fraction(20,100), (m,n,k,formula,v2)
                count+=1
    for m in range(1,21):
        for k in range(m):
            closed=sum(comb(m,j)*comb(m-j-1,k-j) for j in range(k+1))
            assert predicted(m,0,k)==closed
            count+=1
    for m in range(1,8):
        for n in range(8):
            if m+n>=2:
                signs=sum(Fraction(comb(n,b),2**n)*abs(1-m+(n-2*b)) for b in range(n+1))
                assert predicted(m,n,1)==m+signs
                count+=1
    print('PASS',count,'exact-rational or convergence-consistency cases')
if __name__=='__main__':run()
