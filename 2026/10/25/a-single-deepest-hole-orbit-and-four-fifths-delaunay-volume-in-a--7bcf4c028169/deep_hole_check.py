#!/usr/bin/env python3
"""Exact rational certificate for deepest Delaunay simplices of an anisotropic D5+ set."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import factorial, prod

W = (Q(1), Q(1), Q(1), Q(1), Q(4,15))
T = (Q(1,2),) * 5
R2 = Q(27,50)
# Coordinates are x_1,x_2,x_3,x_4,z; all inequalities are c dot x <= b.
ROWS = (
    ((0,0,0,0,1),1), ((0,0,0,0,-1),1),
    ((15,15,15,-15,-4),16),
    ((5,5,5,5,-4),8),
    ((15,15,15,15,4),16),
    ((30,0,0,0,-8),19), ((30,0,0,0,8),19),
    ((1,1,0,0,0),1),
    ((-1,1,0,0,0),0),
    ((0,-1,1,0,0),0),
    ((0,0,-1,1,0),0),
    ((0,0,0,-1,0),0),
)


def solve_square(rows, rhs):
    """Unique rational solution, or None for singular systems."""
    n = len(rhs)
    a = [[Q(rows[i][j]) for j in range(n)] + [Q(rhs[i])]
         for i in range(n)]
    for col in range(n):
        pivot = next((k for k in range(col, n) if a[k][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= scale
        for k in range(col + 1, n):
            scale = a[k][col]
            if scale:
                for j in range(col, n + 1):
                    a[k][j] -= scale * a[col][j]
    x = [Q(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] - sum(a[i][j] * x[j] for j in range(i+1, n))
    return tuple(x)


def determinant(rows):
    n = len(rows)
    a = [[Q(t) for t in row] for row in rows]
    sign = 1
    det = Q(1)
    for col in range(n):
        pivot = next((k for k in range(col, n) if a[k][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        p = a[col][col]
        det *= p
        for k in range(col + 1, n):
            factor = a[k][col] / p
            for j in range(col + 1, n):
                a[k][j] -= factor * a[col][j]
            a[k][col] = Q(0)
    return sign * det


def norm2(x):
    return sum(w*a*a for w,a in zip(W,x))


def feasible(x):
    return all(sum(Q(c)*a for c,a in zip(cs,x)) <= b for cs,b in ROWS)


def polytope_vertices():
    found = set()
    invertible = 0
    for subset in combinations(ROWS,5):
        x=solve_square([a for a,b in subset],[b for a,b in subset])
        if x is None:
            continue
        invertible += 1
        if feasible(x):
            found.add(x)
    assert invertible == 455, invertible
    assert len(found) == 41, len(found)
    assert max(map(norm2,found)) == R2
    deep = {x for x in found if norm2(x) == R2}
    assert deep == {
        (Q(11,30),Q(11,30),Q(1,15),Q(0),Q(-1)),
        (Q(11,30),Q(11,30),Q(1,15),Q(0),Q(1)),
        (Q(1,2),Q(13,30),Q(2,15),Q(2,15),Q(-1,2)),
        (Q(19,30),Q(11,30),Q(1,15),Q(0),Q(0)),
    },deep
    return found,deep


def sites_within_box(p):
    # Every site at weighted-square distance <=27/50 lies in this box:
    # the first four coordinate displacements are <1, the fifth <3/2.
    widths = (Q(1),)*4+(Q(3,2),)
    def bounds(offset):
        return [tuple(k for k in range(-4,5)
                      if abs(Q(k)+offset-p[i]) <= widths[i])
                for i in range(5)]
    for offset in (Q(0),Q(1,2)):
        for v in product(*bounds(offset)):
            if sum(v)%2 == 0:
                yield tuple(Q(k)+offset for k in v)


def nearest_sites(p):
    # Points outside the bounding box each have squared distance >27/50.
    good=[]
    for s in sites_within_box(p):
        d=sum(w*(a-b)**2 for w,a,b in zip(W,p,s))
        if d <= R2:
            assert d == R2,(p,s,d)
            good.append(s)
    assert len(good) == 6,(p,len(good),good)
    rows = [[good[j+1][i]-good[0][i] for j in range(5)]
            for i in range(5)]
    assert abs(determinant(rows))==1,(p,rows,determinant(rows))
    return set(good)


def symmetry_orbit(p):
    orbit = set()
    for sigma in permutations(range(4)):
        for eps in product((-1,1),repeat=5):
            if prod(eps)==1:
                orbit.add(tuple(eps[i]*p[sigma[i]] for i in range(4))
                          +(eps[4]*p[4],))
    return orbit


def main():
    # Independently recover the eight non-chamber inequalities as
    # scaled nearest-site bisectors, rather than assuming their provenance.
    witnesses = (
        (Q(0),Q(0),Q(0),Q(0),Q(2)),
        (Q(0),Q(0),Q(0),Q(0),Q(-2)),
        (Q(1,2),Q(1,2),Q(1,2),Q(-1,2),Q(-1,2)),
        (Q(1,2),Q(1,2),Q(1,2),Q(1,2),Q(-3,2)),
        (Q(1,2),Q(1,2),Q(1,2),Q(1,2),Q(1,2)),
        (Q(1),Q(0),Q(0),Q(0),Q(-1)),
        (Q(1),Q(0),Q(0),Q(0),Q(1)),
        (Q(1),Q(1),Q(0),Q(0),Q(0)),
    )
    recovered=[]
    for s in witnesses:
        assert any(s==site for site in sites_within_box((Q(0),)*5)) or (
            # Some valid witnesses lie outside the small origin box.
            all(z.denominator==1 for z in s) and sum(s)%2==0
        ) or (
            all(z.denominator==2 for z in s) and
            sum(z-Q(1,2) for z in s)%2==0
        )
        a=tuple(2*w*z for w,z in zip(W,s))
        b=sum(w*z*z for w,z in zip(W,s))
        recovered.append((a,b))
    for a,b in ROWS[:8]:
        assert any(
            all(Q(c)*rhs==Q(b)*d for c,d in zip(a,alpha))
            for alpha,rhs in recovered
        ),(a,b)
    vertices,deep=polytope_vertices()
    for p in sorted(deep):
        nearest_sites(p)
    h=(Q(11,30),Q(11,30),Q(1,15),Q(0),Q(1))
    j=(Q(1,2),Q(13,30),Q(2,15),Q(2,15),Q(-1,2))
    k=(Q(19,30),Q(11,30),Q(1,15),Q(0),Q(0))
    orbits=[symmetry_orbit(u) for u in (h,j,k)]
    assert all(len(o)==192 for o in orbits)
    assert not (orbits[0]&orbits[1] or orbits[0]&orbits[2]
                or orbits[1]&orbits[2])
    assert all(p in set.union(*orbits) for p in deep)
    assert sum(map(len,orbits))==576
    # The site-transitive isometry group acts via integer D5 translations,
    # signed coordinate permutations of even parity, and x -> t-x.
    # Recenter the six nearest sites to verify that all three 0-cell types
    # belong to the same global isometry orbit.
    image_types = set()
    for s in nearest_sites(h):
        if all(c.denominator==1 for c in s):
            y=tuple(h[i]-s[i] for i in range(5))
        else:
            y=tuple(s[i]-h[i] for i in range(5))
        matched=[i for i,o in enumerate(orbits) if y in o]
        assert len(matched)==1,(s,y,matched)
        image_types.add(matched[0])
    assert image_types == {0,1,2},image_types
    # Every hole touches 6 sites; two sites occupy one fundamental D5 cell.
    holes_per_period = 2*576//6
    assert holes_per_period == 192 and 2*576%6==0
    # The five-dimensional Delaunay simplex at each hole has coordinate
    # determinant one.  sqrt(det H)=2/sqrt(15), det D5=2.
    # Therefore the occupied fraction is (192/120)/2=4/5.
    fraction = Q(holes_per_period,factorial(5)*2)
    assert fraction == Q(4,5)
    print('DEEP_HOLE_CERTIFICATE_OK candidates=4 chamber_vertices=41 invertible=455')
    print('site_stabilizer_orbits=3 orbit_sizes=192,192,192 local_holes=576')
    print('nearest_sites_per_hole=6 determinant_abs=1 global_hole_orbits=1')
    print('holes_per_D5_period=192 Delaunay_volume_fraction=4/5')


if __name__=='__main__':
    main()
