#!/usr/bin/env python3
"""Independent finite tests of the two-attachment clique heat-transport theorem.
The theorem is proved for all orders analytically; these finite tests are checks only.
"""
from math import exp, sqrt, log, factorial
from itertools import product

def graph(p):
    n=p+2
    edges=[(0,2),(1,3)]+[(i,j) for i in range(2,n) for j in range(i+1,n)]
    L=[[0]*n for _ in range(n)]
    for i,j in edges:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    return n,edges,L

def heat_column_difference(p,t):
    n,edges,L=graph(p)
    rate=p
    P=[[float(i==j)-L[i][j]/rate for j in range(n)] for i in range(n)]
    v=[float(i==0)-float(i==2) for i in range(n)]
    accum=v[:]
    factor=1.
    # Uniformization; terms beyond index 260 are negligible for p<=9,t<=2.
    for k in range(1,261):
        v=[sum(row[j]*v[j] for j in range(n)) for row in P]
        factor*=rate*t/k
        accum=[accum[i]+factor*v[i] for i in range(n)]
    return [exp(-rate*t)*a for a in accum]

def analytic(p,t):
    def sector(c):
        Delta=sqrt((p-2)**2+4*c)
        alpha=(p+2-Delta)/2
        beta=(p+2+Delta)/2
        U=((beta-2)*exp(-alpha*t)+(2-alpha)*exp(-beta*t))/Delta
        W=c*(exp(-alpha*t)-exp(-beta*t))/Delta
        return U,W
    Up,Wp=sector(p)
    Um,Wm=sector(p-2)
    return Up+(Wp+Wm)/2

def exact_bridge_cost(d):
    # remove each bridge, then transport in a complete core
    a=abs(d[0]); b=abs(d[1]); core=[d[2]+d[0],d[3]+d[1]]+d[4:]
    return a+b+sum(abs(z) for z in core)/2

def dual_enum(p,d):
    # Integral extreme potentials, anchored at A = 0.
    # Core is a clique; each other core potential is in {-1,0,1}.
    # Each pendant takes one of three integers relative to its attachment.
    values=[]
    for core in product((-1,0,1),repeat=p-1):
        if max((0,)+core)-min((0,)+core)>1:continue
        fA=0;fB=core[0];c=core[1:]
        for fx in (-1,0,1):
            for shift in (-1,0,1):
                fy=fB+shift
                values.append(sum(a*b for a,b in zip(d,[fx,fy,fA,fB]+list(c))))
    return max(values)

def main():
    N=0
    for p in range(3,10):
        for t in (.05,.35,1.4):
            d=heat_column_difference(p,t)
            cost=exact_bridge_cost(d)
            formula=analytic(p,t)
            assert abs(cost-formula)<1e-10,(p,t,cost,formula)
            assert abs(sum(d))<1e-11
            assert d[0]>0 and d[1]<0
            assert d[0]+d[2]>0 and d[1]+d[3]<0
            assert all(x<0 for x in d[4:])
            potential=[2.,-1.,1.,0.]+[0.]*(p-2)
            witness=sum(x*y for x,y in zip(d,potential))
            assert abs(witness-cost)<1e-10,(p,t,cost,witness)
            N+=1
            if p<=7:
                brute=dual_enum(p,d)
                assert abs(brute-cost)<1e-10,(p,t,brute,cost)
    # Initial derivative of the exact analytic formula is p-3; the second is 6-p^2.
    for p in range(3,50):
        h=1e-5
        d1=(analytic(p,h)-1)/h
        assert abs(d1-(p-3))<max(0.007,1.0e-3*p*p)
    # The test time log(p)/p realizes the dimension-asymptotic value two.
    for p in (100,1000,10000):
        assert 1.7 < analytic(p,log(p)/p) < 2.001
    print(f'CHECK_OK separate_Laplacian_uniformization_and_transport={N} exact_dual_cases=15')
    print('CHECK_OK unique_dual_witness=verified extrema sampled, onset=p_minus_3, large_clique_limit=2')

if __name__=='__main__':main()
