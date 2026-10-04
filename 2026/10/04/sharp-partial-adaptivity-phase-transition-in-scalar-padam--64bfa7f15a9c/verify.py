import math

def F(q,p):
    return q/((q-1.0)**(2.0*p))

def radius(alpha, lam, p):
    a = alpha*(lam**(1.0-2.0*p))
    return (a/2.0)**(1.0/(2.0*p))

def reduced(x1, alpha, lam, p, steps):
    a = alpha*(lam**(1.0-2.0*p))
    x = x1
    M = abs(x1)
    out = [(x,M,a/(M**(2.0*p)))]
    for _ in range(steps):
        q = a/(M**(2.0*p))
        x = x*(1.0-q)
        M = max(M,abs(x))
        out.append((x,M,a/(M**(2.0*p))))
    return out

def direct_padam(x1, alpha, lam, p, steps):
    x=x1
    vmax=0.0
    out=[]
    for _ in range(steps+1):
        g=lam*x
        v=g*g
        vmax=max(vmax,v)
        q=alpha*lam/(vmax**p)
        out.append((x, math.sqrt(vmax)/lam, q))
        x=x-alpha*g/(vmax**p)
    return out

# Exact-reduction agreement numerically.
for p in (0.125,0.25,0.3,0.5):
    alpha=0.25
    lam=3.0
    r=radius(alpha,lam,p)
    x1=0.4*r
    A=reduced(x1,alpha,lam,p,40)
    B=direct_padam(x1,alpha,lam,p,40)
    for a,b in zip(A,B):
        assert abs(a[0]-b[0]) < 2e-11
        assert abs(a[1]-b[1]) < 2e-11
        assert abs(a[2]-b[2]) < 2e-11

# For p <= 1/4, F(q)>2 for q>2 and F(q)<q.
for p in (0.05,0.125,0.2,0.25):
    for q in (2.0001,2.01,2.2,3.0,10.0,100.0):
        assert F(q,p) > 2.0
        assert F(q,p) < q

# Persistent small-initialization overshoot approaches the critical radius.
for p in (0.125,0.25):
    alpha=0.2
    lam=2.0
    r=radius(alpha,lam,p)
    traj=reduced(0.1*r,alpha,lam,p,20000)
    x,M,q=traj[-1]
    assert q >= 2.0-2e-12
    assert abs(M-r)/r < 2e-8
    # Late signs alternate and magnitudes are near r.
    vals=[z[0] for z in traj[-10:]]
    for a,b in zip(vals,vals[1:]):
        assert a*b < 0.0

# Above one quarter, overshoot crosses below two in finite time.
for p in (0.26,0.3,0.4,0.5):
    for q0 in (2.001,2.1,3.0,10.0,100.0):
        q=q0
        crossed=False
        for _ in range(10000):
            if q <= 2.0:
                crossed=True
                break
            q=F(q,p)
        assert crossed

# Once q<2, the historical maximum freezes and the recurrence is geometric.
p=0.4
alpha=0.2
lam=2.0
r=radius(alpha,lam,p)
traj=reduced(0.1*r,alpha,lam,p,1000)
cross=None
for j,(_,_,q) in enumerate(traj):
    if q < 2.0:
        cross=j
        break
assert cross is not None
M0=traj[cross][1]
q0=traj[cross][2]
for x,M,q in traj[cross:]:
    assert abs(M-M0) < 1e-10
    assert abs(q-q0) < 1e-10
assert abs(traj[-1][0]) < 1e-12

print("verification passed")
