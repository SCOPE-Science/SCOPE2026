"""Independent finite-prime-field checker for fourth-order substitution groups.
Run: python jet_group_check.py
Uses direct truncated-series composition, not normal forms or group-theory software.
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd


def compose(f, g, q):
    a,b,c,d=f
    A,B,C,D=g
    return ((a*A)%q,
            (a*B+b*A*A)%q,
            (a*C+2*b*A*B+c*A*A*A)%q,
            (a*D+b*(2*A*C+B*B)+3*c*A*A*B+d*A*A*A*A)%q)


def expected_orbit_size_counts(q):
    h=q-1
    d=gcd(3,h)
    expected=defaultdict(Counter)
    def add(a,size,number_of_classes):
        expected[a][size]+=size*number_of_classes
    add(1,1,1)
    add(1,h//d,d)
    add(1,q*h,q)
    add(1,q*h//2,2)
    add(q-1,q*q,1)
    add(q-1,q*q*h//2,2)
    for a in range(1,q):
        if a!=1 and a**3%q==1:
            add(a,q*q,1)
            add(a,q*q*h//3,3)
        elif a not in (1,q-1):
            add(a,q**3,1)
    return expected


def test(q):
    group=list(product(range(1,q),range(q),range(q),range(q)))
    N=len(group)
    pair_count=0
    actual=defaultdict(Counter)
    for f in group:
        centralizer=0
        for g in group:
            if compose(f,g,q)==compose(g,f,q):
                centralizer+=1
        assert N%centralizer==0
        actual[f[0]][N//centralizer]+=1
        pair_count+=centralizer
    expect=expected_orbit_size_counts(q)
    assert dict(actual)==dict(expect),(q,actual,expect)
    d=gcd(3,q-1)
    k=2*q+4*d
    assert pair_count==k*N,(q,pair_count,k*N)
    assert sum(sum(count//size for size,count in C.items()) for C in actual.values())==k
    print(f'q={q}: |G|={N}; commuting ordered pairs={pair_count}; classes={k}; multiplier-resolved class sizes verified')


if __name__=='__main__':
    for q in (5,7): test(q)
    print('ALL_FOUR_JET_CHECKS_PASSED')
