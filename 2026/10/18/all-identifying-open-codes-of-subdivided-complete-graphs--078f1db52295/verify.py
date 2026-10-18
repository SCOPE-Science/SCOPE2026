#!/usr/bin/env python3
"""Independent finite verification of the identifying open code formulas."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
from math import factorial, comb, ceil


def auxiliary_graph_valid(n, fmask, pairs):
    neighborhoods=[0]*n
    for e,(a,b) in enumerate(pairs):
        if fmask>>e &1:
            neighborhoods[a]|=1<<e
            neighborhoods[b]|=1<<e
    return all(neighborhoods) and len(set(neighborhoods)) == n


def brute_graph_code(n, xmask, fmask, pairs):
    nverts=n+len(pairs)
    signatures=[]
    for i in range(n):
        signature=0
        for e,(a,b) in enumerate(pairs):
            if fmask>>e&1 and i in (a,b):
                signature |= 1<<(n+e)
        signatures.append(signature)
    for a,b in pairs:
        signatures.append(xmask & ((1<<a)|(1<<b)))
    return all(signatures) and len(set(signatures)) == nverts


def count_min_forests(n):
    q,r=divmod(n,3)
    def term(size_counts):
        d=factorial(n)
        for k,multiplicity in size_counts.items():
            d*= (k**(k-2))**multiplicity
            d//=factorial(k)**multiplicity * factorial(multiplicity)
        # Above repeated divisions might prematurely truncate; use rational instead.
    def rational(counts):
        numer=factorial(n)
        denom=1
        for s,c in counts.items():
            numer*=pow(s,s-2)**c
            denom*=pow(factorial(s),c)*factorial(c)
        assert numer%denom==0
        return numer//denom
    if r==0:
        return rational({3:q})
    if r==1:
        return rational({3:q-1,4:1})
    v=rational({3:q-1,5:1})
    if q>=2:
        v+=rational({3:q-2,4:2})
    return v


def egf_edge_counts(n):
    """Coefficient extraction from exp(-x-z*x*x/2) sum (1+z)^C(j,2)x^j/j!."""
    answer=Counter()
    for a in range(n+1):
        for b in range((n-a)//2+1):
            j=n-a-2*b
            coeff=Fraction((-1)**(a+b)*factorial(n),
                           factorial(a)*factorial(b)*2**b*factorial(j))
            for t in range(comb(j,2)+1):
                answer[b+t]+=coeff*comb(comb(j,2),t)
    assert all(v.denominator==1 for v in answer.values())
    return Counter({k:int(v) for k,v in answer.items() if v})


def main():
    counts={}
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        m=len(pairs)
        hist=Counter()
        count_valid=0
        for fmask in range(1<<m):
            if auxiliary_graph_valid(n,fmask,pairs):
                hist[fmask.bit_count()]+=1
                count_valid+=1
        assert hist == egf_edge_counts(n), (n,hist,egf_edge_counts(n))
        minf=min(hist)
        assert minf==ceil(2*n/3),(n,minf)
        predicted=count_min_forests(n)
        assert hist[minf]==predicted, (n,hist[minf],predicted)
        predicted_min=n-1+ceil(2*n/3)
        predicted_min_count=n*predicted
        if n<=5:
            direct_poly=Counter()
            for xmask in range(1<<n):
                for fmask in range(1<<m):
                    actual=brute_graph_code(n,xmask,fmask,pairs)
                    from_separation=(xmask.bit_count()>=n-1 and auxiliary_graph_valid(n,fmask,pairs))
                    assert actual==from_separation,(n,xmask,fmask)
                    if actual:
                        direct_poly[xmask.bit_count()+fmask.bit_count()]+=1
            expected_poly=Counter()
            for size,fcount in hist.items():
                expected_poly[size+n-1]+=n*fcount
                expected_poly[size+n]+=fcount
            assert direct_poly==expected_poly,(n,direct_poly,expected_poly)
            assert min(direct_poly)==predicted_min
            assert direct_poly[predicted_min]==predicted_min_count
        counts[n]=(count_valid,minf,hist[minf],predicted_min,predicted_min_count)
    for n,val in sorted(counts.items()):
        print(f'n={n}: edge selections satisfying distinct nonempty incidence signatures={val[0]}, '
              f'minimum edges={val[1]}, minimizing selections={val[2]}, '
              f'minimum code size={val[3]}, minimizing codes={val[4]}')
    print('All independent finite checks passed.')

if __name__=='__main__':
    main()
