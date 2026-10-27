#!/usr/bin/env python3
"""Exact arithmetic verification of the first quartic-egg Fefferman--Szego zero threshold.
Uses only the Python standard library. All tested dimensions comprise the theorem's
complete finite range; floating-point roots are not used for any certification.
"""
from fractions import Fraction as F
from math import comb, gcd, lcm
from functools import reduce

def rising(x, k):
    ans = F(1)
    for j in range(k):
        ans *= x + j
    return ans

def numerator(n):
    assert 2 <= n <= 11
    k = n-1
    mu = F(n+2, 2*(n+1))
    values = [rising(F(j,2)+mu,k) for j in range(k+1)]
    return [sum((-1)**(b-j)*comb(k+1,b-j)*values[j]
                for j in range(b+1)) for b in range(k+1)]

def cayley(p):
    k = len(p)-1
    # (1+t)^k P((1-t)/(1+t)): coefficient of t^d.
    return [sum(p[j]*sum((-1)**a*comb(j,a)*comb(k-j,d-a)
                for a in range(max(0,d-(k-j)),min(j,d)+1))
                for j in range(k+1)) for d in range(k+1)]

def primitive_positive_lead(q):
    d=reduce(lcm,(x.denominator for x in q),1)
    ints=[int(x*d) for x in q]
    g=reduce(gcd,(abs(x) for x in ints))
    ints=[x//g for x in ints]
    return [-x for x in ints] if ints[-1]<0 else ints

def bareiss_determinant(matrix):
    # Fraction-free Gaussian elimination over Z, with exact divisions.
    n=len(matrix)
    a=[list(map(int,row)) for row in matrix]
    prev=1
    sign=1
    for k in range(n-1):
        if a[k][k] == 0:
            for j in range(k+1,n):
                if a[j][k]:
                    a[k],a[j]=a[j],a[k]
                    sign=-sign
                    break
            else:
                return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=a[i][j]*pivot-a[i][k]*a[k][j]
                assert top%prev==0
                a[i][j]=top//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def hurwitz_signs(q):
    k=len(q)-1
    a=list(reversed(q))
    def a_at(idx):
        return a[idx] if 0<=idx<=k else 0
    signs=[]
    for size in range(1,k+1):
        matrix=[[a_at(2*col-row+1) for col in range(size)]
                for row in range(size)]
        D=bareiss_determinant(matrix)
        assert D!=0, ('singular Hurwitz minor', k, size)
        signs.append('+' if D>0 else '-')
    return ''.join(signs)

def routh_signs(q):
    k=len(q)-1
    a=list(reversed(q))
    width=(k+2)//2
    rows=[[F(a[2*j]) if 2*j<len(a) else F(0) for j in range(width)],
          [F(a[2*j+1]) if 2*j+1<len(a) else F(0) for j in range(width)]]
    assert rows[0][0]!=0 and rows[1][0]!=0
    for _ in range(2,k+1):
        u,v=rows[-2:]
        r=[(v[0]*(u[j+1] if j+1<width else 0)-u[0]*(v[j+1] if j+1<width else 0))/v[0]
           for j in range(width)]
        assert r[0]!=0
        rows.append(r)
    signs=''.join('+' if row[0]>0 else '-' for row in rows)
    variations=sum(signs[j]!=signs[j-1] for j in range(1,len(signs)))
    return signs,variations

EXPECTED={
 2:('+','++',0), 3:('++','+++',0),
 4:('+++','++++',0),5:('++++','+++++',0),
 6:('+++++','++++++',0),7:('++++++','+++++++',0),
 8:('+++++++','++++++++',0),9:('++++++++','+++++++++',0),
 10:('+++++++++','++++++++++',0),11:('+++++-----','++++++-++++',2)
}

def main():
    for n in range(2,12):
        p=numerator(n)
        k=n-1
        assert all((-1)**j*x>0 for j,x in enumerate(p))
        # Verify the rational generating-function numerator through k+5 terms.
        for d in range(k+6):
            coeff=sum(p[j]*comb(n+d-j-1,d-j) for j in range(min(k,d)+1))
            expected=rising(F(d,2)+F(n+2,2*(n+1)),k)
            assert coeff==expected,(n,d)
        q=primitive_positive_lead(cayley(p))
        assert len(q)==n and q[-1]>0
        h=hurwitz_signs(q)
        r,count=routh_signs(q)
        assert (h,r,count)==EXPECTED[n],(n,h,r,count)
        print(f'n={n}: Hurwitz {h}; Routh {r}; open-disk roots {count}')
    expected_q11=[1253826625536,24031676989440,217138391580672,
        1227061877391360,4848264135825408,14167589762055168,
        31520830021726464,53923972270029696,70091293939542360,
        65386761710460684,34205944490311243]
    assert primitive_positive_lead(cayley(numerator(11)))==expected_q11
    print('CHECK_OK: full n=2..11 exact Hurwitz and Routh certificates')

if __name__=='__main__':
    main()
