"""Reproducible numerical checks for a Poisson-weighted sharp L1 extremal.
The proof of the theorem is analytic; finite checks are supplementary.
Requires mpmath>=1.3.
"""
import mpmath as mp
mp.mp.dps = 35
checks=0

def ok(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def poisson(r, t):
    return (1-r*r)/(1-2*r*mp.cos(t)+r*r)

def F(r,c):
    return mp.quad(lambda t: poisson(r,t)*abs(1-c*mp.e**(1j*t)), [0,mp.pi])/mp.pi

def moments(r,c):
    val=F(r,c)
    def moment(k):
        def fun(x):
            g=mp.e**(1j*x)-c*mp.e**(-1j*x)
            phi=-mp.conj(g)/(val*abs(g))
            return poisson(r,2*x)*phi*mp.e**(-1j*k*x)/(2*mp.pi)
        return mp.quad(fun,[-mp.pi,-mp.pi/2,0,mp.pi/2,mp.pi])
    return [moment(k) for k in [-1,0,1]]

for r_text in ['0.1','0.25','0.5','0.75','0.9']:
    r=mp.mpf(r_text);c=2*r/(1+r*r);h=(1-r)/(1+r)
    f=F(r,c)
    ok(0<c<1, 'admissible optimum')
    ok(f>0,'positive exact distance')
    # Direct first-order condition, independent of involution proof
    deriv=mp.quad(lambda t:poisson(r,t)*(c-mp.cos(t))/abs(1-c*mp.e**(1j*t)),[0,mp.pi])/mp.pi
    ok(abs(deriv)<mp.mpf('1e-23'),'stationarity')
    for delta in [mp.mpf('0.006'), mp.mpf('0.03')]:
        ok(F(r,c+delta)>f,'strict local lower competitor')
        ok(F(r,c-delta)>f,'strict local upper competitor')
    # Independent complete elliptic third-kind representation.
    m=-4*c/(1-c)**2;n=-4*r/(1-r)**2
    elliptic=2*(1-r*r)*(1-c)/(mp.pi*(1-r)**2) * ((m/n)*mp.ellipk(m)+(1-m/n)*mp.ellippi(n,m))
    ok(abs(elliptic-f)<mp.mpf('1e-23'),'elliptic identity')
    minus,zero,plus=moments(r,c)
    ok(abs(minus+1)<mp.mpf('1e-22'),'target moment')
    ok(abs(zero)<mp.mpf('1e-22'),'zero mean moment')
    ok(abs(plus)<mp.mpf('1e-22'),'zero first moment')
    # Tangent-half-angle involution identity at sampled positive u
    for us in ['0.13','0.65','1.7']:
        u=mp.mpf(us)
        def I(u):
            return (u*u-h*h)/((u*u+h*h)*mp.sqrt(1+u*u)*mp.sqrt(u*u+h**4))
        ok(abs(I(u)+(h*h/u**2)*I(h*h/u))<mp.mpf('1e-28'),'involution')
print('CHECK_OK',checks)
