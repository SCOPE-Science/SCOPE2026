#!/usr/bin/env python3
from fractions import Fraction as F

r1=F(3)
r2=F(2)
r0=F(1)
a1=a2=F(1)
d12=F(1)
d21=F(0)
sigma1=sigma2=F(1)
lam1=lam2=F(0)
alpha=F(1)
f=g=m=F(1)
h=F(2)
ue=F(1)
ce=F(1,2)
c0=F(1,4)

# Exact environmental equilibrium.
assert f*ce-(g+m)*c0 == 0
assert -h*ce+ue == 0
assert F(0) <= ce <= F(1)
assert F(0) <= c0 <= F(1)
assert f <= g+m
assert ue < h

# Effective patch rates at lambda1=lambda2=0.
R1 = r1-r0*c0-d12
R2 = r2-d21
assert R1 == F(7,4)
assert R2 == F(2)

hyp1 = R1-sigma1*sigma1/F(2)
hyp2 = R2-sigma2*sigma2/F(2)
assert hyp1 == F(5,4) and hyp1 > 0
assert hyp2 == F(3,2) and hyp2 > 0

# Patch 1 decouples because d21=0. Source Lemma 2.3 applies with
# effective scalar logistic coefficient R1, self-limitation a1, noise sigma1.
actual_mean = (R1-sigma1*sigma1/F(2))/a1
proof_bound = actual_mean
displayed_bound = (r1-sigma1*sigma1/F(2))/a1

assert actual_mean == F(5,4)
assert proof_bound == F(5,4)
assert displayed_bound == F(5,2)
assert actual_mean < displayed_bound

print("VERIFY_OK")
print("R1", R1)
print("R2", R2)
print("actual_mean", actual_mean)
print("proof_bound", proof_bound)
print("displayed_theorem_bound", displayed_bound)
