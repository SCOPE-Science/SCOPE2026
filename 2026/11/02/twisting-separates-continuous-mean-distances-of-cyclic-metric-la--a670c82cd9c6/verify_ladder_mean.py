#!/usr/bin/env python3
"""Exact edge-pair integration for unit-edge prisms and Möbius ladders.

Usage: python3 verify_ladder_mean.py
No external packages are required. The finite checks corroborate the
all-parameter argument given in RESULT.md; they are not its replacement.
"""
from collections import deque
from fractions import Fraction as Q


def graph(n, twisted):
    N = 2*n
    edges = set()
    def add(i,j): edges.add(tuple(sorted((i,j))))
    if twisted:
        for i in range(N): add(i,(i+1)%N)
    else:
        for layer in range(2):
            for i in range(n): add(layer*n+i,layer*n+(i+1)%n)
    for i in range(n): add(i,i+n)
    return sorted(edges)


def distances(n, edges):
    N=2*n
    adj=[set() for _ in range(N)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    mat=[]
    for source in range(N):
        row=[None]*N;row[source]=0
        q=deque([source])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if row[v] is None:
                    row[v]=row[u]+1;q.append(v)
        assert None not in row
        mat.append(row)
    return mat


def clip(poly, a, b, c):
    if not poly:return []
    def v(p):return a*p[0]+b*p[1]+c
    out=[]
    prev=poly[-1];last=v(prev)
    for cur in poly:
        new=v(cur)
        if (last<0<new) or (new<0<last):
            t=last/(last-new)
            out.append((prev[0]+t*(cur[0]-prev[0]),
                        prev[1]+t*(cur[1]-prev[1])))
        if new<=0:out.append(cur)
        prev,last=cur,new
    return out


def integrate_affine(poly,a,b,c):
    if len(poly)<3:return Q(0)
    area2=xsum=ysum=Q(0)
    for j,(x,y) in enumerate(poly):
        xx,yy=poly[(j+1)%len(poly)]
        cross=x*yy-xx*y
        area2+=cross
        xsum+=(x+xx)*cross
        ysum+=(y+yy)*cross
    return (a*xsum+b*ysum)/6+c*area2/2


def pair_integral(e,f,dist):
    if e==f:return Q(1,3)
    u,v=e; s,t=f
    forms=[(Q(1),Q(1),Q(dist[u][s])),
           (Q(1),Q(-1),Q(1+dist[u][t])),
           (Q(-1),Q(1),Q(1+dist[v][s])),
           (Q(-1),Q(-1),Q(2+dist[v][t]))]
    square=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    total=Q(0)
    for i,fi in enumerate(forms):
        region=square
        for j,fj in enumerate(forms):
            if i!=j:
                region=clip(region, *(fi[k]-fj[k] for k in range(3)))
                if not region:break
        total+=integrate_affine(region,*fi)
    return total


def expected(n,twisted):
    edges=graph(n,twisted); d=distances(n,edges)
    h=[e for e in edges if e[1]-e[0]!=n]
    v=[e for e in edges if e[1]-e[0]==n]
    assert len(h)==2*n and len(v)==n
    total={('H','H'):Q(0),('H','V'):Q(0),('V','V'):Q(0)}
    for l1,l2,A,B in [('H','H',h,h),('H','V',h,v),('V','V',v,v)]:
        total[(l1,l2)]=sum((pair_integral(e,f,d) for e in A for f in B), Q(0))/len(A)/len(B)
    hh=total[('H','H')];hv=total[('H','V')];vv=total[('V','V')]
    return hh,hv,vv,Q(4,9)*hh+Q(4,9)*hv+Q(1,9)*vv, Q(sum(map(sum,d)),(2*n)**2)


def formulas(n,twisted):
    n=Q(n); odd=(int(n)%2==1)
    if twisted:
        hh=hv=n/4+Q(1,2)-1/(12*n)
        vv=n/4+Q(2,3)-1/(3*n)-(Q(1,4) if odd else Q(1,6))/n
        vertex=n/4+Q(1,2)-(Q(1,4) if odd else Q(1,2))/n
    else:
        hh=n/4+Q(1,2)+1/(6*n)
        hv=n/4+Q(1,2)
        vv=n/4+Q(2,3)-1/(3*n)-(Q(1,4) if odd else Q(0))/n
        vertex=n/4+Q(1,2)-(Q(1,4) if odd else Q(0))/n
    return hh,hv,vv,Q(4,9)*hh+Q(4,9)*hv+Q(1,9)*vv,vertex


def main():
    count=0
    for n in range(3,19):
        direct_p=expected(n,False);direct_m=expected(n,True)
        for twisted,vals in [(False,direct_p),(True,direct_m)]:
            expected_vals=formulas(n,twisted)
            for k,(got,want) in enumerate(zip(vals,expected_vals)):
                assert got==want,(n,twisted,k,got,want)
                count+=1
        expected_gap=Q(4,27*n) if n%2 else Q(1,6*n)
        assert direct_p[3]-direct_m[3]==expected_gap
        count+=1
        discrete_gap=Q(0) if n%2 else Q(1,2*n)
        assert direct_p[4]-direct_m[4]==discrete_gap
        count+=1
    print(f'PASS: {count} exact rational mean/conditional/vertex/difference comparisons for n=3,...,18')

if __name__=='__main__':main()
