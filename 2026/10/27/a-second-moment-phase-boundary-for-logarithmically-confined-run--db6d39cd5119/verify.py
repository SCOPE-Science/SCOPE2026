"""Finite-domain backward-generator cross-check for logarithmic RTP hitting times.
Discrete upwind CTMC on [lo,hi], two sign orientations, absorbing exits.
No inference about infinite hitting moments is drawn from a finite grid.
"""
import numpy as np
from scipy.sparse import lil_matrix,csc_matrix
from scipy.sparse.linalg import splu

def moments(v,gamma,lo,hi,dx=.04,initial=2.0):
    N=int(round((hi-lo)/dx))
    dx=(hi-lo)/N
    xs=lo+(np.arange(N+1)*dx)
    n=N-1
    Q=lil_matrix((2*n,2*n),dtype=float)
    for i,x in enumerate(xs[1:-1]):
        for sign_idx,sigma in enumerate((1,-1)):
            j=2*i+sign_idx
            vel=v*sigma-1/(1+x)
            Q[j,j]-=abs(vel)/dx+gamma
            Q[j,j^1]+=gamma
            neighbor=i+(1 if vel>0 else -1)
            if 0<=neighbor<n:
                Q[j,2*neighbor+sign_idx]+=abs(vel)/dx
    LU=splu(csc_matrix(-Q))
    m1=LU.solve(np.ones(2*n))
    m2=LU.solve(2*m1)
    k=int(round((initial-lo)/dx))-1
    return (m1[2*k]+m1[2*k+1])/2,(m2[2*k]+m2[2*k+1])/2

def symbolic_checks():
    import sympy as sp
    y,v,g,C=sp.symbols('y v g C',positive=True)
    D=v**2/(2*g)
    H2=lambda s:y**2+(v/g)*s*y
    H4=lambda s:y**4+(2*v/g)*s*y**3
    for s in (-1,1):
        def act(H):
            return (v*s-1/y)*sp.diff(H(s),y)+g*(H(-s)-H(s))
        expected2=-2*(1-D)-(v*s)/(g*y)
        expected4=-4*(1-3*D)*y**2-(6*v/g)*s*y
        assert sp.simplify(act(H2)-expected2)==0
        assert sp.simplify(act(H4)-expected4)==0
    c=1/(2*(1-D)); lead_c=c/(2*(1-3*D))
    assert sp.simplify(-4*(1-3*D)*lead_c+2*c)==0
    print('exact generator and large-distance coefficient identities: PASS')

if __name__=='__main__':
    symbolic_checks()
    v=0.5; lo=1.5; start=2
    print('v=0.5; positive-drift exterior; start=2; finite absorbing box')
    for gamma in (0.25,0.375,0.50):
        D=v*v/(2*gamma)
        print('gamma',gamma,'D',D)
        for hi in (12,24,48,96,192):
            m1,m2=moments(v,gamma,lo,hi,dx=.045,initial=start)
            print('L',hi,'m1',round(m1,6),'m2',round(m2,6))

    # Finite-domain asymptotic trends, not proofs at infinite volume.
    noncrit_a=[moments(v,0.25,lo,hi,.045,start)[1] for hi in (48,192)]
    crit_a=[moments(v,0.375,lo,hi,.045,start)[1] for hi in (48,192)]
    finite_a=[moments(v,0.50,lo,hi,.045,start)[1] for hi in (48,192)]
    assert noncrit_a[1]>3*noncrit_a[0]
    assert crit_a[1]>1.4*crit_a[0]
    assert 1<finite_a[1]/finite_a[0]<1.10
    print('finite-box trend consistency checks: PASS')
