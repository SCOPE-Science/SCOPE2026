"""Numerical consistency checks for the polygonal short-chord curvature limit.

Requires only Python 3 standard library. Numerical tests supplement, not replace,
the analytic proof in RESULT.md.
"""
import math


def point_from_arclength(s, p, eps=0.5):
    """Convex oval with support h(theta)=1+eps*cos(p*theta)/(1-p*p)."""
    t = s
    for _ in range(8):
        t -= (t + eps * math.sin(p*t) / p - s) / (1 + eps*math.cos(p*t))
    h = 1 + eps / (1-p*p) * math.cos(p*t)
    dh = -eps*p / (1-p*p) * math.sin(p*t)
    return (h*math.cos(t) - dh*math.sin(t),
            h*math.sin(t) + dh*math.cos(t))


def turning_energy(n, p):
    vertices = [point_from_arclength(2*math.pi*j/n, p) for j in range(n)]
    edges = [(vertices[(j+1) % n][0]-vertices[j][0],
              vertices[(j+1) % n][1]-vertices[j][1]) for j in range(n)]
    energy = 0.0
    for j in range(n):
        x, y = edges[j-1]
        u, v = edges[j]
        beta = math.atan2(x*v-y*u, x*u+y*v)
        assert 0 < beta < math.pi
        energy += beta/math.sin(beta)-1
    return energy


def exact_secondary(p):
    return 4*math.sqrt(3)*math.pi**4*(378-85*p*p)/3645


def periodic_integral(func, count=4096):
    return 2*math.pi/count * sum(func(2*math.pi*j/count)
                                 for j in range(count))


def run():
    eps = 0.5
    third = periodic_integral(lambda t: (1+eps*math.cos(t))**(-3))
    gradient = periodic_integral(
        lambda t: eps**2*math.sin(t)**2 / (1+eps*math.cos(t))**5)
    assert abs(third - 8*math.sqrt(3)*math.pi/3) < 1e-9
    assert abs(gradient - 34*math.sqrt(3)*math.pi/81) < 1e-9

    leading = 4*math.pi**2/(3*math.sqrt(3))
    for p in (2, 3):
        previous_error = float('inf')
        for n in (64, 128, 256, 512, 1024):
            estimate = n*n * (n*turning_energy(n,p)-leading)
            error = abs(estimate-exact_secondary(p))
            print('oval mode',p,'edges',n,'second-order estimate',
                  format(estimate,'.11g'),'absolute error',format(error,'.6g'))
            assert error < previous_error
            previous_error = error
        assert previous_error < 0.03
    assert exact_secondary(2) > 0 > exact_secondary(3)

    previous_error = float('inf')
    for n in (64, 128, 256, 512):
        beta = 2*math.pi/n
        scaled_energy = n*n*(beta/math.sin(beta)-1)
        estimate = n*n*(scaled_energy-2*math.pi**2/3)
        limit = 14*math.pi**4/45
        error = abs(estimate-limit)
        print('circle edges',n,'second-order estimate',
              format(estimate,'.11g'),'absolute error',format(error,'.6g'))
        assert error < previous_error
        previous_error = error
    assert previous_error < 0.001
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
