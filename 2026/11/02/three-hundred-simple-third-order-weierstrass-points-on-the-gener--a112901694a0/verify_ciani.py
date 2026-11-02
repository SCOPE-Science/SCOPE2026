#!/usr/bin/env python3
"""Dependency-free finite-field certificate for generic Ciani quartic Wronskians.
Run with Python 3.11+. All arithmetic is exact in F_1009, a = 1.
The accompanying proof explains how this modular nonvanishing witness
implies a nonempty Zariski-open statement in characteristic zero.
"""
PRIME = 1009
PARAMETER = 1
SERIES_LENGTH = 10

def add(u, v):
    return [(a+b)%PRIME for a,b in zip(u,v)]

def mul(u, v):
    n=len(u); result=[0]*n
    for i,ui in enumerate(u):
        if ui:
            for j in range(n-i):
                result[i+j]=(result[i+j]+ui*v[j])%PRIME
    return result

def power(u,k):
    result=[1]+[0]*(len(u)-1)
    for _ in range(k): result=mul(result,u)
    return result

def curve_series(x, y):
    xs=mul(x,x); ys=mul(y,y)
    return add(add(add(mul(xs,xs),mul(ys,ys)),[1]+[0]*(len(x)-1)),
               add(add(mul(xs,ys),xs),ys))

def determinant_mod(matrix):
    matrix=[row[:] for row in matrix]
    n=len(matrix); result=1
    for j in range(n):
        pivot_row=next((i for i in range(j,n) if matrix[i][j]%PRIME),None)
        if pivot_row is None:return 0
        if pivot_row!=j:
            matrix[j],matrix[pivot_row]=matrix[pivot_row],matrix[j]
            result=-result
        pivot=matrix[j][j]%PRIME
        result=result*pivot%PRIME
        inv=pow(pivot,-1,PRIME)
        for i in range(j+1,n):
            factor=matrix[i][j]*inv%PRIME
            if factor:
                for k in range(j+1,n):
                    matrix[i][k]=(matrix[i][k]-factor*matrix[j][k])%PRIME
                matrix[i][j]=0
    return result%PRIME

MONOMIALS=[(i,d-i) for d in range(4) for i in range(d,-1,-1)]
assert len(MONOMIALS)==10

def wronskian_pair(x0,y0):
    n=SERIES_LENGTH
    x=[x0,1]+[0]*(n-2)
    y=[y0]+[0]*(n-1)
    fy=(4*y0**3+2*y0*(x0*x0+1))%PRIME
    if fy==0:return None
    fyinv=pow(fy,-1,PRIME)
    for i in range(1,n):
        y[i]=-curve_series(x,y)[i]*fyinv%PRIME
    assert curve_series(x,y)==[0]*n
    xs=[power(x,i) for i in range(4)]
    ys=[power(y,j) for j in range(4)]
    coefficient_rows=[[mul(xs[i],ys[j])[r] for i,j in MONOMIALS] for r in range(n)]
    U=(x0*x0+y0*y0+1)%PRIME
    B=x0*y0*(x0*x0-y0*y0)*(y0*y0-1)*(1-x0*x0)%PRIME
    if not U or not B:return None
    t=x0*x0*y0*y0*pow(U,-3,PRIME)%PRIME
    outputs=[]
    for width,exponent,upower in [(6,15,9),(10,45,33)]:
        det=determinant_mod([row[:width] for row in coefficient_rows[:width]])
        omega=det*pow(fy,exponent,PRIME)%PRIME
        q=omega*pow(B,-1,PRIME)*pow(U,-upower,PRIME)%PRIME
        outputs.append(q)
    return (t,*outputs)

def points_on_curve():
    roots={}
    for z in range(PRIME):roots.setdefault(z*z%PRIME,[]).append(z)
    half=pow(2,-1,PRIME)
    for x in range(PRIME):
        x2=x*x%PRIME
        b=(x2+1)%PRIME
        c=(x2*x2+x2+1)%PRIME
        discriminant=(b*b-4*c)%PRIME
        for sd in roots.get(discriminant,[]):
            y2=(-b+sd)*half%PRIME
            for y in roots.get(y2,[]):
                yield x,y

