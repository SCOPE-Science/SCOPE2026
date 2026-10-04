import math
import random

def first_direct(x, h, gamma, c, eps):
    g = h*x
    lam = gamma
    s = lam*g
    nu = lam*g*g
    z = x - s/(nu**(1.0/3.0) + eps) if nu > 0.0 else x
    return (1.0-c)*x + c*z

def first_closed(x, h, gamma, c, eps):
    if x == 0.0:
        return 0.0
    q = c*gamma*h/(gamma**(1.0/3.0)*h**(2.0/3.0)*abs(x)**(2.0/3.0)+eps)
    return (1.0-q)*x

random.seed(350054)

# Direct source recurrence versus closed form.
for _ in range(5000):
    h = 10.0**random.uniform(-4.0,4.0)
    gamma = 10.0**random.uniform(-6.0,0.0)
    c = random.uniform(1e-4,1.0)
    eps = 10.0**random.uniform(-10.0,-1.0)
    sign = -1.0 if random.random() < 0.5 else 1.0
    x = sign*10.0**random.uniform(-12.0,4.0)
    a = first_direct(x,h,gamma,c,eps)
    b = first_closed(x,h,gamma,c,eps)
    assert abs(a-b) <= 2e-11*max(1.0,abs(a),abs(b))

# Sharp globally monotone side.
for _ in range(1000):
    h = 10.0**random.uniform(-3.0,3.0)
    gamma = 10.0**random.uniform(-5.0,-1.0)
    c = random.uniform(0.01,1.0)
    # Choose epsilon at or above the exact frontier.
    eps = 0.5*c*gamma*h*random.uniform(1.0,10.0)
    for x in (-1e6,-1.0,-1e-6,-1e-12,1e-12,1e-6,1.0,1e6):
        y = first_direct(x,h,gamma,c,eps)
        assert h*y*y <= h*x*x*(1.0+2e-12)

# Violating side: exact spike radius separates increase from decrease.
for _ in range(1000):
    h = 10.0**random.uniform(-2.0,2.0)
    gamma = 10.0**random.uniform(-5.0,-1.0)
    c = random.uniform(0.02,1.0)
    eps = 0.5*c*gamma*h*random.uniform(0.01,0.99)
    r = ((c*gamma*h/2.0-eps)/(gamma**(1.0/3.0)*h**(2.0/3.0)))**1.5
    for factor,should_increase in ((0.1,True),(0.9,True),(1.1,False),(10.0,False)):
        x = factor*r
        y = first_direct(x,h,gamma,c,eps)
        if should_increase:
            assert h*y*y > h*x*x
        else:
            assert h*y*y < h*x*x

# Limiting amplification near the minimizer.
for Q in (2.1,3.0,10.0,1000.0):
    h=1.0
    gamma=0.01
    c=0.1
    eps=c*gamma*h/Q
    target=(Q-1.0)**2
    ratios=[]
    for x in (1e-12,1e-15,1e-18):
        y=first_direct(x,h,gamma,c,eps)
        ratios.append((y/x)**2)
    assert abs(ratios[-1]-target) <= 3e-3*max(1.0,target)

# Multidimensional worst-factor formula on a diagonal Hessian.
hvals=[0.5,2.0,7.0]
gamma=0.02
c=0.3
eps=1e-3
L=max(hvals)
Q=c*gamma*L/eps
closed=max(1.0,(Q-1.0)**2)
# Approach the supremum along the top-curvature coordinate near zero.
x=1e-18
y=first_direct(x,L,gamma,c,eps)
ratio=(y/x)**2
assert abs(ratio-closed) <= 3e-3*closed

print("verification passed")
