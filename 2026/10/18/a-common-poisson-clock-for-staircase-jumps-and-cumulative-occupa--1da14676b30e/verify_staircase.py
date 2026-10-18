#!/usr/bin/env python3
"""Standalone finite arithmetic and stochastic sanity checks for a staircase chain.

Finite checks do not establish the asymptotic coupling theorem; see the proof.
"""
from fractions import Fraction as F
from math import comb, ceil, log
import random

checks=0

def ok(condition):
    global checks
    assert condition
    checks += 1

# Exact recurrence of the Markov jump-count PGF as a polynomial in the height.
for p in (F(1, 4), F(1, 2), F(1, 1)):
    for z in (F(0), F(1), F(2), F(3)):
        poly=[F(1)]
        for n in range(1, 15):
            tmp=[F(0)]*(len(poly)+1)
            for k,v in enumerate(poly):
                tmp[k]+=v
                tmp[k+1]+=p*v*(z/F(k+1)-1)
            poly=tmp
            rhs=F(0)
            ff=F(1)
            for j in range(n+1):
                if j:
                    ff*=F(z-j,j)
                rhs+=comb(n,j)*ff*p**j
            ok(sum(poly)==rhs)
            ok(poly[0]==1)

# Exact moment integration identities for running minima M_i from iid U(0,1).
for i in range(1,65):
    ex=F(1,i+1)
    ex2=F(2,(i+1)*(i+2))
    var=ex2-ex**2
    ok(var==F(i,(i+1)**2*(i+2)))
    for j in range(i,65):
        # E[M_i*M_j] = integral of two joint-survival regions.
        mixed=F(1,(j+1)*(j+2))+F(1,(i+1)*(j+2))
        cov=mixed-ex*F(1,j+1)
        ok(cov==F(i,(i+1)*(j+1)*(j+2)))
        if j>i:
            # E[I_j M_i], with I_j the new lower-record indicator.
            mixed2=F(1,j*(j+1))+F(1,(i+1)*(j+1))
            cov2=mixed2-F(1,j)*ex
            ok(cov2==F(i,(i+1)*j*(j+1)))

# One law of large numbers level calculation for exact second moments.
prefix=F(0); v=F(0); c=F(0)
for j in range(1,500):
    if j>1:
        v += 2*prefix/F((j+1)*(j+2))
        c += prefix/F(j*(j+1))
    v += F(j,(j+1)**2*(j+2))
    prefix += F(j,j+1)
    if j>=2: ok(v>0 and c>0)

# A finite simulation of the exact renewal representation and its Poisson marks.
# Use rejection-free geometric waits generated from exponentials.
rng=random.Random(20261011)
for p,n in ((0.15,50000),(0.008,3000000)):
    errors=[]
    for replicate in range(200):
        level=1.0; t=0; count=0; area=0.0
        depths=[]; marks=[]; depth=0.0
        unfinished_e=None
        while t<n:
            e=rng.expovariate(1.0)
            x=p*level
            h=-__import__('math').log1p(-x)
            wait=max(1,ceil(e/h))
            taken=min(wait,n-t)
            area += x*taken
            t+=taken
            if taken<wait:
                unfinished_e=e
                break
            # The jump factor is independent of its preceding waiting time.
            u=rng.random()
            depth-=log(u)
            depths.append(depth)
            marks.append(e)
            level*=u
            count+=1
        tau=log(n*p)
        reference=sum(1 for d in depths if d<=tau)
        # The whole Poisson path may continue past the observed terminal jump.
        while depth<=tau:
            if unfinished_e is not None:
                e=unfinished_e
                unfinished_e=None
            else:
                e=rng.expovariate(1.0)
            u=rng.random()
            depth-=log(u)
            depths.append(depth)
            marks.append(e)
            if depth>tau: break
        reference=sum(d<=tau for d in depths)
        reference_area=sum(marks[j] for j,d in enumerate(depths) if d<=tau)
        errors.append(abs(count-reference)+abs(area-reference_area))
    ok(sum(errors)/len(errors)<40)
print('PASS:',checks,'exact finite identities and seeded stochastic sanity checks')
