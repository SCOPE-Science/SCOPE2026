#!/usr/bin/env python3
"""Exact, standalone incidence arithmetic for the 49-line dodecagon construction.
Run: python3 verify_dodecagon.py (Python 3.10+, standard library only).
"""
from collections import Counter
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import gcd, lcm

ZERO = (F(0), F(0))

def atom(n):
    return (F(n), F(0))

def add(u, v):
    return (u[0]+v[0], u[1]+v[1])

def sub(u, v):
    return (u[0]-v[0], u[1]-v[1])

def mul(u, v):
    return (u[0]*v[0]+3*u[1]*v[1],u[0]*v[1]+u[1]*v[0])

def div(u, v):
    n=v[0]*v[0]-3*v[1]*v[1]
    assert n
    return ((u[0]*v[0]-3*u[1]*v[1])/n,(u[1]*v[0]-u[0]*v[1])/n)

def cross(v,w):
    return (sub(mul(v[1],w[2]),mul(v[2],w[1])),
            sub(mul(v[2],w[0]),mul(v[0],w[2])),
            sub(mul(v[0],w[1]),mul(v[1],w[0])))

def dot(v,w):
    return add(add(mul(v[0],w[0]),mul(v[1],w[1])),mul(v[2],w[2]))

def canonical(v):
    c=next((e for e in v if e!=ZERO),None)
    assert c is not None
    return tuple(div(e,c) for e in v)

def primitive(v):
    d=lcm(*(t.denominator for z in v for t in z))
    a=[(int(z[0]*d),int(z[1]*d)) for z in v]
    g=reduce(gcd,(abs(t) for z in a for t in z))
    return tuple((x//g,y//g) for x,y in a)

# The twelve exact points (2cos(k*pi/6),2sin(k*pi/6),2) on
# the affine circle, with elements a+b*sqrt(3) stored as pairs (a,b).
x=[atom(2),(F(0),F(1)),atom(1),ZERO,atom(-1),(F(0),F(-1)),
   atom(-2),(F(0),F(-1)),atom(-1),ZERO,atom(1),(F(0),F(1))]
y=[ZERO,atom(1),(F(0),F(1)),atom(2),(F(0),F(1)),atom(1),
   ZERO,atom(-1),(F(0),F(-1)),atom(-2),(F(0),F(-1)),atom(-1)]
vertices=[(x[i],y[i],atom(2)) for i in range(12)]
sides=list(dict.fromkeys(canonical(cross(vertices[i],vertices[(i+1)%12]))
                              for i in range(12)))
assert len(sides)==12
intersection_seeds=list(dict.fromkeys(canonical(cross(v,w))
                                       for v,w in combinations(sides,2)))
assert len(intersection_seeds)==66
candidates=set(canonical(cross(v,w)) for v,w in combinations(intersection_seeds,2))
assert len(candidates)==913
rich={l:sum(dot(l,p)==ZERO for p in intersection_seeds) for l in candidates}
assert Counter(rich.values())[4]==24
lines=sorted(l for l,n in rich.items() if n>=4)
assert len(lines)==49
assert Counter(rich[l] for l in lines)==Counter({4:24,5:6,6:7,11:12})

points=set(canonical(cross(v,w)) for v,w in combinations(lines,2))
def incidence_count(p):
    return sum(dot(l,p)==ZERO for l in lines)
assert len(points)==349
assert Counter(map(incidence_count,points))==Counter({2:204,3:96,4:6,5:24,6:6,7:12,12:1})

# Primitive coefficients in the quadratic order; determinant norms
# certify the only primes where additional triple concurrences can arise.
ll=[primitive(l) for l in lines]
def imul(u,v):
    return (u[0]*v[0]+3*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def isub(u,v):
    return (u[0]-v[0],u[1]-v[1])
def iadd(u,v):
    return (u[0]+v[0],u[1]+v[1])
def icross(v,w):
    return (isub(imul(v[1],w[2]),imul(v[2],w[1])),
            isub(imul(v[2],w[0]),imul(v[0],w[2])),
            isub(imul(v[0],w[1]),imul(v[1],w[0])))
def idot(v,w):
    return iadd(iadd(imul(v[0],w[0]),imul(v[1],w[1])),imul(v[2],w[2]))
def absnorm(v):
    return abs(v[0]*v[0]-3*v[1]*v[1])
def coordinate_norm_gcd(v):
    return reduce(gcd,(absnorm(z) for z in v))
def factors(n):
    a=set();d=2
    while d*d<=n:
        if n%d==0:
            a.add(d)
            while n%d==0:n//=d
        d+=1
    if n>1:a.add(n)
    return a
bad_line_primes=set()
for v in ll:bad_line_primes |= factors(coordinate_norm_gcd(v))
bad_pair_primes=set()
for v,w in combinations(ll,2):bad_pair_primes |= factors(coordinate_norm_gcd(icross(v,w)))
assert bad_line_primes <= {2,3}
assert bad_pair_primes <= {2,3}

nonzero_norms=set(); zero_determinants=0
for i,j,k in combinations(range(49),3):
    det=idot(icross(ll[i],ll[j]),ll[k])
    if det==(0,0):
        zero_determinants+=1
    else:
        nonzero_norms.add(absnorm(det))
assert zero_determinants==1120
assert len(nonzero_norms)==60 and max(nonzero_norms)==1944
nonzero_prime_support=set()
for n in nonzero_norms:nonzero_prime_support |= factors(n)
assert nonzero_prime_support=={2,3,11,13}

def finite_line(v,p,r):
    a=tuple((u+r*w)%p for u,w in v)
    i=next(i for i,z in enumerate(a) if z)
    return tuple(z*pow(a[i],-1,p)%p for z in a)
def finite_cross(v,w,p):
    z=((v[1]*w[2]-v[2]*w[1])%p,(v[2]*w[0]-v[0]*w[2])%p,
       (v[0]*w[1]-v[1]*w[0])%p)
    if not any(z):return None
    i=next(i for i,t in enumerate(z) if t)
    return tuple(t*pow(z[i],-1,p)%p for t in z)
def finite_profile(p,r):
    ls=[finite_line(v,p,r) for v in ll]
    assert len(set(ls))==49
    pts=set(filter(None,(finite_cross(v,w,p) for v,w in combinations(ls,2))))
    return Counter(sum(sum(a*b for a,b in zip(l,q))%p==0 for l in ls) for q in pts)
for p,roots,expected in [
    (11,(5,6),{2:24,3:12,4:18,5:60,6:6,7:12,12:1}),
    (13,(4,9),{3:96,4:30,5:12,6:18,7:12,12:1}),
    (23,(7,16),{2:204,3:96,4:6,5:24,6:6,7:12,12:1})]:
    for r in roots:
        assert r*r%p==3
        profile=finite_profile(p,r)
        assert profile==Counter(expected),(p,r,profile)
        assert sum(k*(k-1)//2*v for k,v in profile.items())==1176
print('VERIFY_OK: 49 lines, 349 characteristic-zero intersections, 18424 exact determinant tests,')
print('             bad-prime support {2,3,11,13}; exceptional profiles at 11 and 13.')
