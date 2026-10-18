"""Standalone finite-periodic checks for the two-periodic affine-spline slope law.

Requires only Python 3 standard library. Finite tests do not prove the infinite theorem.
"""
import math


def short_edge_constant(r):
    assert r > 0
    s = 3*r*r + 8*r + 3
    q = 2*r / (s + math.sqrt(s*s - 4*r*r))
    d = 2*(1+r)
    beta = (r+q)/d
    u = d / (d*(d-1) - r*(r+q))
    f = 3*u + 6*u/(1-q) * (r*(1+beta*beta)/(1+beta)
                              + (beta*beta+q*q)/(beta+q))
    assert abs(r*q*q - s*q + r) < 1e-10*(1+r*r)
    return f


def finite_periodic_edge_norms(r, n=24):
    assert n >= 6 and n % 2 == 0 and r > 0
    h = [1.0 if i % 2 == 0 else r for i in range(n)]
    mass = [[0.0]*n for _ in range(n)]
    for i in range(n):
        mass[i][i] = (h[i-1]+h[i])/3.0
        mass[i][(i+1) % n] += h[i]/6
        mass[(i+1) % n][i] += h[i]/6
    augmented = [mass[i] + [float(j==i) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = augmented[i][i]
        assert pivot > 0.0
        augmented[i] = [x/pivot for x in augmented[i]]
        for k in range(n):
            if k == i: continue
            t = augmented[k][i]
            if t:
                augmented[k] = [a-t*b for a,b in zip(augmented[k],augmented[i])]
    inverse = [row[n:] for row in augmented]
    norms = []
    for edge in (0,1):
        coeff = [inverse[(edge+1)%n][j]-inverse[edge][j] for j in range(n)]
        total = 0.0
        for j in range(n):
            a,b = coeff[j],coeff[(j+1)%n]
            if a*b >= 0:
                total += h[j]*(abs(a)+abs(b))/2
            else:
                total += h[j]*(a*a+b*b)/(2*(abs(a)+abs(b)))
        norms.append(total/h[edge])
    return norms


def main():
    ratios = (0.1,0.5,1.0,1.1,1.2,1.5,2.0,3.0,10.0)
    for r in ratios:
        c1 = short_edge_constant(r)
        cr = short_edge_constant(1/r)/r
        measured = finite_periodic_edge_norms(r)
        for actual,predicted in zip(measured,(c1,cr)):
            assert abs(actual-predicted) < 2e-6, (r,actual,predicted)
    base = (9-math.sqrt(3))/2
    two = 65/14-math.sqrt(105)/10
    assert abs(short_edge_constant(1)-base) < 1e-12
    assert abs(short_edge_constant(2)-two) < 1e-12
    assert short_edge_constant(1.1)>base>short_edge_constant(2)
    assert short_edge_constant(2)>short_edge_constant(.5)/2
    eps=1e-5
    gradient=(short_edge_constant(1+eps)-short_edge_constant(1-eps))/(2*eps)
    assert abs(gradient-(2-math.sqrt(3))/8)<1e-7
    print('PASS: 18 independent period-24 edge comparisons; exact special values, inequalities, and derivative consistency.')

if __name__=='__main__':
    main()
