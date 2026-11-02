#!/usr/bin/env python3
"""Reproducible finite checks for two independent pair-averaging rounds.

Uses exhaustive matching enumeration, exact polynomial recurrences, and
independently computed singular values. Finite checks do not prove limits.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import math
import numpy as np

checks = 0

def verify(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)

def matchings(xs):
    xs = tuple(xs)
    if not xs:
        yield ()
        return
    first = xs[0]
    for j in range(1, len(xs)):
        second = xs[j]
        rest = xs[1:j] + xs[j+1:]
        for other in matchings(rest):
            yield ((first,second),) + other

def components(m, B):
    adj = [[] for _ in range(m)]
    for u,v in B:
        a,b = u//2,v//2
        adj[a].append(b)
        adj[b].append(a)
    for a in range(m):
        verify(len(adj[a]) == 2, f'degree for m={m} at {a}')
    seen=set(); sizes=[]
    for v in range(m):
        if v in seen: continue
        todo=[v]; seen.add(v); count=0
        while todo:
            u=todo.pop(); count += 1
            for w in adj[u]:
                if w not in seen:
                    seen.add(w);todo.append(w)
        sizes.append(count)
    verify(sum(sizes)==m, 'components partition')
    return sizes

def averaging(d, pairs):
    p=np.zeros((d,d),dtype=float)
    for u,v in pairs:
        p[u,u]=p[u,v]=p[v,u]=p[v,v]=0.5
    return p

def exact_pgf_polys(m):
    # F_m(s)=[x^m] exp(sum_{l>=1} t_l x^l/l),
    # where t_l=1/2 for odd l and s/2 for even l.
    f=[[Fraction(1)]]
    for n in range(1,m+1):
        a=[Fraction(0)]*(n//2+1)
        for l in range(1,n+1):
            old=f[n-l]
            for j,c in enumerate(old):
                k=j+(l%2==0)
                a[k]+=c/Fraction(2*n)
        f.append(a)
    return f[m]

def verify_exhaustive(max_m=6):
    A_cache={}; total=0
    for m in range(1,max_m+1):
        d=2*m
        A=tuple((2*j,2*j+1) for j in range(m))
        PA=averaging(d,A)
        count=Counter()
        for B in matchings(range(d)):
            sizes=components(m,B)
            z=sum((l%2)==0 for l in sizes)
            count[z]+=1
            PB=averaging(d,B)
            C=PA@PB
            expected=[0.0]*m
            for l in sizes:
                expected.extend(abs(math.cos(math.pi*j/l)) for j in range(l))
            exact=sorted(expected)
            numeric=sorted(np.linalg.svd(C,compute_uv=False))
            verify(len(exact)==d, f'spectrum size m={m}')
            verify(max(abs(a-b) for a,b in zip(exact,numeric))<5e-12,
                   f'singular spectrum m={m}, B={B}')
            verify(sum(s>1e-8 for s in numeric)==m-z,
                   f'rank m={m}, B={B}')
            verify(len(B)==m, 'matching size')
            total+=1
        pred=exact_pgf_polys(m)
        normalize=sum(pred)
        observed_total=sum(count.values())
        verify(observed_total==math.prod(range(1,d,2)),f'matching count m={m}')
        for z in range(len(pred)):
            verify(Fraction(count[z],observed_total)==pred[z]/normalize,
                   f'PGF coefficient m={m}, z={z}')
        for z in count:
            verify(z<len(pred), f'PGF support m={m}, z={z}')
        print(f'm={m}: {observed_total} matchings; rank defect distribution '+
              ', '.join(f'{z}:{count[z]}' for z in sorted(count)))
    return total

def verify_recursion():
    # Independent enumeration of coefficient generating functions from finite
    # Ewens cycle-count formula; compares with the derivative recurrence.
    for m in range(1,12):
        poly=exact_pgf_polys(m)
        denominator=sum(poly)
        verify(denominator==Fraction(math.comb(2*m,m),4**m),f'den m={m}')
        coeff=Counter()
        def rec(left,minimum,mult,z):
            if left==0:
                coeff[z]+=mult
                return
            for l in range(minimum,left+1):
                # Build a composition of the partition with factors 1/(2*l)^c/c!.
                for copies in range(1,left//l+1):
                    weight=Fraction(1,(2*l)**copies*math.factorial(copies))
                    rec(left-l*copies,l+1,mult*weight,z+(l%2==0)*copies)
        rec(m,1,Fraction(1),0)
        for z in range(len(poly)):
            verify(poly[z]==coeff[z],f'cycle index m={m}, z={z}')

if __name__=='__main__':
    total=verify_exhaustive()
    verify_recursion()
    print(f'PASS: {checks:,} assertions; {total:,} exhaustive matchings. '
          'The finite checks do not establish the asymptotic statements.')
