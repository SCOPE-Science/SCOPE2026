"""Independent exact Prüfer-tree enumeration for weighted Cayley forests.

Run: python3 verify.py; Python standard library only.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict, Counter
from math import comb


def tree_edges(code, vertices):
    degree = [1] * vertices
    for u in code:
        degree[u] += 1
    edges = []
    for u in code:
        leaf = min(v for v in range(vertices) if degree[v] == 1)
        edges.append((leaf, u))
        degree[leaf] -= 1
        degree[u] -= 1
    left = [v for v in range(vertices) if degree[v] == 1]
    edges.append((left[0], left[1]))
    return edges


def forest_counts(edges, n):
    # Vertex 0 is the hub; remove hub edges and find forest components.
    adjacency = [set() for _ in range(n + 1)]
    for u,v in edges:
        if 0 not in (u,v):
            adjacency[u].add(v)
            adjacency[v].add(u)
    seen = set()
    sizes = Counter()
    for v in range(1,n+1):
        if v in seen:
            continue
        todo = [v]
        seen.add(v)
        m=0
        while todo:
            u=todo.pop()
            m += 1
            for w in adjacency[u]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        sizes[m] += 1
    assert sum(k*v for k,v in sizes.items())==n
    return sizes


def F(n,t):
    return Fraction(1) if n == 0 else t*(n+t)**(n-1)


def EZ(n,t,k):
    return Fraction(comb(n,k)*k**(k-1),1)*t*F(n-k,t)/F(n,t)


def EZZ(n,t,k,l):
    if k+l>n:
        return Fraction(0)
    return Fraction(comb(n,k)*comb(n-k,l)*k**(k-1)*l**(l-1),1)*t**2*F(n-k-l,t)/F(n,t)


def verify(n,t):
    den = Fraction(0)
    one = [Fraction(0)]*(n+1)
    pair = [[Fraction(0)]*(n+1) for _ in range(n+1)]
    count=0
    for code in product(range(n+1),repeat=n-1):
        z=forest_counts(tree_edges(code,n+1), n)
        w=t**sum(z.values())
        den +=w
        count+=1
        for k in range(1,n+1):
            one[k]+=w*z[k]
            for l in range(k+1,n+1):
                pair[k][l]+=w*z[k]*z[l]
    assert den==F(n,t),(n,t,'partition',den,F(n,t))
    tests=1
    for k in range(1,n+1):
        assert one[k]/den==EZ(n,t,k),(n,t,k,'mean',one[k]/den,EZ(n,t,k))
        tests+=1
        for l in range(k+1,n+1):
            assert pair[k][l]/den==EZZ(n,t,k,l),(n,t,k,l,'pair',pair[k][l]/den,EZZ(n,t,k,l))
            tests+=1
    return count,tests


def main():
    cases=0
    checks=0
    tree_count=0
    for n in range(2,7):
        for t in (Fraction(1,2),Fraction(1),Fraction(2)):
            c,a=verify(n,t)
            cases+=1
            checks+=a
            tree_count+=c
    print('EXACT_ENUMERATION_PASS cases=%d checks=%d enumerated_weighted_tree_cases=%d' %(cases,checks,tree_count))

if __name__=='__main__':
    main()
