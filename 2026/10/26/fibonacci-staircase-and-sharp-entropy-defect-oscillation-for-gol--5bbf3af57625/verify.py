#!/usr/bin/env python3
"""Exact Q(sqrt(5)) gap-split audit of the golden-rotation ordinal theorem.
No external packages; finite checks supplement the all-n proof in RESULT.md.
"""
import math

# Pair (a,b) encodes a+b*alpha, alpha=(sqrt(5)-1)/2.
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def cmp0(x):
    a,b=x;u=2*a-b
    if b==0:return (u>0)-(u<0)
    if b>0:
        if u>=0:return 1
        z=5*b*b-u*u
        return (z>0)-(z<0)
    if u<=0:return -1
    z=u*u-5*b*b
    return (z>0)-(z<0)
def compare(x,y):return cmp0(sub(x,y))
def times_alpha(x):
    a,b=x
    return b,a-b

alpha=(math.sqrt(5)-1)/2
powers=[(1,0),(0,1)]
for _ in range(40):powers.append(times_alpha(powers[-1]))
def as_float(x):return x[0]+alpha*x[1]
def fract(n):
    k=math.floor(n*alpha)
    v=(-k,n)
    while cmp0(v)<0:
        k-=1;v=(-k,n)
    while cmp0(sub(v,(1,0)))>=0:
        k+=1;v=(-k,n)
    return v

fib=[0,1,1]
while fib[-1]<3000:fib.append(fib[-1]+fib[-2])
N=2000
sorted_points=[((0,0),0)]
counts={};maxerr=0.0
for n in range(1,N+1):
    t=fract(n)
    low,high=0,len(sorted_points)
    while low<high:
        mid=(low+high)//2
        if compare(sorted_points[mid][0],t)<0:low=mid+1
        else:high=mid
    j=low
    lo=sorted_points[j-1][0] if j else sub(sorted_points[-1][0],(1,0))
    hi=sorted_points[j][0] if j<len(sorted_points) else add(sorted_points[0][0],(1,0))
    lengths=[sub(t,lo),sub(hi,t)]
    m=2
    while fib[m+1]<=n:m+=1
    assert fib[m]<=n<fib[m+1],(n,m)
    expect={powers[m-1],powers[m]}
    assert set(lengths)==expect,(n,m,lengths,expect)
    # Neighbor witnesses: for n>=2, they are n-F_m and n-F_(m-1).
    if n>=2:
        ix={sorted_points[j-1][1] if j else sorted_points[-1][1],
            sorted_points[j][1] if j<len(sorted_points) else sorted_points[0][1]}
        assert ix=={n-fib[m],n-fib[m-1]},(n,m,ix)
    a,b=[as_float(x) for x in lengths]
    val=-(a*math.log(a)+b*math.log(b))+(a+b)*math.log(a+b)
    C=-(2-alpha)*math.log(alpha)
    expected=C*alpha**(m-2)
    maxerr=max(maxerr,abs(val-expected))
    assert abs(val-expected)<1e-11,(n,m,val,expected)
    counts[m]=counts.get(m,0)+1
    sorted_points.insert(j,(t,n))
print('VERIFY_OK exact field comparisons; all',N,'successive splits match golden powers and predecessor Fibonacci indices')
print('FIBONACCI_INTERVALS_CHECKED',len(counts),'MAX_FLOAT_ENTROPY_ERROR',maxerr)
C=-(2-alpha)*math.log(alpha);phi=(1+math.sqrt(5))/2
print('C',format(C,'.15g'))
print('LIMINF',format(C*phi**2/math.sqrt(5),'.15g'))
print('LIMSUP',format(C*phi**3/math.sqrt(5),'.15g'))
