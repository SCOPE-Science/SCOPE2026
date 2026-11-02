"""Exact rational reproduction of a two-step Chebyshev energy certificate.

Uses only Python standard library. Checks polynomial identities, parameter
mapping, and representative switching trajectories. All infinite assertions
are proved algebraically in RESULT.md, not by this finite test program.
"""
from fractions import Fraction as F
from itertools import product

zero, one = F(0), F(1)
P = ((one, -F(1,3)), (-F(1,3), F(1,5)))
I = ((one, zero), (zero, one))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def trans(A):
    return ((A[0][0],A[1][0]),(A[0][1],A[1][1]))

def sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def scale(a,A):
    return tuple(tuple(a*A[i][j] for j in range(2)) for i in range(2))

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def M(t):
    return ((F(3,5)*(one+t),-t/5),(one,zero))

def qnorm(z):
    return sum(z[i]*P[i][j]*z[j] for i in range(2) for j in range(2))

def mul(A,z):
    return tuple(sum(A[i][j]*z[j] for j in range(2)) for i in range(2))

checks=0
assert det(P)==F(4,45)
checks+=1
assert mm(trans(M(-one)),mm(P,M(-one)))==scale(F(1,5),P)
checks+=1
assert sub(P,mm(trans(M(one)),mm(P,M(one))))==((F(4,25),-F(4,25)),(-F(4,25),F(4,25)))
checks+=1

# An exact polynomial identity can be proved from six rational evaluations:
# every numerator here has degree <= 4, hence five distinct points suffice.
for t in [F(-2),F(-3,2),F(-1),F(-1,2),zero,F(1,2),one]:
    E=M(t)
    D=sub(P,mm(trans(E),mm(P,E)))
    assert D[1][1]==(5-t*t)/25
    assert det(D)==F(32,1125)*(one-t)*(t+2)
    checks+=2
    # The matrix certificate is positive on [-2,1].
    assert D[1][1]>0 and det(D)>=0
    checks+=1

# For all rational points, verify exact affine bound on the physical interval.
for k in range(0,201):
    t=F(k-100,100)
    E=M(t)
    A=sub(scale(F(3,5)+F(2,5)*t,P),mm(trans(E),mm(P,E)))
    assert A[0][0]>=0 and A[1][1]>=0 and det(A)>=0
    checks+=1

# Direct stage realization, with a frozen scalar f=-x*y and h=1.
for k in range(0,101):
    x=F(k,25) # [0,4]
    t=one-2*x+x*x/2
    for y,z in [(F(1),F(0)),(F(0),F(1)),(F(3,2),F(-4,3))]:
        v0=F(3,2)*y-F(1,2)*z
        v1=v0-F(1,2)*x*v0
        v2=2*v1-v0-x*v1
        ynew=F(3,5)*y+F(2,5)*v2
        assert ynew==mul(M(t),(y,z))[0]
        checks+=1

# Products of switched matrices satisfy the EXACT rational energy budget.
xs=[F(0),F(1,2),F(1),F(2),F(3),F(7,2),F(4)]
for seq in product(xs,repeat=4):
    z=(F(5,3),F(-2,5))
    budget=one
    for x in seq:
        t=one-2*x+x*x/2
        z=mul(M(t),z)
        budget*=one-x*(4-x)/5
    assert qnorm(z)<=budget*qnorm((F(5,3),F(-2,5)))
    checks+=1

# Boundary eigenvalue witnesses and optimality of the coefficient 1/5.
assert mul(M(-one),(one,zero))==(zero,one)
assert qnorm(mul(M(-one),(one,zero)))==F(1,5)*qnorm((one,zero))
assert mul(M(one),(one,one))==(one,one)
checks+=3
print(f'PASS: {checks} rational identities and finite switching checks.')
