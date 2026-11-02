"""Independent finite tests of weighted graph p-heat oscillation decay.

The universal statement is proved analytically; this script checks the exact
pairwise formula and sharpness witnesses on finite rational configurations.
Only standard Python libraries are required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import inf
import random


def phi(s, p):
    return (abs(s)**(p-2))*s if s != 0 else 0


def pair_coefficient(i,j,p,w,m):
    n=len(m)
    direct=w[i][j]*(F(1,m[i])+F(1,m[j]))
    for z in range(n):
        if z==i or z==j or not(w[i][z] and w[j][z]):continue
        a=w[i][z]/m[i];b=w[j][z]/m[j]
        if p<=2:direct+=min(a,b)
        elif p==3:direct+=a*b/(a+b)
        else:direct+= (a**(-1/(p-2))+b**(-1/(p-2)))**(-(p-2))
    return direct


def witness(i,j,p,w,m):
    n=len(m);u=[F(1,2)]*n;u[i]=F(1);u[j]=F(0)
    for z in range(n):
        if z in (i,j):continue
        a=w[i][z]/m[i];b=w[j][z]/m[j]
        if a and b:
            if p<=2:u[z]=F(0) if a<=b else F(1)
            elif p==3:u[z]=a/(a+b)
            else:
                ra=float(a)**(1/(p-2));rb=float(b)**(1/(p-2))
                u[z]=ra/(ra+rb)
        elif a:u[z]=F(1)
        elif b:u[z]=F(0)
    return u


def flow(u,p,w,m):
    n=len(m)
    return [sum((w[i][j]/m[i])*phi(u[j]-u[i],p) for j in range(n)) for i in range(n)]


def dini(u,du):
    lo=min(u);hi=max(u)
    return max(du[i] for i,v in enumerate(u) if v==hi)-min(du[j] for j,v in enumerate(u) if v==lo)


def graph(n,rng):
    w=[[F(0) for _ in range(n)] for _ in range(n)]
    # Spanning tree plus arbitrary further edges: guaranteed connected.
    for j in range(1,n):
        i=rng.randrange(j)
        w[i][j]=w[j][i]=F(rng.randint(1,5))
    for i,j in combinations(range(n),2):
        if not w[i][j] and rng.randrange(2):w[i][j]=w[j][i]=F(rng.randint(1,5))
    m=[F(rng.randint(1,5)) for _ in range(n)]
    return w,m


def main():
    rng=random.Random(18192026);exact=0;inequalities=0
    for n in range(2,9):
        for _ in range(35):
            w,m=graph(n,rng)
            for p in [2,3]:
                lam=min(pair_coefficient(i,j,p,w,m) for i,j in combinations(range(n),2))
                i,j=min(combinations(range(n),2),key=lambda ij:pair_coefficient(*ij,p,w,m))
                u=witness(i,j,p,w,m)
                du=flow(u,p,w,m)
                # Every extremal-pair derivative bounded by -lambda.
                assert du[i]-du[j]==-lam, (n,p,du[i]-du[j],lam)
                assert dini(u,du)==-lam, (n,p,dini(u,du),lam)
                exact+=1
                for _ in range(8):
                    v=[F(rng.randrange(-12,13),rng.randint(1,9)) for k in range(n)]
                    dv=flow(v,p,w,m)
                    osc=max(v)-min(v)
                    if osc:assert dini(v,dv)<=-lam*(osc**(p-1)),(v,p,lam)
                    inequalities+=1
    print('EXACT_RATIONAL_SHARPNESS_OK',exact)
    print('EXACT_RATIONAL_OSCILLATION_BOUNDS_OK',inequalities)
    # Different exponents, with a tolerance only for floating-point evaluation.
    numeric=0
    for n in range(2,9):
        for _ in range(50):
            w,m=graph(n,rng)
            for p in [1.25,1.5,2.5,3.5,7]:
                lam=min(pair_coefficient(i,j,p,w,m) for i,j in combinations(range(n),2))
                v=[rng.random()*4-2 for k in range(n)]
                dv=flow(v,p,w,m);osc=max(v)-min(v)
                assert dini(v,dv)<=-float(lam)*osc**(p-1)+1e-8
                numeric+=1
    print('FLOATING_EXPONENT_DIAGNOSTICS_OK',numeric)
    # Exact topology test: lambda>0 if and only if diameter<=2.
    tested=0
    for n in range(2,7):
        edges=list(combinations(range(n),2))
        for mask in range(1,1<<len(edges)):
            w=[[F(0) for _ in range(n)] for _ in range(n)]
            for k,(i,j) in enumerate(edges):
                if (mask>>k)&1:w[i][j]=w[j][i]=F(1)
            reachable={0};
            while 1:
                new=reachable|{j for i in reachable for j in range(n) if w[i][j]}
                if new==reachable:break
                reachable=new
            if len(reachable)!=n:continue
            dist=[[inf]*n for _ in range(n)]
            for i in range(n):
                dist[i][i]=0
                for j in range(n):
                    if w[i][j]:dist[i][j]=1
            for k in range(n):
                for i in range(n):
                    for j in range(n):dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            lam=min(pair_coefficient(i,j,3,w,[F(1)]*n) for i,j in edges)
            assert (lam>0)==(max(max(row) for row in dist)<=2)
            tested+=1
    print('EXACT_DIAMETER_TWO_RIGIDITY_OK',tested)
    print('ALL_WEIGHTED_P_HEAT_OSCILLATION_CHECKS_OK')

if __name__=='__main__':main()
