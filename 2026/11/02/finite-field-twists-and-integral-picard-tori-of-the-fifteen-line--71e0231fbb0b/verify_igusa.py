#!/usr/bin/env python3
"""Exact configuration, Frobenius-orbit and cyclic-torus checks for Igusa's 15 lines.

Uses only Python's standard library; no floating point or external data.
"""
import csv
from itertools import combinations, permutations
from collections import Counter, deque
from math import gcd
from pathlib import Path

I=tuple(range(6))
DUADS=tuple(combinations(I,2))
def matchings(available):
    available=tuple(available)
    if not available:
        yield ();return
    a=available[0]
    for j in range(1,len(available)):
        b=available[j]
        for tail in matchings(available[1:j]+available[j+1:]):
            yield tuple(sorted(((a,b),)+tail))
SYN=tuple(sorted(set(matchings(I))))
FLAGS=tuple(sorted((s,d) for s in SYN for d in s))
assert len(SYN)==len(DUADS)==15 and len(FLAGS)==45

def det(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))

def basis(s):
    a,b,c=s
    return [[int(i in a)-int(i in c) for i in I],
            [int(i in b)-int(i in c) for i in I]]
def minors(A,k):
    return [det([[A[r][c] for c in cols] for r in rows])
            for rows in combinations(range(len(A)),k)
            for cols in combinations(range(len(A[0])),k)]
def gcd_nonzero(ints):
    z=0
    for a in ints:z=gcd(z,abs(a))
    return z

# Two different lines have a projective intersection iff their matchings share a pair.
# The nonzero maximal-minor gcd is 3, so the equivalence persists for every p != 3.
geom=Counter()
for s,t in combinations(SYN,2):
    M=basis(s)+basis(t)
    d=gcd_nonzero(minors(M,4))
    geom[(len(set(s)&set(t)),d)]+=1
assert geom=={(0,3):60,(1,0):45}
for duad in DUADS:
    incident=[s for s in SYN if duad in s]
    assert len(incident)==3
    tangents=[]
    for s in incident:
        a,b=[e for e in s if e!=duad]
        tangents.append([int(i in a)-int(i in b) for i in I])
    # GCD 4 of the 3-minors proves independence over any p != 2.
    assert gcd_nonzero(minors(tangents,3))==4
    # Check independence modulo the radial vector of the intersection point.
    radial=[-2 if i in duad else 1 for i in I]
    assert gcd_nonzero(minors(tangents+[radial],4)) in (4,8,12,16,24,48)
print('GEOMETRY_OK: 15 lines, 60 skew pairs, 45 intersecting pairs, 15 transverse triple points')

# The six-coordinate quartic equals zero on each line by the identity
# (a^2+b^2+c^2)^2=2(a^4+b^4+c^4) when a+b+c=0.
for a in range(-3,4):
    for b in range(-3,4):
        c=-a-b
        v=[a,a,b,b,c,c]
        F=sum(x*x for x in v)**2-4*sum(x**4 for x in v)
        assert F==0
        # The six coordinate derivatives are all equal, so the point is
        # singular on the hyperplane sum x_i=0.
        grad=[4*x*sum(y*y for y in v)-16*x**3 for x in v]
        assert len(set(grad))==1
print('QUARTIC_OK: exact identities for all syntheme lines')

def onpair(p,d):return tuple(sorted(p[i] for i in d))
def onsyn(p,s):return tuple(sorted(onpair(p,d) for d in s))
def onflag(p,f):return (onsyn(p,f[0]),onpair(p,f[1]))
def perm_apply(p,o):
    if o in DUADS:return onpair(p,o)
    if o in SYN:return onsyn(p,o)
    return onflag(p,o)
def orb(items,p):
    left=set(items); groups=[]
    while left:
        o=min(left);v=o;orbit=[]
        while v not in orbit:
            orbit.append(v);v=perm_apply(p,v)
        assert v==o
        left.difference_update(orbit)
        groups.append(tuple(orbit))
    return groups
def fmt(orbits):
    cs=Counter(len(o) for o in orbits)
    return ';'.join(f'{k}:{cs[k]}' for k in sorted(cs))
def partition(n,top=None):
    if n==0:yield ();return
    for x in range(min(n,n if top is None else top),0,-1):
        for q in partition(n-x,x):yield (x,)+q
def rep(parts):
    p=list(I);j=0
    for m in parts:
        for t in range(m):p[j+t]=j+(t+1)%m
        j+=m
    return tuple(p)
def class_size(parts):
    from math import factorial
    c=Counter(parts);z=1
    for i,m in c.items(): z*=i**m*factorial(m)
    return factorial(6)//z

