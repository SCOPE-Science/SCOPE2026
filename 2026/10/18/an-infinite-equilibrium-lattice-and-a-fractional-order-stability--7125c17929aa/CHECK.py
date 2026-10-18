"""Independent numerical consistency checks for the reported equilibrium lattice.
Standard-library only. These are finite checks, not substitutes for proofs.
"""
import cmath
import math


def threshold(nu):
    assert 0 < nu <= 1
    def residual(d):
        angle = math.acos(-1 / (2 * math.sqrt(d)))
        return math.sqrt(d) - (2 * math.cos((angle - math.pi) / (2 - nu))) ** nu
    lo, hi = .25, 2.
    while residual(hi) <= 0:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if residual(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def eigen_stable(mu, nu):
    angle = abs(cmath.phase(mu))
    if angle <= nu * math.pi / 2:
        return False
    return abs(mu) < (2 * math.cos((angle - math.pi) / (2 - nu))) ** nu


def determinant(x, y, c):
    return 2 * math.pi * c * x * y * math.cos(math.pi * y)


def nonzero_equilibria(c, kmax):
    s = math.sqrt(1 - 1 / c)
    tau = math.asin(s) / math.pi
    for sign in (-1, 1):
        x = sign * s
        theta = sign * tau
        for k in range(-kmax, kmax + 1):
            for y in (2 * k + theta, 2 * k + 1 - theta):
                yield x, y


def test():
    checks = 0
    for nu in (0.01, .1, .25, .5, .75, .9, .98, 1.):
        dcrit = threshold(nu)
        assert dcrit > 1 if nu < 1 else abs(dcrit - 1) < 1e-12
        checks += 1
        for c in (1.0001, 1.005, 1.02, 1.1, 1.5, 2., 3., 4., 8.):
            s = math.sqrt(1 - 1/c)
            tau = math.asin(s)/math.pi
            predicted = 2 * max(0, math.ceil(dcrit/(2*math.pi*math.sqrt(c-1)) - tau))
            observed = 0
            seen = {}
            for x, y in nonzero_equilibria(c, 300):
                assert abs(math.sin(math.pi*y) - x) < 5e-13
                assert abs(c*(1-x*x)*y - y) < 2e-12
                det = determinant(x,y,c)
                trace = -1
                eigs = ((trace + cmath.sqrt(trace*trace-4*det))/2,
                        (trace - cmath.sqrt(trace*trace-4*det))/2)
                if det > 0:
                    jfloat = det/(2*math.pi*math.sqrt(c-1)) - tau
                    j = round(jfloat)
                    assert j >= 0 and abs(j-jfloat) < 1e-8
                    seen[j] = seen.get(j,0)+1
                stable = all(eigen_stable(z,nu) for z in eigs)
                if stable:
                    assert 0 < det < dcrit * (1 + 2e-13)
                    observed += 1
                elif det > 0 and abs(det-dcrit)>1e-8:
                    assert det>dcrit
                checks += 4
            for j in range(300):
                assert seen.get(j,0)==2
                checks += 1
            assert observed == predicted,(nu,c,predicted,observed)
            checks += 1
    # The closed-form level and eigenvalue relations are also tested at distinct points.
    for c in (1.003,1.2,1.9,8.4):
        s=math.sqrt(1-1/c);tau=math.asin(s)/math.pi
        for j in range(101):
            x=s
            y=(j+tau) if j%2==0 else -(j+tau)
            # These y represent the sine branch at every integer parity.
            assert abs(math.sin(math.pi*y)-x)<4e-13
            assert abs(determinant(x,y,c)-2*math.pi*math.sqrt(c-1)*(j+tau)) < 1e-12 + 3e-12 * (j + 1) * math.sqrt(c)
            checks+=2
    print('PASS',checks,'finite consistency checks; analytical proof required for infinite assertions')

if __name__=='__main__':
    test()
