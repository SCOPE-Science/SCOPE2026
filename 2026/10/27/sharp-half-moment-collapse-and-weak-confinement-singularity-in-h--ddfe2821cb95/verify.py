import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.special import erfcx
from scipy.integrate import cumulative_trapezoid

def search_resolvent(k,r,h=.002,left=-12.0):
    right=1.; n=round((right-left)/h); h=(right-left)/n
    grid=left+h*np.arange(1,n)
    N=n-1
    # Fokker-Planck adjoint generator G''+k*x*G'+k*G
    # flux discretization conservative centered: L G = G''+k d_x(xG)
    # finite differences at x_i: k*(x G)'=k*x G' +k G
    main=np.full(N, r-k+2/h**2)
    lo=-1/h**2 + k*grid[1:]/(2*h)    # x_i for lower neighbour (row i)
    up=-1/h**2 - k*grid[:-1]/(2*h)  # x_i for upper neighbour (row i)
    # want offdiag at row i col i-1: -1/h2 + k*x_i/(2h)
    M=diags([lo,main,up],[-1,0,1],format='csc')
    rhs=np.zeros(N); rhs[np.argmin(abs(grid))]=1/h
    G=spsolve(M,rhs)
    # positive hitting flux (Dirichlet at x=1) from last interior
    phi=(4*G[-1]-G[-2])/(2*h)
    J=np.trapezoid(G*np.maximum(grid,0), grid)
    I=np.trapezoid(G*np.maximum(-grid,0), grid)
    p=phi+r*J
    K=r*I/p
    identity=(r+k)*(I-J)/phi
    return grid,G,phi,I,J,p,K,identity

def retour_params(x,kappa):
    b=np.zeros_like(x)
    m=np.zeros_like(x)
    neg=x<0; pos=x>0
    xx=x[pos]; yy=x[neg]
    # integrate on independent fine grid [0,1] for S,A,B
    y=np.linspace(0,1,4001)
    S=np.r_[0,cumulative_trapezoid(np.exp(kappa*y*y/2),y)]
    A=np.r_[0,cumulative_trapezoid(S*np.exp(-kappa*y*y/2),y)]
    B0=(S[-1]-S)*np.exp(-kappa*y*y/2)
    B=np.r_[0,cumulative_trapezoid(B0[::-1],y[::-1])][::-1]
    # scipy cumulative_trapezoid with reversed x produces negative; take minus
    B=-B
    Sx=np.interp(xx,y,S); Ax=np.interp(xx,y,A); Bx=np.interp(xx,y,B)
    b[pos]=Sx/S[-1]
    m[pos]=((S[-1]-Sx)*Ax+Sx*Bx)/S[-1]
    if neg.any():
      a=np.linspace(0,-min(yy),10001)
      V=np.r_[0,cumulative_trapezoid(erfcx(np.sqrt(kappa/2)*a),a)]
      m[neg]=np.sqrt(np.pi/(2*kappa))*np.interp(-yy,a,V)
    return b,m

if __name__ == '__main__':
    for k in (0.5, 2.0):
        r=1.0
        x,G,phi,I,J,p,K,identity=search_resolvent(k,r)
        assert 0.0<K<1.0 and p>0 and phi>0
        assert abs(identity-1)<0.002
        assert abs(K-(1-k*phi/((k+r)*p)))<0.002
        last_err=float('inf')
        for kap in (0.04,0.01,0.0025,0.0001):
            b,m=retour_params(x,kap)
            pr=phi+r*np.trapezoid(G*b,x)
            E=((1-phi)/r+r*np.trapezoid(G*m,x))/pr
            target=np.sqrt(np.pi/2)*K
            err=abs(np.sqrt(kap)*E-target)
            assert err<last_err and np.isfinite(E) and E>0
            last_err=err
        assert last_err < 0.025
        print(f'k={k}, r={r}: K={K:.6f}; predicted scaled mean={target:.6f}; final error={last_err:.6f}; checks passed')
    print('Verification complete: all finite-grid tests passed.')
