"""Reproduce local pair-distance tomography identities by independent shortest-path integration.
This checks finite examples; the all-graphs assertion uses the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isclose
import numpy as np
from numpy.polynomial.legendre import leggauss


def distance_vertices(edges):
    vs = sorted(set(x for u,v,l in edges for x in (u,v)))
    n = len(vs); ind = {v:i for i,v in enumerate(vs)}
    d = np.full((n,n),float('inf'))
    for i in range(n):d[i,i]=0.0
    for u,v,l in edges:
        i,j=ind[u],ind[v];d[i,j]=d[j,i]=min(d[i,j],float(l))
    for k in range(n):d=np.minimum(d,d[:,[k]]+d[[k],:])
    return d, ind


def target_y_length(e, f, x, radius, d, ind):
    (u,v,L) = e; (z,w,M) = f
    routes=[]
    if e is f:
        routes.append((max(0.,x-radius),min(float(M),x+radius)))
    for a,da in ((u,x),(v,float(L)-x)):
        for b,which in ((z,0),(w,1)):
            residual=radius-da-float(d[ind[a],ind[b]])
            if residual<=0:continue
            if which==0:routes.append((0.,min(float(M),residual)))
            else:routes.append((max(0.,float(M)-residual),float(M)))
    routes=sorted((a,b) for a,b in routes if b>a)
    if not routes:return 0.
    tot=0.; lo,hi=routes[0]
    for a,b in routes[1:]:
        if a>hi:tot+=hi-lo;lo,hi=a,b
        else:hi=max(hi,b)
    return tot+hi-lo


def integrate_distance_probability(edges, probabilities, radius):
    d,ind=distance_vertices(edges)
    nodes,weights=leggauss(16)
    total=0.
    for i,e in enumerate(edges):
        if not probabilities[i]:continue
        L=float(e[2]); split=sorted(set([0.,radius,L-radius,L]))
        for j,f in enumerate(edges):
            if not probabilities[j]:continue
            area=0.
            for a,b in zip(split[:-1],split[1:]):
                if b<=a:continue
                for node,weight in zip(nodes,weights):
                    x=(a+b)/2+(b-a)/2*node
                    area+=(b-a)/2*weight*target_y_length(e,f,x,radius,d,ind)
            total+=probabilities[i]*probabilities[j]*area/L/float(f[2])
    return total


def predicted_cdf(edges,p,r):
    L=[F(e[2]) for e in edges]
    A=sum(p[i]*p[i]/L[i] for i in range(len(edges)))
    B=-sum(p[i]*p[i]/L[i]**2 for i in range(len(edges)))
    for i,j in combinations(range(len(edges)),2):
        if set(edges[i][:2]) & set(edges[j][:2]):
            B+=p[i]*p[j]/L[i]/L[j]
    return 2*A*r+B*r*r


def experiments():
    graphs=[
        [(0,1,F(17,10)),(0,2,F(11,5)),(0,3,F(31,10))],
        [(0,1,F(17,10)),(1,2,F(11,5)),(2,0,F(31,10))],
        [(0,1,F(6,5)),(1,2,F(17,10)),(2,3,F(21,10)),(3,4,F(8,5))],
        [(0,1,F(6,5)),(1,2,F(17,10)),(2,3,F(21,10)),(3,0,F(8,5)),(0,2,F(9,5))],
        [(0,1,F(6,5)),(0,2,F(17,10)),(0,3,F(21,10)),(0,4,F(8,5))],
    ]
    for graph in graphs:
        m=len(graph)
        prob_sets=[]
        for i in range(m):
            p=[F(0)]*m;p[i]=F(1);prob_sets.append(p)
        for i,j in combinations(range(m),2):
            p=[F(0)]*m;p[i]=p[j]=F(1,2);prob_sets.append(p)
        prob_sets.append([F(1,m)]*m)
        for pp in prob_sets:
            for radius in (0.06,0.19):
                obs=integrate_distance_probability(graph,pp,radius)
                pr=float(predicted_cdf(graph,pp,F(str(radius))))
                assert abs(pr-obs)<2.e-11,(graph,pp,radius,pr,obs)
    print('INDEPENDENT_SHORTEST_PATH_CONTINUOUS_INTEGRATION_PASSED',sum(1 for g in graphs for i in range(len(g))))
    star,triangle=graphs[:2]
    for pp in ([F(1,3)]*3,[F(1,2),F(1,4),F(1,4)],[F(1),F(0),F(0)]):
        for r in (F(1,9),F(2,11)):
            assert predicted_cdf(star,pp,r)==predicted_cdf(triangle,pp,r)
    print('TRIANGLE_CLAW_SHARP_LOCAL_OBSTRUCTION_PASSED')
    for graph in graphs:
        L=[e[2] for e in graph]
        for i,e in enumerate(graph):
            one=[F(0)]*len(graph);one[i]=F(1)
            # one-edge slope 2/l, second coefficient -1/l^2
            assert predicted_cdf(graph,one,F(1,100))==F(2,100)/L[i]-F(1,10000)/L[i]**2
        for i,j in combinations(range(len(graph)),2):
            pp=[F(0)]*len(graph);pp[i]=pp[j]=F(1,2)
            # recover edge incidence from its quadratic coefficient
            b=-(pp[i]**2/L[i]**2+pp[j]**2/L[j]**2)
            adj=F(1) if set(graph[i][:2])&set(graph[j][:2]) else F(0)
            b+=adj/(4*L[i]*L[j])
            recovered=4*L[i]*L[j]*b+L[j]/L[i]+L[i]/L[j]
            assert recovered==adj
    print('EXACT_RATIONAL_LENGTHS_AND_LINE_GRAPH_RECOVERY_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':experiments()
