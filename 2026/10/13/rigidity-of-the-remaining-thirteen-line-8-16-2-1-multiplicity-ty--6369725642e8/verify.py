"""Exact incidence check for the thirteen-line cyclotomic arrangement.

This computation verifies selected finite-field reductions. The geometric
classification in characteristic zero follows from the accompanying proof.
"""
from collections import Counter


def normalize(v, p):
    v = tuple(t % p for t in v)
    for t in v:
        if t:
            c = pow(t, -1, p)
            return tuple((c * a) % p for a in v)
    raise AssertionError('zero projective vector')


def cross(u, v, p):
    a, b, c = u
    x, y, z = v
    return normalize((b*z-c*y, c*x-a*z, a*y-b*x), p)


def check(p):
    root = next(g for g in range(2,p) if pow(g,5,p)==1 and g != 1)
    mu5 = [pow(root,k,p) for k in range(5)]
    assert len(set(mu5)) == 5
    A = [(0,1,(-a)%p) for a in mu5 if a != 1]
    B = [(1,0,(-b)%p) for b in mu5 if b != 1]
    C = [(1,(-c)%p,0) for c in mu5]
    lines = A+B+C
    assert len(lines) == 13
    incidences = {}
    for i in range(13):
        for j in range(i+1,13):
            pt = cross(lines[i], lines[j], p)
            incidences.setdefault(pt,set()).update([i,j])
    # Check that each computed point carries exactly the lines listed.
    for pt, ids in incidences.items():
        actual = {i for i,(a,b,c) in enumerate(lines)
                  if (a*pt[0]+b*pt[1]+c*pt[2])%p==0}
        assert actual == ids
    counts = Counter(len(v) for v in incidences.values())
    assert counts == Counter({2:8,3:16,4:2,5:1}), (p,counts)
    row = [sum(i in v for v in incidences.values()) for i in range(13)]
    assert all(x<=6 for x in row)
    assert sorted(row[:8]) == [6]*8
    assert sorted(row[8:]) == [5,6,6,6,6]
    # The four-by-four grid has one direction with four triples,
    # and four directions with three triples.
    triple_by_direction = Counter()
    for a in mu5[1:]:
        for b in mu5[1:]:
            direction = (b*pow(a,-1,p))%p
            triple_by_direction[direction] += 1
    assert sorted(triple_by_direction.values()) == [3,3,3,3,4]
    return counts, row


if __name__ == '__main__':
    for p in (11,31,41):
        check(p)
    print('THIRTEEN_LINE_INCIDENCE_OK')
