import math

# Positive conditional lifetime law H: mass 0.3 at 1 and 0.7 at 4.
support = [1.0, 4.0]
weights = [0.3, 0.7]
mu = sum(w*x for w,x in zip(weights,support))
assert abs(mu-3.1) < 1e-15

def laplace_H(lam):
    return sum(w*math.exp(-lam*x) for w,x in zip(weights,support))

def profile_from_H(lam):
    return mu/(1-laplace_H(lam)) - 1/lam

# Reconstruct the transform from the profile.
for lam in [0.05,0.1,0.3,0.7,1.0,3.0,10.0]:
    r = profile_from_H(lam)
    rec = 1-mu/(r+1/lam)
    assert abs(rec-laplace_H(lam)) < 2e-14

# Direct unconditional computation with different positive-mass probabilities.
# T=0 with probability 1-p, and T~H with probability p.
for lam in [0.1,0.7,2.0,7.0]:
    target = profile_from_H(lam)
    for p in [0.2,0.8,1.0]:
        ET = p*mu
        den = p*(1-laplace_H(lam))
        num = ET-den/lam
        direct = num/den
        assert abs(direct-target) < 2e-14

# Complete-data estimator identity and zero-observation invariance.
sample_positive = [1.0,1.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,1.0]
sample_with_zeros = [0.0,0.0,0.0] + sample_positive

def empirical_profile(xs,lam):
    numerator = sum(xs)
    denominator = sum(1-math.exp(-lam*x) for x in xs)
    return numerator/denominator - 1/lam

for lam in [0.1,0.5,1.5,5.0]:
    a=empirical_profile(sample_positive,lam)
    b=empirical_profile(sample_with_zeros,lam)
    assert abs(a-b) < 1e-14

# High-rate convergence toward the positive conditional mean.
for lam in [20.0,50.0,100.0]:
    r=profile_from_H(lam)
    assert abs((r + 1/lam)-mu) < 1e-7

print("VERIFY_OK")
print("positive_conditional_mean", format(mu,".15f"))
for lam in [0.1,0.7,1.0,3.0,10.0]:
    r=profile_from_H(lam)
    rec=1-mu/(r+1/lam)
    print("rate_profile_reconstructed_L", format(lam,".3f"), format(r,".15f"), format(rec,".15f"))
print("zero_inflation_profiles_equal", True)
print("empirical_zero_invariance", True)
