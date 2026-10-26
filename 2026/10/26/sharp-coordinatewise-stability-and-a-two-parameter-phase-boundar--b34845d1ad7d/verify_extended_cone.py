"""Numerical reproducibility checks for a sharp extended-Lorentz-cone projection bound.

Python 3 standard library only. Finite tests are sanity checks, not a universal proof.
"""
from math import sqrt, isclose
from random import Random

TOL = 1e-7
checks = 0


def verify(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)


def h_value(q, a):
    return a - a*a + sqrt(q-1) * a * sqrt(max(0., 1-a*a))


def h_derivative(q, a):
    return 1-2*a + sqrt(q-1) * (1-2*a*a) / sqrt(1-a*a)


def h_optimum(q):
    if q == 1:
        return 0., 1.
    lo, hi = 0., 1.-1.e-13
    for _ in range(95):
        mid = (lo+hi)/2
        if h_derivative(q, mid) > 0:
            lo = mid
        else:
            hi = mid
    a = (lo+hi)/2
    return h_value(q,a),a


def lip(p,q):
    if q == 1:
        return 1.
    H,_ = h_optimum(q)
    return 1.+max((sqrt(q)-1)/2, p/(p+1)*H)


def project(x,u):
    """Projection via the scalar monotone root (derived from convex KKT)."""
    t=sqrt(sum(z*z for z in u))
    if t == 0:
        return [max(z,0.) for z in x]+[0. for _ in u]
    lo,hi=0.,t
    for _ in range(95):
        r=(lo+hi)/2
        g=sum(max(r-z,0.) for z in x) + r-t
        if g>0:hi=r
        else:lo=r
    r=(lo+hi)/2
    return [max(z,r) for z in x]+[r*z/t for z in u]


def analytic_jacobian(x,u):
    p,q=len(x),len(u)
    t=sqrt(sum(z*z for z in u))
    y=project(x,u)
    r=sqrt(sum(z*z for z in y[p:]))
    assert t>0 and 0<r<t
    v=[z/t for z in u]
    active=[i for i in range(p) if x[i]<r-1e-10]
    k=len(active)
    assert k>0 and all(abs(x[i]-r)>1e-9 for i in range(p))
    alpha=r/t
    J=[[0. for _ in range(p+q)] for _ in range(p+q)]
    for i in range(p):
        if i not in active:J[i][i]=1.
        else:
            for j in active:J[i][j]=1/(k+1)
            for j in range(q):J[i][p+j]=v[j]/(k+1)
    for j in range(q):
        for i in active:J[p+j][i]=v[j]/(k+1)
        for ell in range(q):
            J[p+j][p+ell]=alpha*(j==ell)+(1/(k+1)-alpha)*v[j]*v[ell]
    return J


rng=Random(20261019)
for q in range(1,31):
    H,a=h_optimum(q)
    verify(H>=0, 'nonnegative H')
    if q>1:
        verify(0<a<1 and abs(h_derivative(q,a))<2e-10,'stationarity')
        for j in range(1001):
            aa=j/1000
            verify(h_value(q,aa)<=H+1e-11,'scalar global optimum grid')

for p in range(1,9):
 for q in range(1,10):
    L=lip(p,q)
    for attempt in range(18):
        u=[rng.uniform(-1.,1.) for _ in range(q)]
        t=sqrt(sum(z*z for z in u))
        r_fraction=rng.uniform(.2,.8)
        r=r_fraction*t
        k=rng.randrange(1,p+1)
        x=[r-(t-r)/k for _ in range(k)] + [r+1. for _ in range(p-k)]
        J=analytic_jacobian(x,u)
        measured=max(sum(abs(a) for a in row) for row in J)
        verify(measured<=L+2e-10,'Jacobian norm globally bounded')
        z=x+u
        for col in range(p+q):
            h=2e-6
            zp=z.copy(); zm=z.copy();zp[col]+=h;zm[col]-=h
            yp=project(zp[:p],zp[p:]); ym=project(zm[:p],zm[p:])
            for row in range(p+q):
                finite=(yp[row]-ym[row])/(2*h)
                verify(abs(finite-J[row][col])<1e-6,'finite difference Jacobian')
    for attempt in range(14):
        z=[rng.uniform(-2,2) for _ in range(p+q)]
        w=[rng.uniform(-2,2) for _ in range(p+q)]
        dz=max(abs(a-b) for a,b in zip(z,w))
        pz=project(z[:p],z[p:]);pw=project(w[:p],w[p:])
        dy=max(abs(a-b) for a,b in zip(pz,pw))
        verify(dy<=L*dz+2e-10,'global pairs bound')

for p in range(1,11):
 for q in range(2,25):
    H,a=h_optimum(q)
    L=lip(p,q)
    v=[1/sqrt(q)]*q
    x=[0.]+[2.]*(p-1)
    J=analytic_jacobian(x,v)
    x_row=sum(abs(w) for w in J[0])
    verify(abs(x_row-(1+(sqrt(q)-1)/2))<1e-11,'scalar row sharp')
    v=[a]+[sqrt(1-a*a)/sqrt(q-1)]*(q-1)
    r=1-1e-7
    x=[r-(1-r)/p]*p
    J=analytic_jacobian(x,v)
    u_row=sum(abs(w) for w in J[p])
    limit=1+p/(p+1)*H
    verify(u_row<=limit+1e-11 and u_row>limit-1.2e-6,'vector row sharp limit')
    verify(abs(L-max(x_row,limit))<1e-11,'both sharp branches')

print('PASS: %d reproducibility assertions (not a proof for every dimension pair).' % checks)
print('Selected constants:')
for p,q in [(1,2),(1,3),(1,4),(1,5),(2,5),(2,13),(3,13),(5,30)]:
 print('p=%d q=%d L=%.12f' %(p,q,lip(p,q)))
