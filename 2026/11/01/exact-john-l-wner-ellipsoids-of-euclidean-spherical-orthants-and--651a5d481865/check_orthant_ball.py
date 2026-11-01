#!/usr/bin/env python3
"""Independent numerical checks for spherical-orthant extremal ellipsoids.

No finite test substitutes for the containment and contact proofs.
"""
import math
import numpy as np
from scipy.optimize import minimize


def params(d):
    root=math.sqrt(d)
    center_j=d/(d+1)
    sj=1/(d+1)**2
    tj=1/(d+1)
    if d<=5:
        lam=.5; s=.25; t=(root+1)/4
        a=(root+1)/(4*d)
        c=(1-1/root)/4
        b=(2-root+1/root)/4
    else:
        lam=(root+1)/(d+1)
        s=d*(root-1)**2/(d+1)**2
        t=d/(d+1)
        a=c=1/(d+1)
        b=0.
    return (center_j,sj,tj),(lam,s,t),(a,b,c)


def Q(d,s,t):
    e=np.ones(d)/math.sqrt(d)
    return t*np.eye(d)+(s-t)*np.outer(e,e)


def run():
    max_j=0.0; max_l=0.0; max_moment=0.0
    rng=np.random.default_rng(111)
    for d in range(3,61):
        (lj,sj,tj),(lam,s,t),(a,b,c)=params(d)
        e=np.ones(d)/math.sqrt(d)
        J=Q(d,sj,tj)
        L=Q(d,s,t)
        center_j=lj*e
        center_l=lam*e
        # Simplex contact decomposition for the inner ellipsoid.
        v=np.column_stack([-np.linalg.solve(np.linalg.cholesky(J),J[:,i])/math.sqrt(J[i,i]) for i in range(d)] + [np.linalg.solve(np.linalg.cholesky(J),e-center_j)])
        # Use Q^{-1/2} in the verification (Cholesky form is equivalent).
        weights=np.full(d+1,d/(d+1))
        max_moment=max(max_moment,float(np.max(np.abs(v@weights))),float(np.max(np.abs((v*weights)@v.T-np.eye(d)))))
        # Outer decomposition: weighted support covariance Q/d.
        pts=np.vstack([np.eye(d),np.zeros((1,d)),e])
        wts=np.array([a]*d+[b,c])
        mean=np.einsum('i,ij->j',wts,pts)
        cov=np.einsum('i,ij,ik->jk',wts,pts-mean,pts-mean)
        max_moment=max(max_moment,float(np.max(np.abs(mean-center_l))),float(np.max(np.abs(d*cov-L))),abs(float(wts.sum()-1)))
        assert np.linalg.eigvalsh(J).min()>0 and np.linalg.eigvalsh(L).min()>0
        assert np.min(wts)>=-1e-14
        assert s<t
        for _ in range(100):
            z=np.abs(rng.normal(size=d))
            z/=np.linalg.norm(z)
            rr=rng.random()
            x=rr*z
            ql=(np.linalg.norm(x-(x@e)*e)**2/t)+((x@e-lam)**2/s)
            max_l=max(max_l,ql-1)
            p=rng.normal(size=d)
            p/=np.linalg.norm(p)
            y=center_j+np.linalg.cholesky(J)@(rng.random()**(1/d)*p)
            max_j=max(max_j, np.linalg.norm(y)**2-1,-y.min())
        if d in (3,4,5,6,7,10,20,60):
            print(f'd={d:2d} J(vol/ball)={math.sqrt(sj)*tj**((d-1)/2):.8g} L(vol/ball)={math.sqrt(s)*t**((d-1)/2):.8g} origin_contact={b>0} normalized_Q0={lam**2/s:.12f}')
    print('maximum positive containment residual (inner,outer):',max_j,max_l)
    print('maximum identity/moment residual:',max_moment)
    assert max_j<1e-12 and max_l<1e-12 and max_moment<1e-11
    # Independent optimal-design calculation in the three natural contact orbits.
    for d in (3,4,5,6,7,10,20):
        (_,_,_),(lam,s,t),(a,b,c)=params(d)
        def neg_logdet(y):
            u,z=y   # u is total mass on the d coordinate vectors, z on the diagonal.
            aw=u/d
            avg=aw+z/math.sqrt(d)
            axial=aw+z-d*avg*avg
            if aw<=0 or axial<=0: return 1e8
            return -((d-1)*math.log(aw)+math.log(axial))
        res=minimize(neg_logdet,[.55,.25],bounds=[(1e-9,1),(0,1)],
                     constraints=[{'type':'ineq','fun':lambda y:1-y[0]-y[1]}],
                     method='SLSQP',options={'ftol':1e-11,'maxiter':500})
        assert res.success, (d,res.message)
        err=max(abs(res.x[0]-d*a),abs(res.x[1]-c))
        print(f'optimized d={d:2d} contact-weight-error={err:.2e} origin_weight={1-res.x.sum():.8g}')
        assert err<3e-5
    print('All numerical verification checks passed.')

if __name__=='__main__': run()
