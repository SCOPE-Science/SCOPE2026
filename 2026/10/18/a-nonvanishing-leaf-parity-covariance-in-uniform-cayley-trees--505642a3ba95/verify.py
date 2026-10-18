"""Exact finite checks for the rooted-Cayley leaf/parity covariance identity."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def prufer_tree(code, n):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    edges = []
    for v in code:
        u = next(i for i in range(n) if deg[i] == 1)
        edges.append((u, v))
        deg[u] -= 1
        deg[v] -= 1
    last = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(last))
    return edges


def root_even_and_leaves(edges, n):
    graph = [[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    leaves = sum(len(row) == 1 for row in graph)
    seen = {0}
    frontier = [0]
    depth = 0
    even = 0
    while frontier:
        if depth % 2 == 0:
            even += len(frontier)
        nxt = []
        for u in frontier:
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    nxt.append(v)
        frontier = nxt
        depth += 1
    assert len(seen) == n
    return even, leaves


def path_sign(n):
    out = Fraction(0)
    for d in range(1,n):
        out += Fraction((-1)**d * (d+1)*factorial(n-2),factorial(n-d-1)*n**d)
    return out


def predicted(n):
    b = Fraction(n+1,2) + Fraction(n-1,2)*path_sign(n)
    return b


def covariance_formula(n):
    if n == 2:
        return Fraction(0)
    p = Fraction(n-1,n)**(n-2)
    return p * (2*n-1+(n-3)*predicted(n-1)-n*predicted(n))


def expectation_given_even_size(n,k):
    l=n-k
    # 0**0 is 1: these are empty occupancy words.
    return (Fraction(k*(k-1)**(l-1),k**(l-1)) +
            Fraction(l*(l-1)**(k-1),l**(k-1)))


def check():
    assertions=0
    for n in range(2,8):
        moments=defaultdict(lambda:[0,0])
        B=L=BL=0
        for code in product(range(n), repeat=n-2):
            k,ell=root_even_and_leaves(prufer_tree(code,n),n)
            B+=k;L+=ell;BL+=k*ell
            moments[k][0]+=1;moments[k][1]+=ell
        z=n**(n-2)
        assert sum(c[0] for c in moments.values())==z
        assertions+=1
        b=Fraction(B,z)
        cov=Fraction(BL,z)-Fraction(B*L,z*z)
        assert b==predicted(n),(n,b,predicted(n));assert cov==covariance_formula(n),(n,cov,covariance_formula(n))
        assertions+=2
        for k in range(1,n):
            l=n-k
            expected_mass=comb(n-1,k-1)*k**(l-1)*l**(k-1)
            assert moments[k][0]==expected_mass,(n,k,moments[k][0],expected_mass)
            assert Fraction(moments[k][1],moments[k][0])==expectation_given_even_size(n,k)
            assertions+=2
        print(f'n={n}: trees={z}; covariance={cov}; exact identities confirmed')
    for n in range(4,55):
        assert covariance_formula(n) > 0, n  # finite diagnostics, not general proof
        assertions+=1
    print(f'{assertions} aggregate exact checks completed')


if __name__=='__main__':
    check()
