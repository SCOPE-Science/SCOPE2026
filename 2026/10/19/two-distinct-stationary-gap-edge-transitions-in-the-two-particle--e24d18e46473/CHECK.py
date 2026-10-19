"""Reproducibility checks for the two-particle active-Dyson gap edge law.

Run with: python CHECK.py
Dependencies: Python 3, numpy, scipy. The proof of the exponents is
analytical and is written in RESULT.md; finite-volume checks are corroboration.
"""
from math import sqrt, isclose
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

CHECKS = 0

def check(condition, detail=''):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail or f'check number {CHECKS}')


def parameters(lam,g,v,gamma):
    h=sqrt(v*v+2*lam*g)
    a=(h-v)/lam
    b=(h+v)/lam
    kappa_left=lam+2*g/a**2
    kappa_right=lam+2*g/b**2
    theta_left=2*gamma/kappa_left
    theta_right=2*gamma/kappa_right
    return h,a,b,kappa_left,kappa_right,theta_left,theta_right


def algebra_tests():
    for lam,g,v,gamma in [(1.,1.,1.,1.), (2.,.75,1.2,2.), (.8,1.3,.6,.7), (3.,.01,2.5,.2), (.2,7.,.01,4.)]:
        h,a,b,kl,kr,tl,tr=parameters(lam,g,v,gamma)
        close=lambda x,y: isclose(x,y,rel_tol=1e-10,abs_tol=1e-10)
        check(0<a<b)
        check(close(a*b,2*g/lam))
        check(close(-lam*a+2*g/a-2*v,0.))
        check(close(-lam*b+2*g/b+2*v,0.))
        check(close(kl,2*lam*h/(h-v)))
        check(close(kr,2*lam*h/(h+v)))
        check(kl>kr>0)
        check(close(tl,gamma/lam*(1-v/h)))
        check(close(tr,gamma/lam*(1+v/h)))
        check(close(tl+tr,2*gamma/lam))
        check(close(tl/tr,a/b))
        check(close((kl/2)/(kr/2),b/a))
        check(kr/2<lam<kl/2)
        check((tl-1)<(tr-1))


def finite_volume(lam,g,v,gamma,n):
    """Independent conservative upwind stationary discretization of 3-state PDMP."""
    h,a,b,kl,kr,tl,tr=parameters(lam,g,v,gamma)
    dx=(b-a)/n
    # modes ordered by driving velocities -2v, 0, +2v
    Q=np.array([[-2*gamma,2*gamma,0.],
                [gamma,-2*gamma,gamma],
                [0.,2*gamma,-2*gamma]])
    rr=[]; cc=[]; dd=[]
    def add(i,j,w):
        rr.append(i);cc.append(j);dd.append(w)
    for s,c in enumerate([-2*v,0.,2*v]):
        for j in range(n):
            row=s*n+j
            for sp in range(3):
                if Q[sp,s]!=0.: add(row,sp*n+j,Q[sp,s])
        for j in range(1,n):
            y=a+j*dx
            speed=-lam*y+2*g/y+c
            upstream=s*n+j-1 if speed>=0 else s*n+j
            add(s*n+j-1,upstream,-speed/dx)
            add(s*n+j,upstream,speed/dx)
    mat=coo_matrix((dd,(rr,cc)),shape=(3*n,3*n)).tolil()
    mat[0,:]=dx*np.ones(3*n)
    rhs=np.zeros(3*n);rhs[0]=1.
    p=np.asarray(spsolve(mat.tocsc(),rhs)).reshape(3,n)
    return a,b,dx,p


def cumulative_exponent(masses,dx,lower=30,upper=300):
    z=np.arange(1,len(masses)+1)*dx
    cumulative=np.cumsum(masses)*dx
    select=(np.arange(len(masses))+1>=lower)&(np.arange(len(masses))+1<=upper)
    return float(np.polyfit(np.log(z[select]),np.log(cumulative[select]),1)[0])


def finite_volume_tests():
    expected=parameters(1.,1.,1.,1.)
    a,b,dx,p=finite_volume(1.,1.,1.,1.,20000)
    check(abs(a-expected[1])<1e-12)
    check(abs(b-expected[2])<1e-12)
    check(np.min(p)>-1e-10)
    check(abs(p.sum()*dx-1.)<1e-8)
    for row,target in zip(p,[.25,.5,.25]):
        check(abs(row.sum()*dx-target)<1e-8)
    total=p.sum(axis=0)
    tleft=cumulative_exponent(total,dx)
    tright=cumulative_exponent(total[::-1],dx)
    check(abs(tleft-expected[-2])<.035,f'left theta {tleft}; predicted {expected[-2]}')
    check(abs(tright-expected[-1])<.035,f'right theta {tright}; predicted {expected[-1]}')
    # Opposite endpoint phases at gamma=lambda (the exact central regime).
    check(expected[-2]<1.<expected[-1])
    print('numerical cumulative slopes',tleft,tright)
    for gamma in [.3,3.]:
        h,a,b,kl,kr,tl,tr=parameters(1.,1.,1.,gamma)
        check((tl<1 and tr<1) if gamma<1 else (tl>1 and tr>1))
        aa,bb,dx,p=finite_volume(1.,1.,1.,gamma,4000)
        check(np.min(p)>-1e-9)
        check(abs(p.sum()*dx-1.)<1e-8)
        for row,target in zip(p,[.25,.5,.25]):
            check(abs(row.sum()*dx-target)<1e-7)
        total=p.sum(axis=0)
        low=cumulative_exponent(total,dx)
        high=cumulative_exponent(total[::-1],dx)
        check(abs(low-tl)<.25,(gamma,'low',low,tl))
        check(abs(high-tr)<.25,(gamma,'high',high,tr))
        print('gamma',gamma,'numerical slopes',low,high,'exact',tl,tr)

if __name__=='__main__':
    algebra_tests()
    finite_volume_tests()
    print(f'{CHECKS} checks passed')
