#!/usr/bin/env python3
from fractions import Fraction

# Exact arithmetic in Q(sqrt(3)): represent a+b*sqrt(3) by (a,b).
def add(x,y):
    return (x[0]+y[0], x[1]+y[1])
def scale(q,x):
    return (q*x[0], q*x[1])
def positive(x):
    a,b=x
    if b==0:
        return a>0
    if a>=0 and b>=0:
        return True
    if a<=0 and b<=0:
        return False
    if a>=0 and b<0:
        return a*a > 3*b*b
    return 3*b*b > a*a

checks=0
for n in range(3,201):
    A=Fraction(n**(2*n)-(n-1)*n**4)
    u=n-3
    den=u*u-3
    # x = r_n*sqrt(2) = A/(u+sqrt(3)).
    x=(Fraction(A*u,den), Fraction(-A,den))

    # Exact total-gap identity:
    # endpoint correction = x*sqrt(3)/2, interior correction = x.
    # 2*(x*sqrt(3)/2)+(n-3)*x = x*(sqrt(3)+n-3) = A.
    # Multiplication by sqrt(3): (a+b sqrt3)*sqrt3 = 3b+a sqrt3.
    x_sqrt3=(3*x[1],x[0])
    total_corr=add(x_sqrt3, scale(Fraction(n-3),x))
    assert total_corr==(A,Fraction(0)), (n,total_corr,A)

    # Every longer interval with r adjacent gaps has exact excess
    # E = r*n^4 - n^(2r+2) + (r-1)*x.
    for r in range(2,n-1):
        E=add((Fraction(r*n**4-n**(2*r+2)),Fraction(0)), scale(Fraction(r-1),x))
        assert positive(E), (n,r,E)
        checks+=1

    # The proof's key bound r_n*sqrt(2) > n^(2n-2).
    key=add(x,(-Fraction(n**(2*n-2)),Fraction(0)))
    assert positive(key), (n,key)

print(f"VERIFY_OK Sack-chain-poset-associahedron n=3..200 longer_interval_checks={checks} exact_Qsqrt3=yes")
