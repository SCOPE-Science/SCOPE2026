"""Reproducible checks for the Gaussian sketched-harmonic sign frontier.
Only finite diagnostic calculations; proof is contained in RESULT.md.
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.special import betainc

rng = np.random.default_rng(17032026)
tests=0

def check(cond, msg):
    global tests
    if not cond:
        raise AssertionError(msg)
    tests+=1

# Algebraic 2x2 determinant, equivalent sample-correlation criterion.
for j in range(1500):
    a=float(np.exp(rng.uniform(-3,3)))
    b=float(a*np.exp(rng.uniform(.01,5)))
    G=rng.standard_normal((rng.integers(2,20),2))
    W=G.T@G
    A=np.diag([a,b]); H=(A@W+W@A)/2
    rho=2*math.sqrt(a*b)/(a+b)
    c=W[0,1]/math.sqrt(W[0,0]*W[1,1])
    check((np.linalg.eigvalsh(H)[0]<0)==(abs(c)>rho), 'correlation/sign criterion')
    check(abs(np.linalg.det(H) -(a*b*W[0,0]*W[1,1] - ((a+b)**2/4)*W[0,1]**2)) < 1e-7*max(1.,abs(np.linalg.det(H))), 'determinant formula')

# Sharp deterministic boundary; constructive SPD W reaching negative denominator.
for j in range(600):
    k=float(np.exp(rng.uniform(.001,8)))
    a,b=1.,k
    v=np.array([math.sqrt(b/(a+b)), math.sqrt(a/(a+b))])
    Av=np.array([a*v[0],b*v[1]])
    rho=2*math.sqrt(a*b)/(a+b)
    check(abs(np.dot(v,Av)/(np.linalg.norm(v)*np.linalg.norm(Av))-rho)<2e-14,'Kantorovich optimizer')
    x=Av/np.linalg.norm(Av)
    d=v-x;d=d/np.linalg.norm(d)
    U=np.eye(2)-2*np.outer(d,d)
    check(np.linalg.norm(U@v-x)<1e-11,'Householder')
    eps=(rho+1.)/2
    W=np.eye(2)-eps*U
    check(np.linalg.eigvalsh(W)[0]>0 and np.dot(Av,W@v)<-1e-15,'sharp failure')
    W0=np.eye(2)-rho*U
    check(abs(np.dot(Av,W0@v))<2e-13*np.linalg.norm(Av),'boundary zero')

# Formula for Gaussian risk of uniform sign failure at preselected condition numbers.
# Sampling all Gaussian sketches simultaneously gives reproducible binomial intervals.
for k,s,N in [(4.,2,60000),(9.,3,60000),(16.,5,60000),(25.,8,60000)]:
    R=rng.standard_normal((N,s,2))
    c=(R[:,:,0]*R[:,:,1]).sum(axis=1)/np.linalg.norm(R[:,:,0],axis=1)/np.linalg.norm(R[:,:,1],axis=1)
    rho=2*math.sqrt(k)/(k+1)
    estimate=np.mean(np.abs(c)>rho)
    expected=betainc((s-1)/2,0.5,1-rho*rho)
    check(abs(estimate-expected)<7*math.sqrt(max(expected*(1-expected),.01)/N),'uniform Gaussian risk CDF')

# Pointwise maximum over fixed v. The worst v weights eigenvalues inversely.
for k,s,N in [(4.,2,60000),(9.,3,60000),(16.,5,60000),(25.,8,60000)]:
    R=rng.standard_normal((N,s,2))
    v=np.array([math.sqrt(k/(1+k)),math.sqrt(1/(1+k))]); Av=np.array([v[0],k*v[1]])
    score=np.einsum('ns,ns->n',R@v,R@Av)
    estimate=np.mean(score<0)
    rho=2*math.sqrt(k)/(k+1)
    expected=betainc(s/2,s/2,(1-rho)/2)
    check(abs(estimate-expected)<7*math.sqrt(max(expected*(1-expected),.01)/N),'fixed Gaussian risk CDF')
    check(expected < betainc((s-1)/2,0.5,1-rho*rho),'uniform dominates fixed')

# Uniform strict positivity under controlled embedding distortion.
for j in range(200):
    k=float(np.exp(rng.uniform(.1,6)))
    A=np.diag([1.,k]); rho=2*math.sqrt(k)/(k+1)
    Q=np.linalg.qr(rng.standard_normal((2,2)))[0]
    eig=1.+rng.uniform(-.9*rho,.9*rho,size=2)
    W=Q@np.diag(eig)@Q.T
    check(np.linalg.eigvalsh((A@W+W@A)/2)[0]>0,'safe distortion')

print('PASS',tests,'deterministic checks; 480000 simulated sketch samples')
for s in (2,3,4,5,8,12):
    k=9.;rho=2*math.sqrt(k)/(k+1)
    print('s',s,'uniform',betainc((s-1)/2,.5,1-rho*rho),'worst_fixed',betainc(s/2,s/2,(1-rho)/2))
