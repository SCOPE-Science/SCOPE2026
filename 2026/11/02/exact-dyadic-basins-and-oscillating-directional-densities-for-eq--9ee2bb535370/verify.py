"""Exact rational regression checks for the equilateral three-line farthest-projection map.

Checks are finite diagnostics, not a replacement for the universal proof.
Run with Python 3 using only its standard library.
"""
from fractions import Fraction as Q

# Oblique basis e1=(1,0), e2=(1/2,sqrt(3)/2), hence
# <(a,b),(c,d)>=ac+bd+(ad+bc)/2.
def dot(x,y):
    return x[0]*y[0]+x[1]*y[1]+(x[0]*y[1]+x[1]*y[0])/2

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def scale(a,x): return (a*x[0],a*x[1])

# Three oriented supporting lines BC, CA, AB.
verts=((Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1)))  # B,C,A
bases=((verts[0],sub(verts[1],verts[0])),
       (verts[1],sub(verts[2],verts[1])),
       (verts[2],sub(verts[0],verts[2])))

def point(i,t):
    v,d=bases[i]
    return add(v,scale(t,d))

def project(x,j):
    v,d=bases[j]
    t=dot(sub(x,v),d)/dot(d,d)
    y=point(j,t)
    return t, dot(sub(x,y),sub(x,y))

def geometric_step(i,t):
    x=point(i,t)
    targets=[j for j in range(3) if j!=i]
    projected=[(j,*project(x,j)) for j in targets]
    if projected[0][2]==projected[1][2]:return i,t
    return max(projected,key=lambda z:z[2])[:2]

def symbolic_step(i,t):
    if t==Q(1,2):return i,t
    if t<Q(1,2):return (i+1)%3,(1-t)/2
    return (i-1)%3,1-t/2

def m_from_dyadic(r):
    assert r>0
    m=0
    # Finds smallest nonnegative m with 2^m >= r+1/2.
    while 2**m < r+Q(1,2):m+=1
    return m

def predicted_type(p):
    if p==0:return 'fixed'
    r=abs(p)
    m=m_from_dyadic(r)
    if r+Q(1,2)==2**m:return 'fixed'
    return 'plus' if (p>0)==(m%2==0) else 'minus'

def is_close(a,b,eps=Q(1,10**5)):return abs(a-b)<eps

assert all(dot(d,d)==1 for _,d in bases)
num=0
for i in range(3):
    for n in range(-1024,1025):
        t=Q(1,2)+Q(n,32)
        assert symbolic_step(i,t)==geometric_step(i,t),(i,t)
        p=t-Q(1,2)
        typ=predicted_type(p)
        I,T=i,t
        for _ in range(135):
            I,T=symbolic_step(I,T)
        if typ=='fixed':
            assert T==Q(1,2)
            assert symbolic_step(I,T)==(I,T)
        else:
            assert is_close(T,Q(2,3) if typ=='plus' else Q(1,3))
            assert symbolic_step(I,T)[0]== ((I-1)%3 if typ=='plus' else (I+1)%3)
        num+=1

# Both primitive three-cycles and all midpoints are exact.
for i in range(3):
    assert symbolic_step(i,Q(1,2))==(i,Q(1,2))
    for v in (Q(1,3),Q(2,3)):
        I,T=i,v
        for k in range(3):I,T=symbolic_step(I,T)
        assert (I,T)==(i,v)

# Exceptional rays: 2^m-1/2 land on switching line after m+1 steps.
for m in range(16):
    for s in (-1,1):
        i,t=0,Q(1,2)+s*(2**m-Q(1,2))
        for _ in range(m+1):i,t=symbolic_step(i,t)
        assert t==Q(1,2)

# Exact interval lengths and two subsequence limits.
for k in range(1,20):
    even=4**k-Q(1,2)
    plus=Q(2,3)*4**k-Q(1,6)
    odd=2*4**k-Q(1,2)
    assert Q(2,3) < plus/even < Q(3,4)
    assert plus/odd == Q(1,3)
    assert abs(plus/even-Q(2,3))<Q(1,4**k)
    assert abs(plus/odd-Q(1,3))<Q(1,4**k)

print(f'CHECK_OK {num} exact geometric projection and basin tests; exact dyadic endpoints and two cycle equations')
