#!/usr/bin/env python3
"""Independent finite tests for the maximum Jordan-block law of tree incidence radicals.
Scientific reproducibility only; uses Python standard library.
"""
from fractions import Fraction
from itertools import product


def regular_tree(b, h):
    par = [-1]
    level = [0]
    last = [0]
    for d in range(1, h + 1):
        nxt = []
        for u in last:
            for _ in range(b):
                nxt.append(len(par))
                par.append(u)
                level.append(d)
        last = nxt
    return par, level


def strict_pairs(par):
    pairs = []
    for v in range(len(par)):
        u = par[v]
        while u != -1:
            pairs.append((u, v))
            u = par[u]
    return sorted(pairs)


def prime_matrix_power(data, pairs, n, h, q):
    A = [[0] * n for _ in range(n)]
    for (i, j), val in zip(pairs, data):
        A[i][j] = val
    B = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(h):
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for k in range(i, n):
                if B[i][k]:
                    for j in range(k + 1, n):
                        if A[k][j]:
                            C[i][j] = (C[i][j] + B[i][k] * A[k][j]) % q
        B = C
    return B


def expected_probability(b, h, q):
    s = Fraction(1)
    t = Fraction(q - 1, q)
    for _ in range(h):
        s = 1 - (1 - t * s)**b
    return s


def run_exhaustive(b, h, q):
    par, _ = regular_tree(b, h)
    pairs = strict_pairs(par)
    count = 0
    for vals in product(range(q), repeat=len(pairs)):
        B = prime_matrix_power(vals, pairs, len(par), h, q)
        nonzero = any(any(x for x in row) for row in B)
        if nonzero:
            count += 1
            # The last power must have exactly one nonzero row and rank one.
            assert not any(any(B[i]) for i in range(1, len(par)))
    expected = expected_probability(b, h, q) * q**len(pairs)
    assert expected.denominator == 1, (b, h, q, expected)
    assert count == expected, (b, h, q, count, expected)
    return len(pairs), count, q**len(pairs)


def run_sample(b, h, q, sample_count=256):
    import random
    r = random.Random(1729 + q*1000 + b*100 + h)
    par, levels = regular_tree(b, h)
    pairs = strict_pairs(par)
    index = {pair: i for i, pair in enumerate(pairs)}
    leaves = [i for i, dep in enumerate(levels) if dep == h]
    for _ in range(sample_count):
        vals = [r.randrange(q) for _ in pairs]
        B = prime_matrix_power(vals, pairs, len(par), h, q)
        nonzero = any(any(x for x in row) for row in B)
        cover_event = False
        for leaf in leaves:
            current = leaf
            all_nonzero = True
            while par[current] != -1:
                all_nonzero &= (vals[index[(par[current], current)]] != 0)
                current = par[current]
            cover_event |= all_nonzero
        assert nonzero == cover_event, (b, h, q, nonzero, cover_event)
        assert not any(any(B[i]) for i in range(1, len(par)))


def nonbalanced_tree_test():
    # Root with two branches: a length-three branch and a length-two branch.
    par = [-1, 0, 0, 1, 3, 2]
    pairs = strict_pairs(par)
    h = 3
    idx = {e: k for k, e in enumerate(pairs)}
    counter = 0
    for vals in product((0,1), repeat=len(pairs)):
        B = prime_matrix_power(vals,pairs,len(par),h,2)
        event = any(any(x for x in row) for row in B)
        assert event == bool(vals[idx[(0,1)]] and vals[idx[(1,3)]] and vals[idx[(3,4)]])
        counter += event
    assert counter*8 == 2**len(pairs), (counter,len(pairs))
    return len(pairs),counter




def field4_mul(a, b):
    c = 0
    for shift in (0, 1):
        if (b >> shift) & 1:
            c ^= a << shift
    for power in (3, 2):
        if (c >> power) & 1:
            c ^= 0b111 << (power - 2)
    return c


def field4_sample():
    import random
    r = random.Random(1919)
    par, levels = regular_tree(2, 3)
    pairs = strict_pairs(par)
    look = {e:i for i,e in enumerate(pairs)}
    leaves = [i for i,dep in enumerate(levels) if dep == 3]
    n = len(par)
    for _ in range(300):
        vals = [r.randrange(4) for _ in pairs]
        A = [[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,vals):
            A[i][j]=v
        B = [[int(i==j) for j in range(n)] for i in range(n)]
        for _ in range(3):
            C = [[0]*n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if B[i][k]:
                        for j in range(n):
                            if A[k][j]:
                                C[i][j] ^= field4_mul(B[i][k],A[k][j])
            B = C
        evt=any(any(row) for row in B)
        cover=False
        for leaf in leaves:
            w=leaf
            nz=True
            while par[w]>=0:
                nz &= vals[look[(par[w],w)]]!=0
                w=par[w]
            cover |= nz
        assert evt==cover
        assert all(not any(B[i]) for i in range(1,n))
    # Check multiplicative closure and nonzero inverses for the finite field.
    assert {field4_mul(2,x) for x in (1,2,3)}=={1,2,3}
    assert {field4_mul(3,x) for x in (1,2,3)}=={1,2,3}

def critical_check():
    s=1.0
    for i in range(1,20001):
        s=1-(1-s/2)**2
    assert abs(20000*s/4-1)<0.005, 20000*s/4


def main():
    stats=[]
    for b,h,q in ((1,3,2),(2,1,2),(2,2,2),(2,1,3),(2,2,3)):
        M,k,n = run_exhaustive(b,h,q)
        stats.append((b,h,q,M,k,n))
    for b,h,q in ((2,3,2),(2,3,3),(3,2,2),(2,2,5)):
        run_sample(b,h,q)
    m,c=nonbalanced_tree_test()
    critical_check()
    field4_sample()
    print('EXHAUSTIVE',stats)
    print('NONBALANCED',m,c)
    print('SAMPLES',4*256+300)
    print('ALL_TREE_INCIDENCE_TOP_JORDAN_CHECKS_PASSED')

if __name__ == '__main__':
    main()
