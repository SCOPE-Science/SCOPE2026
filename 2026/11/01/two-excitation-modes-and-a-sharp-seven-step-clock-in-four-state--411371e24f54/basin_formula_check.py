#!/usr/bin/env python3
"""Expand 6561 cap signatures to exact labelled basin counts for small bipartite boards."""
import csv
from collections import Counter
from math import factorial

def multinomial_distribution(n):
    out=Counter()
    F=factorial(n)
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                l=n-i-j-k
                m=(i,j,k,l)
                cap=''.join(str(min(x,2)) for x in m)
                out[cap]+=F//(factorial(i)*factorial(j)*factorial(k)*factorial(l))
    return out

def summarize(a,b,table):
    wa,wb=multinomial_distribution(a),multinomial_distribution(b)
    total=Counter()
    for ac,bc,h,p in table:
        if ac in wa and bc in wb:
            total[(h,p)]+=wa[ac]*wb[bc]
    assert sum(total.values())==4**(a+b)
    return total

if __name__=='__main__':
    import sys
    assert len(sys.argv)==2,'pass cap_certificate.csv'
    with open(sys.argv[1],encoding='utf-8',newline='') as f:
        data=list(csv.DictReader(f))
    table=[(r['cap_A_0123'],r['cap_B_0123'],int(r['first_entry']),int(r['eventual_period'])) for r in data]
    assert len(table)==6561
    expected={
        (2,2):([1,15,65,161,14,0,0,0],1),
        (3,3):([1,63,665,2636,611,120,0,0],1),
        (4,4):([73,471,7169,36681,15054,4552,1536,0],73),
        (4,5):([241,1471,23731,135544,70561,21356,9240,0],241),
        (5,5):([801,5023,82025,491040,339387,96700,33600,0],801)
    }
    for (a,b),(hist,periodic) in expected.items():
        total=summarize(a,b,table)
        per=[sum(x for (t,p),x in total.items() if t==i) for i in range(8)]
        assert per==hist,(a,b,per,hist)
        assert sum(x for (t,p),x in total.items() if t==0)==periodic
        print(f'K_{a},{b} labelled={4**(a+b)} first_entry={per} exact weighted certificate PASS')
    print('BASIN-FORMULA CROSSCHECK PASS')
