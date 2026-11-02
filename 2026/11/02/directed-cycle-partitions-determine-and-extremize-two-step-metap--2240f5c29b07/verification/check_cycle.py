#!/usr/bin/env python3
"""Exact arithmetic checks for the two-census directed-cycle extinction law.

Python 3 standard library only. All enumerations have explicit finite ranges;
no numerical test is used as a proof for arbitrary population size.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter

assertions = 0

def verify(statement):
    global assertions
    assert statement
    assertions += 1

def part(n, low=2):
    """All nondecreasing partitions of n into lengths at least 2."""
    if n == 0:
        yield ()
    for k in range(low, n + 1):
        for z in part(n-k, k):
            yield (k,) + z

def sigma_from_lengths(parts):
    sigma = []
    start = 0
    for l in parts:
        sigma.extend(start+(j-1)%l for j in range(l))
        start += l
    return tuple(sigma)

def direct(sigma, e, c):
    """Full exact sum over stage-one survival and colonization coins."""
    n=len(sigma)
    val=F(0)
    for survived in product((0,1), repeat=n):
        surv_count=sum(survived)
        ps=(1-e)**surv_count * e**(n-surv_count)
        allowed=tuple(i for i in range(n) if not survived[i] and survived[sigma[i]])
        for coins in product((0,1), repeat=len(allowed)):
            count=sum(coins)
            pb=c**count * (1-c)**(len(allowed)-count)
            occupied=surv_count+count
            val+=ps*pb*e**occupied
    return val

def cycle_traces(n,e,c):
    s=e*(2-e); d=c*e*e*(1-e)**2
    u=[F(2),s]
    for l in range(2,n+1):
        u.append(s*u[-1]-d*u[-2])
    return u

def formula(parts,e,c):
    u=cycle_traces(sum(parts),e,c)
    v=F(1)
    for l in parts: v*=u[l]
    return v

def poly_product(parts):
    a=[1]
    for l in parts:
        b=[0]*(len(a)+l)
        for j,x in enumerate(a):
            b[j]+=x; b[j+l]+=x
        a=b
    return tuple(a)

# Independent probability enumeration, including a fully reciprocal two-cycle.
for e,c in ((F(1,2),F(1)),(F(1,3),F(2,5)),(F(3,5),F(4,7))):
    for n in range(2,8):
        for lengths in part(n):
            verify(direct(sigma_from_lengths(lengths),e,c)==formula(lengths,e,c))

# Strict optimal cycle partitions, and sharp extrema at fixed reciprocal-pair count.
for e,c in ((F(1,2),F(1)),(F(1,3),F(2,5)),(F(3,5),F(4,7))):
    for n in range(2,19):
        choices=list(part(n)); values={x:formula(x,e,c) for x in choices}
        verify(values[(n,)]==min(values.values()))
        maxparts=(2,)*(n//2) + ((3,) if n%2 else ())
        if n%2: maxparts=(2,)*((n-3)//2)+(3,)
        verify(values[maxparts]==max(values.values()))
        for m in sorted({x.count(2) for x in choices}):
            subset={x:v for x,v in values.items() if x.count(2)==m}
            rem=n-2*m
            lower=(2,)*m+((rem,) if rem else ())
            if rem==0: upper=(2,)*m
            else:
                q,r=divmod(rem,3)
                upper=(2,)*m+(3,)*q if r==0 else (2,)*m+(3,)*(q-1)+(3+r,)
            verify(subset[lower]==min(subset.values()))
            verify(subset[upper]==max(subset.values()))

def recover(poly):
    """Recover multiset of cycle lengths from product of (1+z^length)."""
    result=[]
    p=list(poly)
    while any(p[k] for k in range(1,len(p))):
        g=next(k for k in range(1,len(p)) if p[k])
        multiplicity=p[g]
        verify(g>=2 and multiplicity>0)
        for _ in range(multiplicity):
            q=[]
            for k in range(len(p)):
                q.append(p[k]-(q[k-g] if k>=g else 0))
            verify(all(t==0 for t in q[-g:]))
            p=q[:-g]
        result.extend([g]*multiplicity)
    verify(p==[1])
    return tuple(result)

# Recoverability of cycle lengths from the exact response polynomial.
for n in range(2,23):
    polys={poly_product(lengths):lengths for lengths in part(n)}
    verify(len(polys)==len(list(part(n))))
    for lengths in part(n):
        p=poly_product(lengths)
        verify(recover(p)==lengths)
        verify(p[0]==1)
        first=min(lengths)
        verify(all(p[k]==0 for k in range(1,first)))
        verify(p[first]==lengths.count(first))

# Example with identical n, indegree, outdegree, reciprocal-link count and spectrum.
e=F(1,2); c=F(1)
verify(formula((8,),e,c)==F(2207,65536))
verify(formula((4,4),e,c)==F(2209,65536))
verify(formula((3,5),e,c)==F(2214,65536))
verify(formula((8,),e,c)<formula((4,4),e,c)<formula((3,5),e,c))
print(f"PASS: {assertions} exact-rational assertions")
