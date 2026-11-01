"""Exact and numerical checks for two-distance-class weighted star leaf metrics.

Requires Python 3 standard library, scipy, and numpy. All exact quadratic
identities use Fraction arithmetic and integer exponents. Finite diagnostics
corroborate, but do not replace, the analytic all-parameter proof.
"""
from fractions import Fraction as F
import math
import random
import numpy as np
from scipy.optimize import brentq


def powered_matrix(m,n,a,b,p):
    d=[a]*m+[b]*n
    return [[F(0) if i==j else (d[i]+d[j])**p for j in range(m+n)] for i in range(m+n)]


def exact_check(m,n,a,b,p,vector):
    N=m+n
    assert sum(vector)==0
    D=powered_matrix(m,n,a,b,p)
    lhs=sum(vector[i]*vector[j]*D[i][j] for i in range(N) for j in range(N))
    s=sum(vector[:m]); A=(2*a)**p; B=(2*b)**p; C=(a+b)**p
    fluctuations_a=sum((z-F(s,m))**2 for z in vector[:m]);fluctuations_b=sum((z+F(s,n))**2 for z in vector[m:])
    margin=2*C-(1-F(1,m))*A-(1-F(1,n))*B
    rhs=-A*fluctuations_a-B*fluctuations_b-margin*s*s
    assert lhs==rhs,(m,n,a,b,p,lhs,rhs)


def threshold(m,n,a,b):
    if a==b: return math.inf
    q=(a-b)/(a+b)
    A=1-1/m;B=1-1/n
    def normalized(p):
        return A*math.exp(p*math.log1p(q))+B*math.exp(p*math.log1p(-q))-2
    hi=2.
    while normalized(hi)<0:hi*=2
    return brentq(normalized,1,hi,xtol=1e-12,rtol=1e-14)


def spectrum_check(m,n,a,b,p,kind):
    D=np.array([[0. if i==j else (a if i<m else b)+(a if j<m else b) for j in range(m+n)] for i in range(m+n)], dtype=float)
    D=np.power(D/np.max(D),p)
    N=m+n
    H=np.eye(N)-np.ones((N,N))/N
    B=-.5*H@D@H
    ev=np.linalg.eigvalsh(B)
    effective=np.delete(ev, np.argmin(np.abs(ev)))
    if kind=='strict':assert min(effective)>1e-8, (m,n,a,b,p,ev)
    if kind=='failure':assert min(effective)<-1e-8, (m,n,a,b,p,ev)
    if kind=='endpoint':assert abs(effective[0])<1e-7 and effective[1]>1e-8,(m,n,a,b,p,ev)


def main():
    random.seed(117)
    exact=0
    for m,n in [(2,2),(2,3),(3,4),(4,5)]:
      for a,b in [(F(1),F(1)),(F(3,2),F(2,1)),(F(5,3),F(3,4))]:
       for p in [0,1,2,3,4]:
        for _ in range(8):
         x=[F(random.randint(-5,5)) for j in range(m+n-1)]
         x.append(-sum(x));exact_check(m,n,a,b,p,x);exact+=1
    print('EXACT_DECOMPOSITION_OK',exact)
    samples=0
    for m,n in [(2,2),(2,5),(3,3),(3,6),(6,2)]:
     for a,b in [(1.,3.),(4.,1.),(.7,1.3),(1.,1.6)]:
      p=threshold(m,n,a,b)
      spectrum_check(m,n,a,b,p-.03,'strict')
      spectrum_check(m,n,a,b,p,'endpoint')
      spectrum_check(m,n,a,b,p+.03,'failure')
      samples+=1
    print('INERTIA_AND_ENDPOINT_RANK_OK',samples)
    for m,n in [(2,2),(2,5),(3,4),(7,2)]:
     vals=[threshold(m,n,1+eps,1) for eps in [.003,.006,.015,.03,.1,.5,2,20]]
     assert all(vals[i]>vals[i+1] for i in range(len(vals)-1)),(m,n,vals)
     vals2=[threshold(m,n,1,1+eps) for eps in [.003,.006,.015,.03,.1,.5,2,20]]
     assert all(vals2[i]>vals2[i+1] for i in range(len(vals2)-1)),(m,n,vals2)
    print('STRICT_ANISOTROPY_MONOTONICITY_OK')
    for m,n in [(2,3),(3,5),(9,2)]:
     A=1-1/m;B=1-1/n
     kpos=math.log((1+math.sqrt(1-A*B))/A)
     kneg=math.log((1+math.sqrt(1-A*B))/B)
     for eps in [1.e-3,1.e-4,1.e-5]:
      xp=threshold(m,n,1+eps,1)*math.log1p(eps)
      xm=threshold(m,n,1,1+eps)*math.log1p(eps)
      assert abs(xp-2*kpos)<.01 and abs(xm-2*kneg)<.01,(m,n,eps,xp,xm,2*kpos,2*kneg)
    print('ASYMMETRIC_SINGULAR_LIMIT_OK')
    for m,n in [(2,2),(2,3),(4,7)]:
     A=1-1/m;B=1-1/n
     S=A+B;D=A-B;K=2-S
     qm=(-D-math.sqrt(D*D+S*K))/S
     qp=(-D+math.sqrt(D*D+S*K))/S
     assert -1-1.e-12<=qm<0<qp<=1+1.e-12
     for q in [qm*.98,qp*.98]:assert A*(1+q)**2+B*(1-q)**2<2
     for q in [qm,qp]:assert abs(A*(1+q)**2+B*(1-q)**2-2)<1e-12
     if qp<.999:
      q=(qp+1)/2;assert A*(1+q)**2+B*(1-q)**2>2
     if qm>-.999:
      q=(qm-1)/2;assert A*(1+q)**2+B*(1-q)**2>2
    print('SHARP_EUCLIDEAN_WINDOW_OK')
    print('ALL_TWO_CLASS_LEAF_METRIC_CHECKS_OK')

if __name__=='__main__':main()
