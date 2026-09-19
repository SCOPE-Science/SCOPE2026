import math
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import gammaln, kv
from scipy.stats import chi2, norm


def vg_density(x, m):
    # Density with mgf (1-2 t^2/m)^(-m/4), i.e. the balanced flat signed chaos.
    k = m / 4.0
    theta = math.sqrt(2.0 / m)
    ax = abs(x)
    if ax == 0.0:
        if k <= 0.5:
            return math.inf
        return math.exp(gammaln(k - 0.5) - gammaln(k) - math.log(theta)
                        - 0.5 * math.log(math.pi) - math.log(2.0))
    log_pref = (-math.log(theta) - 0.5 * math.log(math.pi) - gammaln(k)
                + (k - 0.5) * (math.log(ax) - math.log(2.0 * theta)))
    return math.exp(log_pref) * kv(k - 0.5, ax / theta)


def vg_tail(x, m):
    value, err = quad(lambda z: vg_density(z, m), x, np.inf,
                      epsabs=1e-14, epsrel=2e-10, limit=300)
    return value, err


def positive_rows():
    rows = []
    for L in [10.0, 20.0, 40.0, 80.0]:
        p_tail = math.exp(-L)
        b = norm.isf(p_tail)
        m = int(round(L ** 3))
        threshold = m + math.sqrt(2.0 * m) * b
        log_ratio = math.log(chi2.sf(threshold, m)) - math.log(norm.sf(b))
        finite_asym = math.sqrt(2.0) * b ** 3 / (3.0 * math.sqrt(m))
        rows.append((L, m, b, log_ratio, finite_asym, 4.0 / 3.0))
    return rows


def balanced_rows():
    rows = []
    for L in [6.0, 10.0, 15.0, 20.0]:
        p_tail = math.exp(-L)
        b = norm.isf(p_tail)
        m = int(round(L ** 2))
        if m % 2:
            m += 1
        tail, err = vg_tail(b, m)
        log_ratio = math.log(tail) - math.log(norm.sf(b))
        finite_asym = b ** 4 / (2.0 * m)
        rows.append((L, m, b, log_ratio, finite_asym, 2.0, err))
    return rows


print(f"SciPy {scipy.__version__}; NumPy {np.__version__}")
print("CUMULANTS AND EFFECTIVE RANK")
for m in [64, 256]:
    r4 = m
    k3_pos = 2.0 * math.sqrt(2.0) / math.sqrt(m)
    k3_bal = 0.0
    k4 = 12.0 / m
    print(f"m={m:4d}  r4={r4:4d}  kappa3(+)= {k3_pos:.12f}  "
          f"kappa3(bal)= {k3_bal:.1f}  kappa4(both)= {k4:.12f}")

print("\nPOSITIVE FLAT SPECTRUM: m=(log p)^3")
print(" L      m       b_p       exact log-tail-ratio   cubic asymptotic   limit")
for L, m, b, exact, approx, lim in positive_rows():
    print(f"{L:4.0f} {m:7d} {b:10.6f} {exact:22.12f} {approx:18.12f} {lim:9.6f}")

print("\nBALANCED SIGNED FLAT SPECTRUM: m=(log p)^2")
print(" L      m       b_p       exact log-tail-ratio   quartic asymptotic  limit")
for L, m, b, exact, approx, lim, err in balanced_rows():
    print(f"{L:4.0f} {m:7d} {b:10.6f} {exact:22.12f} {approx:19.12f} {lim:9.6f}")

print("\nGUMBEL-TRANSLATION KOLMOGOROV GAP")
def D(a):
    a = abs(a)
    if a == 0.0:
        return 0.0
    return (1.0 - math.exp(-a)) * math.exp(-a / math.expm1(a))
for a in [4.0/3.0, 2.0]:
    print(f"a={a:.12f}  D(a)={D(a):.12f}")
