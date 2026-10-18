"""Numerical and algebraic consistency checks for a simplex-ridge normal law."""
import math
import numpy as np
from fractions import Fraction

rng = np.random.default_rng(981732)
checks = 0
for d in range(2, 7):
    for t in (1.25, 2.0, 3.0):
        V = np.zeros((d + 1, d)); V[1:] = np.eye(d); V[d, 0] += t
        B=np.vstack((V.T,np.ones(d+1)))
        inv=np.linalg.inv(B)
        q=inv[:,:d]; norm=np.linalg.norm(q,axis=1)
        u=-q/norm[:,None]
        # All other facet pairs nonpositive, sole positive (0,d).
        for a in range(d+1):
            for b in range(a+1,d+1):
                prod=float(u[a]@u[b]);
                if (a,b)==(0,d): assert prod>0
                else: assert prod<1e-10, (d,t,a,b,prod)
        g=u[0]@u[d]
        sample=80000
        lam=rng.dirichlet(np.ones(d+1),size=sample)
        Y=lam@V
        s=np.stack([lam[:,0]/norm[0],lam[:,d]/norm[d]],axis=1)
        mu=np.empty_like(s)
        mu[:,0]=(s[:,0]-g*s[:,1])/(1-g*g)
        mu[:,1]=(s[:,1]-g*s[:,0])/(1-g*g)
        Z=Y+mu[:,0,None]*u[0]+mu[:,1,None]*u[d]
        # Face supported when outward cone and other facets remain valid.
        active=(mu.min(axis=1)>=-1e-10)
        bary=np.column_stack((Z,np.ones(sample)))@inv.T
        assert np.all(bary[active][:,[0,d]] < 2e-9)
        assert np.all(bary[active][:,[k for k in range(d+1) if k not in(0,d)]]>0)
        predicted=(d-1)/(t*(d-1+t*(t-1)))
        assert abs(active.mean()-predicted)<0.013, (d,t,active.mean(),predicted)
        checks+=sample
    # Right-angled simplex: every nonempty proper face is active for every interior y.
    V=np.vstack([np.zeros(d),np.eye(d)])
    inv=np.linalg.inv(np.vstack((V.T,np.ones(d+1))))
    q=inv[:,:d];norm=np.linalg.norm(q,axis=1);u=-q/norm[:,None]
    for la in rng.dirichlet(np.ones(d+1),size=20):
        y=la@V
        for mask in range(1,2**(d+1)-1):
            I=np.array([i for i in range(d+1) if (mask>>i)&1])
            mu=np.linalg.solve(u[I]@u[I].T,la[I]/norm[I]); z=y+mu@u[I]
            bary=np.append(z,1)@inv.T
            assert min(mu)>-1e-10 and min(bary[[i for i in range(d+1) if i not in I]])>1e-10
            checks+=1
# Exact rational check of formula for integer t in shear family.
for d in range(2,10):
    for t in range(2,8):
        q = Fraction(t-1,t) + Fraction(t-1, d-1+t*(t-1))
        p = Fraction(d-1, t*(d-1+t*(t-1)))
        assert q+p==1
        checks+=1
print('PASS:',checks,'checks; sheared ridge normal probabilities, complete right-simplex active-face census, rational identities')
