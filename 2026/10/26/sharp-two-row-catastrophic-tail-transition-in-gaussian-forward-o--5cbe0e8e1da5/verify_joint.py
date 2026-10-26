"""Checks for two-row simultaneous catastrophic error in Gaussian forward-only least squares.
Use python verify_joint.py. NumPy/SciPy required. Finite diagnostics not universal proofs.
"""
import math
import numpy as np
from scipy.stats import f as f_dist
from scipy.special import betainc
rng=np.random.default_rng(20261024)
checks=0

def approx(x,y,rtol=1e-10,atol=1e-12):
    global checks
    assert abs(x-y) <= atol+rtol*abs(y),(x,y)
    checks+=1

def constants(q):
    single=math.gamma((q+1)/2)/(math.sqrt(math.pi)*math.gamma(q/2+1))
    joint=4*math.gamma((q+1)/2)**2*math.gamma(3*q/2)/(math.pi*math.gamma(q+1)**2*math.gamma(q/2))
    return single,joint

for q in (3,4,5,6):
    C,K=constants(q)
    assert C>0 and K>C*C
    checks+=1
    # Identity between the single-row tail formula and the F distribution.
    for t in (.01, .1, 1, 10):
        approx(f_dist.sf(q*t,1,q),betainc(q/2,.5,1/(1+t)))

# Independently compute both row reconstruction coefficient errors from Algorithm 1.
for q in (3,5,8):
    for rho in (-1.,-.7,0.,.4,.95,1.):
        n=3
        v1=np.array([1.,0.,0.]);v2=np.array([rho,np.sqrt(max(0,1-rho*rho)),0.]);w=np.array([0.,0.,1.])
        A=np.vstack([w+.7*v1,w-1.1*v2])
        for j in range(65):
            G=rng.normal(size=(n,q));Z=A@G
            g1=v1@G;g2=v2@G
            coef1=np.linalg.lstsq(g1[:,None],Z[0],rcond=None)[0][0]
            coef2=np.linalg.lstsq(g2[:,None],Z[1],rcond=None)[0][0]
            e1=(w@G@g1)/(g1@g1);e2=(w@G@g2)/(g2@g2)
            approx(coef1-.7,e1)
            approx(coef2+1.1,e2)
            if abs(rho)==1:approx(e1*e1,e2*e2)

# Importance-sampling Gaussian small-ball integral, checking sharp simultaneous-tail constant.
# Sample the scaled Gaussian sketch vectors u_i from radius-R balls, R=||g0||.
q=3
N=450000
g0=rng.normal(size=(N,q));R=np.linalg.norm(g0,axis=1)
uis=[]
for i in range(2):
    u=rng.normal(size=(N,q));u/=np.linalg.norm(u,axis=1)[:,None]
    u*= (R*rng.random(N)**(1/q))[:,None]
    uis.append(u)
u1,u2=uis
active=((np.sum(g0*u1,axis=1)**2 > np.sum(u1*u1,axis=1)**2)&
        (np.sum(g0*u2,axis=1)**2 > np.sum(u2*u2,axis=1)**2))
ballvol=(4*math.pi/3)*R**3
single,K=constants(q)
for rho in (0,.5,.85):
    determinant=1-rho*rho
    quad=(np.sum(u1*u1,axis=1)+np.sum(u2*u2,axis=1)-2*rho*np.sum(u1*u2,axis=1))/determinant
    normalization=(2*math.pi)**(-q)*determinant**(-q/2)
    for t in (1000.,10000.):
        weighted=active*normalization*np.exp(-quad/(2*t))*ballvol**2
        estimate=weighted.mean()
        analytic=K*determinant**(-q/2)
        # Importance integral estimates t^q P(Y1>t,Y2>t), with finite-t bias.
        assert abs(estimate/analytic-1)<.12,(rho,t,estimate,analytic)
        checks+=1
        print(f'angle corr={rho:.2f}, t={t:.0f}: t^q P(both exceed t) estimated {estimate:.6f}, limiting {analytic:.6f}')

# Single row: P(Y>t)=P(F_{1,q}>q*t), independent of correlation.
for t in (10.,1e3,1e5):
    single=constants(q)[0]
    approx(f_dist.sf(q*t,1,q)*t**(q/2)/single, 1.,rtol=.12)

print('PASS:',checks,'independent deterministic/numerical checks. Importance sampling N=',N)
