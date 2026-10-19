#!/usr/bin/env python3
"""Exact enumerations for pairwise odd-occupancy independence theorem."""
from fractions import Fraction as F
from itertools import product, combinations

def closed(n, p, q):
    return ((1-2*p-2*q)**n - ((1-2*p)*(1-2*q))**n)/4

def direct(n, probs, i, j):
    e_i=e_j=e_ij=F(0)
    for seq in product(range(len(probs)), repeat=n):
        w=F(1)
        for x in seq: w*=probs[x]
        oi=(seq.count(i)%2)
        oj=(seq.count(j)%2)
        e_i+=w*oi; e_j+=w*oj; e_ij+=w*oi*oj
    return e_ij-e_i*e_j

def run():
    count=0
    for m in (2,3,4):
        # Sum to one (with optional residual), all categories positive.
        profiles=[tuple(F(k,20) for k in range(1,m+1))]
        profiles += [tuple(F(k, (m+1)*m) for k in range(1,m+1))]
        for base in profiles:
            residual=1-sum(base)
            probs=base + ((residual,) if residual>0 else ())
            assert sum(probs)==1
            for n in range(1,7):
                for i,j in combinations(range(m),2):
                    value=direct(n,probs,i,j)
                    formula=closed(n,base[i],base[j])
                    assert formula==value,(n,base,i,j,formula,value)
                    if n%2:
                        assert value<0
                    else:
                        threshold=base[i]+base[j]-base[i]*base[j]-F(1,2)
                        assert (value>0)-(value<0)==(threshold>0)-(threshold<0)
                    count+=1
    import sympy as s
    t=s.sqrt(2)
    p=1-1/t
    a=1-2*p
    pair=1-4*p
    triple=1-6*p
    assert s.simplify(pair**2 - a**4)==0
    assert s.simplify(triple**2 - a**6)!=0
    assert 0<float(p)<1/3
    for k in range(1,101):
        assert s.simplify((pair**(2*k)-a**(4*k))/4)==0
        assert s.simplify(triple**(2*k)-a**(6*k))!=0
        count+=2
    # Verify a nonmonotone sign switch as the third residual probability varies.
    assert closed(2,F(1,5),F(1,5))<0
    assert closed(2,F(1,3),F(1,3))>0
    assert closed(2,F(1,4),F(1,3))==0
    print('VERIFIED exact direct multinomial enumeration, signs, and symbolic independence cases:',count)
if __name__=='__main__':run()
