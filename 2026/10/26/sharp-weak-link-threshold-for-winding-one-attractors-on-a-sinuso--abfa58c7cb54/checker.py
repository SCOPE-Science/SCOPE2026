"""Numerical diagnostics for weak-edge winding-one phase locking.
Requires Python 3 and NumPy. Finite tests supplement the analytic argument.
"""
import math
import numpy as np

PI=math.pi

def root_bisect(fun,lo,hi,k=90):
    flo=fun(lo)
    fhi=fun(hi)
    assert flo*fhi<0
    for _ in range(k):
        mid=(lo+hi)/2
        if flo*fun(mid)>0:
            lo=mid;flo=fun(lo)
        else:
            hi=mid
    return (lo+hi)/2

def critical(n):
    m=n-1
    t=root_bisect(lambda z: math.tan(z)-m*math.tan((PI+z)/m), PI/(m-1)+1e-11, PI/2-1e-10)
    beta=PI-t
    return math.sin((PI+t)/m)/math.sin(t),beta

def weight_of_beta(beta,m):
    return math.sin((2*PI-beta)/m)/math.sin(beta)

def branches(n,w):
    m=n-1
    wc,beta=critical(n)
    if not w>wc: return None
    eps=1e-7
    b1=root_bisect(lambda b:weight_of_beta(b,m)-w,eps,beta)
    b2=root_bisect(lambda b:weight_of_beta(b,m)-w,beta,PI-eps)
    return b1,b2

def phase_hessian(n,w,beta):
    m=n-1;alpha=(2*PI-beta)/m
    diffs=np.array([alpha]*m+[beta]);weights=np.array([1.]*m+[w]);theta=np.zeros(n)
    for j in range(m): theta[j+1]=theta[j]+alpha
    # Incidence edge e=j -> j+1 mod n
    B=np.zeros((n,n))
    for j in range(n):B[j,j]=-1;B[(j+1)%n,j]=1
    flux=weights*np.sin(diffs)
    gradient=B@flux
    H=B@np.diag(weights*np.cos(diffs))@B.T
    eigs=np.linalg.eigvalsh(H)
    assert min(abs(eigs))<1e-12
    assert max(abs(gradient))<1e-11
    return np.delete(eigs,np.argmin(abs(eigs)))

for n in [5,6,7,8,10,20,50,100]:
    wcrit,beta=critical(n);m=n-1
    assert 0<wcrit<1
    w=(1+wcrit)/2
    beta1,beta2=branches(n,w)
    ev1=phase_hessian(n,w,beta1)
    ev2=phase_hessian(n,w,beta2)
    assert min(ev1)>1e-6
    assert sum(v<-1e-8 for v in ev2)==1
    assert max(abs(weight_of_beta(b,m)-w) for b in (beta1,beta2))<1e-9
    print(f'n={n} w_c={wcrit:.12f} beta_c={beta:.12f} w={w:.12f} b_attract={beta1:.12f} b_saddle={beta2:.12f} attract_min_eig={min(ev1):.6g} saddle_min_eig={min(ev2):.6g}')

tstar=root_bisect(lambda t: math.tan(t)-(PI+t),1,PI/2-1e-10)
C=1/math.cos(tstar)
for m in [10,30,100,300,1000]:
    w,_=critical(m+1)
    approx=C/m-C*(PI+tstar)**2/(6*m**3)
    print(f'm={m} critical={w:.12g} three_term={approx:.12g} scaled_error={m**5*(w-approx):.8g}')
print('WEAK_EDGE_THRESHOLD_AND_STABILITY_DIAGNOSTICS_PASS')
