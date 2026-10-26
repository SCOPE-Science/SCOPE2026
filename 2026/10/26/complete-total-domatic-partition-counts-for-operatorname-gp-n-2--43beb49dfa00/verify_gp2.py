#!/usr/bin/env python3
"""Exact integer certificate for total-domatic partitions of GP(n,2).

This program uses only the Python standard library.  Its exhaustive finite
computations support the infinite transfer-matrix proof in RESULT.md.
"""
from collections import defaultdict
from itertools import product


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def expected_determinant():
    p20 = [1,-1,1,-4,-5,-8,-9,-13,-17,-22,-42,-22,-17,-13,-9,-8,-5,-4,1,-1,1]
    p24 = [1,-1,5,-8,25,-26,85,-75,172,-145,269,-192,323,-192,269,-145,172,-75,85,-26,25,-8,5,-1,1]
    factors = [[1,0,-4,0,6,0,-4,0,1], [1,0,-2,0,0,0,-1], [1,0,0,0,2,0,-1], p20, p24]
    f = [1]
    for factor in factors:
        f = multiply(f, factor)
    assert len(f) == 65 and f[0] == 1 and f[-1] == 1
    return f


def transfer_edges():
    # A state is four consecutive columns, with each column a binary pair
    # (outer, inner).  An edge appends a fifth column and tests its center.
    edges = []
    for state in range(256):
        cols = [(state >> (2 * (3 - j))) & 3 for j in range(4)]
        next_states = []
        for last in range(4):
            window = cols + [last]
            a = lambda j: window[j] & 1
            b = lambda j: (window[j] >> 1) & 1
            # Neighborhoods of outer vertex i and inner vertex i.
            if 0 < a(1)+a(3)+b(2) < 3 and 0 < a(2)+b(0)+b(4) < 3:
                next_states.append(((state & 63) << 2) | last)
        edges.append(next_states)
    assert sum(map(len, edges)) == 576
    return edges


def traces(edges, limit):
    values = [0] * (limit + 1)
    for root in range(len(edges)):
        current = {root: 1}
        for n in range(1, limit + 1):
            following = defaultdict(int)
            for state, paths in current.items():
                for dest in edges[state]:
                    following[dest] += paths
            current = following
            values[n] += current.get(root, 0)
    return values


def newton_determinant(power_sums):
    # det(I-zT)=sum c_k z^k, with c_k = -(sum_{i=1}^k
    # c_{k-i} trace(T^i))/k.  All quantities are exact integers.
    c = [1]
    for k in range(1, len(power_sums)):
        numerator = sum(c[k-i] * power_sums[i] for i in range(1,k+1))
        assert numerator % k == 0, (k, numerator)
        c.append(-numerator // k)
    return c


def direct_count(n):
    ans = 0
    for mask in range(1 << (2*n)):
        a = [(mask >> i)&1 for i in range(n)]
        b = [(mask >> (n+i))&1 for i in range(n)]
        if all(0 < a[(i-1)%n]+a[(i+1)%n]+b[i] < 3 and
               0 < a[i]+b[(i-2)%n]+b[(i+2)%n] < 3 for i in range(n)):
            ans += 1
    return ans


def three_colour_universal_check():
    # Over F3, a 3-coupon coloring satisfies
    # b_i = -(a_(i-1)+a_(i+1)),
    # a_(i+6)=a_(i+3)-a_(i+4)-a_(i+2)-a_i.
    # The recurrence polynomial is (t-1)^2*(t^4-t^3+t^2-t+1).
    # It divides t^30-1 over F3, so every solution is 30-periodic.
    good=[]
    for initial in product(range(3), repeat=6):
        a=list(initial)
        for i in range(6, 36):
            a.append((a[i-3]-a[i-4]-a[i-2]-a[i-6])%3)
        assert a[:6]==a[30:36]
        a=a[:30]
        b=[(-a[(i-1)%30]-a[(i+1)%30])%3 for i in range(30)]
        if all(a[(i-1)%30]!=a[(i+1)%30] and
               b[(i-2)%30]!=b[(i+2)%30] for i in range(30)):
            good.append((a,b))
    assert len(good)==6
    for a,b in good:
        assert a == b and all(a[i]==a[i%3] for i in range(30))
        assert set(a[:3]) == {0,1,2}
    return len(good)


def main():
    edges = transfer_edges()
    t = traces(edges, 256)
    observed = newton_determinant(t)
    expected = expected_determinant()
    assert observed == expected + [0] * (257-len(expected))
    print('DETERMINANT_OK degree=64 states=256 transitions=576 checked_Newton_orders=1..256')
    samples = [12,116,226,1286,2486,5172,13202,23232,48128,121844]
    assert t[5:15] == samples
    print('TRACES_OK A_5..A_14=' + ','.join(map(str,samples)))
    for n in range(5,10):
        actual=direct_count(n)
        assert actual==t[n], (n,actual,t[n])
    print('DIRECT_BRUTE_OK n=5..9 counts=' + ','.join(str(t[n]) for n in range(5,10)))
    assert three_colour_universal_check()==6
    print('THREE_COLOUR_OK 729 initial assignments, six globally admissible 30-periodic sequences')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
