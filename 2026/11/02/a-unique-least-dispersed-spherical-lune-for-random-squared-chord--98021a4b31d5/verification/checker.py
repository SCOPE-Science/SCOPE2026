"""Numerical cross-checks for squared chord statistics of spherical lunes.

Analytic uniqueness is established in the accompanying mathematical proof,
not inferred from finite tests. Python standard library only.
"""
import math
import random

PI = math.pi


def target_mean(a):
    return 2 - PI**2 * math.sin(a / 2)**2 / (2*a*a)


def target_var(a):
    return (4/3 + (8/9)*(math.sin(a)/a)**2
            - (PI**4/4)*(math.sin(a/2)/a)**4)


def H(t):
    return (t/math.tan(t))**2 + t**3/(math.tan(t)-t)


def bisection():
    target = 9*PI**4/256
    lo, hi = .15, 1.3
    assert H(lo) > target > H(hi)
    for _ in range(90):
        mid = (lo + hi)/2
        if H(mid) > target:
            lo = mid
        else:
            hi = mid
    return lo + (hi-lo)/2


def sample_pair(a, rg):
    z1, z2 = 2*rg.random()-1, 2*rg.random()-1
    f1, f2 = a*(rg.random()-.5), a*(rg.random()-.5)
    dot = z1*z2 + math.sqrt((1-z1*z1)*(1-z2*z2))*math.cos(f1-f2)
    return 2-2*dot


def verify():
    t = bisection()
    a0 = 2*t
    assert abs(a0-1.116475225945476) < 1e-11
    assert abs(target_var(a0)-.6753158386946393) < 2e-13
    assert abs(target_var(PI)-13/12) < 2e-14
    assert abs((20/9-PI**4/64)-.7002051748159341) < 2e-13
    print('STATIONARY_POINT_AND_EXACT_HEMISPHERE_LIMIT_PASSED')

    # Checks derivative signs and the strictly decreasing H profile on a
    # finite grid; analytic proof establishes the all-t statement.
    grid = [(.001 + (PI/2-.002)*j/512) for j in range(513)]
    hh = [H(x) for x in grid]
    assert all(hh[j] > hh[j+1] for j in range(512))
    assert all(target_var(2*grid[j]) < target_var(2*grid[j-1])
               for j in range(1,512) if 2*grid[j] < a0-.03)
    assert all(target_var(2*grid[j]) > target_var(2*grid[j-1])
               for j in range(1,512) if 2*grid[j-1] > a0+.03)
    print('DIRECT_PROFILE_GRID_DIAGNOSTIC_PASSED 513')

    # Independently sample the area measure: z is uniform on [-1,1],
    # azimuth is uniform on the lune's longitude interval.
    rng = random.Random(540312)
    for a in (.2, a0, 2.4, PI):
        n = 180000
        total = total2 = 0.
        for _ in range(n):
            x = sample_pair(a,rng)
            total += x
            total2 += x*x
        avg = total/n
        variance = total2/n-avg*avg
        assert abs(avg-target_mean(a)) < .015, (a, avg, target_mean(a))
        assert abs(variance-target_var(a)) < .02, (a, variance, target_var(a))
    print('INDEPENDENT_AREA_UNIFORM_TWO_POINT_SIMULATIONS_PASSED 4')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    verify()
