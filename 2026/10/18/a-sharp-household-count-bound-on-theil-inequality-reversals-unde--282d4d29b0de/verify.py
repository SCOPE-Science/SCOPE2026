"""Exact integer verification of a uniform-grant Theil-ranking reversal."""
from math import prod

X = (1, 7, 25, 35)
Y = (2, 5, 29, 32)

def multiply_polynomial(coeff, b):
    result = [0]*(len(coeff)+1)
    for j,v in enumerate(coeff):
        result[j] += v*b
        result[j+1] += v
    return result

def polynomial(values):
    p=[1]
    for b in values:
        p=multiply_polynomial(p,b)
    return p

def exact_entropy_sign(x,y,t):
    """Sign of sum (x_i+t) log(x_i+t) minus corresponding y sum."""
    numerator=prod(pow(a+t,a+t) for a in x)
    denominator=prod(pow(b+t,b+t) for b in y)
    return (numerator>denominator)-(numerator<denominator)

assert sum(X)==sum(Y)==68
assert polynomial(X)==[6125,7420,1362,68,1]
assert polynomial(Y)==[9280,7106,1365,68,1]
assert [a-b for a,b in zip(polynomial(X),polynomial(Y))]==[-3155,314,-3,0,0]
assert [exact_entropy_sign(X,Y,t) for t in (0,20,40)]==[1,-1,1]
assert exact_entropy_sign(X,Y,5)==1
assert exact_entropy_sign(X,Y,6)==-1
assert exact_entropy_sign(X,Y,32)==-1
assert exact_entropy_sign(X,Y,33)==1
# Two simultaneous double roots are impossible since the derivative
# numerator is a nonzero quadratic. Three distinct value zeros would
# require three derivative zeros, using its limiting value zero at infinity.

# Independent sharpness check at three households.
U=(1,11,24); V=(2,9,25)
assert sum(U)==sum(V)==36
assert [exact_entropy_sign(U,V,t) for t in (0,20)]==[1,-1]
assert len([z for z in [a-b for a,b in zip(polynomial(U),polynomial(V))] if z!=0])<=2
print('PASS: coefficient identities; three exact sign certificates; two brackets; three-household sharpness.')
