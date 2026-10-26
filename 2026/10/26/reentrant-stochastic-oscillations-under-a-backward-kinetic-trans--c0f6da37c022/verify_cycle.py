"""Symbolic and independently structured numerical checks for a stochastic kinetic ring.

Runs with Python, NumPy, and SciPy; it does not use external data.
"""
import math
import numpy as np
from scipy.linalg import expm
import sympy as sp


def generator(a, b, c, h):
    return np.array([[-a, a, 0.0], [h, -h - b, b], [c, 0.0, -c]], dtype=float)


def formula(a, b, c, h):
    s = a + b + c + h
    disc = (h - (c - a - b)) ** 2 - 4 * a * b
    return np.array([-s / 2 + np.sqrt(complex(disc)) / 2,
                     -s / 2 - np.sqrt(complex(disc)) / 2])


def stationary(a, b, c, h):
    z = c * (b + h) + a * c + a * b
    return np.array([c * (b + h), a * c, a * b]) / z


def quality(a, b, c, h):
    inside = 4 * a * b - (h - c + a + b) ** 2
    return math.sqrt(max(0.0, inside)) / (a + b + c + h)


def check_exact_algebra():
    a,b,c,h,z = sp.symbols('a b c h z', positive=True)
    Q = sp.Matrix([[-a,a,0], [h,-(h+b),b], [c,0,-c]])
    S=a+b+c
    P=a*b+a*c+b*c
    H=c-a-b
    assert sp.factor((z*sp.eye(3)-Q).det()-z*(z*z+(S+h)*z+P+c*h))==0
    assert sp.factor((S+h)**2-4*(P+c*h)-((h-H)**2-4*a*b))==0
    norm=c*(b+h)+a*c+a*b
    pi=sp.Matrix([[c*(b+h),a*c,a*b]])/norm
    assert sp.factor((pi*sp.ones(3,1))[0]-1)==0
    assert all(sp.factor(x)==0 for x in (pi*Q))
    J=a*b*c/norm
    assert sp.factor(a*pi[0]-h*pi[1]-J)==0
    assert sp.factor(sp.diff(J,h)+a*b*c*c/norm**2)==0
    hstar=H-2*a*b/c
    rho2=(4*a*b-(h-H)**2)/(S+h)**2
    assert sp.factor(sp.diff(rho2,h)-4*c*(hstar-h)/(S+h)**3)==0
    assert sp.factor(rho2.subs(h,hstar)-a*b/(c*c-a*b))==0



def run():
    check_exact_algebra()
    rng = np.random.default_rng(20261023)
    eigen_cases = 0
    stationary_cases = 0
    row_cases = 0
    for i in range(2200):
        a, b, c = np.exp(rng.uniform(-2.2, 2.2, 3))
        h = float(np.exp(rng.uniform(-3, 2.6)))
        M = generator(a, b, c, h)
        assert np.max(np.abs(M.sum(axis=1))) < 2e-14
        vals = np.linalg.eigvals(M)
        # Compare the unordered nontrivial spectrum, independent matrix eigensolver.
        vals = sorted(vals, key=lambda z: (round(z.real, 9), z.imag))
        nonzero = [z for z in vals if abs(z) > 1e-8]
        if len(nonzero) != 2:
            raise AssertionError('nontrivial spectrum cardinality')
        closed = list(formula(a, b, c, h))
        err = min(max(abs(nonzero[0]-closed[0]), abs(nonzero[1]-closed[1])),
                  max(abs(nonzero[0]-closed[1]), abs(nonzero[1]-closed[0])))
        assert err < 2e-7 * (1+a+b+c+h), (a,b,c,h,err)
        eigen_cases += 1
        pi = stationary(a, b, c, h)
        A = M.T.copy()
        A[2] = 1
        rhs = np.array([0,0,1], dtype=float)
        pi_independent = np.linalg.solve(A, rhs)
        assert np.max(np.abs(pi-pi_independent)) < 1e-11
        assert abs(pi @ M).max() < 1e-12 * (1+a+b+c+h)
        stationary_cases += 1
        current = a*b*c/(c*(b+h)+a*c+a*b)
        assert abs((a*pi[0]-h*pi[1])-current)<1e-11
        assert abs((b*pi[1])-current)<1e-11
        assert abs((c*pi[2])-current)<1e-11
        row_cases += 1

    optimize_cases = 0
    for i in range(900):
        a, b = np.exp(rng.uniform(-1.4, 1.4, 2))
        lower = (math.sqrt(a)-math.sqrt(b))**2
        # Ensure an open oscillatory set at some nonnegative backward rate.
        c = lower + float(np.exp(rng.uniform(-1.4, 2)))
        hstar = max(0.0, c-a-b-2*a*b/c)
        max_allowed = c-(math.sqrt(a)-math.sqrt(b))**2
        hstar = min(hstar, max_allowed)
        candidates = [quality(a,b,c,0.0), quality(a,b,c,hstar)]
        xs = np.linspace(0, max(1.0,c+4*math.sqrt(a*b)), 1601)
        values = np.array([quality(a,b,c,float(x)) for x in xs])
        assert max(candidates)+1e-11 >= max(values)
        optimize_cases += 1

    exceptional_cases = 0
    for i in range(300):
        a,b = np.exp(rng.uniform(-1,1,2))
        c = (math.sqrt(a)+math.sqrt(b))**2 + rng.uniform(.02,5)
        for h in (c-(math.sqrt(a)+math.sqrt(b))**2,
                  c-(math.sqrt(a)-math.sqrt(b))**2):
            M=generator(a,b,c,h)
            lam=-(a+b+c+h)/2
            # Defective double eigenvalue, one-dimensional eigenspace:
            assert np.linalg.matrix_rank(M-lam*np.eye(3),tol=1e-8)==2
            exceptional_cases+=1

    transition_cases = 0
    for i in range(180):
        a,b,c=1.,1.,5.
        h = float(rng.uniform(1.2,5.0))
        Q=generator(a,b,c,h)
        pi=stationary(a,b,c,h)
        gamma=(a+b+c+h)/2
        w=math.sqrt(4*a*b-(h-c+a+b)**2)/2
        f0=1-pi[0]
        # P00'(0)=-a; solve coefficient in damped cosine/sine.
        g0=(-a+gamma*f0)/w
        for t in (0.02,0.1,0.3,0.8,1.4):
            direct=expm(Q*t)[0,0]-pi[0]
            analytic=math.exp(-gamma*t)*(f0*math.cos(w*t)+g0*math.sin(w*t))
            assert abs(direct-analytic)<3e-11
            transition_cases+=1

    print('PASS: exact algebra identities; {} eigensystems; {} stationary laws; {} currents; {} sampled optimality comparisons; {} exceptional-point ranks; {} matrix-exponential identities'.format(
        eigen_cases,stationary_cases,row_cases,optimize_cases,exceptional_cases,transition_cases))

if __name__=='__main__':
    run()
