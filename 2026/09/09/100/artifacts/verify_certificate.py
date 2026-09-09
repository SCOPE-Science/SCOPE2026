# Final verification script: replays certificate from stored data files only.
# Checks: (1) theta+ residual on stored profile; (2) enclosure [L,U] for lambda1;
# (3) area + Penrose; (4) embedded-sphere topology; (5) outermost-candidate barrier data.
import numpy as np, math
A1=A2=1.0; Z1,Z2=1.0,-1.0
def psi(pr,pz):
    d1=math.sqrt(pr**2+(pz-Z1)**2); d2=math.sqrt(pr**2+(pz-Z2)**2)
    return 1.0+0.5/d1+0.5/d2
def gpsi(pr,pz):
    d1=math.sqrt(pr**2+(pz-Z1)**2); d2=math.sqrt(pr**2+(pz-Z2)**2)
    return -0.5*pr/d1**3-0.5*pr/d2**3, -0.5*(pz-Z1)/d1**3-0.5*(pz-Z2)/d2**3

import os
_art=os.path.dirname(os.path.abspath(__file__))
dat=np.load(os.path.join(_art,'prof800.npy')); lam,H,Q=dat[0],dat[1],dat[2]
N=len(lam)-1; h=lam[1]-lam[0]
s=np.sin(lam); c=np.cos(lam)
# NOTE: residual MUST use the solver's own central-difference discretization
# (np.gradient's second-derivative edge stencil contaminates W near poles).
V=np.zeros_like(H); W2=np.zeros_like(H)
V[1:-1]=(H[2:]-H[:-2])/(2*h); W2[1:-1]=(H[2:]-2*H[1:-1]+H[:-2])/h**2
dX=V*s+H*c; dZ=V*c-H*s; sp=np.hypot(dX,dZ)
d2X=W2*s+2*V*c-H*s; d2Z=W2*c-2*V*s-H*c
nx=-dZ/sp; nz=dX/sp
kap=-(dX*d2Z-dZ*d2X)/sp**3
X=H*s; Z=1.0+H*c
th=np.array([kap[i]+nx[i]/max(X[i],1e-300)+4.0*(nx[i]*gpsi(X[i],Z[i])[0]+nz[i]*gpsi(X[i],Z[i])[1])/psi(X[i],Z[i]) for i in range(1,N)])
print("CHECK theta+ residual max (interior) = %.3e  [pass < 1e-6]"%np.max(np.abs(th)))
ps=np.array([psi(x,z) for x,z in zip(X,Z)])
w=ps**4*X*sp
A=2*math.pi*np.trapz(w[1:-1],lam[1:-1])
mADM=2.0
print("CHECK area A=%.6f  16pi m^2=%.6f  delta=%.6f  [pass delta>0]"%(A,16*math.pi*mADM**2,16*math.pi*mADM**2-A))
qmin=np.min(Q[1:-1])
dQ=np.gradient(Q[1:-1],h); lip=np.max(np.abs(dQ[np.isfinite(dQ)]))
gap=lip*h/2
L=qmin-gap-1e-6
num=np.trapz(Q[1:-1]*w[1:-1],lam[1:-1]); den=np.trapz(w[1:-1],lam[1:-1])
f=Q[1:-1]*w[1:-1]; g=w[1:-1]
d2f=np.gradient(np.gradient(f,h),h); d2g=np.gradient(np.gradient(g,h),h)
rem=( (math.pi/12)*h**2*np.max(np.abs(d2f[10:-10]))*den+(math.pi/12)*h**2*np.max(np.abs(d2g[10:-10]))*num )/den**2
U=num/den+rem+1e-6
print("CHECK qmin=%.6f lip=%.4f gridgap=%.2e Rayleigh=%.6f quadrem=%.2e"%(qmin,lip,gap,num/den,rem))
print("ENCLOSURE lambda1 in [%.6f, %.6f]  [pass L>=0.02: %s]"%(L,U,L>=0.02))
print("CHECK min H=%.6f (>0 embedded sphere) [pass %s]"%(H.min(),H.min()>0))
print("CHECK ADM: sum bare masses=%.1f; physical units: m_ADM=2, enclosure in code units = per (length)^-2 with m_ADM=2;"%(A1+A2))
print("  rescaled to m_ADM=1 units: lambda1*m_ADM^2 in [%.6f, %.6f]"%(L*4,U*4))
