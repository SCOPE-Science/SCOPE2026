"""Exact algebra and finite diagnostics for a punctured bilinear Walsh fourth-moment inequality.

The all-dimensional proof is in RESULT.md; finite tests here do not replace it.
Run: python3 verify.py
Requires Python 3 and sympy.
"""
from fractions import Fraction
from itertools import combinations, product
import random
import sympy as sp

k,p,q,r=sp.symbols('k p q r', real=True)
D=6*k*k+k-4
pstar=k*(6*k-5)/D
C=3-1/k+(6*k-5)**2/D
A=(6*(k-1)**2-2)/k**2
F=3+A*p*p-sp.Rational(2)/k*(q*q+r*r)+12*(k-1)/k*p*(q+r)
F_reduced=sp.expand(F.subs({q:(1-p)/2,r:(1-p)/2}))
assert sp.simplify(F_reduced-(3-1/k+(12*k-10)*p/k-D*p*p/k**2))==0
assert sp.simplify(F_reduced.subs(p,pstar)-C)==0
assert sp.simplify((F-(C-D*(p-pstar)**2/k**2-(q-r)**2/k)).subs(r,1-p-q))==0
assert sp.simplify((pstar/(k*((1-pstar)/2)))-(6*k-5)/(3*k-2))==0

for kval in range(1,15):
    c=sp.factor(C.subs(k,kval))
    full=(3-sp.Rational(2,kval+1))**2
    assert 0 < pstar.subs(k,kval) < 1
    assert 0 < c < full
assert sp.simplify(C.subs(k,1)-sp.Rational(7,3))==0
assert sp.simplify(C.subs(k,2)-sp.Rational(52,11))==0

def moment_via_rectangles(aa,n):
    aa={key:sp.sympify(v) for key,v in aa.items()}
    B=sum((v*v for v in aa.values()),sp.Integer(0))
    fourth=3*B**2-2*sum((v**4 for v in aa.values()),sp.Integer(0))
    for i,ip in combinations(range(n),2):
        for j,jp in combinations(range(n),2):
            if all(e in aa for e in [(i,j),(i,jp),(ip,j),(ip,jp)]):
                fourth+=24*aa[i,j]*aa[i,jp]*aa[ip,j]*aa[ip,jp]
    return sp.expand(fourth),sp.expand(B)

def exact_enum(aa,n):
    z=sp.Integer(0)
    for bits in product((-1,1),repeat=2*n):
        v=sum((a*bits[i]*bits[n+j] for (i,j),a in aa.items()),sp.Integer(0))
        z+=v**4
    return sp.expand(z/4**n)

for n in (2,3,4):
    kval=n-1
    T=(6*kval-5)
    S=(3*kval-2)
    t=sp.sqrt(sp.Rational(T,S))
    aa={(i,j):(t if i<kval and j<kval else sp.Integer(1))
        for i in range(n) for j in range(n) if (i,j)!=(kval,kval)}
    moment,B=moment_via_rectangles(aa,n)
    assert sp.simplify(moment/B**2-C.subs(k,kval))==0
    if n<=3:
        assert sp.simplify(exact_enum(aa,n)-moment)==0
    print('exact_sharp',n,'constant',sp.factor(C.subs(k,kval)),'moment_ratio_verified')

random.seed(1742)
for n in (2,3,4):
    cn=float(C.subs(k,n-1))
    for trial in range(30):
        aa={(i,j):random.randint(-5,5) for i in range(n)
            for j in range(n) if (i,j)!=(n-1,n-1)}
        moment,B=moment_via_rectangles(aa,n)
        if B:
            assert float(moment/B**2)<=cn+1e-10
    print('random_cases',n,30,'passed')

# Rank over GF(2) of rectangle boundaries: sufficient for sign switching.
def rank_mod2(rows):
    pivots={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in pivots:
                x^=pivots[i]
            else:
                pivots[i]=x
                break
    return len(pivots)
for n in range(2,7):
    edges=[(i,j) for i in range(n) for j in range(n) if (i,j)!=(n-1,n-1)]
    idx={e:t for t,e in enumerate(edges)}
    cycles=[]
    for i,ip in combinations(range(n),2):
        for j,jp in combinations(range(n),2):
            vertices=[(i,j),(i,jp),(ip,j),(ip,jp)]
            if all(e in idx for e in vertices):
                cycles.append(sum(1<<idx[e] for e in vertices))
    assert rank_mod2(cycles)==len(edges)-(2*n)+1
    print('cycle_span',n,'verified')
print('VERIFY_OK')
