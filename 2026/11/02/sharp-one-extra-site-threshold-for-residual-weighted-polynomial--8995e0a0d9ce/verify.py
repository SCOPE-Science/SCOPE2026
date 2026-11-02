"""Exact-rational regression checks for the residual-stencil selectivity theorem.

Run with Python 3 standard library. Finite checks complement the proof.
"""
from fractions import Fraction as F
from math import comb


def interpolate(nodes, values, x):
    total = F(0)
    for j, xj in enumerate(nodes):
        term = F(values[j])
        for k, xk in enumerate(nodes):
            if k != j:
                term *= (x - xk) / (xj - xk)
        total += term
    return total


def outside_residual(xs, f, stencil_indices, outside):
    return F(f[outside]) - interpolate([xs[i] for i in stencil_indices],
                                       [f[i] for i in stencil_indices], xs[outside])


def compact_numerator(xs, indices, target, radius, mu):
    out = F(1)
    for i in indices:
        dist = abs(target-xs[i])
        assert dist > 0 and dist < radius
        out *= (F(1)/dist-F(1)/radius)**mu
    return out


def test():
    num_checks = 0
    # Rank-one identity for all omitted nodes, arbitrary nonequispaced grids.
    for d in range(0, 9):
        n = d+2
        xs = [F(j*j+3*j, 2) for j in range(n)]
        f = [F((j+1)*(j*j+2)-7, j+3) for j in range(n)]
        w = []
        for j, xj in enumerate(xs):
            prod = F(1)
            for i, xi in enumerate(xs):
                if i != j: prod *= xj-xi
            w.append(F(1)/prod)
        global_defect = sum((w[i]*f[i] for i in range(n)), F(0))
        for j in range(n):
            r = outside_residual(xs, f, [i for i in range(n) if i!=j], j)
            assert r == global_defect/w[j]
            num_checks += 1

    # Exact common-residual and nonvanishing compact-Shepard jump response.
    for d in range(1, 12):
        xs = [F(j) for j in range(d+2)]
        left = list(range(d+1)); right = list(range(1,d+2))
        f = [0]*(d+1)+[1]
        L = abs(outside_residual(xs,f,left,d+1))
        R = abs(outside_residual(xs,f,right,0))
        assert L == R == 1
        C = F(comb(2*d,d), 4**d)
        P = interpolate([xs[i] for i in right], [f[i] for i in right], F(1,2))
        assert P == (-1)**d*C
        for mu in range(1, 6):
            WL = compact_numerator(xs,left,F(1,2),F(d+1),mu)
            WR = compact_numerator(xs,right,F(1,2),F(d+1),mu)
            assert WR/WL == F(1,(2*d+1)**(2*mu))
            for eps in [F(1,100000),F(1,8),F(3,2)]:
                for t in [1,2,4]:
                    beta_L = WL/(eps+L)**t
                    beta_R = WR/(eps+R)**t
                    ans = P*beta_R/(beta_L+beta_R)
                    expect = (-1)**d*C/F(1+(2*d+1)**(2*mu))
                    assert ans == expect
                    num_checks += 1

    # One extra node enables opposite strict preferences using endpoint impulses.
    for d in range(0, 12):
        xs = [F(j) for j in range(d+3)]
        left=list(range(d+1)); right=list(range(1,d+2))
        f_first=[1]+[0]*(d+2)
        f_last=[0]*(d+2)+[1]
        assert (abs(outside_residual(xs,f_first,left,d+1)),
                abs(outside_residual(xs,f_first,right,d+2))) == (1,0)
        assert (abs(outside_residual(xs,f_last,left,d+1)),
                abs(outside_residual(xs,f_last,right,d+2))) == (0,1)
        num_checks += 2

    print('VERIFIED', num_checks, 'exact-rational identities')

if __name__ == '__main__':
    test()
