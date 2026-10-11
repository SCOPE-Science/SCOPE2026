"""Reproduce algebraic and finite spectral checks for wheel root-polytope ellipsoids.

Requires Python 3.10+ standard library. Finite tests corroborate the separate proof.
"""
from fractions import Fraction
from math import sin, pi, sqrt, isclose


def add(a,b):
    o=[0]*max(len(a),len(b))
    for i,x in enumerate(a):o[i]+=x
    for i,x in enumerate(b):o[i]+=x
    return o

def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o

def cm(n):
    # U_n=alpha^n+beta^n where alpha+beta=1+2t, alpha*beta=t^2.
    u0=[2];u1=[1,2]
    for _ in range(2,n+1):
        u0,u1=u1,add(mul([1,2],u1),[-x for x in mul([0,0,1],u0)])
    out=u1+[0]*max(0,n+1-len(u1))
    out[n]-=2
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def val(p,t):return sum(v*t**i for i,v in enumerate(p))

def hp(n):
    c=cm(n)
    dc=[i*c[i] for i in range(1,len(c))]
    return add(add(dc,[0]+dc),[-n*x for x in c])

def divide(p,q):
    r=list(map(Fraction,p));q=list(map(Fraction,q))
    while len(r)>1 and r[-1]==0:r.pop()
    while len(r)>=len(q):
        shift=len(r)-len(q)
        z=r[-1]/q[-1]
        for i in range(len(q)):r[shift+i]-=z*q[i]
        while r and r[-1]==0:r.pop()
    return r

def F(n,t):
    return sum(4*sin(pi*k/n)**2/(1+4*t*sin(pi*k/n)**2) for k in range(1,n))-n/(1+t)

def root(n):
    lo,hi=1.0,2.0
    for _ in range(65):
        t=(lo+hi)/2
        if F(n,t)>0:lo=t
        else:hi=t
    return (lo+hi)/2

def solve(A,b):
    n=len(A)
    a=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(a[i][j]))
        a[j],a[p]=a[p],a[j]
        d=a[j][j]
        assert abs(d)>1e-13
        for k in range(j,n+1):a[j][k]/=d
        for i in range(n):
            if i==j:continue
            d=a[i][j]
            for k in range(j,n+1):a[i][k]-=d*a[j][k]
    return [a[i][-1] for i in range(n)]

def gauges(n,t):
    a=1/(n*(1+t));b=t*a
    B=[[a*(i==j)+b*(2*(i==j)-(j==(i+1)%n)-(j==(i-1)%n)) for j in range(n)] for i in range(n)]
    e=[1.0]+[0.0]*(n-1)
    x=solve(B,e)
    f=[1.,-1.]+[0.]*(n-2)
    y=solve(B,f)
    return x[0],y[0]-y[1]

# Symbolic coefficient identity, exact endpoints, and small algebraic factors.
for n in range(3,81):
    C=cm(n);H=hp(n)
    assert val(C,2)==(2**n-1)**2
    assert Fraction(val(H,2),3*val(C,2))==Fraction(-n,3*(2**n-1))
    if n==3:assert val(H,1)==0
    if n>=4:assert val(H,1)>0 and val(H,2)<0
for n,q in [(4,[-1,-2,2]),(5,[-1,-1,1]),(6,[-1,-3,2])]:
    assert divide(hp(n),q)==[]
assert cm(3)==[1,6,9]

# Independent Gaussian-elimination effective-resistance contact checks.
for n in range(3,21):
    t=root(n)
    assert 1-1e-10<=t<2
    spoke,rim=gauges(n,t)
    assert abs(spoke-n)<3e-7, (n,t,spoke)
    assert abs(rim-n)<3e-7, (n,t,rim)
    a=1/(n*(1+t));b=t*a
    eigen=[(n+1)*a]+[a+4*b*sin(pi*k/n)**2 for k in range(1,n)]
    # Trace of Laplacian equals twice normalized edge mass.
    assert abs(sum(eigen)-2)<1e-10
    assert all(x>0 for x in eigen)
    if n==3:assert abs(t-1)<1e-10
for n in (16,18,20,22,24):
    t=root(n)
    assert abs(2**n*(2-t)-18)<0.23
print('VERIFY_OK: 78 exact endpoint identities, three algebraic factors,')
print('18 finite resistance contact pairs, and exponential asymptotic checks.')
