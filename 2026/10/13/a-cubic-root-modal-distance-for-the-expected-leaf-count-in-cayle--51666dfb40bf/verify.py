"""Exact finite checks for Cayley-tree leaf count conditioned on pair distance.

The combinatorial forest-determinant argument, rather than finite checks,
proves the general theorem.
"""
from fractions import Fraction
from itertools import product
from collections import deque


def mean_leaves(n, k):
    assert n >= 2 and 1 <= k < n
    if k == n - 1:
        return Fraction(2)
    return (Fraction(n-k+1)-Fraction(2,k+1))*Fraction(n-1,n)**(n-k-2)


def forest_count(n, s):
    assert 1 <= s <= n
    if s == n:
        return 1
    return s * n**(n-s-1)


def decode(n, code):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    adj = [[] for _ in range(n)]
    for v in code:
        u = next(i for i in range(n) if deg[i] == 1)
        adj[u].append(v); adj[v].append(u)
        deg[u] -= 1; deg[v] -= 1
    u,v = (i for i in range(n) if deg[i] == 1)
    adj[u].append(v); adj[v].append(u)
    return adj


def distance_01(adj):
    seen = {0}
    wave = [0]
    steps = 0
    while wave:
        if 1 in wave:
            return steps
        nxt = []
        for x in wave:
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); nxt.append(y)
        wave = nxt; steps += 1
    raise AssertionError('not a tree')


def exact_enumeration():
    cases = 0
    ntrees = 0
    for n in range(2,9):
        sums = [0]*n
        counts = [0]*n
        for code in product(range(n), repeat=n-2):
            adj = decode(n, code)
            k = distance_01(adj)
            counts[k] += 1
            sums[k] += sum(len(a)==1 for a in adj)
            ntrees += 1
        assert sum(counts) == n**(n-2)
        for k in range(1,n):
            expected_count = 1
            if k <= n-2:
                num_path_choices = 1
                for j in range(k-1):
                    num_path_choices *= n-2-j
                expected_count = num_path_choices * forest_count(n,k+1)
            else:
                expected_count = __import__('math').factorial(n-2)
            assert counts[k] == expected_count, (n,k,counts[k],expected_count)
            assert Fraction(sums[k],counts[k]) == mean_leaves(n,k), (n,k)
            cases += 1
    return cases, ntrees


def determinant(a):
    # Integer permutation expansion for small principal minors, independent
    # of the matrix-tree identity being checked.
    from itertools import permutations
    r=len(a)
    z=0
    for p in permutations(range(r)):
        inv=sum(p[i]>p[j] for i in range(r) for j in range(i+1,r))
        term=1
        for i in range(r):term*=a[i][p[i]]
        z += (-1 if inv%2 else 1)*term
    return z


def determinant_checks():
    tests=0
    for n in range(2,9):
        for s in range(1,n+1):
            r=n-s
            a=[[n-1 if i==j else -1 for j in range(r)] for i in range(r)]
            assert determinant(a) == forest_count(n,s), (n,s)
            tests+=1
    return tests


def finite_algebra_checks():
    steps = 0
    maxchecks=0
    for n in range(3,151):
        values = [None]+[mean_leaves(n,k) for k in range(1,n)]
        for k in range(1,n-1):
            delta=values[k+1]-values[k]
            if k<=n-3:
                expected=(Fraction(n-1,n)**(n-k-3)*
                  Fraction(2*n-(k*k+1)*(k+2), n*(k+1)*(k+2)))
            else:
                expected=Fraction(3-n,n-1)
            assert delta==expected,(n,k,delta,expected)
            steps+=1
        mode=next(k for k in range(1,n-1) if (k*k+1)*(k+2)>=2*n)
        maximum=max(values[1:])
        assert values[mode] == maximum,(n,mode)
        if n>=4:
            for k in range(1,mode):
                assert values[k+1]>values[k]
            for k in range(mode+1,n):
                assert values[k]<=values[k-1]
        maxchecks+=1
    return steps,maxchecks


if __name__ == '__main__':
    a,b = exact_enumeration()
    c = determinant_checks()
    d,e = finite_algebra_checks()
    print('PASS exact conditional means and distance frequencies:',a,
          'pairs,',b,'trees; forest determinants:',c,
          '; algebraic transitions:',d,'; mode checks:',e)
