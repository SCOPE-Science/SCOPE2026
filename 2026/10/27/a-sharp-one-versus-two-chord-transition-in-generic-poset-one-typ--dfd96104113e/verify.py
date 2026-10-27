#!/usr/bin/env python3
"""Exact finite tests of the chorded-crown one-type classification."""
from itertools import combinations, product


def fibonacci(limit):
    f = [0, 1]
    for i in range(2, limit + 1):
        f.append(f[-1] + f[-2])
    return f


def incidences(n, chords=()):
    edges = {(i, i) for i in range(n)}
    edges |= {((i + 1) % n, i) for i in range(n)}
    edges |= set(chords)
    return edges


def direct_ideal_and_cross(n, chords=()):
    E = incidences(n, chords)
    lowmask = [sum(1 << i for i in range(n) if (i, j) in E) for j in range(n)]
    highmask = [sum(1 << j for j in range(n) if (i, j) in E) for i in range(n)]
    J = B = 0
    for s in range(1 << n):
        eligible = sum(int(r & s == r) for r in lowmask)
        J += 1 << eligible
        if s:
            common = (1 << n) - 1
            for i in range(n):
                if s >> i & 1:
                    common &= highmask[i]
            B += (1 << common.bit_count()) - 1
    return J, B, 2 * J + B - 1


def direct_state_count(n, chords):
    # Independent 3-valued relational extension enumeration, no ideal formula.
    E = incidences(n, chords)
    pair_rules = []
    for i in range(2*n):
        for j in range(i+1, 2*n):
            if (i, j-n) in E and i < n <= j:
                permitted = {(a,b) for a in (-1,0,1) for b in (-1,0,1)
                             if not (a == 1 and b != 1) and not (b == -1 and a != -1)}
            else:
                permitted = {(a,b) for a in (-1,0,1) for b in (-1,0,1)
                             if (a,b) not in ((-1,1),(1,-1))}
            pair_rules.append((i,j,permitted))
    ans = 0
    for statuses in product((-1,0,1), repeat=2*n):
        if all((statuses[i],statuses[j]) in permitted for i,j,permitted in pair_rules):
            ans += 1
    return ans


def main():
    F = fibonacci(60)
    for n in range(5,14):
        lucas = F[2*n-1] + F[2*n+1]
        one = []
        for k in range(1,n-1):
            J,B,N = direct_ideal_and_cross(n, [(0,k)])
            theo = 2*(lucas-F[2*k]*F[2*(n-k-1)])+4*n+6+int(k in (1,n-2))
            assert N == theo, ('one-chord formula', n,k,N,theo)
            if n <= 6:
                assert direct_state_count(n,[(0,k)]) == N
            one.append(N)
        half = [one[t-1] for t in range(1,(n-1)//2+1)]
        assert all(a > b for a,b in zip(half,half[1:]))
        assert all(one[k-1] == one[n-2-k] for k in range(1,n-1))
        Q = [(0,1),(0,2)]
        R = [(0,1),(0,n-2)]
        j1,b1,t1 = direct_ideal_and_cross(n,Q)
        j2,b2,t2 = direct_ideal_and_cross(n,R)
        assert j1 == j2 == F[2*n+1]+4*F[2*n-5], (n,j1,j2)
        assert b1 == b2 == 4*n+20, (n,b1,b2)
        assert t1 == t2 == 2*F[2*n+1]+8*F[2*n-5]+4*n+19
        if n <= 6:
            assert direct_state_count(n,Q) == t1
            assert direct_state_count(n,R) == t2
        print('n=%d one-chord %s; two-chord twins J=%d B=%d types=%d' %
              (n,one,j1,b1,t1))
    X=[(0,1),(1,3)]
    Y=[(0,1),(2,0)]
    assert direct_ideal_and_cross(4,X)==direct_ideal_and_cross(4,Y)==(41,34,115)
    assert direct_state_count(4,X)==direct_state_count(4,Y)==115
    # For n=3 all three candidate missing incidences form one cyclic orbit,
    # so all two-chord combinations are isomorphic by rotations.
    missing=[(i,j) for i in range(3) for j in range(3)
             if (i,j) not in incidences(3)]
    assert len(missing)==3 and len(list(combinations(missing,2)))==3
    assert len({direct_ideal_and_cross(3,ch)[-1] for ch in combinations(missing,2)})==1
    print('n=4 collision: J=41, B=34, types=115; n=3 all two-chord patterns rotate')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
