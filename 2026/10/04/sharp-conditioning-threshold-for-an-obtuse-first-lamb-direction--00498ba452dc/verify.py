import math, random
import numpy as np

KSTAR = 3.0 + 2.0*math.sqrt(2.0)

def lamb_first_direction(H, x, eps, beta1=0.9, beta2=0.999):
    g = H @ x
    m = (1.0-beta1)*g
    v = (1.0-beta2)*(g*g)
    mhat = m/(1.0-beta1)
    vhat = v/(1.0-beta2)
    r = mhat/(np.sqrt(vhat)+eps)
    return g, r

# Exact simple counterexample.
H = np.array([[2.0,-5.0],[-5.0,13.0]])
x = np.array([2.0,1.0])
g = H @ x
assert np.allclose(g,[-1.0,3.0])
for eps in (1e-6,0.01,0.1,1.0,2.9):
    _,r = lamb_first_direction(H,x,eps,0.3,0.7)
    expected = (eps-3.0)/((1.0+eps)*(3.0+eps))
    assert abs(float(x@r)-expected) < 2e-14
    assert float(x@r) < 0.0
    for a in (1e-9,1e-4,0.01,0.5,2.0):
        xp = x-a*r
        assert float(xp@xp) > float(x@x)

# Sharp SPD turning-angle lower cosine bound.
random.seed(1)
np.random.seed(1)
for kappa in (1.0,2.0,5.0,KSTAR,10.0,100.0):
    lower = 2.0*math.sqrt(kappa)/(kappa+1.0)
    for _ in range(2000):
        th = random.uniform(0.0,2.0*math.pi)
        Q = np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
        H = Q @ np.diag([1.0,kappa]) @ Q.T
        x = np.random.randn(2)
        g = H@x
        c = float(x@g)/(np.linalg.norm(x)*np.linalg.norm(g))
        assert c >= lower-2e-12

# Below threshold, random searches never produce a nonacute saturated direction.
for kappa in (1.2,2.0,4.0,5.5,KSTAR):
    for eps in (1e-6,0.01,1.0,100.0):
        for _ in range(3000):
            th = random.uniform(0.0,2.0*math.pi)
            Q = np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
            scale = 10.0**random.uniform(-4,4)
            H = scale*(Q @ np.diag([1.0,kappa]) @ Q.T)
            x = np.random.randn(2)
            _,r = lamb_first_direction(H,x,eps)
            assert float(x@r) > -2e-10

# Reconstruct the sharpness family for every tested kappa above threshold.
def sharp_family(kappa, eps):
    y = np.array([1.0,1.0/math.sqrt(kappa)])
    D = np.diag([1.0,kappa])
    gy = D@y
    ax = math.atan2(y[1],y[0])
    ag = math.atan2(gy[1],gy[0])
    delta = ag-ax
    assert delta > math.pi/4
    target_mid = 3.0*math.pi/8.0
    rot = target_mid-(ax+ag)/2.0
    Q = np.array([[math.cos(rot),-math.sin(rot)],[math.sin(rot),math.cos(rot)]])
    x = Q@y
    H0 = Q@D@Q.T
    g0 = H0@x
    assert x[0] > x[1] > 0.0
    assert g0[0] < 0.0 < g0[1]
    assert float(x@np.sign(g0)) < 0.0
    scale = 1.0
    for _ in range(80):
        H = scale*H0
        _,r = lamb_first_direction(H,x,eps)
        if float(x@r) < 0.0:
            return H,x,r
        scale *= 10.0
    raise AssertionError("failed to reach sign limit")

for kappa in (5.9,6.0,10.0,100.0):
    for eps in (1e-6,1.0,1e6):
        H,x,r = sharp_family(kappa,eps)
        assert abs(np.linalg.cond(H)-kappa)/kappa < 2e-12
        assert float(x@r) < 0.0
        for eta in (1e-12,1e-6,1e-3,0.1,1.0):
            # identity scaling phi(||x||)=||x|| gives this exact positive multiplier
            a = eta*np.linalg.norm(x)/np.linalg.norm(r)
            xp = x-a*r
            assert float(xp@xp) > float(x@x)

print("verification passed")
