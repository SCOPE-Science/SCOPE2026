"""Exact rational checks of stable-matching probability with uniform top ties.
Public-source data independent of preferences not embedded; Python stdlib only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb


def integral_edge_expansion(vertices, edges):
    verts = list(vertices); idx = {v:i for i,v in enumerate(verts)}
    ans = F(0)
    for mask in range(1<<len(edges)):
        deg=[0]*len(verts)
        for j,(u,v) in enumerate(edges):
            if mask>>j&1:
                deg[idx[u]]+=1;deg[idx[v]]+=1
        term=F((-1)**mask.bit_count())
        for d in deg: term/=d+1
        ans+=term
    return ans


def direct_local_order_enumeration(vertices,edges):
    verts=list(vertices); nbr={v:[] for v in verts}
    for u,v in edges: nbr[u].append(v);nbr[v].append(u)
    choices=[]
    for u in verts:
        d=len(nbr[u]); st=[]
        for bits in range(1<<d):
            subset=frozenset(nbr[u][j] for j in range(d) if bits>>j&1)
            st.append((subset,F(1,(d+1)*comb(d,len(subset)))))
        choices.append(st)
    total=F(0)
    for profile in product(*choices):
        if any(v in profile[verts.index(u)][0] and u in profile[verts.index(v)][0] for u,v in edges):
            continue
        w=F(1)
        for state,p in profile:w*=p
        total+=w
    return total


def forest_dp(vertices,edges):
    verts=list(vertices)
    nbr={v:[] for v in verts}
    for u,v in edges:nbr[u].append(v);nbr[v].append(u)
    visited=set()
    def node(u,parent):
        visited.add(u)
        q=[F(1)]
        for w in nbr[u]:
            if w==parent:continue
            assert w not in visited
            a,b=node(w,u)
            nq=[F(0)]*(len(q)+1)
            for j,v in enumerate(q):nq[j]+=a*v;nq[j+1]-=b*v
            q=nq
        A=sum((coef/F(j+1) for j,coef in enumerate(q)),F(0))
        B=sum((coef/F(j+2) for j,coef in enumerate(q)),F(0))
        return A,B
    z=F(1)
    for r in verts:
        if r not in visited:
            a,b=node(r,None);z*=a
    return z


def path_probability(n):
    p1,p2=F(1),F(3,4)
    if n==1:return p1
    for _ in range(3,n+1):p1,p2=p2,F(2,3)*p2+F(1,12)*p1
    return p2


def cycle_probability(n):
    c0,c1=F(2),F(2,3)
    for _ in range(2,n+1):c0,c1=c1,F(2,3)*c1+F(1,12)*c0
    return c1


def is_forest(vertices,edges):
    p={u:u for u in vertices}
    def root(u):
        while p[u]!=u:u=p[u]
        return u
    for u,v in edges:
        ru,rv=root(u),root(v)
        if ru==rv:return False
        p[ru]=rv
    return True


def verify():
    count=0; forest_cases=0; path_cases=0;cycle_cases=0
    for n in range(1,7):
        vertices=list(range(n))
        poss=list(combinations(vertices,2))
        for mask in range(1<<len(poss)):
            edges=[e for j,e in enumerate(poss) if mask>>j&1]
            if len(edges)>6:continue
            deg={u:0 for u in vertices}
            for u,v in edges:deg[u]+=1;deg[v]+=1
            if max(deg.values())>3:continue
            exact=integral_edge_expansion(vertices,edges)
            direct=direct_local_order_enumeration(vertices,edges)
            assert exact==direct,(vertices,edges,exact,direct)
            count+=1
            if is_forest(vertices,edges):
                assert forest_dp(vertices,edges)==exact,(vertices,edges)
                forest_cases+=1
    for n in range(1,22):
        vertices=list(range(n))
        path=[(i,i+1) for i in range(n-1)]
        a=path_probability(n)
        assert forest_dp(vertices,path)==a,(n,a)
        path_cases+=1
        if n<=9: assert a==integral_edge_expansion(vertices,path)
    for n in range(3,22):
        vertices=list(range(n))
        cycle=[(i,(i+1)%n) for i in range(n)]
        a=cycle_probability(n)
        if n<=9:assert a==integral_edge_expansion(vertices,cycle)
        cycle_cases+=1
    from itertools import permutations
    rank_vectors=[]
    for order in permutations(range(3)):
        rank_vectors.append(tuple(order.index(j) for j in range(3)))
    stable=0
    for ratings in product(rank_vectors, repeat=6):
        if all(not (ratings[i][j] < ratings[i][i] and ratings[3+j][i] < ratings[3+j][j])
               for i in range(3) for j in range(3) if i!=j):
            stable+=1
    assert F(stable,6**6)==cycle_probability(6)==F(5027,23328)
    print('VERIFY_OK', 'direct_profile_graphs=',count, 'forest_dp_graphs=',forest_cases,
          'paths=',path_cases,'cycles=',cycle_cases,
          'realizable_three_pair_stable_refinements=',stable, 'out_of=',6**6)

if __name__=='__main__':verify()