def polynomial_eval(coeff,t):
    result=0
    for v in reversed(coeff):result=(result*t+v)%PRIME
    return result

def interpolate(pairs,degree):
    size=degree+1
    rows=[[pow(t,j,PRIME) for j in range(size)]+[v] for t,v in pairs[:size]]
    for col in range(size):
        pivot=next((r for r in range(col,size) if rows[r][col]),None)
        assert pivot is not None
        rows[col],rows[pivot]=rows[pivot],rows[col]
        inv=pow(rows[col][col],-1,PRIME)
        rows[col]=[v*inv%PRIME for v in rows[col]]
        for r in range(size):
            if r!=col:
                factor=rows[r][col]
                if factor:
                    rows[r]=[(a-factor*b)%PRIME for a,b in zip(rows[r],rows[col])]
    return [row[-1] for row in rows]

def trim(coeff):
    c=coeff[:]
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def remainder(a,b):
    a=trim(a);b=trim(b)
    assert b!=[0]
    inverse=pow(b[-1],-1,PRIME)
    while a!=[0] and len(a)>=len(b):
        factor=a[-1]*inverse%PRIME
        offset=len(a)-len(b)
        for j in range(len(b)):
            a[j+offset]=(a[j+offset]-factor*b[j])%PRIME
        a=trim(a)
    return a

def gcd_polynomial(a,b):
    a=trim(a);b=trim(b)
    while b!=[0]: a,b=b,remainder(a,b)
    if a==[0]:return a
    inv=pow(a[-1],-1,PRIME)
    return [v*inv%PRIME for v in a]

def main():
    samples={}
    for x,y in points_on_curve():
        if not x*y:continue
        U=(x*x+y*y+1)%PRIME
        if not U:continue
        t=x*x*y*y*pow(U,-3,PRIME)%PRIME
        if t in samples:continue
        values=wronskian_pair(x,y)
        if values is None:continue
        assert values[0]==t
        samples[t]=(values[1],values[2],x,y)
        if len(samples)==35:break
    assert len(samples)==35
    observations=list(samples.items())
    p2=interpolate([(t,r[0]) for t,r in observations],3)
    p3=interpolate([(t,r[1]) for t,r in observations],11)
    assert p2==[353,959,322,857]
    assert p3==[879,326,508,141,914,387,343,133,815,401,47,498]
    for t,(w2,w3,x,y) in observations:
        assert polynomial_eval(p2,t)==w2,(x,y,'W2')
        assert polynomial_eval(p3,t)==w3,(x,y,'W3')
    assert p2[-1] and p3[-1]
    assert gcd_polynomial(p3,[(i*p3[i])%PRIME for i in range(1,len(p3))])==[1]
    assert gcd_polynomial(p2,p3)==[1]
    roots=[r for r in range(PRIME) if (r*r+2*PARAMETER*r+PARAMETER+2)%PRIME==0]
    assert roots==[54,953]
    branch=[0]+[r*pow(r+2,-3,PRIME)%PRIME for r in roots]
    assert branch==[0,889,270]
    assert len(set(branch))==3
    assert all(polynomial_eval(p3,t) for t in branch)
    print('field=F_1009 parameter=1 samples=35')
    print('P2 low-to-high:',p2)
    print('P3 low-to-high:',p3)
    print('finite branch t:',branch)
    print('P3 at branches:',[polynomial_eval(p3,t) for t in branch])
    print('first 12 points (t,x,y):',[(t,r[2],r[3]) for t,r in observations[:12]])
    print('degree(P3)=11, gcd(P3,P3prime)=gcd(P2,P3)=1')
    print('VERIFY_OK')

if __name__=='__main__': main()
