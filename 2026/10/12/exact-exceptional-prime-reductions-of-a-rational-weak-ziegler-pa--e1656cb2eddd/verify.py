"""Exact rational and modular incidence verification for two plane conic-line arrangements.

Run: python3 verify_weak_pair_reductions.py
Dependencies: Python >=3.9 standard library only.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd, isqrt

LINES_1 = (
    (1, 0, -4), (1, 0, 4), (3, 4, 0),
    (1, 0, 3), (6, 1, 21), (0, 1, 3),
)
LINES_2 = (
    (1, 0, 4), (1, 0, 0), (1, 0, -4),
    (0, 1, -3), (0, 1, 3), (3, -4, 0),
)


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def primitive(p):
    p = [Fraction(z) for z in p]
    from math import lcm
    denominator = lcm(*(z.denominator for z in p))
    p = [int(z*denominator) for z in p]
    k = reduce(gcd, p)
    assert k > 0
    p = tuple(z//k for z in p)
    return tuple(-z for z in p) if next(z for z in p if z) < 0 else p


def conic_points(line):
    """Find both Q-rational intersections using [5(1-t²):10t:1+t²]."""
    a, b, c = line
    A, B, C = c-5*a, 10*b, c+5*a
    values = []
    if A:
        disc = B*B - 4*A*C
        assert disc > 0 and isqrt(disc)**2 == disc
        d = isqrt(disc)
        roots = (Fraction(-B+d, 2*A), Fraction(-B-d, 2*A))
        assert roots[0] != roots[1]
        for t in roots:
            n, den = t.numerator, t.denominator
            values.append(primitive((5*(den*den-n*n), 10*n*den, den*den+n*n)))
    else:
        assert B != 0
        t = Fraction(-C, B)
        n, den = t.numerator, t.denominator
        values.append(primitive((5*(den*den-n*n), 10*n*den, den*den+n*n)))
        values.append(primitive((-5, 0, 1)))
    assert len(set(values)) == 2
    for p in values:
        assert sum(line[i]*p[i] for i in range(3)) == 0
        assert p[0]*p[0] + p[1]*p[1] == 25*p[2]*p[2]
    return tuple(values)


def incidence(lines):
    pts = {primitive(cross(a,b)) for a,b in combinations(lines,2)}
    for line in lines:
        pts.update(conic_points(line))
    records = {}
    for pt in pts:
        onlines = tuple(i+1 for i,line in enumerate(lines)
                        if sum(x*y for x,y in zip(line,pt)) == 0)
        onconic = (pt[0]**2 + pt[1]**2 == 25*pt[2]**2)
        assert len(onlines)+onconic >= 2
        records[pt] = (onlines, onconic)
    return records


def prime_factors(n):
    n = abs(int(n))
    out = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def projective_bad_support(vectors):
    support = set()
    for a,b in combinations(vectors,2):
        wedge = cross(a,b)
        content = reduce(gcd,wedge)
        assert content > 0 or all(x == 0 for x in wedge)
        if not any(wedge):
            raise AssertionError('Coincident rational vectors')
        support |= prime_factors(content)
    return support


def mod_projective(point, p):
    v = tuple(int(z) % p for z in point)
    first = next(i for i,z in enumerate(v) if z)
    scale = pow(v[first], -1, p)
    return tuple(z*scale % p for z in v)


def specializations(records,p):
    out = {}
    for pt in records:
        out.setdefault(mod_projective(pt,p),[]).append(pt)
    return out


def finite_profile(lines, p):
    """Independently enumerate every F_p-projective point."""
    components = dict()
    for i,line in enumerate(lines):
        components.setdefault(mod_projective(line,p), []).append(i+1)
    points = [(1,a,b) for a in range(p) for b in range(p)]
    points += [(0,1,a) for a in range(p)] + [(0,0,1)]
    singular = {}
    for point in points:
        hit = tuple(sorted((tuple(indexes) for line,indexes in components.items()
                   if sum(l*x for l,x in zip(line,point)) % p == 0)))
        on_conic = (point[0]**2 + point[1]**2 - 25*point[2]**2) % p == 0
        if len(hit) + on_conic >= 2:
            singular[point] = (hit,on_conic)
    profile = Counter(len(groups) + c for groups,c in singular.values())
    # Conic intersections are rational by conic_points and hence no extra
    # geometric singularities can be hidden in field extensions.
    return components,singular,profile


def check():
    R1,R2 = incidence(LINES_1),incidence(LINES_2)
    assert len(R1)==len(R2)==11
    for R in (R1,R2):
        assert Counter(len(lines)+int(c) for lines,c in R.values()) == {2:6,3:3,4:2}
    assert projective_bad_support(R1) == {2,3,5,7,11}
    assert projective_bad_support(R2) == {2,3,5}
    assert projective_bad_support(LINES_1) == {2,3,7}
    assert projective_bad_support(LINES_2) == {2,3}

    # p=7 merges precisely the two indicated pairs of lines in arrangement 1.
    comps7,S7,profile7 = finite_profile(LINES_1,7)
    assert sorted(sorted(v) for v in comps7.values()) == [[1,4],[2],[3,5],[6]]
    assert len(S7) == 5 and profile7 == {2:2,3:2,4:1}
    assert len(specializations(R1,7)) == 5
    for line in LINES_1:
        q,r = conic_points(line)
        assert mod_projective(q,7) != mod_projective(r,7)
    # The other arrangement is stable even at characteristic 7.
    comps7b,S7b,prof7b = finite_profile(LINES_2,7)
    assert len(comps7b)==6 and len(S7b)==11
    assert prof7b == {2:6,3:3,4:2}

    # p=11 leaves six distinct lines but produces one tangent conic-line pair.
    comps11,S11,profile11 = finite_profile(LINES_1,11)
    assert len(comps11)==6 and len(S11)==10
    assert profile11 == {2:5,3:3,4:2}
    assert len(specializations(R1,11)) == 10
    tangent = mod_projective((4,-3,-1),11)
    assert tangent == mod_projective((104,153,-37),11)
    line_5 = tuple(v%11 for v in LINES_1[4])
    gradient = tuple(v%11 for v in (2*tangent[0],2*tangent[1],-50*tangent[2]))
    assert mod_projective(line_5,11) == mod_projective(gradient,11)
    assert len(S11[tangent][0]) == 3 and S11[tangent][1]
    # All remaining line/conic intersections are transverse.
    for k,line in enumerate(LINES_1):
        pair = conic_points(line)
        coincide = (mod_projective(pair[0],11)==mod_projective(pair[1],11))
        assert coincide == (k==4)
    comps11b,S11b,prof11b = finite_profile(LINES_2,11)
    assert len(comps11b)==6 and len(S11b)==11
    assert prof11b == {2:6,3:3,4:2}

    # Spot-check further characteristics independently; exact support above
    # proves the all-prime statements, rather than these finite samples.
    for p in (13,17,19,23,29):
        for lines in (LINES_1,LINES_2):
            components,singular,profile = finite_profile(lines,p)
            assert len(components)==6 and len(singular)==11
            assert profile == {2:6,3:3,4:2}
    print('VERIFY_OK: rational intersection lists, all-prime support, p=7 coalescence, p=11 tangency, and finite-field profiles')
    print('A rational singular points:')
    for point in sorted(R1):print(point,R1[point])
    print('B rational singular points:')
    for point in sorted(R2):print(point,R2[point])

if __name__=='__main__':
    check()
