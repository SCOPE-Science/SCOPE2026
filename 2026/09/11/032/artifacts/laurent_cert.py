"""Exact Laurent-polynomial certificate for the Cilleruelo-Granville Fibonacci norm
and distance identities (lane-738 TARGET). Stdlib only, exact arithmetic in Q(sqrt5).

For fixed parity sig = (-1)^n in {+1,-1}, put u = phi^n (formal), v = psi^n = sig/u.
Binet: F_{a*n+b} = (phi^b u^a - psi^b v^a)/sqrt(5), a Laurent polynomial in u with
coefficients in Q(sqrt5). All claimed identities become Laurent-polynomial identities,
verified here by exact coefficient comparison (every coefficient must be (0,0)).

Checks:
 G1..G4: |nu_j(n)|^2 - N(n) == 0 for j=1..4, both parities (degrees <= 6 in u^{+-1}).
 H_ij:   |z_i - z_j|^2 - c*F_{2n+k} == 0 for the six pairs, both parities.
"""
from fractions import Fraction

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

def neg(p):
    return (-p[0], -p[1])

def mul(p, q):
    return (p[0]*q[0] + 5*p[1]*q[1], p[0]*q[1] + p[1]*q[0])

def inv(p):
    d = p[0]*p[0] - 5*p[1]*p[1]
    assert d != 0
    return (p[0]/d, -p[1]/d)

PHI = (Fraction(1, 2), Fraction(1, 2))
PSI = (Fraction(1, 2), Fraction(-1, 2))
INV_S5 = (Fraction(0), Fraction(1, 5))  # 1/sqrt(5)

def pw(base, k):
    if k < 0:
        return pw(inv(base), -k)
    r = ONE
    for _ in range(k):
        r = mul(r, base)
    return r

def scale(c, P):
    return {e: mul(c, v) for e, v in P.items() if v != ZERO}

def padd(P, Q):
    R = dict(P)
    for e, v in Q.items():
        R[e] = add(R.get(e, ZERO), v)
        if R[e] == ZERO:
            del R[e]
    return R

def pmul(P, Q):
    R = {}
    for e1, v1 in P.items():
        for e2, v2 in Q.items():
            e = e1 + e2
            R[e] = add(R.get(e, ZERO), mul(v1, v2))
    return {e: v for e, v in R.items() if v != ZERO}

def Fib(a, b, sig):
    """Laurent poly of F_{a*n+b} given parity sig = (-1)^n."""
    A = mul(pw(PHI, b), INV_S5)
    Bs = -1 if (sig == -1 and a % 2 == 1) else 1
    B = mul(pw(PSI, b), INV_S5)
    if Bs == -1:
        B = neg(B)
    # F = A u^a - B' v^a with v^a = sig^a u^{-a}; Bs folds sig^a into B coefficient
    R = {}
    R[a] = add(R.get(a, ZERO), A)
    R[-a] = add(R.get(-a, ZERO), neg(B))
    return {e: v for e, v in R.items() if v != ZERO}

def fib_int(k):
    x, y = 0, 1
    for _ in range(k):
        x, y = y, x + y
    return x

fails = 0
# Norm identities
for sig in (1, -1):
    A = scale((Fraction(1, 2), Fraction(0)), Fib(3, 3, sig))
    Bm = scale((Fraction(1, 2), Fraction(0)), Fib(3, 0, sig))
    Z = [
        (scale((Fraction(-2), Fraction(0)), Fib(1, -1, sig)),
         scale((Fraction(2), Fraction(0)), Fib(1, 2, sig))),
        (scale((Fraction(-1), Fraction(0)), Fib(1, -2, sig)),
         Fib(1, 1, sig)),
        (Fib(1, -1, sig),
         scale((Fraction(-1), Fraction(0)), Fib(1, 2, sig))),
        (Fib(1, 0, sig),
         scale((Fraction(-1), Fraction(0)), Fib(1, 3, sig))),
    ]
    N = scale((Fraction(5, 2), Fraction(0)),
              pmul(pmul(Fib(2, -1, sig), Fib(2, 1, sig)), Fib(2, 3, sig)))
    s = (Fraction(sig), Fraction(0))
    for j, (zx, zy) in enumerate(Z):
        nux = padd(A, pmul({0: s}, zx))
        nuy = padd(Bm, pmul({0: s}, zy))
        G = padd(padd(pmul(nux, nux), pmul(nuy, nuy)), scale((Fraction(-1), Fraction(0)), N))
        ok = (G == {})
        print(f"parity {sig:+d} nu{j+1}: {'IDENTITY' if ok else 'FAIL ' + str(G)}")
        fails += (not ok)

# Distance identities: (pair, c, k)
pairs = [((0, 1), 10, -1), ((0, 2), 18, 1), ((0, 3), 10, 3),
         ((1, 2), 2, 3), ((1, 3), 10, 1), ((2, 3), 2, -1)]
for sig in (1, -1):
    Z = [
        (scale((Fraction(-2), Fraction(0)), Fib(1, -1, sig)),
         scale((Fraction(2), Fraction(0)), Fib(1, 2, sig))),
        (scale((Fraction(-1), Fraction(0)), Fib(1, -2, sig)),
         Fib(1, 1, sig)),
        (Fib(1, -1, sig),
         scale((Fraction(-1), Fraction(0)), Fib(1, 2, sig))),
        (Fib(1, 0, sig),
         scale((Fraction(-1), Fraction(0)), Fib(1, 3, sig))),
    ]
    for (i, j), c, k in pairs:
        dx = padd(Z[i][0], scale((Fraction(-1), Fraction(0)), Z[j][0]))
        dy = padd(Z[i][1], scale((Fraction(-1), Fraction(0)), Z[j][1]))
        H = padd(padd(pmul(dx, dx), pmul(dy, dy)),
                 scale((Fraction(-c), Fraction(0)), Fib(2, k, sig)))
        ok = (H == {})
        print(f"parity {sig:+d} d{i+1}{j+1}: {'IDENTITY' if ok else 'FAIL ' + str(H)}")
        fails += (not ok)

# Spot-check Binet evaluator against integers
for m in range(0, 15):
    P = Fib(1, 0, 1)
    # evaluate at n=m is not direct (sig fixed); instead check Fib(0,b,1) == F_b
    pass
for b in range(0, 10):
    P = Fib(0, b, 1)
    assert set(P.keys()) == ({0} if fib_int(b) != 0 else set()), (b, P)
    if fib_int(b) != 0:
        assert P[0] == (Fraction(fib_int(b)), Fraction(0)), (b, P)
print("Binet evaluator spot-checks OK")
print("LAURENT_CERT_OK" if fails == 0 else "LAURENT_CERT_FAIL")
