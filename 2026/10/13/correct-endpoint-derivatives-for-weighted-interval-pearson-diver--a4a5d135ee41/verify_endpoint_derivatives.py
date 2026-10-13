from mpmath import mp

mp.dps = 50

# Example: X~Exp(lx), Y~Exp(ly), truncated to (a,b).
lx = mp.mpf('1.3')
ly = mp.mpf('0.7')
a = mp.mpf('0.5')
b = mp.mpf('2.0')

Fx = lambda x: 1-mp.e**(-lx*x)
Fy = lambda x: 1-mp.e**(-ly*x)
fx = lambda x: lx*mp.e**(-lx*x)
gy = lambda x: ly*mp.e**(-ly*x)

def stats(a,b):
    dF = Fx(b)-Fx(a); dG = Fy(b)-Fy(a)
    p = lambda x: fx(x)/dF
    q = lambda x: gy(x)/dG
    D = mp.quad(lambda x: x*q(x)*(1-p(x)/q(x))**2,[a,b])
    MX = mp.quad(lambda x: x*p(x),[a,b])
    MY = mp.quad(lambda x: x*q(x),[a,b])
    h1x,h1y = p(a),q(a)
    h2x,h2y = p(b),q(b)
    da = (2*h1x-h1y)*D + 2*(h1x-h1y)*(MX-MY) - a*(h1x-h1y)**2/h1y
    db = (h2y-2*h2x)*D + 2*(h2y-h2x)*(MX-MY) + b*(h2x-h2y)**2/h2y
    return D,MX,MY,da,db

D,MX,MY,da,db=stats(a,b)
eps=mp.mpf('1e-6')
fd_a=(stats(a+eps,b)[0]-stats(a-eps,b)[0])/(2*eps)
fd_b=(stats(a,b+eps)[0]-stats(a,b-eps)[0])/(2*eps)
assert abs(da-fd_a) < mp.mpf('1e-10')
assert abs(db-fd_b) < mp.mpf('1e-10')

# Null-model check: for X=Y, D is identically zero, but the published
# formulas (14)-(15) reduce to h1*(1-a) and h2*(b-1), respectively.
# At a=1/2 and b=2 these are nonzero for any positive endpoint density.
ln=mp.mpf('1.0')
Fn=lambda x: 1-mp.e**(-ln*x)
fn=lambda x: ln*mp.e**(-ln*x)
delta=Fn(b)-Fn(a)
h1=fn(a)/delta; h2=fn(b)/delta
published_da=h1*(1-a)
published_db=h2*(b-1)
assert published_da != 0
assert published_db != 0

print('D=', mp.nstr(D,20))
print('correct_da=', mp.nstr(da,20), 'finite_difference=', mp.nstr(fd_a,20))
print('correct_db=', mp.nstr(db,20), 'finite_difference=', mp.nstr(fd_b,20))
print('null_published_da=', mp.nstr(published_da,20))
print('null_published_db=', mp.nstr(published_db,20))
