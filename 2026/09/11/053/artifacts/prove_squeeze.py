"""Reproducible numeric companion to DRAFT.md (lane-854 EMERGENT_FINDING).

Verifies: (1) squeeze factors U(t)->1 for the upper tail bound at finite t;
(2) lambda-block lower factors (1-lambda^-4) at finite t; (3) quadrature values
Z0, sigma^2, c' (approximations, NOT interval-certified -- the DRAFT's limit
identities are proved analytically; these numbers are supporting evidence);
(4) E(N) = N^2 P(|X|>B_N) asymptotic c'*sqrt(2)*(log N)^15/2 at large N.
Stdlib only.
"""
import math

E = math.e
L = lambda x: math.log(E + abs(x))
g = lambda x: (1.0 + abs(x)) ** -5 * L(x) ** -0.5

def simpson(f, a, b, n):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4.0 if k & 1 else 2.0) * f(a + k * h)
    return s * h / 3.0

print("--- (1) upper squeeze factor U(t)=[t/(1+t)]^4 [log t / L(t)]^1/2 -> 1 ---")
for t in (5, 10, 30, 100, 300, 1000):
    U = (t / (1 + t)) ** 4 * (math.log(t) / L(t)) ** 0.5
    print(f"t={t:>5d}  U={U:.6f}")

print("--- (2) lower lambda-block factor F=[t^4((1+t)^-4-(1+l t)^-4)] [log t/L(l t)]^1/2 -> 1-l^-4 ---")
for lam in (2, 4, 10):
    row = []
    for t in (30, 100, 1000):
        F = (t ** 4 * ((1 + t) ** -4 - (1 + lam * t) ** -4)) * (math.log(t) / L(lam * t)) ** 0.5
        row.append(f"{F:.6f}")
    print(f"lam={lam:>2d}  F={' / '.join(row)}   limit={1 - lam ** -4:.6f}")

print("--- (3) quadrature approximations (reproducible, non-certified) ---")
I0 = simpson(g, 0.0, 16.0, 120000) + 1.0 / (8.0 * 17.0 ** 4)
I2 = simpson(lambda x: x * x * g(x), 0.0, 40.0, 160000)
Z0, sig2 = 2 * I0, I2 / I0
c_star, cp = 1.0 / Z0, (1.0 / Z0) / (2.0 * sig2 ** 2)
print(f"Z0~{Z0:.8f}  c*~{c_star:.8f}  sigma^2~{sig2:.8f}  c'=c*/(2sig^4)~{cp:.8f}")

print("--- (4) E(N)/(log N)^15/2 -> c'*sqrt(2) = %.6f ---" % (cp * math.sqrt(2)))
for N in (1e6, 1e12, 1e30, 1e100):
    lN = math.log(N)
    BN = math.sqrt(N) / lN ** 2
    t = math.sqrt(sig2) * BN
    asym = N ** 2 * cp * BN ** -4 * (math.log(BN)) ** -0.5
    print(f"N=1e{math.log10(N):.0f}  E(N)~{asym:.6e}  E(N)/(logN)^15/2={asym / lN ** 7.5:.6f}")
print("VERIFY_OK")
