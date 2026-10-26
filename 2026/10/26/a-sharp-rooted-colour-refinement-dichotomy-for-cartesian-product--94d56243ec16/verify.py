#!/usr/bin/env python3
"""Direct finite tests of rooted one-dimensional refinement on Cartesian SRG products.
Run: python3 verify.py
Standard library only. Root is the all-zero coordinate tuple.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import comb, factorial


def build_graph(vertices, edges):
    vs=list(vertices)
    ids={x:i for i,x in enumerate(vs)}
    adj=[set() for _ in vs]
    for u,v in edges:
        i,j=ids[u],ids[v]
        if i==j:raise AssertionError('loop')
        adj[i].add(j);adj[j].add(i)
    return [sorted(x) for x in adj]


def petersen():
    vs=list(combinations(range(5),2))
    return build_graph(vs,((a,b) for a,b in combinations(vs,2) if not(set(a)&set(b))))


def triangular5():
    vs=list(combinations(range(5),2))
    return build_graph(vs,((a,b) for a,b in combinations(vs,2) if set(a)&set(b)))


def c4():
    return build_graph(range(4),[(0,1),(1,2),(2,3),(3,0)])


def rook(q):
    vs=list(product(range(q),repeat=2))
    return build_graph(vs,((a,b) for a,b in combinations(vs,2) if a[0]==b[0] or a[1]==b[1]))


def shrikhande():
    vs=list(product(range(4),repeat=2))
    moves=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
    edges=[]
    for a in vs:
        for x,y in moves:
            edges.append((a,((a[0]+x)%4,(a[1]+y)%4)))
    return build_graph(vs,edges)


def clebsch():
    # Quotient the 5-dimensional cube by antipodal identification.
    vs=list(range(16))
    def rep(a):return min(a,a^31)
    return build_graph(vs,((a,rep(a^(1<<j))) for a in vs for j in range(5)))


def srg_parameters(adj):
    n=len(adj)
    sets=[set(x) for x in adj]
    degrees={len(x) for x in adj}
    assert len(degrees)==1
    k=degrees.pop(); lam=set();mu=set()
    for i,j in combinations(range(n),2):
        v=len(sets[i]&sets[j])
        (lam if j in sets[i] else mu).add(v)
    assert len(lam)==len(mu)==1
    return n,k,lam.pop(),mu.pop()


def product_adj(factors):
    sizes=[len(g) for g in factors]
    vertices=list(product(*(range(s) for s in sizes)))
    lookup={v:i for i,v in enumerate(vertices)}
    neighbors=[]
    for v in vertices:
        a=[]
        for i,graph in enumerate(factors):
            for t in graph[v[i]]:
                w=list(v);w[i]=t;a.append(lookup[tuple(w)])
        neighbors.append(a)
    return vertices,neighbors


def refine(adj,steps):
    colors=[1]*len(adj);colors[0]=0
    states=[tuple(colors)]
    for _ in range(steps):
        sig=[]
        for i,neighbors in enumerate(adj):
            counts=Counter(colors[j] for j in neighbors)
            sig.append((colors[i],tuple(sorted(counts.items()))))
        palette={s:i for i,s in enumerate(sorted(set(sig)))}
        colors=[palette[s] for s in sig]
        states.append(tuple(colors))
    return states


def equivalent_partition(p,q):
    a={};b={}
    for x,y in zip(p,q):
        if x in a and a[x]!=y:return False
        if y in b and b[y]!=x:return False
        a[x]=y;b[y]=x
    return True


def level_profile(v,distances):
    vals=[distances[i][v[i]] for i in range(len(v))]
    return vals.count(0),vals.count(1),vals.count(2)


def check(name,factors):
    params={srg_parameters(a) for a in factors}
    assert len(params)==1,(name,params)
    n,k,lam,mu=params.pop()
    d=len(factors)
    assert all(len(g)==n for g in factors)
    graph_vertices,adj=product_adj(factors)
    # The root is index zero; every test graph is indexed with a fixed root at zero.
    distances=[]
    for g in factors:
        dist=[-1]*len(g);dist[0]=0
        fringe=[0]
        for u in fringe:
            for w in g[u]:
                if dist[w]<0:dist[w]=dist[u]+1;fringe.append(w)
        assert max(dist)==2
        distances.append(dist)
    hist=[level_profile(v,distances) for v in graph_vertices]
    shell=[p[1]+2*p[2] for p in hist]
    regime=mu==2 and k==2*lam+2
    expected=shell if regime else hist
    states=refine(adj,2*d)
    classes=[len(set(x)) for x in states]
    assert classes[2*d-1]==classes[2*d],(name,classes)
    assert classes[2*d-2]<classes[2*d-1],(name,classes)
    assert equivalent_partition(states[2*d-1],expected),(name,'partition mismatch')
    expected_classes=2*d+1 if regime else comb(d+2,2)
    assert len(set(states[-1]))==expected_classes
    observed_multiplicities=sorted(Counter(states[-1]).values())
    if regime:
        assert k%2==0
        wanted=sorted(comb(2*d,s)*(k//2)**s for s in range(2*d+1))
    else:
        wanted=sorted(factorial(d)//(factorial(a)*factorial(b)*factorial(c))
                      * k**b *(n-k-1)**c
                      for a in range(d+1) for b in range(d+1-a) for c in [d-a-b])
    assert observed_multiplicities==wanted,(name,'size mismatch')
    return name,n,d,('Hamming-distance' if regime else 'coordinate-profile'),classes


def main():
    base={'C4':c4(),'Rook3':rook(3),'Rook4':rook(4),'Shrikhande':shrikhande(),
          'Petersen':petersen(),'Triangular5':triangular5(),'Clebsch':clebsch()}
    expected={'C4':(4,2,0,2),'Rook3':(9,4,1,2),'Rook4':(16,6,2,2),
              'Shrikhande':(16,6,2,2),'Petersen':(10,3,0,1),
              'Triangular5':(10,6,3,4),'Clebsch':(16,5,0,2)}
    for name,adj in base.items():
        assert srg_parameters(adj)==expected[name],(name,srg_parameters(adj))
    cases=[]
    for name,g in base.items():
        for d in (1,2,3):
            if len(g)**d<=1200:
                cases.append(check(name+'^'+str(d),[g]*d))
    cases.append(check('Shrikhande*Rook4',[base['Shrikhande'],base['Rook4']]))
    cases.append(check('Rook4*Shrikhande',[base['Rook4'],base['Shrikhande']]))
    for name,n,d,regime,seq in cases:
        print(f'{name:24} vertices={n**d:5} depth={2*d-1} regime={regime:19} count={seq}')
    print('CASES',len(cases),'ALL_TESTS_PASS')

if __name__=='__main__':main()
