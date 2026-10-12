import math
import mpmath as mp

mp.mp.dps = 70

def loglik(p, xs):
    p = mp.mpf(p)
    m = max(mp.mpf(x) for x in xs)
    if p <= max(mp.mpf("0"), m-1):
        return mp.ninf
    s = mp.mpf(len(xs))*mp.log(p) - mp.mpf(len(xs))*mp.log(p+1)
    for x in xs:
        x = mp.mpf(x)
        s += (p-1)*mp.log(1-x/(p+1))
    return s

def likelihood(p, xs):
    v = loglik(p, xs)
    return mp.e**v if mp.isfinite(v) else mp.mpf("0")

def cdf(x, p):
    x = mp.mpf(x); p = mp.mpf(p)
    if x <= 0:
        return mp.mpf("0")
    if x >= p+1:
        return mp.mpf("1")
    return 1-(1-x/(p+1))**p

# Boundary trichotomy.
small = [mp.mpf("0.2"), mp.mpf("0.7")]
mid = [mp.mpf("1.1"), mp.mpf("1.5")]
large = [mp.mpf("1.0"), mp.mpf("3.0")]

assert likelihood(mp.mpf("1e-8"), small) < mp.mpf("1e-14")
p0_mid = max(mid)-1
assert likelihood(p0_mid+mp.mpf("1e-10"), mid) > mp.mpf("1e4")
p0_large = max(large)-1
assert likelihood(p0_large+mp.mpf("1e-10"), large) < mp.mpf("1e-8")

# Large-p limit for representative samples.
for xs in [small, mid, large, [mp.mpf("0.5"),mp.mpf("1.0"),mp.mpf("3.0")]]:
    target = -sum(xs)
    assert abs(loglik(mp.mpf("1e8"), xs)-target) < mp.mpf("1e-6")

# One-observation stress test.
assert loglik(mp.mpf("5.9744358963916538"), [mp.mpf("3")]) > mp.mpf("-3")
assert likelihood(mp.mpf("2.0000000001"), [mp.mpf("3")]) < mp.mpf("1e-8")

# Exact probability used for the source's p=5.3245, n=20 simulation regime.
p = mp.mpf("5.3245")
prob = 1-cdf(mp.mpf("2"),p)**20
assert abs(prob-mp.mpf("0.9412282298523752040628")) < mp.mpf("1e-20")

# Published real-data observations.
d1 = [
mp.mpf(x) for x in (
"0.047 0.115 0.121 0.132 0.164 0.197 0.203 0.260 0.282 0.296 0.334 "
"0.395 0.458 0.466 0.501 0.507 0.529 0.534 0.540 0.641 0.644 0.696 "
"0.841 0.863 1.099 1.219 1.271 1.326 1.447 1.485 1.553 1.581 1.589 "
"2.178 2.343 2.416 2.444 2.825 2.830 3.578 3.658"
).split()
]
d2 = [
mp.mpf(x) for x in (
"0.02 0.09 0.18 0.19 0.20 0.23 0.24 0.24 0.29 0.34 0.35 0.36 "
"0.38 0.40 0.42 0.43 0.52 0.54 0.56 0.60 0.60 0.63 0.65 0.10 "
"0.12 0.67 0.68 0.72 0.72 0.72 0.73 0.03 0.04 0.79 0.79 0.80 "
"0.80 0.83 0.85 0.90 0.92 0.10 0.95 0.99 1.00 1.01 1.02 1.03 "
"1.05 1.10 1.10 0.07 1.11 1.15 1.18 1.20 1.29 1.31 1.33 1.34 "
"1.40 0.01 1.43 0.11 0.11 1.45 1.50 1.51 1.52 0.06 0.08 1.53 "
"1.54 1.54 0.03 1.55 1.58 1.60 1.63 1.64 1.80 0.01 1.80 1.81 "
"2.02 2.05 0.09 0.13 2.14 2.17 2.33 0.02 0.05 3.03 3.03 0.07 "
"3.34 4.20 4.69 0.02 7.89"
).split()
]

assert len(d1) == 41 and max(d1) == mp.mpf("3.658") and abs(sum(d1)-mp.mpf("44.608")) < mp.mpf("1e-50")
assert len(d2) == 101 and max(d2) == mp.mpf("7.89") and abs(sum(d2)-mp.mpf("103.51")) < mp.mpf("1e-50")

ll1_20 = loglik(mp.mpf("20"), d1)
ll2_20 = loglik(mp.mpf("20"), d2)
assert ll1_20 > mp.mpf("-49.20")
assert ll2_20 > mp.mpf("-126.50")
assert abs(ll1_20-mp.mpf("-44.4074950234584")) < mp.mpf("1e-12")
assert abs(ll2_20-mp.mpf("-104.362922989487")) < mp.mpf("1e-12")

# The source's displayed boundary values equal maximum minus one and have zero lower-boundary likelihood.
assert max(d1)-1 == mp.mpf("2.658")
assert max(d2)-1 == mp.mpf("6.89")
assert likelihood(mp.mpf("2.658")+mp.mpf("1e-12"), d1) < mp.mpf("1e-10")
assert likelihood(mp.mpf("6.89")+mp.mpf("1e-12"), d2) < mp.mpf("1e-20")

print("VERIFY_OK")
print("prob_M20_gt_2", mp.nstr(prob, 30))
print("dataset1_n_max_sum", len(d1), mp.nstr(max(d1),10), mp.nstr(sum(d1),10))
print("dataset1_loglik_p20", mp.nstr(ll1_20, 30))
print("dataset2_n_max_sum", len(d2), mp.nstr(max(d2),10), mp.nstr(sum(d2),10))
print("dataset2_loglik_p20", mp.nstr(ll2_20, 30))
