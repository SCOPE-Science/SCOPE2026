"""Exact finite verifier for three-member-group additions in a linear opinion model.

Python 3 standard library only. All arithmetic is exact rational.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def inverse(M):
    n = len(M)
    a = [[F(M[i][j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        q = next(i for i in range(k, n) if a[i][k])
        a[k], a[q] = a[q], a[k]
        p = a[k][k]
        a[k] = [v / p for v in a[k]]
        for i in range(n):
            if i != k and a[i][k]:
                t = a[i][k]
                a[i] = [a[i][j] - t * a[k][j] for j in range(2 * n)]
    return [row[n:] for row in a]


def triple_list(n):
    return list(combinations(range(n), 3))


def matrix(n, triples):
    # The resulting integer matrix is three times (I + clique-projection Laplacian).
    m = [[3 * int(i == j) for j in range(n)] for i in range(n)]
    for tri in triples:
        for i, j in combinations(tri, 2):
            m[i][i] += 1
            m[j][j] += 1
            m[i][j] -= 1
            m[j][i] -= 1
    return m


def opinions(n):
    return [(1,) + tuple(1 if mask & (1 << (i-1)) else -1
                         for i in range(1, n)) for mask in range(1 << (n-1))]


def connected(n, triples):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for a, b, c in triples:
        parent[root(b)] = root(a)
        parent[root(c)] = root(a)
    return len(set(root(i) for i in range(n))) == 1


def polarizations(n, triples, signs):
    inv = inverse(matrix(n, triples))
    out = []
    for s in signs:
        z = [3 * sum(inv[i][j] * s[j] for j in range(n)) for i in range(n)]
        mean = F(sum(s), n)
        assert sum(z) == sum(s)
        out.append(sum((v-mean)**2 for v in z))
    return out


def cutoff():
    for n in range(3, 6):
        E = triple_list(n)
        pats = opinions(n)
        values = {}
        for mask in range(1, 1 << len(E)):
            triples = [E[i] for i in range(len(E)) if mask & (1 << i)]
            if connected(n, triples):
                values[mask] = polarizations(n, triples, pats)
        tests = 0
        for mask, before in values.items():
            for i in range(len(E)):
                if mask & (1 << i):
                    continue
                after = values[mask | (1 << i)]
                for k, (a, b) in enumerate(zip(before, after)):
                    assert b <= a, (n, mask, i, pats[k], b-a)
                    tests += 1
        expected = {3:(1,0), 4:(11,128), 5:(958,73760)}[n]
        assert (len(values), tests) == expected, (n,len(values),tests)
        print('n={} connected={} exact_signed_addition_checks={}'.format(n,len(values),tests))


def witness():
    n=6
    old = [(0,1,4),(0,2,5),(0,3,4)]
    new = (0,1,3)
    s=(-1,-1,-1,-1,1,-1)
    assert connected(n,old)
    before = polarizations(n,old,[s])[0]
    after = polarizations(n,old+[new],[s])[0]
    assert after > before
    print('six_node_before=',before)
    print('six_node_after=',after)
    print('six_node_increase=',after-before)
    unit_binary = (0,0,0,0,1,0)
    pb = polarizations(n,old,[unit_binary])[0]
    pa = polarizations(n,old+[new],[unit_binary])[0]
    assert pb==F(2585,16854) and pa==F(1193,7776)
    assert pa-pb==F(977,21842784)==(after-before)/4
    print('zero_one_binary_increase=',pa-pb)
    assert len(old)==3 and not connected(n,old[:2])
    assert matrix(n,old)==list(map(list,zip(*matrix(n,old))))
    return before,after,after-before



def positive_weight_identity():
    """Certify the exact rational identity for every positive group weight."""
    n = 6
    base = [(0, 1, 4), (0, 2, 5), (0, 3, 4)]
    extra = (0, 1, 3)
    sign = [-1, -1, -1, -1, 1, -1]
    M0 = matrix(n, base)
    M1 = matrix(n, [extra])
    Q = [[M1[i][j] - (3 if i == j else 0) for j in range(n)] for i in range(n)]
    a = [-41, -41, -53, -41, 1, -53]
    b = [-111, -117, -147, -117, 3, -147]
    mv = lambda M, v: [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
    assert mv(M0, b) == [9 * 53 * w for w in sign]
    assert [x+y for x,y in zip(mv(M0,a), mv(Q,b))] == [9*19*w for w in sign]
    assert mv(Q,a) == [0]*n
    # Therefore z_i(t)=(a_i*t+b_i)/(3*(19*t+53)) solves the
    # equilibrium equation for every t>=0, by coefficient comparison.
    # The mean opinion is -2/3 for every t.
    alpha = [a[i]+38 for i in range(n)]
    beta = [b[i]+106 for i in range(n)]
    coefficients = [sum(x*x for x in beta),
                    2*sum(x*y for x,y in zip(alpha,beta)),
                    sum(x*x for x in alpha)]
    denominator_coefficients = [53*53, 2*53*19, 19*19]
    right_coefficients = [0,9*8*424,9*8*553]
    for k in range(3):
        assert 8427*coefficients[k]-9*5170*denominator_coefficients[k] == right_coefficients[k]
    # Hence P(t)-P(0)=8*t*(553*t+424)/(8427*(19*t+53)**2)>0 for t>0.
    # Affine rescaling from {-1,+1} to {0,1} divides polarization by four.
    print('all_positive_group_weights_algebraic_identity=PASS')

if __name__ == '__main__':
    cutoff()
    witness()
    positive_weight_identity()
    print('EXACT VERIFICATION PASSED')
