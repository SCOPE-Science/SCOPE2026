#!/usr/bin/env python3
"""Matrix-level checks for weakly noncollective XX-battery relaxation."""
import numpy as np
from scipy.linalg import expm

sx = np.array([[0.,1.],[1.,0.]])
sy = np.array([[0.,-1j],[1j,0.]])
sz = np.diag([1.,-1.])
sm = np.array([[0.,0.],[1.,0.]])
I = np.eye(2)

def initial(J,h,beta):
    H=J*(np.kron(sx,sx)+np.kron(sy,sy))+h*(np.kron(sz,I)+np.kron(I,sz))
    return H, expm(-beta*H)/np.trace(expm(-beta*H))

def lindblad(H,alpha,gamma):
    a=np.kron(sm,I); b=np.kron(I,sm)
    ls=np.sqrt(gamma*(1+alpha)/2)*(a+b)
    la=np.sqrt(gamma*(1-alpha)/2)*(a-b)
    def L(rho):
        out=-1j*(H@rho-rho@H)
        for l in (ls,la):
            m=l.conj().T@l
            out+=l@rho@l.conj().T-.5*(m@rho+rho@m)
        return out
    # Column-major vectorized superoperator, built from its action on basis matrices.
    m=np.zeros((16,16),complex)
    for k in range(16):
        e=np.zeros((4,4),complex);e[k%4,k//4]=1
        m[:,k]=L(e).ravel(order='F')
    return m

def analytical(J,h,beta,gamma,alpha,t):
    en=np.array([-2*J,-2*h,2*h,2*J])
    z=np.exp(-beta*en); z/=sum(z)
    a0,g0,e0,s0=z
    qa=gamma*(1-alpha);qs=gamma*(1+alpha)
    e=e0*np.exp(-2*gamma*t)
    a=a0*np.exp(-qa*t)+qa/qs*e0*(np.exp(-qa*t)-np.exp(-2*gamma*t))
    if qa>0:
        s=s0*np.exp(-qs*t)+qs/qa*e0*(np.exp(-qs*t)-np.exp(-2*gamma*t))
    else:
        s=np.exp(-qs*t)*(s0+qs*e0*t)
    g=1-a-e-s
    return np.array([a,g,e,s]),en

def work_from_population(p,en):
    return float(np.dot(p,en)-np.dot(np.sort(p)[::-1],en))

def exact_reduced_from_full(J,h,beta,gamma,alpha,t):
    H,rho=initial(J,h,beta)
    mat=lindblad(H,alpha,gamma)
    rt=(expm(t*mat)@rho.ravel(order='F')).reshape((4,4),order='F')
    eg=np.array([1.,0.,0.,0.]);ge=np.array([0.,0.,1.,0.]) # wrong? basis |ee>,|eg>,|ge>,|gg> indices 0,1,2,3
    e0=np.eye(4)[0];g0=np.eye(4)[3]
    a=(np.eye(4)[1]-np.eye(4)[2])/np.sqrt(2)
    s=(np.eye(4)[1]+np.eye(4)[2])/np.sqrt(2)
    basis=(a,g0,e0,s)
    return np.array([np.real(np.vdot(v,rt@v)) for v in basis]),rt,H

def run():
    n=0
    for J,h,beta,gamma in [(1.,.1,.2,.05),(1.,.1,2.,.05),(1.6,.3,1.,.3),(.7,.4,0.,.12)]:
        for alpha in [0.,.2,.8,.95,.995,1.]:
            for t in [0.,.3,3.,15.,100.]:
                pop,en=analytical(J,h,beta,gamma,alpha,t)
                pmat,rt,H=exact_reduced_from_full(J,h,beta,gamma,alpha,t)
                assert np.max(np.abs(pop-pmat))<2e-10, (J,h,beta,gamma,alpha,t,pop,pmat)
                assert abs(np.trace(rt)-1)<2e-10
                assert np.linalg.eigvalsh(rt).min()>-2e-10
                assert abs(work_from_population(pop,en)-(np.real(np.trace(rt@H))-np.dot(np.sort(np.linalg.eigvalsh(rt))[::-1],en)))<2e-9
                n+=4
    for J,h,beta in [(1,.1,0.),(1,.1,.5),(1,.1,2.),(1.6,.3,1.),(1,.8,3.)]:
        en=np.array([-2*J,-2*h,2*h,2*J]);z=np.exp(-beta*en);z/=sum(z);a0=z[0]
        for u in [.1,.6,1.,2.,4.]:
            lim=2*(J-h)*max(0.,1.-2*a0*np.exp(-u))
            errs=[]
            for eps in [.05,.025,.0125]:
                t=u/eps
                p,e=analytical(J,h,beta,1.,1.-eps,t)
                work=work_from_population(p,e)
                errs.append(abs(work-lim))
                assert abs(work-lim)<4*eps+1e-7, (J,h,beta,u,eps,work,lim)
                n+=1
            assert errs[-1]<=max(errs[0],1e-9)+1e-8
            n+=1
    print('PASS:',n,'density-matrix and slow-limit checks')

if __name__=='__main__':run()
