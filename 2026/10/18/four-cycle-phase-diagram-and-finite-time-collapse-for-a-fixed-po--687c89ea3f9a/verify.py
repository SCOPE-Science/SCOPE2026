#!/usr/bin/env python3
"""Exact-rational finite checks for the stated two-step reduction and root phase table.
Proof of the all-parameter theorem is analytical; finite checks are diagnostics only.
"""
from fractions import Fraction as Q
from itertools import product

def T(x):
    assert 0<=x<=1
    return 2*x if x<=Q(1,2) else 2*(1-x)

def map_f(x,p,a,b):
    if x<=p:
        return 1-(1-a)*T(x/p)
    return b*T((x-p)/(1-p))

def H(t,c,d):
    return d*T(c*T(t))

def interval_roots(c,d):
    # independent affine-branch root extraction, including flat fixed intervals
    hinges=sorted(set([Q(0),Q(1,2),Q(1),*( [Q(1,4)/c, 1-Q(1,4)/c] if c>Q(1,2) else [])]))
    roots=set();intervals=[]
    for l,r in zip(hinges,hinges[1:]):
        yl=H(l,c,d)-l;yr=H(r,c,d)-r
        if yl==0 and yr==0:
            intervals.append((l,r));roots.add(l);roots.add(r)
        elif yl==0:roots.add(l)
        elif yr==0:roots.add(r)
        elif (yl<0<yr or yr<0<yl):
            roots.add(l+(r-l)*(-yl)/(yr-yl))
    return sorted(roots),intervals

def formula(c,d):
    K=4*c*d
    if K==1:
        return [],[Q(0), min(Q(1,2),Q(1,4)/c)]
    z=[Q(0)]
    if c<=Q(1,2):
        if K>1:z.append(K/(1+K))
    else:
        D=Q(1,4)/c;B=1-D;A=Q(1,4)/(1-c)
        if d>D and d<=A:z.append(2*d/(1+K))
        if d>=B and d<=A:z.append(2*d*(2*c-1)/(K-1))
        if d>=B:z.append(K/(1+K))
    return sorted(set(z)),[]

def test():
    tests=0
    grid=[Q(n,60) for n in range(1,60)]
    for c,d in product(grid,grid):
        roots,segments=interval_roots(c,d)
        expected,cont=formula(c,d)
        if cont:
            assert segments,('critical interval missing',c,d,roots,segments)
            assert segments[0][0]==0
            assert segments[0][1]==cont[1]
        else:
            assert roots==expected,('root mismatch',c,d,roots,expected)
        tests+=1
    # force all codimension-one boundaries in rational arithmetic
    for c in [Q(2,5),Q(1,2),Q(3,5),Q(2,3),Q(3,4),Q(4,5),Q(9,10)]:
        points=[Q(1,4)/c,1-Q(1,4)/c,Q(1,4)/(1-c)]
        for d in points:
            if not (0<d<1):continue
            roots,segments=interval_roots(c,d);expected,cont=formula(c,d)
            if cont:assert segments and segments[0][1]==cont[1],(c,d,segments,cont)
            else:assert roots==expected,(c,d,roots,expected)
            tests+=1
    for c,d in [(Q(1,2),Q(1,4)),(Q(3,4),Q(1,3)),(Q(4,5),Q(2,5)),(Q(4,5),Q(11,16)),(Q(4,5),Q(9,10)),(Q(3,5),Q(5,8)),(Q(3,5),Q(4,5))]:
        p=Q(1,2);a=1-(1-p)*c;b=p*d
        assert p<a<1 and 0<b<p
        for j in range(501):
            t=Q(j,500);x=p*t
            Fx=map_f(x,p,a,b)
            assert Fx>p and Fx<=1
            F2=map_f(Fx,p,a,b)
            assert F2/p==H(t,c,d),('return failure',c,d,t,F2/p,H(t,c,d))
            if 4*c*d==1:
                assert H(H(t,c,d),c,d)==H(t,c,d)
            elif 4*c*d<1:
                assert H(t,c,d)<=4*c*d*t
            tests+=1
    print('PASS exact-rational tests',tests)
    for c,d in [(Q(1,2),Q(1,4)),(Q(3,4),Q(1,3)),(Q(4,5),Q(2,5)),(Q(4,5),Q(11,16)),(Q(4,5),Q(9,10)),(Q(3,5),Q(5,8)),(Q(3,5),Q(4,5))]:
        print('c=',c,'d=',d,'K=',4*c*d,'roots/interval=',formula(c,d))

if __name__=='__main__':test()
