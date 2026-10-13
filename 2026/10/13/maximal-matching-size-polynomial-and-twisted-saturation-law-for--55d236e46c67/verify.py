#!/usr/bin/env python3
"""Exact symbolic and exhaustive checks of maximal matchings of Moebius ladders.
Requires Python 3 and SymPy. Run: python verify.py
"""
from collections import Counter
from itertools import product
import sympy as s

z,t,u,w=s.symbols('z t u w')
STATES=[('V','V')]+[p for p in product('ULR', repeat=2) if p != ('U','U')]
INDEX={a:i for i,a in enumerate(STATES)}

def admissible(a,b):
    return all((a[j]=='R')==(b[j]=='L') and not (a[j]=='U' and b[j]=='U') for j in (0,1))

def weight(a):
    return 1 if a==('V','V') else a.count('R')

N=len(STATES)
T=s.zeros(N)
S=s.zeros(N)
for i,a in enumerate(STATES):
    S[i,INDEX[a[::-1]]]=1
    for j,b in enumerate(STATES):
        if admissible(a,b):T[i,j]=z**weight(a)
assert T*S==S*T

fixed=[a for a in STATES if a==a[::-1]]
pairs=[]
used=set(fixed)
for a in STATES:
    if a not in used:
        b=a[::-1];pairs.append((a,b));used.add(a);used.add(b)
unit=s.eye(N)
cols=[unit[:,INDEX[a]] for a in fixed]
cols += [unit[:,INDEX[a]]+unit[:,INDEX[b]] for a,b in pairs]
cols += [unit[:,INDEX[a]]-unit[:,INDEX[b]] for a,b in pairs]
B=s.Matrix.hstack(*cols)
A=B.inv()*T*B
m=len(fixed)+len(pairs)
assert A[:m,m:]==s.zeros(m,N-m) and A[m:,:m]==s.zeros(N-m,m)
qplus=s.factor((s.eye(m)-t*A[:m,:m]).det())
qminus=s.factor((s.eye(N-m)-t*A[m:,m:]).det())
assert s.expand(qplus-(1-2*z*t-z**2*t**3+z**3*t**3-z**3*t**4-z**4*t**5))==0
assert s.expand(qminus-(1+z*t-z**2*t**3))==0

# Weighted series at the three smallest allowed excesses, 3k-2n=1,2,3.
F1=-u*s.diff((-3*u-u**4)/(1-u**3),u)
F2=-u*s.diff((-u**5)/(1-u**3)-((2*u+u**4)**2-u**2)/(2*(1-u**3)**2),u)
F3=-u*s.diff(u**3/(1-u**3)-(2*u**6+u**9)/(1-u**3)**2-(9*u**3+12*u**6+6*u**9+u**12)/(3*(1-u**3)**3),u)
coeff_series=[s.series(F,u,0,55).removeO().expand() for F in (F1,F2,F3)]
for n in range(1,55):
    a=coeff_series[{0:2,1:0,2:1}[n%3]].coeff(u,n)
    if n>=3:
        r=n//3
        expected=({0:(6 if n==3 else 2*r*(7*r*r-2*r-3)),1:4*n,2:n*(4*n-2)//3})[n%3]
        assert a==expected, (n,a,expected)

# Build the generating-function coefficients exactly by Newton's recurrence.
def log_derivative_coeffs(q, upto):
    coeff=[s.expand(q).coeff(t,i) for i in range(1,s.degree(q,t)+1)]
    k=len(coeff)
    val=[s.Integer(0)]*(upto+1)
    for n in range(1,upto+1):
        val[n]=s.expand(-n*(coeff[n-1] if n<=k else 0)-sum(coeff[j-1]*val[n-j] for j in range(1,min(n,k)+1)))
    return val
plus=log_derivative_coeffs(qplus,40)
minus=log_derivative_coeffs(qminus,40)
polys={n:s.Poly(s.expand(plus[n]-minus[n]),z) for n in range(3,41)}

def brute(n):
    edges=[]
    for i in range(n):
        edges.append((i,n+i))
        if i<n-1:
            edges.extend([(i,i+1),(n+i,n+i+1)])
    edges.extend([(n-1,n),(2*n-1,0)])
    adj=[0]*(2*n)
    for v,w in edges:
        adj[v] |=1<<w
        adj[w] |=1<<v
    ans=Counter()
    allbits=(1<<(2*n))-1
    def walk(seen,unmatched,k):
        if seen==allbits:
            ans[k]+=1
            return
        bit=(allbits^seen)&-(allbits^seen)
        v=bit.bit_length()-1
        if not (adj[v]&unmatched):
            walk(seen|bit,unmatched|bit,k)
        available=adj[v]&~seen
        while available:
            wbit=available&-available
            available^=wbit
            walk(seen|bit|wbit,unmatched,k+1)
    walk(0,0,0)
    return ans

for n in range(3,11):
    b=brute(n)
    a=dict(polys[n].terms())
    assert {k[0]:int(v) for k,v in a.items()}==dict(b),(n,a,b)
oeis=[6,23,43,102,213,447,978,2083,4491,9650,20699,44495,95536,205215,440813,946758,2033611,4367943,9381882,20151431,43283105,92967858,199685543,428904271,921243300,1978737343]
for n, total in enumerate(oeis,3):
    assert polys[n].eval(1)==total, (n,total,polys[n].eval(1))
for n in range(3,41):
    poly=polys[n]
    lo=n//3*2+1 if n%3==0 else (2*n)//3+1
    assert poly.monoms() and min(a[0] for a in poly.monoms())==lo,(n,poly)
    assert poly.eval(1)>0
print('VERIFY_OK states=9 symmetry_blocks=6+3 exact_determinants=2 brute_ladders=3..10 cardinality_coefficients=all extrema=3..40 excess_series=1..54 OEIS_totals=3..28')
