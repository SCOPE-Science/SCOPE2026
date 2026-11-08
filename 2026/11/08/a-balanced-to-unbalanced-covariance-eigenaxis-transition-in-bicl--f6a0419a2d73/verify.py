#!/usr/bin/env python3
"""Exact moment and spectral consistency checks for complete-bipartite stable-set polytopes."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt
import numpy as np

def check(p,q):
    n=p+q
    verts=[]
    for bits in product((0,1),repeat=p):
        verts.append(tuple(bits)+(0,)*q)
    for bits in product((0,1),repeat=q):
        if any(bits):
            verts.append((0,)*p+tuple(bits))
    N=2**p+2**q-1
    assert len(verts)==N and len(set(verts))==N
    av=[sum(v[i] for v in verts)*Q(1,N) for i in range(n)]
    cov=[[sum(Q(v[i]*v[j],N) for v in verts)-av[i]*av[j] for j in range(n)] for i in range(n)]
    a=Q(2**(p-1),N); b=Q(2**(q-1),N)
    pred=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i<p and j<p: row.append((a/2 if i==j else 0)+a/2-a*a)
            elif i>=p and j>=p: row.append((b/2 if i==j else 0)+b/2-b*b)
            else: row.append(-a*b)
        pred.append(row)
    assert cov==pred
    L11=a/2+p*(a/2-a*a)
    L22=b/2+q*(b/2-b*b)
    lam_plus=(float(L11)+float(L22)+sqrt(float((L11-L22)**2)+4*p*q*float(a*b)**2))/2
    lam_minus=(float(L11)+float(L22)-sqrt(float((L11-L22)**2)+4*p*q*float(a*b)**2))/2
    expect=sorted([lam_plus,lam_minus]+[float(a/2)]*(p-1)+[float(b/2)]*(q-1))
    eigen=np.linalg.eigvalsh(np.array(cov,dtype=float))
    assert np.allclose(eigen,expect,rtol=2e-11,atol=2e-11),(p,q,eigen,expect)
    assert lam_plus>max(float(a/2),float(b/2))
    if p==q:
        assert lam_minus<float(a/2)-1e-12
        assert Q(2**(p-1),N)*Q(p+1,2)==Q.from_float(lam_plus).limit_denominator(10**7) if p<6 else True
    elif p>q:
        assert lam_minus>float(b/2)
    else:
        assert lam_minus>float(a/2)
    return N

def main():
    count=0; vertices=0
    for p in range(2,8):
        for q in range(2,8):
            vertices+=check(p,q);count+=1
    print('BICLIQUE_VERTEX_COVARIANCE_CHECKS_PASSED profiles=',count,'vertices=',vertices)
if __name__=='__main__': main()
