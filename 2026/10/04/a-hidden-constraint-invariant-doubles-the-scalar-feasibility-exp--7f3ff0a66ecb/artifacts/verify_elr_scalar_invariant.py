import math

def rk4_step(fun, s, y, h):
    k1 = fun(s, y)
    k2 = fun(s + h/2, [y[i] + h*k1[i]/2 for i in range(len(y))])
    k3 = fun(s + h/2, [y[i] + h*k2[i]/2 for i in range(len(y))])
    k4 = fun(s + h, [y[i] + h*k3[i] for i in range(len(y))])
    return [y[i] + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6 for i in range(len(y))]

def full_rhs(mu):
    def f(s, y):
        x, zx, lam, zl = y
        return [(zx-x)/s, -(mu*x+zl), (zl-lam)/s, zx]
    return f

def red_rhs(mu, invariant):
    def f(s, y):
        w, wp = y
        return [wp, invariant - (1 + mu/s)*w]
    return f

def integrate(fun, s0, y0, s1, h):
    s=s0
    y=list(y0)
    out=[(s, list(y))]
    while s < s1 - 1e-15:
        hh=min(h, s1-s)
        y=rk4_step(fun,s,y,hh)
        s+=hh
        out.append((s,list(y)))
    return out

for mu, init in [
    (0.7, [0.4, -0.2, 0.1, 0.05]),
    (2.0, [-0.3, 0.7, -0.4, 0.25]),
]:
    s0=1.3
    inv=s0*init[0]-init[3]
    full=integrate(full_rhs(mu),s0,init,80.0,0.002)
    red=integrate(red_rhs(mu,inv),s0,[s0*init[0],init[1]],80.0,0.002)
    max_inv=max(abs(s*y[0]-y[3]-inv) for s,y in full)
    assert max_inv < 2e-7
    # Compare w=s*x from the full system with the independently reduced oscillator.
    max_gap=max(abs(s*yf[0]-yr[0]) for (s,yf),(_,yr) in zip(full,red))
    assert max_gap < 3e-6
    max_w=max(abs(s*y[0]) for s,y in full)
    assert max_w < 10.0

# Sharp family I=0: choose z_lambda=s0*x initially.
mu=1.25
s0=1.0
x0=0.6
zl0=s0*x0
init=[x0,0.0,0.2,zl0]
full=integrate(full_rhs(mu),s0,init,120.0,0.002)
inv=s0*x0-zl0
assert abs(inv) < 1e-15
tail=[abs(s*y[0]) for s,y in full if s > 100.0]
assert max(tail) > 0.15
# Energy lower bound for I=0, checked numerically.
def energy(s, y):
    w=s*y[0]
    wp=y[1]
    q=1+mu/s
    return 0.5*wp*wp+0.5*q*w*w
e0=energy(s0,init)
emin=min(energy(s,y) for s,y in full)
assert emin >= e0/(1+mu/s0) - 2e-5

print("VERIFY_OK")
