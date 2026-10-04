from fractions import Fraction
from itertools import combinations
from math import prod


def check_box(a, x):
    n=len(a)
    V=prod(a)
    M=(2**(n-1))*V
    C=(2**(n-2))*V
    mean=sum(x,Fraction(0))/n
    den=2*M*sum((t-mean)**2 for t in x)
    num=4*C*sum((x[i]-x[j])**2 for i,j in combinations(range(n),2))
    rhs=n*den
    assert num==rhs, (a,x,num,rhs)
    return num,den

cases=[
    ([1,1],[Fraction(0),Fraction(1)]),
    ([2,3,5],[Fraction(1),Fraction(-2),Fraction(4)]),
    ([1,2,4,7],[Fraction(3,2),Fraction(-1,3),Fraction(5,4),Fraction(7,5)]),
    ([2,3,5,7,11],[Fraction(i*i-3*i+1, i+1) for i in range(5)]),
]
for a,x in cases:
    num,den=check_box(a,x)
    if den:
        assert num/den==len(a)
print('VERIFY_OK exact box Rayleigh identity in dimensions', [len(a) for a,_ in cases])
