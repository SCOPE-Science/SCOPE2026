"""Independent, exact checks for edge-open-packing enumeration on forests.

Runs without third-party dependencies except NetworkX for its optional tree census.
"""
from itertools import combinations
from collections import Counter
from random import Random


def poly_add(*terms):
    n = max((len(a) for a in terms), default=0)
    ans = [0]*n
    for a in terms:
        for i, x in enumerate(a): ans[i] += x
    return trim(ans)


def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a


def poly_mul(a,b):
    if not a or not b or a==[0] or b==[0]: return [0]
    ans=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v: ans[i+j]+=u*v
    return trim(ans)


def shift(a):return [0]+a


def dp_poly(n, edges):
    graph=[[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v);graph[v].append(u)
    seen=set()
    result=[1]
    for root in range(n):
        if root in seen:continue
        stack=[(root,-1,False)]
        values={}
        while stack:
            u,parent,done=stack.pop()
            if not done:
                if u in seen: raise ValueError('Not a forest')
                seen.add(u)
                stack.append((u,parent,True))
                for v in graph[u]:
                    if v!=parent:
                        if v in seen:raise ValueError('Not a forest')
                        stack.append((v,u,False))
            else:
                A=[1]
                Bp=[1]
                B0=[0]
                Q0=[1]
                Q1=[0]
                Q2=[0]
                for v in graph[u]:
                    if v==parent:continue
                    a,bp,b0,c0,c1=values[v]
                    A=poly_mul(A,poly_add(a,b0,c0))
                    # Exactly one selected child; child can be a leaf or center.
                    B0=poly_add(poly_mul(B0,a),poly_mul(Bp,shift(poly_add(bp,c1))))
                    Bp=poly_mul(Bp,a)
                    # A center accepts only leaf children (never another center).
                    y=shift(bp)
                    nQ2=poly_add(poly_mul(Q2,poly_add(a,y)),poly_mul(Q1,y))
                    nQ1=poly_add(poly_mul(Q1,a),poly_mul(Q0,y))
                    Q0=poly_mul(Q0,a)
                    Q1,Q2=nQ1,nQ2
                values[u]=(A,Bp,B0,Q2,poly_add(Q1,Q2))
        a,bp,b0,c0,c1=values[root]
        result=poly_mul(result,poly_add(a,b0,c0))
    return result


def is_pack(edges, S):
    # Direct definition, with the third (witness) edge distinct from both selected edges.
    for i,j in combinations(S,2):
        ei=set(edges[i]); ej=set(edges[j])
        for k,ek in enumerate(edges):
            if k==i or k==j:continue
            a,b=ek
            if (a in ei and b in ej) or (b in ei and a in ej):
                return False
    return True


def brute_poly(n,edges):
    m=len(edges); out=[0]*(m+1)
    for mask in range(1<<m):
        S=[i for i in range(m) if mask>>i&1]
        if is_pack(edges,S):out[len(S)]+=1
    return trim(out)


def is_induced_star_forest(n,edges,S):
    endpoints=set()
    for i in S:endpoints.update(edges[i])
    induced=[i for i,(a,b) in enumerate(edges) if a in endpoints and b in endpoints]
    if set(induced)!=set(S):return False
    adj={u:set() for u in endpoints}
    for i in induced:
        a,b=edges[i]; adj[a].add(b);adj[b].add(a)
    if any(not adj[u] for u in endpoints):return False
    seen=set()
    for start in endpoints:
        if start in seen:continue
        todo=[start];component=[];seen.add(start)
        while todo:
            u=todo.pop();component.append(u)
            for v in adj[u]:
                if v not in seen:seen.add(v);todo.append(v)
        # A connected forest is a star iff it has at most one vertex of degree >=2.
        if sum(len(adj[u])>=2 for u in component)>1:return False
    return True


def prufer_tree(n, rng):
    if n<=1:return []
    import heapq
    seq=[rng.randrange(n) for _ in range(n-2)]
    deg=[1]*n
    for v in seq:deg[v]+=1
    heap=[v for v in range(n) if deg[v]==1];heapq.heapify(heap)
    e=[]
    for v in seq:
        u=heapq.heappop(heap);e.append((u,v));deg[u]-=1;deg[v]-=1
        if deg[v]==1:heapq.heappush(heap,v)
    e.append(tuple(heap))
    return e


def run():
    import networkx as nx
    counts={'unlabelled_trees':0,'direct_edge_subsets':0,'support_bijection_subsets':0,'random_forests':0,'direct_random_subsets':0,'star_tests':0}
    for n in range(1,12):
        trees=[nx.Graph()] if n==1 else nx.nonisomorphic_trees(n)
        for g in trees:
            if n==1: g.add_node(0)
            E=[tuple(sorted(e)) for e in g.edges()]
            expected=brute_poly(n,E)
            actual=dp_poly(n,E)
            assert actual==expected,(n,E,actual,expected)
            counts['unlabelled_trees']+=1
            counts['direct_edge_subsets']+=1<<len(E)
            for mask in range(1<<len(E)):
                sel=[i for i in range(len(E)) if mask>>i&1]
                assert is_pack(E,sel)==is_induced_star_forest(n,E,sel),(E,sel)
                counts['support_bijection_subsets']+=1
    rng=Random(20261009)
    for trial in range(600):
        n=rng.randint(1,16)
        E=prufer_tree(n,rng)
        E=[e for e in E if rng.randrange(4)>0]
        p=dp_poly(n,E)
        b=brute_poly(n,E)
        assert p==b,(n,E,p,b)
        counts['random_forests']+=1
        counts['direct_random_subsets']+=1<<len(E)
    for n in range(2,100):
        E=[(0,j) for j in range(1,n)]
        from math import comb
        assert dp_poly(n,E)==[comb(n-1,j) for j in range(n)]
        counts['star_tests']+=1
    print('ALL_CHECKS_PASSED')
    print('COUNTS',counts)
    for kind,n,E in [('P4',4,[(0,1),(1,2),(2,3)]),('P5',5,[(0,1),(1,2),(2,3),(3,4)]),('K1,4',5,[(0,j) for j in range(1,5)])]:
        print(kind,dp_poly(n,E))

if __name__=='__main__':run()
