"""Exact Fraction tests for the two-block signed bounded-confidence classification.
Only finite cases are computationally checked; all-size conclusions are analytical.
"""
from fractions import Fraction as Q
from itertools import combinations

def make_graph(m,kind):
    A=list(range(m));B=list(range(m,2*m)); signed={}
    if kind in ('internal_matching','all'):
        for part in (A,B):
            for i,j in combinations(part,2):signed[i,j]=1
    if kind=='internal_matching':
        for i in range(m):signed[i,m+i]=-1
    else:
        for i in A:
            for j in B:signed[i,j]=-1
    return signed

def step(graph,x,c):
    out=[]
    for i in range(len(x)):
        neighbors=[j if i==u else u for (u,j),sgn in graph.items() if i in (u,j) and abs(x[u]-x[j])<c]
        force=Q(0)
        for j in neighbors:
            edge=tuple(sorted((i,j))); sgn=graph[edge]
            d=x[j]-x[i]
            if sgn>0:force+=d
            else:
                assert d!=0
                force-= (Q(1) if d>0 else Q(-1))*(c-abs(d))
        out.append(x[i]+force/(len(neighbors)+1))
    return tuple(out)

def trial(m,kind,T=22):
    graph=make_graph(m,kind)
    c=Q(3,5); a=Q(1,4); b=Q(11,20); d=b-a
    x=(a,)*m+(b,)*m
    r=m if kind!='internal_matching' else 1
    p=m-1 if kind!='bipartite' else 0
    alpha=Q(r,p+r+1); eta=alpha*2
    assert (eta<1 if kind=='internal_matching' else eta==1 if kind=='all' else eta>1)
    for t in range(T):
        assert all(z==x[0] for z in x[:m]) and all(z==x[m] for z in x[m:])
        if eta<1:
            expected=a-alpha*(c-d)*(1-(1-eta)**t)/eta
            expected_b=b+alpha*(c-d)*(1-(1-eta)**t)/eta
            assert x[0]==expected and x[m]==expected_b
            assert x[m]-x[0]<c
        elif t>=1:
            assert x[0]==a-alpha*(c-d) and x[m]==b+alpha*(c-d)
            assert x[m]-x[0]>=c
        x=step(graph,x,c)
    return (m,kind,eta,x[m]-x[0])

if __name__=='__main__':
    count=0
    for m in range(2,12):
        for kind in ('internal_matching','all','bipartite'):
            trial(m,kind);count+=1
    print('PASS:',count,' exact rational signed-graph configurations, 22 synchronous steps each; all 3 phases and m=2..11')
