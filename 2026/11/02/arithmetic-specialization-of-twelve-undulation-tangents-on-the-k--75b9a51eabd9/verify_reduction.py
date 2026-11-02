#!/usr/bin/env python3
"""Exact arithmetic verification of one quartic's undulation-line specializations.
Python standard library only. All Gaussian arithmetic and finite residue fields are exact.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

# Gaussian integers a+b*i, i^2=-1.
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm(a): return a[0]**2+a[1]**2
def divexact(a,b):
    c=mul(a,(b[0],-b[1])); d=norm(b)
    assert c[0]%d==0 and c[1]%d==0
    return (c[0]//d,c[1]//d)
def isdiv(a,b):
    c=mul(a,(b[0],-b[1])); d=norm(b)
    return c[0]%d==0 and c[1]%d==0

def nearestquot(a,b):
    c=mul(a,(b[0],-b[1])); d=norm(b)
    def rounddiv(n,d):return (2*n+d)//(2*d) if n>=0 else -((-2*n+d)//(2*d))
    return (rounddiv(c[0],d),rounddiv(c[1],d))
def ggcd(a,b):
    while b!=(0,0):
        q=nearestquot(a,b)
        a,b=b,sub(a,mul(q,b))
    return a

def zi(n):return (n,0)
I=(0,1); ONE=(1,0); ZERO=(0,0)
L=[((0,-2),zi(-1),ONE),((0,-2),ONE,ONE),((0,2),zi(-1),ONE),((0,2),ONE,ONE),
   (zi(-1),(0,-2),ONE),(ONE,(0,-2),ONE),(zi(-1),(0,2),ONE),(ONE,(0,2),ONE),
   (ONE,zi(-1),(0,-2)),(ONE,ONE,(0,-2)),(ONE,zi(-1),(0,2)),(ONE,ONE,(0,2))]
P=[(I,ONE,zi(-1)),(neg(I),ONE,ONE),(neg(I),ONE,zi(-1)),(I,ONE,ONE),
   (zi(-1),neg(I),ONE),(ONE,neg(I),ONE),(zi(-1),I,ONE),(ONE,I,ONE),
   (ONE,zi(-1),neg(I)),(ONE,ONE,neg(I)),(ONE,zi(-1),I),(ONE,ONE,I)]
assert len(L)==len(P)==12

def dot(a,b):
    r=ZERO
    for x,y in zip(a,b):r=add(r,mul(x,y))
    return r

def cross(a,b):
    return tuple(sub(mul(a[(j+1)%3],b[(j+2)%3]),mul(a[(j+2)%3],b[(j+1)%3])) for j in range(3))

def determinant(a,b,c):return dot(a,cross(b,c))

# Multivariate polynomial with integer Gaussian coefficients. Variables x,y,z.
def mono():return {(0,0,0):ONE}
def polyadd(a,b):
    o=dict(a)
    for e,c in b.items():o[e]=add(o.get(e,ZERO),c)
    return {e:c for e,c in o.items() if c!=ZERO}
def polymul(a,b):
    o={}
    for e,c in a.items():
        for f,d in b.items():
            k=tuple(x+y for x,y in zip(e,f))
            o[k]=add(o.get(k,ZERO),mul(c,d))
    return {e:c for e,c in o.items() if c!=ZERO}
def polypow(a,n):
    v=mono()
    for _ in range(n):v=polymul(v,a)
    return v
X={(1,0,0):ONE}; Y={(0,1,0):ONE}; Z={(0,0,1):ONE}
def linear(a):
    return {e:c for e,c in zip([(1,0,0),(0,1,0),(0,0,1)],a) if c!=ZERO}
def scale(a,k):return {e:mul(v,k) for e,v in a.items()}
def fm(v):
    x,y,z=v
    return add(add(mul(mul(x,x),mul(x,x)),mul(mul(y,y),mul(y,y))),
               add(mul(mul(z,z),mul(z,z)),mul(zi(3),add(add(mul(mul(x,x),mul(y,y)),
                                 mul(mul(x,x),mul(z,z))),mul(mul(y,y),mul(z,z))))))
# Every printed maximal-tangency line has an exact fourth-contact certificate
# F(s*P+t*V)=5*t^4 over Z[i], not just over a field of characteristic zero.
for ell,p in zip(L,P):
    assert dot(ell,p)==ZERO
    v=(ONE,ZERO,neg(ell[0])) if ell[2]==ONE else (neg(ell[1]),ONE,ZERO)
    assert dot(ell,v)==ZERO
    assert cross(p,v)!=(ZERO,ZERO,ZERO)
    for j in range(5):
        pt=tuple(add(mul(zi(j),p[k]),v[k]) for k in range(3))
        assert fm(pt)==zi(5), (ell,j,fm(pt))
    # polynomial degree 4: five distinct integer evaluations determine the identity.

norms=Counter()
for ids in combinations(range(12),3):
    d=determinant(*(L[i] for i in ids))
    n=norm(d)
    assert n>0
    norms[n]+=1
assert norms==Counter({4:8,20:48,36:24,40:24,64:12,80:48,100:48,200:8})
assert sum(norms.values())==comb(12,3)==220
assert all(n%p!=0 for n in norms for p in [7,11,13,17,19])

# Each generic pair is a distinct K=Q(i) point, and its Gaussian-primitive
# coordinates define a section of P^2_{Z[i]} extending it over every prime.
primitives={}
for a,b in combinations(range(12),2):
    v=cross(L[a],L[b]); assert v!=(ZERO,ZERO,ZERO)
    g=ggcd(ggcd(v[0],v[1]),v[2])
    assert g!=(ZERO,ZERO)
    w=tuple(divexact(t,g) for t in v)
    assert norm(ggcd(ggcd(w[0],w[1]),w[2]))==1
    primitives[(a+1,b+1)]=w
assert len(primitives)==66

# Residue rings: characteristic 3 inert (Fp[i]=F9), above 5 choose i=2 or 3.
# Above 2, residue field F2 with i=1.
def residue(a,p,root=None):
    if root is None:return (a[0]%p,a[1]%p)
    return (a[0]+root*a[1])%p

def radd(a,b,p):
    if isinstance(a,tuple):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    return (a+b)%p
def rmul(a,b,p):
    if isinstance(a,tuple):return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    return (a*b)%p
def rinv(a,p):
    if isinstance(a,tuple):
        n=(a[0]*a[0]+a[1]*a[1])%p
        assert n
        inv=pow(n,-1,p)
        return (a[0]*inv%p,-a[1]*inv%p)
    return pow(a,-1,p)

def normalize(v,p):
    for z in v:
        if z!=(0,0) and z!=0:
            inv=rinv(z,p)
            return tuple(rmul(t,inv,p) for t in v)
    raise AssertionError('zero projective vector')

def reducev(v,p,root=None):
    return tuple(residue(z,p,root) for z in v)

def line_points(p,root):
    out=defaultdict(list)
    for ab,w in primitives.items():
        pt=normalize(reducev(w,p,root),p)
        out[pt].append(ab)
    return out

# Good characteristic: all line pairs give distinct intersection points.
good=line_points(7,None)
assert len(good)==66 and Counter(map(len,good.values()))==Counter({1:66})

# Characteristic 3: six quadruple points and thirty double points.
p3=line_points(3,None)
assert len(p3)==36 and Counter(map(len,p3.values()))==Counter({1:30,6:6})
q3={pt for pt,pairs in p3.items() if len(pairs)==6}
for pt in q3:
    assert sum(z==(0,0) for z in pt)==1
    assert radd(radd(rmul(pt[0],pt[0],3),rmul(pt[1],pt[1],3),3),rmul(pt[2],pt[2],3),3)==(0,0)
# The specialized line set becomes the dual to the twelve original MTPs.
assert len({normalize(reducev(t,3),3) for t in L})==12
assert {normalize(reducev(t,3),3) for t in L}=={normalize(reducev(t,3),3) for t in P}

# The Hermitian quartic in characteristic 3 has 28 rational points in P^2(F9),
# and their polar tangents are 28 distinct lines, including our twelve.
F9=[(a,b) for a in range(3) for b in range(3)]
Hpts=set()
for v in __import__('itertools').product(F9,repeat=3):
    if v==((0,0),)*3:continue
    pt=normalize(v,3)
    v4=[rmul(rmul(z,z,3),rmul(z,z,3),3) for z in pt]
    if radd(radd(v4[0],v4[1],3),v4[2],3)==(0,0):Hpts.add(pt)
assert len(Hpts)==28
T={normalize(tuple(rmul(rmul(z,z,3),z,3) for z in pt),3) for pt in Hpts}
assert len(T)==28
assert {normalize(reducev(t,3),3) for t in L}.issubset(T)

# Characteristic 5, for both primes over 5, the pair sections reduce to all
# 18 rational points on the four-line special fiber: node weight 9, other 12 weight 1.
F5special=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
for root in (2,3):
    buckets=line_points(5,root)
    assert len(buckets)==18
    assert Counter(map(len,buckets.values()))==Counter({9:6,1:12})
    nodal=[]
    smooth=[]
    for pt,pairs in buckets.items():
        n=sum(sum(a*b for a,b in zip(eq,pt))%5==0 for eq in F5special)
        assert n==(2 if len(pairs)==9 else 1)
        (nodal if n==2 else smooth).append(pt)
    assert len(nodal)==6 and len(smooth)==12
    all_points=set()
    for v in __import__('itertools').product(range(5),repeat=3):
        if v==(0,0,0):continue
        if any(sum(a*b for a,b in zip(eq,v))%5==0 for eq in F5special):
            all_points.add(normalize(v,5))
    assert len(all_points)==18 and set(buckets)==all_points
    # Each of the four distinct limiting lines represents precisely 3 labels.
    limits={normalize(reducev(v,5,root),5) for v in L}
    assert len(limits)==4
    assert Counter(normalize(reducev(v,5,root),5) for v in L)==Counter({z:3 for z in limits})

# Characteristic 2: three coincident four-tuples, and the 66 marked
# intersections yield 7 support points, not merely the common concurrency.
p2=line_points(2,1)
assert Counter(map(len,p2.values()))==Counter({48:1,4:3,2:3})
assert {pt:len(pairs) for pt,pairs in p2.items()}=={
    (1,1,1):48,(1,0,0):4,(0,1,0):4,(0,0,1):4,
    (1,1,0):2,(1,0,1):2,(0,1,1):2}
assert Counter(normalize(reducev(v,2,1),2) for v in L)==Counter({(0,1,1):4,(1,0,1):4,(1,1,0):4})

# Coefficient-level quartic reductions: Q^2 modulo 2 and minus the
# four general-position lines modulo 5.
F=polyadd(polyadd(polypow(X,4),polypow(Y,4)),polypow(Z,4))
for A,B in ((X,Y),(X,Z),(Y,Z)):
    F=polyadd(F,scale(polymul(polypow(A,2),polypow(B,2)),zi(3)))
Q=polyadd(polyadd(polypow(X,2),polypow(Y,2)),polypow(Z,2))
for A,B in ((X,Y),(X,Z),(Y,Z)):Q=polyadd(Q,polymul(A,B))
prod=mono()
for eq in F5special:prod=polymul(prod,linear(tuple(zi(z) for z in eq)))
def polyeqmod(a,b,p):
    return all(sub(a.get(e,ZERO),b.get(e,ZERO))[0]%p==0 and
               sub(a.get(e,ZERO),b.get(e,ZERO))[1]%p==0 for e in set(a)|set(b))
assert polyeqmod(F,polypow(Q,2),2)
assert polyeqmod(F,scale(prod,zi(-1)),5)

print('KOMIYA_KURIBAYASHI_PRIMITIVE_66_SECTION_ARITHMETIC_AND_HERMITIAN_JUMP_OK')
print('triple_norms',dict(sorted(norms.items())))
print('characteristic_3_weights',dict(sorted(Counter(map(len,p3.values())).items())))
print('characteristic_5_weights',dict(sorted(Counter(map(len,line_points(5,2).values())).items())))
print('characteristic_2_weights',dict(sorted(Counter(map(len,p2.values())).items())))
