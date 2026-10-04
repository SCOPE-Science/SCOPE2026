import math, random

def source_adamw_step(x, v, t, h, alpha, beta2, eps, delta):
    # beta1 = 0, unit schedule multiplier, decoupled branch
    g = h*x
    v_new = beta2*v + (1.0-beta2)*g*g
    vhat = v_new/(1.0-beta2**t) if beta2 != 0.0 else v_new
    x_new = (1.0-delta)*x - alpha*g/(math.sqrt(vhat)+eps)
    return x_new, v_new, vhat

def F_memoryless(x, h, alpha, eps, delta):
    return (1.0-delta)*x - alpha*h*x/(h*abs(x)+eps)

# Exact alternating path for arbitrary beta2.
for beta2 in (0.0,0.3,0.9,0.999):
    for delta in (0.0,0.05,0.4,0.8):
        h = 3.7
        eps = 0.2
        c = (2.0-delta) + 1.3
        alpha = c*eps/h
        a = alpha/(2.0-delta) - eps/h
        assert a > 0.0
        x = a
        v = 0.0
        for t in range(1,30):
            xnew, v, vhat = source_adamw_step(x,v,t,h,alpha,beta2,eps,delta)
            assert abs(vhat-h*h*a*a) < 2e-11*max(1.0,h*h*a*a)
            assert abs(xnew + x) < 2e-11*max(1.0,a)
            x = xnew

# Global magnitude contraction below and at threshold for beta2=0.
random.seed(5)
for delta in (0.0,0.1,0.5,0.9):
    h = 2.0
    eps = 0.7
    for frac in (0.1,0.7,1.0):
        c = frac*(2.0-delta)
        alpha = c*eps/h
        for _ in range(1000):
            x = (1 if random.random()<0.5 else -1)*10.0**random.uniform(-10,8)
            xn = F_memoryless(x,h,alpha,eps,delta)
            assert abs(xn) < abs(x) + 1e-13*max(1.0,abs(x))

# Exact cycle and local two-step multiplier above threshold.
for delta in (0.0,0.05,0.4,0.9):
    h = 4.0
    eps = 0.3
    for excess in (0.01,0.2,1.0,5.0):
        c = 2.0-delta+excess
        alpha = c*eps/h
        a = alpha/(2.0-delta)-eps/h
        assert a > 0.0
        assert abs(F_memoryless(a,h,alpha,eps,delta)+a) < 2e-13
        assert abs(F_memoryless(-a,h,alpha,eps,delta)-a) < 2e-13
        d = 1.0-delta-(2.0-delta)**2/c
        assert -1.0 < d < 1.0
        mult = d*d
        for perturb in (1e-8,1e-7,1e-6):
            x0 = a + perturb
            x1 = F_memoryless(x0,h,alpha,eps,delta)
            x2 = F_memoryless(x1,h,alpha,eps,delta)
            numerical = (x2-a)/perturb
            assert abs(numerical-mult) < 2e-4

# The decay-created strip: no-decay convergent, AdamW cyclic.
h = 1.0
eps = 1.0
delta = 0.2
c = 1.9
alpha = c
assert 2.0-delta < c <= 2.0
a_decay = alpha/(2.0-delta)-eps/h
assert a_decay > 0.0
assert abs(F_memoryless(a_decay,h,alpha,eps,delta)+a_decay) < 1e-14
# Without decay the magnitude map is globally contracting at c <= 2.
for x in (1e-8,1e-4,0.1,1.0,100.0):
    assert abs(F_memoryless(x,h,alpha,eps,0.0)) < abs(x)

print("verification passed")
