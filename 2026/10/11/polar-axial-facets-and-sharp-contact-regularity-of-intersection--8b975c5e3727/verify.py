"""Independent quadrature checks for cylindrical central-section facet contact."""
from mpmath import mp

mp.dps = 65

def kappa(k):
    return mp.pi**(mp.mpf(k)/2)/mp.gamma(mp.mpf(k)/2+1)

def formula(n,R,h,theta):
    theta0=mp.atan(h/R)
    if theta <= theta0:
        return kappa(n-1)*R**(n-1)/mp.cos(theta)
    top=h*mp.cot(theta)
    return 2*kappa(n-2)/mp.cos(theta)*mp.quad(lambda x:(R**2-x**2)**(mp.mpf(n-2)/2),[0,top])

def cap(n,R,h,theta):
    theta0=mp.atan(h/R)
    if theta<=theta0:return mp.mpf(0)
    delta=R-h*mp.cot(theta)
    # variable y=R-x to resolve very thin cap without cancellation
    return 2*kappa(n-2)/mp.cos(theta)*mp.quad(lambda y:(y*(2*R-y))**(mp.mpf(n-2)/2),[0,delta])

def coefficient(n,R,h):
    theta0=mp.atan(h/R)
    return 4*kappa(n-2)/n/mp.cos(theta0)*(2*R)**(mp.mpf(n-2)/2)*((R**2+h**2)/h)**(mp.mpf(n)/2)

def polar_area_3d(R,h,theta):
    # Independently integrate the squared radial reach in section-plane polar coordinates.
    st=mp.sin(theta)
    if st==0: return mp.pi*R**2
    c0=h/(st*mp.sqrt(R**2+h**2))
    a=mp.acos(c0) if c0<1 else mp.mpf(0)
    def first(phi):return h**2/(st**2*mp.cos(phi)**2)
    def second(phi):return R**2/(1-st**2*mp.cos(phi)**2)
    return 2*(mp.quad(first,[0,a]) if a>0 else 0)+2*mp.quad(second,[a,mp.pi/2])

cases=0
max_ref=mp.mpf(0)
max_cap=mp.mpf(0)
for n in range(3,13):
    for R,h in [(mp.mpf(1),mp.mpf(1)),(mp.mpf('1.3'),mp.mpf('.7')),(mp.mpf('.9'),mp.mpf('2.1'))]:
        t0=mp.atan(h/R)
        A=kappa(n-1)*R**(n-1)
        for t in [t0*mp.mpf('.1'),t0*mp.mpf('.8'),t0,(t0+mp.pi/2)/2,t0+(mp.pi/2-t0)*mp.mpf('.9')]:
            q=formula(n,R,h,t)
            missing=cap(n,R,h,t)
            comparison=A/mp.cos(t)-missing
            err=abs(q-comparison)/max(abs(q),1)
            max_ref=max(max_ref,err)
            assert err<mp.mpf('1e-58'),(n,err)
            cases+=1
        for d in [mp.mpf('1e-5'),mp.mpf('1e-8')]:
            err=abs(cap(n,R,h,t0+d)/d**(mp.mpf(n)/2)/coefficient(n,R,h)-1)
            max_cap=max(max_cap,err)
            assert err<mp.mpf('0.003'),(n,R,h,d,err)
            cases+=1

for n in range(3,13):
    for R,h in [(mp.mpf(1),mp.mpf(1)),(mp.mpf('1.3'),mp.mpf('.7'))]:
        A=kappa(n-1)*R**(n-1)
        t0=mp.atan(h/R)
        r0=A*h/R
        C_r=4*kappa(n-2)/n*(2*R)**(mp.mpf(n-2)/2)*(R/r0)**(mp.mpf(n)/2)
        for eps in [mp.mpf('1e-9'),mp.mpf('1e-11')]:
            th=t0+eps
            c=cap(n,R,h,th)
            r=A*mp.tan(th)-c*mp.sin(th)
            z=A-c*mp.cos(th)
            err=abs((A-z)/(r-r0)**(mp.mpf(n)/2)/C_r-1)
            assert err<mp.mpf('0.001'),(n,R,h,err)
            cases+=1

# Noncircular smooth base: anisotropic ellipse contact, tested in two normal directions.
for a,b,h in [(mp.mpf('1.7'),mp.mpf('.9'),mp.mpf('.6')),(mp.mpf('2.2'),mp.mpf('1.4'),mp.mpf('1.1'))]:
    V=mp.pi*a*b
    for phi in [mp.mpf('0.2'),mp.mpf('.9')]:
        H=mp.sqrt((a*mp.cos(phi))**2+(b*mp.sin(phi))**2)
        gauss_curvature=H**3/(a*a*b*b)
        r0=h*V/H
        th0=mp.atan(h/H)
        C=2**(mp.mpf(5)/2)*kappa(1)/3/mp.sqrt(gauss_curvature)*(H**2/(h*V))**(mp.mpf(3)/2)
        for eps in [mp.mpf('1e-9'),mp.mpf('1e-11')]:
            th=th0+eps
            cutoff=h*mp.cot(th)/H
            # independent affine-disk cap formula, not the general geometric cap lemma.
            z=4*a*b*mp.quad(lambda s:mp.sqrt(1-s*s),[0,cutoff])
            r=z*mp.tan(th)
            err=abs((V-z)/(r-r0)**(mp.mpf(3)/2)/C-1)
            assert err<mp.mpf('.001'),(a,b,phi,eps,err)
            cases+=1

for R,h in [(mp.mpf(1),mp.mpf(1)),(mp.mpf('1.5'),mp.mpf('.6'))]:
    t0=mp.atan(h/R)
    for t in [t0*mp.mpf('.5'),t0*mp.mpf('.9'),t0+mp.mpf('.02'),(t0+mp.pi/2)/2]:
        geom=polar_area_3d(R,h,t)
        q=formula(3,R,h,t)
        assert abs(geom-q)<mp.mpf('1e-54')*max(1,q),(R,h,t,geom,q)
        cases+=1

print('VERIFY_OK', 'cases='+str(cases),'max_slicing_relative_error='+mp.nstr(max_ref,8),'max_cap_coefficient_relative_error='+mp.nstr(max_cap,8))
