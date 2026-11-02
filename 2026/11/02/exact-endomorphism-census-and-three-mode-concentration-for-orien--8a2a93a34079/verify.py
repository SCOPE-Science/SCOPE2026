#!/usr/bin/env python3
"""Independent finite verification of an endomorphism count for oriented-star monoids.

Uses canonical monoid multiplication, not a precomputed graph-admissibility predicate.
Python 3, standard library only; run with `python3 verify.py`.
"""
from itertools import product
from math import comb


def count_formula(m):
    assert m >= 1
    return sum(comb(m, a) * ((2 * (2**a + 2**(m-a) - 1))**m
              + (2**a + 2**(m-a+1) - 1)**m)
               for a in range(m+1))


def monoid(m):
    masks = range(1 << m)
    # (0,u,0) = leaf product u; (1,p,q) = L_p c L_q with p & q = 0
    return [(0,u,0) for u in masks] + [
        (1,p,q) for p in masks for q in masks if not p&q]


def mult(x, y):
    bx,p,q = x
    by,r,s = y
    if not bx and not by:
        return (0,p|r,0)
    if not bx and by:
        return (1,(p|r)&~s,s)
    if bx and not by:
        return (1,p&~(q|r),q|r)
    t=q|r|s
    return (1,p&~t,t)


def prod(*args):
    out=args[0]
    for arg in args[1:]:
        out=mult(out,arg)
    return out


def image_idempotent(mask):
    leaves=mask >> 1
    return (1,0,leaves) if mask&1 else (0,leaves,0)


def direct_count(m):
    n=m+1
    count=0
    strata={}
    for masks in product(range(1<<n),repeat=n):
        xs=[image_idempotent(x) for x in masks]
        center=xs[0]
        leaves=xs[1:]
        if not all(prod(center,x,center)==prod(x,center,x)==prod(center,x)
                   for x in leaves):
            continue
        if not all(mult(leaves[i],leaves[j])==mult(leaves[j],leaves[i])
                   for i in range(m) for j in range(i+1,m)):
            continue
        count+=1
        a=sum(x&1 for x in masks[1:])
        b=masks[0]&1
        strata[a,b]=strata.get((a,b),0)+1
    return count,strata


def check():
    for m in range(1,4):
        elts=monoid(m)
        lookup=set(elts)
        assert len(elts)==2**m+3**m
        assert all(mult(x,y) in lookup for x in elts for y in elts)
        assert all(prod(x,y,z)==mult(x,mult(y,z))
                   for x in elts for y in elts for z in elts)
        idem={x for x in elts if mult(x,x)==x}
        assert idem=={image_idempotent(mask) for mask in range(1 << (m+1))}
        total,strata=direct_count(m)
        predicted=count_formula(m)
        assert total==predicted,(m,total,predicted)
        expected={} 
        for a in range(m+1):
            k=2**a+2**(m-a)-1
            expected[a,1]=comb(m,a)*2**m*k**m
            expected[a,0]=comb(m,a)*(k+2**(m-a))**m
        assert strata==expected,(m,strata,expected)
        print('m=',m,'monoid_size=',len(elts),'endomorphisms=',total,'independent_strata=OK')
    values=[15,339,22233,4780047,4058199945]
    assert [count_formula(m) for m in range(1,6)]==values
    for m in [10,20,30]:
        ratio=count_formula(m)/(1 << (m*(m+1)))
        print('asymptotic_check_m=',m,'ratio=',f'{ratio:.12f}')
    print('VERIFY_OK')

if __name__=='__main__':
    check()
