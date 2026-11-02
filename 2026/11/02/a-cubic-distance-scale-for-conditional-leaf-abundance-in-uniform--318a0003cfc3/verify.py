"""Independent finite-size reproducibility checks for a conditional Cayley-tree leaf law.

Run with Python 3.8+: python verify.py
The proof for all n is mathematical; finite checks are not a replacement for it.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def mean(n, ell):
    m = n-ell-1
    return Fraction(n-1, n)**(m-1)*(m+Fraction(2*ell,ell+1))


def binom_moment(n, ell, j):
    m = n-ell-1
    if m == 0:
        return Fraction(comb(2,j) if 0 <= j <= 2 else 0)
    a = comb(m+2,j) if 0 <= j <= m+2 else 0
    b = comb(m+1,j-1) if 1 <= j <= m+2 else 0
    return (Fraction(a)-Fraction(2*b,ell+1))*Fraction(n-j,n)**(m-1)


def enumerate_trees(n):
    counts = defaultdict(Counter)
    for code in product(range(n), repeat=n-2):
        deg = [1]*n
        for x in code:
            deg[x] += 1
        num_leaves = sum(d==1 for d in deg)
        residual = deg[:]
        graph = [[] for _ in range(n)]
        for x in code:
            leaf = next(i for i in range(n) if residual[i]==1)
            graph[leaf].append(x)
            graph[x].append(leaf)
            residual[leaf] -= 1
            residual[x] -= 1
        a,b = [i for i in range(n) if residual[i]==1]
        graph[a].append(b)
        graph[b].append(a)
        queue = [0]
        distance = {0:0}
        for x in queue:
            for y in graph[x]:
                if y not in distance:
                    distance[y]=distance[x]+1
                    queue.append(y)
        counts[distance[1]][num_leaves] += 1
    return counts


def run():
    assertions = 0
    for n in range(2,9):
        counts = enumerate_trees(n)
        assert sum(map(sum, (h.values() for h in counts.values())))==n**(n-2)
        assertions += 1
        for ell in range(1,n):
            h = counts[ell]
            total = sum(h.values())
            expected_dist_count = ((ell+1)*__import__('math').factorial(n-2)//__import__('math').factorial(n-ell-1))*n**(n-ell-2) if ell<n-1 else __import__('math').factorial(n-2)
            assert total==expected_dist_count, (n,ell,'path count')
            assertions += 1
            assert Fraction(sum(k*v for k,v in h.items()),total)==mean(n,ell), (n,ell,'mean')
            assertions += 1
            for j in range(n+1):
                empirical = Fraction(sum(comb(k,j)*v for k,v in h.items() if k>=j),total)
                assert empirical==binom_moment(n,ell,j), (n,ell,j,'factorial moment',empirical)
                assertions += 1
    for n in range(3,201):
        for ell in range(1,n-1):
            q = Fraction(n-1,n)**(n-ell-2)
            difference = q*Fraction(2*(n-1)-ell*(ell+1)**2,(n-1)*(ell+1)*(ell+2))
            assert mean(n,ell+1)-mean(n,ell)==difference,(n,ell,'difference')
            assertions += 1
    for n in range(11,51):
        assert mean(n,3)>mean(n,2)
        assertions += 1
    print('PASS:',assertions,'exact assertions; exhaustive Cayley trees n=2..8 and symbolic rational differences through n=200')

if __name__=='__main__':
    run()
