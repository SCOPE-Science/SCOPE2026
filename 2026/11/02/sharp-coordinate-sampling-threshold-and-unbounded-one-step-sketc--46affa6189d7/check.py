#!/usr/bin/env python3
"""Reproduce matrix, sketch, exact one-step residual and threshold identities."""
import math
import numpy as np

assertions = 0

def check(cond, msg):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)

def close(x,y,tol=1e-9):
    return np.allclose(x,y,rtol=tol,atol=tol)

for n in range(2,27):
    for s in range(1,n):
        for q in (1.0,1.02,1.6,2.4):
            w = np.r_[np.full(s,q),np.ones(n-s)]
            b = w / np.linalg.norm(w)
            P = np.arange(s)
            mass = np.linalg.norm(b[P]); u = np.zeros(n); u[P]=b[P]/mass
            up = (b+u)/math.sqrt(2*(1+mass))
            un = (b-u)/math.sqrt(2*(1-mass))
            H = np.outer(up,up)-np.outer(un,un)
            check(close(H@b,u), ('reflection',n,s,q))
            check(close(H@u,b),('swap',n,s,q))
            check(close(H@H@b,b),('involution',n,s,q))
            check(close(np.linalg.norm(b[P]),mass),('mass',n,s,q))
            check(mass>=math.sqrt(s/n)-1e-12,('universal mass lower',n,s,q))
            A0=np.eye(n)-mass*H
            check(close(A0@b,b-mass*u),('action',n,s,q))
            check(close((A0@b)[P],np.zeros(s)),('zero sketch',n,s,q))
            lam=np.linalg.eigvalsh(A0)
            check(close(lam[0],1-mass),('lamlo',n,s,q))
            check(close(lam[-1],1+mass),('lamhi',n,s,q))
            check(close(lam[-1]/lam[0],(1+mass)/(1-mass)),('kappa',n,s,q))
            for eta in (0.0004,0.015,0.4):
                A=A0+eta*np.eye(n)
                Ab=A@b
                Sab=Ab[P]
                check(close(Sab,eta*b[P]),('sampled image',n,s,q,eta))
                t=np.dot(b[P],Sab)/np.dot(Sab,Sab)
                check(close(t,1/eta),('sketched coefficient',n,s,q,eta))
                res=np.linalg.norm(b-t*Ab)
                check(close(res,math.sqrt(1-mass**2)/eta,1e-7),('blown residual',n,s,q,eta))
                tstar=np.dot(Ab,b)/np.dot(Ab,Ab)
                opt=np.linalg.norm(b-tstar*Ab)
                check(close(opt,mass*math.sqrt(1-mass**2)/np.linalg.norm(Ab)),('gmres residual',n,s,q,eta))
                check(close(res/opt,np.linalg.norm(Ab)/(mass*eta),1e-7),('gap ratio',n,s,q,eta))
                check(close(np.linalg.cond(A),(1+eta+mass)/(1+eta-mass)),('perturbed kappa',n,s,q,eta))
                if n>=2*s:
                    J=np.arange(s,2*s)
                    tt=np.dot(b[J],Ab[J])/np.dot(Ab[J],Ab[J])
                    check(close(tt,1/(1+eta)),('alternate coefficient',n,s,q,eta))
                    check(close(np.linalg.norm(b-tt*Ab),mass/(1+eta)),('alternate residual',n,s,q,eta))

# Safety bound for arbitrary SPD matrices, including noncommuting orientations.
rng=np.random.default_rng(1729)
for n in range(2,31):
    for s in range(1,n):
        frontier=(math.sqrt(n)+math.sqrt(s))/(math.sqrt(n)-math.sqrt(s))
        for j in range(25):
            x=rng.normal(size=n);x/=np.linalg.norm(x)
            ind=np.argsort(-np.abs(x))[:s]
            Q,_=np.linalg.qr(rng.normal(size=(n,n)))
            eig=1 + (frontier-1)*0.85*rng.random(n)
            A=(Q*eig)@Q.T
            lo,hi=np.linalg.eigvalsh(A)[[0,-1]]
            alpha=(hi+lo)/2
            rho=(hi-lo)/2
            val=np.linalg.norm((A@x)[ind])
            check(val>=alpha*np.linalg.norm(x[ind])-rho-1e-9,('bound',n,s,j))
            check(val>1e-10,('nonzero under below-frontier',n,s,j))

print('PASS:',assertions,'assertions. Analytic universal and critical-limit proofs are given separately.')
