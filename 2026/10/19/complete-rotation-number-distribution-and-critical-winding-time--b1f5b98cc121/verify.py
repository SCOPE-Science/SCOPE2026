"""Finite numerical cross-checks of the square-map polygon-area identities.

Uses only Python's standard library. These checks do not establish the theorem
for arbitrarily many polygons or unbounded winding times.
"""
import math


def matrix(delta):
    t = 0.5 - delta
    s = math.sqrt(t * (1 - t))
    d = t - s
    return t, s, (( (t*t-(1-s)**2)/d, (1-2*s)*t/d),
                  ((2*s-1)*t/d, (2*t-1)*t/d))


def mul(m, z):
    return (m[0][0]*z[0]+m[0][1]*z[1],
            m[1][0]*z[0]+m[1][1]*z[1])


def delta_k(k):
    def residual(delta):
        t, s, b = matrix(delta)
        z = (t, 1 - s)
        for _ in range(k):
            z = mul(b, z)
        return z[0] - s
    a, c = .45 / k, min(.49, 1.6 / k)
    assert residual(a) * residual(c) < 0
    fa = residual(a)
    for _ in range(65):
        m = (a + c) / 2
        fm = residual(m)
        if fm * fa > 0:
            a, fa = m, fm
        else:
            c = m
    return (a + c) / 2


def rot(z):
    return (1 - z[1], z[0])


def det(a, b):
    return a[0]*b[1]-a[1]*b[0]


def polygon(k, n):
    t, s, b = matrix(delta_k(k))
    q = 1.0 / (1 + n*(1-2*s))
    v = [(t, 1-s)]
    for _ in range(k):
        v.append(mul(b, v[-1]))
    assert max(abs(v[-1][i] - (s,t)[i]) for i in range(2)) < 1e-9
    vertices = []
    for turn in range(4):
        for vertex in v:
            z = (q*vertex[0], q*vertex[1])
            for _ in range(turn):
                z = rot(z)
            vertices.append(z)
    poly_area = .5*sum(det(vertices[i],vertices[(i+1)%len(vertices)])
                         for i in range(len(vertices)))
    h = sum(det(v[j], v[j+1]) for j in range(k)) + v[k][0]*v[0][0] + v[k][1]*v[0][1]
    formula_area = 1-4*t*q+2*h*q*q
    return poly_area, formula_area, t, s, h


def main():
    count=0
    for k in (3,4,5,7,10,20):
        for n in (0,1,2,7,30,100):
            geometric, algebraic, t,s,h = polygon(k,n)
            assert abs(geometric-algebraic) < 4e-9, (k,n,geometric,algebraic)
            assert 0 < geometric < 1
            count += 1
    _, _, t,s,h = polygon(3,0)
    assert abs(t-(2-math.sqrt(2))/4)<1e-11
    assert abs(h-(5*math.sqrt(2)-7)/4)<1e-10
    d=1-2*s
    w=4*t-2*h
    assert abs(w-(11-7*math.sqrt(2))/2)<1e-10
    assert abs(16*t/d-8)<1e-10
    for k in (10,20,50,100):
        t,s,_=matrix(delta_k(k))
        c=16*t/(1-2*s)
        assert abs(c-(4*k*k-32*k/3+128/45))<4, (k,c)
    print('VERIFY_OK',count)


if __name__ == '__main__':
    main()
