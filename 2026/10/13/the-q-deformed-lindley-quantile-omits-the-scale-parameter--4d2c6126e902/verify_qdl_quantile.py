import mpmath as mp

mp.mp.dps = 80

def qexp(x, q):
    base = 1 + (1-q)*x
    if base <= 0:
        raise ValueError("outside real q-exponential domain")
    return base**(1/(1-q))

def cdf_true(x, theta, q):
    A = 1 + (3-2*q)*theta
    b = (2-q)*theta
    E = qexp(-theta*x, q)
    return 1 - (1 + b*x/A)*E**(2-q)

def cdf_printed_inverse_target(x, theta, q):
    A0 = 1 + (3-2*q)
    b = (2-q)*theta
    E = qexp(-theta*x, q)
    return 1 - (1 + b*x/A0)*E**(2-q)

def qlambert_lower(xi, r):
    # Lower real branch of w*qexp(w,r)=xi for r<2 and xi in (minimum,0).
    wstar = -1/(2-r)
    def g(w):
        return w*qexp(w, r)
    gstar = g(wstar)
    if abs(xi-gstar) < mp.mpf("1e-70"):
        return wstar
    if not (gstar < xi < 0):
        raise ValueError((xi, gstar, r))
    if r < 1:
        left = -1/(1-r) + mp.mpf("1e-60")
    else:
        left = mp.mpf("-1")
        while g(left) < xi:
            left *= 2
    right = wstar
    for _ in range(500):
        mid = (left+right)/2
        if g(mid) > xi:
            left = mid
        else:
            right = mid
    return (left+right)/2

def lambert_formula(u, theta, q, A):
    qp = 1/(2-q)
    kappa = 1 + (1-qp)*A
    if kappa <= 0:
        raise ValueError("shift representation is not real")
    xi = -A*(1-u)/(kappa*qexp(A, qp))
    w = qlambert_lower(xi, qp)
    return -(A+kappa*w)/((2-q)*theta)

pairs = [
    (mp.mpf("1.5"), mp.mpf("1.1")),
    (mp.mpf("0.75"), mp.mpf("0.85")),
    (mp.mpf("0.4"), mp.mpf("1.4")),
    (mp.mpf("0.15"), mp.mpf("-0.5")),
]

expected_true_cdf_at_printed_median = [
    mp.mpf("0.538808396481169335535236596569"),
    mp.mpf("0.475426435703481976443041122081"),
    mp.mpf("0.452340867985052804889827069005"),
    mp.mpf("0.378732658184916586114081024564"),
]

for (theta, q), target in zip(pairs, expected_true_cdf_at_printed_median):
    A0 = 1 + (3-2*q)
    Ath = 1 + (3-2*q)*theta
    b = (2-q)*theta

    qpub = lambert_formula(mp.mpf("0.5"), theta, q, A0)
    assert abs(cdf_printed_inverse_target(qpub, theta, q)-mp.mpf("0.5")) < mp.mpf("1e-55")

    true_at_qpub = cdf_true(qpub, theta, q)
    assert abs(true_at_qpub-target) < mp.mpf("1e-28")

    E = qexp(-theta*qpub, q)
    residual = b*qpub*E**(2-q)*(1/A0-1/Ath)
    assert abs((true_at_qpub-mp.mpf("0.5"))-residual) < mp.mpf("1e-55")

    qcorr = lambert_formula(mp.mpf("0.5"), theta, q, Ath)
    assert abs(cdf_true(qcorr, theta, q)-mp.mpf("0.5")) < mp.mpf("1e-55")

# On theta=1 the printed and correct constants coincide.
theta = mp.mpf("1")
q = mp.mpf("1.2")
A0 = 1 + (3-2*q)
Ath = 1 + (3-2*q)*theta
assert A0 == Ath
for u in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9")):
    qpub = lambert_formula(u, theta, q, A0)
    assert abs(cdf_true(qpub, theta, q)-u) < mp.mpf("1e-55")

# Missing domain restriction for the corrected shifted formula.
q = mp.mpf("1.4")
theta = mp.mpf("3")
Ath = 1 + (3-2*q)*theta
qp = 1/(2-q)
kappa = 1 + (1-qp)*Ath
assert 1 < q < mp.mpf("1.5")
assert theta > 0
assert kappa < 0

# The distribution's CDF itself is still proper on this admissible pair.
for x in (mp.mpf("0"), mp.mpf("1"), mp.mpf("10"), mp.mpf("100")):
    F = cdf_true(x, theta, q)
    assert 0 <= F < 1
assert cdf_true(mp.mpf("1e8"), theta, q) > mp.mpf("0.99")

print("VERIFY_OK")
for theta, q in pairs:
    A0 = 1 + (3-2*q)
    Ath = 1 + (3-2*q)*theta
    qpub = lambert_formula(mp.mpf("0.5"), theta, q, A0)
    qcorr = lambert_formula(mp.mpf("0.5"), theta, q, Ath)
    print(
        "pair", mp.nstr(theta,10), mp.nstr(q,10),
        "Qpub", mp.nstr(qpub,24),
        "Ftrue_Qpub", mp.nstr(cdf_true(qpub,theta,q),24),
        "Qcorr", mp.nstr(qcorr,24)
    )
print("domain_example_kappa", mp.nstr(kappa,24))
