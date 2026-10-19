#!/usr/bin/env python3
"""Standalone analytic and numerical checks of Gaussian current tomography."""
from mpmath import mp
mp.dps = 70

def msd(t,D,a,lam):
    return 2*D*t+mp.fsum(2*aa*(t/ll+mp.expm1(-ll*t)/ll**2) for aa,ll in zip(a,lam))

def current_variance(t,rho,D,a,lam):
    return rho*mp.sqrt(2/mp.pi)*mp.sqrt(msd(t,D,a,lam))

def reconstructed(msd_samples,h,N):
    ds=[msd_samples[k+2]-2*msd_samples[k+1]+msd_samples[k] for k in range(2*N)]
    H=mp.matrix([[ds[i+j] for j in range(N)] for i in range(N)])
    rhs=mp.matrix([-ds[i+N] for i in range(N)])
    coeff=mp.lu_solve(H,rhs)
    roots=mp.polyroots([mp.mpf(1)]+list(reversed(coeff)), maxsteps=300, error=False)
    roots=sorted([mp.re(r) for r in roots]); assert all(mp.fabs(mp.im(r))<mp.mpf('1e-35') for r in mp.polyroots([mp.mpf(1)]+list(reversed(coeff)), maxsteps=300))
    assert all(0<r<1 for r in roots)
    V=mp.matrix([[r**i for r in roots] for i in range(N)])
    w=mp.lu_solve(V,mp.matrix(ds[:N]))
    lam_rec=[-mp.log(q)/h for q in roots]
    a_rec=[w[j]*lam_rec[j]**2/(2*(1-roots[j])**2) for j in range(N)]
    D_rec=(msd_samples[1]-mp.fsum(2*aj*(h/lj+mp.expm1(-lj*h)/lj**2) for aj,lj in zip(a_rec,lam_rec)))/(2*h)
    return D_rec,a_rec,lam_rec,ds

cases = [(mp.mpf('0.6'), [mp.mpf('1.7')], [mp.mpf('.53')],mp.mpf('1.25')),
 (mp.mpf('.33'),[mp.mpf('.91'),mp.mpf('.27')],[mp.mpf('.31'),mp.mpf('1.37')],mp.mpf('.83')),
 (mp.mpf('.75'),[mp.mpf('.1'),mp.mpf('2.3'),mp.mpf('.6')],[mp.mpf('.18'),mp.mpf('.7'),mp.mpf('2.2')],mp.mpf('.6')),
 (mp.mpf('.28'),[mp.mpf('.2'),mp.mpf('.4'),mp.mpf('.9'),mp.mpf('1.1')],[mp.mpf('.13'),mp.mpf('.45'),mp.mpf('.96'),mp.mpf('2.1')],mp.mpf('.5'))]
count=0
for D,a,lam,h in cases:
 N=len(lam);rho=mp.mpf('1.9');samples=[(mp.pi/(2*rho**2))*current_variance(k*h,rho,D,a,lam)**2 for k in range(2*N+2)]
 Dr,ar,lr,ds=reconstructed(samples,h,N)
 recpairs=sorted(zip(lr,ar)); origpairs=sorted(zip(lam,a))
 for ob,ex in zip([Dr]+[v for ll,v in recpairs]+[ll for ll,v in recpairs],[D]+[v for ll,v in origpairs]+[ll for ll,v in origpairs]):
  assert mp.fabs(ob-ex)<mp.mpf('2e-25'),(ob,ex);count+=1
 for k in range(2*N):
  pred=mp.fsum(2*a[j]/lam[j]**2*(1-mp.exp(-lam[j]*h))**2*mp.exp(-lam[j]*k*h) for j in range(N))
  assert mp.fabs(pred-ds[k])<mp.mpf('1e-40');count+=1
 # independent Green-Kubo numerical integral
 for t in [mp.mpf('.19'),mp.mpf('1.5')]:
  quad=2*D*t+2*mp.quad(lambda u:(t-u)*mp.fsum(a[j]*mp.exp(-lam[j]*u) for j in range(N)), [0,t])
  assert mp.fabs(quad-msd(t,D,a,lam))<mp.mpf('1e-45');count+=1
 print('N=',N,'D=',mp.nstr(Dr,12),'relaxation rates=',[mp.nstr(x,10) for x in lr])
# Reverse Poisson jump distribution: numerical direct integral of crossing probability
rho=mp.mpf('1.8');D,a,lam,h=cases[1]
t=mp.mpf('1.3');sig=mp.sqrt(msd(t,D,a,lam)); p=lambda y:mp.erfc(y/(mp.sqrt(2)*sig))/2
mu_num=rho*mp.quad(p,[0,2,5,12,40]);mu_closed=rho*sig/mp.sqrt(2*mp.pi)
assert mp.fabs(mu_num-mu_closed)<mp.mpf('1e-45');count+=1
# Generic finite-sampling obstruction: two distinct nonnegative spectra on 4 frequencies, 2 times, same mass.
from itertools import count as counter
freqs=[mp.mpf('0.4'),mp.mpf('1.1'),mp.mpf('2.0'),mp.mpf('3.3')]
times=[mp.mpf('.7'),mp.mpf('1.6')]
rows=[[mp.mpf(1)]*4]+[[2*(1-mp.cos(x*t))/x**2 for x in freqs] for t in times]
M=mp.matrix(rows); c=mp.lu_solve(M[:,:3],-M[:,3]); v=list(c)+[mp.mpf(1)]
weights_1=[mp.mpf(1)]*4;weights_2=[mp.mpf(1)+(mp.mpf('.5')/max(map(abs,v)))*z for z in v]
assert all(z>0 for z in weights_2)
for row in rows:
 assert mp.fabs(mp.fdot(row,weights_1)-mp.fdot(row,weights_2))<mp.mpf('1e-45');count+=1
assert mp.fabs(mp.fsum(mp.cos(mp.mpf('.09')*f)*z for f,z in zip(freqs,v)))>mp.mpf('1e-8');count+=1
# High-frequency identifiability can be arbitrarily ill-conditioned.
for omega in [20,100,1000]:
 e=mp.mpf('.3'); difference_upper=rho*mp.sqrt(2/mp.pi)*(mp.sqrt(4*e)/omega)
 assert difference_upper<mp.mpf('2')/omega;count+=1
print('ALL',count,'independent checks PASSED; Poisson-rate integral:',mp.nstr(mu_closed,18))
