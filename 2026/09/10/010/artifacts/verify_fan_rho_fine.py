"""Tightened rho integration for fan datum: x1 in [-30,30] step 1, x2 step 2,
x3 step 2.5 (finer), cap quadrature m=14. Also split wall energy by which plane
(|x1| vs |x2| vs |x3|) for the ledger. Vectorized over x1,x2 per z-slice."""
import math, cmath
import numpy as np
K=5; rcap=0.2; p0=3.25
centers=[(0.0,-0.8+1.6*k/(K-1)) for k in range(K)]
m=14; h=2*rcap/m
cap=[]
for (c1,c2) in centers:
    for i in range(m):
        for j in range(m):
            u=c1-rcap+h/2+i*h; v=c2-rcap+h/2+j*h
            if (u-c1)**2+(v-c2)**2<=rcap*rcap: cap.append((u,v))
cap=np.array(cap); U=cap[:,0]; V=cap[:,1]; H=(U*U+V*V)/2.0+(0.05/6.0)*U**3
fL2=math.sqrt(K*math.pi*rcap**2); w=h*h/fL2
print("cap pts:",len(cap),"fL2:",round(fL2,4))
x1=np.arange(-30,31,1.0); x2=np.arange(-100,101,2.0); x3=np.arange(-100,101,2.5)
dv=1.0*2.0*2.5
tot=0; wall=0; w1=0; w2=0; w3=0
eU=np.exp(1j*0)
for z in x3:
    A1=x1[:,None]*U[None,:]+z*H[None,:]
    E1=np.exp(1j*A1)
    E2=np.exp(1j*x2[:,None]*V[None,:])
    Efull=w*(E1[:,None,:]*E2[None,:,:]).sum(axis=2)
    P=np.abs(Efull)**p0
    X1=np.abs(x1)[:,None]; X2=np.abs(x2)[None,:]; AZ=abs(z)
    inball=(x1[:,None]**2+x2[None,:]**2+z*z)<=100**2
    inwall=(np.minimum(np.minimum(X1*np.ones_like(X2),np.ones_like(X1)*X2),AZ* np.ones_like(X2) if False else AZ)<=10)
    # inwall: min(|x1|,|x2|,|z|)<=10
    M=(np.minimum(np.minimum(np.broadcast_to(np.abs(x1)[:,None],P.shape),np.broadcast_to(np.abs(x2)[None,:],P.shape)),abs(z))<=10)
    V_ = P*dv*inball
    tot+=V_.sum(); wall+=(V_*M).sum()
    w1+=(V_*(np.broadcast_to(np.abs(x1)[:,None],P.shape)<=10)).sum()
    w2+=(V_*(np.broadcast_to(np.abs(x2)[None,:],P.shape)<=10)).sum()
    w3+=(V_*(abs(z)<=10)).sum()
print("tot:",float(tot),"wall:",float(wall),"rho=",float(wall/tot))
print("by-plane (overlap) |x1|<=10:",float(w1/tot),"|x2|<=10:",float(w2/tot),"|x3|<=10:",float(w3/tot))
