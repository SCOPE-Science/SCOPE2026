#!/usr/bin/env python3
"""Exact finite checks for leaf-conditioned crossing counts of uniform Cayley trees.

Standard-library only. Exhausts labelled Prüfer words for n=4,...,8;
for larger n checks independent finite rational formulas, not the theorem.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb

CHECKS = 0

def check(got, expected, msg):
    global CHECKS
    CHECKS += 1
    if got != expected:
        raise AssertionError(f"{msg}: {got!r} != {expected!r}")

def stirling_row(m):
    a = [0] * (m + 1)
    a[0] = 1
    for t in range(1, m + 1):
        b = [0] * (m + 1)
        for j in range(1, t + 1):
            b[j] = j*a[j] + a[j-1]
        a = b
    return a

def edges_from_prufer(code, n):
    d = [1]*n
    for i in code:
        d[i] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if d[i] == 1)
        edges.append(tuple(sorted((leaf,v))))
        d[leaf] -= 1
        d[v] -= 1
    a,b = (i for i in range(n) if d[i] == 1)
    edges.append((a,b))
    return edges

def crossings(edges):
    return sum((a<c<b<d) or (c<a<d<b)
               for i,(a,b) in enumerate(edges)
               for (c,d) in edges[i+1:])

def run():
    for n in range(4,9):
        m=n-2; q=Fraction(n-1,n); B=comb(m,2)
        sm=stirling_row(m); sm1=stirling_row(m-1)
        by=defaultdict(lambda:[0,0])
        SX=SL=SXL=SL2=SW=SW2=0
        for code in product(range(n), repeat=m):
            x=crossings(edges_from_prufer(code,n))
            l=n-len(set(code))
            w=m+sum(code[i]==code[j] for i in range(m) for j in range(i+1,m))
            by[l][0]+=1; by[l][1]+=x
            SX+=x;SL+=l;SXL+=x*l;SL2+=l*l;SW+=w;SW2+=w*w
            check(w, sum(comb(d,2) for d in _degree_list(code,n)), f'wedge Prüfer n={n}')
        N=n**m
        EX=Fraction(SX,N);EL=Fraction(SL,N)
        check(EX, Fraction((n-1)*(n-2)*(n-3),6*n),f'mean crossing n={n}')
        check(EL, n*q**m,f'mean leaves n={n}')
        check(Fraction(SW,N), Fraction(m)+Fraction(B,n),f'mean wedges n={n}')
        check(Fraction(SW2,N)-Fraction(SW,N)**2, Fraction(B*(n-1),n*n),f'wedge variance n={n}')
        check(Fraction(SXL,N)-EX*EL, -Fraction(B,3*n)*q**(m-1), f'cross leaf covariance n={n}')
        check(Fraction(SL2,N)-EL*EL,
              n*q**m*(1-q**m)+n*(n-1)*(Fraction(n-2,n)**m-q**(2*m)),
              f'leaf variance n={n}')
        means=[]
        for leaves in range(2,n):
            occ=n-leaves
            ratio=Fraction(sm1[occ],sm[occ]) if occ<m else Fraction(0)
            expected=Fraction(B,3)*(1-ratio)
            observed=Fraction(by[leaves][1],by[leaves][0])
            check(observed,expected,f'conditional mean n={n}, leaves={leaves}')
            check(by[leaves][0], comb(n,occ)*__factorial(occ)*sm[occ], f'Prüfer count n={n}, leaves={leaves}')
            means.append(observed)
        check(all(a>b for a,b in zip(means,means[1:])),True, f'strict regression n={n}')
    # Independent exact Stirling-ratio comparison on dimensions not enumerated.
    for m in range(2,101):
        row=stirling_row(m);previous=stirling_row(m-1)
        ratios=[Fraction(previous[k],row[k]) if k<m else Fraction(0) for k in range(1,m+1)]
        check(all(a>b for a,b in zip(ratios,ratios[1:])),True,f'ratio order m={m}')
    print(f"VERIFY_OK {CHECKS} exact assertions; Prüfer enumeration through 8 vertices")

def __factorial(n):
    z=1
    for i in range(2,n+1):z*=i
    return z

def _degree_list(code,n):
    d=[1]*n
    for v in code:d[v]+=1
    return d

if __name__=='__main__':
    run()
