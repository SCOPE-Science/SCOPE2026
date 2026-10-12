import math

def simulate(alpha,gamma,gamma0,tau,eps,lam,x0,steps):
    h=1.0+1.0/tau
    x=x0
    L=0.5*lam*x*x
    stored=gamma0*L
    rows=[]
    for t in range(steps):
        L=0.5*lam*x*x
        M=min(stored,L)
        q=M/L
        c=1.0-0.5*alpha*(1.0-gamma*q)*(lam*lam*x*x)/(lam*lam*x*x+eps)
        assert 0.0<c<1.0
        xn=c*x
        stored=h*M
        rows.append((t,x,L,q,c,xn))
        x=xn
    return rows

# Finite-lock bound and post-lock recurrence.
for params in [
    (0.15,0.9,0.75,1000.0,1e-4,1.0,3.0),
    (0.7,0.4,0.3,17.0,0.2,2.0,-1.7),
    (2.0,0.2,0.9,3.0,0.7,0.4,5.0),
]:
    alpha,gamma,gamma0,tau,eps,lam,x0=params
    N=math.ceil(math.log(1.0/gamma0)/math.log(1.0+1.0/tau)) if gamma0<1 else 0
    rows=simulate(*params,steps=N+50)
    lock=[t for t,_,_,q,_,_ in rows if abs(q-1.0)<1e-14]
    assert lock and lock[0] <= N
    first=lock[0]
    A=alpha*(1-gamma)/2
    for t,x,L,q,c,xn in rows[first:first+25]:
        assert abs(q-1.0)<1e-14
        z=lam*lam*x*x/eps
        zn=lam*lam*xn*xn/eps
        closed=z*(1-A*z/(1+z))**2
        assert abs(zn-closed)<2e-12*max(1.0,abs(closed))

# Source defaults: universal lock bound.
Ndefault=math.ceil(math.log(1/0.75)/math.log(1.001))
assert Ndefault==288

# Asymptotic constant checked directly on the post-lock dimensionless recurrence.
for A in (0.0075,0.05,0.3,0.9):
    z=2.7
    for t in range(1,2000001):
        z=z*(1-A*z/(1+z))**2
    assert abs(t*z-1/(2*A)) < 4e-4*(1/(2*A))

# Translate dimensionless asymptotic to loss.
alpha=0.15; gamma=0.9; eps=1e-12; lam=1.7
A=alpha*(1-gamma)/2
expected=eps/(2*alpha*(1-gamma)*lam)
z=1.0
for t in range(1,1500001):
    z=z*(1-A*z/(1+z))**2
L=eps*z/(2*lam)
assert abs(t*L-expected) < 6e-4*expected
assert abs(eps/(2*0.15*0.1)-3.3333333333333335e-11) < 1e-25

# Formal epsilon=0 post-lock law.
for alpha,gamma in ((0.15,0.9),(0.8,0.3),(2.0,0.4)):
    A=alpha*(1-gamma)/2
    c=1-A
    assert 0<=c<1
    L=3.0
    for _ in range(30):
        Ln=c*c*L
        assert abs(Ln/L-c*c)<2e-15 if L!=0 else True
        L=Ln

print("verification passed")
