"""Standalone numerical checks for Gaussian generalized Nystrom leave-out laws.

Run: python verify.py
Requirements: numpy, scipy. These finite checks are not proofs of tail/moment claims.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

rng=np.random.default_rng(20261017)
checks=0
max_residual=0.0

def check(a,b,tol=1e-8):
    global checks,max_residual
    delta=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    checks+=1
    max_residual=max(max_residual,delta)
    if not np.isfinite(delta) or delta>tol:
        raise AssertionError((a,b,delta))

def gn(y,phi):
    # Identity input: Omega=Y and Phi is the independent left sketch.
    return y@np.linalg.pinv(phi.T@y, rcond=1e-13)@phi.T

for n in (2,3,4):
  for r in (n,n+1,n+3):
    for trial in range(85):
      omega=rng.standard_normal((n,n))
      phi=rng.standard_normal((n,r))
      check(gn(omega,phi),np.eye(n),2e-7)
      h=phi.T@omega
      hth_inverse=np.linalg.inv(h.T@h)
      fast_total=0.0
      brute_total=0.0
      for j in range(n):
        y=np.delete(omega,j,axis=1)
        residual=omega[:,j]-gn(y,phi)@omega[:,j]
        direct=float(residual@residual)
        coeff=hth_inverse[:,j]/hth_inverse[j,j]
        fast=float((omega@coeff)@(omega@coeff))
        check(direct,fast,2e-7)
        brute_total+=direct
        fast_total+=fast
        # Independent orthogonal-coordinate decomposition (no use of the fast formula).
        u,_=np.linalg.qr(y,mode='reduced')
        v=np.linalg.svd(y.T)[2][-1,:]
        g=phi.T@u
        z=phi.T@v
        x=np.linalg.lstsq(g,z,rcond=None)[0]
        val=float((omega[:,j]@v)**2*(1+x@x))
        check(direct,val,2e-7)
      check(brute_total/n,fast_total/n,2e-7)
      if r==n:
        core=phi.T@omega
        inv=np.linalg.inv(core)
        lp=0.0
        lt=0.0
        for j in range(n):
          for ell in range(n):
            y=np.delete(omega,j,axis=1)
            f=np.delete(phi,ell,axis=1)
            resid=omega[:,j]-gn(y,f)@omega[:,j]
            measured=float(phi[:,ell]@resid)
            rapid=1.0/inv[j,ell]
            check(measured,rapid,4e-7)
            lp+=measured**2
            if ell==j:lt+=measured**2
            # Independently build the two orthogonal normals and check the rank-one residual.
            a=np.linalg.svd(f.T)[2][-1,:]
            b=np.linalg.svd(y.T)[2][-1,:]
            if abs(a@b)>1e-6:
              alt=float((phi[:,ell]@a)*(b@omega[:,j])/(a@b))
              check(measured,alt,4e-7)
        check(lp/n**2,sum((1/inv[j,l])**2 for j in range(n) for l in range(n))/n**2,3e-7)
        check(lt/n,sum((1/inv[j,j])**2 for j in range(n))/n,3e-7)


# Non-square right sketches: the same chi-square ratio geometry holds with
# codimension d=n-s+1. Check leave-one-right-out identities without ever
# forming a full-rank identity reconstruction.
for ambient in (3,4,6):
  for samples in range(2,ambient+1):
    k=samples-1
    for leftcols in (samples,samples+1,samples+3):
      for trial in range(37):
        omega=rng.standard_normal((ambient,samples))
        phi=rng.standard_normal((ambient,leftcols))
        total=0.
        for j in range(samples):
          y=np.delete(omega,j,axis=1)
          test=omega[:,j]
          resid=test-gn(y,phi)@test
          direct=float(resid@resid)
          u,_=np.linalg.qr(y,mode='reduced')
          qfull=np.linalg.svd(u.T,full_matrices=True)[2].T
          v=qfull[:,k:]
          g=phi.T@u
          h=phi.T@v
          z=v.T@test
          x=np.linalg.lstsq(g,h@z,rcond=None)[0]
          check(direct,float(z@z+x@x),3e-7)
          total+=direct
        check(total/samples, sum(
           float((omega[:,j]-gn(np.delete(omega,j,axis=1),phi)@omega[:,j])@
                 (omega[:,j]-gn(np.delete(omega,j,axis=1),phi)@omega[:,j]))
           for j in range(samples))/samples,3e-7)

# Independent integration of the chi-square inverse-moment identity
# used in the exact closed-form mean, at finite parameters.
for degrees in (3,4,5,6,9):
    norm=2**(degrees/2)*gamma(degrees/2)
    density=lambda x: x**(degrees/2-1)*math.exp(-x/2)/norm
    integral,_=quad(lambda t: density(t)/t,0,1000,epsabs=1e-8,epsrel=1e-9,limit=200)
    check(integral,1/(degrees-2),2e-7)
for degrees in (5,6,7,9):
    norm=2**(degrees/2)*gamma(degrees/2)
    density=lambda x: x**(degrees/2-1)*math.exp(-x/2)/norm
    integral,_=quad(lambda t: density(t)/(t*t),0,1000,epsabs=2e-8,epsrel=1e-9,limit=200)
    check(integral,1/((degrees-2)*(degrees-4)),4e-7)

print(f'PASS checks={checks} maximum_numerical_discrepancy={max_residual:.3g}')
print('Finite checks corroborate formula identities only; they do not certify infinite tails.')
