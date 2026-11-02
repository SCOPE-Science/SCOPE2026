"""Reproduce algebraic identities and finite-volume edge diagnostics.

The finite-volume calculation checks the theorem numerically but is not its proof.
Requires Python 3, sympy, scipy, numpy.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, lil_matrix
from scipy.sparse.linalg import spsolve


def symbolic_checks():
    mu, v, R, gamma = sp.symbols('mu v R gamma', positive=True)
    g = (R**2-v**2)/(2*mu)
    lo, hi = (R-v)/mu, (R+v)/mu
    drift = lambda z, s: -mu*z + 2*g/z + 2*v*s
    z = sp.Symbol('z')
    kap_lo = sp.simplify(-sp.diff(drift(z,-1),z).subs(z,lo))
    kap_hi = sp.simplify(-sp.diff(drift(z,1),z).subs(z,hi))
    checks = [
        sp.simplify(drift(lo,-1)), sp.simplify(drift(hi,1)),
        sp.simplify(drift(hi,0)+2*v), sp.simplify(drift(lo,0)-2*v),
        sp.simplify(kap_lo-2*mu*R/(R-v)),
        sp.simplify(kap_hi-2*mu*R/(R+v)),
        sp.simplify(mu*R/(R-v)-mu*R/(R+v)-v*R/g),
        sp.simplify((R+v)/(mu*R)+(R-v)/(mu*R)-2/mu),
        sp.simplify((2*gamma/kap_hi)-(gamma*(R+v)/(mu*R))),
        sp.simplify((2*gamma/kap_lo)-(gamma*(R-v)/(mu*R))),
    ]
    assert all(c == 0 for c in checks), checks
    assert sp.simplify(kap_lo.subs({mu:1,R:3,v:1})-3) == 0
    assert sp.simplify(kap_hi.subs({mu:1,R:3,v:1})-sp.Rational(3,2)) == 0
    assert sp.simplify((2*gamma/kap_lo).subs({mu:1,R:3,v:1,gamma:1})-sp.Rational(2,3)) == 0
    assert sp.simplify((2*gamma/kap_hi).subs({mu:1,R:3,v:1,gamma:1})-sp.Rational(4,3)) == 0
    print('Symbolic algebra: 14 exact identities passed')


def generator(mu=1.,v=1.,g=4.,gamma=1.,N=4000):
    R=math.sqrt(v*v+2*mu*g)
    lo,hi=(R-v)/mu,(R+v)/mu
    dx=(hi-lo)/N
    dim=3*N
    rows=[]; cols=[]; vals=[]
    def add(i,j,value):
        rows.append(i); cols.append(j); vals.append(value)
    # state -1, 0, 1; column generator
    for i in range(N):
        for s in range(3):
            j=3*i+s
            ss=s-1
            left=lo+i*dx; right=left+dx
            fl=-mu*left+2*g/left+2*v*ss
            fr=-mu*right+2*g/right+2*v*ss
            outgoing=0.
            if i>0 and fl<0:
                rate=-fl/dx
                add(3*(i-1)+s,j,rate); outgoing+=rate
            if i<N-1 and fr>0:
                rate=fr/dx
                add(3*(i+1)+s,j,rate); outgoing+=rate
            if s in (0,2):
                add(3*i+1,j,2*gamma); outgoing+=2*gamma
            else:
                for other in (0,2):
                    add(3*i+other,j,gamma); outgoing+=gamma
            add(j,j,-outgoing)
    Q=coo_matrix((vals,(rows,cols)),shape=(dim,dim)).tocsr()
    # Replace one row by normalization; actual Q columns sum to zero.
    assert np.max(np.abs(np.asarray(Q.sum(axis=0)).ravel()))<1e-10
    A=Q.tolil()
    A[0,:]=1.
    rhs=np.zeros(dim);rhs[0]=1.
    mass=spsolve(A.tocsr(),rhs).reshape(N,3)
    assert abs(mass.sum()-1)<1e-9
    assert mass.min()>-1e-10
    return mass,dx,lo,hi


def finite_volume_checks():
    mass,dx,lo,hi=generator()
    R=3.
    target_low=2/3
    target_high=4/3
    # Edge tails over broad mesoscopic windows: finite-volume approximation.
    cells=np.array([15,20,30,45,65,90,125,170],dtype=int)
    lower=np.array([mass[:i,:].sum() for i in cells]);upper=np.array([mass[-i:,:].sum() for i in cells])
    low_est=np.polyfit(np.log(cells*dx),np.log(lower),1)[0]
    high_est=np.polyfit(np.log(cells*dx),np.log(upper),1)[0]
    print(f'Finite-volume N={len(mass)}, interval [{lo:g},{hi:g}]: '
          f'low tail exponent {low_est:.5f} (theory {target_low:.5f}); '
          f'high tail exponent {high_est:.5f} (theory {target_high:.5f})')
    assert abs(low_est-target_low)<0.14
    assert abs(high_est-target_high)<0.14
    # Rare switches and geometry imply unequal rates; one vanishing and one diverging edge.
    assert target_low < 1 < target_high
    # The zero-velocity population vanishes linearly relative to the
    # endpoint-attracting velocity population on either side.
    cell=20
    eps=cell*dx
    at_lower=mass[cell,:]
    at_upper=mass[-cell-1,:]
    lower_ratio=at_lower[1]/(at_lower[0]*eps)
    upper_ratio=at_upper[1]/(at_upper[2]*eps)
    assert abs(lower_ratio-1.5)<0.15
    assert abs(upper_ratio-0.75)<0.15
    print(f'Conditioned ratios per distance: lower={lower_ratio:.5f} '
          f'(theory 1.5), upper={upper_ratio:.5f} (theory 0.75)')
    print('Finite-volume edge diagnostics: 6 assertions passed')


if __name__ == '__main__':
    symbolic_checks()
    finite_volume_checks()
    print('All algebraic and finite-volume checks passed.')
