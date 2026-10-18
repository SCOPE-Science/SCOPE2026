"""Standalone finite checks for Bernoulli first-chaos multiplier endpoint norms.

The proof is analytic; this file checks finite rational/complex examples only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def rational_row(a, c, x):
    n = len(a)
    ans = F(0)
    for y in product((0, 1), repeat=n):
        weight = F(1)
        kernel = F(0)
        for i in range(n):
            weight *= a[i] if y[i] else (1-a[i])
            chi_prod = ((F(x[i])-a[i]) * (F(y[i])-a[i])) / (a[i]*(1-a[i]))
            kernel += c[i] * chi_prod
        ans += weight * abs(kernel)
    return ans


def predicted(a, c):
    return rational_row(a, c, (1,)*len(a))


def homogeneous(n, a):
    k = (n*a.numerator)//a.denominator
    return 2*n*(1-a)*comb(n-1,k)*a**k*(1-a)**(n-1-k)


def complex_row(a, c, x):
    ans=0.0
    for y in product((0,1), repeat=len(a)):
        w=1.0
        z=0j
        for i in range(len(a)):
            w*=float(a[i] if y[i] else 1-a[i])
            z+=c[i]*(x[i]-float(a[i]))*(y[i]-float(a[i]))/float(a[i]*(1-a[i]))
        ans+=w*abs(z)
    return ans


def run_checks():
    a_all=[F(1,2),F(1,3),F(1,4),F(2,5),F(1,6),F(2,7)]
    c_all=[F(2),F(-3),F(1),F(4),F(0),F(-2)]
    rational=0
    for n in range(1,7):
        a=a_all[:n]
        c=c_all[:n]
        m=predicted(a,c)
        for x in product((0,1),repeat=n):
            assert rational_row(a,c,x)<=m,(n,x)
            rational+=1
    homogeneous_tested=0
    for a in [F(1,2),F(1,3),F(1,5),F(2,5),F(1,10)]:
        for n in range(1,13):
            v=predicted([a]*n,[F(1)]*n)
            target=homogeneous(n,a)
            assert v==target,(n,a,v,target)
            homogeneous_tested+=1
    coeff=[1+2j,-2+1j,3-0.5j,-2-1j,0.4+3j]
    complex_tested=0
    for n in range(1,6):
        aa=a_all[:n]
        best=complex_row(aa,coeff[:n],(1,)*n)
        for x in product((0,1),repeat=n):
            assert complex_row(aa,coeff[:n],x)<=best+1e-10,(n,x)
            complex_tested+=1
    print('PASS: exact rational row inequalities:',rational)
    print('PASS: homogeneous closed forms:',homogeneous_tested)
    print('PASS: complex-valued row comparisons:',complex_tested)
    print('Finite checks do not prove the universal theorem or asymptotic limits.')


if __name__=='__main__':
    run_checks()
