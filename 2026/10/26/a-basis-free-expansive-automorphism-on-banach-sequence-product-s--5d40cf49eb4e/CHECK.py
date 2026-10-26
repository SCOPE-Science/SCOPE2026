"""Reproducible finite-support algebra checks for the shift-interface theorem.
These computations illustrate but do not replace the infinite-dimensional proof.
"""
import random
import cmath

r = random.Random(261019954)

def trim(v):
    a=list(v)
    while a and a[-1]==0:
        a.pop()
    return tuple(a)

def shift(x):
    return (0,)+tuple(x)

def forward(m,y,w, lam):
    mm=tuple(lam*z for z in shift(m))
    if w:
        mm=(mm[0]+w[0],)+mm[1:]
    return trim(mm),lam*y,trim(w[1:])

def inverse(m,y,w,lam):
    h=m[0] if m else 0
    tail=tuple(z/lam for z in m[1:])
    return trim(tail),y/lam,trim((h,)+tuple(w))

def maxabs(xs):
    return max([0]+[abs(z) for z in xs])

def err(a,b):
    return abs(a-b) <= 1e-7*(1+abs(a)+abs(b))

counter=0
for trial in range(1200):
    lam=(0.35+2.7*r.random())*cmath.exp(1j*2*3.141592653589793*r.random())
    m=trim(tuple(complex(r.randint(-3,3),r.randint(-3,3)) for _ in range(r.randint(0,8))))
    w=trim(tuple(complex(r.randint(-3,3),r.randint(-3,3)) for _ in range(r.randint(0,8))))
    y=complex(r.randint(-3,3),r.randint(-3,3))
    m1,y1,w1=forward(m,y,w,lam)
    m2,y2,w2=inverse(m1,y1,w1,lam)
    assert all(err(a,b) for a,b in zip(m2+(0,)*max(0,len(m)-len(m2)),m+(0,)*max(0,len(m2)-len(m))))
    assert err(y,y2)
    assert w2==w
    z=(m,y,w)
    for n in range(1,7):
        z=forward(*z,lam)
        measured=maxabs(z[0]); expected=max([abs(lam)**n*maxabs(m)]+[abs(lam)**(n-j)*abs(w[j-1]) for j in range(1,min(n,len(w))+1)])
        assert err(measured,expected),(trial,n,measured,expected)
        assert err(abs(z[1]),abs(lam)**n*abs(y))
        assert z[2]==trim(w[n:])
        counter+=3
print('PASS:',counter,'finite-support forward/inverse/orbit consistency assertions across 1200 cases')
