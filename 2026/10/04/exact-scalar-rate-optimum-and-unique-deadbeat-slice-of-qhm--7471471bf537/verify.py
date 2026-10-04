from fractions import Fraction
import cmath
import math

def matrix(beta, nu, s):
    return (
        (1-s*(1-nu*beta), -s*nu*beta),
        (1-beta, beta),
    )

def roots(beta, nu, s):
    T = 1+beta-s*(1-nu*beta)
    D = beta*(1-s*(1-nu))
    disc = cmath.sqrt(T*T-4*D)
    return (T+disc)/2, (T-disc)/2

def rho(beta, nu, s):
    r1, r2 = roots(beta, nu, s)
    return max(abs(r1), abs(r2))

def smax(beta, nu):
    return 2*(1+beta)/(1+beta-2*beta*nu)

# Exact rational nilpotence on the Nesterov slice.
for beta in (Fraction(1,5), Fraction(1,2), Fraction(9,10)):
    nu = beta
    s = 1/(1-beta)
    M = matrix(beta, nu, s)
    M2 = (
        (M[0][0]*M[0][0]+M[0][1]*M[1][0],
         M[0][0]*M[0][1]+M[0][1]*M[1][1]),
        (M[1][0]*M[0][0]+M[1][1]*M[1][0],
         M[1][0]*M[0][1]+M[1][1]*M[1][1]),
    )
    assert M2 == ((0,0),(0,0))

# Interior closed-form optimum and discriminant endpoints.
for beta in (0.1, 0.3, 0.7, 0.95):
    for nu in (0.05, 0.2, 0.5, 0.8, 0.95):
        t = math.sqrt(beta*nu)
        sl = (1-beta)/(1+t)**2
        sr = (1-beta)/(1-t)**2
        rl = (beta+t)/(1+t)
        rr = (beta-t)/(1-t)
        a1, a2 = roots(beta, nu, sl)
        b1, b2 = roots(beta, nu, sr)
        assert abs(a1-rl) < 2e-7 and abs(a2-rl) < 2e-7
        assert abs(b1-rr) < 2e-7 and abs(b2-rr) < 2e-7
        target = abs(rr)
        assert sr < smax(beta, nu)
        assert abs(rho(beta, nu, sr)-target) < 2e-7

        # Dense deterministic search guard.
        ceiling = smax(beta, nu)
        best = 10.0
        bests = None
        for j in range(1, 20001):
            s = ceiling*j/20001
            val = rho(beta, nu, s)
            if val < best:
                best, bests = val, s
        assert best >= target-3e-4
        assert abs(bests-sr) < 3e-3*max(1.0, sr)

# Endpoint nu=0 plateau.
for beta in (0.1, 0.5, 0.9):
    for s in (1-beta, 1.0, 1+beta):
        assert abs(rho(beta, 0.0, s)-beta) < 2e-7
    assert rho(beta, 0.0, 0.5*(1-beta)) > beta
    assert rho(beta, 0.0, 1+beta+0.1*(1-beta)) > beta

# Endpoint nu=1 plateau.
for beta in (0.1, 0.5, 0.9):
    sb = math.sqrt(beta)
    lo = (1-sb)/(1+sb)
    hi = (1+sb)/(1-sb)
    for s in (lo, (lo+hi)/2, hi):
        assert abs(rho(beta, 1.0, s)-sb) < 2e-7
    assert rho(beta, 1.0, lo/2) > sb
    assert rho(beta, 1.0, (hi+smax(beta,1.0))/2) > sb

# Stability boundary.
for beta in (0.1, 0.5, 0.9):
    for nu in (0.0, 0.2, beta, 0.8, 1.0):
        cap = smax(beta, nu)
        assert rho(beta, nu, 0.999999*cap) < 1+2e-7
        assert rho(beta, nu, 1.000001*cap) > 1-2e-7

print("verification passed")
