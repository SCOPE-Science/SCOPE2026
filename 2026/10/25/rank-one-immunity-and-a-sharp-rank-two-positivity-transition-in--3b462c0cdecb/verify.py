"""Numerical reproduction of the positive-semidefinite truncation boundary.

Dependencies: Python 3, NumPy. Analytical claims are proved separately.
"""
import math
import numpy as np

count = 0

def check(condition, description):
    global count
    if not condition:
        raise AssertionError(description)
    count += 1

def close(a, b, description, rtol=2e-10, atol=2e-12):
    check(np.allclose(a, b, rtol=rtol, atol=atol), description)

def projected_step(Y, C, h, a):
    n = len(Y)
    eigenvalues, vecs = np.linalg.eigh(Y)
    rank = int(np.sum(eigenvalues > 1e-11))
    U = vecs[:, -rank:]
    P = U @ U.T
    tangent = P @ C + C @ P - P @ C @ P
    s = math.exp(-2*a*h)
    q = -math.expm1(-2*a*h)/(2*a) if a else h
    W = s*Y + q*tangent
    exact = s*Y + q*C
    return W, exact, rank, s, q

def signed_truncate(W, r):
    eigenvalues, V = np.linalg.eigh(W)
    ordered = np.argsort(-np.abs(eigenvalues))
    keep = ordered[:r]
    return (V[:,keep] * eigenvalues[keep]) @ V[:,keep].T

def formula(d, e, t):
    p = (d+t+math.sqrt((d+t)**2 + 4*t*t))/2
    b = (math.sqrt((d+t)**2 + 4*t*t)-(d+t))/2
    threshold = (e+math.sqrt(4*d*e+5*e*e))/2
    return p,b,threshold

for a in [0.0, 0.25, 1.0, 3.0]:
    for d in [0.1, 0.7, 1.0, 6.0]:
        for e in [0.002, 0.1, 0.4]:
            p, b, tcrit = formula(d,e,1.)
            hcrit = math.log1p(2*a*tcrit)/(2*a) if a else tcrit
            for factor in [0.2,0.5,0.85,1.15,1.5,2.]:
                h = factor*hcrit
                s = math.exp(-2*a*h)
                t = math.expm1(2*a*h)/(2*a) if a else h
                p,b,t_ = formula(d,e,t)
                Y = np.diag([d,e,0.])
                v = np.array([1.,0.,1.])
                C = np.outer(v,v)
                W, exact,rank,s,q=projected_step(Y,C,h,a)
                vals=np.linalg.eigvalsh(W)
                close(np.sort(vals),np.sort(np.array([-s*b,s*e,s*p])), 'full eigenvalues')
                close(np.linalg.eigvalsh(exact)[0] >= -1e-11, True, 'exact flow PSD')
                T=signed_truncate(W,rank)
                if factor<1:
                    check(np.linalg.eigvalsh(T)[0]>-1e-10,'safe rank two')
                    close(np.linalg.norm(W-T,'fro'),s*b,'safe residual')
                else:
                    close(np.linalg.eigvalsh(T)[0],-s*b,'indefinite rank two')
                    close(np.linalg.norm(W-T,'fro'),s*e,'indefinite residual')
                    # Closest PSD rank-at-most-two keeps positive eigenvalues.
                    evals,U=np.linalg.eigh(W)
                    closest=(U*np.maximum(evals,0.))@U.T
                    close(np.linalg.norm(W-closest,'fro'),s*b,'PSD repair residual')

# Rank-one immunity, including correlated positive sources and varying dimension.
rng=np.random.default_rng(2067)
for n in [2,3,5,9]:
    for a in [0.,0.3,2.]:
        for h in [0.005,0.4,1.2]:
            for _ in range(40):
                u=rng.normal(size=n);u/=np.linalg.norm(u)
                Y=(0.05+rng.uniform(0,2.))*np.outer(u,u)
                B=rng.normal(size=(n,n));C=B@B.T
                W, exact,rank, s,q=projected_step(Y,C,h,a)
                check(rank==1,'rank one input')
                T=signed_truncate(W,1)
                check(np.linalg.eigvalsh(T)[0]>-1e-9,'rank-one PSD')
                check(np.linalg.eigvalsh(exact)[0]>-1e-9,'rank-one exact PSD')

# Arbitrary-rank higher-dimensional embedding.
for r in [2,3,4,7]:
    n=r+2
    d=1.;e=0.05;a=1.;h=0.5
    Y=np.zeros((n,n));Y[0,0]=d;Y[1,1]=e
    for j in range(2,r):Y[j,j]=2.+j
    v=np.zeros(n);v[0]=v[r]=1.
    W, exact,rank,s,q=projected_step(Y,np.outer(v,v),h,a)
    check(rank==r,'embedded rank')
    T=signed_truncate(W,r)
    check(np.linalg.eigvalsh(T)[0]<-0.01,'embedded negative mode')
    check(np.linalg.eigvalsh(exact)[0]>-1e-10,'embedded exact PSD')

# Nonzero damping, exact rational intermediate at a specific step.
a=d=1.;e=0.1;h=math.log(3)/2
Y=np.diag([d,e,0.]);v=np.array([1.,0.,1.]);C=np.outer(v,v)
W,exact,rank,s,q=projected_step(Y,C,h,a)
close(s,1/3,'specific drift factor')
close(q,1/3,'specific forcing factor')
close(np.linalg.eigvalsh(signed_truncate(W,2))[0],-(math.sqrt(2)-1)/3,'specific negative eigenvalue')
close(exact,(Y+C)/3,'specific exact solution')
print(f'PASS: {count} deterministic checks')
