"""Reproduce finite-network temporal three-body consensus calculations.
Python >=3.9; uses only the standard library.  Each unordered hyperedge
contributes s(|x_j-x_k|)*(x_j+x_k-2*x_i) to vertex i.
"""
from math import exp, cosh, log
from itertools import permutations


def edges(n, kind):
    assert n >= 2
    if kind == 'A':
        ed = [tuple(sorted((i, (i+1)%n, n+i))) for i in range(n)]
    elif kind == 'B':
        ed = [tuple(sorted((i, n+i, n+(i+1)%n))) for i in range(n)]
    else:
        raise ValueError(kind)
    assert len(set(ed)) == n
    return ed


def vertex_field(x, ed, kappa):
    dx = [0.0]*len(x)
    for e in ed:
        for i in e:
            j,k = [v for v in e if v!=i]
            dx[i] += exp(-kappa*abs(x[j]-x[k]))*(x[j]+x[k]-2*x[i])
    return dx


def scalar_field(z, kappa):
    # c=2 for the explicit cyclic construction M=n.
    return -2*z*(1+exp(-kappa*z))


def rk4(x, dt, func):
    k1=func(x)
    k2=func([a+dt*b/2 for a,b in zip(x,k1)])
    k3=func([a+dt*b/2 for a,b in zip(x,k2)])
    k4=func([a+dt*b for a,b in zip(x,k3)])
    return [a+dt*(b1+2*b2+2*b3+b4)/6 for a,b1,b2,b3,b4 in zip(x,k1,k2,k3,k4)]


def evolve(x, ed, kappa, duration, step=0.002):
    nsteps=max(1,int(duration/step+0.999999))
    dt=duration/nsteps
    for _ in range(nsteps):
        x=rk4(x,dt,lambda z:vertex_field(z,ed,kappa))
    return x


def scalar_z(z0,kappa,duration,step=0.0005):
    nsteps=max(1,int(duration/step+0.999999))
    dt=duration/nsteps
    z=[z0]
    for _ in range(nsteps):
        z=rk4(z,dt,lambda v:[scalar_field(v[0],kappa)])
    return z[0]


def L(z,kappa):
    return log(cosh(kappa*z/2))/kappa


def check_case(n,kappa,tau):
    ea,eb=edges(n,'A'),edges(n,'B')
    for i in range(n):
        assert sum(i in e for e in ea)==2
        assert sum(n+i in e for e in ea)==1
        assert sum(i in e for e in eb)==1
        assert sum(n+i in e for e in eb)==2
    x0=[1.0]*n+[0.0]*n
    z1=scalar_z(1.0,kappa,tau)
    z2=scalar_z(1.0,kappa,2*tau)
    delta=L(1.0,kappa)-2*L(z1,kappa)+L(z2,kappa)
    assert 0<delta<0.5
    a=evolve(x0,ea,kappa,tau)
    a=evolve(a,eb,kappa,tau)
    assert max(abs(v-a[0]) for v in a[:n])<1e-10
    assert max(abs(v-a[n]) for v in a[n:])<1e-10
    assert abs((a[0]-a[n])-z2)<8e-10
    assert abs((a[0]+a[n])/2- (0.5+delta))<8e-10
    b=evolve(x0,eb,kappa,tau)
    b=evolve(b,ea,kappa,tau)
    assert abs((b[0]+b[n])/2- (0.5-delta))<8e-10
    assert abs((b[0]-b[n])-z2)<8e-10
    eall=sorted(set(ea+eb))
    afinal=evolve(a,eall,kappa,7.0)
    assert max(afinal)-min(afinal)<1e-8
    assert abs(sum(afinal)/(2*n) -(0.5+delta))<8e-10
    # Interleaving equal exposures never beats front-loaded A.
    mix=evolve(x0,ea,kappa,tau/2)
    mix=evolve(mix,eb,kappa,tau/2)
    mix=evolve(mix,ea,kappa,tau/2)
    mix=evolve(mix,eb,kappa,tau/2)
    mm=(mix[0]+mix[n])/2
    assert 0.5-delta+1e-10<mm<0.5+delta-1e-10
    return delta


def check_small_tau():
    k=2.0
    c=2.0
    z=1.0
    s=exp(-k*z)
    pref=c*c*z*(1+s)*(1-s+k*z*s)/2
    for tau in (0.01,0.005,0.0025):
        z1=scalar_z(z,k,tau,step=0.00002)
        z2=scalar_z(z,k,2*tau,step=0.00002)
        delta=L(z,k)-2*L(z1,k)+L(z2,k)
        assert abs(delta/tau**2-pref)<0.05
    return pref


def main():
    count=0
    for n in (2,3,5):
        for k in (0.4,1.3,3.0,5.0):
            for tau in (0.2,0.6):
                delta=check_case(n,k,tau)
                count+=1
    pref=check_small_tau()
    print('PASS: {} full-vertex A-first/B-first/interleaved comparisons,'.format(count))
    print('     24 consensus checks, 24 class invariance and graph incidence checks,')
    print('     24 post-release consensus checks, 3 small-window scaling checks.')
    print('small-window leading coefficient for k=2,c=2,d0=1: {:.12f}'.format(pref))
    z1=scalar_z(1.0,2.0,0.6); z2=scalar_z(1.0,2.0,1.2)
    gain=L(1.0,2.0)-2*L(z1,2.0)+L(z2,2.0)
    print('example n=3,k=2,tau=.6: d1={:.12f}, d2={:.12f}, gain={:.12f}, consensus={:.12f}'.format(z1,z2,gain,0.5+gain))

if __name__=='__main__':
    main()
