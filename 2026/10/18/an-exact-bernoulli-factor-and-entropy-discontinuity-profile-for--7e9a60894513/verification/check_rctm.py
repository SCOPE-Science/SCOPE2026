#!/usr/bin/env python3
"""Exact rational finite-cylinder tests for the scaled modulo-tent map.

The analytical proof is independent of these finite tests.
"""
from fractions import Fraction as Q
from itertools import product
from math import log


def parameters(mu):
    assert mu > 2
    k = (mu / 2).__floor__()
    theta = mu / 2 - k
    assert 0 < theta < 1
    return k, theta


def branches(mu):
    k, theta = parameters(mu)
    # Each branch is an affine inverse: x = a*t+b on t in (0,1).
    res = []
    for side in (0, 1):
        for j in range(k):
            a = Q(1) / mu
            b = Q(j) / mu
            if side:
                a, b = -a, 1 - b
            res.append((side, j, a, b))
        a = theta / mu
        b = Q(k) / mu
        if side:
            a, b = -a, 1 - b
        res.append((side, k, a, b))
    return res


def map_direct(mu, x):
    k, theta = parameters(mu)
    y = min(x, 1-x)
    t = (mu*y) % 1
    return t / theta if y >= Q(k)/mu else t


def test(mu, max_depth):
    k, theta = parameters(mu)
    bs = branches(mu)
    assert len(bs) == 2*(k+1)
    assert sum(abs(a) for _,_,a,_ in bs) == 1
    assert sum(abs(a) for side,_,a,_ in bs if side==0) == Q(1,2)
    assert sum(abs(a) for side,_,a,_ in bs if side==1) == Q(1,2)
    direct_checks = 0
    for side, j, a, b in bs:
        for t in (Q(1,7), Q(2,7), Q(5,7)):
            x = a*t + b
            assert (x < Q(1,2)) == (side==0)
            assert map_direct(mu, x) == t, (mu, side,j,a,b,x,t,map_direct(mu,x))
            direct_checks += 1
    total = 0
    for n in range(1,max_depth+1):
        totals = {word:Q(0) for word in product((0,1),repeat=n)}
        # Cylinder inverse composition; each word's interval length is
        # product of inverse slopes because every branch covers full [0,1].
        for seq in product(bs, repeat=n):
            word = tuple(b[0] for b in seq)
            # Construct an actual interior orbit realizing the symbolic word.
            x = Q(1,2)
            for _, _, a, b in reversed(seq):
                x = a*x+b
            t = x
            for side, _, _, _ in seq:
                assert int(t >= Q(1,2)) == side, (mu, n, word, t)
                t = map_direct(mu, t)
            measure = Q(1)
            for _,_,a,_ in seq:
                measure *= abs(a)
            totals[word] += measure
            total += 1
        assert all(v == Q(1,2**n) for v in totals.values()), (mu,n,totals)
    h = log(float(mu)) - (2*float(theta)/float(mu))*log(float(theta))
    hs = log(2*(k+1))
    assert log(2) < h < hs
    return dict(mu=str(mu),k=k,theta=str(theta),exact_cylinders_through=max_depth,
                branch_sequences_checked=total, inverse_checks=direct_checks,
                metric_entropy=h, branch_entropy=hs)


def main():
    tests = [(Q(9,4),4),(Q(5,2),4),(Q(3,1),4),(Q(11,3),4),
             (Q(17,4),4),(Q(79,10),3),(Q(201,10),2)]
    checks = [test(mu,n) for mu,n in tests]
    for item in checks:
        print(item)
    print('PASS',sum(x['branch_sequences_checked'] for x in checks),'exact rational cylinder contributions;',
          sum(x['inverse_checks'] for x in checks),'exact source-map inverse identities.')

if __name__=='__main__':
    main()
