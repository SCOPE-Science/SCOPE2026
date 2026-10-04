#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def covariance_enum(N):
    k=N-1
    count=0
    sums=[0]*k
    prods=[[0]*k for _ in range(k)]
    for p in permutations(range(N)):
        count+=1
        d=[int(p[i]>p[i+1]) for i in range(k)]
        for i in range(k):
            sums[i]+=d[i]
            for j in range(k):
                prods[i][j]+=d[i]*d[j]
    means=[Fraction(s,count) for s in sums]
    return [[Fraction(prods[i][j],count)-means[i]*means[j] for j in range(k)] for i in range(k)],count

def invA(k):
    den=fib(2*(k+1))
    return [[Fraction(fib(2*(min(i,j)+1))*fib(2*(k-max(i,j))),den) for j in range(k)] for i in range(k)]

def run():
    perms_checked=0
    covariance_entries=0
    for N in range(2,9):
        C,nperm=covariance_enum(N)
        perms_checked+=nperm
        k=N-1
        for i in range(k):
            for j in range(k):
                expected=Fraction(1,4) if i==j else Fraction(-1,12) if abs(i-j)==1 else Fraction(0)
                assert C[i][j]==expected
                covariance_entries+=1

    determinant_checks=2
    dm2,dm1=1,3
    assert dm2==fib(2) and dm1==fib(4)
    for k in range(2,81):
        d=3*dm1-dm2
        assert d==fib(2*k+2)
        determinant_checks+=1
        dm2,dm1=dm1,d

    inverse_product_checks=0
    positive_precision_checks=0
    partial_square_checks=0
    for k in range(1,81):
        B=invA(k)
        for i in range(k):
            for j in range(k):
                s=3*B[i][j]
                if i>0:
                    s-=B[i-1][j]
                if i+1<k:
                    s-=B[i+1][j]
                assert s==(1 if i==j else 0)
                inverse_product_checks+=1
                assert B[i][j]>0
                positive_precision_checks+=1
        for i0 in range(k):
            for j0 in range(i0+1,k):
                i,j=i0+1,j0+1
                lhs=Fraction(B[i0][j0]**2,B[i0][i0]*B[j0][j0])
                rhs=Fraction(fib(2*i)*fib(2*(k-j+1)),fib(2*j)*fib(2*(k-i+1)))
                assert lhs==rhs and B[i0][j0]>0
                partial_square_checks+=1

    print(
        "VERIFY_OK "
        f"permutations_checked={perms_checked} "
        f"covariance_entries={covariance_entries} "
        f"determinant_checks={determinant_checks} "
        f"inverse_product_checks={inverse_product_checks} "
        f"positive_precision_checks={positive_precision_checks} "
        f"partial_square_checks={partial_square_checks}"
    )

if __name__=="__main__":
    run()
