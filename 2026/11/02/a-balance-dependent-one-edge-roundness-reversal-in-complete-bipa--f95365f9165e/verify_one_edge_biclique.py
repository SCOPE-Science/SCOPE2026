"""Reproducible exact and numerical checks for one-edge-deformed biclique metrics.

Run: python verify_one_edge_biclique.py. Requires numpy and mpmath.
"""
from fractions import Fraction as Fr
import random
import math
import numpy as np
import mpmath as mp


def f_polynomial(m, n, a, h):
    T = 2*m*n-m-n
    C = 2*(m-1)*(n-1)-a*(2*m*n-3*m-3*n+4)
    return a*a*(a*T-2*m*n-2*h)+C*h*h


def matrix_3(m, n, a, h):
    # Scalar coordinates: total mass in first part, special A fluctuation,
    # special B fluctuation. This is the positive quadratic form -alpha^T D alpha.
    return [[a*(Fr(1,m)+Fr(1,n))-2*(a-1)+Fr(2, m*n)*h, Fr(1,n)*h, -Fr(1,m)*h],
            [Fr(1,n)*h, a*Fr(m,m-1), -h],
            [-Fr(1,m)*h, -h, a*Fr(n,n-1)]]


def determinant_3(X):
    (a,b,c),(d,e,f),(g,h,i)=X
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def direct_energy(m, n, s, p, alpha):
    z=Fr(0)
    for i in range(m+n):
        for j in range(i):
            if (i<m)==(j<m): delta=Fr(2)
            else: delta=s if {i,j}=={0,m} else Fr(1)
            z+=2*alpha[i]*alpha[j]*delta**p
    return z


def matrix_energy(m,n,s,p,alpha):
    a=Fr(2)**p;h=s**p-1
    r=sum(alpha[:m]); x0=alpha[0]; y0=alpha[m]
    u=x0-Fr(r,m); v=y0+Fr(r,n)
    X=matrix_3(m,n,a,h)
    t=[r,u,v]
    e=sum(X[i][j]*t[i]*t[j] for i in range(3) for j in range(3))
    e+=a*(sum((z-Fr(r-x0,m-1))**2 for z in alpha[1:m])
          +sum((z-Fr(-r-y0,n-1))**2 for z in alpha[m+1:]))
    return e


def full_distance(m,n,s,p):
    N=m+n
    D=np.ones((N,N),float)
    np.fill_diagonal(D,0.)
    D[:m,:m]=(2.**p)*(np.ones((m,m))-np.eye(m))
    D[m:,m:]=(2.**p)*(np.ones((n,n))-np.eye(n))
    D[0,m]=D[m,0]=s**p
    return D


def max_conditional_eigen(m,n,s,p):
    N=m+n
    V=np.eye(N)[:,:-1]-np.eye(N)[:,[-1]]
    eig=np.linalg.eigvalsh(V.T@full_distance(m,n,s,p)@V)
    return eig[-1],eig


def critical(m,n,s,dps=70):
    mp.mp.dps=dps
    if m==n==2:
        fn=lambda p: (mp.power(2,p)-1)**2-mp.power(s,p)
        lo=mp.mpf('0.9');hi=mp.mpf('2.1')
    else:
        fn=lambda p: f_polynomial(m,n,mp.power(2,p),mp.power(s,p)-1)
        lo=mp.mpf('0.0000001');hi=mp.mpf('1.0000001')
    for _ in range(240):
        mid=(lo+hi)/2
        if fn(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def run():
    R=random.Random(202611)
    exact=0
    for m in range(2,8):
        for n in range(m,9):
            for p in (1,2):
                for s in (Fr(1),Fr(3,2),Fr(2),Fr(3)):
                    a=Fr(2)**p;h=s**p-1
                    X=matrix_3(m,n,a,h)
                    assert determinant_3(X)==-f_polynomial(m,n,a,h)/Fr((m-1)*(n-1))
                    exact+=1
                    for _ in range(10):
                        alpha=[Fr(R.randint(-5,5)) for _ in range(m+n-1)]
                        alpha.append(-sum(alpha))
                        assert -direct_energy(m,n,s,p,alpha)==matrix_energy(m,n,s,p,alpha)
                        exact+=1
    print('EXACT_FORM_AND_DETERMINANT_IDENTITIES_OK',exact)
    numerical=0
    for m in range(2,7):
        for n in range(m,9):
            for s in (1.,1.4,2.,2.65,3.):
                p=float(critical(m,n,s))
                for q in (max(p*0.82,1e-6),p,p+0.07):
                    val,eigs=max_conditional_eigen(m,n,s,q)
                    if q<p-1e-7: assert val<-1e-6,(m,n,s,q,p,val)
                    if q>p+1e-7: assert val>1e-6,(m,n,s,q,p,val)
                    if abs(q-p)<1e-8: assert abs(val)<1e-6,(m,n,s,q,p,val)
                    numerical+=1
    print('FULL_MATRIX_CRITICAL_SPECTRA_OK',numerical)
    p0=mp.log(mp.mpf(16)/11,2)
    H=Fr(256,319)
    assert 16**13>2**7*11**13
    assert 3**7*319**13>575**13
    assert mp.power(3,p0)-1>mp.mpf(H.numerator)/H.denominator
    p3=critical(2,8,3.)
    assert p3<p0
    assert abs(float(p3)-0.539792024119)<1e-9
    print('EXACT_UNBALANCED_REVERSAL_CERTIFICATE_OK', 'K_2,8')
    assert abs(float(critical(2,2,3))-2)<1e-12
    assert abs(float(critical(2,3,3))-1)<1e-12
    print('FOUR_AND_FIVE_POINT_ENDPOINTS_OK')
    for k in (2,3,4,8,16):
        p0=mp.log(mp.mpf(k)/(k-1),2)
        for s in (1.2,2.,3.):
            assert critical(k,k,s)>p0
    print('BALANCED_STRICT_IMPROVEMENT_OK')
    c=mp.log(mp.mpf('2.5'))/mp.log(2)**2
    for k in (64,128,256,512,1024):
        p=critical(k,k,mp.mpf('2.5'),dps=85)
        p0=mp.log(mp.mpf(k)/(k-1),2)
        scaled=k**3*(p-p0)
        if k>=512: assert abs(float(scaled-c))<0.002
    print('BALANCED_INVERSE_CUBIC_SENSITIVITY_OK',mp.nstr(c,15))
    for m in (2,3,4,6):
        pi=mp.log(mp.mpf(2*m)/(2*m-1),2)
        n=100000
        T=2*m*n-m-n
        H=mp.mpf(4*m*m*n*n)/(T*(m*m-m+n*n-n))
        sreturn=mp.power(1+H,1/mp.log(mp.mpf(2*m*n)/T,2))
        lim=mp.mpf(4*m*m)/((2*m-1)*pi)
        assert abs(float(n*(sreturn-1)-lim))<.08
    print('FIXED_SMALL_PART_CROSSOVER_ASYMPTOTIC_OK')
    print('ALL_ONE_EDGE_BICLIQUE_NEGATIVE_TYPE_CHECKS_OK')

if __name__=='__main__':run()
