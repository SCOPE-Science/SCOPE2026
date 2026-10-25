#!/usr/bin/env python3
"""Exact-rational verification of projection norms for a clique-augmented biclique.

Requires Python 3.9+ standard library only. Run: python check_clique_bipartite.py
"""
from fractions import Fraction as F


def build_graph(m, n, k):
    assert m >= 4 and n >= 2 and 3 <= k < m
    e = [(i, j) for i in range(k) for j in range(i+1, k)]
    e += [(i, m+j) for i in range(m) for j in range(n)]
    return e


def predicted(m, n, k):
    p = m-k
    q0 = F(3)-F(2,m)-F(2,n)+F(2,m*n)
    p0 = F(4*(m-1)*(n-1),m*n)
    if p <= n:
        dq = -F((k-1)*(n-2),n*(n+k))
        dp = -F((k-1)*(n-4),n*(n+k))
    else:
        dq = F((k-1)*(n*p-k*(n-2)-2*n*(n-1)), n*(n+k)*m)
        dp = F((k-1)*((n+2)*p-k*(n-4)-2*n*(n-1)),n*(n+k)*m)
    return q0+max(F(0),dq),p0+max(F(0),dp),q0,p0,dq,dp


def explicit_potential(m, n, k, kind):
    v = [F(0)]*(m+n)
    if kind == 'CC':
        v[0],v[1] = F(1,n+k),-F(1,n+k)
        e = (0,1)
    elif kind == 'CB':
        v[0] = F(n+1,n*(n+k))
        for j in range(1,k):
            v[j] = F(1,n*(n+k))
        v[m] = -F(n-1,n*m)
        for j in range(m+1,m+n):
            v[j] = F(1,n*m)
        e=(0,m)
    elif kind == 'UB':
        v[k],v[m] = F(1,n),-F(n-1,n*m)
        for j in range(m+1,m+n):
            v[j] = F(1,n*m)
        e=(k,m)
    else:
        raise ValueError(kind)
    return e,v


def volt_drop_column(edges, pot, distinguished):
    q = [abs(pot[u]-pot[v]) for u,v in edges]
    r = abs(pot[distinguished[0]]-pot[distinguished[1]])
    return sum(q), F(1)+sum(q)-2*r


def verify_equation(m,n,k,e,pot,edges):
    net=[F(0)]*(m+n)
    for u,v in edges:
        d=pot[u]-pot[v]
        net[u]+=d;net[v]-=d
    assert all(net[i]==(F(int(i==e[0])-int(i==e[1]))) for i in range(m+n)),(m,n,k,e,net)


def inverse_rational(a):
    n=len(a)
    aug=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[pivot]=aug[pivot],aug[j]
        f=aug[j][j]
        aug[j]=[x/f for x in aug[j]]
        for i in range(n):
            if i!=j and aug[i][j]:
                f=aug[i][j]
                aug[i]=[x-f*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def grounded_inverse(m,n,k,edges):
    v=m+n-1
    a=[[0]*v for _ in range(v)]
    for x,y in edges:
        if x<v:a[x][x]+=1
        if y<v:a[y][y]+=1
        if x<v and y<v:
            a[x][y]-=1;a[y][x]-=1
    return inverse_rational(a)


def norm_from_inverse(m,n,k,edges,inv):
    v=m+n-1
    qmax=pmax=F(0)
    for x,y in edges:
        potential=[(inv[i][x] if x<v else F(0))-(inv[i][y] if y<v else F(0)) for i in range(v)]+[F(0)]
        cq,cp=volt_drop_column(edges,potential,(x,y))
        qmax=max(qmax,cq);pmax=max(pmax,cp)
    return qmax,pmax


def main():
    orbit_count=0;orbit_edge_count=0
    full_graph_count=0;full_edge_count=0
    for m in range(4,20):
        for n in range(2,16):
            for k in range(3,m):
                edges=build_graph(m,n,k)
                pred=predicted(m,n,k)
                orbit=[]
                for kind in ('CC','CB','UB'):
                    e,pot=explicit_potential(m,n,k,kind)
                    verify_equation(m,n,k,e,pot,edges)
                    c=volt_drop_column(edges,pot,e)
                    orbit.append(c)
                    orbit_count+=1
                    orbit_edge_count+=len(edges)
                assert max(q for q,p in orbit)==pred[0],(m,n,k,'Q',orbit,pred)
                assert max(p for q,p in orbit)==pred[1],(m,n,k,'P',orbit,pred)
                assert pred[0]<4 and pred[1]<5
                # Independent grounded-matrix inversion across representative dimensions,
                # including both exact phase boundaries and opposite-direction regimes.
                if (m,n,k) in {
                    (4,2,3),(4,3,3),(4,4,3),(4,5,3),(4,9,3),
                    (5,2,3),(5,4,3),(5,7,3),(6,3,3),(6,4,4),
                    (7,2,5),(7,5,4),(8,3,5),(8,6,3),(9,5,3),
                    (10,5,3),(11,5,3),(12,5,3),(13,5,3),
                    (10,7,6),(12,9,6),(14,3,9),(15,3,5)
                }:
                    inv=grounded_inverse(m,n,k,edges)
                    ans=norm_from_inverse(m,n,k,edges,inv)
                    assert ans[:2]==pred[:2],(m,n,k,'grounded',ans,pred)
                    full_graph_count+=1
                    full_edge_count+=len(edges)
    for t in (20,40,100):
        n=t;k=t*t;p=t**4;m=k+p
        out=predicted(m,n,k)
        assert out[0]<4 and out[1]<5
        assert out[0]>F(4)-F(10,t) and out[1]>F(5)-F(10,t)
    print('CLIQUE_AUGMENTED_BICLIQUE_EXACT_OK',
          'orbit_cases='+str(orbit_count),
          'orbit_edges='+str(orbit_edge_count),
          'grounded_graphs='+str(full_graph_count),
          'grounded_columns='+str(full_edge_count),
          'sharp_limit_samples=3')

if __name__=='__main__':main()
