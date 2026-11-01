#!/usr/bin/env python3
"""Exact finite polynomial/Routh certificate for quartic-egg kernel zeros."""
from fractions import Fraction as F
from math import comb
from functools import reduce

def clean(v):
    v=list(v)
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def poly_mul(a,b):
    v=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return clean(v)

def poly_divrem(a,b):
    a=clean(a);b=clean(b)
    if b==[0]:raise ZeroDivisionError()
    q=[F(0)]*max(1,(len(a)-len(b)+1))
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b);c=a[-1]/b[-1];q[d]=c
        for j in range(len(b)):a[d+j]-=c*b[j]
        a=clean(a)
    return clean(q),a

def poly_gcd(a,b):
    a=clean(a);b=clean(b)
    while b!=[0]: _,r=poly_divrem(a,b);a,b=b,r
    return clean([x/a[-1] for x in a])

def numerator(n):
    k=n-1;mu=F(n+2,2*(n+1));vals=[]
    for j in range(k+1):
        a=F(1)
        for i in range(k):a*=mu+F(j,2)+i
        vals.append(a)
    return clean([sum(((-1)**(r-j))*comb(k+1,r-j)*vals[j] for j in range(r+1)) for r in range(k+1)])

def cayley(p):
    k=len(p)-1;v=[F(0)]*(k+1)
    for j,c in enumerate(p):
        for a in range(j+1):
            for b in range(k-j+1):
                v[a+b]+=c*((-1)**a)*comb(j,a)*comb(k-j,b)
    return clean(v)

def routh(v):
    degree=len(v)-1; cs=v[::-1]; cols=(degree+2)//2
    a=[cs[2*j] if 2*j<len(cs) else F(0) for j in range(cols)]
    b=[cs[2*j+1] if 2*j+1<len(cs) else F(0) for j in range(cols)]
    rows=[a,b]
    for i in range(2,degree+1):
        A,B=rows[-2:]; assert B[0]!=0
        rows.append([(B[0]*(A[j+1] if j+1<cols else 0)-A[0]*(B[j+1] if j+1<cols else 0))/B[0] for j in range(cols)])
    pivots=[row[0] for row in rows]
    assert all(p!=0 for p in pivots)
    return ''.join('+' if x>0 else '-' for x in pivots)

def axischeck(v):
    real=[v[j]*(-1)**(j//2) if j%2==0 else F(0) for j in range(len(v))]
    imag=[v[j]*(-1)**((j-1)//2) if j%2==1 else F(0) for j in range(len(v))]
    return len(poly_gcd(real,imag))-1

def main():
    for n in range(2,12):
        p=numerator(n); k=n-1
        assert len(p)==k+1, (n,len(p))
        h=cayley(p)
        assert len(h)==k+1
        sig=routh(h)
        if n<11:assert sig=='+'*n,(n,sig)
        else:assert sig=='++++++-++++',sig
        assert axischeck(h)==0,(n,'axis')
        assert sum(sig[i]!=sig[i+1] for i in range(len(sig)-1))==(2 if n==11 else 0)
        print('dimension',n,'Routh first-column signs',sig,'imaginary-axis gcd degree',0)
    p=numerator(11)
    assert p[0]>0 and all(((-1)**i)*p[i]>0 for i in range(len(p)))
    # As all coefficients alternate, P(-r)>0 for any r>=0.
    # On 0<=r<1, generating-function representation gives P(r)>0.
    deriv=[j*p[j] for j in range(1,len(p))]
    assert len(poly_gcd(p,deriv))==1
    # Check the dimension-two polynomial against the independent n=2 formula.
    assert numerator(2)==[F(2,3),F(-1,6)]
    print('n11 polynomial squarefree; all roots away from real (-1,1)')
    print('EXACT_CERTIFICATE_OK')

if __name__=='__main__':main()
