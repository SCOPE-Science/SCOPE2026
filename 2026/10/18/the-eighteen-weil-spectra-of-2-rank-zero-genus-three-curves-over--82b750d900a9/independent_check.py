#!/usr/bin/env python3
"""Independent polynomial-field, root-fiber, and fourth-extension checker.

Use after verify_classification.py: python independent_check.py.
No imports from the primary verifier or optional packages.
"""
import csv
from collections import Counter

MOD={2:0x7,4:0x19,6:0x61,8:0x11d}

def product(u,v,m):
    w=0
    for i in range(m):
        if (v>>i)&1:
            w^=u<<i
    top=w.bit_length()-1
    while top>=m:
        if (w>>top)&1:
            w^=MOD[m]<<(top-m)
        top-=1
    return w

def eval_polynomial(coefficients,x,m):
    p=0
    for coef in coefficients[::-1]:
        p=product(p,x,m)^coef
    return p

def number_of_points(tuple4,m):
    quadratic_roots=[z for z in range(2,1<<m) if product(z,z,m)^z^1==0]
    assert len(quadratic_roots)==2
    w=max(quadratic_roots)  # deliberately choose conjugate embedding
    field_coeff=[0,1,w,w^1]
    a,b,c,d=(field_coeff[k] for k in tuple4)
    polynomial=[d,c,0,b,0,a,0,1]
    fibers=Counter(product(y,y,m)^y for y in range(1<<m))
    assert set(fibers.values())=={2} and len(fibers)==(1<<(m-1))
    return 1+sum(fibers.get(eval_polynomial(polynomial,x,m),0) for x in range(1<<m))

def main():
    with open('classification.csv',encoding='utf-8',newline='') as stream:
        rows=list(csv.DictReader(stream))
    assert len(rows)==32
    seen=set()
    for row in rows:
        r={k:int(v) for k,v in row.items()}
        key=(r['a'],r['b'],r['c'],r['d'])
        assert key not in seen
        seen.add(key)
        assert key[0]==0 and key[3] in (0,2)
        ns=[number_of_points(key,m) for m in (2,4,6,8)]
        assert ns[:3]==[r['N1'],r['N2'],r['N3']]
        e1,e2,e3=r['e1'],r['e2'],r['e3']
        s1,s2,s3=(4**i+1-ns[i-1] for i in (1,2,3))
        assert e1==s1 and s2==e1*e1-2*e2 and s3==e1*s2-e2*s1+3*e3
        s4=e1*s3-e2*s2+e3*s1-16*e2
        assert 4**4+1-ns[3]==s4
    assert len(seen)==32
    print('PASS: 32 distinct representatives; alternate irreducible moduli')
    print('PASS: direct y^2+y=f(x) root-fiber enumeration reproduces N1,N2,N3')
    print('PASS: independent N4 counts verify genus-three functional equation for every class')

if __name__=='__main__':main()
