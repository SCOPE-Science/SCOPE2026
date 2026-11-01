"""Independent finite checks for a ball-spindle illumination volume law.
Run: python verify.py. This checks integrals and endpoint rates, not an infinite proof.
"""
import math
import mpmath as mp
mp.mp.dps = 45

def kappa(n):
    return mp.pi**(mp.mpf(n)/2)/mp.gamma(mp.mpf(n)/2+1)

def profile(n,R,r,alpha):
    R=mp.mpf(R);r=mp.mpf(r);a=mp.mpf(alpha);c=R-r
    s=c*mp.cos(a)+mp.sqrt(R*R-c*c*mp.sin(a)**2)
    q=-r*mp.cos(a)
    f=lambda z: max(mp.mpf('0'),r*r-z*z)**(mp.mpf(n-1)/2)
    g=lambda z: max(mp.mpf('0'),mp.sqrt(max(mp.mpf('0'),R*R-(z-c*mp.cos(a))**2))-c*mp.sin(a))**(n-1)
    # Use quadrature in x, with endpoints away from floating cancellation.
    v=kappa(n-1)*(mp.quad(f,[-r,q])+mp.quad(g,[q,s]))
    return s,v

def area_two_dim(R,r,alpha):
    R=mp.mpf(R);r=mp.mpf(r);c=R-r;a=mp.mpf(alpha)
    s=c*mp.cos(a)+mp.sqrt(R*R-c*c*mp.sin(a)**2)
    beta=mp.asin(c*mp.sin(a)/R)
    return r*r*a+R*R*(mp.pi-a-beta)-c*s*mp.sin(a)

def T(n,R,r):
    c=R-r
    return c*(n-1)*kappa(n-1)*R**(n-1)*mp.beta(mp.mpf('0.5'),mp.mpf(n)/2)

checks=0
for n in (2,3,4,6):
    for R,r in ((mp.mpf(2),mp.mpf(1)),(mp.mpf(5)/2,mp.mpf(1)/2)):
        prev=kappa(n)*r**n-mp.mpf('1e-20')
        for a in (mp.pi,mp.pi*mp.mpf('0.82'),mp.pi/2,mp.pi/3,mp.pi*mp.mpf('0.1'),mp.mpf(0)):
            s,v=profile(n,R,r,a)
            assert r-mp.mpf('1e-30') <= s <= 2*R-r+mp.mpf('1e-30')
            assert v>prev
            prev=v
            checks+=2
            if n==2:
                assert abs(v-area_two_dim(R,r,a))<mp.mpf('1e-27')*R**2
                checks+=1
        assert abs(prev-kappa(n)*R**n)<mp.mpf('1e-27')
        checks+=1
        a=mp.mpf('0.006')
        s,v=profile(n,R,r,a)
        delta_star=kappa(n)*(R**n-r**n)
        gap=delta_star-(v-kappa(n)*r**n)
        assert abs(gap/(T(n,R,r)*a)-1)<mp.mpf('0.025')
        h=(2*R-r)-s
        H2=(R-r)*(2*R-r)/(2*R)
        assert abs(h/(H2*a*a)-1)<mp.mpf('0.025')
        checks+=2
        a=mp.pi-mp.mpf('0.002')
        s,v=profile(n,R,r,a)
        delta=v-kappa(n)*r**n
        d_n=(mp.mpf('0.5')*(n*(n+1)/kappa(n-1))**(mp.mpf(2)/(n+1))
             *((R-r)/(r*R))**(mp.mpf(n-1)/(n+1)))
        assert abs((s-r)/(d_n*delta**(mp.mpf(2)/(n+1)))-1)<mp.mpf('0.025')
        checks+=1
print('passed',checks,'finite checks; n=2,3,4,6, two radius pairs')
