"""Reproduce finite-node and asymptotic checks for arcsine-node quadratic cubature.
Requires Python 3.10+, numpy, scipy. No randomness is needed for proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog

PI = math.pi
G = lambda x: math.asin(x) / PI

def failure_parts(q: float, m: int):
    assert 0 < q < 1 and m >= 2
    alpha0 = math.asin(q)
    alpha1 = PI / 2
    alpha_star = math.asin(math.sqrt(q))
    rate_u = 0.5 + G(q)
    def psi(alpha):
        return math.asin(q / math.sin(alpha))
    def inner(alpha):
        v = 1 - (alpha + psi(alpha)) / PI
        return v ** (m - 1) - (0.5 - alpha / PI) ** (m - 1)
    def outer(alpha):
        return ((alpha + psi(alpha)) / PI) ** (m - 1)
    L, _ = quad(inner, alpha0, alpha1, points=[alpha_star], epsabs=1e-14, epsrel=1e-11)
    U, _ = quad(outer, alpha0, alpha1, epsabs=1e-14, epsrel=1e-11)
    return m / PI * U + rate_u ** m, m / PI * L

def criterion(xs, q):
    neg = sorted(-x for x in xs if x < 0)
    pos = sorted(x for x in xs if x > 0)
    if not neg or not pos:
        return False
    return (neg[0] * pos[0] < q < neg[-1] * pos[-1])

def check():
    checks = 0
    for q in [0.08, 0.2, 1.0 / 3, 0.5, 0.8]:
        for m in [2, 3, 4, 5, 10, 20, 40, 80, 160]:
            U, L = failure_parts(q, m)
            P = 1 - U - L
            assert -2e-10 <= P <= 1 + 2e-10, (q, m, U, L, P)
            checks += 1
        U, L = failure_parts(q, 240)
        ru = 0.5 + G(q)
        rl = 1 - 2 * G(math.sqrt(q))
        c = math.sqrt(math.sqrt(q * (1 - q)) / rl)
        assert abs((U / ru**240) - 2) < 0.1
        assert abs((L / (math.sqrt(240) * rl**240)) - c) < 0.08
        checks += 2
    # Independent primal feasibility via linear programming, not the extreme product test.
    rng = np.random.default_rng(20261031)
    for q in [0.08, 1.0/3.0, 0.7]:
        for m in [3, 4, 6, 9]:
            for i in range(100):
                xs = np.sin(rng.uniform(-PI/2, PI/2, size=m))
                Aeq = np.vstack([np.ones(m), xs, xs*xs])
                out = linprog(np.zeros(m), A_eq=Aeq, b_eq=[1,0,q],
                              bounds=[(1e-9, None)] * m, method='highs',
                              options={'primal_feasibility_tolerance': 1e-9})
                if out.success:
                    assert np.linalg.norm(Aeq @ out.x - [1,0,q], ord=np.inf) < 1e-7
                assert out.success == criterion(xs, q), (q,m,i,xs.tolist())
                checks += 1
    # The exact rate crossing occurs at the uniform target's quadratic moment.
    q = 1.0/3
    assert abs(0.5 + G(q) - (1-2*G(math.sqrt(q)))) < 1e-14
    assert abs((math.log(3/2)/(-math.log(0.5+G(q))))-0.8153409475) < 1e-9
    checks += 2
    print('PASS', checks, 'independent quadrature, phase-rate and LP feasibility checks')
    q = 1/3; r=0.5+G(q); c=math.sqrt(math.sqrt(q*(1-q))/r)
    print('r=',format(r,'.16f'),'C=',format(c,'.16f'),'node_ratio=',format(math.log(1.5)/(-math.log(r)),'.16f'))
    for m in [20, 40, 80, 160, 240]:
        u, l = failure_parts(q,m)
        print(m,'P=',1-u-l,'ratio=',(u+l)/(math.sqrt(m)*r**m),'outer_scaled=',u/r**m)

if __name__=='__main__':
    check()
