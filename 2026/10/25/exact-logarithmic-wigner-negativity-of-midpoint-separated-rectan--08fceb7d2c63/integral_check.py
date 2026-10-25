import numpy as np
from verify import coeff

def nv(R,c,a,dt=0.002):
    c=np.array(c,float);a=np.array(a,complex);S=np.vdot(a,a).real
    xi=np.linspace(-R,R,int(round(2*R/dt))+1)
    xx=np.abs(xi); h=2*np.pi*xx
    q=np.floor(h/np.pi).astype(int);v=h-q*np.pi
    J=np.zeros_like(xi)
    np.divide(2*q+1-np.cos(v),2*np.pi*xx,where=xx>1e-12,out=J)
    fac=np.zeros_like(xi)
    np.divide(J,np.pi*S*xx,where=xx>1e-12,out=fac)
    fac[xx<=1e-12]=1/S
    rest=np.full_like(xi,S)
    for j in range(len(c)):
        for k in range(j+1,len(c)):
            rest+=2*abs(a[j]*a[k])*np.abs(np.cos(2*np.pi*(c[j]-c[k])*xi-np.angle(a[j]*np.conj(a[k]))))
    l1=np.trapezoid(rest*fac,xi)
    fhat=np.sinc(xi)/np.sqrt(S)*sum(aj*np.exp(-2j*np.pi*cj*xi) for cj,aj in zip(c,a))
    signed=np.trapezoid(abs(fhat)**2,xi)
    return (l1-signed)/2
for cc,aa in [([0],[1]),([-6,6],[1,.7*np.exp(.41j)]),([1,10,100],[1,np.exp(.41j),np.exp(-.73j)])]:
    x=nv(30,cc,aa); y=nv(300,cc,aa);C=coeff(aa)
    print('N',len(cc),'negvol30',round(x,7),'negvol300',round(y,7),'slope_30_to_300',round((y-x)/np.log(10),7),'analytic_coeff',round(C,7))
