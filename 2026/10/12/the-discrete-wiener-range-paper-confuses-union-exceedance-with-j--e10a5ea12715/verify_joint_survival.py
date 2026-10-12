from math import prod

def published_survival(Fs):
    return 1.0 - prod(Fs)

def joint_strict_survival(Fs):
    return prod(1.0-f for f in Fs)

# Diagnostic half-CDF example.
Fs = [0.5, 0.5]
assert abs(published_survival(Fs) - 0.75) < 1e-15
assert abs(joint_strict_survival(Fs) - 0.25) < 1e-15

# Equal-tail identity and divergence.
for s in [0.1, 0.01, 1e-4, 1e-7]:
    pub = published_survival([1-s, 1-s])
    co = s*s
    exact_ratio = 2.0/s - 1.0
    assert abs(pub/co - exact_ratio) / exact_ratio < 1e-9
assert published_survival([1-1e-7,1-1e-7]) / (1e-7**2) > 1e7

# n-dimensional equal-tail formula.
for n in range(2, 7):
    s = 1e-3
    pub = 1-(1-s)**n
    co = s**n
    assert pub > co

# Discrete geometric example for the hazard event.
# P(X=k)=p*q^k on k=0,1,..., P(X>=k)=q^k.
p = 0.5
q = 1-p
r1 = r2 = 2
cell1 = p*q**r1
cell2 = p*q**r2
joint_cell = cell1*cell2

inclusive_joint_survival = (q**r1)*(q**r2)
correct_joint_hazard = joint_cell/inclusive_joint_survival
assert abs(correct_joint_hazard - p*p) < 1e-15

# Paper-style denominator using 1-F_joint at the same coordinates.
F1 = 1-q**(r1+1)
F2 = 1-q**(r2+1)
paper_style = joint_cell/(1-F1*F2)
assert abs(paper_style-correct_joint_hazard) > 0.1

print("VERIFY_OK")
print("half_cdf_published_survival", published_survival([0.5,0.5]))
print("half_cdf_true_co_survival", joint_strict_survival([0.5,0.5]))
print("tail_ratio_s_1e-7", published_survival([1-1e-7,1-1e-7])/(1e-7**2))
print("geometric_correct_joint_hazard", correct_joint_hazard)
print("geometric_paper_style_ratio", paper_style)
