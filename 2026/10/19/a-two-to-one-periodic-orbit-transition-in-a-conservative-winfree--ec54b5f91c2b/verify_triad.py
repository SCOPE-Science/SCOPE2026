"""Self-contained numerical and algebraic checks for the conservative Winfree triad.

Numerics corroborate exact identities; the published proof establishes all-parameter claims.
"""
import math
import random
from fractions import Fraction

B = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
TWO_PI = 2 * math.pi


def theta_of_t(t, e):
    # Conjugate of the strictly increasing circle change of phase.
    s = math.sqrt((1 + e) / (1 - e))
    return 2 * math.atan2(s * math.sin(t / 2), math.cos(t / 2))


def A(theta, e):
    return 1 + e * math.cos(theta)


def Aprime(theta, e):
    return -e * math.sin(theta)


def H(t, e):
    return -sum(math.log1p(-e * math.cos(x)) for x in t)


def gradH(t, e):
    return [-e * math.sin(x) / (1 - e * math.cos(x)) for x in t]


def vector_t_direct(t, e):
    k = math.sqrt(1 - e * e)
    theta = [theta_of_t(x, e) for x in t]
    dtheta = [A(theta[i], e) * sum(B[i][j] * Aprime(theta[j], e) for j in range(3)) for i in range(3)]
    return [k * dtheta[i] / A(theta[i], e) for i in range(3)]


def vector_t_hamilton(t, e):
    g = gradH(t, e)
    return [(1 - e * e) * sum(B[i][j] * g[j] for j in range(3)) for i in range(3)]


def curv(t, e):
    return -e * (math.cos(t) - e) / (1 - e * math.cos(t)) ** 2


def run():
    rng = random.Random(73)
    tests = 0
    for e in (0.02, 0.15, 0.5, 0.9, 0.999):
        for _ in range(200):
            t = [rng.uniform(-math.pi, math.pi) for _ in range(3)]
            direct, ham = vector_t_direct(t, e), vector_t_hamilton(t, e)
            assert max(abs(a - b) for a, b in zip(direct, ham)) < 3e-11
            assert abs(sum(ham)) < 3e-12
            assert abs(sum(a*b for a, b in zip(ham, gradH(t, e)))) < 3e-12
            tests += 1
        emin = -3 * math.log(1 + e/2)
        esad = -math.log((1-e)*(1+e)**2)
        emax = -3 * math.log(1-e)
        assert emin < esad < emax
        candidates = [(0,0,0), (2*math.pi/3,)*3, (-2*math.pi/3,)*3]
        for idx in range(3):
            x = [math.pi, math.pi, math.pi]
            x[idx] = 0
            candidates.append(tuple(x))
        assert len(candidates) == 6
        for i, t in enumerate(candidates):
            assert abs(sum(t) % (2*math.pi)) < 1e-11 or abs(sum(t) % (2*math.pi) - 2*math.pi) < 1e-11
            g = gradH(t,e)
            assert max(g) - min(g) < 2e-14
            h11 = curv(t[0],e) + curv(t[2],e)
            h22 = curv(t[1],e) + curv(t[2],e)
            h12 = curv(t[2],e)
            d = h11*h22 - h12*h12
            assert abs(d)>1e-12
            if i == 0:
                assert h11 < 0 and d > 0 and abs(H(t,e)-emax)<1e-10
            elif i in (1,2):
                assert h11 > 0 and d > 0 and abs(H(t,e)-emin)<1e-10
            else:
                assert d < 0 and abs(H(t,e)-esad)<1e-10
    # Polynomial sign certificate for all eps in (0,1), cos(u) in [-1,1].
    for e in (Fraction(1,7), Fraction(1,2), Fraction(9,10)):
        for c in (Fraction(-1), Fraction(-1,2), Fraction(0), Fraction(1,2), Fraction(1)):
            lhs = 1 + e + 2*c - 4*e*c*c
            rhs = (2*c+1)*(1+e-2*e*c)
            assert lhs == rhs and 1+e-2*e*c>0
        assert (1+e/2)**3 - (1-e)*(1+e)**2 == e*(9*e*e+14*e+4)/8
        assert (1-e)*(1+e)**2 - (1-e)**3 == 4*e*(1-e)
    print('VERIFY_OK',tests,'random conjugacy/energy/Casimir checks, 30 Morse Hessians, exact rational sign certificates')


if __name__ == '__main__':
    run()
