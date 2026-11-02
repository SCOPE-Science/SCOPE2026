#!/usr/bin/env python3
"""Reproduce finite Moore-graph incidence and all-edge exact transport certificates.
Only Python standard library is required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import exp, log, sqrt


def build_graph(kind):
    if kind == 2:
        n=5
        edges={(i,(i+1)%5) for i in range(5)}
    elif kind == 3:
        vv=list(combinations(range(5),2));n=len(vv)
        edges={(i,j) for i in range(n) for j in range(i+1,n)
               if not (set(vv[i]) & set(vv[j]))}
    elif kind == 7:
        n=50;edges=set()
        # Five pentagons P_h, five pentagrams Q_i, and five cross edges per vertex.
        for h in range(5):
            for j in range(5):edges.add((5*h+j,5*h+(j+1)%5))
        for i in range(5):
            for j in range(5):edges.add((25+5*i+j,25+5*i+(j+2)%5))
        for h in range(5):
            for j in range(5):
                for i in range(5):
                    edges.add((5*h+j,25+5*i+(h*i+j)%5))
    else: raise ValueError(kind)
    adj=[set() for _ in range(n)]
    for a,b in edges:
        assert a != b
        adj[a].add(b);adj[b].add(a)
    return adj


def dists(adj,x):
    D={x:0}; q=[x]
    for a in q:
        for b in adj[a]:
            if b not in D: D[b]=D[a]+1;q.append(b)
    return D

count=0
for degree in (2,3,7):
    adj=build_graph(degree)
    n=len(adj)
    assert n==degree**2+1
    assert all(len(s)==degree for s in adj)
    distances=[dists(adj,x) for x in range(n)]
    assert all(len(D)==n and max(D.values())==2 for D in distances)
    # This entrywise equality proves the strongly regular polynomial A^2=(d-1)I-A+J.
    for x in range(n):
        for y in range(n):
            common=len(adj[x]&adj[y])
            expected=(degree if x==y else (0 if y in adj[x] else 1))
            assert common==expected
            count+=1
    # Verifies the graph-distance geometry used in the primal/dual W_1 certificate.
    for x in range(n):
        for y in adj[x]:
            if x>y: continue
            X=adj[x]-{y};Y=adj[y]-{x}
            assert len(X)==degree-1 and len(Y)==degree-1
            assert X.isdisjoint(Y)
            assert all(distances[x][b]==2 for b in Y)
            assert all(distances[a][y]==2 for a in X)
            assert all(distances[a][b]==2 for a in X for b in Y)
            # All 1-Lipschitz pairwise distances on support:
            vals={x:1,y:0,**{a:2 for a in X},**{b:0 for b in Y}}
            assert all(abs(vals[a]-vals[b])<=distances[a][b]
                       for a,b in combinations(vals,2))
            count+=1
    # Exact rational exponential values at a legitimate positive time for degrees 3,7.
    if degree in (3,7):
        if degree==3:
            u,v=F(1,4),F(1,32)  # t=log(2); eigenvalues 2,5
            root=3; r,s=1,-2
        else:
            u,v=F(1,2),F(1,4)   # t=log(2)/5; eigenvalues 5,10
            root=5;r,s=2,-3
        beta=(u-v)/root
        alpha=(r*v-s*u)/root
        assert alpha>=beta>=0
        target=alpha+(2*degree-3)*beta
        for x in range(n):
            for y in adj[x]:
                if x>y:continue
                X=adj[x]-{y};Y=adj[y]-{x}
                # Signed heat-row difference from P_t = alpha I + beta A + constant J.
                row=[alpha*((z==x)-(z==y))+
                     beta*((z in adj[x])-(z in adj[y])) for z in range(n)]
                assert all(row[z]>=0 for z in ({x}|X))
                assert all(row[z]<=0 for z in ({y}|Y))
                assert all(row[z]==0 for z in (set(range(n))-{x,y}-X-Y))
                f={x:F(1),y:F(0),**{a:F(2) for a in X},**{b:F(0) for b in Y}}
                dual=sum(row[z]*f[z] for z in f)
                primal=(alpha-beta)+2*(degree-1)*beta
                assert target==dual==primal
                count+=1
    d=float(degree);delta=sqrt(4*d-3)
    rr=(-1+delta)/2;ss=(-1-delta)/2
    lam1=d-rr;lam2=d-ss
    A=(2*d-3-ss)/delta;D=(2*d-3-rr)/delta
    assert A>1 and D>0 and abs(A-D-1)<1e-12
    for t in (0,.0001,.02,.05,.10,.25,.5,1,2):
        u=exp(-lam1*t);v=exp(-lam2*t)
        aa=(rr*v-ss*u)/delta;bb=(u-v)/delta
        c=aa+(2*d-3)*bb
        assert aa>=bb-1e-12 and bb>=-1e-12
        assert abs(c-(A*u-D*v))<1e-11
        h=(lam1*A*u-lam2*D*v)/c
        hprime=A*D*(lam2-lam1)**2*u*v/c**2
        assert hprime>0
        if t==0:assert abs(h-(3-d))<1e-10
        count+=1

# The realized seven-regular Moore graph has a strict, exactly rational transient peak.
assert F(14,5)*F(7,9)-F(9,5)*F(7,9)**2==F(49,45)
assert F(14,5)*F(5,9)-F(9,5)*F(5,9)**2==1
assert 0<log(F(9,7))/5<log(F(9,5))/5
print('CHECK_OK exact_combinatorial_and_transport_checks=',count,
      'Hoffman_Singleton_peak=49/45',
      'Petersen_profile=(5exp(-2t)-2exp(-5t))/3')

# For signed adjacency filters, the sharp universal norm has three distinct phases.
# The exact four-support Lipschitz constraints are verified independently for every
# edge on each realized finite Moore graph, with rational parameters.
signed_count=0
for degree in (2,3,7):
    graph=build_graph(degree)
    n=len(graph)
    distances=[dists(graph,z) for z in range(n)]
    parameters=((F(1),F(0)),(F(0),F(1)),(F(0),F(-1)),
                (F(1),F(1)),(F(1),F(-1)),(F(-1),F(1)),
                (F(10),F(-1)),(F(-10),F(1)),(F(-degree),F(1)),
                (F(degree),F(1)),(F(1,3),F(1,2)),(F(-1,3),F(1,2)))
    for alpha,beta in parameters:
        norm=max(abs(alpha-degree*beta),
                 abs(alpha+(2*degree-3)*beta),2*(degree-1)*abs(beta))
        # Sharpness certificates on each edge from the three extreme u values.
        for x in range(n):
            for y in graph[x]:
                if y<x:continue
                X=graph[x]-{y};Y=graph[y]-{x}
                results=[]
                for u,v,w in ((F(-1),F(0),F(-1)),
                              (F(0),F(1),F(-1)),
                              (F(1),F(2),F(0))):
                    potential={x:u,y:F(0),**{a:v for a in X},**{b:w for b in Y}}
                    assert all(abs(potential[a]-potential[b])<=distances[a][b]
                               for a,b in combinations(potential,2))
                    row=[alpha*((z==x)-(z==y))+
                         beta*((z in graph[x])-(z in graph[y]))
                         for z in range(n)]
                    results.append(sum(row[z]*potential[z] for z in potential))
                    signed_count+=1
                assert norm==max(results) if beta>=0 else norm==-min(results)
# The six bounding linear inequalities are all essential (nonempty open sectors).
for degree in (2,3,7):
    for alpha,beta,k in ((-F(degree),F(1),0),(F(1,2),F(1),2),
                         (F(degree),F(1),1)):
        vals=[abs(alpha-degree*beta),abs(alpha+(2*degree-3)*beta),
              2*(degree-1)*abs(beta)]
        assert vals[k]>max(vals[:k]+vals[k+1:])
print('SIGNED_OK exact_rational_potential_checks=',signed_count,
      'degrees=2,3,7 phases=3')
