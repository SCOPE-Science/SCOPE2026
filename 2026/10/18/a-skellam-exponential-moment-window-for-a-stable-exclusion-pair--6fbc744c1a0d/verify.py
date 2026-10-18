"""Finite consistency checks for the stated two-particle exclusion exponential tilt.
Does not certify infinite-time asymptotics or research priority.
"""
import math
from fractions import Fraction
import random
import numpy as np
from scipy.linalg import expm


def parameters(a1, b1, a2, b2, th):
    birth = a1 + b2
    death = b1 + a2
    assert 0 < birth < death
    u = math.log((b1 * math.exp(th) + a2) / death)
    rp = b1 * b2 / death
    rm = a1 * a2 / death
    lam = rp * math.expm1(th) + rm * math.expm1(-th)
    tilted_birth = (a1 * math.exp(-th) + b2) * math.exp(u)
    return birth, death, u, lam, tilted_birth, rp, rm


def test_one(a1, b1, a2, b2, th, t=2.5, h0=1, hmax=18):
    birth, death, u, lam, tilted_birth, rp, rm = parameters(a1, b1, a2, b2, th)
    assert abs((tilted_birth - birth) - lam) < 1e-10
    assert tilted_birth < death
    assert abs((a1 * math.exp(-th) + b2) - tilted_birth * math.exp(-u)) < 1e-10
    # Direct check of the unbounded positive eigenfunction on all interior states.
    gen_birth = a1 * math.exp(-th + u) + b2 * math.exp(u)
    gen_death = b1 * math.exp(th - u) + a2 * math.exp(-u)
    assert abs(gen_birth - birth - lam) < 1e-10
    assert abs(gen_birth + gen_death - birth - death - lam) < 1e-10
    # Time-t Feynman-Kac finite restriction and independent tilted-generator calculation.
    N = hmax + 1
    fk = np.zeros((N, N), dtype=float)
    qtilt = np.zeros((N, N), dtype=float)
    for h in range(N):
        fk[h,h] = -(birth + (death if h > 0 else 0))
        qtilt[h,h] = -(tilted_birth + (death if h > 0 else 0))
        if h < hmax:
            fk[h,h+1] = a1 * math.exp(-th) + b2
            qtilt[h,h+1] = tilted_birth
        if h > 0:
            fk[h,h-1] = b1 * math.exp(th) + a2
            qtilt[h,h-1] = death
    direct = expm(fk*t)[h0].sum()
    via_tilt = (math.exp(t*lam+u*h0) *
                np.dot(expm(qtilt*t)[h0], np.exp(-u*np.arange(N))))
    assert abs(direct - via_tilt) < 2e-9, (direct, via_tilt)
    return 1


def test_exact():
    count = 0
    for ia in range(1, 5):
        for ib in range(3, 8):
            for ja in range(1, 5):
                for jb in range(1, 5):
                    a1,b1,a2,b2 = map(Fraction, (ia,ib,ja,jb))
                    delta = b1+a2
                    beta = a1+b2
                    if not beta < delta:
                        continue
                    for z in (Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(5,4),Fraction(2)):
                        U = (b1*z+a2)/delta
                        B = a1/z+b2
                        beta_t = B*U
                        lam = (b1*b2/delta)*(z-1) + (a1*a2/delta)*(1/z-1)
                        assert beta_t-beta == lam
                        assert a1/z*U+b2*U-beta == lam
                        assert b1*z/U+a2/U == delta
                        count += 1
    return count


def main():
    rand = random.Random(7262026)
    count = 0
    for i in range(24):
        a1 = 0.2 + rand.random()*0.8
        b2 = 0.2 + rand.random()*0.8
        a2 = 0.6 + rand.random()*1.3
        b1 = 2.0 + rand.random()*1.9
        for th in (-0.09, 0, 0.09):
            count += test_one(a1, b1, a2, b2, th)
    print('PASS:', count, 'independent finite-dimensional tilt-consistency comparisons; plus', test_exact(), 'exact rational tilted-generator identities')


if __name__ == '__main__':
    main()
