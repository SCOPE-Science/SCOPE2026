"""Exact rational checks for a Friedkin--Johnsen predictive-loop theorem.

Requires Python 3.9+ standard library only. Run: python3 verify.py
Finite examples supplement, and do not substitute for, the general proof.
"""
from fractions import Fraction as F
from itertools import product


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def product_mat(a, b):
    assert len(a[0]) == len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def times(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def inverse(m):
    n = len(m)
    a = [m[i][:] + eye(n)[i] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j] != 0)
        a[j], a[k] = a[k], a[j]
        t = a[j][j]
        a[j] = [v/t for v in a[j]]
        for k in range(n):
            if k == j:
                continue
            t = a[k][j]
            a[k] = [a[k][i] - t*a[j][i] for i in range(2*n)]
    return [row[n:] for row in a]


def build_p(adjacency, alpha):
    n = len(alpha)
    degree = [sum(row) for row in adjacency]
    assert n > 1 and all(z > 0 for z in degree)
    assert all(F(0) < x < F(1) for x in alpha)
    w = [[adjacency[i][j]/degree[i] for j in range(n)] for i in range(n)]
    b = [1-a for a in alpha]
    q = [[alpha[i]*w[i][j] for j in range(n)] for i in range(n)]
    p = product_mat(inverse([[F(i==j)-q[i][j] for j in range(n)]
                             for i in range(n)]),
                    [[b[i] if i == j else F(0) for j in range(n)]
                     for i in range(n)])
    raw = [degree[i]*b[i]/alpha[i] for i in range(n)]
    pi = [z/sum(raw) for z in raw]
    assert all(sum(row)==1 for row in p)
    assert all(pi[i]*p[i][j]==pi[j]*p[j][i]
               for i in range(n) for j in range(n))
    assert all(t>0 for row in p for t in row)
    return p, pi


def equilibrium(p, initial, beta):
    assert F(0) <= beta < F(1)
    n=len(initial)
    return [(1-beta)*v for v in
            times(inverse([[F(i==j)-beta*p[i][j]
                            for j in range(n)] for i in range(n)]),
                  times(p, initial))]


def variance(x, weight=None):
    n=len(x)
    w=weight if weight is not None else [F(1,n)]*n
    mean=sum(w[i]*x[i] for i in range(n))
    return sum(w[i]*(x[i]-mean)**2 for i in range(n))


def check_example():
    a=[[F(0),F(1),F(1)],[F(1),F(0),F(0)],[F(1),F(0),F(0)]]
    alpha=[F(1,10), F(1,100), F(19,20)]
    p,pi=build_p(a, alpha)
    assert pi == [F(342,2224),F(1881,2224),F(1,2224)]
    x0=[F(0),F(1,4),F(1)]
    at_zero=equilibrium(p,x0,F(0))
    at_twentieth=equilibrium(p,x0,F(1,20))
    assert at_zero == [F(1,64),F(317,1280),F(83,1280)]
    assert variance(at_zero)==F(8163,819200)
    assert variance(at_twentieth)==F(4179945336867,419399996328968)
    assert variance(at_twentieth)>variance(at_zero)
    # First derivative of the public's ordinary variance at beta=0.
    derivative_x=[times(p,[at_zero[i]-x0[i] for i in range(3)])[k]
                  for k in range(3)]
    mu=sum(at_zero)/3; mu_der=sum(derivative_x)/3
    derivative_var=F(2,3)*sum((at_zero[i]-mu)*(derivative_x[i]-mu_der)
                              for i in range(3))
    assert derivative_var==F(36441,458752000)>0
    weighted=[variance(equilibrium(p,x0,b),pi)
              for b in (F(0),F(1,20),F(1,3),F(3,4),F(19,20))]
    assert all(weighted[i]>weighted[i+1] for i in range(4))
    c=sum(pi[i]*x0[i] for i in range(3))
    assert all(sum(pi[i]*v[i] for i in range(3))==c
               for v in [at_zero,at_twentieth])
    print('Three-vertex exact counterexample: PASS')
    print('Ordinary variance beta=0:',variance(at_zero))
    print('Ordinary variance beta=1/20:',variance(at_twentieth))
    print('Exact excess:',variance(at_twentieth)-variance(at_zero))
    print('Positive initial variance derivative:', derivative_var)


def check_graphs():
    checked=0
    # Connected paths, stars and nonbipartite weighted triangles.
    for n in range(2,6):
        for shape in ('path','star','complete'):
            a=[[F(0) for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(i+1,n):
                    if shape=='complete' or shape=='path' and j==i+1 or \
                       shape=='star' and i==0:
                        a[i][j]=a[j][i]=F(1+i+2*j)
            for xs in ((F(1,5),F(2,5),F(3,5),F(4,5),F(1,2)),
                       (F(1,20),F(19,20),F(1,4),F(3,4),F(2,3))):
                alpha=list(xs[:n]); x=[F((3*i+2)%7,7) for i in range(n)]
                p,pi=build_p(a,alpha)
                prev=None
                for b in (F(0),F(1,10),F(1,2),F(9,10)):
                    y=equilibrium(p,x,b)
                    v=variance(y,pi)
                    assert sum(pi[i]*y[i] for i in range(n))==sum(pi[i]*x[i] for i in range(n))
                    assert prev is None or v<prev
                    prev=v
                    checked += 1
    print('Exact weighted-variance, reversibility and mean checks:',checked,'PASS')


def check_two_vertices():
    for a1,a2 in product((F(1,20),F(1,3),F(3,4),F(19,20)),repeat=2):
        p,pi=build_p([[F(0),F(1)],[F(1),F(0)]],[a1,a2])
        lam=p[0][0]-p[1][0]
        assert F(0)<lam<F(1)
        x=[F(0),F(1)]
        for b in (F(0),F(1,10),F(1,2),F(9,10)):
            y=equilibrium(p,x,b)
            assert y[1]-y[0] == (1-b)*lam/(1-b*lam)
    print('Two-vertex minimality (16 profiles x 4 levels): PASS')

if __name__=='__main__':
    check_example()
    check_graphs()
    check_two_vertices()
    print('ALL EXACT CHECKS PASSED')
