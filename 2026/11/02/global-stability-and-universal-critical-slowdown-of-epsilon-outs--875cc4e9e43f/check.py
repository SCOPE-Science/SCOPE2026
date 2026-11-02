"""Finite reproducibility checks for critical epsilon-outside RMSProp.

The universal asymptotic and global-stability statements require the
analytical proof supplied in RESULT.md; finite iterations cannot prove them.
"""
from fractions import Fraction
from math import sqrt


def scalar_run(a, eps, beta, x0, v0, n):
    x, v = float(x0), float(v0)
    h = 2.0 * eps / a
    result = {}
    for k in range(1, n + 1):
        vp = beta * v + (1.0 - beta) * (a*x)**2
        x = x - h * a * x / (eps + sqrt(vp))
        v = vp
        if k in (10000, 60000, n):
            result[k] = (k*abs(x), k*k*v)
    return result


def objective(x):
    return (3*x[0]*x[0] + 2*x[0]*x[1] + 2*x[1]*x[1]) / 2


def gradient(x):
    return (3*x[0] + x[1], x[0] + 2*x[1])


def check_matrix_step():
    # Hessian [[3,1],[1,2]] has largest eigenvalue (5+sqrt(5))/2.
    L = (5+sqrt(5))/2
    eps, beta = 1.0, 0.8
    h = 2*eps/L
    for x, v in [((.25,-.33),(.1,.03)), ((-1.4,.7),(0.,0.)),
                 ((.001,.004),(4.,.2))]:
        g = gradient(x)
        vp = [beta*v[i] + (1-beta)*g[i]**2 for i in range(2)]
        xp = [x[i] - h*g[i]/(eps+sqrt(vp[i])) for i in range(2)]
        decrement = h*sum(g[i]**2*sqrt(vp[i])/(eps+sqrt(vp[i]))**2 for i in range(2))
        assert objective(xp)-objective(x) <= -decrement + 1e-12
        assert objective(xp) < objective(x)
    print('NONDIAGONAL_QUADRATIC_ENDPOINT_DESCENT_PASS 3')


def check_finite_hit():
    # This choice gives v1=1 exactly and h*a/(eps+sqrt(v1))=1.
    a, eps, beta = Fraction(2), Fraction(1), Fraction(4,5)
    x0, v0 = Fraction(1,10), Fraction(31,25)
    v1 = beta*v0 + (1-beta)*(a*x0)**2
    assert v1 == eps**2
    h = 2*eps/a
    x1 = x0 - h*(a*x0)/(eps+Fraction(1))
    assert x1 == 0
    print('EXACT_RATIONAL_FINITE_HIT_PASS',str(v1),str(x1))


def check_scalar_limits():
    for a, eps, beta, x0 in [(2.0,1.0,.2,.1),(1.4,.8,.95,.02)]:
        samples=scalar_run(a,eps,beta,x0,0.,120000)
        target_x = eps/(2*a)
        target_v = eps**2/4
        for k in (60000,120000):
            nx,nv=samples[k]
            assert abs(nx-target_x) < .003
            assert abs(nv-target_v) < .003
        print('SCALAR_CRITICAL_TREND_PASS',a,eps,beta,
              'k=120000',f'{samples[120000][0]:.9f}',f'{samples[120000][1]:.9f}',
              'limits',f'{target_x:.9f}',f'{target_v:.9f}')
    print('UNIVERSAL_INFINITE_TIME_AND_GLOBAL_STATEMENTS_USE_ANALYTICAL_PROOF')


if __name__ == '__main__':
    check_matrix_step()
    check_finite_hit()
    check_scalar_limits()
