#!/usr/bin/env python3
"""Independent exact chain-incidence enumeration for polygon face-spectrum identities."""
import itertools
from collections import Counter, defaultdict
from math import comb, factorial


def expected(p, q):
    n = p + q
    assert n >= 4 and p >= 1 and q >= 1
    vertices = p*q*factorial(n-2)
    square = comb(n-3, 2)*vertices//4
    assert comb(n-3, 2)*vertices % 4 == 0
    hex_inside = (n-4)*vertices//6
    assert (n-4)*vertices % 6 == 0
    hex_initial = (p*comb(q,3)+q*comb(p,3))*factorial(n-4)
    octagon = comb(p,2)*comb(q,2)*factorial(n-4)
    return Counter({4:square,6:hex_inside+hex_initial,8:octagon})


def enumerate_polygon_spectrum(p,q):
    n = p+q
    colors_a = tuple(range(p)); colors_b = tuple(range(p,n))
    faces = defaultdict(int)
    # Vertex = maximal nested family of connected, convex, proper tubes;
    # the tube chain starts with a pair of unlike colors, then inserts
    # remaining labels in any order.
    for a in colors_a:
        for b in colors_b:
            tail = tuple(x for x in range(n) if x!=a and x!=b)
            for order in itertools.permutations(tail):
                mask = (1<<a)|(1<<b)
                tubes = [mask]
                for x in order[:-1]:
                    mask |= 1<<x
                    tubes.append(mask)
                assert len(tubes) == n-2
                for omitted in itertools.combinations(range(n-2),2):
                    subchain = tuple(t for i,t in enumerate(tubes) if i not in omitted)
                    faces[subchain] += 1
    observed = Counter(faces.values())
    predicted = expected(p,q)
    assert observed == predicted, (p,q,observed,predicted)
    V = p*q*factorial(n-2)
    assert sum(s*count for s,count in observed.items()) == V*comb(n-2,2)
    return len(faces), observed


def main():
    total = 0
    count2 = 0
    for n in range(4,9):
        for p in range(1,n):
            q=n-p
            faces,spectrum=enumerate_polygon_spectrum(p,q)
            total+=1;count2+=faces
            print('OK',p,q, 'polygon_faces',faces,'spectrum',dict(sorted(spectrum.items())))
    print('VERIFY_OK', 'instances',total,'total_polygon_faces',count2)

if __name__=='__main__':
    main()
