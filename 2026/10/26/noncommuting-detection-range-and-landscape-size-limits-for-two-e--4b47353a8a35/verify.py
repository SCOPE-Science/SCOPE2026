#!/usr/bin/env python3
"""Exact checks for two distance-decaying ecological detection traps.
Run: python verify.py > verification_certificate.json
Uses only the Python standard library. This finite checker does not prove the asymptotic theorem.
"""
import json
from fractions import Fraction
from hashlib import sha256

def score(n,a,b,q):
    return sum((q**abs(i-a)+q**abs(i-b)-q**(abs(i-a)+abs(i-b)) for i in range(n)), Fraction())

def closed(n,a,b,q):
    s=b-a; r=n-1-b
    return 2*(1+q)/(1-q)-((1+q**s)*q/(1-q))*(q**a+q**r)-q**s*(s+1+q*q*(2-q**(2*a)-q**(2*r))/(1-q*q))

def poly(n,a,b):
    c=[0]*(2*n+1)
    for i in range(n):
        da=abs(i-a); db=abs(i-b)
        c[da]+=1; c[db]+=1; c[da+db]-=1
    while c and c[-1]==0:c.pop()
    return c

def sub(a,b):
    return [ (a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]

def mul(*args):
    z=[1]
    for a in args:
        v=[0]*(len(z)+len(a)-1)
        for i,x in enumerate(z):
            for j,y in enumerate(a):v[i+j]+=x*y
        z=v
    return z

# Symbolic factorizations of central-pair comparisons, for all n<=7.
Q=[0,1]; QM1=[-1,1]; P=mul(Q,QM1,QM1)
FACTORS={
  (3,2,1):mul(P),
  (4,2,1):mul(P,[1,-1]),(4,2,3):mul(P,[1,-1]),
  (5,2,1):mul(P,[2,0,1]),(5,2,3):mul(P,[1,-1,1]),(5,2,4):mul(P,[2,1]),
  (6,3,1):mul(P,[2,2]),(6,3,2):mul(P,Q,[2,0,1]),
  (6,3,4):mul(P,[1,2,-1,1]),(6,3,5):mul(P,[2,4,2]),
  (7,3,1):mul(P,[2,3,1]),(7,3,2):mul(P,Q,[2,0,0,-1]),
  (7,3,5):mul(P,[1,1], [1,2,-1]),
  (7,3,6):mul(P,[2,5,4,3,-1]),
  (7,4,3):mul(P,Q,[-1,2,0,1]),
}
# For n7 s3-vs-s5 and s3-vs-s6 polynomials have manifest positive factors above.
# For n7 s4 beats s3 exactly when q^3+2q-1>0.
counts={'score_closed_checks':0,'centrality_checks':0,'global_optimizer_checks':0,'factor_identity_checks':0,'n7_phase_checks':0}
qvals=[Fraction(i,19) for i in range(1,19)]+[Fraction(1,101),Fraction(100,101)]
for n in range(3,26):
    for q in qvals:
        vals={}
        for a in range(n):
            for b in range(a+1,n):
                v=score(n,a,b,q)
                assert v==closed(n,a,b,q), ('closed',n,a,b,q)
                counts['score_closed_checks']+=1
                vals[a,b]=v
        for s in range(1,n):
            best=max(vals[a,a+s] for a in range(n-s))
            centera=(n-1-s)//2
            assert vals[centera,centera+s]==best,('center',n,s,q)
            counts['centrality_checks']+=1
        globalbest=max(vals.values())
        assert globalbest==max(vals[(n-1-s)//2,(n-1-s)//2+s] for s in range(1,n))
        counts['global_optimizer_checks']+=1
for (n,win,s),expected in FACTORS.items():
    aa=(n-1-win)//2;ab=aa+win; ba=(n-1-s)//2;bb=ba+s
    got=sub(poly(n,aa,ab),poly(n,ba,bb))
    while got and got[-1]==0:got.pop()
    while expected and expected[-1]==0:expected.pop()
    assert got==expected,(n,win,s,got,expected)
    counts['factor_identity_checks']+=1
for q in qvals:
    vals={(a,b):score(7,a,b,q) for a in range(7) for b in range(a+1,7)}
    mx=max(vals.values()); opt={pair for pair,v in vals.items() if v==mx}
    c=q**3+2*q-1
    expected={(1,4),(2,5)} if c<0 else {(1,5)} if c>0 else {(1,4),(2,5),(1,5)}
    assert opt==expected,(q,opt,expected)
    counts['n7_phase_checks']+=1
# Check examples in two distinct detection-length regimes.
examples={}
for q in (Fraction(1,10),Fraction(9,10)):
    vals={(a,b):score(7,a,b,q) for a in range(7) for b in range(a+1,7)}
    mx=max(vals.values());best=sorted(pair for pair,v in vals.items() if v==mx)
    examples[str(q)]={'optimizers':best,'score':[mx.numerator,mx.denominator]}
cert={'schema_version':1,'model':'two-independent-geometric-detection-traps-on-path','exact_checks':counts,'seven_site_examples':examples,'limits':'Exact finite checks support but do not replace the general analytic proof.'}
print(json.dumps(cert,sort_keys=True,separators=(',',':')))
