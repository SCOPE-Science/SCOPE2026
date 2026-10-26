"""Exact integer checks of signed-tree obstruction certificates.

Standard-library verification: python3 verify.py
Finite checks supplement, and do not replace, the mathematical proof.
"""
from fractions import Fraction
from math import gcd, pi, sin


def family(branches, level):
    assert branches >= 3 and branches % 2 == 1 and level >= 2
    edges = []
    signs = []
    for j in range(branches):
        branch = 'B{}'.format(j)
        sign = 1 if j < (branches + 1) // 2 else -1
        edges.append(('A0', branch))
        signs.append(sign)
        leaf_count = level - 1 if sign == 1 else level + 1
        for ell in range(leaf_count):
            edges.append((branch, 'A{}_{}'.format(j, ell)))
            signs.append(1)
    return edges, signs


def component(edges, excluded_edge, starting):
    adjacent = {}
    for i, (u, v) in enumerate(edges):
        if i == excluded_edge:
            continue
        adjacent.setdefault(u, []).append(v)
        adjacent.setdefault(v, []).append(u)
    seen = {starting}
    stack = [starting]
    while stack:
        for v in adjacent.get(stack.pop(), ()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def test_family(branches, level):
    edges, signs = family(branches, level)
    vertices = set(v for edge in edges for v in edge)
    a = {v for v in vertices if v.startswith('A')}
    b = vertices - a
    m = len(edges)
    assert m + 1 == len(vertices) == branches * (level + 1)
    assert len(a) == branches * level and len(b) == branches
    assert len(component(edges, -1, next(iter(vertices)))) == len(vertices)
    r = signs.count(-1)
    assert r == (branches - 1) // 2
    inc = {v: 0 for v in vertices}
    for (u, v), sign in zip(edges, signs):
        inc[u] += sign
        inc[v] += sign
    assert all(inc[v] == 1 for v in a)
    assert all(inc[v] == level for v in b)
    q = m - 2*r
    assert q == len(a) == len(b)*level
    k = [[(int(u == w) + int(u == z) + int(v == w) + int(v == z))
          for (w, z) in edges] for (u, v) in edges]
    assert all(sum(row[j]*signs[j] for j in range(m)) == level+1 for row in k)
    for i,(u,v) in enumerate(edges):
        if u in a:
            au = u
        else:
            au = v
        cut = component(edges,i,au)
        lval = len(cut & a) - level*len(cut & b)
        assert lval == signs[i]
    degree = max(sum(v in e for e in edges) for v in vertices)
    h = 1/(4*degree)  # Valid because lambda_max(K) <= 2 max degree.
    for phi in (0.27,0.91,2.14):
        z = [(pi if d == -1 else 0)+phi for d in signs]
        transformed = [z[i] + h*sum(k[i][j]*sin(z[j]) for j in range(m)) for i in range(m)]
        predicted = phi+(level+1)*h*sin(phi)
        assert all(abs(transformed[i] - ((pi if signs[i]==-1 else 0)+predicted)) < 1e-12
                   for i in range(m))
    return len(vertices),m,r


def check_lower_bound():
    # Necessary divisibility for unequal class signatures and at least one negative edge.
    for n in range(2,9):
        for a in range(1,n):
            b = n-a
            if a == b:
                continue
            minimum_q = a*b//gcd(a,b)
            assert minimum_q > n-3, (n,a,b,minimum_q)
    # First possible unequal-bipartition pair is 3+6 with q=6 and one negative.
    candidates = []
    n = 9
    for a in range(1,n):
        b=n-a
        if a==b: continue
        for r in range(1,(n-2)//2+1):
            q = n-1-2*r
            if q>0 and q%a==0 and q%b==0:
                candidates.append((a,b,r,q,q//a,q//b))
    assert candidates == [(3,6,1,6,2,1),(6,3,1,6,1,2)], candidates


def main():
    check_lower_bound()
    sample = test_family(3,2)
    assert sample == (9,8,1)
    cases = 0
    for branches in (3,5,7):
        for level in range(2,7):
            test_family(branches,level)
            cases += 1
    print('VERIFY_OK: 15 family instances; 9-node sharp witness; exact signed cuts;')
    print('          exact Kd vectors; scalar invariant-line evaluations; n<=8 arithmetic obstruction.')

if __name__ == '__main__':
    main()
