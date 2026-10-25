"""Reproducible exact checks of exchangeable rank-one spectral sketch formulas.

This code verifies finite rational identities and examples. The universal theorem
is established by the accompanying analytic argument, not by enumeration.
"""
from fractions import Fraction as F
from itertools import permutations, product
import math

checks=0

def assert_exact(a,b):
    global checks
    assert a==b, (a,b)
    checks+=1

def mean(items):
    items=list(items)
    return sum(items,F(0))/len(items)

def gap(s,c,t):
    n=len(s)
    C=sum(c)
    D=sum(c[i]*t[i] for i in range(n))
    assert D>0
    G=sum(c[i]*s[i]*t[i] for i in range(n))/D
    flat=sum(c[i]*s[i] for i in range(n))/C
    E=F(0)
    for i in range(n):
        for j in range(i+1,n):
            v=list(t)
            v[i],v[j]=v[j],v[i]
            Ds=sum(c[k]*v[k] for k in range(n))
            E+=(c[i]*c[j]*(s[i]-s[j])*(c[i]-c[j])
                *(t[i]-t[j])**2/(D*Ds))/(2*C)
    return G,flat,E

for n in (2,3,4):
    for sraw in product((1,2,4),repeat=n):
        s=tuple(F(v) for v in sraw)
        for t0 in (tuple(F(i+1) for i in range(n)),
                   tuple(F(1) for _ in range(n)),
                   tuple(F(i%2+1) for i in range(n))):
            ts=sorted(set(permutations(t0)))
            for c in (s, tuple(v**3 for v in s), tuple(1/v for v in s),
                      tuple(F(i+1) for i in range(n))):
                trials=[gap(s,c,t) for t in ts]
                avg=mean(v[0] for v in trials)
                flat=trials[0][1]
                gapp=mean(v[2] for v in trials)
                assert_exact(flat-avg,gapp)
                if c==s or c==tuple(v**3 for v in s):
                    assert_exact(avg<=flat,True)
                if c==tuple(1/v for v in s):
                    assert_exact(avg>=flat,True)

# Every signed probe gives exactly the same rank-one Frobenius error on
# an orthogonal-column matrix. The factor-two inequality is also exact.
for n in range(2,9):
    for r in range(1,100):
        s=tuple(F(r if i==0 else i+1) for i in range(n))
        for q in (0,1,2,3):
            a=tuple(v**(2*q+1) for v in s)
            e=sum(s)-sum(a[i]*s[i] for i in range(n))/sum(a)
            optimum=sum(s)-max(s)
            assert_exact(0<=e<=2*optimum,True)

# Explicit planar Gaussian vs flat-sign formulas.
for a in range(1,30):
    for b in range(1,30):
        s,t=F(a*a),F(b*b)
        er=2*s*t/(s+t)
        assert_exact(er<=F(a*b),True)
        assert_exact(er <= 2*min(s,t),True)

# At an isotropic spectrum no square-magnitude distribution matters.
for n in range(2,9):
    s=[F(3)]*n
    for c in ([F(3)]*n,[F(i+1) for i in range(n)]):
        for t in ([F(i+1) for i in range(n)],[F(1)]*n):
            g,f,_=gap(s,c,t)
            assert_exact(g,f)

print(f"PASS: {checks} deterministic exact-rational assertions")
