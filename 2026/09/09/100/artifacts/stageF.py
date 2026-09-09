# STAGE F: vectorized Newton MOTS solve + stability-potential Q profile + mesh-convergence
# error bounds for validated enclosure [L,U] of lambda1.
# Operator reduction (documented in DRAFT): time-symmetric (K=0) => MOTS torsion X=0;
# vacuum => L_Sigma = -Delta + Q, Q = -(Ric(n,n)+|A|^2)_phys. Min-principle: lambda1 >= min Q.
# Upper: Rayleigh u=1: lambda1 <= mean(Q) = 4pi/A - mean(|A|^2/2) <= max Q.
import numpy as np, math, time
A1=A2=1.0; Z1,Z2=1.0,-1.0

def vec_residuals(H, lam, h, zc):
    N=len(H)-1
    s=np.sin(lam); c=np.cos(lam)
    V=np.empty_like(H); W=np.empty_like(H)
    V[1:-1]=(H[2:]-H[:-2])/(2*h); W[1:-1]=(H[2:]-2*H[1:-1]+H[:-2])/h**2
    V[0]=0.0; V[-1]=0.0; W[0]=W[1]; W[-1]=W[-2]
    dX=V*s+H*c; dZ=V*c-H*s
    d2X=W*s+2*V*c-H*s; d2Z=W*c-2*V*s-H*c
    spd=np.hypot(dX,dZ)+1e-300
    nx=-dZ/spd; nz=dX/spd
    kap=-(dX*d2Z-dZ*d2X)/spd**3
    X_=H*s; Z_=zc+H*c
    d1=np.sqrt(X_**2+(Z_-Z1)**2); d2=np.sqrt(X_**2+(Z_-Z2)**2)
    ps=1.0+0.5/d1+0.5/d2
    gr=-0.5*X_/d1**3-0.5*X_/d2**3; gz=-0.5*(Z_-Z1)/d1**3-0.5*(Z_-Z2)/d2**3
    th=kap+nx/np.maximum(X_,1e-300)+4.0*(nx*gr+nz*gz)/ps
    R=np.empty_like(H); R[1:-1]=th[1:-1]
    R[0]=(-3*H[0]+4*H[1]-H[2])/(2*h)
    R[-1]=(3*H[-1]-4*H[-2]+H[-3])/(2*h)
    return R

def solve_mots(zc, N=400, iters=25, tol=3e-12, Hinit=0.42):
    lam=np.linspace(0,math.pi,N+1); h=math.pi/N
    H=np.full(N+1,Hinit)
    R=vec_residuals(H,lam,h,zc)
    for it in range(iters):
        nrm=np.max(np.abs(R))
        if nrm<tol: break
        J=np.zeros((N+1,N+1)); e=1e-7
        # vectorized Jacobian via loop over j but residuals are vectorized: O(N^2) cheap ops
        for j in range(N+1):
            Hej=H.copy(); Hej[j]+=e
            J[:,j]=(vec_residuals(Hej,lam,h,zc)-R)/e
        d=np.linalg.solve(J,-R)
        al=1.0
        for _ in range(14):
            Hn=H+al*d
            if np.any(Hn<=0): al*=0.5; continue
            Rn=vec_residuals(Hn,lam,h,zc)
            if np.max(np.abs(Rn))<nrm: break
            al*=0.5
        H=H+al*d; R=vec_residuals(H,lam,h,zc)
    return lam,H,R

def Q_profile(H, lam):
    h=lam[1]-lam[0]
    s=np.sin(lam); c=np.cos(lam)
    V=np.gradient(H,h)
    dX=V*s+H*c; dZ=V*c-H*s
    sp=np.hypot(dX,dZ)
    nx=-dZ/sp; nz=dX/sp
    X=H*s; Z=1.0+H*c
    W2=np.gradient(V,h)
    d2X=W2*s+2*V*c-H*s; d2Z=W2*c-2*V*s-H*c
    with np.errstate(all='ignore'):
        k1=-(dX*d2Z-dZ*d2X)/sp**3
        k2=nx/np.maximum(X,1e-300)
    Ahat2=(k1-k2)**2/2
    Q=np.full_like(H, np.nan)
    for i in range(1,len(lam)-1):
        x,z=X[i],Z[i]
        d1=math.sqrt(x**2+(z-Z1)**2); d2=math.sqrt(x**2+(z-Z2)**2)
        ps=1.0+0.5/d1+0.5/d2
        gx=-0.5*x/d1**3-0.5*x/d2**3; gz=-0.5*(z-Z1)/d1**3-0.5*(z-Z2)/d2**3
        gxx=-0.5/d1**3+1.5*x**2/d1**5-0.5/d2**3+1.5*x**2/d2**5
        gzz=-0.5/d1**3+1.5*(z-Z1)**2/d1**5-0.5/d2**3+1.5*(z-Z2)**2/d2**5
        gxz=1.5*x*(z-Z1)/d1**5+1.5*x*(z-Z2)/d2**5
        nxn,nzn=nx[i],nz[i]
        Rnn=-2/ps*(gxx*nxn*nxn+2*gxz*nxn*nzn+gzz*nzn*nzn) \
            +6/ps**2*(gx*nxn+gz*nzn)**2-2/ps**2*(gx**2+gz**2)
        Q[i]=-(Rnn+Ahat2[i])/ps**4
    return Q

if __name__=="__main__":
    profs={}
    for N in [400,800]:
        t0=time.time()
        lam,H,R=solve_mots(1.0,N=N)
        Q=Q_profile(H,lam)
        dt=time.time()-t0
        profs[N]=(lam,H,R,Q)
        print("N=%d maxres=%.2e Hrange=[%.5f,%.5f] qmin=%.6f qmax=%.6f t=%.1fs"%(
            N,np.max(np.abs(R)),H.min(),H.max(),np.nanmin(Q[1:-1]),np.nanmax(Q[1:-1]),dt))
    np.save('output/artifacts/prof400.npy', np.vstack([profs[400][0],profs[400][1],profs[400][3]]))
    np.save('output/artifacts/prof800.npy', np.vstack([profs[800][0],profs[800][1],profs[800][3]]))
