"""Exact arithmetic checks for two-age seasonal-phase mixing. Python 3 stdlib."""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mat(a, b, c):
    return ((a,b),(c,F(0)))


def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))


def sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))


def scale(k,A):
    return tuple(tuple(k*A[i][j] for j in range(2)) for i in range(2))


def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def tr(A):
    return A[0][0]+A[1][1]


# Exhaustive exact samples across fecundities and admissible survival rates.
values = (F(1,3),F(1,2),F(1),F(2))
survival = (F(1,3),F(1,2),F(1))
tests = 0
for a,b,c,d,e,f in product(values,values,survival,values,values,survival):
    A,B=mat(a,b,c),mat(d,e,f)
    X,Y=mm(mm(A,A),B),mm(mm(A,B),A)
    j=det(sub(X,Y))
    formula= b*c*((b*f-c*e)**2+(a*e-b*d)*(c*d-a*f))
    assert j == formula
    assert tr(X)==tr(Y)
    assert det(X)==det(Y)==-(b*c)**2*e*f
    assert tr(X)==a*a*d+a*b*f+a*c*e+b*c*d
    for p in (F(0), F(1,4), F(1,3), F(1,2),F(2,3),F(3,4),F(1)):
        M=add(scale(p,X),scale(1-p,Y))
        assert det(M)==det(X)-p*(1-p)*j
        assert tr(M)==tr(X)
        # Discriminant positive: off-diagonals of the positive matrices are positive.
        disc=tr(M)**2-4*det(M)
        assert disc>0
        tests+=1

# Witness with survival probabilities no greater than one.
A=mat(F(1,2),F(1),F(1,2))
B=mat(F(1,2),F(3,2),F(1,4))
X,Y=mm(mm(A,A),B),mm(mm(A,B),A)
assert X==((F(1,2), F(9,8)),(F(1,4),F(3,8)))
assert Y==((F(5,8), F(1,2)),(F(1,2),F(1,4)))
assert tr(X)==F(7,8) and det(X)==F(-3,32) and det(sub(X,Y))==F(9,64)
assert tr(X)**2-4*det(X)==F(73,64)
M=scale(F(1,2),add(X,Y))
assert tr(M)**2-4*det(M)==F(82,64)
for p in (F(0),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(1)):
    E=add(scale(p,X),scale(1-p,Y))
    char_at_one=F(1)-tr(E)+det(E)
    assert char_at_one==F(2,64)-F(9,64)*p*(1-p)
    # det(E)<0, so char_at_one<0 iff Perron root >1.
    assert (char_at_one<0)==(p>F(1,3) and p<F(2,3))
print(f'PASS: {tests} exact rational mixture identities plus sharp interval witness')
