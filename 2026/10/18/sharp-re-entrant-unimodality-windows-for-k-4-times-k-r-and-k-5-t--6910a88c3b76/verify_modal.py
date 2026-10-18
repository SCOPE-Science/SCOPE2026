"""Exact integer checks of symbolic coefficient formula, signs and sharp modal windows."""
from math import comb, factorial

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def coeff(a,r):
    b=[1,a*r,C(a*r,2)]
    for k in range(3,max(a,r)+1):
        b.append(a*C(r,k)+r*C(a,k)+factorial(k)*C(a,k)*C(r,k)+C(a,2)*C(r,2)*C(4,k))
    return b

def unimodal(b):
    down=False
    for x,y in zip(b,b[1:]):
        if down and y>x:return False
        if y<x:down=True
    return True

cases=0
for a in (4,5):
    for r in range(3,501):
        b=coeff(a,r)
        expected=(r<=11 or r>=40) if a==4 else (r<=13 or r>=156)
        assert unimodal(b)==expected,(a,r)
        if a==4 and r>=5:
            assert b[5]-b[4]==4*(r-39)*C(r,4)//5-6*C(r,2)-r
        if a==5 and r>=6:
            assert b[6]-b[5]==5*(r-155)*C(r,5)//6-r
        cases+=1
    print('EXACT_MODAL_OK a=',a,' r=3..500')
for a,r,k in [(4,11,6),(4,12,6),(4,39,6),(4,40,6),(5,13,7),(5,14,7),(5,155,7),(5,156,7)]:
    b=coeff(a,r)
    print('BOUNDARY',a,r,'coeffs',[(j,b[j]) for j in range(k-2,k+1)])
print('CHECK_OK cases=',cases)
