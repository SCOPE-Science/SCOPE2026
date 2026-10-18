#!/usr/bin/env python3
"""Exact-rational comparisons between weighted-cycle Mahler formulas and
independently triangulated primal and polar vertex hulls.
Dependencies: Python 3, NumPy, SciPy. Rational determinants use only stdlib.
"""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import factorial, prod
import numpy as np
from scipy.spatial import ConvexHull

def det(M):
    n = len(M)
    if n == 1:return M[0][0]
    if n == 2:return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))

def formula(a):
    n=len(a);d=n-1;tot=sum(a);vp=F(0);vq=F(0)
    for i in range(n):
        cnt=F(0)
        for s in product((-1,1),repeat=n-1):
            v=abs(sum(z*b for z,b in zip(s,a[:i]+a[i+1:])))
            cnt+=(1 if v<a[i] else F(1,2) if v==a[i] else 0)
        vp+=a[i]*cnt
    vp/=factorial(d)*prod(a)
    for mask in product((0,1),repeat=n):
        h=tot-2*sum(a[i]*mask[i] for i in range(n))
        if h>0:vq+=(-1)**sum(mask)*h**d
    vq/=factorial(d)
    return vp,vq

def hull_vertices(a):
    n=len(a);d=n-1
    pp=[]
    for i in range(n):
        vec=[F(int(j==i)-int(j==(i+1)%n),1)/a[i] for j in range(1,n)]
        pp.extend([vec,[-z for z in vec]])
    # dual coordinates consist of the first n-1 cyclic gradients;
    # convert to rooted potential coordinates by cumulative sums.
    qq=[]
    for signs in product((-1,1),repeat=d):
        u=[sgn*a[i] for i,sgn in enumerate(signs)]
        if abs(sum(u))<=a[-1]:
            qq.append([sum(u[:j]) for j in range(1,n)])
    for missing in range(d):
        for signslab in (-1,1):
            for signs in product((-1,1),repeat=d-1):
                u=[F(0)]*d;it=iter(signs)
                for i in range(d):
                    if i!=missing:u[i]=next(it)*a[i]
                u[missing]=-signslab*a[-1]-sum(u)
                if abs(u[missing])<=a[missing]:
                    qq.append([sum(u[:j]) for j in range(1,n)])
    qq=list(dict.fromkeys(tuple(v) for v in qq))
    return pp,qq

def exact_hull_volume(v):
    d=len(v[0]);a=np.array([[float(x) for x in row] for row in v]);h=ConvexHull(a)
    ans=F(0)
    for indices in h.simplices:
        M=[[v[i][j] for j in range(d)] for i in indices]
        ans+=abs(det(M))/factorial(d)
    return ans

def main():
    cases=[
      ['1','1','1'], ['1','1','1','1'],['1','1','1','1','1'],
      ['1/2','1','1'], ['3/4','1','1'],['1/2','1','1','1'],
      ['2/3','3/4','5/4','4/3'], ['1/2','4/5','11/10','5/4'],
      ['2/3','5/6','11/12','7/6','13/12'],
      ['1','1','1','1','1','1'],
      ['3/4','1','1','1','1','1'],
    ]
    for vals in cases:
        a=list(map(F,vals));p,q=formula(a);vp,vq=hull_vertices(a)
        ph=exact_hull_volume(vp);qh=exact_hull_volume(vq)
        assert p==ph,(vals,'primal',p,ph)
        assert q==qh,(vals,'polar',q,qh)
        print('PASS',','.join(vals),'primal',str(p),'polar',str(q),'Mahler',str(p*q))
    print('ALL EXACT WEIGHTED CYCLE MAHLER TESTS PASSED')
if __name__=='__main__':main()
