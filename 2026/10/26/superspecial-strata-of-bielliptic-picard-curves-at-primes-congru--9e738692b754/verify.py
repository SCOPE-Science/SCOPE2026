#!/usr/bin/env python3
"""Independent finite-prime checks of coefficient and simple-root identities.
The proof for all primes is algebraic and given in RESULT.md."""
from math import comb

def polypow(h, n, p):
    out = {(0, 0): 1}
    for _ in range(n):
        new = {}
        for (t, a), z in out.items():
            for dt, da, c in h:
                key = (t + dt, a + da)
                new[key] = (new.get(key, 0) + z*c) % p
        out = {key: v for key, v in new.items() if v}
    return out

def coefficient(n, tdeg, p):
    h = [(2, 0, 1), (1, 1, 1), (0, 0, 1)]
    return {a: v for (t, a), v in polypow(h, n, p).items() if t == tdeg}

def pmul(a, b, p):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            r[i+j] = (r.get(i+j, 0) + x*y) % p
    return {i: v for i, v in r.items() if v}

def ppow(x, n, p):
    r = {0:1}
    for _ in range(n):r = pmul(r, x, p)
    return r

def normalize(d,p):
    if not d:return {}
    c=pow(d[max(d)],-1,p)
    return {j:v*c%p for j,v in d.items() if v%p}

def modpoly(a,b,p):
    a=dict(a)
    if not b:raise ZeroDivisionError
    db=max(b);ib=pow(b[db],-1,p)
    while a and max(a)>=db:
        shift=max(a)-db;c=a[max(a)]*ib%p
        for j,v in b.items():
            t=j+shift;a[t]=(a.get(t,0)-c*v)%p
            if not a[t]:del a[t]
    return a

def gcdpoly(a,b,p):
    while b:a,b=b,modpoly(a,b,p)
    return normalize(a,p)

for p in (5,11,17,23,29,41,47):
    m=(p-5)//6;k=3*m+2
    R=coefficient(2*m+1,k,p)
    S=coefficient(4*m+3,k,p)
    K=comb(4*m+3,3*m+2)*pow(comb(2*m+1,m),-1,p)%p
    predicted={j:K*v%p for j,v in pmul(ppow({2:1,0:-4%p},m+1,p),R,p).items()}
    assert S==predicted, (p,S,predicted)
    assert max(R)==m and R[m]%p!=0
    derivative={j-1:j*v%p for j,v in R.items() if j and j*v%p}
    assert gcdpoly(R, derivative,p)=={0:1}
    assert sum(v*pow(2,j,p) for j,v in R.items())%p!=0
    assert sum(v*pow(-2,j,p) for j,v in R.items())%p!=0
    print('p',p,'m',m,'identity_OK','simple_roots_OK','K',K)
print('VERIFY_OK')
