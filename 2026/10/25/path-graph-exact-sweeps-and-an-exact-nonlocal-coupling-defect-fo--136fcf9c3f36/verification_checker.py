"""Reproducibility checks for the one-pass coordinate-sketch RCGLS theorem.
Run with Python 3, numpy and sympy; no external input or online services.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp


def one_pass(H, error, order=None):
    """Source Algorithm 1 recurrence with S=e_i/sqrt(H_ii), on error=x*-x.
    Using S=e_i is equivalent here: line search is scale invariant.
    Generic nonzero branch only; return errors and normalized directions.
    """
    H=np.array(H,dtype=float); error=np.array(error,dtype=float)
    d=H.shape[0]; order=list(range(d)) if order is None else order
    old=np.zeros(d); dirs=[]; errors=[error.copy()]
    for j in order:
        g=H@error
        c=g[j]
        v=np.zeros(d); v[j]=c
        if np.dot(old,H@old)>0:
            v=v-(np.dot(v,H@old)/np.dot(old,H@old))*old
        if np.linalg.norm(v)==0:
            raise AssertionError('nongeneric branch')
        error=error-v*(np.dot(v,H@error)/np.dot(v,H@v))
        old=v
        dirs.append(v/c)
        errors.append(error.copy())
    return errors,dirs

a,b,c,d,e,f=sp.symbols('a b c d e f',real=True)
# 3x3 upper triangle H=[[a,b,c],[b,d,e],[c,e,f]].
H=sp.Matrix([[a,b,c],[b,d,e],[c,e,f]])
w0=sp.Matrix([1,0,0]); w1=sp.Matrix([-b/a,1,0]); D=sp.factor((w1.T*H*w1)[0]);
co=sp.factor((sp.Matrix([0,0,1]).T*H*w1)[0]/D)
w2=sp.Matrix([0,0,1])-co*w1
W=sp.factor((w2.T*H*w2)[0]);
assert sp.simplify((w2.T*H*w1)[0])==0
assert sp.simplify((w2.T*H*w0)[0]-c)==0
assert sp.simplify(D-(d-b*b/a))==0
assert sp.simplify(W-(f-(e-b*c/a)**2/(d-b*b/a)))==0
# Exact matrix example, failure for the order 1,2,3 and recovery 1,3,2.
J=sp.Matrix([[1,0,sp.Rational(9,10)],[0,1,0],[sp.Rational(9,10),0,1]])
X=sp.Matrix([1,1,1]); h=lambda x:sp.factor((x.T*J*x)[0]);
err=X
for i in range(3):
    g=J*err; raw=sp.eye(3)[:,i]*g[i]
    if i==0:p=raw
    else:p=raw-sp.factor((raw.T*J*p)[0]/h(p))*p
    assert p!=sp.zeros(3,1)
    err=sp.simplify(err-sp.factor((p.T*J*err)[0]/h(p))*p)
    if i==1: second=err
assert second==sp.Matrix([-sp.Rational(9,10),0,1])
assert err==sp.Matrix([-sp.Rational(9,10),0,sp.Rational(81,100)])
assert sp.simplify(h(err)/h(second)-sp.Rational(81,100))==0

rng=np.random.default_rng(17341)
for sample in range(2000):
    M=rng.normal(size=(3,3)); Hf=M.T@M+.2*np.eye(3)
    err0=rng.normal(size=3)
    errs,dirs=one_pass(Hf,err0)
    if np.linalg.norm(errs[2])<1e-10:
        continue
    w0=np.array([1.,0,0]);w1=np.array([-Hf[0,1]/Hf[0,0],1,0]);
    w2=np.array([0.,0,1.]);w2-=((w2@Hf@w1)/(w1@Hf@w1))*w1
    ratio=abs(Hf[0,2])/np.sqrt(Hf[0,0]*(w2@Hf@w2))
    measured=np.sqrt((errs[3]@Hf@errs[3])/(errs[2]@Hf@errs[2]))
    assert np.isclose(measured,ratio,atol=1e-9,rtol=1e-8),(sample,ratio,measured)
    assert all(np.isclose(np.dot(dirs[j],Hf@dirs[j-1]),0,atol=1e-9) for j in (1,2))

for dim in (3,4,5,7):
    for case in range(150):
        main=3+rng.random(dim)
        off=.3*rng.normal(size=dim-1)
        K=np.diag(main)+np.diag(off,k=1)+np.diag(off,k=-1)
        err=rng.normal(size=dim)
        errs,dirs=one_pass(K,err)
        assert np.linalg.norm(errs[-1])<=1e-10
        assert np.max(np.abs(np.array(dirs)@K@np.array(dirs).T - np.diag(np.diag(np.array(dirs)@K@np.array(dirs).T))))<1e-8
print('PASS: symbolic 3x3 identities, exact 9/10 witness, 2000 random 3x3 ratios, 600 path-matrix one-pass recoveries.')
