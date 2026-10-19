#!/usr/bin/env python3
"""Independent finite-dimensional checks of concentric cyclic polynomial evaluation spectra."""
import math, cmath, json
import numpy as np

def compare(n,r,s,phase,c):
    order=2*n
    angles=np.arange(n)*2*np.pi/n
    z=np.r_[r*np.exp(1j*angles),s*np.exp(1j*(angles+phase))]
    kval=np.array([sum(c[k]**2*rad**(2*k) for k in range(order)) for rad in (r,s)])
    F=np.array([[c[k]*zz**k/math.sqrt(kval[i//n]) for k in range(order)] for i,zz in enumerate(z)])
    direct=np.linalg.eigvalsh(F.conj().T@F)
    blocks=[]
    for k in range(n):
        tr=n/kval[0]*(c[k]**2*r**(2*k)+c[k+n]**2*r**(2*(k+n)))+n/kval[1]*(c[k]**2*s**(2*k)+c[k+n]**2*s**(2*(k+n)))
        det=n*n*c[k]**2*c[k+n]**2*(r*s)**(2*k)/np.prod(kval)*abs(s**n*np.exp(1j*n*phase)-r**n)**2
        disc=max(0.,tr**2-4*det)
        blocks.extend([(tr-math.sqrt(disc))/2,(tr+math.sqrt(disc))/2])
    formula=np.sort(blocks)
    return float(max(abs(direct-formula))), float(abs(float(2*np.linalg.slogdet(F)[1])-float(np.log(formula).sum()))) if min(formula)>1e-10 else None

def hardyspectrum(n,r,phase):
    rad2=r*r
    a=n*(1-r*r)/(-math.expm1(2*n*math.log(r))) if r<1 else 1.
    # equivalent n(1-r²)/(1-r^(2n))
    theta=r**n
    gamma=abs(cmath.exp(1j*n*phase)-theta)**2/(2*(1+theta**2))
    lam=[]
    for k in range(n):
        u=a*r**(2*k)
        disc=(1-u)**2+4*(1-gamma)*u
        lam.extend([(1+u-math.sqrt(max(0,disc)))/2,(1+u+math.sqrt(max(0,disc)))/2])
    return np.sort(lam),gamma,a

out={'comparisons':0,'worst_eigenvalue_abs_error':0.,'worst_logdet_abs_error':0.,'optimizations':0,'asymptotics':[]}
for n in range(2,10):
    for r,s in [(0.25,1.),(.7,.91),(.89,.89),(1.,1.),(.58,1.19)]:
        for phase in [math.pi/n, .12/n, .7/n,1.8/n]:
            # equal radii with collision at phase zero excluded; phases here nonzero
            c=np.array([1.0+0.03*k for k in range(2*n)],dtype=float)
            err,logerr=compare(n,r,s,phase,c)
            out['comparisons']+=1
            out['worst_eigenvalue_abs_error']=max(out['worst_eigenvalue_abs_error'],err)
            if logerr is not None:out['worst_logdet_abs_error']=max(out['worst_logdet_abs_error'],logerr)
            assert err < 2e-10,(n,r,s,phase,err)
            if logerr is not None and r>=.5:assert logerr<3e-6
        # conditions and determinants optimized at half-shift
        if not (r==s==1):
            ck=np.array([math.sqrt(math.comb(2*n-1,k)) for k in range(2*n)],dtype=float)
            opt, _=compare(n,r,s,math.pi/n,ck)
            assert opt<1e-9
            def spectrum(p):
                z=np.r_[r*np.exp(2j*np.pi*np.arange(n)/n),s*np.exp(1j*(2*np.pi*np.arange(n)/n+p))]
                kr=sum(ck[k]**2*r**(2*k) for k in range(2*n));ks=sum(ck[k]**2*s**(2*k) for k in range(2*n))
                F=np.array([[ck[k]*zz**k/math.sqrt(kr if j<n else ks) for k in range(2*n)] for j,zz in enumerate(z)])
                return np.linalg.eigvalsh(F.conj().T@F)
            vopt=spectrum(math.pi/n)
            for p in np.linspace(.02,2*math.pi/n-.02,15):
                v=spectrum(p)
                assert vopt[0]>=v[0]-1e-10
                assert vopt[-1]<=v[-1]+1e-10
                assert np.log(vopt).sum()>=np.log(v).sum()-1e-8
                out['optimizations']+=1
# Hardy special formulas, avoiding loss of precision for min eigen via det/max.
for r in (.35,.65,.85):
    for n in (10,20,40,70):
        q,g,a=hardyspectrum(n,r,math.pi/n)
        # stable lambda_min = gamma * umin / lambda_plus(umin)
        theta=r**n;gamma=(1+theta)**2/(2*(1+theta**2))
        u_min=a*r**(2*n-2)
        lp_min=(1+u_min+math.sqrt((1-u_min)**2+4*(1-gamma)*u_min))/2
        la_max=(1+a+math.sqrt((1-a)**2+4*(1-gamma)*a))/2
        ratio=la_max*lp_min/(gamma*u_min)
        out['asymptotics'].append({'r':r,'n':n,'asymptotic_scaled_ratio':ratio*r**(2*n-2)/2})
print(json.dumps(out,indent=2))
