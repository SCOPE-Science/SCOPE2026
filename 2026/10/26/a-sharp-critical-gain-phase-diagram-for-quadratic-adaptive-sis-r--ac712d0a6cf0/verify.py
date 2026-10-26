#!/usr/bin/env python3
"""Independent rational and time-stepping checks for a scalar adaptive-recovery SIS theorem.

The checks test the equations and representative phase regimes; the analytical proof
in RESULT.md is required for the universal assertions.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def check(test, explanation):
    global checks
    checks += 1
    if not test:
        raise AssertionError(explanation)


def rhs(beta, delta, alpha, x, g):
    return (x * (beta * (1 - x) - delta * g), alpha * x * x)


def rk4(beta, delta, alpha, x0, g0, dt, count):
    x, g = float(x0), float(g0)
    b, d, a = float(beta), float(delta), float(alpha)
    for _ in range(count):
        k1x, k1g = rhs(b, d, a, x, g)
        k2x, k2g = rhs(b, d, a, x + dt*k1x/2, g + dt*k1g/2)
        k3x, k3g = rhs(b, d, a, x + dt*k2x/2, g + dt*k2g/2)
        k4x, k4g = rhs(b, d, a, x + dt*k3x, g + dt*k3g)
        x += dt*(k1x+2*k2x+2*k3x+k4x)/6
        g += dt*(k1g+2*k2g+2*k3g+k4g)/6
        check(-1e-10 <= x <= 1+1e-10 and g >= float(g0)-1e-10,
              'epidemiological invariance / nondecreasing gain')
    return x, g

# Verify the projective change of variables as polynomial identities at exact points.
for beta in (F(11,10), F(2), F(5,3)):
    for delta in (F(1), F(1,2)):
        for alpha in (F(1,5), F(1), F(2)):
            for x in (F(1,7), F(2,3)):
                for y in (F(1,10), F(3,4)):
                    g = beta/delta-y
                    dx, dg = rhs(beta, delta, alpha, x, g)
                    dy = -dg
                    z = x/y
                    dz = (dx*y-x*dy)/(y*y)
                    polynomial = y*z*(delta-beta*z+alpha*z*z)
                    check(dx == x*(delta*y-beta*x), 'homogeneous x derivative')
                    check(dy == -alpha*x*x, 'homogeneous y derivative')
                    check(dz == polynomial, 'exact projective derivative')

# Exact phase-side comparisons with rational arithmetic; no float inequalities.
beta, delta, alpha = F(11,10), F(1), F(1,5)
Delta = beta*beta-4*alpha*delta
check(Delta == F(41,100), 'discriminant')
# zplus = (11+sqrt(41))/4.  2 < zplus < 6 by rational squaring.
check(F(8)-F(11) < 0 and 13*13>41, 'critical and overcontrol seeds')
check(beta*beta-4*F(2,5)*delta<0, 'universal overcontrol parameter')
check(F(2)*F(2)-4*F(1)*F(1)==0, 'double-root parameter')
# Closed-form invariant ray at beta=2, delta=alpha=1, x0=g0=1.
for t in (F(0), F(1,7), F(1), F(3), F(17)):
    x = 1/(1+t)
    g = 2-x
    dx, dg = rhs(F(2), F(1), F(1), x, g)
    check(dx == -x*x and dg == x*x, 'explicit critical exact trajectory')

# Reproduce both regimes under the same parameters; these are corroborative,
# not a proof of the asymptotic statements.
x_crit, g_crit = rk4(F(11,10), F(1), F(1,5), F(1,5), F(1), 0.1, 100000)
x_over, g_over = rk4(F(11,10), F(1), F(1,5), F(3,5), F(1), 0.1, 100000)
x_fast, g_fast = rk4(F(11,10), F(1), F(2,5), F(1,5), F(1), 0.1, 100000)
check(abs(g_crit-1.1)<0.0005 and abs(x_crit*10000 - 1/(0.2*((11-sqrt(41))/4)))<0.1,
      'critical 1/t asymptotics')
check(g_over>1.11 and x_over < 1e-8, 'seed-driven overcontrol')
check(g_fast>1.102 and x_fast<1e-8, 'rate-driven overcontrol')
print('PASS:', checks, 'exact and numerical invariant checks; critical/overcontrol examples reproduced.')
print('critical:', format(x_crit,'.12g'),format(g_crit,'.12g'))
print('seed-over:',format(x_over,'.12g'),format(g_over,'.12g'))
print('rate-over:',format(x_fast,'.12g'),format(g_fast,'.12g'))
