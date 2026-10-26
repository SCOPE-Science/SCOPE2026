#!/usr/bin/env python3
"""Independent finite-case check of the class-size census for Aut(C_p + C_(p^b))."""
from collections import Counter
from itertools import product

def units(p,b):
    m=p**b
    return [d for d in range(m) if d%p]

def group(p,b):
    return list(product(range(1,p),range(p),range(p),units(p,b)))

def multiply(A,B,p,b):
    a,u,v,d=A; aa,uu,vv,dd=B
    m=p**b
    return ((a*aa)%p, (a*uu+u*dd)%p,
            (v*aa+d*vv)%p, (p**(b-1)*v*uu+d*dd)%m)

def predicted(p,b):
    return Counter({1:(p-1)*p**(b-1),p*(p-1):(p-1)*(p*p-1)*p**(b-1),p*p:(p-1)*(p-2)*p**(b+1)})

def test(p,b):
    G=group(p,b); n=len(G)
    want=(p-1)**2*p**(b+1)
    assert n==want,(p,b,n,want)
    measured=Counter()
    for A in G:
        centralizer=sum(multiply(A,B,p,b)==multiply(B,A,p,b) for B in G)
        assert n%centralizer==0,(p,b,A,centralizer)
        measured[n//centralizer]+=1
    formula=predicted(p,b)
    for z in list(formula):
        if formula[z]==0: del formula[z]
    assert measured==formula,(p,b,measured,formula)
    cls=sum(count//sz for sz,count in measured.items())
    assert cls==p**(b-2)*(p-1)*(p*p+1),(p,b,cls)
    print(f'p={p} b={b} order={n} classes={cls} sizes={dict(sorted(measured.items()))}')

if __name__=='__main__':
    for p,b in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(5,2)]:
        test(p,b)
    print('AUT_CYCLIC_MIXED_CLASS_EQUATION_OK')
