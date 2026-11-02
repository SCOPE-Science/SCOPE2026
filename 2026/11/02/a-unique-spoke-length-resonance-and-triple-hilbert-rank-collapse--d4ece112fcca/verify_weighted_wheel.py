"""Standalone independent checks for weighted wheel shortest-path negative type.
Uses NetworkX shortest paths and exact SymPy arithmetic; never assumes the
closed distance formula when constructing the graph metric.
"""
import math
from fractions import Fraction
import numpy as np
import networkx as nx
import sympy as sp
from scipy.optimize import brentq


def shortest_metric(n, t):
    graph=nx.Graph()
    graph.add_nodes_from(range(n+1))
    for j in range(n):
        graph.add_edge(j,(j+1)%n,weight=sp.Rational(1))
        graph.add_edge(n,j,weight=t)
    dist=dict(nx.all_pairs_dijkstra_path_length(graph,weight='weight'))
    return sp.Matrix([[sp.Rational(str(dist[i][j])) for j in range(n+1)] for i in range(n+1)])


def predicted_radial(n,p,t):
    b=(2*t)**p
    return 2+(n-3)*b-2*n*(t**p)


def bcrit(n):
    c=1 if n%2==0 else math.cos(math.pi/n)
    return 2*c/(2*c-1)


def thresholds(n,t):
    bc=bcrit(n)
    pf=float('inf') if t==0.5 else math.log(bc)/math.log(2*t)
    pr=brentq(lambda p: predicted_radial(n,p,t),0.0,40.0,xtol=2e-14)
    return pr,pf,min(pr,pf)


def transition(n):
    bc=bcrit(n)
    s=(2+(n-3)*bc)/(2*n)
    p=math.log2(bc/s)
    t=s**(1/p)
    return t,p


def gram_eigenvalues(D,p):
    a=np.array(D,dtype=float)**p
    count=a.shape[0]
    Z=np.concatenate([np.eye(count-1),-np.ones((1,count-1))],axis=0)
    g=-0.5*Z.T@a@Z
    return np.linalg.eigvalsh((g+g.T)/2)

exact_count=0
for n in range(4,14):
    for t in (sp.Rational(1,2),sp.Rational(2,3),sp.Rational(3,4),sp.Rational(1)):
        D=shortest_metric(n,t)
        assert all(D[i,j]==(sp.Rational(0) if i==j else (t if i==n or j==n else (sp.Rational(1) if ((i-j)%n in (1,n-1)) else 2*t))) for i in range(n+1) for j in range(n+1))
        for power in (1,2,3):
            P=D.applyfunc(lambda x:x**power)
            b=(2*t)**power
            for a in range(5):
                Y=sp.Matrix([((i+2*a+1)**2+3*i*a)%11-5 for i in range(n)])
                S=sum(Y)
                Z=Y.col_join(sp.Matrix([-S]))
                quad=(Z.T*P*Z)[0]
                y0=Y-sp.ones(n,1)*S/n
                # Fourier-free decomposition: rim modes from adjacent inner product
                ram=(sp.Rational(2)+(n-3)*b-2*n*t**power)*S*S/n
                fluct= -b*y0.dot(y0)+2*(1-b)*sum(y0[i]*y0[(i+1)%n] for i in range(n))
                assert sp.simplify(quad-ram-fluct)==0,(n,t,power,a,quad,ram,fluct)
                exact_count+=1
print('EXACT_WEIGHTED_SHORTEST_PATH_DECOMPOSITION_OK',exact_count)

transition_cases=0
for n in range(4,40):
    tc, pc=transition(n)
    assert .5 < tc < 1 and pc>1
    pr,pf,ps=thresholds(n,tc)
    assert abs(pr-pc)<1e-10 and abs(pf-pc)<1e-10
    for t in [0.5,(.5+tc)/2,tc,(tc+1)/2,1.0]:
        rr,ff,pp=thresholds(n,t)
        if t<tc-1e-9: assert rr<ff
        if t>tc+1e-9: assert ff<rr
        if t not in [tc]:
            e=gram_eigenvalues(shortest_metric(n,sp.Rational(str(t))),pp-1e-4)
            assert min(e)>-1e-8,(n,t,pp,min(e))
            f=gram_eigenvalues(shortest_metric(n,sp.Rational(str(t))),pp+1e-4)
            assert min(f)<-1e-9,(n,t,pp,min(f))
    D=shortest_metric(n,sp.Rational(str(tc)))
    eig=gram_eigenvalues(D,pc)
    expected=2 if n%2==0 else 3
    assert np.count_nonzero(abs(eig)<1e-8)==expected,(n,tc,pc,eig[:5])
    assert np.count_nonzero(eig<-1e-8)==0
    transition_cases+=1
print('CRITICAL_TRANSITIONS_OK',transition_cases,'n=4..39','nullities even=2 odd=3')
for n in (4,5,6,7,10,11,20,21):
    t,p=transition(n)
    print('TRANSITION',n,'t=',round(t,12),'p=',round(p,12))
print('ALL_WEIGHTED_WHEEL_CHECKS_OK')
