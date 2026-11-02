#!/usr/bin/env python3
"""Standalone checks of the stated cyclic TR-BDF2 endpoint formula.

Run: python3 verify.py
Only Python 3 standard library is needed. Finite tests supplement the proof.
"""
from fractions import Fraction
from math import sqrt, exp

checks = 0

def check(test, context):
    global checks
    checks += 1
    if not test:
        raise AssertionError(context)

class Qsqrt2:
    """Exact a+b*sqrt(2), a,b rational."""
    def __init__(self,a=0,b=0):
        self.a,self.b = Fraction(a),Fraction(b)
    def __add__(self,x):
        x=coerce(x);return Qsqrt2(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return Qsqrt2(-self.a,-self.b)
    def __sub__(self,x): return self+-coerce(x)
    def __rsub__(self,x): return coerce(x)+-self
    def __mul__(self,x):
        x=coerce(x);return Qsqrt2(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=coerce(x);den=x.a*x.a-2*x.b*x.b
        if den==0:raise ZeroDivisionError
        return self*Qsqrt2(x.a/den,-x.b/den)
    def __eq__(self,x):
        x=coerce(x);return self.a==x.a and self.b==x.b
    def __repr__(self):return f'{self.a}+({self.b})sqrt(2)'

def coerce(x):return x if isinstance(x,Qsqrt2) else Qsqrt2(x)

root2=Qsqrt2(0,1)
beta=root2-1
gamma=2-root2
c=1-root2/2
# Source stability function at gamma=2-sqrt(2):
# [2(2-gamma)+(1+(1-gamma)^2)z] /
# [2(2-gamma)(1-gamma*z/2)(1-(1-gamma)z/(2-gamma))].
check((1+(1-gamma)*(1-gamma))/(2*(2-gamma))==beta,'source numerator')
check(gamma/2==c,'first pole')
check((1-gamma)/(2-gamma)==c,'second pole')
check(beta/c==root2,'resolvent decomposition')
check(beta+gamma==1,'constant sum')

# Positivity proof for n <= 4: Q_4(t) >= P(t)/5, with
# P(t)=2-3t-3t²-3t³+15t⁴. On either half interval,
# its degree-four Bernstein coefficients are all positive.
from math import comb
p=[Fraction(2),Fraction(-3),Fraction(-3),Fraction(-3),Fraction(15)]

def poly_mul(p,q):
    result=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):result[i+j]+=a*b
    return result

def affine(p,a,b):
    out=[Fraction(0)]*len(p)
    for k,coef in enumerate(p):
        for j in range(k+1):
            out[j]+=coef*comb(k,j)*a**(k-j)*(b-a)**j
    return out

def bernstein4(p,a,b):
    coeff=affine(p,a,b)
    return [sum(coeff[k]*Fraction(comb(j,k),comb(4,k)) for k in range(j+1)) for j in range(5)]

left=bernstein4(p,Fraction(0),Fraction(1,2))
right=bernstein4(p,Fraction(1,2),Fraction(1))
check(left==list(map(Fraction,['2','13/8','9/8','13/32','5/16'])),'first half Bernstein')
check(right==list(map(Fraction,['5/16','7/32','3/4','11/4','8'])),'second half Bernstein')
for entry in left+right: check(entry>0,'Bernstein strict coefficient')
# sqrt(2) > 7/5 gives beta > 2/5 and gamma < 3/5.
check(Fraction(7,5)**2<2,'lower radical bound')
# The witness Q_5(3/5)=(7205sqrt2-10313)/3125<0
sample=Fraction(3,5)
q5=beta-gamma*sum(sample**j for j in range(1,5))+4*sample**5
check(q5==Qsqrt2(Fraction(-10313,3125),Fraction(7205,3125)),'five-cycle witness identity')
check(Fraction(10,7)**2>2,'upper radical bound')
check(Fraction(7205,1)*Fraction(10,7)<10313,'five-cycle witness strict negativity')

# Direct matrix calculation, not using Fourier transforms.
cf=1-1/sqrt(2)
bf=sqrt(2)-1

def mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def invert(A):
    n=len(A)
    t=[list(map(float,A[i]))+[1. if j==i else 0. for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=max(range(k,n), key=lambda i:abs(t[i][k]))
        t[k],t[pivot]=t[pivot],t[k]
        v=t[k][k]
        assert abs(v)>1e-15
        t[k]=[x/v for x in t[k]]
        for i in range(n):
            if i==k:continue
            v=t[i][k]
            t[i]=[t[i][j]-v*t[k][j] for j in range(2*n)]
    return [row[n:] for row in t]

for n in range(2,14):
    for h in (0.05,0.25,1.,2.,3.,5.,8.,20.,50.):
        S=[[1. if (j-i)%n==1 else 0. for j in range(n)] for i in range(n)]
        I=[[1. if i==j else 0. for j in range(n)] for i in range(n)]
        Q=[[S[i][j]-I[i][j] for j in range(n)] for i in range(n)]
        T=invert([[I[i][j]-cf*h*Q[i][j] for j in range(n)] for i in range(n)])
        T2=mul(T,T)
        P=mul([[I[i][j]+bf*h*Q[i][j] for j in range(n)] for i in range(n)],T2)
        t=cf*h/(1+cf*h)
        predicted=[]
        for r in range(n):
            v=(1-t)*t**r/(1-t**n)
            bracket=(1+sqrt(2))*(1-t)*(r+1+n*t**n/(1-t**n))-sqrt(2)
            predicted.append(v*bracket)
        for i in range(n):
            check(abs(sum(P[i])-1)<1e-10,(n,h,'row sum'))
            for j in range(n):
                check(abs(P[i][j]-predicted[(j-i)%n])<3e-10,(n,h,i,j,'entry formula'))
        check((min(predicted)>=-1e-11)==(predicted[0]>=-1e-11),(n,h,'minimum diagonal'))

# Numerical supplementary checks: two roots and negativity between them.
# Finite tests are not used to infer the number of roots for arbitrary n.
def polynomial(n,t):
    return bf-(2-sqrt(2))*sum(t**j for j in range(1,n))+(n-1)*t**n

def bisect(fn,a,b):
    fa=fn(a);fb=fn(b)
    assert fa*fb<0
    for _ in range(80):
        m=(a+b)/2;fm=fn(m)
        if fa*fm<=0:b=m;fb=fm
        else:a=m;fa=fm
    return (a+b)/2

for n in range(5,65):
    lo=bisect(lambda t:polynomial(n,t),0.3,0.6)
    hi=bisect(lambda t:polynomial(n,t),0.6,1-1e-8)
    check(lo<hi,(n,'root order'))
    check(polynomial(n,(lo+hi)/2)<-1e-12,(n,'negative interior'))
    check(polynomial(n,lo-.02)>0 if lo-.02>0 else True,(n,'positive left'))
    check(polynomial(n,(hi+1)/2)>0,(n,'positive right'))

print('PASS',checks,'assertions; exact radical/Bernstein checks and numerical matrix/root checks')