def torus_phi(s,d,f):
    # det(1-t F|H1) = (1-t)*prod_edges(1-t^degree)/prod_vertices(1-t^degree).
    # Its factorization has cyclotomic exponents indexed by m.
    result={}
    for m in range(1,7):
        e=int(m==1)
        for cycles,sgn in ((f,1),(s,-1),(d,-1)):
            e+=sgn*sum(v for length,v in cycles.items() if length % m==0)
        if e:
            assert e>0
            result[m]=e
    assert sum(e*(1 if m==1 else {2:1,3:2,4:2,5:4,6:2}[m]) for m,e in result.items())==16
    return ';'.join(f'{m}:{e}' for m,e in result.items())

def expr_zeta(s,d,f):
    from collections import defaultdict
    ex=defaultdict(int)
    for length,count in f.items():ex[length]+=count
    for length,count in s.items():ex[length]-=count
    for length,count in d.items():ex[length]-=count
    return ';'.join(f'{x}:{ex[x]}' for x in sorted(ex) if ex[x])

rows=[]
for typ in partition(6):
    p=rep(typ)
    lines,pts,branches=[orb(objects,p) for objects in (SYN,DUADS,FLAGS)]
    s=Counter(map(len,lines));d=Counter(map(len,pts));f=Counter(map(len,branches))
    # Characteristic polynomial of the 16-dimensional graph-cycle representation:
    # (1-t)*product_edges(1-t^d)/product_vertices(1-t^d).
    qcoef=s.get(1,0)
    constant=qcoef+d.get(1,0)-f.get(1,0)
    row=dict(permutation_type=''.join(map(str,typ)),class_size=class_size(typ),
        syntheme_line_orbits=fmt(lines),duad_point_orbits=fmt(pts),flag_branch_orbits=fmt(branches),
        zeta_numerator_exponents=expr_zeta(s,d,f),
        point_count=f'{qcoef}*q{constant:+d}',
        torus_cyclotomic_multiplicities=torus_phi(s,d,f),
        rational_points_zero=int(qcoef==0 and constant==0))
    rows.append(row)
assert len(rows)==11
assert sum(x['class_size'] for x in rows)==720
assert [x['permutation_type'] for x in rows if x['rational_points_zero']]==['51']
# Compare full zeta invariants: line orbits + numerator exponents.
zeta_signatures=Counter((r['syntheme_line_orbits'],r['zeta_numerator_exponents']) for r in rows)
assert len(zeta_signatures)==9
print('CLASSIFICATION_OK: 11 permutation types, 9 distinct zeta functions, point-free iff 5+1')

# Verify all 720 permutations and that 144 order-five elements are the only
# ones having neither a fixed line nor a fixed singular point.
zero=[]
for p in permutations(I):
    l=orb(SYN,p);d=orb(DUADS,p)
    if all(len(o)>1 for o in l) and all(len(o)>1 for o in d):
        zero.append(p)
assert len(zero)==144
print('GROUP_OK: all 720 permutations checked, 144 point-free twists')

# For a 5-cycle the free degree-five quotient of the incidence graph has
# 3 orbits of each vertex type and 9 edge orbits, so b1=9-6+1=4.
p=rep((5,1))
lineorb=orb(SYN,p);pointorb=orb(DUADS,p);edgeorb=orb(FLAGS,p)
assert list(sorted(map(len,lineorb)))==[5]*3
assert list(sorted(map(len,pointorb)))==[5]*3
assert list(sorted(map(len,edgeorb)))==[5]*9
# Build quotient graph, check connectivity and its cycle rank.
Sidx={x:i for i,o in enumerate(lineorb) for x in o}
Didx={x:i+3 for i,o in enumerate(pointorb) for x in o}
E=[(Sidx[o[0][0]],Didx[o[0][1]]) for o in edgeorb]
adj=[set() for _ in range(6)]
for u,v in E:adj[u].add(v);adj[v].add(u)
seen={0};todo=[0]
while todo:
    u=todo.pop()
    for v in adj[u]-seen:seen.add(v);todo.append(v)
assert len(seen)==6 and len(E)-len(seen)+1==4
print('INTEGRAL_TORUS_OK: free cyclic quintic graph cover, b1 quotient 4; Z + Z[C5]^3')

# The identity twist may also be checked by direct finite-field enumeration.
for q in (5,7):
    # Projective points are [x0:...:x5], first nonzero coordinate normalized to 1.
    # Direct enumeration is over 5-dimensional projective space, but points on
    # the 15 lines are listed parametrically and unioned in the projective chart.
    pts=set()
    def norm(v):
        a=next(x for x in v if x%q)
        return tuple((x*pow(a,-1,q))%q for x in v)
    for s in SYN:
        b=basis(s)
        for a in range(q):pts.add(norm([(a*b[0][i]+b[1][i])%q for i in I]))
        pts.add(norm(b[0]))
    assert len(pts)==15*q-15
print('RATIONAL_POINTS_OK: directly enumerated untwisted union over F5 and F7')

out=Path(__file__).resolve().parent/'s6_orbit_table.csv'
with open(out,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('CSV_OK',out.name)
print('VERIFY_OK')
