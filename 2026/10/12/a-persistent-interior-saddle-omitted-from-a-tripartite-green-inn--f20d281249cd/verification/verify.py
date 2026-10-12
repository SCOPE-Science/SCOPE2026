#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt
a=Fraction(1,2); R=Fraction(4)
s1=f1=s2=f2=Fraction(1); d1=d2=Fraction(1,2)
C1=C2=l1=l2=Fraction(1); u1=Fraction(3); u2=Fraction(1); c0=Fraction(3,2)
x=y=z=Fraction(1,2)
assert (u1-u2)*y*z+u2-c0 == 0
assert (s1+f1)*x+(a*R-2*d1)*z+d1-C1-l1 == 0
assert (s2+f2)*x+((1-a)*R-2*d2)*y+d2-C2-l2 == 0
M=[[Fraction(0),Fraction(1),Fraction(1)],[Fraction(2),Fraction(0),Fraction(1)],[Fraction(2),Fraction(1),Fraction(0)]]
detM=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert detM == 4
J=[[v/Fraction(4) for v in row] for row in M]
assert sum(J[i][i] for i in range(3)) == 0
J2=[[sum(J[i][k]*J[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert sum(J2[i][i] for i in range(3)) == Fraction(5,8)
ev=[-0.25,(1.0-sqrt(17.0))/8.0,(1.0+sqrt(17.0))/8.0]
for lam in ev: assert abs(lam**3-(5.0/16.0)*lam-1.0/16.0)<1e-12
assert ev[0]<0 and ev[1]<0 and ev[2]>0 and abs(sum(ev))<1e-12
print("VERIFY_OK")
