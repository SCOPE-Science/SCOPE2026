from fractions import Fraction
import math
import random
import numpy as np

def closed_matrix(a1, a2, eta, K):
    z1 = 1.0 - eta*a1
    z2 = 1.0 - eta*a2
    p1 = z1**K
    p2 = z2**K
    s1 = sum(z1**j for j in range(K))/K
    s2 = sum(z2**j for j in range(K))/K
    return np.array([
        [(p1+p2)/2.0, K*eta*(s1-s2)/2.0],
        [(p2-p1)/(2.0*K*eta), 1.0-(s1+s2)/2.0]
    ], dtype=float)

def direct_round(x, d, a1, a2, eta, K):
    c1, c2 = d, -d
    c = 0.5*(c1+c2)
    y1 = x
    y2 = x
    for _ in range(K):
        y1 -= eta*(a1*y1 + c - c1)
        y2 -= eta*(a2*y2 + c - c2)
    xp = 0.5*(y1+y2)
    c1p = c1-c + (x-y1)/(K*eta)
    c2p = c2-c + (x-y2)/(K*eta)
    dp = 0.5*(c1p-c2p)
    return np.array([xp, dp])

def jury_values(A):
    T = np.trace(A)
    D = np.linalg.det(A)
    return 1-T+D, 1+T+D, 1-D

rng = random.Random(350052)

# Direct round agrees with the closed matrix.
for K in (1,2,3,4,7,12):
    for _ in range(50):
        eta = 10**rng.uniform(-2,0.5)
        z1 = rng.uniform(-0.95,0.95)
        z2 = rng.uniform(-0.95,0.95)
        a1 = (1-z1)/eta
        a2 = (1-z2)/eta
        x = rng.uniform(-3,3)
        d = rng.uniform(-2,2)
        A = closed_matrix(a1,a2,eta,K)
        got = direct_round(x,d,a1,a2,eta,K)
        want = A @ np.array([x,d])
        assert np.linalg.norm(got-want) < 2e-10

# Every locally contractive pair is Schur stable for arbitrary tested K.
for K in (1,2,3,4,5,8,16,31):
    for _ in range(500):
        eta = 1.0
        z1 = rng.uniform(-0.999,0.999)
        z2 = rng.uniform(-0.999,0.999)
        a1 = 1-z1
        a2 = 1-z2
        A = closed_matrix(a1,a2,eta,K)
        j = jury_values(A)
        assert min(j) > 1e-10
        rho = max(abs(np.linalg.eigvals(A)))
        assert rho < 1.0 - 1e-10

# Exact rational unstable-client witness.
K = 3
eta = Fraction(1,1)
a1 = Fraction(11,5)
a2 = Fraction(1,10)
z1 = 1-eta*a1
z2 = 1-eta*a2
assert z1 == Fraction(-6,5)
assert z2 == Fraction(9,10)
p1 = z1**K
p2 = z2**K
s1 = sum((z1**j for j in range(K)), Fraction(0,1))/K
s2 = sum((z2**j for j in range(K)), Fraction(0,1))/K
A11 = (p1+p2)/2
A12 = K*eta*(s1-s2)/2
A21 = (p2-p1)/(2*K*eta)
A22 = 1-(s1+s2)/2
assert A11 == Fraction(-999,2000)
assert A12 == Fraction(-147,200)
assert A21 == Fraction(819,2000)
assert A22 == Fraction(41,120)
T = A11+A22
D = A11*A22-A12*A21
disc = T*T-4*D
assert T == Fraction(-947,6000)
assert D == Fraction(1629,12500)
assert disc == Fraction(-17869271,36000000)
assert disc < 0
rho = math.sqrt(float(D))
assert abs(rho - 0.3609986149557918) < 1e-15
assert abs(float(p1)) > 1.0
assert rho < 1.0

print("verification passed")
