"""Finite-volume stationary check for a two-particle active Coulomb gap."""
import math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def fvm(lam,g,v,gamma,n):
    k=math.hypot(v, math.sqrt(2*lam*g))
    a=(k-v)/lam; b=(k+v)/lam
    h_a=lam*(a+b)/a; h_b=lam*(a+b)/b
    alpha_a=2*gamma/h_a; alpha_b=2*gamma/h_b
    face=a+(b-a)*(1-np.cos(np.linspace(0,math.pi,n+1)))/2
    width=np.diff(face)
    mid=(face[:-1]+face[1:])/2
    rows=[]; cols=[]; vals=[]
    diag=np.zeros(3*n)
    for is_,s in enumerate((-1,0,1)):
        face_v=-lam*face[1:-1]+2*g/face[1:-1]+2*v*s
        for j,F in enumerate(face_v):
            if F>0: src=is_*n+j; dst=src+1; rate=F/width[j]
            else: src=is_*n+j+1; dst=src-1; rate=-F/width[j+1]
            rows.append(dst);cols.append(src);vals.append(rate)
            diag[src]-=rate
    for i in range(n):
        for src_s, dst_s, rate in [(0,1,2*gamma),(2,1,2*gamma),(1,0,gamma),(1,2,gamma)]:
            src=src_s*n+i;dst=dst_s*n+i
            rows.append(dst);cols.append(src);vals.append(rate)
            diag[src]-=rate
    rows.extend(range(3*n));cols.extend(range(3*n));vals.extend(diag)
    # stationary column kernel with pinned equation
    mat=coo_matrix((vals,(rows,cols)),shape=(3*n,3*n)).tolil()
    mat[-1,:]=1
    vec=np.zeros(3*n);vec[-1]=1
    mass=spsolve(mat.tocsc(),vec)
    assert np.isfinite(mass).all() and mass.min()>-1e-10
    assert abs(sum(mass)-1)<1e-9
    probs=mass.reshape((3,n)).sum(axis=0)
    assert max(abs(mass[:n].sum()-.25),abs(mass[n:2*n].sum()-.5),abs(mass[2*n:].sum()-.25))<5e-8
    def left_cdf(e):
        j=np.searchsorted(face,a+e,side='right')-1
        j=max(0,min(n,j))
        left=probs[:j].sum()
        if j<n: left+=probs[j]*max(0,min(1,((a+e)-face[j])/width[j]))
        return left
    def right_cdf(e):
        j=np.searchsorted(face,b-e,side='right')-1
        j=max(0,min(n,j))
        right=probs[j+1:].sum() if j+1<n else 0
        if j<n: right+=probs[j]*max(0,min(1,(face[j+1]-(b-e))/width[j]))
        return right
    e1=(b-a)*.002; e2=(b-a)*.007
    slope_left=math.log(left_cdf(e2)/left_cdf(e1))/math.log(e2/e1)
    slope_right=math.log(right_cdf(e2)/right_cdf(e1))/math.log(e2/e1)
    assert abs(slope_left-alpha_a)<.13, (slope_left,alpha_a)
    assert abs(slope_right-alpha_b)<.13, (slope_right,alpha_b)
    assert math.isclose(alpha_a+alpha_b,2*gamma/lam,rel_tol=2e-14)
    return dict(n=n, gamma=gamma, interval=[a,b], predicted=[alpha_a,alpha_b], finite_volume=[slope_left,slope_right], endpoint_prob=[left_cdf(e1),right_cdf(e1)])


def main():
    lam=1.;g=1.;v=1.
    for gamma in (.35,.8,1.,2.8):
        result=fvm(lam,g,v,gamma,5000)
        print(result)
        h=2*math.sqrt(v*v+2*lam*g)
        ga=lam*math.sqrt(v*v+2*lam*g)/(math.sqrt(v*v+2*lam*g)-v)
        gb=lam*math.sqrt(v*v+2*lam*g)/(math.sqrt(v*v+2*lam*g)+v)
        assert gb<ga
        if gamma<gb: assert result['predicted'][1]<1
        elif gamma<ga: assert result['predicted'][0]<1<result['predicted'][1]
        else: assert result['predicted'][0]>1
    print('PASS: all stationary generators, mode marginals, predicted edge slopes, and strict threshold regimes.')

if __name__=='__main__':
    main()
