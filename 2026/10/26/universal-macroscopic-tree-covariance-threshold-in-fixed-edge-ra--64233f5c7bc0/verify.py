#!/usr/bin/env python3
"""Independent finite graph enumeration and asymptotic checks for an exact random-graph dependence law."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, exp, floor, log, sqrt


def fall(a, q):
    z=1
    for t in range(q): z *= a-t
    return z


def ratio(n,r,k):
    assert 1<=r<=n-3 and 2<=k<=n-r
    total=comb(n,2); remaining=comb(n-r,2)
    return Fraction(fall(n-k,r)*fall(total,k-1), fall(n,r)*fall(remaining,k-1))


def rootscale(n,r):
    p=comb(n-r,2); N=comb(n,2)
    logratio = 0.
    logs = {}
    for k in range(2,n-r+1):
        if k==2:
            lr=sum(log((n-k-i)/(n-i)) for i in range(r)) + sum(log((N-i)/(p-i)) for i in range(k-1))
        else:
            lr+=log((n-k-r+1)/(n-k+1)) + log((N-k+2)/(p-k+2))
        logs[k]=lr
    for k in range(3,n-r):
        if logs[k]>=0 and logs[k+1]<0:
            return k+logs[k]/(logs[k]-logs[k+1])
    raise AssertionError('missing decreasing sign crossing')


def enumerate_graphs():
    checked=0; graphs=0
    for n in (4,5,6):
        E=[(i,j) for i in range(n) for j in range(i+1,n)]
        eindex={pair:t for t,pair in enumerate(E)}
        templates={}
        for k in range(3,n):
            shapes=[('path',tuple((j,j+1) for j in range(k-1)))]
            if k>=4:
                shapes.append(('star',tuple((0,j) for j in range(1,k))))
            for label,edges in shapes:
                patterns=set()
                for placement in permutations(range(n),k):
                    mask=0
                    for a,b in edges:
                        pair=tuple(sorted((placement[a],placement[b])))
                        mask|=1<<eindex[pair]
                    patterns.add(mask)
                templates[(k,label)]=tuple(patterns)
        stats=defaultdict(lambda:[0,0,0,0,0,0])
        for graph in range(1<<len(E)):
            m=graph.bit_count(); deg=[0]*n
            for j,(a,b) in enumerate(E):
                if graph>>j & 1:
                    deg[a]+=1;deg[b]+=1
            leaf=sum(d==0 for d in deg)
            f1,f2=leaf,leaf*(leaf-1)
            for (k,label),patterns in templates.items():
                x=sum((graph & p)==p for p in patterns)
                z=stats[(k,label,m)]; z[0]+=1;z[1]+=x
                z[2]+=f1; z[3]+=f1*x
                z[4]+=f2; z[5]+=f2*x
            graphs+=1
        for (k,label,m),v in stats.items():
            cnt,sx,s1,sx1,s2,sx2=v
            for r,sf,sxf in ((1,s1,sx1),(2,s2,sx2)):
                if not(1<=r<=n-3 and k<=n-r and k-1<=m<=comb(n-r,2)):
                    continue
                if sf==0 or sx==0: raise AssertionError('unexpected zero expectation')
                empirical=Fraction(sxf*cnt,sx*sf)
                target=ratio(n,r,k)
                assert empirical==target,(n,r,k,label,m,empirical,target)
                checked+=1
    return checked,graphs


def unimodal_test():
    comparisons=0
    for n in range(4,65):
        for r in range(1,n-2):
            assert ratio(n,r,2)==1
            assert ratio(n,r,3)>1
            ratios=[ratio(n,r,k) for k in range(2,n-r+1)]
            direction=[]
            for k in range(2,n-r):
                d=ratios[k-1]-ratios[k-2]  # R(k+1)-R(k)
                expected=(n*n-n*r-2-k*(2*n-r-3))
                assert (d>0)-(d<0)==(expected>0)-(expected<0)
                direction.append((d>0)-(d<0))
                comparisons+=1
            assert direction==sorted(direction,reverse=True)
            signs=[(x>1)-(x<1) for x in ratios[1:]]
            assert signs==sorted(signs,reverse=True)
    return comparisons


def asymptotic_test():
    a=.6;b=.9
    for _ in range(100):
        mid=(a+b)/2
        if log(1-mid)+2*mid>0: a=mid
        else:b=mid
    rho=(a+b)/2
    assert abs(rho-0.79681213002002)<3e-14
    comparisons=0
    for r in (1,2,3,4):
        C=lambda x:-2+(r+1)*x+2*x*x-(r-1)*x/(2*(1-x))
        kappa=-C(rho)/(2-1/(1-rho))
        for n in (1000,10000):
            threshold=rootscale(n,r)
            assert abs(threshold-(rho*n+kappa))<.05, (n,r,threshold,rho*n+kappa)
            comparisons+=1
    return rho,comparisons


def main():
    x,y=enumerate_graphs()
    z=unimodal_test()
    rho,asym=asymptotic_test()
    print(f'PASS exact random-graph enumeration: {x} parameter/motif comparisons over {y} labeled graphs')
    print(f'PASS adjacent-ratio and unimodality tests: {z} comparisons')
    print(f'PASS critical root numerical checks: {asym}; rho={rho:.15f}')
    print(f'TOTAL CHECKS: {x+z+asym}')

if __name__=='__main__': main()
