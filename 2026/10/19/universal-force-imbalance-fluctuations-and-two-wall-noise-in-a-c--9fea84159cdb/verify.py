#!/usr/bin/env python3
"""Independent finite-volume generator approximations for confined telegraph-wall noise."""
import numpy as np
from scipy.sparse import lil_matrix,csr_matrix,eye
from scipy.sparse.linalg import spsolve,eigs


def gen(n, length, speed, flip):
    h=length/n; sz=2*(n+1); Q=lil_matrix((sz,sz),dtype=float)
    def index(i,s): return 2*i+s # 0=left velocity minus, 1=right plus
    for i in range(n+1):
        for s in [0,1]:
            a=index(i,s)
            b=index(i,1-s)
            Q[a,b]+=flip
            if (s==0 and i>0) or (s==1 and i<n):
                Q[a,index(i+(-1 if s==0 else 1),s)]+=speed/h
    for i in range(sz): Q[i,i]=-float(Q[i,:].sum())
    return Q.tocsr()


def stationary(Q):
    a=Q.T.tolil(); b=np.zeros(Q.shape[0]);a[0,:]=1;b[0]=1
    return spsolve(a.tocsr(),b)


def green(Q,pi,f):
    rhs=-(f-pi@f);a=Q.tolil();a[0,:]=0;a[0,0]=1;rhs[0]=0
    u=spsolve(a.tocsr(),rhs)
    return float((pi*f)@(u-pi@u))


def theoretical(z,flip):
    rr=(4*z**3+12*z*z+9*z+3)/(24*flip*(1+z)**3)
    lr=-(2*z**3+6*z*z+9*z+3)/(24*flip*(1+z)**3)
    return rr,lr

for speed,flip,length in [(1.0,1.0,0.5),(2.0,1.5,1.7),(1.5,0.3,5.0)]:
    z=flip*length/speed; rr,lr=theoretical(z,flip)
    print('PARAMETERS',speed,flip,length,'z',z,'THEORY_G_RR',rr,'THEORY_G_LR',lr)
    for n in (24,48,96,192):
        Q=gen(n,length,speed,flip)
        pi=stationary(Q)
        R=np.zeros(Q.shape[0]);Lw=R.copy();R[-1]=1;Lw[0]=1
        grr=green(Q,pi,R)
        # cross: integral stationary R(0),L(t): q_R*(u_L(right)- mean)
        rhs=-(Lw-pi@Lw); a=Q.tolil();a[0,:]=0;a[0,0]=1;rhs[0]=0
        u=spsolve(a.tocsr(),rhs)
        glr=(pi*R)@(u-pi@u)
        pth=1/(2*(1+z))
        print('  n',n,'pi_wall',pi[-1],'vs',pth,'G_RR',grr,'G_RL',glr,'err',abs(grr-rr)+abs(glr-lr))
        assert abs(pi[-1]-pth)<0.3/n+0.02
    assert abs(grr-rr)<0.009 and abs(glr-lr)<0.009
    # analytic consequence verified algebraically using exact rational arithmetic separately.
print('FINITE_VOLUME_CHECKS_PASSED')

# Independently inspect the additive-functional tilted generator.  The lattice
# approximation carries extra hopping shot noise which vanishes as mesh -> 0.
for length,speed,flip,theta in [(1.,1.,0.7,0.6),(2.,1.5,1.1,1.0)]:
    exact=(flip*flip+theta*theta)**0.5-flip
    errs=[]
    for n in (50,100,200):
        Q=gen(n,length,speed,flip)
        S=np.zeros(Q.shape[0]); S[-1]=1.; S[0]=-1.
        tilted=Q+csr_matrix((theta*S,(np.arange(len(S)),np.arange(len(S)))),shape=Q.shape)
        ev=eigs(tilted,k=1,which='LR',return_eigenvectors=False,tol=1.e-9,maxiter=10000)[0].real
        errs.append(abs(ev-exact))
        print('LDP_EIGEN',length,speed,flip,theta,n,'num',ev,'target',exact,'err',errs[-1])
    assert errs[-1]<errs[0]*.45

import sympy as sp
z,k=sp.symbols('z k',positive=True)
grr=(4*z**3+12*z*z+9*z+3)/(24*k*(1+z)**3)
glr=-(2*z**3+6*z*z+9*z+3)/(24*k*(1+z)**3)
assert sp.simplify(4*(grr-glr)-1/k)==0
assert sp.simplify(4*(grr+glr)-z*z*(z+3)/(3*k*(1+z)**3))==0
assert sp.simplify(sp.diff(z*z*(z+3)/(3*(1+z)**3),z)-2*z/(1+z)**4)==0
print('SYMBOLIC_IDENTITIES_AND_TILTED_CHECKS_PASSED')
