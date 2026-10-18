#!/usr/bin/env python3
"""Independent finite-matrix checks for a two-orbit graph-gradient norm theorem.
The mathematical proof is in RESULT.md; tests do not establish all-parameter claims.
"""
import math
import itertools
import numpy as np
from scipy.optimize import minimize, minimize_scalar


def theoretical(a,b,t):
    k=(b-1)/math.sqrt(b)+math.sqrt((a+b)/(a*b))
    base=(a-1)/math.sqrt(a)+k
    zcrit=((a-1)+math.sqrt(a)*k)/(2*a)
    if t*t<=zcrit:
        return base,zcrit,0.0
    d=2*t*t/(a-1)-1/a
    u=((a-1)**2*d*d-k*k/a)/((a-1)**2*d*d+k*k*d)
    return math.sqrt(2*(a-1)*t*t+2*a*t*t*k*k/(2*a*t*t-(a-1))),zcrit,u


def full_eigen(a,b,t,u):
    n=a+b
    edges=[(i,j,t) for i in range(a) for j in range(i+1,a)]
    cross=[(i,j,1.) for i in range(a) for j in range(a,n)]
    masses=np.r_[np.repeat(u/len(edges),len(edges)),np.repeat((1-u)/len(cross),len(cross))]
    nvec=len(edges)+len(cross)
    mat=np.zeros((n,n))
    for w,(i,j,c) in zip(masses,edges+cross):
        p=w*c*c
        mat[i,i]+=p;mat[j,j]+=p;mat[i,j]-=p;mat[j,i]-=p
    vals=np.linalg.eigvalsh(mat)
    assert min(vals)>-1.e-10
    return float(np.sqrt(np.maximum(vals,0)).sum())


def unrestricted(a,b,t,amps=None, start_u=None):
    from scipy.linalg import null_space
    n=a+b
    es=[(i,j,t if amps is None else amps.get((i,j),0)) for i in range(a) for j in range(i+1,a)]
    es += [(i,j,1.) for i in range(a) for j in range(a,n)]
    es=[e for e in es if e[2]>0]
    m=len(es)
    basis=null_space(np.ones((1,n)))
    vectors=[]
    for i,j,v in es:
        z=np.zeros(n); z[i]=v;z[j]=-v
        vectors.append(basis.T@z)
    vectors=np.array(vectors)
    B=np.einsum('mi,mj->mij',vectors,vectors)
    cross_indices=[idx for idx,(i,j,v) in enumerate(es) if j>=a]
    clique_indices=[idx for idx,(i,j,v) in enumerate(es) if j<a]
    cross=np.zeros(m);cross[cross_indices]=1/len(cross_indices)
    if start_u is None:
        start_u=theoretical(a,b,t)[2] if amps is None else 0.
    initial=cross*(1-start_u)
    if clique_indices and start_u:
        initial[clique_indices]=start_u/len(clique_indices)
    def val_jac(w):
        M=np.einsum('i,ijk->jk',w,B)
        eig,U=np.linalg.eigh(M)
        eig=np.maximum(eig,1.e-11)
        val=np.sqrt(eig).sum()
        recip=U@np.diag(eig**(-.5))@U.T
        grad=.5*np.einsum('mij,ij->m',B,recip)
        return -val,-grad
    solutions=[]
    for w in [initial,cross,.5*(cross+np.ones(m)/m)]:
        o=minimize(val_jac,w,jac=True,method='SLSQP',bounds=[(0.,1.)]*m,
                 constraints=[{'type':'eq','fun':lambda v: np.sum(v)-1,'jac':lambda v:np.ones(m)}],
                 options={'maxiter':2000,'ftol':1.e-13})
        solutions.append(o)
    best=max((-sol.fun for sol in solutions if np.isfinite(sol.fun)))
    return best


def kkt_certificate(a,b,t):
    from scipy.linalg import null_space
    n=a+b
    _,_,u=theoretical(a,b,t)
    edges=[(i,j,t) for i in range(a) for j in range(i+1,a)]+[(i,j,1.) for i in range(a) for j in range(a,n)]
    w=np.array([u/(a*(a-1)/2)]*(a*(a-1)//2)+[(1-u)/(a*b)]*(a*b))
    B=null_space(np.ones((1,n)))
    L=np.zeros((n-1,n-1)); vecs=[]
    for i,j,v in edges:
        vec=B[i,:]*v-B[j,:]*v
        vecs.append(vec)
    for p,vec in zip(w,vecs):
        L+=p*np.outer(vec,vec)
    eigen,U=np.linalg.eigh(L)
    assert min(eigen)>1.e-10
    inv=U@np.diag(eigen**(-.5))@U.T
    d=np.array([.5*vec@inv@vec for vec in vecs])
    current=np.sqrt(eigen).sum()
    assert d.max()<=current/2+1.e-8,(a,b,t,d.max(),current/2)
    assert np.max(np.abs(d[w>1.e-12]-current/2))<1.e-8
    return current

def main():
    count=0
    for a,b in [(2,2),(2,5),(3,2),(3,4),(4,3),(4,6),(5,2)]:
        _,zc,_=theoretical(a,b,1)
        for t in [0.05, math.sqrt(zc)*0.65, math.sqrt(zc), math.sqrt(zc)*1.2, 2.0]:
            v,zc,u=theoretical(a,b,t)
            vg=full_eigen(a,b,t,u)
            assert abs(v-vg)<2.e-7,(a,b,t,u,v,vg)
            scalar=minimize_scalar(lambda z:-full_eigen(a,b,t,z),bounds=(0,1),method='bounded',options={'xatol':1.e-12})
            assert abs(-scalar.fun-v)<1.e-7,(a,b,t,v,-scalar.fun)
            count+=1
    print('PASS',count,'spectral-formula and orbit-optimizer comparisons')
    for a,b,t in [(2,3,.5),(2,3,1.),(3,2,1.),(3,4,1.5),(3,5,2.),(4,2,.7),(4,3,1.4),(5,2,2.)]:
        v,_,_=theoretical(a,b,t)
        numeric=unrestricted(a,b,t)
        assert abs(v-numeric)<1.e-5,(a,b,t,v,numeric)
        assert abs(v-kkt_certificate(a,b,t))<1.e-7
        count+=1
    print('PASS 8 unrestricted simplex-weight optimizations and first-order certificates')
    for a,b in [(2,3),(3,4),(4,3)]:
        _,zc,_=theoretical(a,b,1.)
        tc=math.sqrt(zc)
        av={(i,j):tc*.85 for i in range(a) for j in range(i+1,a)}
        base=theoretical(a,b,0)[0]
        observed=unrestricted(a,b,0,amps=av)
        assert abs(base-observed)<1.e-5,(a,b,observed,base)
        av[(0,1)]=tc*1.2
        observed=unrestricted(a,b,0,amps=av)
        assert observed>base+1.e-5,(a,b,observed,base)
        count+=2
    print('PASS 6 heterogeneous clique-edge screening checks')
    for a in [2,3,5]:
        for b in [2000,8000,32000]:
            _,zc,_=theoretical(a,b,1)
            leading=.5*math.sqrt(b/a)+.5
            assert abs(zc-leading)<.03,(a,b,zc,leading)
            count+=1
    print('PASS 9 high-imbalance asymptotic checks')
    print('ALL VERIFIED',count,'configurations')

if __name__=='__main__': main()
