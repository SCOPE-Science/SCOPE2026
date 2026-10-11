"""Reproduce the threshold and distinct interior solutions for the real fibers.
Run: python3 verify_real_fibers.py (Python standard library only).
"""
import math

PI=math.pi
XC=2/math.sqrt(PI*PI+4)
MC=PI/math.sqrt(PI*PI+4)

def g(x,y):
    r2=x*x+y*y
    return (2/PI)*math.atan2(4*x*y,1-r2*r2)

def mu(x,y):
    return y/g(x,y) if y else PI*(1-x**4)/(8*x)

def solve_roots(x,m,n=12000):
    b=math.sqrt(1-x*x)
    yy=[b*i/(n+1) for i in range(n+1)]
    vv=[mu(x,y)-m for y in yy]
    roots=[]
    for i in range(n):
        if vv[i]*vv[i+1]<0:
            lo,hi=yy[i],yy[i+1]
            for _ in range(70):
                mid=(lo+hi)/2
                if (mu(x,mid)-m)*vv[i]>0: lo=mid
                else: hi=mid
            roots.append((lo+hi)/2)
    return roots

assert abs(MC*MC+XC*XC-1)<1e-15
assert abs(PI*PI*(PI*PI+8)/(16*(PI*PI+4))-0.7947501652825846)<1e-14
# Search for a five-point real fiber in a bounded interval of real targets.
for M in (1.9,2.0,4.0):
    m=M-1
    lo,hi=0.001,0.999
    for _ in range(65):
        xmid=(lo+hi)/2
        if PI*(1-xmid**4)/(8*xmid)>m: lo=xmid
        else: hi=xmid
    r=(lo+hi)/2
    test_x=[r*(1+1e-4),r*(1+1e-5),r*(1+1e-6)]
    test_x.extend([i/1000 for i in range(10,999,5)])
    samples=[(x,solve_roots(x,m,n=1200)) for x in test_x]
    witnesses=[(x,roots) for x,roots in samples if len(roots)==2]
    assert witnesses,(M,'no five-point fiber found')
    x,roots=witnesses[0]
    assert len(roots)==2 and all(x*x+y*y<1 for y in roots)
    assert all(abs(y-(M-1)*g(x,y))<1e-12 for y in roots)
    print('M=',M,'x=',x,'positive imaginary preimages',roots)
for M in (1.05,1.3,1.8):
    assert max(len(solve_roots(x,M-1,n=700)) for x in [i/1000 for i in range(20,999,5)])<=1
print('THRESHOLD',1+MC,'CHECK_OK')
