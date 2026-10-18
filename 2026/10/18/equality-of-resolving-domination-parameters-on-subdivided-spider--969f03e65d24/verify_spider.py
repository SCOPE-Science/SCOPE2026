"""Reproduce finite checks for vertex-edge domination and resolving on spiders.
No external dependencies. Execute: python verify_spider.py.
"""
from itertools import combinations, combinations_with_replacement
from collections import deque


def ceildiv(a, b):
    return (a + b - 1)//b


def predictions(lengths):
    t=len(lengths)
    u=sum(ceildiv(L-1,3) for L in lengths)
    eta = 0 if (all(L%3!=1 for L in lengths) and any(L%3==2 for L in lengths)) else 1
    dm=u+eta
    centers=1+sum(ceildiv(L-2,4) for L in lengths)+max(0,sum(L==2 for L in lengths)-1)
    nofirst=sum(ceildiv(L,4) for L in lengths)
    first=sum(ceildiv(L-1,4) for L in lengths) + int(all(L%4 in (0,1) for L in lengths))
    em=min(centers,nofirst,first)
    return dm,em


def make_spider(lengths):
    E=[]; n=1
    for L in lengths:
        previous=0
        for d in range(L):
            E.append((previous,n)); previous=n; n+=1
    return n,E


def exact(lengths):
    n, E=make_spider(lengths)
    adj=[set() for _ in range(n)]
    for a,b in E: adj[a].add(b); adj[b].add(a)
    dist=[]
    for v in range(n):
        row=[-1]*n; row[v]=0; q=deque([v])
        while q:
            w=q.popleft()
            for u in adj[w]:
                if row[u]==-1: row[u]=row[w]+1; q.append(u)
        dist.append(row)
    edist=[[min(dist[v][a], dist[v][b]) for a,b in E] for v in range(n)]
    # All pairs of different vertex/edge distance codes get a separating bit mask.
    v_pairs=[sum((1<<w) for w in range(n) if dist[w][a]!=dist[w][b]) for a,b in combinations(range(n),2)]
    e_pairs=[sum((1<<w) for w in range(n) if edist[w][a]!=edist[w][b]) for a,b in combinations(range(len(E)),2)]
    v_cover=[sum(1<<u for u in {v}|adj[v]) for v in range(n)]
    e_cover=[sum(1<<i for i,d in enumerate(edist[v]) if d<=1) for v in range(n)]
    nvm=(1<<n)-1; nem=(1<<len(E))-1
    dmin=emin=n+1
    for mask in range(1,1<<n):
        bits=mask.bit_count()
        if bits>=dmin and bits>=emin: continue
        if bits<dmin:
            cover=0
            for v in range(n):
                if mask>>v&1: cover |= v_cover[v]
            if cover==nvm and all(mask&s for s in v_pairs): dmin=bits
        if bits<emin:
            cover=0
            for v in range(n):
                if mask>>v&1: cover |= e_cover[v]
            if cover==nem and all(mask&s for s in e_pairs): emin=bits
    return dmin,emin


def check_resolution_arm_lemma(lengths):
    """Check the branch-support iff independently for every vertex subset."""
    n, E=make_spider(lengths)
    t=len(lengths)
    arms=[]; k=1
    for L in lengths:
        arms.append(sum(1<<v for v in range(k,k+L)))
        k+=L
    adj=[set() for _ in range(n)]
    for a,b in E: adj[a].add(b); adj[b].add(a)
    distances=[]
    for x in range(n):
        row=[-1]*n; row[x]=0; q=deque([x])
        while q:
            y=q.popleft()
            for z in adj[y]:
                if row[z]<0: row[z]=row[y]+1; q.append(z)
        distances.append(row)
    for mask in range(1<<n):
        landmarks=[j for j in range(n) if mask>>j&1]
        expected=sum(bool(mask&arm) for arm in arms)>=t-1
        vc=[tuple(distances[w][v] for w in landmarks) for v in range(n)]
        ec=[tuple(min(distances[w][a],distances[w][b]) for w in landmarks) for a,b in E]
        assert (len(set(vc))==len(vc))==expected, ('vertex lemma',lengths,mask)
        assert (len(set(ec))==len(ec))==expected, ('edge lemma',lengths,mask)
    return 1<<n


def run_checks():
    support_checks=sum(check_resolution_arm_lemma(L) for L in ((2,2,2),(2,3,3),(2,3,4),(3,3,3)))
    total=0
    for t in (3,4):
        for lengths in combinations_with_replacement(range(2,8),t):
            if sum(lengths)>13: continue
            expected=predictions(lengths)
            actual=exact(lengths)
            assert expected==actual, (lengths,expected,actual)
            assert (expected[0]==expected[1])==(max(lengths)<=3 and min(lengths)==2), lengths
            total+=1
    # Extra exhaustive graph instances with larger branches.
    for lengths in ((2,2,8),(2,3,7),(2,4,6),(3,3,7),(2,2,2,7)):
        if sum(lengths)>15: continue
        assert predictions(lengths)==exact(lengths),lengths
        total+=1
    # Modular equality prediction against closed formulas for many profiles.
    big=0
    for t in (3,4,5):
        for lengths in combinations_with_replacement(range(2,21),t):
            a,b=predictions(lengths)
            assert a>=b,(lengths,a,b)
            assert (a==b) == (max(lengths)<=3 and min(lengths)==2),(lengths,a,b)
            big+=1
    print('PASS: resolving-arm lemma',support_checks,'subsets; exact distance-based minima',total,'spiders; modular equality',big,'profiles')


if __name__=='__main__':
    run_checks()
