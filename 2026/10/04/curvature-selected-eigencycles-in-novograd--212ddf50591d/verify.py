import math

def qroots(trace, det):
    disc = trace*trace - 4.0*det
    if disc >= 0.0:
        s = math.sqrt(disc)
        return ((trace+s)/2.0, (trace-s)/2.0)
    s = math.sqrt(-disc)
    return (complex(trace/2.0,s/2.0), complex(trace/2.0,-s/2.0))

def cycle(beta1,beta2,alpha,lam,eps):
    r2 = alpha*alpha/(4.0*(1.0+beta1)**2) - eps/(lam*lam)
    assert r2 > 0.0
    r = math.sqrt(r2)
    v = lam*lam*r*r
    D = math.sqrt(v+eps)
    assert abs(D-alpha*lam/(2.0*(1.0+beta1))) < 1e-12
    return r,v,D

def state_step(x,mprev,vprev,Hdiag,beta1,beta2,alpha,eps):
    g = [Hdiag[i]*x[i] for i in range(len(x))]
    gn2 = sum(z*z for z in g)
    v = beta2*vprev + (1.0-beta2)*gn2
    D = math.sqrt(v+eps)
    m = [beta1*mprev[i] + g[i]/D for i in range(len(x))]
    xn = [x[i]-alpha*m[i] for i in range(len(x))]
    return xn,m,v

# Exact orbit checks across parameters.
for beta1,beta2,alpha,lam,eps in [
    (0.0,0.2,0.8,3.0,0.01),
    (0.5,0.9,1.0,5.0,0.02),
    (0.95,0.25,0.4,20.0,1e-4),
    (0.9,0.98,0.2,30.0,1e-6),
]:
    r,v,D = cycle(beta1,beta2,alpha,lam,eps)
    for s in (-1.0,1.0):
        x = [s*r]
        mprev = [-s*2.0*r/alpha]
        xn,m,vn = state_step(x,mprev,v,[lam],beta1,beta2,alpha,eps)
        assert abs(xn[0]+s*r) < 2e-12
        assert abs(m[0]-s*2.0*r/alpha) < 2e-12
        assert abs(vn-v) < 2e-12

# Sharp transverse stability boundary.
for beta1 in (0.0,0.2,0.7,0.95):
    for kappa in (0.05,0.25,0.75,0.999):
        trace = (1.0+beta1)*(1.0-2.0*kappa)
        roots = qroots(trace,beta1)
        assert max(abs(z) for z in roots) < 1.0
    trace = -(1.0+beta1)
    roots = qroots(trace,beta1)
    assert min(abs(z+1.0) for z in roots) < 1e-12
    assert min(abs(z+beta1) for z in roots) < 1e-12
    for kappa in (1.001,1.2,2.0):
        trace = (1.0+beta1)*(1.0-2.0*kappa)
        roots = qroots(trace,beta1)
        assert max(abs(z) for z in roots) > 1.0

# Complex-root plateau.
for beta1 in (0.1,0.5,0.9):
    q = math.sqrt(beta1)/(1.0+beta1)
    for kappa in (0.5-0.5*q,0.5,0.5+0.5*q):
        trace = (1.0+beta1)*(1.0-2.0*kappa)
        roots = qroots(trace,beta1)
        assert isinstance(roots[0],complex)
        assert abs(abs(roots[0])-math.sqrt(beta1)) < 1e-12
        assert abs(abs(roots[1])-math.sqrt(beta1)) < 1e-12

# Finite-difference check of the full transverse state map.
beta1 = 0.8
beta2 = 0.37
alpha = 0.7
lam = 5.0
mu = 2.0
eps = 0.01
r,v,D = cycle(beta1,beta2,alpha,lam,eps)
s = 1.0
x0 = [s*r,0.0]
m0 = [-s*2.0*r/alpha,0.0]
Hdiag = [lam,mu]

# Analytic transverse matrix maps (y_t,n_{t-1}) to (y_{t+1},n_t).
a = mu/D
A = [[1.0-alpha*a,-alpha*beta1],[a,beta1]]

h = 1e-7
def transverse_output(y,n):
    x = [x0[0],y]
    mp = [m0[0],n]
    xn,m,vn = state_step(x,mp,v,Hdiag,beta1,beta2,alpha,eps)
    return xn[1],m[1]

base = transverse_output(0.0,0.0)
col_y = tuple((transverse_output(h,0.0)[i]-base[i])/h for i in range(2))
col_n = tuple((transverse_output(0.0,h)[i]-base[i])/h for i in range(2))
assert abs(col_y[0]-A[0][0]) < 2e-7
assert abs(col_y[1]-A[1][0]) < 2e-7
assert abs(col_n[0]-A[0][1]) < 2e-7
assert abs(col_n[1]-A[1][1]) < 2e-7

print("verification passed")
