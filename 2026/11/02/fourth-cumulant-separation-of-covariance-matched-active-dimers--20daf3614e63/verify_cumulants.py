"""Independent finite-time moment-ODE and ordered-cumulant integral checks."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import expm_multiply

def gaussian_moment(n, var):
    return (math.prod(range(1, n, 2)) * var ** (n // 2)) if n % 2 == 0 else 0.0

def moment_ode(a,b,g,sigma,T,kind):
    if kind=='ou':
        ids=[(i,j,k) for k in range(5) for i in range(9) for j in range(9) if i+j+2*k<=8]
    else:
        ids=[(p,j,k) for k in range(5) for j in range(9) for p in (0,1) if j+2*k<=8]
    idx={key:i for i,key in enumerate(ids)}
    M=lil_matrix((len(ids),len(ids)),dtype=float)
    ini=np.zeros(len(ids))
    for key,rr in idx.items():
        if kind=='ou':
            i,j,k=key
            if k==0:ini[rr]=gaussian_moment(i,g*g)*gaussian_moment(j,sigma*sigma)
            terms=[(key,-a*i-b*j),((i-2,j,k),a*g*g*i*(i-1)),((i,j-2,k),b*sigma*sigma*j*(j-1)),((i+1,j+1,k-1),-k/2)]
        else:
            p,j,k=key
            if k==0 and p==0:ini[rr]=gaussian_moment(j,sigma*sigma)
            terms=[(key,-a*p-b*j),((p,j-2,k),b*sigma*sigma*j*(j-1)),((1-p,j+1,k-1),-k*g/2)]
        for c,v in terms:
            if v and c in idx:M[rr,idx[c]]+=v
    val=expm_multiply(csr_matrix(M)*T,ini)
    k2=(0,0,2) if kind=='ou' else (0,0,2)
    k4=(0,0,4)
    var=val[idx[k2]]
    kurt=val[idx[k4]]-3*var**2
    return var,kurt

def calc_ker(a,b,g,sigma,T,kind):
    s=a+b
    def inner(z):
        if z<1e-10:return z**3/6
        return z/s**2*(1+math.exp(-s*z)) - 2*(1-math.exp(-s*z))/s**3
    # integral_0^z dw w(z-w)e^{-s w}: z/s^2(1+e^{-sz})-2(1-e^{-sz})/s^3
    def f(u):
        w=inner(T-u)
        if kind=='ou':z=math.exp(-2*b*u)+math.exp(-2*a*u)+math.exp(-2*s*u)
        elif kind=='tele':z=math.exp(-2*b*u)*(1-math.exp(-2*a*u))
        else:z=math.exp(-2*a*u)+2*math.exp(-2*s*u)
        return 3*g**4*sigma**4*w*z
    return quad(f,0,T,epsabs=1e-10,epsrel=1e-10)[0]

def rates(a,b,g,sigma):
    s=a+b
    tele=3*g**4*sigma**4*a/(2*b*s**3)
    gap=3*g**4*sigma**4*(3*a+b)/(2*a*s**3)
    ou=tele+gap
    return ou,tele,gap

def run():
    cases=[(1.3,2.1,1.7,0.8),(0.55,3.1,1.2,0.71),(3.2,0.45,0.93,1.4)]
    checks=0
    for a,b,g,sigma in cases:
        ou_rate,tele_rate,gap_rate=rates(a,b,g,sigma)
        assert ou_rate>tele_rate>0
        assert abs(tele_rate/ou_rate-a*a/(a*a+3*a*b+b*b))<1e-12
        checks+=2
        for T in (0.5,1.7,5.0,13.0):
            vo,ko=moment_ode(a,b,g,sigma,T,'ou')
            vt,kt=moment_ode(a,b,g,sigma,T,'tele')
            target=g*g*sigma*sigma/(2*(a+b))*(T-(1-math.exp(-(a+b)*T))/(a+b))
            assert abs(vo-target)<5e-8*max(1,target)
            assert abs(vt-target)<5e-8*max(1,target)
            assert ko>kt>0, (a,b,T,ko,kt)
            koo=calc_ker(a,b,g,sigma,T,'ou')
            ktt=calc_ker(a,b,g,sigma,T,'tele')
            gap=calc_ker(a,b,g,sigma,T,'gap')
            for x,y in ((ko,koo),(kt,ktt),(ko-kt,gap)):
                assert abs(x-y)<3e-7*max(1,abs(y)), (a,b,T,x,y)
                checks+=1
            checks+=3
        assert abs(calc_ker(a,b,g,sigma,600,'ou')/600-ou_rate)<0.04*ou_rate
        assert abs(calc_ker(a,b,g,sigma,600,'tele')/600-tele_rate)<0.04*tele_rate
        checks+=2
        print('params',a,b,g,sigma,'rate OU',ou_rate,'rate tele',tele_rate,'ratio',tele_rate/ou_rate)
    print('PASS',checks,'independent identities / moment-evolution checks')
if __name__=='__main__':run()
