#!/usr/bin/env python3
"""Standalone numerical and algebraic checks for a two-orbit graph-lattice norm formula."""
import itertools, math
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from numpy.linalg import eigvalsh

def family(v):
    vertices=list(itertools.combinations(range(v),2))
    N=len(vertices); Es=[[],[]]
    for i in range(N):
        for j in range(i+1,N):
            typ=0 if set(vertices[i]) & set(vertices[j]) else 1
            vec=np.zeros(N);vec[i]=1.;vec[j]=-1.
            Es[typ].append(vec)
    return N, Es

def constants(v):
    c=(v-4)/(v-3)
    A=math.sqrt(2*(v-1)/(v-2))
    B=(v-3)*math.sqrt(v/(v-2))
    lo=(A+B)/(2*A+c*B)
    hi=math.inf if v==4 else (A/math.sqrt(2)+B/math.sqrt(c))/(math.sqrt(2)*A+math.sqrt(c)*B)
    return c,A,B,lo,hi

def formula(v,a):
    b=a*a;c,A,B,lo,hi=constants(v)
    if b<=lo:
        x=1.; f=A+B; branch='original'
    elif b>=hi:
        x=0.;f=a*(math.sqrt(2)*A+math.sqrt(c)*B);branch='complement'
    else:
        # unique interior optimizer; formula exact
        u=2*b-1; z=1-c*b
        x=(2*b*B*B*z*z-c*b*A*A*u*u)/(u*z*(B*B*z+A*A*u))
        f=math.sqrt(b*(2-c)*(A*A/z+B*B/u));branch='mixed'
    return f,x,branch

def direct_uniform(v,a,x):
    N,Es=family(v);L=np.zeros((N,N))
    for vec in Es[0]: L+= x/len(Es[0])*np.outer(vec,vec)
    for vec in Es[1]: L+= (1-x)*a*a/len(Es[1])*np.outer(vec,vec)
    return np.sqrt(np.maximum(eigvalsh(L)[1:],0)).sum()

def unrestricted(v,a,initial_seed):
    N,Es=family(v)
    rows=np.vstack([*Es[0],*Es[1]])
    scales=np.array([1.]*len(Es[0])+[a]*len(Es[1]))
    r=rows*scales[:,None]
    Q=np.linalg.qr(np.column_stack((np.ones(N)/math.sqrt(N),np.eye(N)[:,:N-1])))[0][:,1:]
    # eliminate constant direction to avoid fictitious derivatives
    r=r@Q
    m=len(r)
    rng=np.random.default_rng(initial_seed)
    w=rng.dirichlet(np.full(m,2.))
    def objective(w):
        L=r.T@(w[:,None]*r)
        lam,U=np.linalg.eigh(L)
        if min(lam)<1e-12:
            val=np.sqrt(np.maximum(lam,0)).sum()
            # jitter only if degenerate -- not expected at tested configurations
            return -val, -np.zeros(m)
        val=np.sqrt(lam).sum()
        invhalf=(U*(lam**-.5))@U.T
        g=.5*np.einsum('ij,jk,ik->i',r,invhalf,r)
        return -val,-g
    result=minimize(objective,w,jac=True,method='SLSQP',bounds=[(0,1)]*m,
                    constraints=[{'type':'eq','fun':lambda w:np.sum(w)-1,'jac':lambda w:np.ones(m)}],
                    options={'ftol':1e-11,'maxiter':600})
    if not result.success and abs(result.fun+formula(v,a)[0])>2e-5:
        raise AssertionError(f'unrestricted optimization failed n={v} a={a}: {result.message}')
    return -result.fun, result.x

def run():
    checks=0
    for v in range(4,13):
        N,Es=family(v); assert len(Es[0])==N*(v-2)
        assert len(Es[1])==N*(v-2)*(v-3)//4
        c,A,B,lo,hi=constants(v)
        assert 0<lo<1 and hi>1
        for a in sorted(set([.1,.5,math.sqrt(lo), (math.sqrt(lo)+1)/2,1., 1.05,math.sqrt(hi)*.98 if v>4 else 2.,math.sqrt(hi)*1.02 if v>4 else 10.,2.,4.])):
            f,x,branch=formula(v,a)
            if not(0<=x<=1):raise AssertionError((v,a,f,x,branch))
            baseline=direct_uniform(v,a,x)
            if abs(f-baseline)>1e-8:raise AssertionError((v,a,f,baseline,branch,x))
            res=minimize_scalar(lambda t:-direct_uniform(v,a,t),bounds=(0,1),method='bounded', options={'xatol':1e-13})
            if (-res.fun)-f>1e-7:raise AssertionError((v,a,'scalar',-res.fun,f))
            checks+=1
    print('OK exact-formula vs actual weighted graph eigenspectra',checks)
    checks=0
    for v in (4,5,6):
        c,A,B,lo,hi=constants(v)
        candidates=[math.sqrt(lo)*.93, math.sqrt(lo)*1.015,1.,math.sqrt(hi)*1.02,1.3] if v>4 else [.6,math.sqrt(lo)*1.02,1.,1.5,3.]
        for index,a in enumerate(candidates):
            f,x,branch=formula(v,a)
            observed,w=unrestricted(v,a,31+index)
            if abs(f-observed)>1.5e-5:
                raise AssertionError((v,a,branch,f,observed))
            checks+=1
    print('OK full noninvariant design optimizations',checks)
    print('PASS')

if __name__=='__main__':run()
