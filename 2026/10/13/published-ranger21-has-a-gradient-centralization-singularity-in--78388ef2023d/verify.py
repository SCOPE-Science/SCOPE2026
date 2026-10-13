import math

d = 2
c = 2.0
b = 1.99
tau_clip = 1e-2
eps_clip = 1e-3
eps = 1e-8
beta0 = 0.9
beta1 = 0.9
eta1 = 3e-4
lam = 1e-4
q = [1/math.sqrt(2), -1/math.sqrt(2)]

def norm(v):
    return math.sqrt(sum(x*x for x in v))

def first_step_quantities(delta):
    theta = [c + delta*q[i] for i in range(d)]
    grad = [(c-b) + delta*q[i] for i in range(d)]
    clip_ratio = norm(grad) / max(norm(theta), eps_clip)
    # For the tested delta range clipping is inactive.
    assert clip_ratio < tau_clip
    mean_g = sum(grad)/d
    gc = [x-mean_g for x in grad]
    vhat = [x*x for x in gc]
    mean_vhat = sum(vhat)/d
    r = norm(theta)
    stable_vec = [
        eta1 * lam / math.sqrt(mean_vhat) * (1 - 1/r) * x
        for x in theta
    ]
    stable_displacement = [eta1*x for x in stable_vec]

    # First PNM numerator is linear in the centralized gradient.
    m1 = [(1-beta1*beta1)*x for x in gc]
    mhat = [(1+beta0)*x/(1-beta1) for x in m1]
    amp = math.hypot(1+beta0, beta0)
    adaptive = [
        mhat[i] / (amp*(math.sqrt(vhat[i])+eps))
        for i in range(d)
    ]
    return theta, gc, mean_vhat, stable_displacement, adaptive

# Exact structural identities and inverse-distance law.
scaled = []
adaptive_norms = []
for delta in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
    theta, gc, mean_vhat, stable_disp, adaptive = first_step_quantities(delta)
    assert max(abs(gc[i]-delta*q[i]) for i in range(d)) < 1e-14
    assert abs(mean_vhat-delta*delta/d) < 1e-18
    r = norm(theta)
    predicted = eta1*eta1*lam*math.sqrt(d)*abs(r-1)/abs(delta)
    actual = norm(stable_disp)
    assert abs(actual-predicted) < 1e-12*max(1.0,predicted)
    scaled.append(abs(delta)*actual)
    adaptive_norms.append(norm(adaptive))

limit = eta1*eta1*lam*math.sqrt(d)*abs(abs(c)*math.sqrt(d)-1)
assert abs(scaled[-1]-limit) < 1e-6*max(1.0,limit)
assert scaled[-1] > 0
# Stable displacement grows by about ten per decade near the singular set.
vals = []
for delta in (1e-4,1e-5,1e-6,1e-7):
    vals.append(norm(first_step_quantities(delta)[3]))
assert all(vals[i+1] > 9.9*vals[i] for i in range(len(vals)-1))

# The adaptive part remains bounded and tends toward zero as delta -> 0.
assert max(adaptive_norms) < 10
small_adaptive = norm(first_step_quantities(1e-12)[4])
assert small_adaptive < adaptive_norms[-1]

# At delta=0, GC and corrected second moment are exactly zero.
theta0 = [c,c]
grad0 = [c-b,c-b]
mean0 = sum(grad0)/d
gc0 = [x-mean0 for x in grad0]
assert gc0 == [0.0,0.0]
assert sum(x*x for x in gc0)/d == 0.0
assert abs(norm(theta0)-1.0) > 1e-6

# An epsilon safeguard makes the radial decay finite at the symmetric point.
r0 = norm(theta0)
safe_den = eps
safe_decay_norm = lam*abs(r0-1)*r0/safe_den
assert math.isfinite(safe_decay_norm)

print("verification passed")
