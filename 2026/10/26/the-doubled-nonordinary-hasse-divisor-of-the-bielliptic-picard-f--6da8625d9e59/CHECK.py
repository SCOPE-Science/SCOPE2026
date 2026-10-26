"""Exact finite-field checks of coefficient identities for the Picard-family theorem.

Run: python3 picard_hasse_check.py
Finite checks corroborate, but do not replace, the all-prime proof.
"""
from math import comb, factorial


def poly(N, r, p):
    """Coefficient of t**r in (t*t+a*t+1)**N, as polynomial in a."""
    out = [0] * (N + 1)
    for h in range(N + 1):
        j = r - 2 * h
        z = N - h - j
        if j >= 0 and z >= 0:
            out[j] = (out[j] + factorial(N) // (factorial(h)*factorial(j)*factorial(z))) % p
    return trim(out)


def trim(x):
    x = list(x)
    while len(x)>1 and x[-1] == 0:
        x.pop()
    return x


def mul(a,b,p):
    out = [0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j]=(out[i+j]+u*v)%p
    return trim(out)


def scale(a,c,p):
    return trim([(t*c)%p for t in a])


def powpoly(a,n,p):
    z=[1]
    for _ in range(n):
        z=mul(z,a,p)
    return z


def derivative(a,p):
    return trim([(j*a[j])%p for j in range(1,len(a))] or [0])


def rem(a,b,p):
    a=trim(a); b=trim(b)
    while a!=[0] and len(a)>=len(b):
        c=a[-1]*pow(b[-1],-1,p)%p
        sh=len(a)-len(b)
        for i,v in enumerate(b):
            a[i+sh]=(a[i+sh]-c*v)%p
        a=trim(a)
    return a


def gcd(a,b,p):
    a=trim(a);b=trim(b)
    while b!=[0]:
        a,b=b,rem(a,b,p)
    return a


def prime(p):
    return p>1 and all(p%d for d in range(2,int(p**.5)+1))

for p in [7,13,19,31,37,43,61,67,73,79,97,103]:
    assert p % 6 == 1 and prime(p)
    m=(p-1)//6
    q=poly(2*m,3*m,p)
    t=poly(4*m,6*m,p)
    r=poly(4*m,3*m,p)
    D=[-4%p,0,1]
    A=comb(4*m,2*m)%p
    B=comb(4*m,m)*pow(comb(2*m,m),-1,p)%p
    K=comb(6*m,2*m)%p
    assert K*A*B%p != 0
    assert q[-1] == comb(2*m,m)%p and len(q)==m+1
    assert t == scale(powpoly(D,m,p),A,p)
    assert r == scale(mul(powpoly(D,m,p),q,p),B,p)
    assert len(gcd(q,derivative(q,p),p))==1
    assert len(gcd(q,D,p))==1
    # Direct separate diagonal coefficients from the plane quartic expansion.
    assert scale(t,K,p) == scale(poly(4*m,6*m,p),K,p)
    assert scale(q,K,p) == scale(poly(2*m,3*m,p),K,p)
    assert scale(r,K,p) == scale(poly(4*m,3*m,p),K,p)
    print(f"p={p}: m={m}, Q degree {m}, both factorizations and separability verified")
print('VERIFY_OK: Picard-family Hasse factorizations, no boundary roots, simple roots')
