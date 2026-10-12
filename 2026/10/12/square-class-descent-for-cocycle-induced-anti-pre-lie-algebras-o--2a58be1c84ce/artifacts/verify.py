#!/usr/bin/env python3
"""Reproduce the two-dimensional cocycle-induced anti-pre-Lie classification.
Uses sympy for arbitrary-characteristic-zero identities; enumerates odd prime fields independently.
"""
import sympy as sp
from itertools import product
from collections import Counter

a,b,c=sp.symbols('a b c')
D=a*c-b*b
G=sp.Matrix([[a,b],[b,c]])
Gin=sp.Matrix([[c,-b],[-b,a]])/D
e1=sp.Matrix([1,0]);e2=sp.Matrix([0,1]);basis=[e1,e2]

def bracket(x,y): return (x[0]*y[1]-x[1]*y[0])*e2

def Cprod(x,y):
    rhs=sp.Matrix([(G*y).dot(bracket(x,z)) for z in basis])
    return (Gin*rhs).applyfunc(sp.cancel)

def zero(v): return all(sp.cancel(w)==0 for w in v)

# Exact construction relation and commutator, for all basis inputs.
for x in basis:
    for y in basis:
        xy=Cprod(x,y)
        for j,z in enumerate(basis):
            assert sp.cancel((G*xy)[j] - (G*y).dot(bracket(x,z))) == 0
        assert zero(Cprod(x,y)-Cprod(y,x)-bracket(x,y))
        for z in basis:
            defect=Cprod(x,Cprod(y,z))-Cprod(y,Cprod(x,z))
            defect -= Cprod(bracket(y,x),z)
            assert zero(defect)
            cyclic=Cprod(bracket(x,y),z)+Cprod(bracket(y,z),x)+Cprod(bracket(z,x),y)
            assert zero(cyclic)

# Formula for the four structure columns in a fixed affine Lie basis.
expected=[(-b*b,a*b),(-b*c,a*c),(-b*c,b*b),(-c*c,b*c)]
for (x,y),(p,r) in zip(product(basis, repeat=2),expected):
    assert zero(Cprod(x,y)-sp.Matrix([p/D,r/D]))

# Nondegenerate forms modulo scale (projective symmetric conic complement).
def normalize(v,q):
    lead=next(x for x in v if x%q)
    inv=pow(lead,-1,q)
    return tuple((x*inv)%q for x in v)

def structure(B,q):
    a,b,c=B;d=(a*c-b*b)%q
    assert d
    inv=pow(d,-1,q)
    data=((-b*b,a*b),(-b*c,a*c),(-b*c,b*b),(-c*c,b*c))
    return tuple((z*inv)%q for p in data for z in p)

def prod_t(T,x,y,q):
    x1,x2=x;y1,y2=y
    m=(x1*y1,x1*y2,x2*y1,x2*y2)
    return tuple(sum(m[k]*T[2*k+i] for k in range(4))%q for i in (0,1))

def affine_group(q):
    return list(product(range(q),range(1,q))) # e1 -> e1+u e2; e2 -> s e2

def pullback(B,u,s,q):
    a,b,c=B
    return ((a+2*b*u+c*u*u)%q,(s*(b+c*u))%q,(s*s*c)%q)

def basis_isom(T1,T2,u,s,q):
    Fx=(1,u);Fy=(0,s)
    for x,y in product(((1,0),(0,1)),repeat=2):
        lhs=prod_t(T1,x,y,q)
        FL=(lhs[0],(u*lhs[0]+s*lhs[1])%q)
        Fxs=Fx if x==(1,0) else Fy
        Fys=Fx if y==(1,0) else Fy
        if prod_t(T2,Fxs,Fys,q)!=FL: return False
    return True

for q in (3,5,7,11):
    forms=[(a,b,c) for a,b,c in product(range(q),repeat=3) if (a*c-b*b)%q]
    assert len(forms)==q*q*(q-1)
    projective={normalize(B,q) for B in forms}
    assert len(projective)==q*q
    fibers=Counter(structure(B,q) for B in forms)
    assert len(fibers)==q*q
    assert set(fibers.values())=={q-1}
    group=affine_group(q)

    # Independent orbit enumeration: group action on projectivized forms.
    unseen=set(projective); orbits=[]
    while unseen:
        rep=next(iter(unseen))
        orb={normalize(pullback(rep,u,s,q),q) for u,s in group}
        assert orb<=projective
        unseen-=orb
        orbits.append(orb)
    orbit_sizes=sorted(map(len,orbits))
    assert orbit_sizes==sorted((q,q*(q-1)//2,q*(q-1)//2))

    # Check all 2D anti-pre-Lie identities for each induced tensor.
    v1=(1,0);v2=(0,1);bs=(v1,v2)
    for T in fibers:
        def op(x,y): return prod_t(T,x,y,q)
        def br(x,y):
            xy=op(x,y);yx=op(y,x)
            return ((xy[0]-yx[0])%q,(xy[1]-yx[1])%q)
        assert br(v1,v2)==v2
        for x,y,z in product(bs,repeat=3):
            first=op(x,op(y,z));second=op(y,op(x,z));third=op(br(y,x),z)
            assert tuple((first[k]-second[k]-third[k])%q for k in range(2))==(0,0)
            cyclic=[op(br(x,y),z),op(br(y,z),x),op(br(z,x),y)]
            assert tuple(sum(w[k] for w in cyclic)%q for k in range(2))==(0,0)

    # Independent orbit verification via explicit isomorphism tests among products.
    T0=structure((0,1,0),q)
    sq=next(z for z in range(2,q) if pow(z,(q-1)//2,q)==q-1)
    Tplus=structure((1,0,-1),q)
    Tminus=structure((1,0,-sq),q)
    canon=[T0,Tplus,Tminus]
    hits=[]
    for T in canon:
        matching={S for S in fibers if any(basis_isom(T,S,u,s,q) for u,s in group)}
        hits.append(matching)
    assert len(set.union(*hits))==q*q
    assert all(hits[i].isdisjoint(hits[j]) for i in range(3) for j in range(i+1,3))
    assert sorted(map(len,hits))==orbit_sizes
    stabilizers=[sum(basis_isom(T,T,u,s,q) for u,s in group) for T in canon]
    assert stabilizers==[q-1,2,2]

    # Cocycles without projectivizing: q(q-1) exceptional forms, q(q-1)/2 forms in each c!=0 orbit.
    raw_unseen=set(forms); raw_orbit_sizes=[]
    while raw_unseen:
        rep=next(iter(raw_unseen))
        orbit={pullback(rep,u,s,q) for u,s in group}
        raw_unseen-=orbit
        raw_orbit_sizes.append(len(orbit))
    assert len(raw_orbit_sizes)==2*q-1
    assert Counter(raw_orbit_sizes)==Counter({q*(q-1):1,q*(q-1)//2:2*(q-1)})
    print('q=%d forms=%d projective_products=%d form_orbits=%d product_orbit_sizes=%s stabilizers=%s'%(q,len(forms),len(fibers),len(raw_orbit_sizes),sorted(map(len,hits)),stabilizers))
print('VERIFY_OK')
