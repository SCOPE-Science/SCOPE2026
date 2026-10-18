"""Finite diagnostics for the one-edge-weighted four-cycle phase potential.

Run: python verify.py  (requires Python 3.9+ and numpy).
This checks examples, not the universal theorem, which is proved analytically.
"""
import itertools
import math
import numpy as np

TAU=2*math.pi
B=np.zeros((4,4))
for i in range(4):
    B[i,i]=1
    B[(i-1)%4,i]=-1
K=B.T @ B
WBASE=np.ones(4)
U=np.column_stack([np.eye(4)[:,j]-np.eye(4)[:,3] for j in range(3)])

def spectrum(t):
    w=np.array([t,1.,1.,1.])
    L=B@np.diag(w)@B.T
    observed=np.sort(np.linalg.eigvalsh(L))
    exact=np.sort([0., 2., t+2-math.sqrt((t-1)**2+1),t+2+math.sqrt((t-1)**2+1)])
    assert np.allclose(observed,exact,atol=1e-11)
    return exact[-1]

def roots(t):
    roots=[]
    for z in itertools.product([0.,math.pi],repeat=4):
        if (sum(abs(zj-math.pi)<1e-10 for zj in z))%2==0:
            roots.append(np.array(z))
    if t>1:
        c=math.sqrt((t-1)/(4*t))
        for a in [math.acos(c),-math.acos(c),math.acos(-c),-math.acos(-c)]:
            roots.append(np.array([-3*a,a,a,a]))
    return roots

def wrap(x):
    return (x+math.pi)%TAU-math.pi

def index(z,t):
    w=np.array([t,1.,1.,1.])
    H=U.T@np.diag(-w*np.cos(z))@U
    eigen=np.linalg.eigvalsh(H)
    assert np.min(np.abs(eigen))>1e-5, (t,z,eigen)
    return sum(eigen<0)

checks=0
for t in [1/4,1/2,3/4,9/10,11/10,5/4,2.,5.,12.]:
    lam=spectrum(t); checks+=4
    entries=roots(t)
    assert len(entries)==(8 if t<1 else 12)
    count=[0,0,0,0]
    for z in entries:
        assert abs(math.remainder(float(z.sum()),TAU))<5e-12
        flux=np.array([t,1.,1.,1.])*np.sin(z)
        assert np.max(abs(flux-flux[0]))<1e-11
        count[index(z,t)]+=1
        checks+=8
    assert count==([1,3,3,1] if t<1 else [1,5,5,1]),(t,count)
    h=1.9/lam
    zstar=np.ones(4)*math.pi
    # Critical antiphase sink and the largest multiplier bound.
    nonzero=np.linalg.eigvalsh(B@np.diag([t,1,1,1])@B.T)[1:]
    assert np.max(abs(1-h*nonzero))<1
    # Random direct checks of Lyapunov decrease for the quotient map.
    rng=np.random.default_rng(round(t*100000))
    for _ in range(120):
        z=rng.uniform(-math.pi,math.pi,3)
        z=np.append(z,-sum(z))
        w=np.array([t,1.,1.,1.])
        znext=z+h*K@(w*np.sin(z))
        before=float(np.dot(w,np.cos(z)))
        after=float(np.dot(w,np.cos(znext)))
        grad=B@(w*np.sin(z))
        major=before-h*(1-h*lam/2)*np.dot(grad,grad)
        assert after<=major+1e-11,(t,before,after,major)
        checks+=1
print('PASS:', checks, 'independent exact-formula, Hessian-inertia and descent diagnostics')
