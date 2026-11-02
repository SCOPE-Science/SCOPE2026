#!/usr/bin/env python3
"""Exact, parameter-free finite-state proof certificate for GH dynamics on C4-edge books.

No bound on number of pages is assumed. A nonempty set of occupied page-pair
states suffices because any pages initially of one type have identical evolution.
"""
from collections import Counter
import csv
import sys
from itertools import product
from math import comb

PAIRS = list(product(range(3), repeat=2))

def advance(old, is_exposed):
    return (old + 1) % 3 if old else int(is_exposed)

def step(hubs, images):
    u,v = hubs
    has_left = any(PAIRS[i][0] == 1 for i in images)
    has_right = any(PAIRS[i][1] == 1 for i in images)
    new_hubs = (advance(u, v == 1 or has_left),
                advance(v, u == 1 or has_right))
    new_images = []
    for i in images:
        a,b = PAIRS[i]
        a_new = advance(a, u == 1 or b == 1)
        b_new = advance(b, v == 1 or a == 1)
        new_images.append(3*a_new + b_new)
    return new_hubs, tuple(new_images)

def orbit(hubs, support):
    images = tuple(support)
    seen = {}
    for t in range(18):
        config = (hubs, images)
        if config in seen:
            return seen[config], t - seen[config]
        seen[config] = t
        hubs, images = step(hubs, images)
    raise AssertionError('finite support orbit exceeded certificate depth')

def circulation(u,v,a,b):
    def d(x,y):
        return (x == 0 and y == 1) - (x == 1 and y == 0)
    return d(u,a) + d(a,b) + d(b,v) + d(v,u)

def expected_period(hubs, support):
    u,v=hubs
    circs = {circulation(u,v,*PAIRS[i]) for i in support}
    if -1 in circs and 1 in circs:
        return 3
    if -1 in circs or 1 in circs:
        return 4
    return 1

def main():
    eventual = Counter()
    periodic = Counter()
    tcount = Counter()
    certificate_rows = []
    for u,v in product(range(3),repeat=2):
        for mask in range(1,1<<9):
            support=tuple(i for i in range(9) if mask & (1<<i))
            t,p = orbit((u,v),support)
            circs={circulation(u,v,*PAIRS[i]) for i in support}
            certificate_rows.append((u,v,mask,len(support),t,p, int(-1 in circs),int(1 in circs)))
            assert t <= 5
            assert p in (1,3,4)
            assert p == expected_period((u,v),support)
            eventual[(p,len(support))]+=1
            tcount[(p,t)]+=1
            if t==0:
                periodic[(p,len(support))]+=1
    N={p:tuple(eventual[(p,s)] for s in range(1,10)) for p in (1,3,4)}
    M={p:tuple(periodic[(p,s)] for s in range(1,10)) for p in (1,3,4)}
    expected_N={
        1:(57,153,225,195,99,27,3,0,0),
        3:(0,3,21,63,105,105,63,21,3),
        4:(24,168,510,876,930,624,258,60,6),
    }
    expected_M={
        1:(1,0,0,0,0,0,0,0,0),
        3:(0,3,3,0,0,0,0,0,0),
        4:(8,8,0,0,0,0,0,0,0),
    }
    assert N==expected_N and M==expected_M
    assert sum(map(sum,N.values()))==9*((1<<9)-1)==4599
    print('FULL SUPPORT CLASSIFICATION: 4599/4599 PASS; max entry <= 5; periods exactly 1,3,4')
    print('N eventual period by support size s=1..9:',N)
    print('M immediately periodic by support size s=1..9:',M)
    print('all initial support class entrance counts:',sorted(tcount.items()))
    # Inclusion-exclusion coefficients c_j for sum_s N_{p,s} * onto(k,s).
    def coeff(table,p):
        return tuple(sum(table[p][s-1]*(-1)**(s-j)*comb(s,j)
                         for s in range(max(j,1),10)) for j in range(1,10))
    assert {p:coeff(N,p) for p in (1,3,4)} == {
        1:(0,0,0,0,0,6,3,0,0),
        3:(0,0,0,0,0,0,3,-6,3),
        4:(0,0,0,0,0,-6,-6,6,6),
    }
    assert {p:coeff(M,p) for p in (1,3,4)} == {
        1:(1,0,0,0,0,0,0,0,0),
        3:(3,-6,3,0,0,0,0,0,0),
        4:(-8,8,0,0,0,0,0,0,0),
    }
    print("BASIN POLYNOMIAL COEFFICIENTS j=1..9:", {p:coeff(N,p) for p in (1,3,4)})
    print("PERIODIC-STATE POLYNOMIAL COEFFICIENTS j=1..9:", {p:coeff(M,p) for p in (1,3,4)})
    assert any(p==1 and t==4 and size==1 for _,_,_,size,t,p,_,_ in certificate_rows)
    assert any(p==1 and t==5 and size==2 for _,_,_,size,t,p,_,_ in certificate_rows)
    if len(sys.argv)==3 and sys.argv[1]=="--csv":
        with open(sys.argv[2],"w",newline="",encoding="utf-8") as fh:
            writer=csv.writer(fh,lineterminator="\n")
            writer.writerow(["hub_u","hub_v","support_mask","support_size","entry_time","least_period","has_negative_circulation","has_positive_circulation"])
            writer.writerows(certificate_rows)
        print("WROTE SUPPORT CLASSIFICATION CSV:",sys.argv[2],len(certificate_rows),"data rows")

if __name__=='__main__':
    main()
