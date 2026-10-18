"""Independent finite arithmetic diagnostics for the pole--regular-ring Parseval frame.

All analytic claims concerning infinitely many indices are proved separately.
"""
from math import pi, cos, sin, acos, sqrt, floor, isclose


def data(n):
    assert n >= 5
    alpha = acos(-0.25) / (2 * pi)
    r = floor(n * alpha)
    a_direct = sum(abs(1 + 4 * cos(2 * pi * k / n)) for k in range(n)) / n
    a_closed = -1 + (4 * r + 2) / n + (8 / n) * sin((2 * r + 1) * pi / n) / sin(pi / n)
    L = (1 + a_direct + sqrt((1 - a_direct) ** 2 + 4)) / 4
    return a_direct, a_closed, L


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def vectors(n):
    u = [(0, 0, 1 / sqrt(2))]
    u += [(2 * cos(2 * pi * j / n) / sqrt(2*n),
           2 * sin(2 * pi * j / n) / sqrt(2*n),
           1 / sqrt(2*n)) for j in range(n)]
    return u


def test_finite(n):
    a, closed, L = data(n)
    assert abs(a - closed) < 2e-11, (n, a, closed)
    u = vectors(n)
    for k in range(3):
        for l in range(3):
            assert abs(sum(v[k]*v[l] for v in u) - (1 if k == l else 0)) < 1e-12
    absolute = [[abs(dot(x, y)) for y in u] for x in u]
    # Explicit positive Perron eigenvector on pole/ring symmetry sectors.
    t = 2*L - 1
    w = [1.0] + [t / sqrt(n)] * n
    for i, row in enumerate(absolute):
        assert abs(sum(row[j]*w[j] for j in range(n+1)) - L*w[i]) < 1e-10, (n, i)
    # Spherical fourth-moment design test on finitely many nontrivial vectors.
    raw = [(0, 0, 1)] + [(2*cos(2*pi*j/n)/sqrt(5),
                           2*sin(2*pi*j/n)/sqrt(5),
                           1/sqrt(5)) for j in range(n)]
    ww = [1/6] + [5/(6*n)]*n
    for x in [(1,0,0), (0,0,1), (1,2,3), (-2,3,1), (0.25,-0.7,1.4)]:
        lhs = sum(ww[i] * dot(v,x)**4 for i,v in enumerate(raw))
        rhs = dot(x,x)**2 / 5
        assert abs(lhs-rhs) < 3e-11 * max(1,abs(rhs)), (n,x,lhs,rhs)
    return L


def main():
    n_values = [5,6,7,8,9,10,11,12,16,24,50,100,300,600,1000]
    finite = [test_finite(n) for n in n_values]
    assert abs(finite[0] - (1+sqrt(5))/2) < 2e-12
    assert abs(finite[1] - (11+sqrt(61))/12) < 2e-12
    theta=acos(-0.25)
    alpha=theta/(2*pi)
    a_inf=(2*theta+2*sqrt(15))/pi-1
    LL=(1+a_inf+sqrt((1-a_inf)**2+4))/4
    der=(1+(a_inf-1)/sqrt((1-a_inf)**2+4))/4
    C=4*pi*sqrt(15)*der
    for n in (100,300,600,1000):
        observed=n*n*(data(n)[2]-LL)
        t=(n*alpha)%1
        predicted=-C*(t*t-t+1/6)
        assert abs(observed-predicted) < 0.05, (n,observed,predicted)
    print('PASS: frame Parseval, 4-design sample checks, full positive eigenpair,')
    print('      finite trigonometric identity, n=5 and n=6 exact constants,')
    print('      and phase-asymptotic finite diagnostics.')
    print('limit L = %.15f; phase multiplier C = %.15f' % (LL,C))

if __name__ == '__main__':
    main()
