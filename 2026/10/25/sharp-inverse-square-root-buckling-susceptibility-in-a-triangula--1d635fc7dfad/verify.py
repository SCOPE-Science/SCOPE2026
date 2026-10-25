"""Finite regression checks for the triangular-crystal soft-mode asymptotic.

Run: python3 verify.py
Uses only Python's standard library. Numerical grids are diagnostic, not proofs.
"""
from math import cos, pi, sqrt, isclose
from random import Random


def invariants(k1, k2):
    return (1.0 - cos(k1), 1.0 - cos(k2), 1.0 - cos(k2 - k1))


def exact_trace_inverse(k1, k2, delta):
    a, b, c = invariants(k1, k2)
    det = (8.0 / 3.0) * a * b * c + 4 * delta * (a*a+b*b+c*c) + 3 * delta*delta * (a*b+b*c+c*a)
    trace = 2.0 * (2.0 / 3.0 + delta) * (a+b+c)
    return trace / det


def direct_matrix(k1, k2, delta):
    a, b, c = invariants(k1, k2)
    B = -1.0 / 3.0 + delta
    d11 = 2.0 * (a + (1.0+3.0*B) * (b+c) / 4.0)
    d22 = 2.0 * (B*a + (3.0+B)*(b+c)/4.0)
    d12 = (1.0-B)*sqrt(3.0)*(b-c)/2.0
    return d11, d22, d12


def quad(n, delta):
    phases = [(j+0.5)*2*pi/n for j in range(n)]
    vsum = bsum = csum = asum = 0.0
    for u in phases:
        a = 1.0-cos(u)
        for v in phases:
            b = 1.0-cos(v)
            c = 1.0-cos(v-u)
            numerator = 2.0*a * (2.0*(2.0/3.0+delta)*(a+b+c))
            den = (8.0/3.0)*a*b*c+4*delta*(a*a+b*b+c*c)+3*delta*delta*(a*b+b*c+a*c)
            value = numerator/den
            vsum += value
            bsum += value*cos(v)
            csum += value*cos(v-u)
            asum += value*cos(u)
    scale = sqrt(delta)/(n*n)
    return tuple(scale*x for x in [vsum, bsum, csum, asum])


def main():
    count = 0
    rng = Random(20251201)
    for _ in range(600):
        u, v = rng.random()*2*pi, rng.random()*2*pi
        delta = 10**(-4*rng.random())
        a,b,c = invariants(u,v)
        assert isclose(a*a+b*b+c*c-2*(a*b+b*c+c*a), -2*a*b*c, abs_tol=2e-14)
        count += 1
        m11,m22,m12=direct_matrix(u,v,delta)
        den=m11*m22-m12*m12
        det_known=(8/3)*a*b*c+4*delta*(a*a+b*b+c*c)+3*delta*delta*(a*b+b*c+c*a)
        assert isclose(den,det_known,rel_tol=1e-9,abs_tol=2e-13)
        assert isclose((m11+m22)/den,exact_trace_inverse(u,v,delta),rel_tol=1e-9,abs_tol=2e-10)
        count += 2
    target = 2*sqrt(2/3)
    for delta, tolerance in [(1e-3, .11), (1e-4, .04)]:
        total, cos_b, cos_c, cos_a = quad(900,delta)
        assert abs(total-target)<tolerance, (delta,total,target)
        assert abs(cos_b-sqrt(2/3))<tolerance*1.3, (delta,cos_b)
        assert abs(cos_c-sqrt(2/3))<tolerance*1.3, (delta,cos_c)
        assert abs(cos_a)<tolerance*1.3, (delta,cos_a)
        count += 4
        print(f'delta={delta:g}, sqrt(delta)*V={total:.9f}, target={target:.9f}, cos(k2)={cos_b:.9f}')
    print(f'{count} deterministic checks passed')

if __name__=='__main__':
    main()
