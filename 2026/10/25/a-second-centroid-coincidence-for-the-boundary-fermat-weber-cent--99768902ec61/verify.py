"""Verify the centroid-test signs and median profile for perimeter-uniform isosceles triangles."""
import mpmath as mp

mp.mp.dps = 60
mp.iv.dps = 70

def asinh_interval(x):
    return mp.iv.ln(x + mp.iv.sqrt(1 + x*x))

def B(h, q):
    """Half vertical derivative of unnormalized perimeter potential divided by h."""
    s = mp.sqrt(1+h*h)
    b = 1-q
    return (q*mp.asinh(1/(h*q)) +
            (s*(mp.sqrt(1+h*h*q*q)-h*b)-b*(mp.asinh((1+h*h*q)/(h*b))+mp.asinh(h)))/(s*s))

def B_iv(n, d):
    h = mp.iv.mpf(n) / mp.iv.mpf(d)
    q = mp.iv.mpf(1) / mp.iv.mpf(3)
    s = mp.iv.sqrt(1+h*h)
    b = 1-q
    return (q*asinh_interval(1/(h*q))+
            (s*(mp.iv.sqrt(1+h*h*q*q)-h*b)-b*(asinh_interval((1+h*h*q)/(h*b))+asinh_interval(h)))/(s*s))

for n,d in [(1,10),(1,8),(1,1),(2,1)]:
    interval = B_iv(n,d)
    print('h=',f'{n}/{d}', 'B(h,1/3) interval=',interval)

for h in [mp.mpf('0.05'),mp.mpf('0.1'),mp.mpf('0.125'),mp.mpf('1'),mp.sqrt(3),mp.mpf('2'),mp.mpf('30'),mp.mpf('1000')]:
    root=mp.findroot(lambda q:B(h,q), (mp.mpf('0.2'),mp.mpf('0.5')))
    print('h=',mp.nstr(h,20),'median y/h=',mp.nstr(root,25),'B(h,1/3)=',mp.nstr(B(h,mp.mpf(1)/3),20))

small=mp.findroot(lambda h:B(h,mp.mpf(1)/3),(mp.mpf('.10'),mp.mpf('.125')))
print('non-equilateral centroid-coincidence parameter=',mp.nstr(small,50))
for h,q in [(mp.mpf('.1'),mp.mpf('1')/3),(mp.mpf('1'),mp.mpf('1')/3),(mp.mpf('2'),mp.mpf('1')/3),(mp.mpf('3'),mp.mpf('1')/2)]:
    s=mp.sqrt(1+h*h);b=1-q
    integral=mp.quad(lambda t:(q-t)/mp.sqrt((1-t)**2+h*h*(t-q)**2),[0,q,1]);
    direct=q*mp.asinh(1/(h*q))+s*integral
    print('closed minus independent quadrature h=',mp.nstr(h,8),'err',mp.nstr(B(h,q)-direct,8))
