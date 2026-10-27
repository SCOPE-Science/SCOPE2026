#!/usr/bin/env python3
"""Finite independent checks for chromatic repair on friendship graphs.
Each source is an arbitrary word; the repair is optimized by trying the two
proper orientations on every triangle blade. No external packages needed.
"""
from itertools import product


def distance_to_proper(word, hub_color):
    m = (len(word) - 1) // 2
    others = [c for c in range(3) if c != hub_color]
    a, b = others
    changes = int(word[0] != hub_color)
    for j in range(m):
        x, y = word[2*j+1], word[2*j+2]
        changes += min((x != a) + (y != b),
                       (x != b) + (y != a))
    return changes


def expected(m):
    fixing = m + (m+2)//3
    if m == 1:
        return 0, 0, fixing
    ordinary = m+1
    weak = m if m in (2,3) else m+1
    return ordinary, weak, fixing


def brute(m):
    ordinary = weak = fixing = 0
    count_all = count_legal = 0
    for w in product(range(3), repeat=2*m+1):
        d = [distance_to_proper(w, c) for c in range(3)]
        fixing = max(fixing, min(d))
        count_all += 1
        if m == 1:
            # Every word of profile (1,1,1) is already a proper K3 coloring.
            if sorted(w.count(c) for c in range(3)) == [1,1,1]:
                ordinary = max(ordinary, min(d))
                weak = max(weak, min(d))
                count_legal += 1
        elif w.count(0)==1 and w.count(1)==m and w.count(2)==m:
            # A repaired coloring of the same profile must use singleton
            # color zero on the common vertex.
            ordinary = max(ordinary, d[0])
            weak = max(weak, min(d))
            count_legal += 1
    assert (ordinary, weak, fixing) == expected(m), (m, ordinary, weak, fixing, expected(m))
    return count_all, count_legal


def construction_checks():
    for m in range(2,101):
        k = m//2
        if m % 2 == 0:
            # center 1, special 0-1, (k-1) blades 1-1, k blades 2-2
            w = (1, 0, 1) + (1,1)*(k-1) + (2,2)*k
        else:
            # center 1, special 0-2, k blades 1-1, k blades 2-2
            w = (1, 0, 2) + (1,1)*k + (2,2)*k
        assert len(w) == 2*m+1
        assert [w.count(c) for c in range(3)] == [1,m,m]
        d = [distance_to_proper(w,c) for c in range(3)]
        assert d[0] == m+1
        if m >= 4:
            assert min(d) == m+1
        t = (m+2)//3
        a = [t, t-1, m-2*t+1]
        assert min(a) >= 0 and sum(a) == m
        z = (0,) + (0,0)*a[0] + (1,1)*a[1] + (2,2)*a[2]
        assert min(distance_to_proper(z,c) for c in range(3)) == m+t
        # In triple repetition, cyclic colour relabellings make every global
        # colour occur 2m+1 times, a feasible proper colouring profile.
        tripled = [tuple((x+s)%3 for x in z) for s in range(3)]
        assert all(sum(w.count(c) for w in tripled) == 2*m+1 for c in range(3))
        assert sum(min(distance_to_proper(w,c) for c in range(3)) for w in tripled) == 3*(m+t)


def main():
    allwords = legal = 0
    for m in range(1,7):
        a,b = brute(m)
        allwords += a
        legal += b
    construction_checks()
    print(f'VERIFY_OK m=1..6 all_words={allwords} legal_words={legal} construction_m=2..100')

if __name__ == '__main__':
    main()
