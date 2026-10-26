#!/usr/bin/env python3
"""Exact checks for finite-sample monotonicity thresholds of second-difference smoothing.
Public reproducibility artifact; uses Python standard library only.
"""
from fractions import Fraction as F
from math import sqrt

def inv(a):
    n=len(a)
    z=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(k for k in range(j,n) if z[k][j])
        z[j],z[p]=z[p],z[j]
        h=z[j][j];z[j]=[v/h for v in z[j]]
        for k in range(n):
            if k==j:continue
            h=z[k][j]
            z[k]=[v-h*w for v,w in zip(z[k],z[j])]
    return [r[n:] for r in z]

def h_matrix(n,lam):
    d=[[F(int(j==i)-2*int(j==i+1)+int(j==i+2)) for j in range(n)] for i in range(n-2)]
    A=[[F(i==j)+lam*sum(r[i]*r[j] for r in d) for j in range(n)] for i in range(n)]
    S=inv(A)
    # H_ij = (S_(i+1),sum_{k>j})-(S_i,sum_{k>j})
    return [[sum(S[i+1][k]-S[i][k] for k in range(j+1,n)) for j in range(n-1)] for i in range(n-1)]

def h4_defect(t):
    return max(F(0),t*(1-6*t)/((1+2*t)*(1+10*t)))

def verify():
    # Exact symbolic factor signatures at representative rational parameters,
    # both sides of each sharp boundary.
    probes={3:[F(0),F(1,100),F(1,2),F(100)],
            4:[F(0),F(1,100),F(1,6),F(1,5),F(50)],
            5:[F(0),F(1,100),F(1,5),F(7,10),F(1),F(50)],
            6:[F(0),F(1,100),F(1,3),F(1),F(183,100),F(2),F(50)]}
    boundaries={3:F(0),4:F(1,6),5:F(7,10),6:(14+sqrt(181))/15}
    for n,ls in probes.items():
        for lam in ls:
            H=h_matrix(n,lam)
            assert all(sum(row)==1 for row in H)
            good=all(v>=0 for row in H for v in row)
            assert good==(lam==0 or float(lam)+1e-12 >= float(boundaries[n])),(n,lam,good,boundaries[n])
            assert all(v>=0 for row in H for v in row) if n==3 else True
            if n==4:
                neg=max(F(0),-min(v for row in H for v in row))
                assert neg==h4_defect(lam)
    # Exact four-point cross-threshold coefficient and an explicit step witness.
    for lam in [F(1,20),F(1,6),F(1,2)]:
        H=h_matrix(4,lam)
        assert H[2][0]==lam*(6*lam-1)/((1+2*lam)*(1+10*lam))
    s=sqrt(2)
    peak=(4*s-3)/46
    value=(3-2*s)/8
    assert 0<peak<1/6
    assert abs(float(h4_defect(F(577577,10000000)))-value)<1e-6
    # Any fixed lambda eventually violates monotonicity, tested well into bulk.
    # This numerical demonstration corroborates, but is not the infinite proof.
    try:
        import numpy as np
        for lam in [0.03,0.2,1.0,10.0]:
            n=300
            D=np.diff(np.eye(n),n=2,axis=0)
            A=np.eye(n)+lam*(D.T@D)
            y=np.arange(n)>=n//2
            z=np.linalg.solve(A,y.astype(float))
            assert np.min(np.diff(z)) < -1e-10,(lam,float(np.min(np.diff(z))))
    except ImportError:
        print('Optional large-grid numerical check omitted: NumPy unavailable')
    print('VERIFY_OK')
if __name__=='__main__':verify()
