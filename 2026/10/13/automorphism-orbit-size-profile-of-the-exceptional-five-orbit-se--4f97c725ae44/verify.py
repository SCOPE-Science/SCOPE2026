#!/usr/bin/env python3
from itertools import permutations

POLY = 0b10011  # u^4 + u + 1

def gf_mul(a,b):
    r=0
    while b:
        if b&1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 0b10000:
            a ^= POLY
    return r & 15

def gf_pow(a,n):
    r=1
    while n:
        if n&1:
            r=gf_mul(r,a)
        a=gf_mul(a,a)
        n >>= 1
    return r

def mapply(M,v):
    r=0
    for j in range(4):
        if (v>>j)&1:
            r ^= M[j]
    return r

def mcomp(A,B):
    return tuple(mapply(A,B[j]) for j in range(4))

I=(1,2,4,8)

def mpow(M,n):
    R=I
    while n:
        if n&1:
            R=mcomp(R,M)
        M=mcomp(M,M)
        n >>= 1
    return R

def minv(M):
    pre={mapply(M,v):v for v in range(16)}
    assert len(pre)==16
    return tuple(pre[1<<j] for j in range(4))

def from_linear(f):
    return tuple(f(1<<j) for j in range(4))

zeta=8  # u^3, order 5 in this model
assert gf_pow(zeta,5)==1 and all(gf_pow(zeta,j)!=1 for j in range(1,5))
A=from_linear(lambda x:gf_mul(zeta,x))
T=from_linear(lambda x:gf_pow(x,4))
assert mpow(A,5)==I
assert mpow(T,2)==I
assert mcomp(T,mcomp(A,T))==mpow(A,4)

H={mcomp(mpow(A,i),mpow(T,j)) for i in range(5) for j in range(2)}
assert len(H)==10
C5={mpow(A,i) for i in range(5)}

GL=[]
for M in permutations(range(1,16),4):
    if len({mapply(M,v) for v in range(16)})==16:
        GL.append(M)
assert len(GL)==20160

N=[]
for M in GL:
    Mi=minv(M)
    if mcomp(M,mcomp(A,Mi)) in H and mcomp(M,mcomp(T,Mi)) in H:
        N.append(M)
assert len(N)==60

def acomp(g,h):
    v,M=g; w,K=h
    return (v ^ mapply(M,w), mcomp(M,K))

def ainv(g):
    v,M=g
    Mi=minv(M)
    return (mapply(Mi,v),Mi)

def aconj(phi,g):
    return acomp(acomp(phi,g),ainv(phi))

def aorder(g):
    r=(0,I)
    for n in range(1,21):
        r=acomp(r,g)
        if r==(0,I):
            return n
    raise AssertionError('order bound')

G=[(v,h) for h in H for v in range(16)]
assert len(G)==160
AN=[(b,M) for M in N for b in range(16)]
assert len(AN)==960

unseen=set(G)
orbits=[]
while unseen:
    g=next(iter(unseen))
    orb={aconj(phi,g) for phi in AN}
    orbits.append(orb)
    unseen -= orb
assert not unseen
assert sorted(len(o) for o in orbits)==[1,15,20,60,64]

profile=[]
for orb in orbits:
    os={aorder(g) for g in orb}
    inV={h==I for v,h in orb}
    inGprime={h in C5 for v,h in orb}
    assert len(os)==len(inV)==len(inGprime)==1
    profile.append((len(orb),next(iter(os)),next(iter(inV)),next(iter(inGprime))))

expected={(1,1,True,True),(15,2,True,True),(64,5,False,True),(20,2,False,False),(60,4,False,False)}
assert set(profile)==expected

# Independent direct count of reflection-coset orders.
outside=[g for g in G if g[1] not in C5]
assert sum(aorder(g)==2 for g in outside)==20
assert sum(aorder(g)==4 for g in outside)==60

print('GL4(2)=',len(GL))
print('linear_normalizer=',len(N))
print('affine_normalizer=',len(AN))
print('orbit_profile=',sorted(profile))
print('CHECK_OK')
