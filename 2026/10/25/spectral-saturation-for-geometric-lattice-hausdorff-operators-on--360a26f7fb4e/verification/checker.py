"""Finite exact arithmetic checks for the Hausdorff-semigroup coefficient identities.
This diagnostic does not certify spectral or infinite-dimensional statements.
"""
from fractions import Fraction
from math import comb

def mat(t, n):
    return [[Fraction(comb(i,j))*t**j*(1-t)**(i-j) if j<=i else Fraction(0)
             for j in range(n)] for i in range(n)]

def mul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),Fraction(0))
             for j in range(n)] for i in range(n)]

def main():
    checks=0
    for t in [Fraction(1,2),Fraction(1,3),Fraction(2,3),Fraction(3,5)]:
        for n in range(3,18):
            a=mat(t,n)
            aa=mul(a,a)
            a2=mat(t*t,n)
            for i in range(n):
                for j in range(n):
                    assert aa[i][j]==a2[i][j]
                    checks+=1
            # The formal eigenvector f_k=z^k/(1-z)^(k+1) has coefficients binom(i,k).
            for k in range(n):
                for i in range(n):
                    lhs=sum((a[i][j]*comb(j,k) for j in range(k,i+1)),Fraction(0))
                    rhs=(t**k)*comb(i,k) if i>=k else Fraction(0)
                    assert lhs==rhs
                    checks+=1
            # For the measure delta_t+delta_(t^2), the matrix equals A+A^2.
            p=[[a[i][j]+aa[i][j] for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    assert p[i][j]==a[i][j]+a2[i][j]
                    checks+=1
    print(f"PASS: {checks} exact rational coefficient assertions")
if __name__=='__main__':
    main()
