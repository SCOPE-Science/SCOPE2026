#!/usr/bin/env python3
import cmath
import math

TOL = 2e-8

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return math.sqrt(dot(a,a))

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def scale(c,a):
    return [c*x for x in a]

def shift(x,j):
    n=len(x)
    j%=n
    return x[-j:]+x[:-j] if j else x[:]

def orthonormal_basis(cols):
    Q=[]
    for c in cols:
        v=[float(z) for z in c]
        for q in Q:
            v=sub(v,scale(dot(v,q),q))
        nv=norm(v)
        if nv>1e-11:
            Q.append(scale(1.0/nv,v))
    return Q

def direct_proxy(x):
    n=len(x)
    v=[shift(list(map(float,x)),j) for j in range(n)]
    cols=[sub(v[j],v[n-1]) for j in range(n-1)]
    b=cols[0]
    Q=orthonormal_basis(cols[1:])
    r=b[:]
    for q in Q:
        r=sub(r,scale(dot(r,q),q))
    return norm(r)

def dft(x):
    n=len(x)
    return [sum(x[j]*cmath.exp(-2j*math.pi*k*j/n) for j in range(n)) for k in range(n)]

def fourier_proxy(x):
    n=len(x)
    h=dft(x)
    vals=[abs(h[k]) for k in range(1,n)]
    if min(vals)<1e-10:
        return 0.0
    return math.sqrt(n/sum(1.0/(z*z) for z in vals))

def binary_closed(n,d):
    g=math.gcd(n,d)
    N=n//g
    if N%2==0:
        return 0.0
    return math.sqrt(4.0*n/(n*N-1.0))

def smallest_odd_prime_factor(n):
    m=n
    while m%2==0:
        m//=2
    if m==1:
        return None
    q=3
    while q*q<=m:
        if m%q==0:
            return q
        q+=2
    return m

def is_power_two(n):
    return n>0 and (n & (n-1))==0

def check_close(a,b,msg):
    if abs(a-b)>TOL*max(1.0,abs(a),abs(b)):
        raise AssertionError(f"{msg}: {a} vs {b}")

# General Fourier-altitude spot checks, including a spectral notch.
for x in ([0,1,2,3],[0,1,3,2],[1,0,0,0],[1,2,4,8,16],[2,-1,0,3,5,7]):
    check_close(direct_proxy(x),fourier_proxy(x),f"general x={x}")

# Exhaust all two-one cyclic separations for a nontrivial range.
for n in range(3,31):
    vals=[]
    for d in range(1,n):
        x=[0.0]*n
        x[0]=x[d]=1.0
        a=direct_proxy(x)
        b=fourier_proxy(x)
        c=binary_closed(n,d)
        check_close(a,b,f"direct/fourier n={n} d={d}")
        check_close(a,c,f"direct/closed n={n} d={d}")
        vals.append((a,d))
    positive=[z for z,d in vals if z>1e-8]
    if is_power_two(n):
        if positive:
            raise AssertionError(f"power-of-two collapse failed n={n}")
    else:
        q=smallest_odd_prime_factor(n)
        expected=math.sqrt(4.0*n/(n*q-1.0))
        actual=max(z for z,d in vals)
        check_close(actual,expected,f"global maximum n={n}")
        maximizers={d for z,d in vals if abs(z-actual)<1e-8}
        expected_d={d for d in range(1,n) if math.gcd(n,d)==n//q}
        if maximizers!=expected_d:
            raise AssertionError(f"maximizers n={n}: {maximizers} vs {expected_d}")

# The minimal 5% case.
n=20
positive=[]
for d in range(1,n):
    z=binary_closed(n,d)
    if z>1e-10:
        positive.append(d)
if positive != [4,8,12,16]:
    raise AssertionError(positive)
check_close(binary_closed(20,4),math.sqrt(80.0/99.0),'n=20 value')

print('VERIFY_OK')
