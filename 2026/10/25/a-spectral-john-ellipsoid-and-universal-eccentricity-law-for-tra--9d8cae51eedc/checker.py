"""Numerical consistency checks for spectral John ellipsoids of regular bipartite stable-set polytopes.
Requires Python 3 and NumPy. Analytical proof is provided separately.
"""
import math
import numpy as np


def graph_edges(kind, m):
    if kind == 'complete':
        return 2*m, [(i, m+j) for i in range(m) for j in range(m)], m
    if kind == 'crown':
        return 2*m, [(i, m+j) for i in range(m) for j in range(m) if i != j], m-1
    if kind == 'cube':
        return 2**m, [(i, i ^ (1 << j)) for i in range(2**m) for j in range(m) if not (i & (1 << j))], m
    if kind == 'cycle':
        return m, [(i, (i+1)%m) for i in range(m)], 2
    raise ValueError(kind)


def solve_parameter(eigenvalues, degree, number_vertices):
    def f(r):
        return degree*r*(r+2)*np.mean(1/(degree*r+eigenvalues))/2-1
    lo, hi = 1., math.sqrt(2.)
    assert f(lo) <= 1e-10 and f(hi)>0
    for _ in range(75):
        mid = (lo+hi)/2
        if f(mid)>0: hi = mid
        else: lo = mid
    return (lo+hi)/2


def check_graph(kind,m):
    n, edges, degree = graph_edges(kind,m)
    assert n*degree == 2*len(edges)
    incidence = np.zeros((n,len(edges)))
    for j,(u,v) in enumerate(edges): incidence[u,j]=incidence[v,j]=1
    H = incidence @ incidence.T
    assert np.max(abs(H.sum(axis=1)-2*degree)) < 1e-10
    vals = np.linalg.eigvalsh(H)
    assert vals.min() > -1e-9
    r=solve_parameter(vals,degree,n)
    a=1/(r+2); b=r*a
    k=2*(r+2)/(degree*r)
    precision=k*(degree*r*np.eye(n)+H)
    Q=np.linalg.inv(precision)
    contact_errors=[abs(Q[i,i]-a*a) for i in range(n)]
    for u,v in edges:
        z=np.zeros(n);z[u]=z[v]=1
        contact_errors.append(abs(z@Q@z-b*b))
    assert max(contact_errors)<3e-12,(kind,m,'contact',max(contact_errors))
    weight_vertex=2/(r+2)
    weight_edge=2*r/(degree*(r+2))
    moment1=np.full(n,-weight_vertex/a)
    moment2=(weight_vertex/a**2)*np.eye(n)
    for u,v in edges:
        z=np.zeros(n);z[u]=z[v]=1
        moment1+=weight_edge/b*z
        moment2+=weight_edge/b**2*np.outer(z,z)
    assert np.max(abs(moment1))<2e-12
    assert np.max(abs(moment2-precision))<4e-12
    assert abs(n*weight_vertex+len(edges)*weight_edge-n)<1e-11
    eigQ=np.linalg.eigvalsh(Q)
    assert abs(eigQ.max()/eigQ.min()-(r+2)/r)<2e-10
    assert 1-1e-11<=r<math.sqrt(2)
    return {'graph':kind,'parameter':m,'dimension':n,'degree':degree,
            'r':round(r,12),'max_tangency_error':max(contact_errors)}


def main():
    rows=[]
    for kind,params in [('complete',[3,4,8,20]),('crown',[4,5,7]),
                        ('cube',[3,4,5]),('cycle',[6,8,10])]:
        for m in params:rows.append(check_graph(kind,m))
    print('VERIFY_OK graphs=',len(rows),'facet_norms=',sum(r['dimension']+r['dimension']*r['degree']//2 for r in rows))
    for r in rows:print(r)

if __name__=='__main__': main()
