#!/usr/bin/env python3
"""Standalone exact finite checks for four-run Lyndon-factor enumerations.

Runs with Python 3 standard library only: python verify.py
Finite tests supplement, and do not replace, the general proofs in RESULT.md.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb


def is_lyndon(s):
    return all(s < s[i:] for i in range(1, len(s)))


def direct_spectrum(a, b, c, d):
    w = '0'*a + '1'*b + '0'*c + '1'*d
    distinct = {w[i:j] for i in range(len(w))
                for j in range(i+1,len(w)+1) if is_lyndon(w[i:j])}
    return Counter(map(len, distinct)), distinct


def structural_set(a, b, c, d):
    result = {'0', '1'}
    result |= {'0'*i+'1'*j for i in range(1,a+1) for j in range(1,b+1)}
    result |= {'0'*i+'1'*j for i in range(1,c+1) for j in range(1,d+1)}
    result |= {'0'*i+'1'*b+'0'*c+'1'*j
               for i in range(1,a+1) for j in range(1,d+1)
               if i>c or (i==c and j>b)}
    return result


def exact_count(a, b, c, d):
    return (2 + a*b + c*d - min(a,c)*min(b,d)
            + max(0,a-c)*d + (max(0,d-b) if a>=c else 0))


def compositions(n):
    for a in range(1,n-2):
        for b in range(1,n-a-1):
            for c in range(1,n-a-b):
                d=n-a-b-c
                yield a,b,c,d


def series_coefficients(max_n):
    # N(z)/D(z), with D(z)=(1-z)^6(1+z)^2.
    factors = [(-1)**k*comb(6,k) for k in range(7)]
    extra = [1,2,1]
    den = [sum(factors[k]*extra[j-k]
               for k in range(max(0,j-2),min(6,j)+1))
           for j in range(9)]
    assert den[0]==1
    numer = {4:3, 5:6, 6:-2, 8:2}
    q=[]
    for n in range(max_n+1):
        v=numer.get(n,0)
        v-=sum(den[j]*q[n-j] for j in range(1,min(n,8)+1))
        q.append(v)
    return q


def multiply_polys(a,b):
    p={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            p[(i+k,j+l)]=p.get((i+k,j+l),Q(0))+x*y
    return p


def integrate_rect(poly, x0,x1,y0,y1):
    return sum((v*(x1**(i+1)-x0**(i+1))/Q(i+1)
             *(y1**(j+1)-y0**(j+1))/Q(j+1))
             for (i,j),v in poly.items())


def check_dirichlet_moments():
    h=Q(1,2); zero=Q(0); one=Q(1)
    patches=[
      (zero,h,zero,h,{(0,0):Q(1),(1,0):Q(-1),(0,1):Q(-1),(1,1):Q(1)}),
      (zero,h,h,one,{(0,0):Q(1),(0,1):Q(-1),(1,0):Q(-2),(1,1):Q(3)}),
      (h,one,zero,h,{(1,1):Q(1),(1,0):Q(1),(0,1):Q(-1)}),
      (h,one,h,one,{(0,0):Q(-1),(1,0):Q(2),(0,1):Q(1),(1,1):Q(-1)})]
    moments=[]
    for power in (1,2):
        total=Q(0)
        for x0,x1,y0,y1,p in patches:
            p2=p if power==1 else multiply_polys(p,p)
            total+=integrate_rect(p2,x0,x1,y0,y1)
        moments.append(total)
    assert moments==[Q(9,16),Q(35,96)], moments
    mean=Q(1,5)*moments[0]
    second=Q(3,70)*moments[1]
    variance=second-mean*mean
    assert (mean,second,variance)==(Q(9,80),Q(1,64),Q(19,6400))
    return mean,variance


def main():
    checked=0
    for a,b,c,d in product(range(1,8), repeat=4):
        spectrum,actual=direct_spectrum(a,b,c,d)
        prescribed=structural_set(a,b,c,d)
        assert actual==prescribed, (a,b,c,d,actual^prescribed)
        assert spectrum==Counter(map(len,prescribed))
        assert len(actual)==exact_count(a,b,c,d)
        checked+=1
    coeff=series_coefficients(30)
    for n in range(4,31):
        counts={p:exact_count(*p) for p in compositions(n)}
        optimum=max(counts.values())
        optimizers={p for p,v in counts.items() if v==optimum}
        expected={p for p in compositions(n)
                  if p[1]==p[2]==1 and abs(p[0]-p[3])<=1}
        assert optimum==n*n//4-1,(n,optimum)
        assert optimizers==expected,(n,optimizers,expected)
        assert sum(counts.values())==coeff[n],n
    avg,var=check_dirichlet_moments()
    print('VERIFY_OK exact_length_spectra=%s extremal_and_generating_lengths=4..30 dirichlet_mean=%s dirichlet_variance=%s' %(checked,avg,var))

if __name__=='__main__':
    main()
