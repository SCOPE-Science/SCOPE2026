from decimal import Decimal, getcontext

getcontext().prec = 60

def D(x):
    return Decimal(str(x))

def check(sigma, alpha, omega):
    sigma, alpha, omega = map(D, (sigma, alpha, omega))
    psi = (sigma + 1) / (2 * sigma)
    delta = sigma * psi * psi - (1 + alpha)
    if not (delta > 0 and omega > 0):
        raise AssertionError("requires delta>0 and omega>0")
    root = (sigma * delta).sqrt()
    c3 = (sigma * psi + root) / sigma
    phi = 2 * c3 * root

    # f(n)=n*(delta-sigma*(n-psi)^2)
    fp_c3 = delta - sigma * (c3 - psi) ** 2 - 2 * sigma * c3 * (c3 - psi)
    if abs((-fp_c3) - phi) > D("1e-48"):
        raise AssertionError("linear coefficient mismatch")

    denom = phi * phi + omega * omega
    A = alpha * c3 * omega / denom
    B = -alpha * c3 * phi / denom
    cos_res = omega * B + phi * A
    sin_res = -omega * A + phi * B + alpha * c3
    if abs(cos_res) > D("1e-48") or abs(sin_res) > D("1e-48"):
        raise AssertionError("harmonic residual mismatch")
    return psi, delta, c3, phi, denom, alpha * c3 / denom.sqrt()

for params in [(5, 0.3, 1), (8, 0.2, 0.4), (3, 0.05, 2.5)]:
    check(*params)

psi, delta, c3, phi, denom, amp = check(5, 0.3, 1)
print("psi", psi)
print("delta", delta)
print("c3", c3)
print("phi", phi)
print("phi^2+1", denom)
print("correct harmonic amplitude", amp)
print("published/correct amplitude factor", denom)
print("VERIFY_OK")
