#!/usr/bin/env python3
"""Reproducible exact checks for a characteristic-two quartic surface.

Requires Python 3 stdlib and a C11 compiler. Run from the directory containing
this file and count.c: python3 verify.py
"""
import json
import pathlib
import re
import shutil
import subprocess
import tempfile
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
POLY = {1:0x3,2:0x7,3:0xb,4:0x13,5:0x25,6:0x43,
        7:0x83,8:0x11b,9:0x203,10:0x409,11:0x805,12:0x1009}

def rem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b << (a.bit_length()-b.bit_length())
    return a

def gcd(a,b):
    while b: a,b=b,rem(a,b)
    return a

def mul(a,b,m):
    irr=POLY[m]; out=0; bit=1<<m
    while b:
        if b&1: out^=a
        b>>=1; a<<=1
        if a&bit: a^=irr
    return out

def power(a,n,m):
    z=1
    while n:
        if n&1:z=mul(z,a,m)
        a=mul(a,a,m);n//=2
    return z

def irreducible(m):
    f=POLY[m]; x=rem(2,f); t=x
    for i in range(1,m+1):
        t=mul(t,t,m)
        if m%i==0 and i<m and gcd(t^x,f)!=1:
            return False
    return t==x

# This Rabin-type criterion checks gcd at all proper divisors of m,
# which is stronger than checking just at the prime-index divisors.
assert all(irreducible(m) for m in range(1,13))
assert all(power(a,(1<<m)-1,m)==1 for m in range(1,13)
           for a in range(1,1<<m))

# Independent small-field direct enumeration of the quartic, not using trace.
def direct_count(m):
    q=1<<m
    a=0
    # Affine chart x=1, F=w^4+w^2+y+y^3 z+z^3.
    for w in range(q):
        w4=power(w,4,m); w2=power(w,2,m)
        for y in range(q):
            y3=power(y,3,m)
            for z in range(q):
                if w4 ^ w2 ^ y ^ mul(y3,z,m) ^ power(z,3,m)==0:
                    a+=1
    # For each [y:z] in P1 on x=0, w^4=y^3*z has a unique solution.
    return a+q+1

# Independently reconstruct the Frobenius orbits of the 14 singularities
# over F64, without assuming their orbit lengths.
M=6
roots7=[a for a in range(1,64) if power(a,7,M)==1]
assert len(roots7)==7
nodes=set()
for eps in roots7:
    B=eps
    wroots=[w for w in range(64) if power(w,4,M)^power(w,2,M)==B]
    assert len(wroots)==2
    for w in wroots:
        nodes.add((w,eps,power(eps,5,M)))
assert len(nodes)==14
remaining=set(nodes);orbits=[]
while remaining:
    w,y,z=min(remaining);seq=[];p=(w,y,z)
    while p not in seq:
        assert p in remaining
        seq.append(p);remaining.remove(p)
        p=tuple(mul(v,v,M) for v in p)
    assert p==seq[0]
    orbits.append(len(seq))
assert sorted(orbits)==[2,3,3,6],orbits

if not shutil.which('cc'):
    raise RuntimeError('C11 compiler cc is required to reproduce the 12 exhaustive sums')
with tempfile.TemporaryDirectory() as temp:
    binfile=pathlib.Path(temp)/'exact_count'
    subprocess.run(['cc','-O3','-std=c11','-Wall','-Wextra',str(ROOT/'count.c'),'-o',str(binfile)],check=True)
    p=subprocess.run([str(binfile),'12'],check=True,text=True,capture_output=True)
    lines=p.stdout.strip().splitlines()
assert len(lines)==12
rows=[]
for line in lines:
    pairs=re.findall(r'([A-Za-z0-9_]+)=(-?\d+)',line)
    row={k:int(v) for k,v in pairs}
    rows.append(row)
for i,row in enumerate(rows,1):
    q=1<<i
    assert row['m']==i and row['q']==q
    assert row['X']==q*q+q+1+row['S']
    expected_nodes=sum(d for d in orbits if i%d==0)
    assert row['singular_rational']==expected_nodes
    assert row['Y']==row['X']+q*expected_nodes
    assert row['normalized_trace']==(row['Y']-1-q*q)//q
    if i<=4:assert row['X']==direct_count(i),(i,row['X'],direct_count(i))

s=[row['normalized_trace'] for row in rows]
coeff=[Fraction(1)]
for n in range(1,13):
    coeff.append(-sum(coeff[n-i]*s[i-1] for i in range(1,n+1))/n)
assert all(c.denominator==1 for c in coeff)
assert [int(v) for v in coeff]==[1,0,-2,-3,1,6,3,-3,-6,0,3,0,-3]
# Weight-two cohomology of a K3 surface gives inverse-root pairing.
# c12=-c10, so the sign of the reciprocal functional equation is -1.
assert coeff[12]==-coeff[10] and coeff[10]!=0
full=[int(x) for x in coeff]+[-int(coeff[22-i]) for i in range(13,23)]

def prod(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]+=ai*bj
    return c

def powpoly(a,n):
    out=[1]
    for _ in range(n):out=prod(out,a)
    return out

phi1=[1,-1];phi2=[1,1];phi3=[1,1,1];phi6=[1,-1,1]
phi18=[1,0,0,-1,0,0,1]
PY=[1]
for f,n in [(phi1,5),(phi2,3),(phi6,1),(phi3,3),(phi18,1)]:
    PY=prod(PY,powpoly(f,n))
assert PY==full
exc=prod(prod([1,0,-1],powpoly([1,0,0,-1],2)),[1,0,0,0,0,0,-1])
PX=prod(prod(phi1,phi2),phi18)
assert PY==prod(exc,PX)

# Exact all-extension formula for the original singular quartic.
def c18(n):
    return 3*(n%3==0)-6*(n%6==0)-9*(n%9==0)+18*(n%18==0)
def predicted_x(n):
    q=1<<n
    return 1+q*q+q*(1+(-1)**n+c18(n))
assert all(predicted_x(i)==row['X'] for i,row in enumerate(rows,1))

print('FINITE_FIELD_POLYNOMIALS_IRREDUCIBLE',sorted(POLY.items()))
print('SINGULAR_ORBIT_LENGTHS',sorted(orbits))
print('NORMALIZED_TRACES',s)
print('K3_H2_NORMALIZED_DETERMINANT_FACTORS','Phi1^5 Phi2^3 Phi3^3 Phi6 Phi18')
print('SINGULAR_X_H2_NORMALIZED_DETERMINANT_FACTORS','Phi1 Phi2 Phi18')
print('COUNTS_X',[(r['m'],r['X']) for r in rows])
print('VERIFY_OK')
