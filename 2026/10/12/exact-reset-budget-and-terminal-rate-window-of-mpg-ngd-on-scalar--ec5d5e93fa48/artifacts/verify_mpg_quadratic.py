import math

def update(lam, eps, L, eta0, eta1):
    tau = 2.0*eta0/L
    if lam > tau:
        return 2.0*eta1/L, True
    return (1.0+eps)*lam, False

# Exact curvature identity on a quadratic.
for L in [0.5, 2.0, 7.0]:
    for x0, x1 in [(1.2, -0.4), (3.0, 2.1), (-2.0, -1.1)]:
        d = x1-x0
        f0 = 0.5*L*x0*x0
        f1 = 0.5*L*x1*x1
        g0 = L*x0
        D = f1-f0-g0*d
        assert abs(D - 0.5*L*d*d) < 1e-12

# Positive summable sequence.
eps = [0.04/(k+1)**2 for k in range(1,50000)]
P = math.prod(1.0+e for e in eps)
L, eta0, eta1 = 3.0, 0.5, 0.49
ratio = eta0/eta1
bound = math.ceil(math.log(P)/math.log(ratio))

# Start above threshold to force a reset, then replay.
lam = 0.5
resets = 0
for e in eps:
    lam, reset = update(lam, e, L, eta0, eta1)
    resets += int(reset)
assert resets <= bound

# After a reset, terminal factors lie in the predicted window.
r = 2.0*eta1/L
tau = 2.0*eta0/L
assert r < tau
assert 0.0 <= 1.0-L*tau <= 1.0-L*r + 1e-12

# Realize a selected terminal stepsize with a positive dyadic product tail.
target = 0.995/L
Q = target/r
assert 1.0 < Q <= eta0/eta1
tail = [math.exp(math.log(Q)/(2**(m+1)))-1.0 for m in range(60)]
prod = math.prod(1.0+e for e in tail)
assert abs(r*prod-target) < 1e-12
partials = []
p=1.0
for e in tail:
    p *= 1.0+e
    partials.append(r*p)
assert max(partials) <= tau + 1e-12

# No-reset slow branch can be arbitrarily slow.
Ptail = math.prod(1.0+e for e in eps)
lam0 = 1e-6/(L*Ptail)
lam_inf = lam0*Ptail
q = abs(1.0-L*lam_inf)
assert q > 0.99999

print("VERIFY_OK")
