"""Standalone numerical cross-checks for exact Gaussian-preserving Strang rotation/OU splitting."""
import math


def rates(h, lam):
    p = math.exp(-2 * h)
    r = math.exp(-2 * lam * h)
    k = math.exp(-4 * h)
    a = (1 + k) * p / 2
    b = (1 - k) * math.sqrt(p*r) / 2
    d = (1 + k) * r / 2
    rho = (a+d+math.hypot(a-d,2*b))/2
    return a,b,d,rho,k*math.sqrt(p*r)


def direct_quadrature(h,lam,vector):
    # Integrate the Gaussian angle directly, not through its characteristic function.
    x,y=vector
    x *= math.exp(-h/2)
    y *= math.exp(-lam*h/2)
    n=3000; lo=-9.; hi=9.; dz=(hi-lo)/n
    a=math.exp(-h/2); b=math.exp(-lam*h/2)
    outx=outy=outxy=0.
    for i in range(n+1):
        z=lo+i*dz; theta=(2*h)**.5*z
        u=a*(math.cos(theta)*x-math.sin(theta)*y)
        v=b*(math.sin(theta)*x+math.cos(theta)*y)
        w=math.exp(-z*z/2)/math.sqrt(2*math.pi) * (1 if i in (0,n) else (4 if i%2 else 2))
        outx+=w*u*u;outy+=w*v*v;outxy+=w*u*v
    return tuple(dz*t/3 for t in (outx,outy,outxy))


def matrix_power_vector(a,b,d,n,v):
    x,y=v
    for _ in range(n):x,y=a*x+b*y,b*x+d*y
    return x+y


def run():
    tests=0
    for h in (.01,.05,.2,.7,2.,4.):
        for lam in (.001,.05,.3,1.):
            a,b,d,rho,off=rates(h,lam)
            assert 0<off<rho<1+1e-12 and a*d-b*b>0
            p=math.exp(-2*h);r=math.exp(-2*lam*h); k=math.exp(-4*h)
            assert abs((a*d-b*b)-k*p*r)<1e-12
            for v in ((1.,0.),(0.,1.),(.9,-.4)):
                obs=direct_quadrature(h,lam,v)
                x,y=v; pred=(a*x*x+b*y*y,b*x*x+d*y*y,k*math.sqrt(p*r)*x*y)
                assert max(abs(u-w) for u,w in zip(obs,pred))<8e-10,(h,lam,obs,pred)
                for n in (0,1,3,10,30):
                    assert matrix_power_vector(a,b,d,n,(x*x,y*y)) <= math.sqrt(2)*rho**n*(x*x+y*y)*(1+1e-10)
                    tests+=1
            tests+=4
        # Monotonicity in lambda: the worst case is the vanishing-curvature endpoint.
        earlier=[rates(h,l)[3] for l in (0,.001,.05,.3,1.)]
        assert all(earlier[i]>earlier[i+1] for i in range(len(earlier)-1))
        tests+=1
    g=(3-math.sqrt(5))
    assert abs((1-rates(1e-6,0)[3])/1e-6-g)<1e-5
    assert abs(rates(12.,0)[3]-.5)<1e-9
    for h in (.02,.2,1.,4.):
        assert abs(rates(h,1)[3]-math.exp(-2*h))<1e-12
        tests+=1
    print('PASS:',tests,'quadrature, spectral, coupling, and uniformity checks')

if __name__=='__main__':run()
