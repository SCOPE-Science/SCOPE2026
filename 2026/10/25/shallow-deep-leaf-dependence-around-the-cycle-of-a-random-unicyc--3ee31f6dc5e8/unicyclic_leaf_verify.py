"""Exact checks of leaf depth classes in rooted forests underlying unicyclic graphs.

Only standard-library Python is needed.  Run: python unicyclic_leaf_verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb
from math import factorial


def fall(x, r):
    return factorial(x) // factorial(x-r) if 0 <= r <= x else 0


def forest_count(q, k):
    if q == k:
        return 1
    return k*q**(q-k-1)


def expected_factorial(n, k, r, s):
    m = n-k
    if r+s > m:
        return Fraction(0)
    z = m-r-s
    return Fraction(fall(m, r+s)*k**r*z**s*forest_count(n-r-s,k), forest_count(n,k))


def enumerate_forests(n, k):
    m = n-k
    roots = set(range(k))
    nonroots = list(range(k,n))
    parents = [[v for v in range(n) if v != u] for u in nonroots]
    tally = Counter()
    for parent_choices in product(*parents):
        P=dict(zip(nonroots,parent_choices))
        valid=True
        for x in nonroots:
            seen=set()
            while x not in roots:
                if x in seen:
                    valid=False
                    break
                seen.add(x)
                x=P[x]
            if not valid:
                break
        if not valid:
            continue
        children=Counter(parent_choices)
        j=sum(children[v]==0 and P[v] in roots for v in nonroots)
        h=sum(children[v]==0 and P[v] not in roots for v in nonroots)
        tally[(j,h)] += 1
    return tally


def main():
    checks=0
    total_forests=0
    for n in range(4,10):
        for k in range(3,n):
            m=n-k
            d=enumerate_forests(n,k)
            total=sum(d.values())
            assert total==forest_count(n,k),(n,k,total,forest_count(n,k))
            total_forests+=total
            for r in range(m+1):
                for s in range(m-r+1):
                    empirical=sum(count*fall(j,r)*fall(h,s) for (j,h),count in d.items())
                    theory=expected_factorial(n,k,r,s)*total
                    assert empirical==theory,(n,k,r,s,empirical,theory)
                    checks+=1
            EJ=expected_factorial(n,k,1,0)
            EK=expected_factorial(n,k,0,1)
            EJK=expected_factorial(n,k,1,1)
            cov=EJK-EJ*EK
            assert (cov<0)==(m>=2),(n,k,cov)
    # Independent simple-graph census: connected n-edge graphs are unicyclic.
    graph_checks=0
    all_graphs=0
    for n in range(3,8):
        e=list(combinations(range(n),2))
        by_cycle={}
        for chosen in combinations(e,n):
            adj=[set() for _ in range(n)]
            for a,b in chosen:
                adj[a].add(b);adj[b].add(a)
            visited={0};stack=[0]
            while stack:
                for v in adj[stack.pop()]:
                    if v not in visited:visited.add(v);stack.append(v)
            if len(visited)<n:continue
            degree=[len(a) for a in adj]
            work=[v for v in range(n) if degree[v]<=1]
            deleted=set()
            while work:
                v=work.pop()
                if v in deleted:continue
                deleted.add(v)
                for z in adj[v]:
                    degree[z]-=1
                    if degree[z]==1:work.append(z)
            core=set(range(n))-deleted
            k=len(core)
            assert k>=3
            leaves=[v for v in range(n) if len(adj[v])==1]
            j=sum(next(iter(adj[v])) in core for v in leaves)
            h=len(leaves)-j
            by_cycle.setdefault(k,Counter())[(j,h)]+=1
            all_graphs+=1
        for k,d in by_cycle.items():
            assert sum(d.values())==comb(n,k)*factorial(k-1)//2 * forest_count(n,k)
            m=n-k
            for r in range(m+1):
                for s in range(m-r+1):
                    actual=sum(count*fall(j,r)*fall(h,s) for (j,h),count in d.items())
                    predicted=expected_factorial(n,k,r,s)*sum(d.values())
                    assert actual==predicted,(n,k,r,s,actual,predicted)
                    graph_checks+=1
    print('PASS',checks,'rooted-forest exact mixed moments over',total_forests,'forests;')
    print('PASS',graph_checks,'independent graph exact mixed moments over',all_graphs,'unicyclic graphs; all covariance signs')

if __name__=='__main__':main()
