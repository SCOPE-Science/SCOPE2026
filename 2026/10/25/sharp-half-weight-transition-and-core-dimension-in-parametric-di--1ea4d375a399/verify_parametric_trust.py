"""Exact finite checks for the parametric directed minimum-incoming trust game.

Run with Python 3.9+: python verify_parametric_trust.py
No third-party packages or external data are required.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

PARAMETERS = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))


def graph_components(n, edges):
    parent = list(range(n))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for (i, j), w in edges.items():
        if w > 0:
            a, b = root(i), root(j)
            parent[a] = b
    groups = {}
    for i in range(n):
        groups.setdefault(root(i), 0)
        groups[root(i)] |= 1 << i
    return list(groups.values())


def values(n, edges, alpha, mask):
    internal = sum((w for (i,j), w in edges.items()
                    if mask & (1 << i) and mask & (1 << j)), F(0))
    external = F(0)
    for j in range(n):
        if mask & (1 << j):
            options = [w for (i,k),w in edges.items()
                       if k == j and not (mask & (1 << i))]
            external += min(options) if options else 0
    return alpha * internal + (1-alpha) * external


def check_graph(n, edges, alpha, restricted=True):
    all_mask = (1 << n) - 1
    v = [values(n,edges,alpha,mask) for mask in range(1<<n)]
    incoming = [sum((w for (i,j),w in edges.items() if j==k),F(0)) for k in range(n)]
    outgoing = [sum((w for (i,j),w in edges.items() if i==k),F(0)) for k in range(n)]
    W=sum(incoming,F(0))
    upper=[v[all_mask]-v[all_mask^(1<<i)] for i in range(n)]
    assert all(upper[i] == alpha*incoming[i]+(2*alpha-1)*outgoing[i] for i in range(n))
    assert sum(upper,F(0)) == (3*alpha-1)*W
    assert v[all_mask]==alpha*W
    if not W:
        assert not any(v)
        return
    if alpha<F(1,2):
        assert sum(upper,F(0))<v[all_mask]
        return
    star=[incoming[i]/2+(alpha-F(1,2))*outgoing[i] for i in range(n)]
    assert sum(star,F(0)) == v[all_mask]
    components=graph_components(n,edges)
    crossings=[]
    for S in range(1<<n):
        gap=sum((star[j] for j in range(n) if S&(1<<j)),F(0))-v[S]
        assert gap>=0, (n,edges,alpha,S,gap)
        crossing=any(bool(S&(1<<i))!=bool(S&(1<<j)) for (i,j),w in edges.items() if w>0)
        crossings.append(crossing)
        if alpha>F(1,2):
            assert (gap>0)==crossing, (n,edges,alpha,S,gap)
            union_of_components=all((S&C) in (0,C) for C in components)
            assert union_of_components != crossing
    if alpha==F(1,2):
        assert star==upper
    if not restricted:
        return
    # Verify each restricted game has an explicitly constructed allocation in its core.
    for S in range(1<<n):
        y=[F(0)]*n
        for j in range(n):
            if S&(1<<j):
                inside=sum((w for (i,k),w in edges.items() if k==j and S&(1<<i)),F(0))
                outside=[w for (i,k),w in edges.items() if k==j and not(S&(1<<i))]
                y[j]=alpha*inside+(1-alpha)*(min(outside) if outside else 0)
        assert sum(y,F(0))==v[S]
        for T in range(1<<n):
            if T & ~S: continue
            sub=sum((y[j] for j in range(n) if T&(1<<j)),F(0))
            assert sub>=v[T],('restricted',n,edges,alpha,S,T,sub-v[T])


def run():
    cases=0
    for n in (1,2,3,4):
        pairs = [(i,j) for i in range(n) for j in range(n) if i!=j]
        for bits in product((0,1), repeat=len(pairs)):
            edges = {e:F(w) for e,w in zip(pairs,bits) if w}
            for alpha in PARAMETERS:
                check_graph(n, edges, alpha, restricted=True)
                cases += 1
    rng=Random(260518157)
    weights=(F(0),F(1,5),F(2,5),F(3,5),F(4,5),F(1))
    for n in (2,3,4,5):
        pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
        for _ in range(45):
            edges={e:w for e in pairs if (w:=rng.choice(weights)) > 0}
            for alpha in (F(0),F(1,5),F(2,5),F(1,2),F(3,5),F(4,5),F(1)):
                check_graph(n, edges, alpha)
                cases+=1
    # A single directed arc has core interval: first payoff in [0, 2a-1]
    # for a>1/2, and only (0, 1/2) at the transition.
    edges={(0,1):F(1)}
    for alpha in PARAMETERS:
        v=lambda mask: values(2,edges,alpha,mask)
        if alpha >= F(1,2):
            left=(F(0),alpha)
            right=(2*alpha-1,1-alpha)
            for x in (left,right):
                assert sum(x,F(0)) == v(3)
                assert all(sum((x[j] for j in range(2) if mask&(1<<j)),F(0))>=v(mask)
                           for mask in range(4))
        else:
            assert v(1)+v(2)>v(3)
    print('PASS',cases,'parameterized graph cases; exact rational arithmetic')
    print('Scope: all loopless binary directed supports n<=4; 180 seeded weighted networks n<=5.')
    print('Checked: phase bound, universal core allocation, component tightness,')
    print('restricted-game total balancedness, and the two-player sharp witness.')


if __name__=='__main__':
    run()
