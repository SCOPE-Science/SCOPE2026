"""Reproduce numerical checks for a gamma-mixture Fourier noncancellation theorem.

Run: python check.py (requires mpmath>=1.3.0).
The theorem is proved analytically; these tests do not establish universal claims.
"""
import mpmath as mp
mp.mp.dps = 85

def components(shape, a, b, t):
    v = (mp.mpf(a)/(a-1j*t))**shape
    w = (mp.mpf(b)/(b-1j*t))**shape
    return v,w

def admissible_zeros(shape,a,b):
    th = 2*mp.atan(mp.sqrt(b/a))-mp.pi/2
    q=0; out=[]
    while (2*q+1)*mp.pi/shape <= th:
        phi=(2*q+1)*mp.pi/shape
        c=(b-a)/mp.tan(phi)
        delta=c*c-4*a*b
        if delta < -mp.mpf('1e-65'):
            raise AssertionError('inconsistent discriminant')
        delta=max(mp.mpf(0),delta)
        for t in ([c/2] if delta==0 else [(c-mp.sqrt(delta))/2,(c+mp.sqrt(delta))/2]):
            A=(a/mp.sqrt(a*a+t*t))**shape
            B=(b/mp.sqrt(b*b+t*t))**shape
            weight=B/(A+B)
            out.append((q,t,weight))
        q+=1
    return sorted(out,key=lambda z:z[1])

def analytic_margin(shape,a,b):
    th=2*mp.atan(mp.sqrt(b/a))-mp.pi/2
    return mp.cos(min(shape*th,mp.pi)/2)

cases = [(mp.mpf('0.75'),mp.mpf(1),mp.mpf(3)),
         (mp.mpf('1.7'),mp.mpf(2),mp.mpf(19)),
         (mp.mpf(2),mp.mpf(1),mp.mpf(100)),
         (mp.mpf(3),mp.mpf(1),mp.mpf(10)),
         (mp.mpf(3),mp.mpf(1),mp.mpf(25)),
         (mp.mpf(5),mp.mpf(1),mp.mpf(50)),
         (mp.mpf(8),mp.mpf(1),mp.mpf(1000))]

for shape,a,b in cases:
    t0=mp.sqrt(a*b)
    A=(a/mp.sqrt(a*a+t0*t0))**shape
    B=(b/mp.sqrt(b*b+t0*t0))**shape
    w0=B/(A+B)
    z1,z2=components(shape,a,b,t0)
    actual=abs(w0*z1+(1-w0)*z2)/(w0*abs(z1)+(1-w0)*abs(z2))
    bound=analytic_margin(shape,a,b)
    assert actual+mp.mpf('1e-55')>=bound
    if bound>mp.mpf('1e-30'):
        assert abs(actual-bound)<mp.mpf('1e-65'),(shape,a,b,actual,bound)
    else:
        assert bound<=mp.mpf('1e-30')
    zeros=admissible_zeros(shape,a,b)
    last_w=mp.mpf(0)
    for k,t,weight in zeros:
        x,y=components(shape,a,b,t)
        value=weight*x+(1-weight)*y
        assert abs(value)<mp.mpf('1e-60'),(shape,t,value)
        assert weight>last_w
        last_w=weight
        # Numerically verify the nonzero radial derivative of the ratio.
        deriv=shape*t*(1/(a*a+t*t)-1/(b*b+t*t))
        assert deriv>0
    assert not (shape<=2 and zeros)
    if zeros: assert bound<mp.mpf('1e-30')
    print('shape',mp.nstr(shape,5),'rates',mp.nstr(a,5),mp.nstr(b,5),
          'sharp-margin',mp.nstr(bound,17),'positive-zero-weights',len(zeros))

# Three direct defining-integral comparisons: integral over [0,infinity)
for shape,a,b,t,weight in [
    (mp.mpf(3),mp.mpf(1),mp.mpf(25),mp.mpf('2.132371706962789632512'),mp.mpf('.9281768210986407057582')),
    (mp.mpf('1.7'),mp.mpf(2),mp.mpf(19),mp.mpf('3.2'),mp.mpf('.42')),
    (mp.mpf('2.5'),mp.mpf(1),mp.mpf(6),mp.mpf('0.7'),mp.mpf('.6'))]:
    def gd(rate,xx): return rate**shape*xx**(shape-1)*mp.exp(-rate*xx)/mp.gamma(shape)
    val=mp.quad(lambda x:(weight*gd(a,x)+(1-weight)*gd(b,x))*mp.exp(1j*t*x),[0,1,3,10,40,120])
    z1,z2=components(shape,a,b,t)
    cf=weight*z1+(1-weight)*z2
    err=abs(val-cf)
    print('integral check shape',mp.nstr(shape,3),'t',mp.nstr(t,6),'abs_error',mp.nstr(err,7))
    assert err<mp.mpf('1e-35')

# The m=3 transition is exact: r_c = (2+sqrt(3))^2.
rcrit=mp.tan(mp.pi/4+mp.pi/6)**2
assert abs(rcrit-(2+mp.sqrt(3))**2)<mp.mpf('1e-80')
shape=mp.mpf(3); a=mp.mpf(1); b=rcrit
t0=mp.sqrt(a*b)
w0=b**(shape/2)/(a**(shape/2)+b**(shape/2))
p,q=components(shape,a,b,t0)
assert abs(w0*p+(1-w0)*q)<mp.mpf('1e-75')
print('exact m=3 critical rate ratio',mp.nstr(rcrit,28),
      'double-root-in-phase t',mp.nstr(t0,24),'weight',mp.nstr(w0,24))

# Check linear vanishing of the sharp stability margin from the zero-free side.
slope=shape/(2*mp.sqrt(rcrit)*(1+rcrit))
for eps in [mp.mpf('1e-5'),mp.mpf('1e-7'),mp.mpf('1e-9')]:
    observed=analytic_margin(shape,mp.mpf(1),rcrit-eps)/eps
    assert abs(observed/slope-1)<mp.mpf('1e-4')
    print('boundary slope, eps',mp.nstr(eps,5),'observed',mp.nstr(observed,23))
print('ALL CHECKS PASSED')
