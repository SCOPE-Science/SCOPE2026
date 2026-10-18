#!/usr/bin/env python3
"""Exact classification of all-smooth binary (2,2) pencils on P^1 x P^1.

Bit (3*i+j) represents u^(2-i)v^i s^(2-j)t^j, i,j in {0,1,2}.
Uses Groebner unit-ideal tests over F_2 on all four standard affine charts.
The field-extension calculation checks the Frobenius cycles of the reduced
base scheme of one representative in each automorphism orbit.
"""
from collections import Counter
from itertools import product
import sympy as sp
x,y=sp.symbols('x y')
MONS=list(product(range(3),repeat=2))
CHARTS=[[(i if a==0 else 2-i,j if b==0 else 2-j) for i,j in MONS]
        for a,b in product(range(2),repeat=2)]

def polynomial(mask, exponents):
    return sum(x**a*y**b for k,(a,b) in enumerate(exponents) if mask&(1<<k))

def unit_ideal(gens):
    G=sp.groebner(gens,x,y,modulus=2)
    return len(G.polys)==1 and G.polys[0].as_expr()==1

def smooth(mask):
    for chart in CHARTS:
        F=polynomial(mask,chart)
        if not unit_ideal((F,sp.diff(F,x),sp.diff(F,y))): return False
    return True

S={a for a in range(1,512) if smooth(a)}
assert len(S)==144
P={tuple(sorted((a,b,a^b))) for a in S for b in S if a<b and a^b in S}
assert len(P)==804
# A net containing (a,b,a+b) must have a fourth smooth form d whose
# translates by the three nonzero pencil forms are all smooth.
assert not any(all(d^e in S for e in p) for p in P for d in S if d not in p)

# Standard rational points in P^1(F2), with evaluated bidegree-two monomials.
V=[(1,0,0),(0,0,1),(1,1,1)]
PV=list(product(V,V))
def ev(mask,AA,BB):
    return sum((mask>>(3*i+j)&1)*AA[i]*BB[j] for i,j in MONS)%2
N={a:sum(ev(a,A,B)==0 for A,B in PV) for a in S}
BASE=Counter(); TRIP=Counter()
for a,b,c in P:
    n=sum(ev(a,A,B)==0 and ev(b,A,B)==0 for A,B in PV)
    BASE[n]+=1;TRIP[(tuple(sorted((N[a],N[b],N[c]))),n)]+=1
assert BASE==Counter({0:84,1:504,2:216})
assert TRIP==Counter({((2,3,4),0):72, ((3,3,3),0):12,
 ((2,4,5),1):216,((3,3,5),1):72,((3,4,4),1):216,
 ((3,5,5),2):108,((4,4,5),2):108})

def transverse_base(a,b):
    for chart in CHARTS:
        F=polynomial(a,chart);G=polynomial(b,chart)
        J=sp.diff(F,x)*sp.diff(G,y)+sp.diff(F,y)*sp.diff(G,x)
        if not unit_ideal((F,G,J)): return False
    return True
assert all(transverse_base(a,b) for a,b,c in P)

# Group Aut_F2(P1 x P1) = (PGL2(F2)^2) semidirect C2, order 72.
GL=[]
for a,b,c,d in product((0,1),repeat=4):
    if (a*d ^ b*c)==1:
        T=((a,0,b),(a*c,a*d^b*c,b*d),(c,0,d))
        GL.append(T)
assert len(GL)==6
ACTIONS=list(product(GL,GL,(0,1)))
assert len(ACTIONS)==72

def transform(z,T,U,swap):
    C=[[((z>>(3*i+j))&1) for j in range(3)] for i in range(3)]
    if swap: C=[list(row) for row in zip(*C)]
    D=[[sum(T[i][k]*C[i][j]*U[j][l] for i in range(3) for j in range(3))%2
          for l in range(3)] for k in range(3)]
    return sum(D[i][j]<<(3*i+j) for i,j in MONS)

remaining=set(P); ORBITS=[]
while remaining:
    p=min(remaining)
    orbit={tuple(sorted(transform(z,T,U,w) for z in p)) for T,U,w in ACTIONS}
    assert orbit<=remaining
    remaining-=orbit
    a,b,c=min(orbit)
    n=sum(ev(a,A,B)==ev(b,A,B)==0 for A,B in PV)
    ORBITS.append((min(orbit),len(orbit),n,tuple(sorted((N[a],N[b],N[c])))))
assert len(ORBITS)==13
assert sum(row[1] for row in ORBITS)==804
assert Counter(row[1] for row in ORBITS)==Counter({72:10,36:2,12:1})

# Exact extension-field point counts on reduced degree-eight base schemes.
POLY={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,
      6:0b1000011,7:0b10000011,8:0b100011011}
for degree,modulus in POLY.items():
    assert sp.Poly(sum(x**k for k in range(degree+1) if modulus>>k&1),x,modulus=2).is_irreducible

def mult(a,b,degree,modulus):
    out=0
    while b:
        if b&1:out ^= a
        b >>=1; a <<=1
        if a&(1<<degree):a ^=modulus
    return out

def count_base_extension(a,b,degree):
    q=1<<degree
    table=[[mult(i,j,degree,POLY[degree]) for j in range(q)] for i in range(q)]
    pts=[(1,k,table[k][k]) for k in range(q)]+[(0,0,1)]
    count=0
    for AA in pts:
        for BB in pts:
            av=bv=0
            for k,(i,j) in enumerate(MONS):
                t=table[AA[i]][BB[j]]
                if a>>k&1:av ^=t
                if b>>k&1:bv ^=t
            if av==bv==0:count +=1
    return count

SPECTRUM=Counter(); DETAILS=[]
for (a,b,c),weight,base,counts in ORBITS:
    pts={d:count_base_extension(a,b,d) for d in range(1,9)}
    cycles={}
    for d in range(1,9):
        numerator=pts[d]-sum(j*cycles[j] for j in range(1,d) if d%j==0)
        assert numerator>=0 and numerator%d==0
        cycles[d]=numerator//d
    partition=tuple(d for d in range(1,9) for _ in range(cycles[d]))
    assert sum(partition)==8
    SPECTRUM[partition]+=weight
    DETAILS.append((a,b,c,weight,base,counts,partition))
assert SPECTRUM==Counter({(8,):72,(2,3,3):12,(1,7):288,(1,2,5):216,(1,1,6):216})
print('smooth forms:',len(S))
print('smooth pencils:',len(P),'orbits:',len(ORBITS),'smooth nets: 0')
print('rational base counts:',sorted(BASE.items()))
print('curve rational-point triples and base counts:',sorted(TRIP.items()))
print('Frobenius base-cycle partitions:',sorted(SPECTRUM.items()))
print('orbit representatives: (a,b,a XOR b; size; rational base; curve point triple; Frobenius partition)')
for row in sorted(DETAILS, key=lambda z:(z[6],z[3],z[:3])): print(row)
print('PASS')
