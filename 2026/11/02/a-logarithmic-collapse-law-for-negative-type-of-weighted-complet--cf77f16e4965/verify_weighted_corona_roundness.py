#!/usr/bin/env python3
"""Independent finite checks for weighted complete-corona metric negative type.
Python >=3.9, standard library only. Finite checks corroborate the written proof.
"""
from fractions import Fraction as F
import math


def distances(m, t):
    """Shortest-path metric on clique vertices 0..m-1 and private leaves m..2m-1."""
    n = 2*m
    edges = []
    for i in range(m):
        for j in range(i+1,m):
            edges.append((i,j,F(1)))
        edges.append((i,m+i,t))
    d = [[F(0) if i == j else None for j in range(n)] for i in range(n)]
    for a,b,w in edges:
        d[a][b] = d[b][a] = w
    for k in range(n):
        for i in range(n):
            if d[i][k] is None: continue
            for j in range(n):
                if d[k][j] is None: continue
                s = d[i][k]+d[k][j]
                if d[i][j] is None or s < d[i][j]: d[i][j] = s
    return d


def form(d,z,p):
    return sum(z[i]*z[j]*d[i][j]**p
               for i in range(len(z)) for j in range(len(z)) if i != j)


def decomposition(m,t,z,p):
    x,y=z[:m],z[m:]
    s=sum(x,F(0))/m
    xi=[v-s for v in x]; eta=[v+s for v in y]
    A=(1+2*t)**p; B=(1+t)**p; C=t**p
    fluct=-sum(v*v for v in xi)-A*sum(v*v for v in eta)
    fluct+=2*(C-B)*sum(v*w for v,w in zip(xi,eta))
    radial=m*s*s*((m-1)*(1+A-2*B)-2*C)
    return fluct+radial


def threshold(m,t):
    def f(p): return (m-1)*(1+(1+2*t)**p-2*(1+t)**p)-2*t**p
    a,b=1.,2.
    for _ in range(95):
        c=(a+b)/2
        if f(c) > 0:b=c
        else:a=c
    return (a+b)/2


def jacobi(A):
    M=[list(map(float,row)) for row in A]
    n=len(M)
    for _ in range(70*n*n):
        mx=0.;u=v=0
        for i in range(n):
            for j in range(i+1,n):
                if abs(M[i][j]) > mx: mx=abs(M[i][j]);u=i;v=j
        if mx<1e-11:break
        tau=(M[v][v]-M[u][u])/(2*M[u][v])
        tan=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+tan*tan);s=tan*c
        auu,avv,auv=M[u][u],M[v][v],M[u][v]
        M[u][u]=auu-tan*auv;M[v][v]=avv+tan*auv
        M[u][v]=M[v][u]=0.
        for k in range(n):
            if k not in (u,v):
                a,b=M[k][u],M[k][v]
                M[k][u]=M[u][k]=c*a-s*b
                M[k][v]=M[v][k]=s*a+c*b
    return sorted(M[i][i] for i in range(n))


def zero_sum_matrix(d,p):
    n=len(d);q=[[float(x)**p for x in row] for row in d]
    return [[q[i][j]-q[i][n-1]-q[n-1][j]
             for j in range(n-1)] for i in range(n-1)]


def run():
    count=0
    for m in range(3,7):
        for t in [F(1,4), F(1), F(7,3), F(4)]:
            d=distances(m,t)
            assert all(d[i][j] > 0 for i in range(2*m) for j in range(2*m) if i!=j)
            for k in range(12):
                z=[F(((i+2*k)*(i+1)+3*k)%11-5) for i in range(2*m-1)]
                z.append(-sum(z))
                for p in (1,2,3):
                    assert form(d,z,p)==decomposition(m,t,z,p)
                    count+=1
    print('EXACT_QUADRATIC_DECOMPOSITION_OK checks=',count)
    spectral=0
    for m in range(3,10):
        for t in (.1,.5,1.,2.,10.):
            root=threshold(m,t)
            assert 1<root<2
            d=distances(m,F(str(t)))
            for p,kind in (((1+root)/2,'below'),(root,'critical'),((root+2)/2,'above')):
                eig=jacobi(zero_sum_matrix(d,p))
                # The zero-sum quadratic form has one positive direction above the endpoint.
                if kind=='below':assert eig[-1] < -1e-7,(m,t,kind,eig[-1])
                if kind=='critical':assert abs(eig[-1])<1e-7 and eig[-2]<-1e-7,(m,t,kind,eig[-2:])
                if kind=='above':assert eig[-1]>1e-7 and eig[-2]<-1e-7,(m,t,kind,eig[-2:])
                spectral+=1
    print('ENDPOINT_INERTIA_OK cases=',spectral)
    # p decreases with length t and with branching m.
    for m in (3,4,7,12,50):
        vals=[threshold(m,t) for t in (.01,.1,1.,10.,100.)]
        assert all(vals[i]>vals[i+1] for i in range(4))
    for t in (.03,.3,1.,5.):
        vals=[threshold(m,t) for m in (3,4,6,10,40,100)]
        assert all(vals[i]>vals[i+1] for i in range(5))
    print('STRICT_MONOTONICITY_CHECK_OK')
    m=5; pp=math.log2(2*m/(m-1))
    for t in (1000.,10000.):
        pred=pp+pp*(m-2)/(2*m*math.log(2))/t
        assert abs(threshold(m,t)-pred)*t<.15
    for t in (.0001,.00001):
        val=(2-threshold(3,t))*math.log(1/t)
        assert abs(val-math.log(2)) < .15,(t,val)
    for m in (400,800):
        h=3*math.log(3)-4*math.log(2)
        pred=1+2/((m-1)*h)
        assert abs(threshold(m,1.)-pred)*(m-1)<.1
    print('ASYMPTOTIC_DIAGNOSTICS_OK')
    print('EXAMPLE_OK m=3 t=1 threshold=',format(threshold(3,1.),'.12f'))
    print('ALL_WEIGHTED_CORONA_ROUNDNESS_CHECKS_OK')

if __name__=='__main__':run()
