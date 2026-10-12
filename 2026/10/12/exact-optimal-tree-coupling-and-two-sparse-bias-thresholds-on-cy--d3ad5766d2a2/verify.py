"""Exact, standalone finite-model checks for one-out cycle couplings."""
from fractions import Fraction as F
from itertools import product
from math import comb


def confirm(n, p):
    q = 1-p
    weights_by_m = {}
    tree_marginal = [F(0) for _ in range(n)]
    cost = F(0)
    tree_event = [F(0) for _ in range(n)]
    checks = 0
    for bits in product((0, 1), repeat=n):
        a = sum(bits)
        w = p**a * q**(n-a)
        missing = [i for i in range(n) if bits[i] == 0 and bits[(i+1)%n] == 1]
        m = len(missing)
        weights_by_m[m] = weights_by_m.get(m, F(0)) + w
        for e in (missing if missing else range(n)):
            tprob = w/F(m if m else n)
            tree_marginal[e] += tprob
            if m == 1:
                tree_event[e] += w
        cost += w * abs(m-1)
    assert sum(weights_by_m.values()) == 1; checks += 1
    assert all(v == F(1, n) for v in tree_marginal); checks += n
    assert weights_by_m.get(0, F(0)) == p**n+q**n; checks += 1
    assert weights_by_m.get(1, F(0)) == n*sum((p**j)*(q**(n-j)) for j in range(1,n)); checks += 1
    assert all(t == weights_by_m.get(1, F(0))/n for t in tree_event); checks += n
    exp_m = sum(m*w for m,w in weights_by_m.items())
    assert exp_m == n*p*q; checks += 1
    assert cost == n*p*q - 1 + 2*(p**n+q**n); checks += 1
    assert 1-weights_by_m.get(1,F(0)) == 1-n*sum((p**j)*(q**(n-j)) for j in range(1,n)); checks += 1
    # Distribution of number of missing edges from cyclic runs.
    for m in range(1,n//2+1):
        runs = F(n,m)*sum(F(comb(a-1,m-1)*comb(n-a-1,m-1))
              *p**a*q**(n-a) for a in range(m,n-m+1))
        assert runs == weights_by_m.get(m,F(0)), (n,p,m,runs,weights_by_m.get(m)); checks += 1
    return checks


if __name__ == '__main__':
    ps=[F(0),F(1,10),F(1,6),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(5,6),F(9,10),F(1)]
    total=0
    for n in range(3,11):
        for p in ps:
            total+=confirm(n,p)
    print('PASS:',total,'exact finite checks across 88 (n,p) pairs')
