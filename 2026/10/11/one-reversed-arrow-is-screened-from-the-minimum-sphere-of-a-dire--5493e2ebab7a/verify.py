#!/usr/bin/env python3
"""Exact finite checks and an independent nonlinear minimax sample."""
from fractions import Fraction as F
from scipy.optimize import minimize
import numpy as np

n_exact=0
n_minimax=0
for m in range(3, 26):
    for j in range(m):
        a,b=j,m-1-j
        denom=a*(a+1)*(a+2)+b*(b+1)*(b+2)
        lam=F(12,denom)
        assert denom == (m+1)*(m*(m-1)-3*a*b)
        p=[F(0)]*m
        for i in range(a):
            p[i]=lam*F((i+1)*(a-i),2)
        for u in range(b):
            i=j+1+u
            p[i]=lam*F((u+1)*(b-u),2)
        assert sum(p)==1
        signs=[1]*m
        signs[j]=-1
        verts=[]
        for i in range(m):
            v=[F(0)]*(m+1)
            v[i]=F(signs[i]);v[i+1]=F(-signs[i])
            verts.append(v)
        c=[sum((p[i]*verts[i][t] for i in range(m)), F(0)) for t in range(m+1)]
        assert sum(x*x for x in c)==lam
        d2=[sum((verts[i][t]-c[t])**2 for t in range(m+1)) for i in range(m)]
        R2=F(2)-lam
        assert max(d2)==R2
        assert all(d2[i]==R2 for i in range(m) if i !=j)
        assert R2-d2[j]==lam*(m-3)
        assert (d2[j]<R2)==(m>=4)
        assert all(p[i]>0 for i in range(m) if i !=j)
        assert p[j]==0
        if m>=4:
            a2,b2=(m-1)//2,(m-1)-(m-1)//2
            d2max=a2*(a2+1)*(a2+2)+b2*(b2+1)*(b2+2)
            assert denom>=d2max
        n_exact+=1

        if m <= 10:
            V=np.array(verts,dtype=float)
            def obj(z):return z[-1]
            def grad(z):return np.r_[np.zeros(m+1),1.0]
            def cons(z):return z[-1]-np.sum((V-z[:-1])**2,axis=1)
            def jac(z):
                out=np.zeros((m,m+2))
                out[:,:-1]=2*(V-z[:-1])
                out[:,-1]=1
                return out
            z=np.r_[np.zeros(m+1),2.0]
            sol=minimize(obj,z,jac=grad,constraints=[{'type':'ineq','fun':cons,'jac':jac}],method='SLSQP',options={'ftol':1e-11,'maxiter':500})
            assert sol.success,(m,j,sol.message)
            assert abs(sol.x[-1]-float(R2))<1e-7,(m,j,sol.x[-1],R2)
            assert np.linalg.norm(sol.x[:-1]-np.array(c,dtype=float))<1e-6,(m,j,sol.x[:-1],c)
            n_minimax+=1

print('VERIFY_OK one-flipped-directed-path exact_fraction_cases=%d independent_full_minimax_cases=%d all_contact_spectra=yes position_extremality=yes' % (n_exact,n_minimax))
