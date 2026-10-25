"""Reproducible finite diagnostics for the third angular-width moment theorem.
These tests support, but do not replace, the all-graph proof.
"""
import math
from itertools import combinations
import networkx as nx
import numpy as np

PI = math.pi
A = math.sqrt(2/PI)
B = math.sqrt(3)/PI + 1/6
C = B-A*A
AL = (2/PI)**1.5
F_PATH = AL*(1/math.sqrt(2)+math.asin(1/math.sqrt(3))-math.asin(1/3)/4)
F_STAR = AL*(1/math.sqrt(2)+9*math.asin(1/3)/4)
F_TRI = 3*A/4
K1 = -A+2*A**3
K2 = A*(.25-2*C)
KP = F_PATH-2*A*B+A**3
KS = F_STAR-3*A*B+2*A**3
KT = F_TRI-3*A*B+2*A**3
DELTA = KT-3*KP

def third_abs(R):
    det = max(0.,float(np.linalg.det(R)))
    out = math.sqrt(det)
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
        p=float(R[i,j]);q=float(R[i,k]);r=float(R[j,k]);
        par = (p-q*r)/math.sqrt((1-q*q)*(1-r*r))
        out += (p+q*r)*math.asin(max(-1.,min(1.,par)))
    return AL*out

def triplet_cumulant(R):
    return third_abs(R)-A*sum((math.sqrt(1-R[i,j]**2)+R[i,j]*math.asin(R[i,j]))*2/PI for i,j in [(0,1),(0,2),(1,2)]) +2*A**3

def graph_counts(G):
    d=dict(G.degree()); m=G.number_of_edges()
    wedge=sum(v*(v-1)//2 for v in d.values())
    star=sum(v*(v-1)*(v-2)//6 for v in d.values())
    tri=sum(nx.triangles(G).values())//3
    path=sum((d[u]-1)*(d[v]-1) for u,v in G.edges())-3*tri
    return m,wedge,path,star,tri

def graph_formula(G):
    m,w,p,s,t=graph_counts(G)
    return m*K1+6*w*K2+6*(p*KP+s*KS+t*KT)

def brute_formula(G):
    e=list(G.edges());m=len(e)
    D=np.zeros((m,m))
    for i,(u,v) in enumerate(e):
        for j,(a,b) in enumerate(e):
            D[i,j] = ((u==a)-(u==b)-(v==a)+(v==b))/2
    ans=m*K1
    for i,j in combinations(range(m),2):
        r=D[i,j]
        b=(math.sqrt(1-r*r)+r*math.asin(r))*2/PI
        v=A*(r*r-2*(b-A*A))
        ans +=6*v
    for i,j,k in combinations(range(m),3):
        R=D[np.ix_([i,j,k],[i,j,k])]
        ans+=6*triplet_cumulant(R)
    return ans

def run():
    assert DELTA<0 and KP<0 and KS>0 and KT<0
    assert 55/14+97/56-2-21*70/(4*99)<0  # analytic negativity bound
    checks=0
    for G in nx.graph_atlas_g():
        if 3<=G.number_of_nodes()<=6 and nx.is_connected(G):
            got=brute_formula(G); pred=graph_formula(G)
            assert abs(got-pred)<1e-8, (G.number_of_nodes(),list(G.edges()),got,pred)
            checks+=1
    A1=nx.complete_bipartite_graph(3,3)
    A2=nx.circular_ladder_graph(3)  # triangular prism
    assert graph_counts(A1)[-1]==0 and graph_counts(A2)[-1]==2
    assert A1.number_of_edges()==A2.number_of_edges()==9
    assert graph_counts(A1)[:2]==graph_counts(A2)[:2]
    assert abs((graph_formula(A2)-graph_formula(A1))-12*DELTA)<1e-12
    # Direct uncentered Gaussian simulation is an independent geometric check.
    rng=np.random.default_rng(97391)
    nrep=500000
    g=rng.standard_normal((nrep,6))
    def calc(H):
        edges=np.array(list(H.edges()),dtype=int)
        values=np.abs(g[:,edges[:,0]]-g[:,edges[:,1]]).sum(axis=1)/math.sqrt(2)
        mu=values.mean()
        return np.mean((values-mu)**3)
    observed=calc(A2)-calc(A1)
    assert abs(observed-12*DELTA)<0.12,(observed,12*DELTA)
    print('VERIFY_OK connected_graphs=',checks,'delta=',round(DELTA,12),
          'prism_minus_K33_exact=',round(12*DELTA,12),
          'simulation=',round(float(observed),7))

if __name__=='__main__':run()
