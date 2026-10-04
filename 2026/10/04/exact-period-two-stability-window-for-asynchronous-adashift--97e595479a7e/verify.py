import cmath, math

def roots(T,D):
    disc=T*T-4.0*D
    s=cmath.sqrt(disc)
    return ((T+s)/2.0,(T-s)/2.0)

def params(lam,alpha,eps,b):
    r=alpha/2.0-eps/lam
    assert r>0.0
    c=lam*r/(lam*r+eps)
    T=1.0+b*b-4.0*c*(1.0-b)
    d=b+2.0*c*(1.0-b)
    D=d*d
    return r,c,T,D,d

def step(x,v,lam,alpha,eps,b):
    xn=x-alpha*lam*x/(math.sqrt(v)+eps)
    vn=b*v+(1.0-b)*(lam*x)**2
    return xn,vn

def jacobian_norm(s,c,b):
    return ((-1.0,s*c),(2.0*(1.0-b)*s,b))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

# Exact orbit across stable and unstable regimes.
for lam,alpha,eps,b in [(1.0,3.0,1.0,0.9),(2.0,1.75,1.0,0.5),(3.0,2.0,0.2,0.999),(1.0,5.0,1.0,0.9)]:
    r,c,T,D,d=params(lam,alpha,eps,b)
    v=(lam*r)**2
    x=r
    for _ in range(6):
        xn,vn=step(x,v,lam,alpha,eps,b)
        assert abs(xn+x)<2e-12*max(1.0,r)
        assert abs(vn-v)<2e-12*max(1.0,v)
        x=xn; v=vn

# Analytic monodromy polynomial and discriminant.
for b in (0.1,0.5,0.9,0.999):
    for c in (0.05,0.2,0.49,0.5,0.7,1.0):
        Jp=jacobian_norm(1.0,c,b)
        Jm=jacobian_norm(-1.0,c,b)
        M=mm(Jm,Jp)
        tr=M[0][0]+M[1][1]
        det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        T=1.0+b*b-4.0*c*(1.0-b)
        d=b+2.0*c*(1.0-b)
        D=d*d
        assert abs(tr-T)<2e-14
        assert abs(det-D)<2e-14
        disc=T*T-4.0*D
        fac=(b-1.0)*(b+1.0)**2*(b+8.0*c-1.0)
        assert abs(disc-fac)<2e-13

# Sharp stability boundary.
for b in (0.1,0.5,0.9,0.999):
    for q in (2.01,2.5,3.0,3.99): # q = alpha*lambda/epsilon
        c=1.0-2.0/q
        T=1.0+b*b-4.0*c*(1.0-b)
        d=b+2.0*c*(1.0-b)
        rr=roots(T,d*d)
        assert max(abs(z) for z in rr)<1.0
    q=4.0
    c=1.0-2.0/q
    T=1.0+b*b-4.0*c*(1.0-b)
    d=b+2.0*c*(1.0-b)
    rr=roots(T,d*d)
    assert abs(max(abs(z) for z in rr)-1.0)<2e-12
    for q in (4.01,5.0,10.0,100.0):
        c=1.0-2.0/q
        T=1.0+b*b-4.0*c*(1.0-b)
        d=b+2.0*c*(1.0-b)
        rr=roots(T,d*d)
        assert max(abs(z) for z in rr)>1.0

# Zero-epsilon exact complex modulus.
for b in (0.1,0.5,0.9,0.999):
    c=1.0
    T=1.0+b*b-4.0*(1.0-b)
    d=2.0-b
    rr=roots(T,d*d)
    assert abs(rr[0].imag)>1e-8
    assert abs(abs(rr[0])-d)<2e-12
    assert abs(abs(rr[1])-d)<2e-12

# Finite-difference one-step Jacobian in normalized coordinates.
lam=2.3; alpha=1.7; eps=1.0; b=0.7
r,c,T,D,d=params(lam,alpha,eps,b)
v0=(lam*r)**2
h=1e-7
for s in (-1.0,1.0):
    x0=s*r
    base=step(x0,v0,lam,alpha,eps,b)
    def normout(x,v):
        y,w=step(x,v,lam,alpha,eps,b)
        return y/r,w/(lam*lam*r*r)
    b0=normout(x0,v0)
    colu=[(normout(x0+h*r,v0)[i]-b0[i])/h for i in range(2)]
    colw=[(normout(x0,v0+h*lam*lam*r*r)[i]-b0[i])/h for i in range(2)]
    J=jacobian_norm(s,c,b)
    assert abs(colu[0]-J[0][0])<3e-7
    assert abs(colu[1]-J[1][0])<3e-7
    assert abs(colw[0]-J[0][1])<3e-7
    assert abs(colw[1]-J[1][1])<3e-7

print('verification passed')
