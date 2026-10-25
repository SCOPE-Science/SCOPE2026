"""Numerical checks for an exact packing-covering theorem on two latitude rings.
This independent finite verifier supports, but does not replace, the analytic proof.
Run with Python 3.10 or later; standard library only.
"""
import itertools
import math


def pointset(n, h):
    r = math.sqrt(1.0 - h*h)
    points = []
    for j in range(n):
        theta = 2*math.pi*j/n
        phi = theta + math.pi/n
        points.extend(((r*math.cos(theta), r*math.sin(theta), h),
                       (r*math.cos(phi), r*math.sin(phi), -h)))
    return points


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def facet_supports(points):
    """Enumerate supporting planes of the convex hull, grouping coplanar triples."""
    faces = {}
    for i, j, k in itertools.combinations(range(len(points)), 3):
        normal = cross(sub(points[j], points[i]), sub(points[k], points[i]))
        norm = math.sqrt(dot(normal, normal))
        if norm < 1e-11:
            continue
        unit = tuple(v/norm for v in normal)
        dist = dot(unit, points[i])
        for orientation in (1.0, -1.0):
            o = tuple(orientation*z for z in unit)
            d = orientation*dist
            if d < -1e-8:
                continue
            if all(dot(o, v) <= d + 2e-9 for v in points):
                faces[tuple(round(x, 8) for x in o)] = d
                break
    return list(faces.values())


def analytic(n, h):
    c = math.cos(math.pi/n)
    s = math.sqrt(1-h*h)
    side = s*(1+c)*h/math.sqrt(4*h*h+s*s*(1-c)**2)
    return min(h, side)


def pack(n, h):
    s = math.sqrt(1-h*h)
    alpha = math.pi/n
    return min(2*s*math.sin(alpha),
               math.sqrt(4*h*h + 4*s*s*math.sin(alpha/2)**2))


count = 0
for n in (3, 4, 5, 6, 9, 13):
    c = math.cos(math.pi/n)
    cover = math.sqrt(c/(1+c))
    delta = math.sin(math.pi/n)**2 - math.sin(math.pi/(2*n))**2
    packing = math.sqrt(delta/(1+delta))
    assert cover >= packing - 1e-12
    if n == 3:
        assert abs(cover-packing) < 1e-12
    else:
        assert cover > packing
    for h in (packing, 0.7*cover, cover, 0.5*(1+cover)):
        pts = pointset(n, h)
        values = facet_supports(pts)
        actual = min(values)
        predicted = analytic(n, h)
        assert abs(actual-predicted) < 1e-8, (n, h, actual, predicted)
        multiplicity = sum(abs(v-actual) < 1e-8 for v in values)
        expected = 2 if h < cover - 1e-9 else (2*n if h > cover+1e-9 else 2*n+2)
        assert multiplicity == expected, (n, h, multiplicity, expected)
        pair_min = min(math.dist(a, b) for a, b in itertools.combinations(pts, 2))
        assert abs(pair_min-pack(n,h)) < 1e-9
        count += 1
    for i in range(1, 200):
        h = i/200
        assert analytic(n,h) <= cover + 1e-12
        assert pack(n,h) <= pack(n,packing) + 1e-12
        count += 2

print('PASSED: {} independent numerical facet/packing and optimum checks'.format(count))
print('sample n, packing height, covering height, covering cosine')
for n in (3,4,5,8,12):
    c=math.cos(math.pi/n)
    d=math.sin(math.pi/n)**2-math.sin(math.pi/(2*n))**2
    hp=math.sqrt(d/(1+d)); hc=math.sqrt(c/(1+c))
    print(n, '{:.12f}'.format(hp), '{:.12f}'.format(hc), '{:.12f}'.format(hc))
