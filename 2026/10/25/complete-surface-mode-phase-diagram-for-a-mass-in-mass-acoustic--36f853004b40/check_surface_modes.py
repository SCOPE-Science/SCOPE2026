"""Finite-chain and scalar secular checks for surface modes of a mass-in-mass chain."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import eigh


def edges(M,m,k,K):
    w0=k/m
    A=M*w0+k+4*K
    discr=A*A-16*K*M*w0
    ta=(A-math.sqrt(discr))/(2*M)
    to=(A+math.sqrt(discr))/(2*M)
    t0=w0+k/M
    assert 0<ta<w0<t0<to, (ta,w0,t0,to)
    return ta,w0,t0,to


def f(t,M,m,k,K,delta):
    w0=k/m
    return M+k/(w0-t)+delta*delta*t/(K+delta*t)


def eigenmodes(M,m,k,K,delta):
    ta,w0,t0,to=edges(M,m,k,K)
    found=[]
    if delta>0:
        t=brentq(lambda t:f(t,M,m,k,K,delta), w0+1.e-10*(t0-w0),t0,xtol=1e-13)
        lam=K/(K+delta*t)
        assert w0<t<t0 and 0<lam<1
        found.append((t,lam,'gap+'))
    elif delta<0:
        a=-delta
        for edge,upper,label in [(ta,w0,'gap-'),(to,None,'above')]:
            if a > 2*K/edge:
                if upper:
                    left=edge
                    right=upper-1e-10*(upper-edge)
                else:
                    left=edge
                    right=max(to*2,100)
                    while f(right,M,m,k,K,delta)<0: right*=2
                t=brentq(lambda t:f(t,M,m,k,K,delta),left,right,xtol=1e-12)
                lam=K/(K+delta*t)
                assert (edge<t<upper if upper else t>edge) and -1<lam<0, (t,lam)
                found.append((t,lam,label))
    return found


def finite_matrix(M,m,k,K,delta,N=130):
    H=np.zeros((2*N,2*N))
    masses=np.array([M+delta]+[M]*(N-1)+[m]*N,float)
    assert np.min(masses)>0
    for j in range(N):
        a,b=j,N+j
        H[a,a]+=k;H[b,b]+=k;H[a,b]-=k;H[b,a]-=k
    for j in range(N-1):
        H[j,j]+=K;H[j+1,j+1]+=K;H[j,j+1]-=K;H[j+1,j]-=K
    normal=H/np.sqrt(masses[:,None]*masses[None,:])
    return normal,masses


def test_case(M,m,k,K,delta,N=130):
    ta,w0,t0,to=edges(M,m,k,K)
    solutions=eigenmodes(M,m,k,K,delta)
    mat,masses=finite_matrix(M,m,k,K,delta,N)
    ev,vec=eigh(mat,check_finite=False)
    found_finite=[]
    for t,lam,typ in solutions:
        index=np.argmin(abs(ev-t));err=abs(ev[index]-t)
        assert err<1e-8, (M,m,k,K,delta,typ,t,ev[index],err)
        mode=vec[:,index]/np.sqrt(masses)
        assert abs(abs(mode[1]/mode[0])-abs(lam)) < 1e-7,(mode[1]/mode[0],lam)
        found_finite.append((typ,t,lam))
    tol=1e-7
    # Other finite-volume eigenvalues are inside bands, not extra isolated eigenvalues.
    out=[x for x in ev if x >tol and (ta+tol<x<t0-tol or x>to+tol)]
    assert len(out)==len(solutions),(M,m,k,K,delta,out,solutions)
    return found_finite

if __name__=='__main__':
    import sympy as sp
    M,m,k,K,d,t=sp.symbols('M m k K d t',positive=True)
    w0=k/m
    dyn=M+k/(w0-t)
    assert sp.simplify(sp.diff(t*dyn,t) - (M+k*w0/(w0-t)**2))==0
    assert sp.simplify(K*(2-K/(K+d*t)-(K+d*t)/K) +d*d*t*t/(K+d*t))==0
    assert sp.simplify((M+m)*w0/M-(w0+k/M))==0
    tests=[(1,1,1,1,.5),(1,1,1,1,-.2),(1,1,1,1,-.7),
           (10,1,3,1,-9),(10,1,3,1,-5),(10,1,3,1,-.05),
           (10,1,3,1,2),(3,4,2,.5,1.2),(3,4,2,.5,-1.5),
           (.6,.1,4,2,-.5),(5,.5,.5,3,-4),(5,.5,.5,3,1)]
    import random
    rng=random.Random(4237)
    for _ in range(28):
        mm=10**rng.uniform(-.7,.9)
        mn=10**rng.uniform(-1,1)
        kk=10**rng.uniform(-1,1)
        ss=10**rng.uniform(-.9,.9)
        frac=rng.choice([-1,1])*rng.uniform(.15,.9)
        dd=mm*frac
        tests.append((mm,mn,kk,ss,dd))
    tot=0; mode_total=0
    for vals in tests:
        sol=test_case(*vals)
        mode_total+=len(sol)
        tot+=1
    print('PASS: symbolic identities +',tot,'finite-chain spectrum comparisons and',mode_total,'localized eigenmode matches')
    # Quadratic threshold laws in three cases.
    for M,m,k,K,direction in [(1,1,1,1,'heavy'),(1,1,1,1,'outer'),(10,1,3,1,'inner')]:
        ta,w0,t0,to=edges(M,m,k,K)
        edge={'heavy':t0,'outer':to,'inner':ta}[direction]
        dc={'heavy':0.,'outer':-2*K/to,'inner':-2*K/ta}[direction]
        Dprime=M+k*w0/(w0-edge)**2
        C=edge**2/(K*Dprime)
        ratios=[]
        for eps in [.015,.007,.003]:
            delta=dc+(eps if direction=='heavy' else -eps)
            if delta<=-M:continue
            sol=eigenmodes(M,m,k,K,delta)
            lab={'heavy':'gap+','outer':'above','inner':'gap-'}[direction]
            t=next(t for t,l,s in sol if s==lab)
            ratios.append(abs(t-edge)/eps**2/C)
        assert ratios and max(abs(v-1) for v in ratios)<.11,(direction,ratios)
        print(direction,'critical',dc,'quadratic coefficient',C,'ratios',ratios)
    print('ALL_CHECKS_PASS')
