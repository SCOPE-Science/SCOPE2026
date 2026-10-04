from fractions import Fraction
from math import comb

def bin_tail(n,k,p):
    q=1-p
    return sum(Fraction(comb(n,j))*p**j*q**(n-j) for j in range(k,n+1))

def gap_direct(k,m,p):
    return bin_tail(2*k+m,k,p)-bin_tail(2*k+m+2,k+1,p)

def gap_formula(k,m,p):
    n=2*k+m
    q=1-p
    pk=Fraction(comb(n,k))*p**k*q**(n-k)
    if p in (0,1):
        return gap_direct(k,m,p)
    return pk*q*(q-Fraction(k,k+m+1)*p)

for k in range(1,9):
    for m in range(0,6):
        pstar=Fraction(k+m+1,2*k+m+1)
        tests=[Fraction(0),Fraction(1,3),pstar,(pstar+1)/2,Fraction(1)]
        for p in tests:
            d=gap_direct(k,m,p)
            f=gap_formula(k,m,p)
            assert d==f, (k,m,p,d,f)
        assert gap_direct(k,m,Fraction(1,3))>0
        assert gap_direct(k,m,pstar)==0
        assert gap_direct(k,m,(pstar+1)/2)<0
        assert pstar-Fraction(1,2)==Fraction(m+1,2*(2*k+m+1))
print('VERIFY_OK')
