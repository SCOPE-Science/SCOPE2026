"""Full 3D rho for wall-fan datum: caps along xi1=0 line, radius rcap=0.2 discs
(centers (0,t_k)), L2-normalized sum; P*=x1x2x3 wall width 10; integrate |Ef|^p
over B_100: wall vs total. Ef(x)=sum_k c*int_{cap k} e^{i(x' .xi+x3 h0)}.
Discretize caps with Riemann points; field grid: x1 step 2 (-40..40), x2 step 4
(-100..100)? cost. Cheaper: exploit x1-profile narrow (width ~1/0.2=5 <<10):
most energy inside |x1|<=10 automatically; x2/x3 spread along tube dirs.
Field: x1 in -20..20 step 1; x2 in -100..100 step 2; x3 in -100..100 step 4; ball cut.
Caps: K=5 centers t=-0.8..0.8, r=0.2, equal weights L2-normalized.
Cost: field pts 41*101*51=211k x cap pts (5*~300=1500) = 316M... too slow in python.
Reduce: x2 step 4 (51), x3 step 5 (41): 41*51*41=86k x 1500 = 129M still slow.
Alternative: analytic tube superposition? Use coarser cap quadrature (m=10 -> ~80/cap, 400 tot)
and field 41*51*41=86k: 34M complex mults ~ minutes. Use numpy vectorization.
"""
import math, cmath
import numpy as np
K=5; rcap=0.2
centers=[(0.0,-0.8+1.6*k/(K-1)) for k in range(K)]
m=10; h=2*rcap/m
cappts=[]
for (c1,c2) in centers:
    for i in range(m):
        for j in range(m):
            u=c1-rcap+h/2+i*h; v=c2-rcap+h/2+j*h
            if (u-c1)**2+(v-c2)**2<=rcap*rcap:
                cappts.append((u,v))
cappts=np.array(cappts)
print("cap pts total:",len(cappts))
# L2 norm of f (f=1 on each cap): sqrt(K*pi*rcap^2)
fL2=math.sqrt(K*math.pi*rcap**2)
print("fL2:",fL2)
U=cappts[:,0]; V=cappts[:,1]
H=(U*U+V*V)/2.0+(0.05/6.0)*U**3
w=h*h/fL2  # normalized weights
x1=np.arange(-20,21,1.0); x2=np.arange(-100,101,4.0); x3=np.arange(-100,101,5.0)
tot=0.0; wall=0.0; p0=3.25; dv=1.0*4.0*5.0
Ph=np.exp(1j*0)  # placeholder
for k3,z in enumerate(x3):
    # phase = x1*U+x2*V+z*H for all x1,x2: vectorize over x1,x2 via broadcasting
    # E(x1,x2,z)=sum_cap w e^{i(...)} : shape (len(x1),len(x2))
    E=np.sum(w*np.exp(1j*(x1[:,None,None]*U[None,None,:]+np.zeros(1))),axis=0) if False else None
    A1=x1[:,None]*U[None,:]+z*H[None,:]   # (n1,nc)
    E1=np.exp(1j*A1).sum(axis=1)*w        # sum over caps of e^{i(x1 U+zH)} (n1,nc)->(n1,)
    B1=x2[:,None]*V[None,:]               # (n2,nc)
    E2=np.exp(1j*B1)                      # (n2,nc)
    E=(E1[None,:,:]*E2[:,None,:] if False else (E1[None,:]*np.ones((len(x2),1))))*1
    # E(x1i,x2j) = w*sum_c e^{i(x1i U_c + x2j V_c + z H_c)}
    Efull=w*(np.exp(1j*A1)[:,None,:]*np.exp(1j*B1)[None,:,:]).sum(axis=2)  # (n1,n2)
    P=np.abs(Efull)**p0
    for i,xx1 in enumerate(x1):
        for j,xx2 in enumerate(x2):
            if xx1*xx1+xx2*xx2+z*z>100**2: continue
            v=P[i,j]*dv
            tot+=v
            if min(abs(xx1),abs(xx2),abs(z))<=10: wall+=v
    print(f"z={z}: cum rho={wall/max(tot,1e-30):.4f}")
print("FINAL tot:",tot,"wall:",wall,"rho=",wall/tot)
