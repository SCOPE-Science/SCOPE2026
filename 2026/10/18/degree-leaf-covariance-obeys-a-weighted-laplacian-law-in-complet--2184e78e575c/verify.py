"""Independent exact checks of degree--leaf covariances in multipartite spanning trees.

Uses exhaustive ordinary Prufer codes, compared with a separate factorial-product
occupancy representation. Requires only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import prod


def part_labels(sizes):
    return tuple(p for p, n in enumerate(sizes) for _ in range(n))


def independent_predictions(sizes):
    n = sum(sizes)
    r = len(sizes)
    assert r >= 3
    labels = part_labels(sizes)
    options = [(r-2, tuple(range(n)))]
    for p, cnt in enumerate(sizes):
        options.append((cnt-1, tuple(v for v in range(n) if labels[v] != p)))
    # Prufer excess-degree representation consists of independent categorical tokens.
    no_hit = []
    for i in range(n):
        no_hit.append(prod((F(len(S)-1, len(S)) ** count
                           for count, S in options if i in S), start=F(1)))
    W = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            W[i][j] = W[j][i] = sum(
                (F(cnt, len(S)*(len(S)-1)) for cnt, S in options
                 if i in S and j in S), F(0))
    result = [sum((W[i][j]*(no_hit[j]-no_hit[i])
                  for j in range(n) if j!=i), F(0)) for i in range(n)]
    count = n**(r-2) * prod((n-size)**(size-1) for size in sizes)
    return count, no_hit, result


def prufer_tree(seq,n):
    deg=[1]*n
    for v in seq: deg[v]+=1
    edges=[]
    for v in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, v))
        deg[leaf]-=1;deg[v]-=1
    leafs=[i for i in range(n) if deg[i]==1]
    edges.append((leafs[0],leafs[1]))
    return edges


def brute(sizes):
    labels=part_labels(sizes)
    n=len(labels)
    ct=0
    degsum=[0]*n
    leafsum=0
    mix=[0]*n
    for seq in product(range(n), repeat=n-2):
        edges=prufer_tree(seq,n)
        if any(labels[u]==labels[v] for u,v in edges):
            continue
        ct+=1
        deg=[0]*n
        for u,v in edges:deg[u]+=1;deg[v]+=1
        leaves=sum(d==1 for d in deg)
        leafsum+=leaves
        for i in range(n):
            degsum[i]+=deg[i];mix[i]+=deg[i]*leaves
    cov=[F(mix[i],ct)-F(degsum[i]*leafsum,ct*ct) for i in range(n)]
    return ct,cov


def run():
    tests=[(1,1,2),(1,2,2),(1,2,3),(1,2,4),(2,2,2),(1,1,1,1),(1,1,2,2),(2,2,3)]
    checks=0
    for sizes in tests:
        expected_count, q, calc=independent_predictions(sizes)
        count, direct=brute(sizes)
        assert count==expected_count,(sizes,'count',count,expected_count)
        checks+=1
        for i in range(sum(sizes)):
            assert direct[i]==calc[i],(sizes,i,direct[i],calc[i])
            checks+=1
        print(sizes,'trees',count,'class-covariances',
              [str(calc[sum(sizes[:j])]) for j in range(len(sizes))])
    assert independent_predictions((1,2,3))[2][1] < 0
    assert independent_predictions((1,2,4))[2][1] > 0
    checks+=2
    for a in range(1,7):
        for b in range(a,8):
            for c in range(b,9):
                n, q, cov=independent_predictions((a,b,c))
                if a<c:
                    assert cov[0]>0 and cov[-1]<0,(a,b,c)
                else:
                    assert all(x==0 for x in cov),(a,b,c)
                checks+=1
    print('PASS',checks,'exact assertions')

if __name__=='__main__':run()
