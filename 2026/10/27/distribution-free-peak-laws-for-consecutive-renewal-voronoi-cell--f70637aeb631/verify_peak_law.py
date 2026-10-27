from fractions import Fraction
from itertools import permutations
from math import factorial

expected_joint={1:Fraction(0),2:Fraction(1,36),3:Fraction(1,12),4:Fraction(1,16)}
expected_cov={1:Fraction(-1,16),2:Fraction(-5,144),3:Fraction(1,48),4:Fraction(0)}
checks=0
for k in range(1,5):
    N=k+4 # M0 gaps -2..1, Mk gaps k-2..k+1 => union -2..k+1 length k+4
    totals=[0,0,0]
    for a in permutations(range(N)):
        def peak(i):return a[i+2]>a[i] and a[i+1]>a[i+3]
        u=peak(0);v=peak(k)
        totals[0]+=u;totals[1]+=v;totals[2]+=u and v
    p,q,j=(Fraction(x,factorial(N)) for x in totals)
    assert p==q==Fraction(1,4)
    assert j==expected_joint[k],(k,j)
    assert j-p*q==expected_cov[k]
    checks+=4
    print(k,N,j,j-p*q)
for n in range(1,7):
    N=n+3
    e=0;e2=0
    for a in permutations(range(N)):
        c=sum(a[i+2]>a[i] and a[i+1]>a[i+3] for i in range(n))
        e+=c;e2+=c*c
    mean=Fraction(e,factorial(N)); v=Fraction(e2,factorial(N))-mean*mean
    assert mean==Fraction(n,4)
    stated={1:Fraction(3,16),2:Fraction(1,4),3:Fraction(35,144)}.get(n,Fraction(5*(n+4),144))
    assert v==stated, (n,v,stated)
    checks+=2
    print('n',n,'mean',mean,'var',v)
print('verified comparisons:',checks)
