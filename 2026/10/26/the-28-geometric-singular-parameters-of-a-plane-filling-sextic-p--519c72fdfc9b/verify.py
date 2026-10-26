#!/usr/bin/env python3
"""Exact GF(3) polynomial certificates for the finite-parameter sextic pencil.
No numerical approximations or third-party dependencies.
"""
from functools import reduce
P = 3

def norm(a):
    if not a: return (0,)
    a = tuple(int(v) % P for v in a)
    while len(a) > 1 and a[-1] == 0: a = a[:-1]
    return a

def add(a,b):
    n = max(len(a),len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])

def neg(a): return norm([-x for x in a])
def sub(a,b): return add(a,neg(b))

def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j] += ai*bj
    return norm(c)

def divmodp(a,b):
    a=list(norm(a));b=norm(b)
    assert b!=(0,)
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        degree=len(a)-len(b);c=a[-1]*pow(b[-1],-1,P)%P
        q[degree]=c
        for j,bj in enumerate(b):a[degree+j]=(a[degree+j]-c*bj)%P
        a=list(norm(a))
    return norm(q),norm(a)

def rem(a,m):return divmodp(a,m)[1]
def gcd(a,b):
    while b!=(0,):a,b=b,rem(a,b)
    return norm([(x*pow(a[-1],-1,P))%P for x in a])

def powmod(a,n,m):
    o=(1,);a=rem(a,m)
    while n:
        if n&1:o=rem(mul(o,a),m)
        a=rem(mul(a,a),m);n>>=1
    return o

def poly(d):
    a=[0]*(max(d)+1)
    for e,c in d.items(): a[e]=c
    return norm(a)

def mon(n):return poly({n:1})

def irreducible_prime_degree(f):
    n=len(f)-1
    assert n in (7,19)
    u=(0,1)
    return powmod(u,3**n,f)==u and gcd(f,sub(powmod(u,3,f),u))==(1,)

def pow_poly(a,n):
    v=(1,)
    for _ in range(n):v=mul(v,a)
    return v

def eval_poly(f,x,modulus):
    v=(0,)
    for c in reversed(f):
        v=add(rem(mul(v,x),modulus),(c,))
    return v

u=(0,1)
P7=poly({7:1,5:1,4:1,3:-1,0:-1})
P19=poly({19:1,18:1,17:1,15:-1,11:-1,8:-1,7:1,5:-1,3:-1,1:1,0:1})
Q7=poly({7:1,6:1,4:1,3:-1,0:-1})
Q19=poly({19:1,18:-1,16:-1,15:-1,14:1,11:-1,9:1,8:-1,7:-1,5:-1,3:1,2:1,0:1})
H=poly({31:-1,29:1,21:1,19:-1,16:-1,8:2,0:-1})
fac=mul(mul(pow_poly(sub(u,(1,)),3),pow_poly(add(u,(1,)),2)),mul(P7,P19))
assert H==neg(fac),(H,neg(fac))
print('ELIMINATION_IDENTITY_OK')
for n,f,q in [(7,P7,Q7),(19,P19,Q19)]:
    assert irreducible_prime_degree(f)
    assert irreducible_prime_degree(q)
    # In F_(3^n), u^(-16) = u^(3^n-1-16).
    K=sub(powmod(u,5,f),powmod(u,3**n-1-16,f))
    assert rem(eval_poly(q,K,f),f)==(0,),n
    assert sub(powmod(K,3,f),K)!=(0,),n
    print('MINIMAL_POLYNOMIAL_AND_IRREDUCIBILITY_OK',n)

def value_f(x,y,z,k):
    return (x*x*(x**3*y-x*y**3)+y*y*(y**3*z-y*z**3)+(z*z+k*x*x)*(z**3*x-z*x**3))%3

def partials(x,y,z,k):
    # Compute as homogeneous partial derivatives in F_3.
    fx= (2*x**4*(y-k*z)+z**5)%3
    fy= (x**5+2*y**4*z)%3
    fz= (-k*x**5+y**5+2*z**4*x)%3
    return fx,fy,fz

pts=[(1,y,z) for y in range(3) for z in range(3)] + [(0,1,z) for z in range(3)] + [(0,0,1)]
assert len(pts)==13
for k in range(3):
    bad=[pt for pt in pts if value_f(*pt,k)==0 and partials(*pt,k)==(0,0,0)]
    assert bad==({0:[(1,1,1)],1:[(1,2,1)],2:[]}[k]),(k,bad)
    assert all(value_f(*pt,k)==0 for pt in pts)
    print('RATIONAL_FIBER_CHECK_OK',k,len(bad))
print('VERIFY_OK')
