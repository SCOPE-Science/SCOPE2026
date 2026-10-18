"""Reproduce exact rank-split cosine law and Chebyshev CG obstruction.
No external datasets are required. SciPy, NumPy, and mpmath are used.
"""
import numpy as np
from scipy.special import betainc
from scipy.stats import beta
import mpmath as mp

rng=np.random.default_rng(20261015)
checks=0

def cosine(K,t):
    return (1+(K-1)*t)/np.sqrt(1+(K*K-1)*t)

def cdf_loss(n,r,s,K,ell):
    mn=1-2*np.sqrt(K)/(K+1)
    if ell<=0:return 0.0
    if ell>=mn:return 1.0
    u=1-ell
    disc=u*u*(K+1)*(K+1)-4*K
    low=(u*u*(K+1)-2-u*np.sqrt(max(disc,0)))/(2*(K-1))
    high=(u*u*(K+1)-2+u*np.sqrt(max(disc,0)))/(2*(K-1))
    return float(betainc(r*s/2,(n-r)*s/2,max(0,low))+1-betainc(r*s/2,(n-r)*s/2,min(1,high)))

for n in (3,4,12,80):
    for r in (1,max(1,n//3),n-1):
        for s in (1,2,9):
            for K in (1.5,3,12):
                t=rng.beta(r*s/2,(n-r)*s/2,5000)
                loss=1-cosine(K,t)
                assert min(loss)>-1e-12 and max(loss)<=1-2*np.sqrt(K)/(K+1)+1e-12
                for ell in np.linspace(.00001, 1-2*np.sqrt(K)/(K+1)-.00001,7):
                    if ell<=0:continue
                    true=cdf_loss(n,r,s,K,ell)
                    empirical=np.mean(loss<=ell)
                    assert abs(true-empirical)<.07,(n,r,s,K,ell,true,empirical)
                    checks+=1

for n,r,K in ((30,1,12),(400,3,35),(2000,10,15)):
    for s in (1,4,32):
        Z=rng.standard_normal((n,s))
        BZ=Z.copy();BZ[:r]*=K
        direct=1-(Z*BZ).sum()/(np.linalg.norm(Z)*np.linalg.norm(BZ))
        t=(Z[:r]*Z[:r]).sum()/(Z*Z).sum()
        assert abs(direct-(1-cosine(K,t)))<1e-12
        checks+=1

for k in range(2,15):
    K=1+1.0*k*k
    lam=(K+1)/2+(K-1)/2*np.cos(np.arange(k+1)*np.pi/k)
    cj=np.ones(k+1);cj[0]=cj[-1]=.5
    w=(cj/lam);w=w/w.sum()
    a=(K+1)/(K-1)
    D=1/np.cosh(k*np.arccosh(a))
    p=(-1.)**(np.arange(k+1)+k)*D
    for j in range(k):
        cross=np.dot(w,lam**(j+1)*p)
        assert abs(cross)<max(1e-8,1e-8*max(abs(w*lam**(j+1))))
        checks+=1
    assert abs(np.dot(w,p*p)-D*D)<1e-13
    checks+=1

for k in (3,5,9,15):
    mp.mp.dps=85
    K=mp.mpf(k)**4
    lam=[(K+1)/2+(K-1)/2*mp.cos(j*mp.pi/k) for j in range(k+1)]
    cj=[mp.mpf('0.5') if j in (0,k) else mp.mpf(1) for j in range(k+1)]
    w=[cj[j]/lam[j] for j in range(k+1)]
    w=[v/sum(w) for v in w]
    D=1/mp.cosh(k*mp.acosh((K+1)/(K-1)))
    p=[(-1)**(j+k)*D for j in range(k+1)]
    for a in range(1,k+1):
        cross=sum(w[j]*p[j]*lam[j]**a for j in range(k+1))
        assert abs(cross)<mp.mpf('1e-40')*max(1,max(abs(w[j]*lam[j]**a) for j in range(k+1)))
        checks+=1
    assert abs(sum(w[j]*p[j]**2 for j in range(k+1))-D*D)<mp.mpf('1e-60')
    checks+=1



# Direct energy-norm CG on the weighted Chebyshev design.
for k in range(2,9):
    K=float(k*k+2)
    lam=(K+1)/2+(K-1)/2*np.cos(np.arange(k+1)*np.pi/k)
    cj=np.ones(k+1);cj[[0,-1]]=0.5
    w=(cj/lam);w=w/w.sum()
    target=np.sqrt(w/lam)
    b=lam*target
    x=np.zeros(k+1)
    r=b.copy();direction=r.copy();rs=float(r@r)
    for it in range(k):
        Ap=lam*direction
        alpha=rs/float(direction@Ap)
        x+=alpha*direction
        r-=alpha*Ap
        rs2=float(r@r)
        direction=r+(rs2/rs)*direction
        rs=rs2
    rel=np.sqrt(np.sum(lam*(x-target)**2)/np.sum(lam*target**2))
    delta=1/np.cosh(k*np.arccosh((K+1)/(K-1)))
    assert abs(rel-delta)<2e-6,(k,rel,delta)
    checks+=1

# On a diagonal positive-definite operator, Jacobi smoothing is scalar.
for n in (6,19,128):
    K=9.0
    A=np.diag([K]+[1.]*(n-1))
    DinvA=np.diag(1/np.diag(A))@A
    probe=rng.standard_normal((n,3))
    smooth=probe-0.6*DinvA@probe
    smooth=smooth-0.6*DinvA@smooth
    assert np.allclose(smooth,0.16*probe,atol=1e-14)
    raw=1-np.sum(probe*(A@probe))/(np.linalg.norm(probe)*np.linalg.norm(A@probe))
    post=1-np.sum(smooth*(A@smooth))/(np.linalg.norm(smooth)*np.linalg.norm(A@smooth))
    assert abs(raw-post)<1e-14
    checks+=2

for k in (2,3,4,6,10,25,100):
    K=float(k)**4
    N=float(k)**10
    upper=k*(K-1)**2/N
    delta=1/np.cosh(k*np.arccosh((K+1)/(K-1)))
    assert upper<=1/k*(1+1e-12)
    assert 0<delta<1
    print(f'k={k}, N=k^10, K=k^4, mean-loss-upper={upper:.5g}, worst-CG-relative-A-error-after-k={delta:.9f}')
    checks+=1

print('Passed checks:',checks)
