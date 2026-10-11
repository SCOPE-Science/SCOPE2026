#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb

# Exact checker for the proof of the H_3(ell_3^2) formula.

def det_bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            assert j is not None
            A[k],A[j]=A[j],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
    return sign*A[-1][-1]

def resultant_at(r):
    # A(lambda)=a2 lambda^2+a1 lambda+a0 and B(lambda)=b4...+b0.
    a=[r**4-2*r**3-2*r+1, r**4+2*r**3-2*r-1, 2*r**2]
    b=[1-r, -2*r-2, 2*r**2, 2*r-2, r+1]
    ah=list(reversed(a)); bh=list(reversed(b))
    M=[]
    for sh in range(4):
        row=[0]*6
        for j,c in enumerate(ah): row[sh+j]=c
        M.append(row)
    for sh in range(2):
        row=[0]*6
        for j,c in enumerate(bh): row[sh+j]=c
        M.append(row)
    return det_bareiss(M)

def q4(r): return r**4+6*r**3+4*r**2+2*r-1
def q6(r): return r**6-4*r**5+5*r**4-8*r**3+7*r**2-4*r-1

def expected_res(r):
    return 2*(r-1)*(r*r+1)**4*q4(r)*q6(r)

# The Sylvester determinant and displayed factorization are polynomials in r
# of degree at most 24. Agreement at 25 distinct integers proves identity.
for rv in range(25):
    assert resultant_at(rv)==expected_res(rv)

# q4 is strictly increasing on [0,1] and changes sign once.
assert Fraction(q4(Fraction(1,4))) == Fraction(-39,256)
assert Fraction(q4(Fraction(3,10))) == Fraction(1301,10000)
# q4' = 4r^3+18r^2+8r+2 has positive coefficients.

# Verify the Bernstein representation of -q6 on [0,1].
bern=[Fraction(1),Fraction(5,3),Fraction(28,15),Fraction(2),Fraction(32,15),Fraction(8,3),Fraction(4)]
# Expand sum b_k*C(6,k) r^k(1-r)^(6-k).
coef=[Fraction(0) for _ in range(7)]
for k,bk in enumerate(bern):
    for j in range(6-k+1):
        coef[k+j]+=bk*comb(6,k)*comb(6-k,j)*((-1)**j)
# -q6 coefficients low-to-high: 1,4,-7,8,-5,4,-1
assert coef == list(map(Fraction,[1,4,-7,8,-5,4,-1]))
assert all(x>0 for x in bern)

# Boundary derivative: d/dr F(r,1) has numerator 3 r(r-1)(r^2+r+2),
# so the maximum on that edge is 1; symmetry gives the other edges.
# The unused source-reduction branch G is <=1: the two branch differences
# are concave quadratics in the smaller parameter and have nonnegative endpoint values.
# lambda>=r endpoints: 3 lambda(1-lambda), lambda(3lambda^2-2lambda+3).
# r>=lambda endpoints: 3 r(1-r), r(3r^2-2r+3).
for n in range(101):
    x=Fraction(n,100)
    assert 3*x*(1-x)>=0
    assert x*(3*x*x-2*x+3)>=0

# The diagonal critical point beats the boundary: for r<=3/10 the defect is
# r^2(2r^4-3r^2-6r+3), and the bracket decreases on [0,3/10]
# while its value at 3/10 is 4731/5000 > 0.
assert Fraction(2,1)*Fraction(3,10)**4-3*Fraction(3,10)**2-6*Fraction(3,10)+3 == Fraction(4731,5000)

# High-precision reconstruction of the unique q4 root and the final constant.
getcontext().prec=70
lo=Decimal(1)/Decimal(4); hi=Decimal(3)/Decimal(10)
def q4d(x): return x**4+Decimal(6)*x**3+Decimal(4)*x**2+Decimal(2)*x-Decimal(1)
for _ in range(240):
    mid=(lo+hi)/2
    if q4d(mid)<0: lo=mid
    else: hi=mid
t=(lo+hi)/2
z=(Decimal(1)+t**3)**2/(Decimal(8)*t**3+(Decimal(1)-t**2)**3)
# Newton cube root.
h=Decimal(1)
for _ in range(50): h=(Decimal(2)*h+z/(h*h))/Decimal(3)
assert abs(t-Decimal('0.27799674994077759064456505002871371522304436222532')) < Decimal('1e-50')
assert abs(h-Decimal('1.02906799244515340098771299410007133471425135949')) < Decimal('1e-48')
# Equivalent algebraic check for z=H_3^3.
poly=Decimal(512)*z**4-Decimal(384)*z**3-Decimal(480)*z**2+Decimal(400)*z-Decimal(91)
assert abs(poly)<Decimal('1e-55')
print('VERIFY_OK')
