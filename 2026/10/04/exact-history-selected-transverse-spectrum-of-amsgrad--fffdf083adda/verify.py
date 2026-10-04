import math

def roots(beta1,c):
    T=1.0+beta1-c
    disc=T*T-4.0*beta1
    if disc>=0.0:
        s=math.sqrt(disc)
        return ((T+s)/2.0,(T-s)/2.0)
    s=math.sqrt(-disc)
    return (complex(T/2.0,s/2.0),complex(T/2.0,-s/2.0))

def amap(state,lam,alpha,beta1,beta2):
    x,mprev,vprev,Vprev=state
    g=lam*x
    m=beta1*mprev+(1.0-beta1)*g
    v=beta2*vprev+(1.0-beta2)*g*g
    V=max(Vprev,v)
    xn=x-alpha*m/math.sqrt(V)
    return (xn,m,v,V)

def jacobian_fd(V,lam,alpha,beta1,beta2,h=1e-7):
    base=(0.0,0.0,0.0,V)
    f0=amap(base,lam,alpha,beta1,beta2)
    J=[]
    for j in range(4):
        p=list(base); p[j]+=h
        fp=amap(tuple(p),lam,alpha,beta1,beta2)
        J.append([(fp[i]-f0[i])/h for i in range(4)])
    return [[J[j][i] for j in range(4)] for i in range(4)]

def analytic(V,lam,alpha,beta1,beta2):
    c=alpha*(1.0-beta1)*lam/math.sqrt(V)
    return [
        [1.0-c,-alpha*beta1/math.sqrt(V),0.0,0.0],
        [(1.0-beta1)*lam,beta1,0.0,0.0],
        [0.0,0.0,beta2,0.0],
        [0.0,0.0,0.0,1.0],
    ]

# Full Jacobian check.
for V,lam,alpha,b1,b2 in [
    (0.5,2.0,0.3,0.9,0.999),
    (4.0,1.5,0.7,0.4,0.8),
    (10.0,3.0,0.2,0.0,0.5),
]:
    J=jacobian_fd(V,lam,alpha,b1,b2)
    A=analytic(V,lam,alpha,b1,b2)
    for i in range(4):
        for j in range(4):
            assert abs(J[i][j]-A[i][j])<2e-6

# Sharp stability threshold and boundary factorization.
for b1 in (0.0,0.2,0.7,0.9,0.99):
    for c in (0.01,0.25,1.0,0.999*2.0*(1.0+b1)):
        if c>=2.0*(1.0+b1):
            continue
        rr=roots(b1,c)
        assert max(abs(z) for z in rr)<1.0
    cb=2.0*(1.0+b1)
    rr=roots(b1,cb)
    assert min(abs(z+1.0) for z in rr)<1e-12
    assert min(abs(z+b1) for z in rr)<1e-12
    for c in (1.001*cb,1.2*cb,2.0*cb):
        rr=roots(b1,c)
        assert max(abs(z) for z in rr)>1.0

# Complex-root rate plateau.
for b1 in (0.05,0.2,0.5,0.9):
    lo=(1.0-math.sqrt(b1))**2
    hi=(1.0+math.sqrt(b1))**2
    for c in (lo+0.1*(hi-lo),0.5*(lo+hi),hi-0.1*(hi-lo)):
        rr=roots(b1,c)
        assert isinstance(rr[0],complex)
        assert abs(abs(rr[0])-math.sqrt(b1))<1e-12
        assert abs(abs(rr[1])-math.sqrt(b1))<1e-12

# Large memory sends one position-momentum root to one.
b1=0.9
for c in (1e-3,1e-5,1e-7):
    rr=roots(b1,c)
    assert min(abs(z-1.0) for z in rr) < 20.0*c/(1.0-b1)

# The other transverse optimizer-state eigenvalue is beta2; memory tangent is exactly one.
for b2 in (0.0,0.5,0.999):
    A=analytic(2.0,1.0,0.2,0.9,b2)
    assert A[2][2]==b2
    assert A[3][3]==1.0

print('verification passed')
