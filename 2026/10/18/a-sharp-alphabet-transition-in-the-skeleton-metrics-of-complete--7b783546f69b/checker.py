"""Reproduce exact 1-skeleton and metric counts for layered path polytopes.

Uses three logically distinct methods: face-support path recombination, direct
linear-programming adjacency on small instances, and breadth-first distances.
Run: python layered_path_checker.py
"""
from itertools import product, combinations
from collections import Counter, deque
from math import comb, prod
import numpy as np


def runs_neq(a, b):
    r = 0
    flag = False
    for x, y in zip(a, b):
        if x != y:
            if not flag:
                r += 1
            flag = True
        else:
            flag = False
    return r


def incidence(a):
    k = len(a)
    # Arc keys are (layer, u, v); one endpoint is the single source/sink.
    nodes = (0,) + tuple(x + 1 for x in a) + (0,)
    return frozenset((i, nodes[i], nodes[i + 1]) for i in range(k + 1))


def alternate_paths(a, b):
    allowed = incidence(a) | incidence(b)
    alph = [sorted({a[i], b[i]}) for i in range(len(a))]
    return [z for z in product(*alph) if incidence(z) <= allowed]


def independent_LP_check(q, k):
    import numpy as np
    from scipy.optimize import linprog
    vs = list(product(range(q), repeat=k))
    arcs = sorted(set().union(*(incidence(v) for v in vs)))
    j = {e: i for i, e in enumerate(arcs)}
    a = np.zeros((len(arcs), len(vs)))
    for h,v in enumerate(vs):
        for e in incidence(v):
            a[j[e],h] = 1
    for s,t in combinations(range(len(vs)),2):
        others=[j for j in range(len(vs)) if j not in (s,t)]
        target=(a[:,s]+a[:,t])/2
        mat=np.concatenate([a[:,others], np.ones((1,len(others)))])
        b=np.append(target,1)
        res=linprog(np.zeros(len(others)),A_eq=mat,b_eq=b,bounds=(0,None),method='highs')
        actual = not res.success
        expected = runs_neq(vs[s],vs[t]) == 1
        assert actual==expected, ('LP adjacency',q,k,vs[s],vs[t],expected,actual,res.message)
    return len(vs)*(len(vs)-1)//2


def exhaustive(q, k):
    vs=list(product(range(q),repeat=k)); n=len(vs)
    edge=[[] for _ in vs]; n_edges=0
    for i,j in combinations(range(n),2):
        r=runs_neq(vs[i],vs[j]);alts=alternate_paths(vs[i],vs[j]); assert len(alts)==2**r,(q,k,vs[i],vs[j],r,alts)
        if len(alts)==2:
            edge[i].append(j);edge[j].append(i);n_edges+=1
    predicted_degree=sum((k-j+1)*(q-1)**j for j in range(1,k+1))
    assert all(len(x)==predicted_degree for x in edge)
    assert n_edges==n*predicted_degree//2
    profiles=[]
    for root in range(n):
        ds=[-1]*n;ds[root]=0;dq=deque([root]);
        while dq:
            u=dq.popleft()
            for v in edge[u]:
                if ds[v]<0:ds[v]=ds[u]+1;dq.append(v)
        assert all(d>=0 for d in ds)
        if q==2:
            assert all(d==runs_neq(vs[root],vs[v]) for v,d in enumerate(ds))
            distribution={r:comb(k+1,2*r) for r in range((k+1)//2+1)}
        else:
            assert all(d==(0 if v==root else (1 if runs_neq(vs[root],vs[v])==1 else 2)) for v,d in enumerate(ds))
            distribution={0:1,1:predicted_degree,2:n-1-predicted_degree}
        assert Counter(ds)==Counter({r:nr for r,nr in distribution.items() if nr})
        profiles.append(Counter(ds))
    w = n*sum(r*cnt for r,cnt in profiles[0].items())//2
    if q==2:
        expected_w=(k+1)*2**(2*k-3)
    else:
        expected_w=n*(n-1)-n*predicted_degree//2
    assert w==expected_w,(q,k,w,expected_w)
    return (q,k,n,n_edges,max(profiles[0]),w)



def spectral_check(profile):
    """Direct dense adjacency eigenvalues versus tensor-character prediction."""
    vs = list(product(*(range(q) for q in profile)))
    n = len(vs)
    a=np.zeros((n,n),dtype=int)
    for i,j in combinations(range(n),2):
        if runs_neq(vs[i],vs[j])==1:
            a[i,j]=1;a[j,i]=1
    actual=np.linalg.eigvalsh(np.diag(a.sum(axis=1))-a)
    predicted=[]
    d=sum(prod(profile[i]-1 for i in range(s,t+1)) for s in range(len(profile)) for t in range(s,len(profile)))
    for eta in product(*[(q-1,-1) for q in profile]):
        adjacency_eig=sum(prod(eta[i] for i in range(s,t+1)) for s in range(len(profile)) for t in range(s,len(profile)))
        predicted.extend([d-adjacency_eig] * prod(profile[i]-1 for i in range(len(profile)) if eta[i]==-1))
    assert len(predicted)==n
    predicted.sort()
    assert np.max(np.abs(actual-predicted))<1e-7,(profile,actual,predicted)
    if n<=16:
        import sympy as sp
        tree=sp.det(sp.Matrix((np.diag(a.sum(axis=1))-a)[1:,1:]))
        fact=prod(int(v) for v in predicted[1:])//n
        assert tree==fact,(profile,tree,fact)
        return profile, n, tree
    return profile, n, 'spectra-pass'

def main():
    for q in (2,3,4):
        for k in range(1,9 if q==2 else (6 if q==3 else 5)):
            r=exhaustive(q,k)
            print('EXHAUSTIVE q,k,vertices,edges,diameter,W =',r)
    for q,k in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
        print('LP checked pair count',q,k, independent_LP_check(q,k))
    for profile in [(2,),(2,2),(2,2,2),(2,2,2,2),(2,2,2,2,2), (3,2,2),(2,3,2),(2,3,4),(3,3,3),(3,3,3,3),(4,4,2)]:
        print('SPECTRAL', spectral_check(profile))
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
