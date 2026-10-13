"""Reconstruct and test the exact one-sample AdaLoss target-offset law."""
import math
import random

rng=random.Random(350078)

def one_step(z,b2,eigs,eta,alpha,baseline,target):
    gap=sum(.5*lam*v*v for lam,v in zip(eigs,z))
    b2n=b2+alpha*abs(baseline+gap-target)
    bn=math.sqrt(b2n)
    return [v*(1-eta*lam/bn) for v,lam in zip(z,eigs)],b2n

# Compare the native two-coordinate gradient update with an independent
# arbitrary orthogonal rotation into eigenvectors.
for _ in range(300):
    lam1=rng.uniform(.1,2)
    lam2=rng.uniform(2.1,5)
    ang=rng.uniform(-3,3)
    ca,sa=math.cos(ang),math.sin(ang)
    x=[rng.uniform(-.3,.3),rng.uniform(-.3,.3)]
    z=[ca*x[0]+sa*x[1],-sa*x[0]+ca*x[1]]
    eta=.3
    b2=3.0*3.0
    alpha=.7
    base=2.0
    target=rng.choice([1.5,2.0,2.5])
    if base<target:
        z=[v*.5 for v in z]
        x=[v*.5 for v in x]
    zn,b2n=one_step(z,b2,[lam1,lam2],eta,alpha,base,target)
    hx=[ca*lam1*z[0]-sa*lam2*z[1],sa*lam1*z[0]+ca*lam2*z[1]]
    bn=math.sqrt(b2n)
    xn=[x[j]-eta*hx[j]/bn for j in range(2)]
    rot=[ca*zn[0]-sa*zn[1],sa*zn[0]+ca*zn[1]]
    assert max(abs(a-b) for a,b in zip(xn,rot))<1e-12

# Logarithmic stable simulation retains modal information far below underflow.
eigs=[1.2,3.1]
eta=.25
alpha=.7
baseline=2.0
b0=2.3
z0=[.4,-.2]
gap0=sum(.5*lam*v*v for lam,v in zip(eigs,z0))
assert gap0<.5

for target in (1.5,2.0,2.5):
    b2=b0*b0
    logabs=[math.log(abs(v)) for v in z0]
    delta=abs(target-baseline)
    D=alpha*delta
    ref={}
    cumgap=0.0
    for t in range(1,100001):
        gap=sum(.5*lam*math.exp(2*lv) for lam,lv in zip(eigs,logabs))
        cumgap+=gap
        b2+=alpha*abs(baseline+gap-target)
        b=math.sqrt(b2)
        assert b>=b0
        for i,lam in enumerate(eigs):
            assert 0<eta*lam/b<1
            logabs[i]+=math.log1p(-eta*lam/b)
        if t in (25000,50000,100000):
            if delta:
                centered=[lv+2*eta*lam/math.sqrt(D)*math.sqrt(t)
                          +(eta*lam)**2/(2*D)*math.log(t)
                          for lv,lam in zip(logabs,eigs)]
                signed=1 if baseline>target else -1
                # Exact accumulator accounting, with no use of asymptotic theory.
                assert abs((b2-D*t)-(b0*b0+signed*alpha*cumgap))<3e-7
                ref[t]=centered
            else:
                ref[t]=(b,logabs[:])
    if delta:
        for i in range(2):
            # The centered profiles converge at the predicted inverse sqrt-time scale.
            assert abs(ref[100000][i]-ref[50000][i])<.1
            assert abs(ref[50000][i]-ref[25000][i])<.12
        assert abs(b2-D*100000-(b0*b0+(1 if baseline>target else -1)*alpha*cumgap))<3e-7
    else:
        bfin=math.sqrt(b2)
        assert bfin>b0
        for i,lam in enumerate(eigs):
            expected=math.log1p(-eta*lam/bfin)
            rate=(ref[100000][1][i]-ref[50000][1][i])/50000.0
            assert abs(rate-expected)<1e-6

print('verification passed')
