"""Exact-rational checks for the directed-ring sequential best-response theorem.

Run with Python 3, using only the standard library. Finite tests corroborate,
but do not replace, the general interval-map proof.
"""
from fractions import Fraction as F
from random import Random


def clip(x, lo, hi):
    return max(lo, min(hi, x))


def response(x, target, weight):
    return max(F(0), target - weight*x)


def parameters(u, t, w):
    lo, hi = F(0), u[-1]
    b, s = F(0), F(1)
    for ti, wi in zip(t, w):
        lo, hi = response(hi, ti, wi), response(lo, ti, wi)
        b, s = ti-wi*b, -wi*s
    return lo, hi, b, s


def direct(z, t, w):
    for ti, wi in zip(t, w):
        z = response(z, ti, wi)
    return z


def check_random_compositions():
    rng = Random(20261029)
    checks = 0
    for n in range(3, 12):
        for _ in range(350):
            u = [F(rng.randrange(2, 13), 3) for _ in range(n)]
            t = [v*F(rng.randrange(1, 10), 11) for v in u]
            w = [F(rng.randrange(1, 21), 10) for _ in range(n)]
            lo, hi, b, s = parameters(u, t, w)
            assert lo <= hi <= t[-1] < u[-1]
            for j in range(17):
                z = u[-1]*F(j, 16)
                assert direct(z, t, w) == clip(b+s*z, lo, hi)
                checks += 1
    return checks


def check_critical_cases():
    count = 0
    for n in range(3, 9):
        for k in range(1, 6):
            w = [F(k, k+1), F(k+1, k)] + [F(1)]*(n-2)
            t = [F(1)]*n
            u = [F(2)]*n
            lo, hi, b, s = parameters(u, t, w)
            assert s == F((-1)**n)
            for j in range(17):
                z = u[-1]*F(j, 16)
                y = clip(b+s*z, lo, hi)
                if n % 2:
                    z2 = clip(b+s*y, lo, hi)
                    assert z2 == clip(z, clip(b-hi, lo, hi), clip(b-lo, lo, hi))
                    assert clip(b+s*clip(b+s*z2, lo, hi), lo, hi) == z2
                else:
                    if b == 0:
                        assert clip(b+s*y, lo, hi) == y
                count += 1
    return count


def check_supercritical_finite_orbits():
    rng=Random(314159)
    checks=0
    for n in range(3, 9):
        for _ in range(120):
            u=[F(2)]*n
            t=[F(rng.randrange(1, 8), 6) for _ in range(n)]
            # Targets must lie below upper capacities.
            w=[rng.choice([F(1),F(3,2),F(2)]) for _ in range(n)]
            if all(x == 1 for x in w):
                w[-1]=F(2)
            lo,hi,b,s=parameters(u,t,w)
            assert abs(s)>1
            a=abs(s) if n%2==0 else s*s
            intercept=b if n%2==0 else b*(1+s)
            gl,gh=(lo,hi) if n%2==0 else (clip(b+s*hi,lo,hi),clip(b+s*lo,lo,hi))
            assert gl<=gh
            def G(z):return clip(intercept+a*z,gl,gh)
            for j in range(9):
                z=u[-1]*F(j,8)
                z=G(z)
                # At a slope greater than one, all orbits outside the
                # unique expanding fixed point attain a plateau in finite time.
                for it in range(100):
                    nxt=G(z)
                    if nxt==z:
                        break
                    z=nxt
                else:
                    raise AssertionError(('not finite',n,t,w,j,z,gl,gh,a,intercept))
                checks+=1
    return checks


def check_exact_examples():
    for n, b, s in [(3,F(3),F(-8)),(4,F(-5),F(16))]:
        u=[F(2)]*n;t=[F(1)]*n;w=[F(2)]*n
        lo,hi,B,S=parameters(u,t,w)
        assert (lo,hi,B,S)==(F(0),F(1),b,s)
    assert parameters([F(2)]*3,[F(1)]*3,[F(1)]*3) == (F(0),F(1),F(1),F(-1))
    assert parameters([F(2)]*4,[F(1)]*4,[F(1)]*4) == (F(0),F(1),F(0),F(1))
    return 4


if __name__ == '__main__':
    a=check_random_compositions()
    b=check_critical_cases()
    c=check_supercritical_finite_orbits()
    d=check_exact_examples()
    print(f'PASS: {a} exact composition comparisons, {b} critical checks, '
          f'{c} supercritical orbit checks, {d} exact examples')
