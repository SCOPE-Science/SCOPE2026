"""Self-contained numerical checks of exact planar Haar sketch laws."""
import math, cmath, random

def li2(z):
    acc=0.0; p=z
    for n in range(1,10000):
        a=p/(n*n); acc+=a
        if abs(a)<1e-16: break
        p*=z
    return acc

def factor(t,phi):
    return 1+1j*t*(1-cmath.exp(1j*phi))

def check():
    for t in (.05,.2,.5,1.,2.5,7.):
        n=16384
        arr=[factor(t,2*math.pi*(k+.5)/n) for k in range(n)]
        mean=sum(arr)/n
        mean2=sum(abs(z)**2 for z in arr)/n
        logs=[cmath.log(z) for z in arr]
        ell=sum(logs)/n
        var_x=sum((v.real-ell.real)**2 for v in logs)/n
        var_y=sum((v.imag-ell.imag)**2 for v in logs)/n
        cov=sum((v.real-ell.real)*(v.imag-ell.imag) for v in logs)/n
        target=.5*li2(t*t/(1+t*t))
        assert abs(mean-(1+1j*t))<2e-13,(t,mean)
        assert abs(mean2-(1+2*t*t))<2e-12,(t,mean2)
        assert abs(ell-cmath.log(1+1j*t))<2e-13,(t,ell)
        assert abs(var_x-target)<2e-12,(t,var_x,target)
        assert abs(var_y-target)<2e-12,(t,var_y,target)
        assert abs(cov)<2e-12,(t,cov)
        lo=(math.sqrt(1+t*t)-t)**2
        hi=(math.sqrt(1+t*t)+t)**2
        assert all(lo-1e-12<=abs(z)**2<=hi+1e-12 for z in arr)
    # Direct real two-dimensional update equals complex multiplier formula.
    for k in range(400):
        phi=(k+.17)*2*math.pi/400
        z=cmath.exp(1j*(k*.137))*(1+k/300)
        theta=cmath.phase(z)+phi/2
        u=complex(math.cos(theta),math.sin(theta))
        h=.3
        projected=2*h * ((u.conjugate()*1j*z).real)*u
        z2=z+projected
        m=factor(h,phi)
        assert abs(z2-z*m)<1e-12,(z2,z*m)
    # Exact path product and arithmetic vs logarithmic radial moment demonstration.
    rng=random.Random(426)
    t=.35; N=45; reps=6000
    ls=[]; r2=0.; zmean=0j
    for _ in range(reps):
        z=1+0j
        for j in range(N):
            p=2*math.pi*rng.random()
            z*=factor(t,p)
        ls.append(math.log(abs(z)))
        r2+=abs(z)**2
        zmean+=z
    target=N*.5*math.log(1+t*t)
    s2=sum((v-target)**2 for v in ls)/reps
    v=N*.5*li2(t*t/(1+t*t))
    assert abs(sum(ls)/reps-target)<5*math.sqrt(v/reps)
    assert abs(s2-v)<.12*v
    # Finite-time compensated (gain two) physical-time RMS error coefficient.
    omega=1.3; T=.7
    for h in (.02,.01,.005,.0025):
        steps=int(T/h)
        y=omega*h
        mean=(1+1j*y)**steps
        true=cmath.exp(1j*y*steps)
        mse=(1+2*y*y)**steps+1-2*(mean/true).real
        assert abs(mse/h-omega*omega*(steps*h))<.10, (h,mse/h)
        # Every 2x2 real shear in the model has determinant one.
        for j in range(100):
            theta=2*math.pi*j/100
            a,b=math.cos(theta),math.sin(theta)
            A00=1-2*y*a*b; A01=-2*y*a*a
            A10=2*y*b*b; A11=1+2*y*a*b
            assert abs(A00*A11-A01*A10-1)<2e-14
    print('PASS: 6 angular quadratures x 6 moments; 400 direct updates; 6000 paths; 400 determinants; 4 finite-time error checks')
    print('t=.35 45-step sample-mean log radius',sum(ls)/reps,'theory',target,'sample variance',s2,'theory',v)

if __name__=='__main__':check()
