import mpmath as mp

mp.mp.dps = 90

def log_density(t, alpha, beta, lam):
    x = t/alpha
    s = x*x/2
    G = -mp.expm1(-s)
    H = G**beta
    # Additive normalization constants are unnecessary for curvature.
    return (mp.log(x) - s + (beta-1)*mp.log(G)
            - lam*H - mp.e**lam*(1-mp.e**(-lam*H)))

def curvature(t, alpha, beta, lam):
    return mp.diff(lambda z: log_density(z, alpha, beta, lam), t, 2)

# 1) Claimed region beta>1/4 contains local log-convexity.
alpha = mp.mpf("1.7")
beta = mp.mpf("0.3")
lam = mp.mpf("1.2")
for t in (mp.mpf("0.02"), mp.mpf("0.01"), mp.mpf("0.005")):
    c = curvature(t, alpha, beta, lam)
    assert c > 0
ratio = (mp.mpf("0.001")**2 * curvature(mp.mpf("0.001"), alpha, beta, lam)
         / (1-2*beta))
assert abs(ratio-1) < mp.mpf("0.05")

# 2) beta=1/2 finite boundary curvature and threshold.
beta = mp.mpf("0.5")
for lam in (mp.mpf("0.5"), mp.mpf("1.0")):
    exact_limit = (-mp.mpf("0.75") + mp.e**lam*lam*lam/2)/(alpha*alpha)
    c = curvature(mp.mpf("1e-5"), alpha, beta, lam)
    assert abs(c-exact_limit) < mp.mpf("0.01")
lam0 = mp.findroot(lambda z: z*z*mp.e**z - mp.mpf("1.5"), (mp.mpf("0.7"), mp.mpf("0.9")))
assert abs(lam0-mp.mpf("0.8148840354416833337644784875056099")) < mp.mpf("1e-30")

# 3) Exact beta=1 obstruction at t=alpha.
alpha = mp.mpf("1")
beta = mp.mpf("1")
lam = mp.mpf("2")
c = curvature(alpha, alpha, beta, lam)
closed = lam*lam*mp.e**(-1 + lam*mp.e**(-mp.mpf("0.5"))) - 2
assert abs(c-closed) < mp.mpf("1e-70")
assert c > 0
lam1 = mp.findroot(
    lambda z: z*z*mp.e**(-1 + z*mp.e**(-mp.mpf("0.5"))) - 2,
    (mp.mpf("1.4"), mp.mpf("1.6"))
)
assert abs(lam1-mp.mpf("1.4858293101896016707431485539615843")) < mp.mpf("1e-30")

print("VERIFY_OK")
print("lambda0", mp.nstr(lam0, 40))
print("lambda1", mp.nstr(lam1, 40))
print("beta1_counterexample_curvature", mp.nstr(c, 40))
print("origin_ratio_beta_0_3", mp.nstr(ratio, 30))
