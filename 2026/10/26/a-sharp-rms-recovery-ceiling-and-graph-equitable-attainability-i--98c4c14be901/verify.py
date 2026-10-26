"""Independent finite checks for a logistic-network spectral bound.

Requires Python 3, NumPy and SciPy; the written proof establishes all infinite claims.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt
import numpy as np
from scipy.optimize import root, least_squares, minimize_scalar

checks=0

def check(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks+=1

# Exact algebra in mean-field networks for distinct pairs of growth rates.
for aa,bb in product(range(1,7),repeat=2):
    if aa==bb:
        continue
    for n in range(2,9):
        for k in range(1,n):
            a,b=Q(aa),Q(bb)
            r=[a]*k+[b]*(n-k)
            mean=sum(r,Q(0))/n
            q2=sum((z*z for z in r),Q(0))/n
            d=(a+b)/2
            for ri in r:
                check(ri*ri-q2==2*d*(ri-mean), "mean-field equality identity")
            check(q2>=mean*mean, "RMS mean comparison")

# Exact equitable partition test on a noncomplete connected weighted graph:
# four-node path, groups (a,b,b,a) have two distinct cross degrees;
# balanced four-cycle grouping (a,a,b,b) has equal cross degrees.
a,b=Q(1),Q(4)
r=[a,a,b,b]
L=[[Q(0) for j in range(4)] for i in range(4)]
for i,j,w in [(0,1,Q(2)),(1,2,Q(3)),(2,3,Q(2)),(3,0,Q(3))]:
    L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
m=sum(r,Q(0))/4
z=[ri-m for ri in r]
Lz=[sum(L[i][j]*z[j] for j in range(4)) for i in range(4)]
lam=Q(6)
for lhs,rhs in zip(Lz,z):
    check(lhs==lam*rhs, "exact equitable eigenvector")
d=(a+b)/(2*lam)
q2=sum((ri*ri for ri in r),Q(0))/4
for i in range(4):
    check(r[i]**2-q2==2*d*sum(L[i][j]*r[j] for j in range(4)), "exact graph attainability")

# Randomly selected finite systems: solve positive equilibria and verify the
# bound/equality tolerance. Numerical tests are corroboration, never proof.
rng=np.random.default_rng(43176)
for n in (2,3,4,6):
    for trial in range(8):
        rates=rng.uniform(0.5,4.0,size=n)
        w=rng.uniform(0.15,1.5,size=(n,n))
        w=(w+w.T)/2
        np.fill_diagonal(w,0.0)
        L=np.diag(w.sum(axis=1))-w
        q=sqrt(np.mean(rates**2))
        for coupling in (0.0,0.04,0.4,2.5,17.0,100.0):
            fun=lambda x: rates*x-x*x-coupling*(L@x)
            solution=least_squares(fun,np.full(n,float(np.mean(rates))),bounds=(np.min(rates)*0.99,np.max(rates)*1.01),xtol=1e-13,ftol=1e-13,gtol=1e-13)
            check(solution.success and np.linalg.norm(fun(solution.x))<1e-7, "numeric equilibrium")
            x=solution.x
            check(np.all(x>0), "positive equilibrium")
            J=np.diag(rates-2*x)-coupling*L
            alpha=-np.linalg.eigvalsh(J)[-1]
            v=np.arange(1,n+1,dtype=float)/(n+1)
            zv=v/x
            diff=zv[:,None]-zv[None,:]
            qform=-np.sum(x*v*v)-coupling*0.5*np.sum(w*(x[:,None]*x[None,:])*(diff*diff))
            check(abs(v@J@v-qform)<1e-9*(1+abs(qform)), "equilibrium Hessian energy certificate")
            check(alpha>0 and alpha<=q+1e-8, "strict stability and RMS ceiling")
            check(abs(np.sum(x*x-rates*x))<1e-7, "conservative equilibrium identity")

# Full three-patch example and three-class strict gap check.
rates=np.array([1.,1.,4.]); n=3
L=np.eye(n)-np.ones((n,n))/n
q=sqrt(np.mean(rates**2)); d=2.5
x=(rates+q)/2
check(np.linalg.norm(rates*x-x*x-d*(L@x))<1e-12, "sharp exact-family equilibrium")
J=np.diag(rates-2*x)-d*L
check(abs(-np.linalg.eigvalsh(J)[-1]-q)<1e-12, "sharp example spectral rate")

rates=np.array([1.,2.,4.]);q=sqrt(np.mean(rates**2))
def alpha_at(d):
    f=lambda x: rates*x-x*x-d*(L@x)
    z=least_squares(f,np.full(3,2.4),bounds=(0.99,4.01),xtol=1e-13,ftol=1e-13,gtol=1e-13)
    check(z.success and np.linalg.norm(f(z.x))<1e-8, "three-level root")
    return -np.linalg.eigvalsh(np.diag(rates-2*z.x)-d*L)[-1]
res=minimize_scalar(lambda z:-alpha_at(z),bounds=(0,25),method='bounded',options={'xatol':1e-9})
check(res.success and -res.fun<q-1e-4, "three-level strict numerical gap")
print(f"PASS: {checks} independent rational and numerical assertions")
