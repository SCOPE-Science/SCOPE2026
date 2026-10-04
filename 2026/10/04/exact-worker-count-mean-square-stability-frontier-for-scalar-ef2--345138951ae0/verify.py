import itertools
import math
import numpy as np

def moment_matrix(n, s):
    return np.array([
        [1.0, -2*s, s*s, 0.0],
        [0.5, 0.5-s, 0.5*(s*s-s), 0.0],
        [0.25+0.25/n,
         0.5*(1-s)-0.5*(1+s)/n,
         0.25*(1-s)*(1-s)+0.25*s*(s+2)/n,
         0.25/n],
        [0.5, -s, 0.5*s*s, 0.5],
    ], dtype=float)

def rho(n, s):
    vals = np.linalg.eigvals(moment_matrix(n,s))
    return max(abs(z) for z in vals)

# Symbolic determinant identity checked by direct numerical determinants at exact formula points.
for n in range(1, 21):
    for s in (0.1, 0.3, 0.7, 1.1, 2.3, 4.7):
        lhs = np.linalg.det(np.eye(4)-moment_matrix(n,s))
        rhs = s*(6*n-(n+8)*s)/(16*n)
        assert abs(lhs-rhs) < 2e-10*(1+abs(rhs)), (n,s,lhs,rhs)

# Spectral radius crosses one at the claimed point.
for n in range(1, 101):
    cap = 6*n/(n+8)
    assert rho(n, 0.999*cap) < 1.0
    assert rho(n, 1.001*cap) > 1.0

# Monotonicity and limit.
prev = 0.0
for n in range(1,1000):
    cap = 6*n/(n+8)
    assert cap > prev
    prev = cap
assert abs(6*100000/(100000+8) - (6-48/100000)) < 1e-7

# Direct enumeration of all half-dropout outcomes validates conditional second moments.
def direct_one_step(x, hs, s):
    n = len(hs)
    m = sum(hs)/n
    xp = x-s*m
    outs = []
    for bits in itertools.product((0,1), repeat=n):
        hp = [h + b*(xp-h) for h,b in zip(hs,bits)]
        mp = sum(hp)/n
        qp = sum(h*h for h in hp)/n
        outs.append((xp,mp,qp))
    w = 1/(2**n)
    return (
        sum(w*a*a for a,b,c in outs),
        sum(w*a*b for a,b,c in outs),
        sum(w*b*b for a,b,c in outs),
        sum(w*c for a,b,c in outs),
    )

for n in range(1,5):
    hs = [0.2 + 0.13*i for i in range(n)]
    x = 1.1
    s = 0.73
    X,C,M,Q = x*x, x*sum(hs)/n, (sum(hs)/n)**2, sum(h*h for h in hs)/n
    pred = moment_matrix(n,s) @ np.array([X,C,M,Q])
    got = np.array(direct_one_step(x,hs,s))
    assert np.max(np.abs(pred-got)) < 1e-12

# Infinite-worker deterministic matrix has exact ceiling 6.
def rho_inf(s):
    A=np.array([[1.0,-s],[0.5,0.5*(1-s)]])
    return max(abs(z) for z in np.linalg.eigvals(A))
assert rho_inf(5.999) < 1.0
assert rho_inf(6.001) > 1.0

print("verification passed")
