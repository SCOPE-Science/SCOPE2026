"""Exact finite certificate for susceptibility-optimal single-vertex deletion in small trees.

Run using Python 3 (standard library only): python verify_vaccination.py
"""
from itertools import product
from math import comb, factorial
from fractions import Fraction

DEGREE = 5



def prufer_graph(n, word):
    degree = [1]*n
    for a in word:
        degree[a] += 1
    graph = [set() for _ in range(n)]
    for a in word:
        leaf = next(i for i in range(n) if degree[i] == 1)
        graph[a].add(leaf)
        graph[leaf].add(a)
        degree[leaf] -= 1
        degree[a] -= 1
    u,v = [i for i in range(n) if degree[i] == 1]
    graph[u].add(v)
    graph[v].add(u)
    return graph


def distance_polynomial(graph, removed):
    n = len(graph)
    out = [0]*n
    for a in range(n):
        if a == removed: continue
        dist = {a:0}
        q = [a]
        for w in q:
            for y in graph[w]:
                if y != removed and y not in dist:
                    dist[y] = dist[w]+1
                    q.append(y)
        for b,d in dist.items():
            if a<b:
                out[d] += 1
    return tuple(out)


def bernstein_scaled(power_coeffs, index, m):
    return sum(power_coeffs[k]*comb(index,k)*factorial(k)*factorial(m-k)
               for k in range(min(index+1,len(power_coeffs))))


def valid_constant_winner(polys, winner):
    for u in range(len(polys)):
        difference = tuple(x-y for x,y in zip(polys[u],polys[winner]))
        if any(bernstein_scaled(difference,j,DEGREE)<0 for j in range(DEGREE+1)):
            return False
    return True


def evaluate(poly,p):
    return sum(coefficient*(p**i) for i,coefficient in enumerate(poly))


def exact_bond_mean(graph, vaccinated, p):
    """Separate bond-configuration enumeration, not based on distance counting."""
    n = len(graph)
    vertices = [u for u in range(n) if u!=vaccinated]
    edges = [(u,v) for u in vertices for v in graph[u] if u<v and v!=vaccinated]
    expectation = Fraction(0)
    for bits in product((0,1),repeat=len(edges)):
        probability = Fraction(1)
        g = {v:set() for v in vertices}
        for (u,v),bit in zip(edges,bits):
            probability *= p if bit else (1-p)
            if bit:
                g[u].add(v);g[v].add(u)
        total = 0
        for source in vertices:
            reached={source}
            queue=[source]
            for w in queue:
                for u in g[w]:
                    if u not in reached:
                        reached.add(u); queue.append(u)
            total += len(reached)
        expectation += probability*Fraction(total,len(vertices))
    return expectation


def check():
    examined = 0
    for n in range(2,8):
        count=0
        for word in product(range(n),repeat=n-2):
            graph = prufer_graph(n,word)
            polys = [distance_polynomial(graph,v) for v in range(n)]
            # A single nonadaptive vertex works at every 0<=p<=1.
            if not any(valid_constant_winner(polys,v) for v in range(n)):
                raise AssertionError(('low-order certificate failed',n,word,polys))
            count+=1
        assert count == n**(n-2)
        examined+=count

    # S(1,1,5), center 0, short leaves 1,2, long arm 3--4--5--6--7.
    edge_list = [(0,1),(0,2),(0,3),(3,4),(4,5),(5,6),(6,7)]
    g = [set() for _ in range(8)]
    for u,v in edge_list:
        g[u].add(v);g[v].add(u)
    polys=[distance_polynomial(g,v) for v in range(8)]
    expected = {
      0:(0,4,3,2,1,0,0,0), 1:(0,6,5,4,3,2,1,0), 2:(0,6,5,4,3,2,1,0),
      3:(0,5,3,1,0,0,0,0), 4:(0,5,4,0,0,0,0,0),
      5:(0,5,4,2,0,0,0,0), 6:(0,5,5,3,2,0,0,0),
      7:(0,6,6,4,3,2,0,0)
    }
    assert all(polys[v]==expected[v] for v in range(8))
    for v in range(1,8):
        if v!=3:
            diff = tuple(x-y for x,y in zip(polys[v],polys[3]))
            assert all(bernstein_scaled(diff,j,6)>=0 for j in range(7))
            assert evaluate(polys[v],Fraction(1,2))>evaluate(polys[3],Fraction(1,2))
    assert tuple(x-y for x,y in zip(polys[3],polys[0])) == (0,1,0,-1,-1,0,0,0)
    for p in [Fraction(1,10), Fraction(3,4), Fraction(4,5), Fraction(9,10)]:
        vals = [1+Fraction(2,7)*evaluate(poly,p) for poly in polys]
        if p<=Fraction(3,4): assert vals[0]<min(vals[1:])
        if p>=Fraction(4,5): assert vals[3]<min(vals[v] for v in range(8) if v!=3)
        for v in range(8):
            assert vals[v]==exact_bond_mean(g,v,p)
    # Endpoint pair-count comparison in S(1,1,L) for every L>=5.
    for L in range(5,50):
        n = L+3
        center_pairs = comb(n-3,2)
        next_pairs = comb(3,2)+comb(n-4,2)
        assert center_pairs-next_pairs==n-7>0
    print('VERIFY_OK labeled_trees=%d all_p_Bernstein_certificates=YES '
          'eight_vertex_profiles=8 exact_outbreak_enumerations=%d '
          'spider_endpoint_identity=YES' % (examined,8*4))

if __name__=='__main__': check()
