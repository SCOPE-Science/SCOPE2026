"""Finite numerical checks for the bounded-degree cosmological-polytope width law.

Uses only standard Euclidean coordinates and numpy. Finite checks corroborate, not prove,
the limiting theorem.
"""
import math
import numpy as np


def polytope_vertices(n, edges):
    out = []
    m = len(edges)
    for k, (u, v) in enumerate(edges):
        p = np.zeros(n+m)
        p[u] = p[v] = 1
        p[n+k] = -1
        out.append(p)
        p = np.zeros(n+m)
        p[n+k] = p[u] = 1
        p[v] = -1
        out.append(p)
        p = np.zeros(n+m)
        p[n+k] = p[v] = 1
        p[u] = -1
        out.append(p)
    return np.array(out)


def covariance_properties(n, edges):
    vertices = polytope_vertices(n, edges)
    assert np.all(vertices.sum(axis=1) == 1)
    G = vertices @ vertices.T
    assert np.all(np.diag(G) == 3)
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            e1, e2 = i//3, j//3
            if e1 == e2:
                assert G[i,j] == -1
            elif set(edges[e1]).isdisjoint(set(edges[e2])):
                assert G[i,j] == 0
            else:
                assert abs(G[i,j]) == 1
    wedge_count = sum((sum(v in e for e in edges) * (sum(v in e for e in edges)-1))//2 for v in range(n))
    positive, negative = 0, 0
    for ea, (u,v) in enumerate(edges):
        for eb in range(ea+1,len(edges)):
            if set(edges[ea]).intersection(edges[eb]):
                block = G[3*ea:3*ea+3, 3*eb:3*eb+3]
                assert np.count_nonzero(block == 1) == 5
                assert np.count_nonzero(block == -1) == 4
                positive += 5
                negative += 4
    assert positive == 5*wedge_count and negative == 4*wedge_count
    return len(vertices)


def support_width_check(n, edges, rng, samples):
    vertices = polytope_vertices(n, edges)
    D = n+len(edges)
    for _ in range(samples):
        g = rng.standard_normal(D)
        projected = g - g.mean()
        u = projected / np.linalg.norm(projected)
        direct = np.ptp(vertices@u)
        scores = []
        for k, (a,b) in enumerate(edges):
            scores.extend((g[a]+g[b]-g[n+k],
                           g[a]-g[b]+g[n+k],
                           -g[a]+g[b]+g[n+k]))
        formula = (max(scores)-min(scores))/np.linalg.norm(projected)
        assert abs(direct-formula) < 1e-10


def gumbel_mean_sim(m, batches, batchsize, rng, graph):
    n = m+1 if graph == 'path' else m if graph == 'cycle' else (1+math.isqrt(1+8*m))//2
    if graph == 'path':
        edges = [(i,i+1) for i in range(m)]
    elif graph == 'cycle':
        edges = [(i,(i+1)%m) for i in range(m)]
    elif graph == 'complete':
        edges = [(i,j) for i in range(n) for j in range(i+1,n)]
        assert len(edges)==m
    else:
        raise ValueError
    N=3*m
    L=math.log(N)
    a=math.sqrt(3)*(math.sqrt(2*L)-(math.log(L)+math.log(4*math.pi))/(2*math.sqrt(2*L)))
    b=math.sqrt(3)/math.sqrt(2*L)
    dim=n+m-1
    z=[]
    for _ in range(batches):
        x=rng.standard_normal((batchsize,n))
        y=rng.standard_normal((batchsize,m))
        p=np.empty((batchsize,m,3))
        for k,(i,j) in enumerate(edges):
            p[:,k,0] = x[:,i]+x[:,j]-y[:,k]
            p[:,k,1] = x[:,i]-x[:,j]+y[:,k]
            p[:,k,2] = -x[:,i]+x[:,j]+y[:,k]
        p=p.reshape((batchsize,3*m))
        rad=np.sqrt((x*x).sum(axis=1)+(y*y).sum(axis=1)-((x.sum(axis=1)+y.sum(axis=1))**2)/(n+m))
        z.append(((np.ptp(p,axis=1)*math.sqrt(dim)/rad)-2*a)/b)
    z=np.concatenate(z)
    return float(z.mean()),float(z.var()),len(z)


def main():
    rng=np.random.default_rng(2718281828)
    families = [
       (5,[(i,i+1) for i in range(4)]),
       (7,[(i,(i+1)%7) for i in range(7)]),
       (8,[(i,(i+1)%8) for i in range(8)]),
       (9,[(i-1,i) for i in range(1,9)]),
       (8,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(6,7)]),
       (6,[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(0,3)]),
       (9,[(i,j) for i in range(9) for j in range(i+1,9)])
    ]
    total=0
    for n,edges in families:
        total+=covariance_properties(n,edges)
        support_width_check(n,edges,rng,120)
    print('finite_vertices_checked',total)
    print('finite_support_width_trials',120*len(families))
    for graph in ['path','cycle']:
        for m in [160,600]:
            mean,var,count=gumbel_mean_sim(m,12,200,rng,graph)
            print('limit_diagnostic',graph,m,count,round(mean,5),round(var,5))
    for n in [16,35]:
        m=n*(n-1)//2
        mean,var,count=gumbel_mean_sim(m,12,100,rng,'complete')
        print('limit_diagnostic','complete',m,count,round(mean,5),round(var,5))
    print('reference_gumbel_sum_mean',2*0.5772156649015329)
    print('reference_gumbel_sum_variance',math.pi**2/3)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
