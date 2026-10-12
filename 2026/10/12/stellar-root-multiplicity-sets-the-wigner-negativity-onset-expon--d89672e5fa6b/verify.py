"""Independent finite Fock-basis checks for pure-loss Wigner stellar asymptotics."""
import math
import numpy as np
from scipy.special import eval_genlaguerre, roots_laguerre
from numpy.polynomial.legendre import leggauss


def normalized(coeff):
    a=np.array(coeff,dtype=complex)
    a/=np.linalg.norm(a)
    return a

def bargmann_poly(coeff):
    return np.polynomial.Polynomial(np.array([v/math.sqrt(math.factorial(k)) for k,v in enumerate(coeff)],dtype=complex))

def exact_poly(coeff,eta,beta):
    f=bargmann_poly(coeff)
    z=2*math.sqrt(eta)*np.asarray(beta)
    s=0.
    q=2*eta-1
    for l in range(len(coeff)):
        s+=(-q)**l/math.factorial(l)*np.abs(f.deriv(l)(z))**2
    return 2/np.pi*np.exp(-2*np.abs(beta)**2)*s

def loss_rho(coeff,eta):
    n=len(coeff);rho=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(n):
            for k in range(min(i,j)+1):
                rho[i-k,j-k]+=coeff[i]*np.conj(coeff[j])*math.sqrt(math.comb(i,k)*math.comb(j,k))*(eta**((i+j)/2-k))*((1-eta)**k)
    return rho

def direct_wigner(coeff,eta,beta):
    rho=loss_rho(coeff,eta)
    y=0j
    for i in range(len(coeff)):
        for j in range(len(coeff)):
            if i>=j:
                y+=rho[i,j]*(-1)**j*math.sqrt(math.factorial(j)/math.factorial(i))*(2*beta)**(i-j)*eval_genlaguerre(j,i-j,4*abs(beta)**2)
            else:
                y+=rho[i,j]*(-1)**i*math.sqrt(math.factorial(i)/math.factorial(j))*(2*np.conj(beta))**(j-i)*eval_genlaguerre(i,j-i,4*abs(beta)**2)
    return float(np.real(2/np.pi*np.exp(-2*abs(beta)**2)*y))

def c_laguerre(m):
    roots=roots_laguerre(m)[0]; grid=[0]+list(roots)+[roots[-1]+3]
    from scipy.integrate import quad
    def p(x):return max(0.,(-1)**(m+1)*eval_genlaguerre(m,0,x))
    return sum(quad(p,a,b,epsabs=1e-12)[0] for a,b in zip(grid[:-1],grid[1:]))

def root_data(coeff):
    f=bargmann_poly(coeff);r=np.roots(f.coef[::-1]);seen=[]
    for z in r:
        for pair in seen:
            if abs(pair[0]-z)<1e-5:
                pair[1]+=1
                break
        else:seen.append([z,1])
    return f,seen

def predicted(coeff):
    f,zeros=root_data(coeff);m=min(z[1] for z in zeros)
    c=sum(math.exp(-abs(z)**2)*abs(f.deriv(m)(z)/math.factorial(m))**2*math.factorial(m)*c_laguerre(m) for z,mult in zeros if mult==m)
    return m,c,zeros

def local_volume(coeff,q,R=7.,nr=160,na=140):
    f,zeros=root_data(coeff)
    from numpy.polynomial.legendre import leggauss
    xx,ww=leggauss(nr); th=np.arange(na)*2*np.pi/na
    rr=(xx+1)*R/2; rw=ww*R/2
    total=0.
    for z,m in zeros:
        w=rr[:,None]*np.exp(1j*th[None,:])
        x=z+np.sqrt(q)*w
        s=np.zeros_like(x.real)
        for l in range(len(coeff)):
            s+=(-q)**l/math.factorial(l)*abs(f.deriv(l)(x))**2
        j=(-s).clip(min=0)*np.exp(-abs(x)**2/(1+q))
        total+=float((j*rr[:,None]*rw[:,None]).sum()*2*np.pi/na)*q/(np.pi*(1+q))
    return total

def main():
    rng=np.random.default_rng(2026)
    points=[0, .3+.7j, -.23+0.11j, 1.3-1.2j]
    cases=[]
    for n in range(1,6):
        for case in range(6):
            coeff=normalized(rng.normal(size=n+1)+1j*rng.normal(size=n+1))
            for eta in [0,.4,.50001,.62,.91,1]:
                for beta in points:
                    a=exact_poly(coeff,eta,beta);b=direct_wigner(coeff,eta,beta)
                    assert abs(a-b)<1e-9*(1+abs(a)+abs(b)),(n,eta,beta,a,b)
                    cases.append(1)
    print('exact_fock_kraus_vs_stellar_grid',len(cases))
    one=normalized([0,1]);two=normalized([0,0,1]);squarefree=normalized([1,0,1]);quad=normalized([0,0,-math.sqrt(2),math.sqrt(6)])
    for name,coeff in [('one',one),('two',two),('squarefree',squarefree),('mixed_root',quad)]:
        m,c,zeros=predicted(coeff)
        print(name,'order',m+1,'coefficient',c,'zeros',zeros)
        for q in ([.008,.002,.0005] if m==1 else [.005,.001,.0003]):
            v=local_volume(coeff,q)
            ratio=v/(c*q**(m+1))
            print('q',q,'observed/predicted',ratio)
            assert ratio>.55 and ratio<1.5,(name,q,ratio)
    print('VERIFY_OK independent_Kraus_Wigner=720 local_stellar_asymptotics=12')
if __name__=='__main__':main()
