"""Independent finite checks for affine projection on area-uniform regular polygons.

Run with Python 3 standard library: python verify.py
The asymptotic theorem is proved analytically; these computations test instances only.
"""
import math


def moment_polygon(vertices):
    twice_area = moment6 = 0.0
    for (x, y), (u, v) in zip(vertices, vertices[1:] + vertices[:1]):
        cross = x * v - u * y
        twice_area += cross
        moment6 += (x + u) * cross
    return twice_area / 2.0, moment6 / 6.0


def left_cap(vertices, cutoff):
    out = []
    for (x, y), (u, v) in zip(vertices, vertices[1:] + vertices[:1]):
        if x <= cutoff:
            out.append((x, y))
        if (x - cutoff) * (u - cutoff) < 0:
            z = (cutoff - x) / (u - x)
            out.append((cutoff, y + z * (v - y)))
    return out


def exact_polygon_geometry(n):
    assert isinstance(n, int) and n >= 3
    verts = [(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n))
             for j in range(n)]
    h = math.pi/n
    kappa = 12/(1 + 2*math.cos(h)**2)
    area, _ = moment_polygon(verts)
    cap_area, cap_xmoment = moment_polygon(left_cap(verts, -1/kappa))
    return 1-2*(cap_area+kappa*cap_xmoment)/area


def radial_angular_integral(n, subdivisions_per_side=1000):
    """Independent polar cubature, not using planar polygon clipping."""
    assert subdivisions_per_side % 2 == 0
    h = math.pi/n
    kappa = 12/(1+2*math.cos(h)**2)
    cellwidth = 2*h
    step = cellwidth/subdivisions_per_side
    total = 0.0
    for j in range(n):
        normal = (2*j+1)*h
        summand = 0.0
        for k in range(subdivisions_per_side+1):
            delta = -h + k*step
            phi = normal+delta
            radius = math.cos(h)/math.cos(delta)
            a = kappa*math.cos(phi)
            radial = radius**2/2 + a*radius**3/3
            if a < 0 and -1/a < radius:
                zero = -1/a
                # Integral of |(1+a*r)r|, with one sign change at zero.
                negative_tail = (radius**2-zero**2)/2 + a*(radius**3-zero**3)/3
                radial -= 2*negative_tail
            weight = 1 if k in (0, subdivisions_per_side) else (4 if k%2 else 2)
            summand += weight*radial
        total += summand *step/3
    area = n*math.sin(2*h)/2
    return total/area


def disk_norm():
    return (16*math.asin(1/4)+11*math.sqrt(15))/(8*math.pi)


def main():
    assertions = 0
    for n, rational in [(3, 19/8), (4, 233/108), (6, 361/180)]:
        assert abs(exact_polygon_geometry(n)-rational)<1e-12
        assertions += 1
    for n in (3,4,5,6,7,8,9,10,11,12,15,17,20,25,30,40):
        geometry = exact_polygon_geometry(n)
        independent = radial_angular_integral(n, 1000)
        assert abs(geometry-independent) < 2e-7, (n, geometry, independent)
        assertions += 1
    coefficient = 5*math.pi*math.sqrt(15)/12
    for n in (80,100,120,160,240,320,480):
        scaled = n*n*(exact_polygon_geometry(n)-disk_norm())
        assert abs(scaled-coefficient)<0.006, (n, scaled, coefficient)
        assertions += 1
    print(f"PASS: {assertions} independent finite comparisons")
    print(f"Disk norm: {disk_norm():.15f}")
    print(f"Sharp n^-2 coefficient: {coefficient:.15f}")


if __name__ == '__main__':
    main()
