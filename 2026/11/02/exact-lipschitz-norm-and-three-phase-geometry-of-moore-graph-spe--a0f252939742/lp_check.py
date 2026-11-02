#!/usr/bin/env python3
"""Optional full Lipschitz linear-program cross-check (requires NumPy and SciPy)."""
import math
import numpy as np
from scipy.optimize import linprog
from checker import build_graph

count_heat=0
count_signed=0
for degree in (2,3,7):
    adj=build_graph(degree)
    n=len(adj)
    adjacency=np.zeros((n,n),dtype=float)
    edges=[]
    for x in range(n):
        for y in adj[x]:
            adjacency[x,y]=1
            if x<y:edges.append((x,y))
    constraints=[]
    for x,y in edges:
        line=np.zeros(n)
        line[x]=1
        line[y]=-1
        constraints.extend((line,-line))
    constraints=np.asarray(constraints)
    gap=math.sqrt(4*degree-3)
    high=(-1+gap)/2
    low=(-1-gap)/2
    lamb1=degree-high
    lamb2=degree-low
    sign_params=[(-9.,1.),(-degree+1.,1.),(0.,1.),(.5,1.),
                 (degree,1.),(1.,-1.),(0.,-1.),(-1.,-1.)]
    def verify(alpha,beta,expected,pairs):
        global count_signed
        for x,y in pairs:
            difference=alpha*(np.eye(n)[x]-np.eye(n)[y])+beta*(adjacency[x]-adjacency[y])
            solution=linprog(-difference,A_ub=constraints,b_ub=np.ones(len(constraints)),
                             bounds=[(None,None)]*n,method='highs')
            assert solution.success,solution.message
            assert abs(-solution.fun-expected)<1e-8,(degree,alpha,beta,expected,-solution.fun)
            count_signed+=1
    pairs=[(x,y) for x,y in edges if x<min(n,4)][:12]
    for alpha,beta in sign_params:
        expected=max(abs(alpha-degree*beta),abs(alpha+(2*degree-3)*beta),
                     2*(degree-1)*abs(beta))
        verify(alpha,beta,expected,pairs)
    for t in (.001,.05,.2,1.0):
        u=math.exp(-lamb1*t)
        v=math.exp(-lamb2*t)
        alpha=(high*v-low*u)/gap
        beta=(u-v)/gap
        expected=alpha+(2*degree-3)*beta
        verify(alpha,beta,expected,pairs[:8])
        count_heat+=len(pairs[:8])
print('LP_CROSSCHECK_OK signed_and_heat_edge_cases=',count_signed,'heat_subset=',count_heat)
