"""Reproducible numerical checks of the C_n Cartesian K_m no-holding FMMC theorem.
Run: python verify_cyclic_layers.py  (requires NumPy and SciPy).
The analytical proof in RESULT.md, not finite tests, establishes the infinite claim.
"""
from math import pi,cos,isclose
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.linalg import null_space


def delta(n):
    return 2*(1-cos(2*pi/n)), 2*(1-cos(2*pi*(n//2)/n))


def formulas(n,m):
    assert n>=3 and m>=2
    al,be=delta(n)
    if m==2:
        if n%2==0:
            return 0.25,0.5,1.0,'bipartite; any feasible is optimal'
        ga=4-be
        a=2/(4+ga)
        return a,1-2*a,(4-ga)/(4+ga),'two-layer odd'
    a_l=(m-2)/((m-1)*(al+be)-2*m)
    a_h=m/(2*m+(m-1)*al)
    if (n,m)==(3,3):
        return 1/6,1/3,0.5,'exceptional optimal interval [1/6,1/3]'
    a=min(a_l,a_h)
    return a,(1-2*a)/(m-1),1-al*a,('low-frequency negative' if a_l<=a_h else 'clique-positive')


def spectrum(n,m,a,b):
    ks=np.arange(n)
    dk=2-2*np.cos(2*np.pi*ks/n)
    return np.r_[1-a*dk, 1-m*b-a*dk.repeat(m-1)]


def slem(n,m,a):
    al,be=delta(n)
    b=(1-2*a)/(m-1)
    return max(1-al*a,1-m*b, m*b+be*a-1)


def matrix(n,m,a,b):
    N=n*m
    P=np.zeros((N,N))
    for i in range(n):
        for l in range(m):
            u=i*m+l
            for j in ((i-1)%n,(i+1)%n):P[u,j*m+l]=a
            for r in range(m):
                if r!=l:P[u,i*m+r]=b
    return P


def edge_matrix(n,m):
    E=[]
    for i in range(n):
        for l in range(m): E.append((i*m+l,((i+1)%n)*m+l))
    for i in range(n):
        for l in range(m):
            for r in range(l+1,m): E.append((i*m+l,i*m+r))
    return E


def checks():
    count_scalar=0
    for n in range(3,81):
        for m in range(2,24):
            a,b,mu,kind=formulas(n,m)
            assert -1e-12<=a<=.5+1e-12 and b>=-1e-12 and abs(2*a+(m-1)*b-1)<3e-12
            assert abs(slem(n,m,a)-mu)<5e-11, (n,m,kind)
            res=minimize_scalar(lambda x:slem(n,m,x),bounds=(0,.5),method='bounded',options={'xatol':1e-13})
            assert mu<=res.fun+5e-9, (n,m,res.fun,mu)
            # Independently verify mode transition and the special flat interval.
            al,be=delta(n)
            if m>=3 and n%2==1 and n>=5:
                assert ('clique-positive' in kind)==(m>=8)
            if (n,m)==(3,3):
                for x in (1/6, 1/5, 1/4, 1/3):assert abs(slem(n,m,x)-.5)<1e-12
            count_scalar+=1
    full=0
    perturb=0
    rng=np.random.default_rng(20261026)
    for n in range(3,11):
        for m in range(2,8):
            a,b,mu,kind=formulas(n,m)
            P=matrix(n,m,a,b)
            assert np.max(abs(P-P.T))<1e-12
            assert np.max(abs(P.sum(axis=1)-1))<1e-12
            eig=np.linalg.eigvalsh(P)
            assert abs(max(abs(eig[:-1]))-mu)<1e-10,(n,m,mu,eig)
            ref=np.sort(spectrum(n,m,a,b))
            assert max(abs(ref-eig))<1e-9,(n,m,ref,eig)
            full+=1
    for n,m in [(3,2),(5,2),(7,2),(3,3),(4,3),(5,4),(7,5),(8,6),(9,7)]:
        a,b,mu,_=formulas(n,m)
        P=matrix(n,m,a,b)
        E=edge_matrix(n,m)
        N=n*m
        Inc=np.zeros((N,len(E)))
        for col,(u,v) in enumerate(E): Inc[u,col]=1; Inc[v,col]=1
        V=null_space(Inc)
        if not V.size: continue
        base=np.array([P[u,v] for u,v in E])
        for z in range(25):
            t=V@rng.standard_normal(V.shape[1]);t=t/np.max(abs(t))
            eps=.14*min(base[base>1e-12]) if np.all(base>1e-12) else .0
            if eps==0:continue
            pw=base+eps*t
            Q=np.zeros((N,N))
            for (u,v),w in zip(E,pw): Q[u,v]=Q[v,u]=w
            assert np.min(pw)>0 and np.max(abs(Q.sum(axis=1)-1))<1e-11
            eig=np.linalg.eigvalsh(Q)
            assert max(abs(eig[:-1]))+1e-10>=mu
            perturb+=1
    assert abs(formulas(3,6)[0]-2/9)<1e-12
    assert abs(formulas(3,6)[2]-1/3)<1e-12
    print(f'VERIFY_OK: {count_scalar} scalar optimizations; {full} full matrix spectra; {perturb} asymmetric feasible perturbations; exact small rational values.')

if __name__=='__main__':checks()
