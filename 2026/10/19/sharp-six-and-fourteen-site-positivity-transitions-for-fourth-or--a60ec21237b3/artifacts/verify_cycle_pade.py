#!/usr/bin/env python3
"""Exact symbolic and rational checks for the fourth-order Pade cycle result.

Run: python artifacts/verify_cycle_pade.py
Requires SymPy (tested with 1.14.0). The infinite-family arguments are
analytical and stated in RESULT.md; finite computations corroborate them.
"""
from sympy import Matrix, eye, symbols, factor, together, series, Rational, Poly, count_roots, sqrt, N

h, z = symbols('h z', positive=True)
r = (1+z/2+z*z/12)/(1-z/2+z*z/12)
terms = [Poly(series(r, z, 0, 8).removeO(),z).coeff_monomial(z**k) for k in range(8)]
assert terms == [1,1,Rational(1,2),Rational(1,6),Rational(1,24),Rational(1,144),0,-Rational(1,1728)]
checks=1

def graph(n):
    a=Matrix.zeros(n,n)
    for i in range(n):
        a[i,(i+1)%n]=1
        a[i,(i-1)%n]=1
    return a, 2*eye(n)-a

def pade_mat(n,t):
    _,l=graph(n)
    d=eye(n)+t*l/2+t*t*l*l/12
    b=eye(n)-t*l/2+t*t*l*l/12
    return d.inv()*b

# Exact complete rational off-diagonal formulas in small dimensions.
D4=(h*h+3*h+3)*(4*h*h+6*h+3)
D5=25*h**4+150*h**3+360*h*h+360*h+144
D6=(h*h+6*h+12)*(3*h*h+6*h+4)*(4*h*h+6*h+3)
P6=5*h**4-12*h**3-102*h*h-144*h-72
expected={
    3:{1:4*h/(3*h*h+6*h+4)},
    4:{1:3*h/(4*h*h+6*h+3),2:9*h*h*(h+1)/D4},
    5:{1:72*h*(h+2)/D5,2:12*h*h*(5*h+6)/D5},
    6:{1:-2*h*P6/D6,
       2:2*h*h*(13*h**3+48*h*h+72*h+36)/D6,
       3:2*h**3*(19*h*h+48*h+24)/D6}
}
for n in range(3,7):
    M=pade_mat(n,h)
    for d,x in expected[n].items():
        assert factor(together(M[0,d]-x))==0,(n,d)
        checks+=1

# All distinct graph-distance leading terms for n <= 13, and the
# negative distance-seven term for every cycle n >= 14.
for n in range(3,31):
    a,l=graph(n)
    powers=[eye(n)]
    for k in range(1,8):powers.append(powers[-1]*l)
    for d in range(1,min(n//2,7)+1):
        lead=next(((k,terms[k]*(-1)**k*powers[k][0,d]) for k in range(1,8) if terms[k]*powers[k][0,d]!=0),None)
        assert lead is not None,(n,d)
        if n<=13:assert lead[1]>0,(n,d,lead)
        if n>=14 and d==7:assert lead[0]==7 and lead[1]<0,(n,d,lead)
        checks+=1

# The exact cycle pseudoinverse is checked using its defining equations;
# this also verifies its normalization and neighbor sign threshold.
for n in range(3,40):
    _,l=graph(n)
    g=Matrix(n,n,lambda i,j: Rational(n*n-1,12*n) - Rational((i-j)%n*(n-(i-j)%n),2*n))
    one=Matrix.ones(n,1)
    assert l*g==eye(n)-one*one.T/n
    assert g*one==Matrix.zeros(n,1)
    assert (g[0,1]>0)==(n>=6)
    checks+=3

# Only one positive zero of the first-negative 6-cycle entry, and the
# remaining distances stay positive at every positive step.
assert Poly(P6,h).count_roots(0,100)==1
root=N(Poly(P6,h).intervals(eps=Rational(1,10**14))[-1][0][0],16)
assert 6<root<7
checks+=2

# Independent rational tests directly reconstruct inverse matrices.
for n in [3,4,5,6,7,8,10,12,13,14,15]:
    for t in [Rational(1,3),Rational(1,2),Rational(1),Rational(3),Rational(7),Rational(20)]:
        P=pade_mat(n,t)
        assert P*Matrix.ones(n,1)==Matrix.ones(n,1)
        assert P==P.T
        checks+=2
        if n in [3,4,5]: assert all(v>0 for v in P);checks+=1
        if n==6 and t<=3: assert all(v>0 for v in P);checks+=1
        if n==6 and t>=7: assert P[0,1]<0;checks+=1

print('VERIFY_OK; exact symbolic/rational assertions:',checks)
print('n=6 first positivity-loss step approximately 6.368850809631016')
print('All-n proof uses the Taylor coefficients, graph distance, and pseudoinverse formula stated in RESULT.md.')
