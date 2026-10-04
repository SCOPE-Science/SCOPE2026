from fractions import Fraction as F

# Spectral data for A=diag(1,2,4), b=(sqrt(5),sqrt(15),1).
lam = [F(1), F(2), F(4)]
weights = [F(5,21), F(15,21), F(1,21)]

assert sum(weights, F(0)) == 1

alpha1 = sum(w*l for w,l in zip(weights, lam))
m2 = sum(w*l*l for w,l in zip(weights, lam))
beta1_sq = m2 - alpha1*alpha1
alpha2 = (
    sum(w*l*(l-alpha1)**2 for w,l in zip(weights,lam))
    / beta1_sq
)

assert alpha1 == F(13,7)
assert beta1_sq == F(20,49)
assert alpha2 == F(37,14)

# Characteristic polynomial of T2:
# z^2 - trace*z + determinant.
trace = alpha1 + alpha2
det = alpha1*alpha2 - beta1_sq
assert trace == F(9,2)
assert det == F(9,2)

theta1 = F(3,2)
theta2 = F(3)
for theta in (theta1, theta2):
    assert theta*theta - trace*theta + det == 0

# At t0=(2/3) log(4):
# exp(-theta1*t0)=1/4 and exp(-theta2*t0)=1/16.
f1 = F(1,4)
f2 = F(1,16)
slope = (f2-f1)/(theta2-theta1)
intercept = f1 - slope*theta1
assert slope == F(-1,8)
assert intercept == F(7,16)

def q(l):
    return intercept + slope*l

assert q(F(1)) == F(5,16)
assert q(F(2)) == F(3,16)
assert q(F(4)) == F(-1,16)
assert q(F(1)) > 0 and q(F(2)) > 0 and q(F(4)) < 0

# The threshold t* satisfies
# exp((theta2-theta1)*t*)=(L-theta1)/(L-theta2)=5/2.
# At t0 the same exponential is 4, so t0>t* exactly.
L = F(4)
threshold_ratio = (L-theta1)/(L-theta2)
t0_ratio = F(4)
assert threshold_ratio == F(5,2)
assert t0_ratio > threshold_ratio

print("VERIFY_OK")
