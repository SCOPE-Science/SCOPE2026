#!/usr/bin/env python3
"""Finite-field collision identities and Walsh-transform consistency checks."""
from collections import Counter
from itertools import product
from math import isclose
import random

IRRED={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def mul(a,b,n):
    P=IRRED[n]; z=0
    while b:
        if b&1:z ^= a
        b>>=1
        a <<= 1
        if a & (1<<n): a ^= P
    return z

def apn(F,q):
    for s in range(1,q):
        if max(Counter(F[t]^F[t^s] for t in range(q)).values())>2:
            return False
    return True

def collision(F,q):
    R=Counter((t^u,F[t]^F[u]) for t in range(q) for u in range(q))
    energy=sum(v*v for v in R.values())
    ex=0
    for s in range(1,q):
        for w in range(q):
            m=R[s,w]//2
            ex += m*(m-1)
    assert energy == 3*q*q-2*q+4*ex,(q,energy,ex)
    assert (energy==3*q*q-2*q)==apn(F,q)
    if not apn(F,q): assert energy-(3*q*q-2*q)>=8
    return R,energy,ex

def WHT(x):
    x=list(x); n=len(x)
    h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                a,b=x[j],x[j+h]
                x[j]=a+b; x[j+h]=a-b
        h*=2
    return x

rng=random.Random(73591)
loops=0
for n in range(1,6):
    q=1<<n
    F=[mul(mul(t,t,n),t,n) for t in range(q)]
    assert apn(F,q),n
    R,e,ex=collision(F,q)
    assert ex==0
    for trial in range(10):
        f=[complex(rng.randint(-7,7)/5,rng.randint(-7,7)/5) for _ in range(q)]
        S=sum(abs(z)**2 for z in f)
        T=sum(z*z for z in f)
        Q=sum(abs(z)**4 for z in f)
        c=Counter()
        for t in range(q):
            for u in range(q):
                c[(t^u,F[t]^F[u])] += f[t]*f[u]
        conv=sum(abs(v)**2 for v in c.values())
        formula=abs(T)**2+2*(S*S-Q)
        assert isclose(conv,formula,rel_tol=1e-11,abs_tol=1e-8),(n,conv,formula)
        arr=[0j]*(q*q)
        for t,z in enumerate(f):arr[t+q*F[t]]=z
        transforms=WHT(arr)
        direct=sum(abs(z/q)**4 for z in transforms)
        assert isclose(direct,conv/q**2,rel_tol=1e-11,abs_tol=1e-8),(n,direct,conv/q**2)
        deficit=((3-2/q)*S*S-conv)
        expected=S*S-abs(T)**2+2*(Q-S*S/q)
        assert isclose(deficit,expected,rel_tol=1e-10,abs_tol=1e-8)
        sos=sum(abs(f[t]*f[u].conjugate()-f[t].conjugate()*f[u])**2 +
                (2/q)*(abs(f[t])**2-abs(f[u])**2)**2
                for t in range(q) for u in range(t+1,q))
        assert isclose(expected,sos,rel_tol=1e-10,abs_tol=1e-8)
        assert deficit >= -1e-8
        loops+=1
    for trial in range(3):
        signs=[rng.choice([-1,1]) for _ in range(q)]
        f=[complex(z) for z in signs]
        S=sum(abs(z)**2 for z in f)
        T=sum(z*z for z in f)
        Q=sum(abs(z)**4 for z in f)
        assert abs(T)**2+2*(S*S-Q) == (3-2/q)*S*S
    if q <= 4:
        for H in product(range(q),repeat=q):
            collision(H,q)
    else:
        for trial in range(5):
            H=[rng.randrange(q) for _ in range(q)]
            collision(H,q)
    print('GF(2^%d) size %d: APN cubic, exact energy %d, %d complex coefficient verifications, randomized non-APN collision tests PASS'%(n,q,e,10))
print('TOTAL',loops,'complex moment + Walsh transform + deficit checks')
