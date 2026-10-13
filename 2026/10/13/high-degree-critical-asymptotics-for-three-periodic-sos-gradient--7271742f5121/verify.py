import math


def h(c):
    return math.exp(c) + 1.0 - 2.0 * math.exp(-c) - 3.0 * c


def bisect(fun, lo, hi, steps=160):
    flo = fun(lo)
    fhi = fun(hi)
    if flo == 0.0:
        return lo
    if flo * fhi >= 0.0:
        raise AssertionError((lo, hi, flo, fhi))
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        fm = fun(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def derivative_polynomial(a, k):
    return (2.0 * sum((k-j) * a ** (k+j-1) for j in range(1, k))
            - sum(j * a ** (j-1) for j in range(1, k)))


def minimizer(k):
    return bisect(lambda a: derivative_polynomial(a, k), 1.0e-14, 1.0)


def psi(a, k):
    return 2.0 + (2.0 * a ** k + 1.0) / sum(a ** j for j in range(1, k))


c = bisect(h, 0.5, 2.0)
q = math.exp(-c)
C = c * (math.exp(c) + 2.0) / (math.exp(c) - 1.0)
D = c*c * (1.0 + 2.0*q) * (1.0 + q) / (2.0 * (1.0-q)**2)
B = math.sqrt(C)
E = (D - C*C/12.0) / (2.0 * B)

assert abs(c - 1.0356584794018932) < 2.0e-15
assert abs(C - 2.7456435767327244) < 3.0e-15
assert abs(D - 2.9867777254276540) < 4.0e-15
assert abs(B - 1.6569983635274733) < 3.0e-15
assert abs(E - 0.7116978979796710) < 3.0e-15

rows = []
for k in (2, 3, 5, 10, 20, 50, 100, 500, 1000):
    a = minimizer(k)
    tau = psi(a, k)
    ck = -k * math.log(a)
    approx = 2.0 + C/k + D/(k*k)
    beta = math.acosh(tau/2.0)
    beta_approx = B / math.sqrt(k) + E / (k ** 1.5)
    rows.append((k, a, ck, tau, (tau-approx)*k**3,
                 (beta-beta_approx)*k**2.5))

if not abs(rows[-1][2] - c) < abs(rows[-3][2] - c):
    raise AssertionError("rescaled minimizer is not converging in the sampled tail")
if not max(abs(r[4]) for r in rows[-3:]) < 4.0:
    raise AssertionError("tau residual is inconsistent with cubic order")
if not max(abs(r[5]) for r in rows[-3:]) < 4.0:
    raise AssertionError("beta residual is inconsistent with k^{-5/2}")

print("VERIFY_OK")
print("c_star=%.16f C_star=%.16f D_star=%.16f B_star=%.16f E_star=%.16f" % (c,C,D,B,E))
for r in rows:
    print("k=%d a=%.15g c_k=%.15g tau=%.15g tau_scaled_res=%.9g beta_scaled_res=%.9g" % r)
