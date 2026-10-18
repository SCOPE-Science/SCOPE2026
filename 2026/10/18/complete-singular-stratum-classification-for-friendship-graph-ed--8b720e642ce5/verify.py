"""Exact finite verification for normal fans of friendship-graph edge polytopes.

Requires only the Python standard library. For t=2,3,4, enumerates all
nonempty faces by intersections of facet vertex sets, detects nonsimple
normal cones, and compares the maximal singular face list with the three
closed-form families. Also checks integral smoothness for every simple
cone when t=2,3 by gcd of full-rank lattice minors.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb, gcd


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    h, w, rr = len(a), len(a[0]), 0
    for c in range(w):
        pivot = next((i for i in range(rr, h) if a[i][c]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        s = a[rr][c]
        a[rr] = [x/s for x in a[rr]]
        for i in range(rr+1, h):
            q = a[i][c]
            if q:
                a[i] = [v-q*u for v,u in zip(a[i],a[rr])]
        rr += 1
        if rr == h:
            break
    return rr


def determinant(rows):
    n = len(rows)
    if not n:
        return 1
    a = [[Fraction(x) for x in row] for row in rows]
    det = Fraction(1)
    for c in range(n):
        pivot = next((r for r in range(c,n) if a[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c],a[pivot] = a[pivot],a[c]
            det = -det
        x = a[c][c]
        det *= x
        for r in range(c+1,n):
            q = a[r][c]/x
            if q:
                for j in range(c+1,n):
                    a[r][j] -= q*a[c][j]
                a[r][c] = 0
    assert det.denominator == 1
    return int(det)


def saturated(rows, d):
    k = len(rows)
    if k == 0:
        return True
    g = 0
    for cols in combinations(range(d), k):
        g = gcd(g, determinant([[row[c] for c in cols] for row in rows]))
        if g == 1:
            return True
    return g == 1


def solve(t):
    d = 2*t
    points = []
    for i in range(t):
        for a,b in ((1,0),(0,1),(1,1)):
            v = [0]*d
            v[2*i:2*i+2] = (a,b)
            points.append(tuple(v))
    facets = []
    def put(label, normal, rhs):
        assert all(sum(a*b for a,b in zip(normal,x)) <= rhs for x in points)
        mask = sum(1<<i for i,x in enumerate(points)
                   if sum(a*b for a,b in zip(normal,x)) == rhs)
        assert mask != 0
        idx = [i for i in range(len(points)) if mask>>i & 1]
        assert rank([[points[j][k]-points[idx[0]][k] for k in range(d)]
                     for j in idx[1:]]) == d-1, (t,label)
        facets.append((label,tuple(normal),mask))
    for j in range(d):
        normal = [0]*d
        normal[j] = -1
        put(('Z',j),normal,0)
    put(('T',),[-1]*d,-1)
    for bits in product((0,1),repeat=t):
        normal = [0]*d
        for i,b in enumerate(bits):
            normal[2*i+b] = 1
        put(('Q',bits),normal,1)
    # Nonempty faces are exactly nonempty intersections of facet faces.
    full = (1<<len(points))-1
    faces = {full}
    for _,_,fm in facets:
        old = tuple(faces)
        faces.update(fm & q for q in old if fm & q)
    # Iterate until stable; the first pass already handles all intersections.
    old_len = -1
    while old_len != len(faces):
        old_len = len(faces)
        for _,_,fm in facets:
            faces.update(fm & q for q in tuple(faces) if fm & q)
    bad = {}
    for fm in faces:
        ix = [i for i in range(len(points)) if fm>>i & 1]
        dim = rank([[points[j][k]-points[ix[0]][k] for k in range(d)]
                    for j in ix[1:]])
        normal = [n for _,n,g in facets if fm & g == fm]
        nr = len(normal)
        assert rank(normal) == d-dim, (t,fm,dim,nr)
        singular = nr > d-dim
        if not singular and t <= 3:
            assert saturated(normal,d), (t,fm,normal)
        if singular:
            bad[fm] = (dim,nr)
    maximal_bad = {fm:bad[fm] for fm in bad
                   if not any(fm != other and fm & other == fm for other in bad)}
    # Candidate singular-component faces, independently from the inequalities.
    candidate = {}
    def pmask(items):
        return sum(1 << (3*i+kind) for i,kind in items)
    for i,j in combinations(range(t),2):
        rem = [k for k in range(t) if k not in (i,j)]
        for bits in product((0,1),repeat=len(rem)):
            items = [(i,2),(j,2)]
            for k,b in zip(rem,bits):
                items.extend(((k,b),(k,2)))
            candidate[pmask(items)] = ('square',3)
    for j in range(t):
        rem = [k for k in range(t) if k != j]
        for bits in product((0,1),repeat=t-1):
            items = [(k,b) for k,b in zip(rem,bits)]
            items.extend((k,2) for k in rem)
            candidate[pmask(items)] = ('flip_zero',3)
    for bits in product((0,1),repeat=t):
        candidate[pmask([(i,b) for i,b in enumerate(bits)])] = ('total_choice',t+1)
    assert set(maximal_bad) == set(candidate), (t, len(maximal_bad),len(candidate),
        [q for q in maximal_bad if q not in candidate][:3],
        [q for q in candidate if q not in maximal_bad][:3])
    for fm,(kind,codim) in candidate.items():
        assert fm in faces and maximal_bad[fm][0] == d-codim
    counts = {kind:sum(1 for typ,_ in candidate.values() if typ==kind)
              for kind in ('square','flip_zero','total_choice')}
    assert counts == {'square':comb(t,2)*2**(t-2),
                      'flip_zero':t*2**(t-1),
                      'total_choice':2**t}
    print('t=%d facets=%d faces=%d maximal_singular=%d types=%s' %
          (t,len(facets),len(faces),len(maximal_bad),counts))

if __name__ == '__main__':
    for t in (2,3,4):
        solve(t)
    print('VERIFY_OK')
