#!/usr/bin/env python3
"""Standalone deterministic checks for a two-mode Bernoulli-erasure moment theorem.
Only Python standard library; checks support but do not replace the infinite-series proof.
"""
from fractions import Fraction as F
from itertools import product
from math import fsum, isclose, sqrt

A = ((2, -1), (1, 0))
N = ((0, 0), (1, 0))
D = ((1, -1), (1, -1))
Q = ((6, -3), (-3, 2))
checks = 0

def ok(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)

def mv(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(2)) for i in range(2))

def mt(M):
    return tuple(zip(*M))

def mm(M, P):
    return tuple(tuple(sum(M[i][k] * P[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def quad(Q0, z):
    t = mv(Q0, z)
    return sum(z[i] * t[i] for i in range(2))

def matadd(M,P, alpha, beta):
    return tuple(tuple(alpha*M[i][j]+beta*P[i][j] for j in range(2)) for i in range(2))

def apower(k):
    return ((1+k, -k), (k, 1-k))

# Critical exact rational Lyapunov identity, rank-one/Jordan algebra.
for M in (A, N, D, Q):
    ok(len(M)==2 and all(len(row)==2 for row in M), 'dimension')
for k in range(25):
    Ak = apower(k)
    c = mm(N, mm(Ak, N))
    for i in range(2):
        for j in range(2):
            ok(c[i][j] == -k*N[i][j], ('N A^k N',k,i,j))
    for z in ((0,1), (1,0), (2,-3)):
        ok(mv(Ak,z) == (z[0]+k*(z[0]-z[1]), z[1]+k*(z[0]-z[1])), 'Jordan power')
critical = matadd(mm(mt(A),mm(Q,A)),mm(mt(N),mm(Q,N)),F(1,3),F(2,3))
for i in range(2):
    for j in range(2):
        ok(critical[i][j]==Q[i][j], ('critical Q',i,j))
ok(Q[0][0]>0 and Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]>0, 'Q definite')

# Exact finite-horizon weighted expectation at critical erasure probability.
for z in ((1,0), (0,1), (3,-2), (-2,5)):
    for n in range(8):
        total = F(0)
        for seq in product((0,1),repeat=n):
            zz=z; weight=F(1)
            for erasure in seq:
                zz=mv(A if erasure else N,zz)
                weight*=F(1,3) if erasure else F(2,3)
            total+=weight*quad(Q,zz)
        ok(total==quad(Q,z), ('critical exact finite horizon',z,n,total))

# Bisection for moment eigen-rate: s*g^p*sum_{k>=1} k^p*q^k / lam^{k+1}=1.
# For p=1 and p=2 use exact series formulas to check root algebra.
def moment_rate(q,p,g=1):
    assert 0<q<1 and p>0 and g>0
    def val(lam):
        t=q/lam
        if p==1:
            return (1-q)*g*q/(lam-q)**2
        if p==2:
            return (1-q)*g*g*q*(lam+q)/(lam-q)**3
        summ=0.; term=t
        for k in range(1,200000):
            nxt=term*k**p
            summ+=nxt
            if k>50 and nxt<1.e-15*max(1.,summ):
                break
            term*=t
        else:
            raise AssertionError('series did not converge')
        return (1-q)*g**p*summ/lam
    lo=q; hi=1.
    while val(hi)>1:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if val(mid)>1:
            lo=mid
        else:
            hi=mid
    return (hi+lo)/2

def v_p(q,p,g,z,lam):
    # N_g is [[0,0],[g,0]]. The controlling row ell is (1,0).
    ratio=q/lam
    total=0.
    term=1./lam
    for k in range(40000):
        piece=term*abs(z[0]+k*(z[0]-z[1]))**p
        total+=piece
        if k>80 and piece<2e-15*max(1e-8,total):
            break
        term*=ratio
    else:
        raise AssertionError('V series did not converge')
    return total

for q in (0.2, 1/3, 0.4, 0.5, 0.7):
    for p in (.5,1.,1.5,2.,3.):
        lam=moment_rate(q,p)
        ok(lam>q and lam>0, 'eigen-rate positive')
        for z in ((1.,0.),(0.,1.),(2.,-1.),(-.5,.75),(2.,2.)):
            v=v_p(q,p,1,z,lam)
            av=v_p(q,p,1,mv(A,z),lam)
            nv=v_p(q,p,1,mv(N,z),lam)
            ok(v>0,'positive V')
            ok(isclose(q*av+(1-q)*nv,lam*v,rel_tol=5e-12,abs_tol=1e-11),('eigenfunction',q,p,z))
            for n in range(5):
                weighted=0.
                for seq in product((0,1),repeat=n):
                    zz=z; probability=1.
                    for erasure in seq:
                        zz=mv(A if erasure else N,zz)
                        probability*=q if erasure else (1-q)
                    weighted+=probability*v_p(q,p,1,zz,lam)
                ok(isclose(weighted,lam**n*v,rel_tol=7e-12,abs_tol=1e-11),('finite horizon',q,p,z,n))
    l1=q+sqrt(q*(1-q))
    ok(isclose(moment_rate(q,1),l1,rel_tol=1e-13),'p1 closed root')
    l2=moment_rate(q,2)
    ok(isclose((l2-q)**3,q*(1-q)*(l2+q),rel_tol=2e-13),'p2 cubic')

ok(isclose(moment_rate(1/3,2),1.,rel_tol=1e-13),'critical second moment')
ok(isclose(moment_rate(.5,1),1.,rel_tol=1e-13),'critical first moment')
ok(moment_rate(.4,1)<1<moment_rate(.4,2),'moment gap')
# Check general gamma using N_g, the p-dependent eigenfunction and root.
for gamma_scale in (0.5,2.0):
    Ng=((0.,0.),(gamma_scale,0.))
    for q in (.3,.55):
        for p in (1.,2.,3.5):
            lam=moment_rate(q,p,gamma_scale)
            for z in ((1.,0.),(0.,1.),(1.5,-2.)):
                v=v_p(q,p,gamma_scale,z,lam)
                av=v_p(q,p,gamma_scale,mv(A,z),lam)
                nv=v_p(q,p,gamma_scale,mv(Ng,z),lam)
                ok(isclose(q*av+(1-q)*nv,lam*v,rel_tol=7e-12,abs_tol=1e-11),'general gamma eigenfunction')

print('VERIFY_OK checks=',checks)
print('q=0.4 first-moment growth:', format(moment_rate(.4,1),'.12f'))
print('q=0.4 second-moment growth:',format(moment_rate(.4,2),'.12f'))
print('q=1/2 second-moment growth:',format(moment_rate(.5,2),'.12f'))
