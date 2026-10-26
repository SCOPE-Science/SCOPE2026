#!/usr/bin/env python3
"""Exact GF(2) checks for the characteristic-two Barth--Nieto quintic.

Only Python's standard library is required. The proof of geometric
completeness and smoothness is mathematical and is given in RESULT.md.
"""
from itertools import combinations, product

N = 4
ZERO=(0,)*N
ONE={ZERO}
VAR=[{tuple(1 if j==i else 0 for j in range(N))} for i in range(N)]

def add(*polys):
    out=set()
    for p in polys: out ^= set(p)
    return out

def mul(a,b):
    out=set()
    for x in a:
        for y in b:
            z=tuple(x[i]+y[i] for i in range(N))
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def prod(polys):
    out=ONE
    for a in polys:out=mul(out,a)
    return out

def elem(polys,k):
    return add(*(prod(z) for z in combinations(polys,k)))

def diff(poly,i):
    return {tuple(a[j] - (j==i) for j in range(N)) for a in poly if a[i]%2}

def eva(poly,pt):
    return sum(prodint(x**e for x,e in zip(pt,ex)) for ex in poly)%2

def prodint(xs):
    v=1
    for x in xs:v*=x
    return v

# Dehomogenized chart X_5=1 around E, with X_i=1+y_i.
# e_1(X)=0 forces y_4=y_0+y_1+y_2+y_3 in GF(2).
y=VAR+[add(*VAR)]
X=[add(ONE,t) for t in y]+[ONE]
e5=elem(X,5)
C=elem(y,3)
P=prod(y)
assert e5==add(C,P), 'local polynomial identity failed'
assert all(sum(a)==3 for a in C)
assert all(sum(a)==5 for a in P)
partial=[diff(e5,i) for i in range(4)]
quad=[diff(C,i) for i in range(4)]
assert all(add(partial[i],quad[i])==diff(P,i) for i in range(4))
# Characteristic-two Euler identity: f belongs to its Jacobian ideal.
euler=add(*(mul(VAR[i],partial[i]) for i in range(4)))
assert euler==e5

# Smooth cubic tangent cone can be confirmed on P^3(F_4), not a geometric proof.
# Encode GF(4)=GF(2)[a]/(a^2+a+1).
def f4mul(a,b):
    w=(a&1)*(b&1)
    x=((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1))
    y=((a>>1)&1)*((b>>1)&1)
    return (w^y)|((x^y)<<1)
def f4pow(a,n):
    b=1
    for _ in range(n):b=f4mul(b,a)
    return b

def eva4(poly,pt):
    z=0
    for mon in poly:
        q=1
        for x,e in zip(pt,mon):q=f4mul(q,f4pow(x,e))
        z ^= q
    return z
projective=[]
for p in product(range(4),repeat=4):
    if p!=(0,0,0,0) and next((i for i,z in enumerate(p) if z),None) is not None:
        idx=next(i for i,z in enumerate(p) if z)
        if p[idx]==1:projective.append(p)
assert len(projective)==85
assert all(not all(eva4(d,p)==0 for d in quad) for p in projective)

# Exhaustive F_2 check on the original six-coordinate projective variety.
def e5six(t):
    return sum(prodint(t[j] for j in range(6) if j!=i) for i in range(6))%2

def gradient_six(t):
    return [sum(prodint(t[j] for j in range(6) if j not in (i,k))
                for k in range(6) if k!=i)%2 for i in range(6)]
pts=[p for p in product(range(2),repeat=6) if any(p) and sum(p)%2==0]
assert len(pts)==31 and all(e5six(p)==0 for p in pts)
singular=[p for p in pts if len(set(gradient_six(p)))==1]
assert len(singular)==16
assert sorted(sum(p) for p in singular)==[2]*15+[6]

# Boundary line combinatorics: 20 triples of coordinates forced to zero;
# 15 intersection points each on exactly four such lines.
triples=list(combinations(range(6),3))
assert len(triples)==20
for p in [p for p in pts if sum(p)==2]:
    assert sum(all(p[i]==0 for i in t) for t in triples)==4
for t in triples:
    assert sum(all(p[i]==0 for i in t) for p in pts)==3

# Exact homogeneous Jacobian Hilbert function over F2, by linear elimination.
def monoms(d,n=N):
    if n==1:
        yield (d,)
    else:
        for i in range(d+1):
            for rest in monoms(d-i,n-1):yield (i,)+rest

def gf2_rank(vectors):
    basis={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i not in basis:
                basis[i]=v
                break
            v^=basis[i]
    return len(basis)

h=[]
for deg in range(7):
    mm=list(monoms(deg)); lookup={v:i for i,v in enumerate(mm)}
    rows=[]
    if deg>=2:
        for mon in monoms(deg-2):
            for g in quad:
                rows.append(sum(1<<lookup[tuple(a+b for a,b in zip(mon,v))] for v in g))
    h.append(len(mm)-gf2_rank(rows))
assert h==[1,4,6,4,1,0,0],h
print('PASS local e5=e3+product, Euler, Jacobian leading quadrics')
print('PASS tangent cubic nonsingular on P^3(F4), 85 points (sanity check)')
print('PASS F2 rational geometry: 31 points, 16 singular, (15_4,20_3) boundary')
print('PASS exact gradient CI Hilbert function',h,'length 16')
print('Geometric completeness and the filtered local-length deduction use the written proof.')
