"""Independent numerical checks for the resolvent formula of affine-reset diffusion.
Requires NumPy and SciPy. No random data or external files.
"""
import numpy as np
from scipy.integrate import quad
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def fourier_density(t, a, D, r, n):
    c = D/r
    def inverse_product(k):
        p = 1.0
        z = 1.0
        aa = a*a
        for j in range(n+1):
            p /= 1+c*z*k*k
            z *= aa
        return p
    v, err = quad(inverse_product, 0, np.inf, weight='cos', wvar=abs(t),
                  epsabs=1e-10, epsrel=2e-10, limit=200)
    return v/np.pi


def fourier_mean(x, L=1., a=-0.5, D=1., r=1., N=20):
    pi_L = fourier_density(L, a, D, r, max(N, 60))
    s = 0.0
    for n in range(N):
        an = a**n
        f = fourier_density(L*(1-an),a,D,r,n)
        g = fourier_density(L-an*x,a,D,r,n)
        s += (f-g)/r
    return s/pi_L, pi_L


def finite_difference_mean(x, a, D=1., r=1., L=1., B=16., h=.04):
    grid = np.arange(-B,B+h/2,h)
    m = len(grid)
    jL = int(np.argmin(abs(grid-L)))
    assert abs(grid[jL]-L) < 1e-8
    H = lil_matrix((m,m))
    rhs = np.ones(m)
    for i,z in enumerate(grid):
        if i==jL:
            H[i,i]=1; rhs[i]=0; continue
        if i==0:
            H[i,i]=2*D/h**2+r; H[i,i+1]=-2*D/h**2
        elif i==m-1:
            H[i,i]=2*D/h**2+r; H[i,i-1]=-2*D/h**2
        else:
            H[i,i]=2*D/h**2+r
            H[i,i-1]=-D/h**2
            H[i,i+1]=-D/h**2
        t = (a*z+B)/h
        q = int(np.floor(t))
        w=t-q
        if q>=m-1:q=m-2; w=1.
        H[i,q]-=r*(1-w)
        H[i,q+1]-=r*w
    v=spsolve(H.tocsr(),rhs)
    return float(np.interp(x,grid,v))


def test():
    count=0
    for a in (-.2,-.5,-.8):
        for x in (0.,-1/abs(a),.6):
            val,pi=fourier_mean(x,a=a,N=26)
            approx=finite_difference_mean(x,a,h=.04)
            assert np.isfinite(val) and val>=0 and pi>0
            assert abs(val-approx)<0.005, (a,x,val,approx)
            count+=1
        v12,pi=fourier_mean(0,a=a,N=12)
        v20,_=fourier_mean(0,a=a,N=20)
        C=np.log(1/a**2)/(2*np.pi*(1-a*a)*(1-abs(a))*pi)
        assert abs(v12-v20) <= C*abs(a)**12+1e-7
        count+=1
    v0,_=fourier_mean(0,a=0.0,N=1)
    assert abs(v0-(np.e-1))<1e-8
    count+=1
    print('PASS',count,'checks; examples at a=-0.5:',fourier_mean(0,a=-.5)[0],fourier_mean(-2,a=-.5)[0])

if __name__=='__main__':test()
