"""Independent numerical chord check for quartic-ball directional covariograms.

Requires numpy and scipy. This checks representative parameters, not the
uniform analytic theorem or scientific originality.
"""
import numpy as np
from scipy.optimize import root, brentq
from numpy.polynomial.legendre import leggauss


def cubic_midpoint(lam, r):
    return brentq(lambda m: m**3 + (r*r/4)*m + lam,
                  -(abs(lam)+10)**(1/3)-3, (abs(lam)+10)**(1/3)+3)


def crossover(lam):
    u, w = leggauss(100)
    rr, ww = (u+1)/2, w/2
    vals = []
    for r in rr:
        m = cubic_midpoint(lam, r)
        vals.append(0.75*abs(lam)**(4/3)-0.75*m**4 + m*m*r*r/8 + r**4/64)
    return 2*np.dot(ww, vals)


def exact_chord_quotient(lam, t):
    theta = lam*t**3
    c, d = np.cos(theta), np.sin(theta)
    h = (abs(c)**(4/3)+abs(d)**(4/3))**(3/4)

    def transverse_end(r):
        s = t*r
        a = s*s/4
        m = cubic_midpoint(lam, r)
        initial = [t*m, 1-t**4*(m**4/4+lam*m)]

        def equations(v):
            x, y = v
            return [c*x**3 + d*y**3 + a*(c**3*x+d**3*y),
                    x**4+y**4+6*a*(c*c*x*x+d*d*y*y)
                    +a*a*(c**4+d**4)-1]

        sol = root(equations, initial, tol=1e-12)
        if np.linalg.norm(sol.fun) > 1e-10:
            raise ArithmeticError('quartic endpoint solver residual too large')
        x, y = sol.x
        return -d*x+c*y

    u, w = leggauss(65)
    rs, ws = (u+1)/2, w/2
    return 2*np.dot(ws, [h-transverse_end(r) for r in rs])/t**4


def main():
    for lam in (0.0, 0.2, 1.0, 5.0, 20.0):
        expected = crossover(lam)
        values = [exact_chord_quotient(lam, t) for t in (0.30, 0.20, 0.12)]
        assert abs(values[-1]-expected) < 0.03*max(0.05, expected)
        assert abs(values[-1]-expected) <= abs(values[0]-expected)+1e-9
        print(f'lambda={lam:g}: F={expected:.10f}, checks={values}')
    assert abs(crossover(0)-1/160) < 1e-12
    print('PASS: numerical consistency checks (not an all-parameter proof)')


if __name__ == '__main__':
    main()
