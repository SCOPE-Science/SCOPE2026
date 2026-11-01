#!/usr/bin/env python3
"""Exact rational checks for complete-bipartite metric-network distance laws.

This standalone script uses only the Python standard library.  It supplies
finite reproducibility checks, not a substitute for the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product


def graph_edges(a, b):
    return [(i, a + j) for i in range(a) for j in range(b)]


def distances(a, b):
    n = a + b
    d = [[Q(0) if i == j else Q(n + 2) for j in range(n)] for i in range(n)]
    for u, v in graph_edges(a, b):
        d[u][v] = d[v][u] = Q(1)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def graph_point_distance(e, f, x, y, d):
    (u, v), (w, z) = e, f
    ans = min(x + d[u][w] + y,
              x + d[u][z] + 1 - y,
              1 - x + d[v][w] + y,
              1 - x + d[v][z] + 1 - y)
    return min(ans, abs(x - y)) if e == f else ans


def classified_distance(e, f, x, y):
    if e == f:
        return abs(x - y)
    if e[0] == f[0]:
        return x + y
    if e[1] == f[1]:
        return 2 - x - y
    return 2 - abs(x - y)


def classes(a, b):
    edges = graph_edges(a, b)
    return (sum(e == f for e in edges for f in edges),
            sum(e != f and (e[0] == f[0] or e[1] == f[1])
                for e in edges for f in edges),
            sum(e[0] != f[0] and e[1] != f[1] for e in edges for f in edges))


def components_cdf(t):
    t = Q(t)
    if t <= 0: return Q(0), Q(0), Q(0)
    if t <= 1: return 2 * t - t * t, t * t / 2, Q(0)
    if t <= 2: return Q(1), 1 - (2 - t)**2 / 2, (t - 1)**2
    return Q(1), Q(1), Q(1)


def mixture_cdf(a, b, t):
    p = a * b
    k = a + b - 2
    q = (a - 1) * (b - 1)
    cs, ca, cd = components_cdf(t)
    return (cs + k * ca + q * cd) / p


def formula_cdf(a, b, t):
    t = Q(t)
    n, p = a + b, a * b
    if t <= 0: return Q(0)
    if t <= 1: return (2*t + (n-4)*t*t/2)/p
    if t <= 2:
        return (t-1)**2 + (2-t)*((n-1)*t-(n-2)*(2-t)/2)/p
    return Q(1)


def mean(a, b):
    n, p = a+b, a*b
    return Q(5,3) - Q(2*n,3*p)


def second_moment(a,b):
    n,p=a+b,a*b
    return Q(17,6)-Q(10*n-4,6*p)


def max_cdf_gap(n, p_smaller, p_larger):
    return Q(2*(n-1)**2,3*n-4)*(Q(1,p_smaller)-Q(1,p_larger))


def witness(n):
    return Q(2*(2*n-3), 3*n-4)


def main():
    checks = 0
    for a in range(1,6):
        for b in range(1,6):
            edges = graph_edges(a,b)
            d = distances(a,b)
            assert classes(a,b) == (a*b,a*b*(a+b-2),a*b*(a-1)*(b-1))
            checks += 1
            for e,f in product(edges,repeat=2):
                for x,y in product([Q(1,5),Q(2,5),Q(4,5)],repeat=2):
                    got = graph_point_distance(e,f,x,y,d)
                    expected = classified_distance(e,f,x,y)
                    assert got == expected, (a,b,e,f,x,y,got,expected)
                    checks += 1
            for k in range(-1,18):
                z = Q(k,8)
                assert formula_cdf(a,b,z)==mixture_cdf(a,b,z)
                checks += 1
            assert formula_cdf(a,b,1)==Q(a+b,2*a*b)
            assert formula_cdf(a,b,2)==1
            checks += 2
            # Independently reconstructed conditional moments from their laws.
            ma = (Q(1,3)+(a+b-2)*Q(1)+(a-1)*(b-1)*Q(5,3))/(a*b)
            mb = (Q(1,6)+(a+b-2)*Q(7,6)+(a-1)*(b-1)*Q(17,6))/(a*b)
            assert ma==mean(a,b)
            assert mb==second_moment(a,b)
            checks += 2
    for n in range(4,31):
        pairs=sorted([(a,n-a) for a in range(1,(n//2)+1)],key=lambda ab:ab[0]*ab[1])
        for i in range(len(pairs)-1):
            a,b=pairs[i]; c,d=pairs[i+1]
            p1,p2=a*b,c*d
            assert p1<p2
            for k in range(1,32):
                t=Q(k,16)
                if t>=2:continue
                gap=formula_cdf(a,b,t)-formula_cdf(c,d,t)
                assert gap>0,(n,p1,p2,t,gap)
                assert gap<=max_cdf_gap(n,p1,p2)
                checks+=2
            t=witness(n)
            assert 1<t<2
            assert formula_cdf(a,b,t)-formula_cdf(c,d,t)==max_cdf_gap(n,p1,p2)
            assert mean(c,d)-mean(a,b)==Q(2*n,3)*(Q(1,p1)-Q(1,p2))
            checks+=3
    assert formula_cdf(2,2,Q(3,2))==Q(3,4)
    assert mean(1,3)==Q(7,9)
    assert mean(2,2)==Q(1)
    assert max_cdf_gap(4,3,4)==Q(3,16)
    assert mean(2,2)-mean(1,3)==Q(2,9)
    checks+=5
    print(f'PASS: {checks} exact rational independent checks; graph endpoint paths, densities, stochastic order, W1 and TV gaps.')


if __name__ == '__main__':
    main()
