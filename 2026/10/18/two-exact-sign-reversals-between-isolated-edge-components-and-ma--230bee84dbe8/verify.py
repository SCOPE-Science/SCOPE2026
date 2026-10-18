"""Independent exact enumerations and rational checks for the isolated-edge/maximal-edge covariance."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, sqrt

checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


def predicted_covariance(n, p):
    b = comb(n, 2)
    a = comb(n - 2, 2)
    q = 1 - p * p
    return b * p * (1-p)**(2*(n-2)) * (1 + p * q**(n-4) * (a-b*q*q))


def f_value(n, p):
    a, b = comb(n-2, 2), comb(n, 2)
    return p*(1-p*p)**(n-4)*(b*(1-p*p)**2-a)


def exact_enumeration(n):
    edges = list(combinations(range(n),2))
    edge_count = len(edges)
    hist = defaultdict(lambda:[0,0,0,0])
    for mask in range(1 << edge_count):
        adj = [[False]*n for _ in range(n)]
        for bit,(u,v) in enumerate(edges):
            if mask & (1 << bit):
                adj[u][v] = adj[v][u] = True
        degrees = [sum(row) for row in adj]
        isolated_edges = 0
        maximal_edges = 0
        for u,v in edges:
            if not adj[u][v]:
                continue
            if degrees[u]==degrees[v]==1:
                isolated_edges += 1
            if not any(adj[u][k] and adj[v][k] for k in range(n) if k not in (u,v)):
                maximal_edges += 1
        moment = hist[mask.bit_count()]
        moment[0] += 1
        moment[1] += isolated_edges
        moment[2] += maximal_edges
        moment[3] += isolated_edges*maximal_edges
    for p in [Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(7,8)]:
        terms = [sum(vals[j] * p**k * (1-p)**(edge_count-k)
                     for k,vals in hist.items()) for j in range(4)]
        ex_i, ex_m, ex_im = terms[1:]
        exact_cov = ex_im - ex_i*ex_m
        check(terms[0] == 1, 'probability mass')
        check(ex_i == comb(n,2)*p*(1-p)**(2*(n-2)), 'isolated component marginal')
        check(ex_m == comb(n,2)*p*(1-p*p)**(n-2), 'maximal edge marginal')
        check(exact_cov == predicted_covariance(n,p), 'exact covariance')
    return 20


for n in (3,4,5,6):
    exact_enumeration(n)
check(f_value(3,Fraction(1,2)) == Fraction(9,8), "minimal-order peak witness")
for n in range(4,121):
    check(f_value(n,Fraction(1,n)) > 1,'two-crossing strict certificate')
    if n>=5:
        check(Fraction(n-4,n*n)<=Fraction(1,16),'uniform Bernoulli inequality')
        check(2-Fraction(4,n)>=Fraction(6,5),'lower bound on quadratic bracket')
for n in (4,5,6,8,10,20,50,100):
    a,b=comb(n-2,2), comb(n,2)
    p0 = sqrt(1-sqrt(a/b))
    assert f_value(n,0) == 0
    assert f_value(n,Fraction(1,n))>1
    check(f_value(n,p0*0.9999)>0,'positive near domain right boundary')
    check(f_value(n,(p0+1)/2)<0,'negative beyond positive domain')
    # One root is on each side of p=1/n, and their signs are bracketed exactly
    check(f_value(n,Fraction(1,n*n))<1,'small-p positive covariance')
print(f'PASS: {checks} assertions, all labelled-graph probability spaces of orders 3, 4, 5, 6 exhaustively enumerated')
