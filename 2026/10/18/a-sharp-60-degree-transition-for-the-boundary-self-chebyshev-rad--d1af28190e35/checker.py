"""Reproduce exact rational boundary minimax comparisons for rhombi.

No external packages.  Finite verification supplements the analytic proof;
it is not a proof for continuously many parameters.
"""
from fractions import Fraction as F
from random import Random


def squared_vertex_distances(r, t):
    # Rhombus vertices (sqrt(r),0),(0,1),(-sqrt(r),0),(0,-1).
    # Boundary point (sqrt(r)*(1-t), t), t in [0,1].
    return ((r+1)*t*t, (r+1)*(1-t)**2,
            r*(2-t)**2+t*t, r*(1-t)**2+(1+t)**2)


def exact_minimum(r):
    if r <= 3:
        t = (3*r-1)/(2*(r+1))
        val = (r*r+18*r+1)/(4*(r+1))
    else:
        t = F(1)
        val = r+1
    return t, val


def check():
    rs = [F(1), F(9,8), F(4,3), F(3,2), F(2), F(5,2),
          F(3), F(4), F(11), F(101)]
    rng = Random(20261013)
    checks = 0
    for r in rs:
        t0, value = exact_minimum(r)
        assert 0 <= t0 <= 1
        assert max(squared_vertex_distances(r,t0)) == value
        assert squared_vertex_distances(r,t0)[2] == value
        for t in [F(j, 800) for j in range(801)] + [F(rng.randrange(0, 10**7),10**7) for _ in range(240)]:
            # This checks all vertices independently of the two-active-vertex proof.
            assert max(squared_vertex_distances(r,t)) >= value
            checks += 1
        # Polynomial crossing and relevant derivatives, exact sample identities.
        t_cross = (3*r-1)/(2*(r+1))
        da = r*(2-t0)**2 + t0*t0
        db = r*(1-t0)**2 + (1+t0)**2
        assert (r*(2-t0)**2+t0*t0) - (r*(1-t0)**2+(1+t0)**2) == (3*r-1)-2*(r+1)*t0
        if r <= 3:
            assert da == db == value
            assert t_cross == t0
        else:
            assert da >= db and t0==1
    # Sharp fixed-area crossover at r=3, and fixed-perimeter square bound:
    assert exact_minimum(F(1))[1] == F(5,2)
    assert exact_minimum(F(3))[1] == F(4)
    assert exact_minimum(F(9))[1] == F(10)
    print('PASS: {} independent rational point-versus-all-vertices comparisons; {} parameter cases'.format(checks,len(rs)))

if __name__ == '__main__':
    check()
