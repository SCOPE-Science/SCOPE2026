import math

beta1=0.9
beta2=0.999
eps=1e-8
eps2=0.01
clip=1.0
lam=0.001
rho=0.5
eta=1e-3

# First source Fisher bias-correction coefficient.
beta2hat=beta2*(1-beta2**0)/(1-beta2**1)
assert beta2hat == 0.0

D=eta*((1-beta1)+lam)/(1+eps2)
assert abs(D-1e-4) < 1e-18

def paper_first(theta):
    g=theta
    f1=beta2hat*1.0+(1-beta2hat)*g*g
    epshat=min(eps,eps2*abs(g))
    den=f1**rho + epshat**(2*rho)
    if den == 0.0:
        return None, f1, epshat, den
    ng=g/den
    ng=ng/max(1.0,abs(ng)/clip)
    wg=theta/den
    wg=wg/max(1.0,abs(wg)/clip)
    m=(1-beta1)*ng
    return theta-eta*(m+lam*wg), f1, epshat, den

# Exact branch formula and clipping inactivity.
for theta in (9e-7,5e-7,1e-7,-1e-7,-9e-7):
    x1,f1,eh,den=paper_first(theta)
    assert abs(f1-theta*theta) < 1e-30
    assert abs(eh-eps2*abs(theta)) < 1e-30
    assert abs(den-(1+eps2)*abs(theta)) < 1e-25
    target=theta-D*(1 if theta>0 else -1)
    assert abs(x1-target) < 1e-16
    assert (x1*x1) > (theta*theta)
    ratio=(x1/theta)**2
    closed=(D/abs(theta)-1)**2
    assert abs(ratio-closed) < 1e-8*max(1.0,closed)

# Exact stationary point is undefined in the printed real-arithmetic formula.
x1,f1,eh,den=paper_first(0.0)
assert x1 is None and f1==0.0 and eh==0.0 and den==0.0

# Relative objective amplification diverges along a sequence to zero.
prev=0.0
for k in (3,4,5,6,7,8,9):
    theta=10.0**(-k)
    if theta >= eps/eps2:
        continue
    x1,_,_,_=paper_first(theta)
    amp=(x1/theta)**2
    assert amp > prev
    prev=amp
assert prev > 1e8

# A fixed positive floor removes the constant local jump.
def safe_terms(theta, floor=1e-8):
    den=abs(theta)+floor
    return theta/den, theta/den
for theta in (1e-6,1e-8,1e-10,1e-12):
    ng,wg=safe_terms(theta)
    assert abs(ng) <= abs(theta)/1e-8 + 1e-30
    assert abs(wg) <= abs(theta)/1e-8 + 1e-30
assert abs(safe_terms(1e-12)[0]) < abs(safe_terms(1e-8)[0])

print('verification passed')
