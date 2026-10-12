"""Finite-field consistency checks for the cyclic Frobenius-quadric theorem.

The proof for all primes and all geometric points is in RESULT.md;
this program tests specified small-prime cases exactly.
"""
from itertools import product
from math import comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def rem(a, b, p):
    a, b = trim(a[:]), trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, p) % p
        for i, d in enumerate(b):
            a[i + k] = (a[i + k] - c*d) % p
        trim(a)
    return a


def gcd(a, b, p):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, rem(a, b, p)
    v = pow(a[-1], -1, p)
    return [(v*c) % p for c in a]


def infinity_repeated_factor(p):
    # H(t) = t^(p-1) + t^(2p-1) - t^p - (1+t)^(p-1).
    h = [0] * (2*p)
    for k in range(p):
        h[k] = (-comb(p-1, k)) % p
    for n, coeff in ((p-1, 1), (2*p-1, 1), (p, -1)):
        h[n] = (h[n] + coeff) % p
    d = [(i*h[i]) % p for i in range(1, len(h))]
    return gcd(h, d, p)


def quadratic(w,x,y,z,p):
    return (w*w + x*y + y*z + z*x) % p


def surface(w,x,y,z,p):
    return (pow(w,p+1,p) + x*pow(y,p,p) + y*pow(z,p,p) + z*pow(x,p,p)) % p


def gradients(w,x,y,z,p):
    return [pow(w,p,p),pow(y,p,p),pow(z,p,p),pow(x,p,p)], \
           [(2*w)%p,(y+z)%p,(z+x)%p,(x+y)%p]


def singular(point,p):
    a,b=gradients(*point,p)
    return all((a[i]*b[j]-a[j]*b[i])%p==0
               for i in range(4) for j in range(i+1,4))


def projective_points(p):
    for k in range(4):
        for tail in product(range(p), repeat=3-k):
            yield (0,)*k + (1,) + tail


def tangent_isotropic_directions(point,p):
    # In a normalized affine chart, count isotropic tangent directions.
    fixed = next(i for i,a in enumerate(point) if a)
    grad = gradients(*point,p)[1]
    free = [i for i in range(4) if i != fixed]
    pts=[]
    for a in projective_points(p):
        if len(a)!=4:
            continue
        # Representative of projective directions in the 3-d affine chart.
        if a[fixed] != 0:
            continue
        if sum(grad[i]*a[i] for i in range(4))%p:
            continue
        if quadratic(*a,p) != 0:
            continue
        pts.append(a)
    return len(pts)


def run():
    for p in (5,7,11,13,17,19):
        pts = [t for t in projective_points(p) if quadratic(*t,p)==0]
        assert len(pts)==(p+1)**2, (p,len(pts))
        assert all(surface(*t,p)==0 for t in pts)
        s = [t for t in pts if singular(t,p)]
        expected = 4 if p%3==1 else 0
        assert len(s)==expected, (p,s)
        for pt in s:
            assert tangent_isotropic_directions(pt,p)==2, (p,pt)
        g = infinity_repeated_factor(p)
        expected_g = [1,1,1] if p%3==1 else [1]
        assert g==expected_g, (p,g)
        print(f'p={p} rational={len(pts)} rational_nodes={len(s)} infinity_gcd={g}')
    print('FROBENIUS_QUADRIC_EXACT_OK')

if __name__ == '__main__':
    run()
