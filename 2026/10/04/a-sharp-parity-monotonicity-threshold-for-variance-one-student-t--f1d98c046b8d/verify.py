import math
SQ3=math.sqrt(3.0)
def simpson(f,a,b,N=3000):
    if N%2: N+=1
    h=(b-a)/N; s=f(a)+f(b)
    for i in range(1,N): s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3
def c(n): return math.exp(math.lgamma((n+1)/2)-math.lgamma(n/2))/math.sqrt(math.pi*(n-2))
def g(n,x): return c(n)*(1+x*x/(n-2))**(-(n+1)/2)
def J(n,y): return 2*simpson(lambda z:g(n,z),0.0,y)
def J3(y): return 2/math.pi*(math.atan(y)+y/(1+y*y))
def J4(y): return y*(y*y+3)/(y*y+2)**1.5
def B(n):
    L=math.sqrt(n/(n-2)); m=(1+L)/2
    return n*(L-1)*((n+3)/(n+3*m*m))**((n+1)/2)
for n in range(3,5000): assert B(n)>1-2e-12,(n,B(n))
for y in [0.05,0.3,0.8,1.0,1.4,SQ3]:
    assert abs(J(3,y)-J3(y))<3e-10
    assert abs(J(4,y)-J4(y))<3e-10
    assert J3(y)>J4(y)
for y in [0.05,0.3,0.9,1.0,1.2,1.5,1.7,SQ3]:
    for n in range(3,90): assert J(n,y)>J(n+2,y)-3e-10,(n,y)
for y in [1.8,2.0,2.5]:
    for n in [300,500,800]:
        d=J(n+2,y)-J(n,y)
        lead=y*(y*y-3)*math.exp(-y*y/2)/math.sqrt(2*math.pi)/(n*n)
        assert d>0 and 0.6<d/lead<1.4,(n,y,d,lead)
assert 2/3+SQ3/(2*math.pi)-6*math.sqrt(15)/25>0
print('VERIFY_OK')
