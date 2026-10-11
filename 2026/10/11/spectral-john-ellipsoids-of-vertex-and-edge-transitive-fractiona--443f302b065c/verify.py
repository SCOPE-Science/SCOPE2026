"""Numerical consistency checks for graph-symmetric fractional-matching John ellipsoids.

Requires Python >=3.10, numpy, scipy. All instances below are exact combinatorial
input graphs. Numerical checks corroborate, but do not prove, the general theorem.
"""
import itertools
import math
import numpy as np
from scipy.optimize import brentq


def models():
    for n in range(3, 22):
        yield f'C{n}', n, sorted(tuple(sorted((i,(i+1)%n))) for i in range(n))
    for n in range(3, 11):
        yield f'K{n}', n, list(itertools.combinations(range(n),2))
    for k in range(2, 9):
        yield f'K{k},{k}', 2*k, [(i,k+j) for i in range(k) for j in range(k)]
    for d in range(2, 6):
        yield f'Q{d}', 2**d, [(i,j) for i in range(2**d) for j in range(i+1,2**d) if (i^j).bit_count()==1]
    # Petersen, automorphism group vertex-and-edge transitive.
    yield 'Petersen', 10, ([(i,(i+1)%5) for i in range(5)]
                              + [(5+i,5+(i+2)%5) for i in range(5)]
                              + [(i,5+i) for i in range(5)])
    # octahedron graph = complete 3-partite, each part size 2.
    yield 'Octahedral',6,[(i,j) for i in range(6) for j in range(i+1,6) if i//2!=j//2]


def test(name,n,edges):
    m=len(edges)
    B=np.zeros((n,m))
    for j,(u,v) in enumerate(edges):
        B[u,j]=B[v,j]=1
    deg=B.sum(axis=1)
    d=int(deg[0]); assert d>=2 and np.max(abs(deg-d))<1e-12
    M0=B@B.T
    eig=np.linalg.eigvalsh(M0)
    def vt(t):
        return np.sum(eig/(1+0.5*t*eig))/n
    def eq(t):
        return t*(1+d*t)*vt(t)/d-1
    t=brentq(eq,1e-9,5,xtol=1e-13)
    a=t/(1+d*t); alpha=t/(d*(1+d*t))
    Mat=np.eye(m)+t/2*(B.T@B)
    Sigma=alpha*np.linalg.inv(Mat)
    U=B@Sigma@B.T
    assert np.max(abs(np.diag(Sigma)-a*a)) < 3e-11,(name,'edge',t)
    assert np.max(abs(np.diag(U)-(1-d*a)**2)) < 3e-11,(name,'vertex',t)
    p=d*t/(1+d*t); q=d/(2*(1+d*t))
    # Centroid condition in original coordinates after whitening.
    v1=-p/a*np.ones(m)+q/(1-d*a)*(B.T@np.ones(n))
    assert np.linalg.norm(v1)<2e-10,(name,'first',np.linalg.norm(v1))
    S2=p/a**2*np.eye(m)+q/(1-d*a)**2*(B.T@B)
    assert np.max(abs(S2@Sigma-np.eye(m))) <3e-10,(name,'second')
    assert abs(m*p+n*q-m)<3e-10,(name,'weights')
    assert abs(np.sum(np.linalg.eigvalsh(Sigma)) -np.trace(Sigma))<1e-10
    return n,m,t,a


if __name__=='__main__':
    total=0; ce=0; cv=0; cycle=[]
    for name,n,edges in models():
        row=test(name,n,edges)
        total+=1; ce+=row[1]; cv+=row[0]
        if name.startswith('C'): cycle.append(row)
        print(f'{name}: n={n}, m={row[1]}, root={row[2]:.10f}, center={row[3]:.10f}')
    phi=(1+math.sqrt(5))/2
    print('CYCLE_LIMIT',phi/2)
    assert abs(cycle[-1][2]-phi/2)<0.0005
    print(f'ALL CHECKS PASS graphs={total}, facet_contacts={ce+cv}, edge_contacts={ce}, vertex_contacts={cv}')
