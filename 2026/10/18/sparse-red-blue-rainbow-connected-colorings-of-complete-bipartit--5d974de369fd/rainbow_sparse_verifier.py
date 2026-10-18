#!/usr/bin/env python3
"""Independent finite verification of sparse rainbow two-edge colorings.

Exhausts labelled red/blue edge patterns for small complete bipartite graphs,
checks the graph-theoretic rainbow condition via two-edge paths, and compares
minimum red-edge counts and optimizer multiplicities with the closed formulas.
"""
from itertools import combinations
from math import comb, factorial

def formula(a,b):
    u,v=sorted((a,b),reverse=True)
    if u>2**v:
        return None,0
    remaining=u; weight=0; ways=1
    for r in range(v+1):
        cap=comb(v,r)
        selected=min(remaining,cap)
        weight+=r*selected
        remaining-=selected
        if remaining==0:
            ways=comb(cap,selected)*factorial(u)
            break
    return weight,ways

def direct_ok(mask,a,b):
    # For same-side vertices, independently find a 2-edge path with opposite colors.
    for i in range(a):
        for j in range(i+1,a):
            if not any(((mask>>(i*b+k))&1)!=((mask>>(j*b+k))&1) for k in range(b)):
                return False
    for i in range(b):
        for j in range(i+1,b):
            if not any(((mask>>(k*b+i))&1)!=((mask>>(k*b+j))&1) for k in range(a)):
                return False
    return True

def exhaustive(a,b):
    minimum=a*b+1; count=0
    for mask in range(1<<(a*b)):
        # Skip candidates with more red edges than present best.
        pop=mask.bit_count()
        if pop>minimum: continue
        if direct_ok(mask,a,b):
            if pop<minimum:
                minimum=pop; count=1
            else: count+=1
    got=(minimum,count) if count else (None,0)
    predicted=formula(a,b)
    assert got==predicted,(a,b,got,predicted)
    print(f'K_{{{a},{b}}}: {1<<(a*b)} colorings; minimum,count={got}')

if __name__=='__main__':
    for a,b in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4)]:
        exhaustive(a,b)
    print('PASS')

# Also independently verify the full red-edge polynomial via partition-lattice
# inclusion-exclusion against direct enumeration of colored paths.
def partitions(xs):
    if not xs:
        yield ()
        return
    first,*rest=xs
    for pi in partitions(rest):
        yield ((first,),)+pi
        for i in range(len(pi)):
            expanded=list(pi)
            expanded[i]=(first,)+expanded[i]
            yield tuple(expanded)

def mobius(pi):
    sign=1
    for block in pi:
        sign*=(-1)**(len(block)-1)*factorial(len(block)-1)
    return sign

def mobius_distribution(a,b):
    from collections import defaultdict
    coeffs=defaultdict(int)
    for pi in partitions(tuple(range(a))):
        for sigma in partitions(tuple(range(b))):
            term={0:mobius(pi)*mobius(sigma)}
            for block in pi:
                for other in sigma:
                    degree=len(block)*len(other)
                    new={}
                    for exponent,coef in term.items():
                        new[exponent]=new.get(exponent,0)+coef
                        new[exponent+degree]=new.get(exponent+degree,0)+coef
                    term=new
            for degree,coef in term.items():
                coeffs[degree]+=coef
    return {d:v for d,v in coeffs.items() if v}

def check_weight_distribution(a,b):
    from collections import Counter
    direct=Counter()
    for mask in range(1<<(a*b)):
        if direct_ok(mask,a,b):direct[mask.bit_count()]+=1
    via_mobius=mobius_distribution(a,b)
    assert direct==via_mobius,(a,b,direct,via_mobius)
    print(f'K_{{{a},{b}}}: all {sum(direct.values())} rainbow colorings agree with Möbius polynomial')

if __name__=='__main__':
    for a,b in [(2,2),(2,3),(2,5),(3,3),(3,4),(4,4)]:
        check_weight_distribution(a,b)
    print('FULL WEIGHT ENUMERATOR PASS')
