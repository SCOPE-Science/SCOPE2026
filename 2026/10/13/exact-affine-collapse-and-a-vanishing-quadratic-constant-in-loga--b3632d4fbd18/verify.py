import math


def norm(v):
    return math.sqrt(sum(t*t for t in v))


def residual(diag, x):
    return [a*t for a,t in zip(diag,x)]


def b_times(diag, x):
    return [a*a*t for a,t in zip(diag,x)]


def step(diag, x, lam):
    return [lam/(a*a+lam)*t for a,t in zip(diag,x)]


def damping(diag, x, mu, k):
    F = residual(diag,x)
    Bx = b_times(diag,x)
    nf = norm(F)
    ng = norm(Bx)
    if nf >= 1.0:
        delta = 1.0/nf
    else:
        delta = 1.0 + 1.0/math.log(k+math.e)
    return mu*(nf**delta)/(1.0+ng**delta), delta

# Multi-mode exact-model checks.
diag=[0.7, 1.5, 2.0]
x=[2.0,-0.4,0.7]
mu=3.2
m=0.05
p2=0.9
history=[]
Lambda=3.2*math.exp(1.0/math.e)
q=Lambda/(min(a*a for a in diag)+Lambda)
for k in range(5):
    F=residual(diag,x)
    history.append(norm(F))
    lam,delta=damping(diag,x,mu,k)
    xp=step(diag,x,lam)
    Fp=residual(diag,xp)
    pred=norm(F)**2-norm(Fp)**2
    assert pred>0.0
    M=max(history[max(0,len(history)-4):])
    actual=M*M-norm(Fp)**2
    rhat=actual/pred
    assert rhat >= 1.0-1e-13
    assert rhat > p2
    assert norm(xp) <= q*norm(x)*(1.0+1e-12)
    mu_next=max(mu/4.0,m)
    expected=max(3.2/(4.0**(k+1)),m)
    assert abs(mu_next-expected) <= 1e-15*max(1.0,expected)
    mu=mu_next
    x=xp

# Scalar log-domain continuation.  Here a=m=1 after the floor is reached.
# L=-log(x)>0. Avoid forming x once it becomes tiny.
L=-math.log(0.1)
log_quad_ratios=[]
for k in range(2,45):
    eps=1.0/math.log(k+math.e)
    delta=1.0+eps
    # log lambda = -delta*L - log(1+exp(-delta*L))
    t=delta*L
    correction=0.0 if t>50.0 else math.log1p(math.exp(-t))
    loglam=-t-correction
    # log(1+lambda)
    corr2=0.0 if loglam < -50.0 else math.log1p(math.exp(loglam))
    # log x_next = -L + loglam - log(1+lambda)
    logx_next=-L+loglam-corr2
    logratio=logx_next+2.0*L
    log_quad_ratios.append(logratio)
    L=-logx_next

assert log_quad_ratios[-1] < -1e6
assert all(log_quad_ratios[j+1] < log_quad_ratios[j] for j in range(8,len(log_quad_ratios)-1))
print("VERIFY_OK")
