"""Reproduce tensor-product spectral mixing formulas and Petersen projector identities.

Dependencies: Python 3, numpy, sympy. Finite tests support, but do not replace,
the parameter-uniform mathematical argument given in RESULT.md.
"""
from itertools import combinations
from math import cos, pi
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0

def verify(x, msg='failed'):
    global checks
    assert x, msg
    checks += 1

def petersen():
    verts = tuple(combinations(range(5), 2))
    a = sp.Matrix(10, 10, lambda i,j: int(i!=j and set(verts[i]).isdisjoint(verts[j])))
    return a

def cycle(n):
    return sp.Matrix(n,n,lambda i,j: int((i-j) % n in (1,n-1) and i != j))

def complete(n):
    return sp.ones(n)-sp.eye(n)

def local_projection_test():
    a=petersen(); n=10; I=sp.eye(n); J=sp.ones(n)
    verify(a*a == 2*I-a+J, 'SRG relation')
    e=(4*I+2*a-J)/6
    verify(e*e==e, 'projector idempotence')
    verify(a*e==e, 'Fiedler spectral projection')
    verify(e.rank()==5, 'Fiedler eigenspace dimension')
    for v in range(n):
        nbr=[u for u in range(n) if a[v,u]]
        verify(len(nbr)==3, 'Petersen degree')
        d=sp.Matrix.hstack(*[I[:,u]-I[:,v] for u in nbr])
        verify(d.T*e*d == sp.Rational(2,3)*sp.eye(3), 'local Fiedler Gram')
    # Spectral identity on all Petersen vectors.
    verify(sorted(a.eigenvals().keys()) == [-2,1,3], 'Petersen eigenvalues')

def spectral_gap_values(g):
    a=np.asarray(g).astype(float)
    d=float(sum(a[0,:]))
    l=d*np.eye(len(a))-a
    e=np.linalg.eigvalsh(l)
    return d,float(e[1]),float(e[-1])

def kron_sum(mats):
    sizes=[m.shape[0] for m in mats]
    N=int(np.prod(sizes))
    out=np.zeros((N,N))
    for i,m in enumerate(mats):
        term=np.array([[1.]])
        for j,n in enumerate(sizes):
            if i==j: base=m
            else: base=np.eye(n)
            term=np.kron(term,base)
        out+=term
    return out

def product_test(mats):
    params=[]; laps=[]
    for mat in mats:
        a=np.asarray(mat).astype(float)
        degree, gap, high=spectral_gap_values(mat)
        params.append((degree,gap,high))
        laps.append(degree*np.eye(len(a))-a)
    C=sum(d/x for d,x,b in params)
    E=sum(b/x for d,x,b in params)
    t=min(2/(E+1),1/C)
    weights=[t/x for d,x,b in params]
    L=kron_sum([weights[i]*laps[i] for i in range(len(laps))])
    P=np.eye(L.shape[0])-L
    r=1-t
    verify(np.max(np.abs(P-P.T))<1e-12,'symmetry')
    verify(np.min(P)>-1e-12,'nonnegativity')
    verify(np.max(np.abs(P.sum(axis=1)-1))<1e-12,'row-stochastic')
    eigen=np.linalg.eigvalsh(P)
    verify(abs(eigen[-1]-1)<1e-10,'constant eigenvalue')
    verify(abs(max(abs(eigen[:-1]))-r)<1e-9,'optimal spectral radius')
    verify(abs(1-C*t-P[0,0])<1e-9,'hold probability')
    # All nontrivial tensor eigenvalues lie inside the sharp spectral interval.
    verify(eigen[0]>=-r-1e-9,'lower spectral bound')
    verify(eigen[-2]<=r+1e-9,'upper spectral bound')
    return C,E,t,r

def integer_spectral_bound_tests():
    for k in range(1,21):
        for m in range(4,61):
            th=2*pi/m
            alpha=2-2*cos(th)
            beta=2-2*cos(2*pi*(m//2)/m)
            C=1.5*k+2/alpha
            E=2.5*k+beta/alpha
            t=min(2/(E+1),1/C)
            verify(t>0,'positive step')
            verify(t*C<=1+1e-9,'budget bound')
            verify(t*(E+1)<=2+1e-9,'spectral lower bound')
            if k==1:verify(1-t*C>1e-12,'holding when one Petersen factor')
            else:verify(abs(1-t*C)<1e-10,'no holding when at least two Petersen factors')

def random_local_tests():
    # Perturb edge weights independently; diagonal is reset to maintain row sums.
    rng=np.random.default_rng(21489)
    for mats in ([petersen(),cycle(4)],[petersen(),cycle(5)],[cycle(4),cycle(5)]):
        C,E,t,r=product_test(mats)
        sizes=[x.rows for x in mats]
        weighted_laps=[]
        for a in mats:
            d=float(sum(np.array(a)[0,:])); _,alpha,_=spectral_gap_values(a)
            weighted_laps.append((t/alpha)*(d*np.eye(a.rows)-np.asarray(a,dtype=float)))
        P=np.eye(int(np.prod(sizes)))-kron_sum(weighted_laps)
        N=len(P)
        edges=np.array([(i,j) for i in range(N) for j in range(i+1,N) if P[i,j]>1e-12])
        for rep in range(24):
            Q=P.copy()
            ix=rng.choice(len(edges),size=min(6,len(edges)),replace=False)
            for eidx in ix:
                i,j=edges[eidx]
                perturb=float(rng.uniform(-0.02,0.02))*P[i,j]
                Q[i,j]+=perturb;Q[j,i]+=perturb
                Q[i,i]-=perturb;Q[j,j]-=perturb
            verify(np.min(Q)>-1e-10,'perturbed stochastic feasibility')
            ev=np.linalg.eigvalsh(Q)
            verify(max(abs(ev[:-1]))>=r-1e-9,'no improvement by perturbation')

def main():
    local_projection_test()
    integer_spectral_bound_tests()
    for mats in ([petersen(),cycle(4)],[petersen(),cycle(5)],[petersen(),complete(3)],
                 [petersen(),petersen()],[cycle(4),cycle(5)],[complete(3),cycle(4)]):
        product_test(mats)
    random_local_tests()
    print('PASS',checks,'assertions')
    alpha=(5-sp.sqrt(5))/2;beta=(5+sp.sqrt(5))/2
    for k in (1,2):
        C=sp.Rational(3,2)*k+2/alpha
        E=sp.Rational(5,2)*k+beta/alpha
        t=sp.Min(2/(E+1),1/C)
        print('Petersen^%s x C5:'%k,'t',sp.simplify(t),'r',sp.N(1-t,15),'hold',sp.N(1-C*t,15))

if __name__=='__main__':main()
