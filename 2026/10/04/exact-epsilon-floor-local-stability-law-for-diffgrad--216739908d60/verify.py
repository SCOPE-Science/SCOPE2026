import cmath
import math

def roots(beta1, q):
    chi = q / 2.0
    T = 1.0 + beta1 - (1.0-beta1)*chi
    disc = cmath.sqrt(T*T - 4.0*beta1)
    return ((T+disc)/2.0, (T-disc)/2.0)

def cap(beta1):
    return 4.0*(1.0+beta1)/(1.0-beta1)

def xi(delta_g):
    return 1.0/(1.0+math.exp(-abs(delta_g)))

for beta1 in (0.0,0.2,0.5,0.9):
    q = cap(beta1)
    rs = roots(beta1,q)
    assert min(abs(r+1.0) for r in rs) < 1e-12
    assert min(abs(r+beta1) for r in rs) < 1e-12
    assert max(abs(r) for r in roots(beta1,0.999*q)) < 1.0
    assert max(abs(r) for r in roots(beta1,1.001*q)) > 1.0

for beta1 in (0.1,0.5,0.9):
    s = math.sqrt(beta1)
    lo = 2.0*(1.0-s)/(1.0+s)
    hi = 2.0*(1.0+s)/(1.0-s)
    for q in (0.25*lo+0.75*hi,0.5*(lo+hi),0.75*lo+0.25*hi):
        r1,r2 = roots(beta1,q)
        assert abs(r1.imag) > 1e-12
        assert abs(abs(r1)-s) < 1e-11
        assert abs(abs(r2)-s) < 1e-11

assert abs(cap(0.9)-76.0) < 1e-12

def step_inf(z, alpha, lam, beta1, beta2, eps):
    x,m_prev,v_prev,x_prev = z
    g = lam*x
    g_prev = lam*x_prev
    m = beta1*m_prev + (1.0-beta1)*g
    v = beta2*v_prev + (1.0-beta2)*g*g
    friction = xi(g_prev-g)
    x_new = x - alpha*friction*m/(math.sqrt(v)+eps)
    return (x_new,m,v,x)

def linear(z, alpha, lam, beta1, beta2, eps):
    x,m_prev,v_prev,x_prev = z
    h = alpha/(2.0*eps)
    m = beta1*m_prev + (1.0-beta1)*lam*x
    x_new = x - h*m
    return (x_new,m,beta2*v_prev,x)

alpha=1e-3
lam=0.003
beta1=0.9
beta2=0.999
eps=1e-7
direction=(0.7,-0.2,0.4,-0.5)
prev=None
for scale in (1e-18,1e-20,1e-22,1e-24):
    z=(scale*direction[0],scale*direction[1],scale*direction[2],scale*direction[3])
    n=max(abs(a) for a in z)
    F=step_inf(z,alpha,lam,beta1,beta2,eps)
    L=linear(z,alpha,lam,beta1,beta2,eps)
    rem=max(abs(a-b) for a,b in zip(F,L))/n
    if prev is not None:
        assert rem < prev
    prev=rem
assert prev < 1e-2

for scale in (1e-2,1e-4,1e-6):
    dg=3.0*scale
    m=5.0*scale
    term=abs((xi(dg)-0.5)*m)
    assert term <= 4.0*scale*scale

print("verification passed")
