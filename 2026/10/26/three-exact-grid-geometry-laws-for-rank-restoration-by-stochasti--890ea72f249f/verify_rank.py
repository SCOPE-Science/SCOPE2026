#!/usr/bin/env python3
"""Exact-rational checks for two-column stochastic-rounding rank laws."""
from fractions import Fraction as F
from itertools import product
from math import comb,exp,log

def formula(n,p,q):
    return 1-(1-p)**n-(1-q)**n-(1-p-q+2*p*q)**n+2*((1-p)*(1-q))**n

def brute(n,p,q):
    d={}
    for x,y in product((0,1),repeat=2):
        d[(x,y)]=(p if x else 1-p)*(q if y else 1-q)
    out=F(0)
    for rows in product(d,repeat=n):
        rank2=any(rows[i][0]*rows[j][1] != rows[i][1]*rows[j][0] for i in range(n) for j in range(i+1,n))
        if rank2:
            z=F(1)
            for row in rows:z*=d[row]
            out+=z
    return out

checks=0
for n in range(2,7):
 for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
  for q in (F(0),F(1,3),F(2,3),F(1)):
   got=formula(n,p,q)
   assert got==brute(n,p,q),(n,p,q,got)
   checks+=1
for n in range(2,16):
 for p,q in ((F(1,4),F(3,4)),(F(1,2),F(1,2)),(F(2,3),F(3,4))):
  f=formula(n,p,q)
  lo=1 - ((1-p)**n+(1-q)**n+(1-p-q+2*p*q)**n)
  hi=1-max((1-p)**n,(1-q)**n,(1-p-q+2*p*q)**n)
  assert lo<=f<=hi
  checks+=1
for a,b in ((.4,2.5),(2.0,1.1),(0.,4.),(5.,3.)):
 for n in (1000,4000,16000):
  assert abs(float(formula(n,a/n,b/n))-(1-exp(-a))*(1-exp(-b)))<.035
  assert abs(float(formula(n,1-a/n,1-b/n))-(1-exp(-(a+b))))<.035
  checks+=2
for n in (2,3,6,12,30):
 assert formula(n,F(1,2),F(1,2))==1-3*F(1,2)**n+2*F(1,4)**n
 checks+=1
assert formula(3,F(1),F(1,2))==F(3,4)
assert formula(3,F(2,3),F(2,3))>F(3,4)
checks+=2
def heterogeneous(ps,qs):
    def prod(a):
        ans=F(1)
        for z in a: ans*=z
        return ans
    return 1-prod([1-p for p in ps])-prod([1-q for q in qs])-prod([1-p-q+2*p*q for p,q in zip(ps,qs)])+2*prod([(1-p)*(1-q) for p,q in zip(ps,qs)])

def hetero_brute(ps,qs):
    n=len(ps)
    prob=F(0)
    for rows in product(((0,0),(1,0),(0,1),(1,1)), repeat=n):
        if not any(rows[i][0]*rows[j][1]!=rows[i][1]*rows[j][0] for i in range(n) for j in range(i+1,n)):
            continue
        z=F(1)
        for (x,y),p,q in zip(rows,ps,qs):
            z*= (p if x else 1-p) * (q if y else 1-q)
        prob+=z
    return prob
for n in (2,3,4):
    for shift in range(17):
        ps=[F(1+(shift+2*i)%5,6) for i in range(n)]
        qs=[F(1+(2*shift+3*i)%6,7) for i in range(n)]
        assert heterogeneous(ps,qs)==hetero_brute(ps,qs)
        checks+=1
for a in (.25,.75,3.0):
    sparse=(1-exp(-a))**2
    dense=1-exp(-2*a)
    assert dense>sparse
    for n in (250,1000,4000):
        r=a/n
        assert abs(float(formula(n,r,r))-sparse)<.025
        assert abs(float(formula(n,1-r,1-r))-dense)<.025
        checks+=2
print('PASS',checks,'exact-rational / numerical tests')

# Three distinct geometric collinearity classes for a common quantization bin.
def probability_by_geometry(n,p,q,L,U):
    a=(1-p)*(1-q);b=p*(1-q);c=(1-p)*q;d=p*q
    assert L<U
    if L==0: return formula(n,p,q)
    if U==0: return formula(n,1-p,1-q)
    if L+U==0: return 1-(a+d)**n-(b+c)**n
    return 1-(a+d)**n-b**n-c**n

def brute_geometry(n,p,q,L,U):
    row_probs={(L,L):(1-p)*(1-q),(U,L):p*(1-q),(L,U):(1-p)*q,(U,U):p*q}
    assert len(row_probs)==4
    out=F(0)
    for rows in product(row_probs,repeat=n):
        if any(rows[i][0]*rows[j][1]!=rows[i][1]*rows[j][0] for i in range(n) for j in range(i+1,n)):
            z=F(1)
            for x in rows:z*=row_probs[x]
            out+=z
    return out

extra=0
for L,U in ((F(0),F(1)),(F(-1),F(0)),(F(-1),F(1)),(F(1),F(2)),(F(-3),F(-2)),(F(-2),F(1))):
 for n in (2,3,4,5):
  for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
   for q in (F(0),F(1,3),F(2,3),F(1)):
    assert probability_by_geometry(n,p,q,L,U)==brute_geometry(n,p,q,L,U)
    extra+=1
p=q=F(1,4)
vals=[probability_by_geometry(2,p,q,*T) for T in ((F(0),F(1)),(F(-1),F(1)),(F(1),F(2)))]
assert vals==[F(15,128),F(15,32),F(69,128)], vals
assert vals[0]<vals[1]<vals[2]
print('PASS',extra,'additional exact-rational geometry checks; total',checks+extra)

def heterogeometry(ps,qs,L,U):
    def prod(xs):
        res=F(1)
        for x in xs:res*=x
        return res
    terms=[((1-p)*(1-q),p*(1-q),(1-p)*q,p*q) for p,q in zip(ps,qs)]
    if L==0:return heterogeneous(ps,qs)
    if U==0:return heterogeneous([1-p for p in ps],[1-q for q in qs])
    diag=prod([a+d for a,b,c,d in terms])
    if L+U==0:return 1-diag-prod([b+c for a,b,c,d in terms])
    return 1-diag-prod([b for a,b,c,d in terms])-prod([c for a,b,c,d in terms])

def brute_heterogeometry(ps,qs,L,U):
    out=F(0);n=len(ps)
    for bits in product(((0,0),(1,0),(0,1),(1,1)),repeat=n):
        rows=[(U if x else L,U if y else L) for x,y in bits]
        if not any(rows[i][0]*rows[j][1]!=rows[i][1]*rows[j][0] for i in range(n) for j in range(i+1,n)):continue
        z=F(1)
        for (x,y),p,q in zip(bits,ps,qs):z*=(p if x else 1-p)*(q if y else 1-q)
        out+=z
    return out
heterochecks=0
for n in (2,3,4):
 for t in range(7):
  ps=[F(1+(t+2*i)%5,6) for i in range(n)]
  qs=[F(1+(3*t+i)%6,7) for i in range(n)]
  for L,U in ((F(0),F(1)),(F(-1),F(0)),(F(-1),F(1)),(F(1),F(2)),(F(-2),F(1))):
   assert heterogeometry(ps,qs,L,U)==brute_heterogeometry(ps,qs,L,U)
   heterochecks+=1
print('PASS',heterochecks,'inhomogeneous geometry checks; total',checks+extra+heterochecks)
