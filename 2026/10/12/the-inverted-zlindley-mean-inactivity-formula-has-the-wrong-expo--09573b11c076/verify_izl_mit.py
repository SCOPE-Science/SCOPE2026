import mpmath as mp

mp.mp.dps = 80

def F(t, alpha):
    return (1 + alpha/(2*(1+alpha)*t)) * mp.e**(-alpha/t)

def numerator_direct(t, alpha):
    # Substitute u=alpha/y to avoid endpoint stiffness.
    z = alpha/t
    return alpha*mp.quad(lambda u: mp.e**(-u)/u**2, [z, mp.inf]) + \
           alpha/(2*(1+alpha))*mp.quad(lambda u: mp.e**(-u)/u, [z, mp.inf])

def numerator_correct(t, alpha):
    z = alpha/t
    return alpha*mp.gammainc(-1, z, mp.inf) + alpha/(2*(1+alpha))*mp.e1(z)

def numerator_source(t, alpha):
    z = alpha/t
    return alpha*mp.gammainc(-1, z, mp.inf) + alpha/(2*(1+alpha))*mp.ei(-z)

for alpha, t in [
    (mp.mpf("1"), mp.mpf("0.1")),
    (mp.mpf("0.7"), mp.mpf("0.3")),
    (mp.mpf("2.5"), mp.mpf("0.8")),
]:
    d = numerator_direct(t, alpha)
    c = numerator_correct(t, alpha)
    assert abs(d-c) < mp.mpf("1e-65")

alpha = mp.mpf("1")
t = mp.mpf("0.1")
true_mit = numerator_correct(t, alpha)/F(t, alpha)
source_mit = numerator_source(t, alpha)/F(t, alpha)
assert abs(true_mit-mp.mpf("0.00895071415575969674084218233576")) < mp.mpf("1e-30")
assert abs(source_mit-mp.mpf("-0.00412976212135288638431064848801")) < mp.mpf("1e-30")
assert true_mit > 0
assert source_mit < 0

# Standard sign identity.
for z in [mp.mpf("0.2"), mp.mpf("1"), mp.mpf("10")]:
    assert abs(mp.e1(z) + mp.ei(-z)) < mp.mpf("1e-70")

# Small-time asymptotic ratios.
alpha = mp.mpf("1.7")
for t in [mp.mpf("0.02"), mp.mpf("0.01"), mp.mpf("0.005")]:
    m = numerator_correct(t, alpha)/F(t, alpha)
    mpub = numerator_source(t, alpha)/F(t, alpha)
    assert m > 0 and mpub < 0
ratio_true = alpha*(numerator_correct(mp.mpf("0.002"),alpha)/F(mp.mpf("0.002"),alpha))/mp.mpf("0.002")**2
ratio_pub = alpha*(numerator_source(mp.mpf("0.002"),alpha)/F(mp.mpf("0.002"),alpha))/mp.mpf("0.002")**2
assert abs(ratio_true-1) < mp.mpf("0.02")
assert abs(ratio_pub+1) < mp.mpf("0.02")

print("VERIFY_OK")
print("mit_true_alpha1_t01", mp.nstr(true_mit, 40))
print("mit_source_alpha1_t01", mp.nstr(source_mit, 40))
print("small_time_true_ratio", mp.nstr(ratio_true, 30))
print("small_time_source_ratio", mp.nstr(ratio_pub, 30))
