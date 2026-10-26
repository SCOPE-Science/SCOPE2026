#!/usr/bin/env python3
"""Finite exact checks for the periodic linear-spline projector's endpoint norm.

The universal theorem is proved analytically in RESULT.md; this script tests finite instances.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def inverse_first_row(n):
    a = [[F(4 if i == j else (1 if (j - i) % n in (1, n-1) else 0)) for j in range(n)] + [F(i == 0)] for i in range(n)]
    for k in range(n):
        pivot = next(t for t in range(k,n) if a[t][k])
        a[k],a[pivot]=a[pivot],a[k]
        p=a[k][k]
        a[k]=[z/p for z in a[k]]
        for i in range(n):
            if i==k: continue
            z=a[i][k]
            if z: a[i]=[u-z*v for u,v in zip(a[i],a[k])]
    return [a[i][-1] for i in range(n)]


def segment(a,b):
    if a*b>=0:return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))


def norm_from_matrix(n):
    g=inverse_first_row(n)
    return 6*sum((segment(g[j],g[(j+1)%n]) for j in range(n)),F(0))


def run():
    checks=0
    reference={3:F(16,9),4:F(17,9),5:F(257,132),6:F(2923,1485),7:F(14659,7380),8:F(8083,4059)}
    with localcontext() as ctx:
        ctx.prec=75
        q=Decimal(2)-Decimal(3).sqrt()
        ce=(Decimal(3)*(Decimal(7)*q-1))/(Decimal(32)*Decimal(3).sqrt())
        for n in range(3,29):
            g=inverse_first_row(n)
            for j in range(n):
                z=4*g[j]+g[(j-1)%n]+g[(j+1)%n]
                assert z==F(j==0)
                checks+=1
            for j in range(n):
                assert g[j]==g[-j]
                checks+=1
            u=-q
            c=Decimal(1)/(Decimal(2)*Decimal(3).sqrt())
            for j in range(n):
                closed=c*(u**j+u**(n-j))/(1-u**n)
                direct=Decimal(g[j].numerator)/Decimal(g[j].denominator)
                assert abs(closed-direct)<Decimal('1e-65')
                checks+=1
            norm=norm_from_matrix(n)
            assert norm >1 and norm<2
            checks+=2
            if n in reference:
                assert norm==reference[n]
                checks+=1
            nd=Decimal(norm.numerator)/Decimal(norm.denominator)
            defect=Decimal(2)-nd
            assert ce*(q**(n//2))<defect<Decimal(4)*(q**(n//2))
            checks+=2
            if n%2==0:
                for j in range(n):
                    assert g[j]*g[(j+1)%n]<0
                    checks+=1
            else:
                m=n//2
                for j in range(n):
                    if j==m:assert g[j]*g[(j+1)%n]>0
                    else: assert g[j]*g[(j+1)%n]<0
                    checks+=1
    print('VERIFIED finite exact cases n=3..28; assertions:', checks)

if __name__=='__main__':run()
