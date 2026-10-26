"""Independent finite-degree checks of two-line intensity-jet formulas."""
import math
import numpy as np

def intensity_jets(a,phi):
    c=np.r_[1.+0j,np.asarray(a, dtype=complex)]
    n=len(a)
    return np.array([sum((c[j]*c[k-j].conjugate()*np.exp(1j*(2*j-k)*phi) for j in range(k+1))).real for k in range(1,n+1)])

def reconstruct(y0,y1,theta):
    n=len(y0); c=np.zeros(n+1,dtype=complex);c[0]=1
    for k in range(1,n+1):
        t=[]
        for phi,y in [(0.,y0[k-1]),(theta,y1[k-1])]:
            cross=sum((c[j]*c[k-j].conjugate()*np.exp(1j*(2*j-k)*phi) for j in range(1,k)))
            t.append((y-cross.real)/2)
        x=t[0]; v=(x*math.cos(k*theta)-t[1])/math.sin(k*theta)
        c[k]=x+1j*v
    return c[1:]

def jacobian_spectrum(n,theta):
    a=[]
    for k in range(1,n+1):
        M=2*np.array([[1.,0.],[math.cos(k*theta),-math.sin(k*theta)]])
        a+=list(np.linalg.svd(M,compute_uv=False))
    return min(a)

def main():
    rng=np.random.default_rng(1907)
    tests=0
    for n in range(1,19):
        p=next(k for k in range(1,n+1) if math.gcd(k,n+1)==1)
        theta=math.pi*p/(n+1)
        a=rng.normal(size=n)+1j*rng.normal(size=n)
        r=reconstruct(intensity_jets(a,0),intensity_jets(a,theta),theta)
        assert np.max(np.abs(r-a)) < 1e-6, (n,np.max(np.abs(r-a)))
        sval=jacobian_spectrum(n,theta)
        target=2*math.sqrt(1-math.cos(math.pi/(n+1)))
        assert abs(sval-target)<1e-10,(n,sval,target)
        product=math.prod(abs(math.sin(k*theta)) for k in range(1,n+1))
        assert abs(product-(n+1)/2**n)<1e-10,(n,product)
        tests+=3
    # For each N a compact grid of angles, no other angle beats the theoretical bound.
    for n in range(1,13):
        best=2*math.sqrt(1-math.cos(math.pi/(n+1)))
        for theta in np.linspace(0,math.pi,4001):
            assert jacobian_spectrum(n,theta)<=best+1e-10
            tests+=1
    # Explicit degeneracy at resonant rational angles.
    for n in range(1,13):
        k=n;theta=math.pi/k
        aa=np.zeros(n,dtype=complex);bb=np.zeros(n,dtype=complex)
        aa[k-1]=1j;bb[k-1]=-1j
        assert np.max(np.abs(intensity_jets(aa,0)-intensity_jets(bb,0)))<1e-10
        assert np.max(np.abs(intensity_jets(aa,theta)-intensity_jets(bb,theta)))<1e-10
        tests+=1
    print('PASS',tests,'deterministic checks including inverse, spectrum, optimal-angle upper bound, resonant ambiguity')
if __name__=='__main__':main()
