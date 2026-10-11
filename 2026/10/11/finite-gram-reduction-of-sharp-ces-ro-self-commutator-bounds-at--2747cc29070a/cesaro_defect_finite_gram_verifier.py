"""Exact rational finite-column checks of generalized Cesaro identities.

This reproducibility check supplements the analytic argument: it does not
infer infinite-dimensional identities from finitely many tested cases.
"""
from fractions import Fraction as F
from math import comb, factorial, log


def rising(x,k):
    y=F(1)
    for j in range(k):y*=x+j
    return y


def falling(x,k):
    y=F(1)
    for j in range(k):y*=x-j
    return y


def H(m,t):return rising(t+1,m)
def D(m,t):return rising(t+m+1,m)

def Fpoly(m,x,z):
    return sum((-1)**q * F(factorial(m+q), factorial(q)**2*factorial(m-q-1))
               * falling(x,q)*rising(z+1,m-q-1) for q in range(m))

def p_poly(m,k,n,a):
    d=m-k-1
    return sum(F(comb(d,s))*rising(m+k+1,s)*rising(k+1-a,s)
               /rising(2*k+2,s)*rising(n+a+1,d-s) for s in range(d+1))

def coeff(m,k,a):
    w=F(2*k+1)*comb(m+k,2*k+1)**2*a
    for j in range(1,k+1):w*=a*a-j*j
    return w

def B_entry(m,i,j,a):
    t=j+a
    if i<=j+m-1:return Fpoly(m,i+a,t)/D(m,t)
    if i==j+m:return (-1)**m*H(m,t)/D(m,t)
    return F(0)

def M_entry(m,i,j,a):
    return (F(m)*rising(i-j+1,m-1)/rising(i+a+1,m)) if j<=i else F(0)

def L_entry(m,i,j,a):
    return rising(j+a+1,m)/factorial(m)*(-1)**(i-j)*comb(m,i-j) if j<=i<=j+m else F(0)

for m in (1,2,3,4):
    for a in (F(-1,2), F(0), F(1,2), F(1), F(3,2)):
        for i in range(6):
            ti=i+a
            ri=1-H(m,ti)/D(m,ti)
            vi=[p_poly(m,k,i,a)/D(m,ti) for k in range(m)]
            assert ri>0
            for j in range(6):
                tj=j+a
                vj=[p_poly(m,k,j,a)/D(m,tj) for k in range(m)]
                left=F(i==j)-sum(B_entry(m,z,i,a)*B_entry(m,z,j,a)
                                  for z in range(max(i,j)+m+1))
                right=(ri if i==j else F(0))+sum(
                    coeff(m,k,a)*vi[k]*vj[k] for k in range(m))
                assert left==right,(m,a,i,j,left,right)
        for j in range(4):
            for i in range(14):
                assert sum(M_entry(m,i,k,a)*L_entry(m,k,j,a)
                           for k in range(j,j+m+1))==F(i==j),(m,a,i,j)

# At order two, the closed digamma specialization at alpha=1/2 reduces
# to this exact rational-plus-logarithm value. The truncated positive sum
# must lie between it and a conservative integral tail bound.
a=.5;N=60000
S_N=sum(1/(2*(n+a+3)*(n+a+4)*(2*n+2*a+5)) for n in range(N))
c_closed=261/560+3*log(2)/4
c_partial=1-3*a*(1-a*a)*S_N
assert 0<c_partial-c_closed<1e-8
print('CESARO_ALL_ORDER_FINITE_GRAM_IDENTITIES_OK')
