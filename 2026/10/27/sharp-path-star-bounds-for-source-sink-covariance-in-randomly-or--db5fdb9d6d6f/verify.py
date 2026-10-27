"""Exact finite checks for source-sink covariance in random orientations of trees.
Requires Python 3 and networkx. No external data or network access.
"""
from fractions import Fraction as F
from itertools import product
import networkx as nx


def analytic(T):
    deg=dict(T.degree()); q={v:F(1,2**deg[v]) for v in T}
    return 2*sum((q[u]*q[v] for u,v in T.edges()),F(0))-sum((x*x for x in q.values()),F(0))


def enumerated(T):
    edges=list(T.edges())
    n=2**len(edges); sources=sinks=both=0
    for bits in product((0,1),repeat=len(edges)):
        indeg={v:0 for v in T};outdeg={v:0 for v in T}
        for (u,v),bit in zip(edges,bits):
            a,b=(u,v) if bit==0 else (v,u)
            outdeg[a]+=1;indeg[b]+=1
        a=sum(1 for v in T if indeg[v]==0)
        b=sum(1 for v in T if outdeg[v]==0)
        sources+=a;sinks+=b;both+=a*b
    return F(both,n)-F(sources*sinks,n*n)


def path_val(n):
    if n==2:return F(0)
    return F(n-4,16)


def star_val(n):
    if n==2:return F(0)
    k=n-1
    return F(k,2**k)-F(k,4)-F(1,4**k)


def find_arms(T,u):
    # Return (first branch vertex, terminal leaf) for each pendant-path arm.
    result=[]
    for v in T.neighbors(u):
        previous,current=u,v
        while T.degree(current)==2:
            following=next(w for w in T.neighbors(current) if w!=previous)
            previous,current=current,following
        if T.degree(current)==1:
            result.append((v,current))
    return result


def graft(T,u,v,t):
    R=T.copy();R.remove_edge(u,v);R.add_edge(t,v)
    assert nx.is_tree(R)
    return R


def main():
    total=0; grafts=0
    for n in range(2,13):
        trees=list(nx.nonisomorphic_trees(n))
        vals=[analytic(T) for T in trees]
        lo=min(vals);hi=max(vals)
        assert lo==star_val(n),(n,lo,star_val(n))
        assert hi==path_val(n),(n,hi,path_val(n))
        if n>=4:
            assert sum(v==lo for v in vals)==1,(n,'star nonunique')
            assert sum(v==hi for v in vals)==1,(n,'path nonunique')
        for T in trees:
            a=analytic(T)
            if n<=9:
                assert a==enumerated(T),(n,list(T.edges()),a,enumerated(T))
                total+=1
            for u in T:
                if T.degree(u)<3:continue
                arms=find_arms(T,u)
                for i,(v,leaf) in enumerate(arms):
                    for j,(vv,t) in enumerate(arms):
                        if i==j: continue
                        delta=analytic(graft(T,u,v,t))-a
                        assert delta>0,(n,T.edges(),u,v,t,delta)
                        assert delta>=F(5,64),(n,delta)
                        grafts+=1
        print('TREE_ORDER_PASS',n,'nonisomorphic',len(trees),'min',lo,'max',hi)
    print('EXACT_ORIENTATION_COUNTS_PASS',total)
    print('STRICT_PENDANT_PATH_TRANSFERS_PASS',grafts)
    print('VERIFY_OK')
if __name__=='__main__': main()
