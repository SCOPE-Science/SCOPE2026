import math

def neg_log_survival_from_s(s, alpha, lam):
    G = 1.0 - s
    B = math.exp(-G * math.log(s)) - 1.0
    A = B ** alpha
    q = math.exp(-A) if A < 740.0 else 0.0
    return lam * (A + math.log(lam + (1.0 - lam) * q))

def burr_s(x, beta, k):
    return math.exp(-k * math.log1p(x ** beta))

for alpha,lam,beta,k in [
    (0.5, 2.0, 1.0, 1.0),
    (1.0, 0.8, 1.0, 1.0),
    (2.0, 0.7, 1.0, 1.0),
    (0.8, 1.5, 0.6, 2.0),
]:
    x = 1.0e8
    s = burr_s(x,beta,k)
    nls = neg_log_survival_from_s(s,alpha,lam)
    universal = nls / (lam * s ** (-alpha))
    delta = alpha*beta*k
    burr = nls / (lam * x ** delta)
    assert abs(universal - 1.0) < 2e-4, (alpha,lam,beta,k,universal)
    assert abs(burr - 1.0) < 2e-3, (alpha,lam,beta,k,burr)

for delta_case in ("sub","critical","super"):
    if delta_case == "sub":
        alpha,beta,k = 0.5,1.0,1.0
    elif delta_case == "critical":
        alpha,beta,k = 1.0,1.0,1.0
    else:
        alpha,beta,k = 2.0,1.0,1.0
    lam = 1.3
    x = 1.0e5
    s = burr_s(x,beta,k)
    nls = neg_log_survival_from_s(s,alpha,lam)
    if delta_case == "sub":
        assert 0.2*x - nls > 0.0
    elif delta_case == "critical":
        assert 0.5*x - nls < 0.0
        assert 2.0*x - nls > 0.0
    else:
        assert 10.0*x - nls < 0.0

alpha,lam,c,omega = 0.6,1.7,0.4,0.8
for x in (30.0, 50.0, 70.0):
    s = math.exp(-c*x**omega)
    nls = neg_log_survival_from_s(s,alpha,lam)
    scale = lam*math.exp(alpha*c*x**omega)
    assert abs(nls/scale - 1.0) < 0.12

print("VERIFY_OK")
