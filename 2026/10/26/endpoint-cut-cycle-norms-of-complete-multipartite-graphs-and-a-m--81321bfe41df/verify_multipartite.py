"""Exact rational verification of complete multipartite cut/cycle endpoint norms.

Python 3 standard library only. This is a finite consistency check, not a
replacement for the all-parameter proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def partitions(n, least=1):
    if n == 0:
        yield ()
    else:
        for first in range(least, n + 1):
            for rest in partitions(n - first, first):
                yield (first,) + rest


def invert(matrix):
    n = len(matrix)
    a = [[F(z) for z in row] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        factor = a[j][j]
        a[j] = [z / factor for z in a[j]]
        for i in range(n):
            if i != j:
                factor = a[i][j]
                if factor:
                    a[i] = [x - factor*y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def check_sizes(part_sizes):
    n = sum(part_sizes)
    vertex_parts = [i for i, v in enumerate(part_sizes) for _ in range(v)]
    edges = [(u, v) for u in range(n) for v in range(u+1, n)
             if vertex_parts[u] != vertex_parts[v]]
    L = [[0] * n for _ in range(n)]
    for u, v in edges:
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    Li = invert([row[:n-1] for row in L[:n-1]])
    f = lambda a: F(n*n - 2*n + 2 - a*a, n*(n-a))
    g = lambda a: F((n-2)**2 - a*a, n*(n-a))
    max_q = F(0)
    max_p = F(0)
    for u, v in edges:
        y = [F(int(i == u) - int(i == v)) for i in range(n-1)]
        pot = [sum(Li[i][j] * y[j] for j in range(n-1)) for i in range(n-1)] + [F(0)]
        col = [pot[x]-pot[z] for x,z in edges]
        q = sum(abs(z) for z in col)
        p = sum(abs(F(int((x,z) == (u,v))) - val) for (x,z), val in zip(edges,col))
        a,b=part_sizes[vertex_parts[u]],part_sizes[vertex_parts[v]]
        assert q == f(a)+f(b), (part_sizes, (u,v),q,f(a)+f(b))
        assert p == 1+g(a)+g(b), (part_sizes,(u,v),p,1+g(a)+g(b))
        max_q=max(max_q,q)
        max_p=max(max_p,p)
    assert max_q == max(f(a)+f(b) for a,b in combinations(part_sizes,2))
    assert max_p == max(1+g(a)+g(b) for a,b in combinations(part_sizes,2))
    if len(part_sizes) >= 3:
        top=sorted(part_sizes,reverse=True)
        assert max_q == f(top[0])+f(top[1])
    return len(edges)


def main():
    count = cols = 0
    for n in range(3,10):
        for part_sizes in partitions(n):
            if len(part_sizes)<2:
                continue
            cols += check_sizes(part_sizes)
            count += 1
    for k in range(3,41):
        n=k+3
        f=lambda a:F(n*n-2*n+2-a*a,n*(n-a))
        g=lambda a:F((n-2)**2-a*a,n*(n-a))
        assert f(k)>f(2)>f(1)
        assert g(2)>=g(1)>g(k)
        assert f(k)+f(2)==F(7*k*k+21*k+8,3*(k+1)*(k+3))
        assert 1+g(2)+g(1)==F(k*(3*k+7),(k+1)*(k+3))
        assert f(k)-f(1)==g(1)-g(k)==F(k-1,3*(k+3))
    print('COMPLETE_MULTIPARTITE_CERTIFICATE_OK', 'partitions='+str(count), 'columns='+str(cols),'family_cases=38')


if __name__=='__main__':
    main()
