#!/usr/bin/env python3
"""Exact coefficient arithmetic and rational Sturm certificates for Stern polynomials."""
from fractions import Fraction as F
from functools import lru_cache


def trim(a):
    a=list(a)
    while a and not a[-1]:
        a.pop()
    return tuple(a)


def add(a,b):
    return trim(tuple((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0) for i in range(max(len(a),len(b)))))


def mul(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]+=x*y
    return trim(v)


def deriv(a):
    return trim(tuple(i*a[i] for i in range(1,len(a))))


def evaluate(a,x):
    s=F(0)
    for coeff in a[::-1]: s=s*x+coeff
    return s


def remainder(a,b):
    a=list(map(F,a)); b=list(map(F,b))
    while len(a)>=len(b):
        c=a[-1]/b[-1]
        off=len(a)-len(b)
        for j in range(len(b)): a[off+j]-=c*b[j]
        while a and a[-1]==0:a.pop()
    return tuple(a)


def sturm_roots(a):
    s=[trim(a),deriv(a)]
    while len(s[-1])>1:
        r=trim(tuple(-z for z in remainder(s[-2],s[-1])))
        if not r:break
        s.append(r)
    def variations(pos):
        signs=[]
        for p in s:
            z=p[-1]
            if not pos and (len(p)-1)%2:z=-z
            signs.append(1 if z>0 else -1)
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    return variations(False)-variations(True),len(s)

@lru_cache(None)
def stern(n):
    if n==0:return ()
    if n==1:return (1,)
    if n%2==0:return (0,)+stern(n//2)
    return add(stern(n//2),stern(n//2+1))


def explicit(k):
    S=(1,)
    for j in range(1,k-1):S=add(S,(0,)*j+(2,))
    return add(mul(S,(1,4,5,3)),mul((1,1),(0,0,1,2,2)))

for k in range(2,13,2):
    idx=53*2**k-3
    q=explicit(k)
    assert q==stern(idx),(k,'closed expression disagrees')
    d=deriv(q)
    roots,steps=sturm_roots(d)
    assert roots==0,(k,roots)
    assert d[0]>0
    print('k=',k,'degree=',len(q)-1,'positive_derivative=True','sturm_steps=',steps)

x=F(13,20)
for k in (14,16,18,20,22,24,32):
    idx=53*2**k-3
    d=deriv(explicit(k))
    if k<=20:
        assert explicit(k)==stern(idx)
    lhs=evaluate(d,-x)
    rhs=(80*(82203*k+108923)*x**(k-2)-1026127)/17424000
    assert lhs==rhs,(k,lhs,rhs)
    assert lhs<0
    print('k=',k,'negative_derivative=True')
assert F(13,20)**2 * F(82203*16+108923,82203*14+108923)<1
assert 80*(82203*14+108923)*x**12<1026127
print('VERIFY_OK')
