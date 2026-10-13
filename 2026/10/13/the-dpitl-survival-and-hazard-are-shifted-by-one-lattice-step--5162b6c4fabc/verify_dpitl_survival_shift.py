import mpmath as mp

mp.mp.dps = 70

def S(w, kappa, eta):
    w = mp.mpf(w)
    return ((1 + 2*w**eta) / (1 + w**eta)**2)**kappa

def p(w, kappa, eta):
    return S(w,kappa,eta)-S(w+1,kappa,eta)

def h_true(w, kappa, eta):
    return p(w,kappa,eta)/S(w,kappa,eta)

def h_source(w, kappa, eta):
    return p(w,kappa,eta)/S(w+1,kappa,eta)

kappa = mp.mpf("3")
eta = mp.mpf("1")

# Exact first-cell hazard mismatch.
assert abs(S(0,kappa,eta)-1) < mp.mpf("1e-65")
assert abs(S(1,kappa,eta)-mp.mpf(27)/64) < mp.mpf("1e-65")
ht = h_true(0,kappa,eta)
hs = h_source(0,kappa,eta)
assert abs(ht-mp.mpf(37)/64) < mp.mpf("1e-65")
assert abs(hs-mp.mpf(37)/27) < mp.mpf("1e-65")
assert hs > 1
assert abs(hs-ht/(1-ht)) < mp.mpf("1e-65")

# Hazard/odds relation at additional points and parameters.
for K,E in [(mp.mpf("0.7"),mp.mpf("2")),
            (mp.mpf("2.2"),mp.mpf("0.8")),
            (mp.mpf("5"),mp.mpf("1.5"))]:
    for w in range(5):
        ht = h_true(w,K,E)
        hs = h_source(w,K,E)
        assert 0 <= ht <= 1
        assert abs(hs-ht/(1-ht)) < mp.mpf("1e-55")

# Direct PGF versus correct and shifted survival formulas.
t = mp.mpf("0.7")
direct = mp.nsum(lambda n: t**n*p(n,kappa,eta), [0, mp.inf])
pgf_correct = 1 + (t-1)*mp.nsum(lambda n: t**(n-1)*S(n,kappa,eta), [1, mp.inf])
pgf_shifted = 1 + (t-1)*mp.nsum(lambda n: t**(n-1)*S(n+1,kappa,eta), [1, mp.inf])
assert abs(direct-pgf_correct) < mp.mpf("1e-45")
assert abs(direct-pgf_shifted) > mp.mpf("1e-3")

# Mean: direct PMF, correct tail sum, and paper's shifted series.
mean_direct = mp.nsum(lambda n: n*p(n,kappa,eta), [0, mp.inf])
mean_correct = mp.nsum(lambda n: S(n,kappa,eta), [1, mp.inf])
mean_shifted = mp.nsum(lambda n: S(n+1,kappa,eta), [1, mp.inf])
assert abs(mean_direct-mean_correct) < mp.mpf("1e-40")
assert abs((mean_correct-mean_shifted)-S(1,kappa,eta)) < mp.mpf("1e-45")
assert abs(mean_correct-mp.mpf("0.83279988961886640328")) < mp.mpf("1e-20")
assert abs(mean_shifted-mp.mpf("0.41092488961886640328")) < mp.mpf("1e-20")

print("VERIFY_OK")
print("true_hazard_w0", mp.nstr(h_true(0,kappa,eta), 35))
print("source_hazard_w0", mp.nstr(h_source(0,kappa,eta), 35))
print("direct_pgf_t07", mp.nstr(direct, 35))
print("correct_pgf_t07", mp.nstr(pgf_correct, 35))
print("shifted_pgf_t07", mp.nstr(pgf_shifted, 35))
print("true_mean", mp.nstr(mean_correct, 35))
print("source_shifted_mean", mp.nstr(mean_shifted, 35))
print("mean_difference", mp.nstr(mean_correct-mean_shifted, 35))
