"""Independent numerical checks for a periodic Sobolev-kernel quadrature identity.

Requires Python 3, mpmath. Run `python verify.py`.
The theorem itself is proved analytically; these are supplementary finite checks.
"""
from mpmath import mp

mp.dps = 65
pi = mp.pi


def a_b(n):
    d = n if n % 2 == 0 else 2*n
    z = pi/d
    a = z/mp.tan(z) + z*z/3 - 1
    b = pi*pi/(3*n*n)
    return a,b


def q_zero(n):
    return mp.mpf('0.5')-n*mp.sin(2*pi/n)/(4*pi)


def gamma_threshold(n):
    a,b = a_b(n)
    q = q_zero(n)
    return n*q/(b-a-n*q*b)


def gamma_mass(n):
    a,_ = a_b(n)
    return -1/a


def density(t):
    return pi/2*abs(mp.sin(2*pi*t))


def tent_mass(n, j):
    x = mp.mpf(j)/n
    h = mp.mpf(1)/n
    pts = [-h, mp.mpf(0), h]
    for s in range(-2,4):
        t = mp.mpf(s)/2-x
        if -h < t < h:
            pts.append(t)
    pts = sorted(set(pts))
    val=mp.mpf(0)
    for lo,hi in zip(pts,pts[1:]):
        val += mp.quad(lambda u:density(x+u)*(1-n*abs(u)),[lo,hi])
    return val


def kernel(x,gamma):
    x = x % 1
    return 1+gamma*2*pi*pi*(x*x-x+mp.mpf(1)/6)


def kernel_integral(x):
    return (pi*pi/3+pi*abs(mp.sin(2*pi*x))/2
            +pi*pi/2*(4*x*x-4*x-2*abs(x-mp.mpf(1)/2)
                         +mp.mpf(1)/2-2/(pi*pi)))


def direct_weights(n, gamma):
    coords=[mp.mpf(i)/n for i in range(n)]
    mat=mp.matrix([[kernel(x-y,gamma) for y in coords] for x in coords])
    rhs=mp.matrix([1+gamma*kernel_integral(x) for x in coords])
    return list(mp.lu_solve(mat,rhs))


def exact_weights(n,gamma):
    a,b=a_b(n)
    delta=gamma*(b-a)/(1+gamma*b)
    return [tent_mass(n,j)-delta/n for j in range(n)]


checks=0
for n in range(2,13):
    a,b=a_b(n)
    assert a<0<b
    q=[tent_mass(n,j) for j in range(n)]
    assert abs(sum(q)-1)<mp.mpf('1e-55')
    assert all(x>=q[0]-mp.mpf('1e-55') for x in q)
    assert abs(q[0]-q_zero(n))<mp.mpf('1e-55')
    checks+=3
    critical=gamma_threshold(n)
    mass=gamma_mass(n)
    if n>2: assert 0<critical<mass
    else: assert abs(critical-mass)<mp.mpf('1e-55')
    checks+=1
    for factor in [mp.mpf('0.01'),mp.mpf('0.9'),mp.mpf(1),mp.mpf('1.1'),mp.mpf(10)]:
        gamma=critical*factor
        predicted=exact_weights(n,gamma)
        measured=direct_weights(n,gamma)
        assert max(abs(x-y) for x,y in zip(predicted,measured))<mp.mpf('1e-48'),(n,factor)
        assert (min(predicted)>0 if factor<1 else min(predicted)<0 if factor>1 else abs(min(predicted))<mp.mpf('1e-50'))
        checks+=2

for n in [64,128,256,512,1024,2048]:
    critical=gamma_threshold(n)
    assert abs(critical-n-pi*pi/3)<mp.mpf(20)/n
    mass=gamma_mass(n)
    d=n if n%2==0 else 2*n
    assert abs(mass/(45*d**4/pi**4)-1)<mp.mpf(2)/(d*d)
    checks+=2

for n in [101,201,401,801]:
    critical=gamma_threshold(n)
    assert abs(critical-n-pi*pi/3)<mp.mpf(200)/n
    mass=gamma_mass(n)
    d=2*n
    assert abs(mass/(45*d**4/pi**4)-1)<mp.mpf(2)/(d*d)
    checks+=2

print('PASS:', checks, 'independent finite checks')
print('n=64 weight-positivity frontier', mp.nstr(gamma_threshold(64),20))
print('n=64 constant-sign frontier', mp.nstr(gamma_mass(64),20))
print('large-N offset limit',mp.nstr(pi*pi/3,20))
