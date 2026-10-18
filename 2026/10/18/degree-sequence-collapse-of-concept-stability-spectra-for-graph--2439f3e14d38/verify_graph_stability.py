"""Independent exhaustive checks of graph-incidence concept stability.

Runs with Python 3 without third-party packages.
"""
from fractions import Fraction
from collections import Counter
from itertools import combinations


def predicted(n, edges):
    m = len(edges)
    deg = [sum(u == v or w == v for u, w in edges) for v in range(n)]
    assert min(deg) >= 2
    result = Counter({Fraction(1,1): 1})
    result[Fraction(1,2)] += m
    for d in deg:
        result[Fraction(2**d-1-d,2**d)] += 1
    result[Fraction(2**m - (sum(2**d for d in deg)-n-m+1),2**m)] += 1
    return result


def direct(n,edges):
    m=len(edges)
    full=(1<<m)-1
    incid=[(1<<u)|(1<<v) for u,v in edges]
    # Every subset of the edge objects is formed independently. Derivation
    # is the common-vertex set, starting with all vertices for the empty set.
    intent=[0]*(1<<m)
    intent[0]=(1<<n)-1
    for s in range(1,1<<m):
        lowest=s & -s
        i=lowest.bit_length()-1
        intent[s]=intent[s^lowest]&incid[i]
    # Group all edge-subsets by common attribute set. A closed extent is
    # the union of all edge-subsets having the same common attributes;
    # equivalently all edges covering that intent.
    concepts={}
    for s,b in enumerate(intent):
        a=0
        for j,mask in enumerate(incid):
            if mask & b == b: a |=1<<j
        if a not in concepts:
            concepts[a]=b
        assert concepts[a]==b
    spectrum=Counter()
    for a,b in concepts.items():
        good=sum(1 for s in range(1<<m) if (s & a)==s and intent[s]==b)
        spectrum[Fraction(good,2**a.bit_count())]+=1
    return spectrum,concepts


def verify_graph(n, edges):
    d,cs=direct(n,edges)
    p=predicted(n,edges)
    assert d==p,(n,edges,d,p)
    m=len(edges)
    assert len(cs)==m+n+2, (n,edges,len(cs),m+n+2)
    # Every vertex degree is at least two. Its incident-edge set is a coatom.
    stars=[sum(1<<j for j,(u,w) in enumerate(edges) if v in (u,w)) for v in range(n)]
    atoms=[1<<j for j in range(m)]
    assert set(cs)==({0,(1<<m)-1}|set(stars)|set(atoms))
    for v in range(n):
        assert all(not (stars[v] < a < (1<<m)-1 and (stars[v]&a)==stars[v]) for a in cs)
    for u,v in combinations(range(n),2):
        intersection=stars[u]&stars[v]
        assert (intersection!=0)==((u,v) in edges)
        if intersection: assert intersection in atoms
    return (1<<m)


def all_graphs(n):
    poss=list(combinations(range(n),2))
    for mask in range(1<<len(poss)):
        edges=[e for j,e in enumerate(poss) if mask>>j&1]
        if all(sum(v in e for e in edges)>=2 for v in range(n)):
            yield edges


def run():
    count=0; subsets=0
    for n in range(3,6):
        for edges in all_graphs(n):
            subsets+=verify_graph(n,edges)
            count+=1
    # Explicit connected, cubic, nonisomorphic witness frames.
    k33=[(u,v) for u in range(3) for v in range(3,6)]
    prism=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
    a=predicted(6,k33);b=predicted(6,prism)
    assert a==b
    assert a==Counter({Fraction(1,1):1,Fraction(1,2):15,Fraction(239,256):1})
    assert all(sum(v in e for e in k33)==3 for v in range(6))
    assert all(sum(v in e for e in prism)==3 for v in range(6))
    assert not any(all(tuple(sorted(e)) in k33 for e in combinations(t,2)) for t in combinations(range(6),3))
    assert any(all(tuple(sorted(e)) in prism for e in combinations(t,2)) for t in combinations(range(6),3))
    for name,ed in [('K33',k33),('triangular_prism',prism)]:
        subsets+=verify_graph(6,ed)
        count+=1
    print('VERIFY_OK graphs=%d enumerated_object_subsets=%d witness=K33_vs_triangular_prism spectrum=1:1,1/2:15,239/256:1' % (count,subsets))

if __name__=='__main__':run()
