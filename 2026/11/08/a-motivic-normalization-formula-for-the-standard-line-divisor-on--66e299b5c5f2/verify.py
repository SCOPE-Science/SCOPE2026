#!/usr/bin/env python3
"""Finite-field verification of arithmetic incidence of standard Fermat lines."""
from itertools import product

def representatives(p):
    for tail in product(range(p), repeat=3): yield (1,)+tail
    for tail in product(range(p), repeat=2): yield (0,1)+tail
    for z in range(p): yield (0,0,1,z)
    yield (0,0,0,1)

def profile(p,d):
    matchings=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
    r={0:0,1:0,2:0,d:0}
    for v in representatives(p):
        t=[pow(x,d,p) for x in v]
        if sum(t)%p: continue
        k=0
        for pair1,pair2 in matchings:
            if (t[pair1[0]]+t[pair1[1]])%p or (t[pair2[0]]+t[pair2[1]])%p: continue
            if v[pair1[0]]==v[pair1[1]]==0 or v[pair2[0]]==v[pair2[1]]==0: k+=d
            else:k+=1
        if k:
            assert k in (1,2,d),(p,d,v,k)
            r[k]+=1
    return r

def run():
    c=0
    for p in (3,5,7,11,13,17,19,23):
        for d in range(3,9):
            if d%p==0: continue
            s=sum(pow(x,d,p)==p-1 for x in range(1,p))
            expected={1:3*s*s*(p-1-2*s),2:3*s**3,d:6*s}
            got=profile(p,d)
            for k in (1,2,d): assert got[k]==expected.get(k,0),(p,d,s,k,got,expected)
            c+=1
    print('VERIFY_FERMAT_MOTIVIC_OK prime_degree_cases='+str(c))
if __name__=='__main__':run()
