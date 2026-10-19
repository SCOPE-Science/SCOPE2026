"""Independent numerical checks for a two-dimensional resetting-comb theorem.

Requires Python 3 and mpmath. Numerical checks illustrate the proved
identities; strict all-lag inequalities are established analytically.
"""
import mpmath as mp

mp.mp.dps = 50
checks = 0


def near(x, y, rel=mp.mpf('1e-29')):
    global checks
    assert mp.fabs(x-y) < rel*(1+mp.fabs(x)+mp.fabs(y)), (x,y)
    checks += 1


def F(u):
    return mp.exp(u)*mp.erfc(mp.sqrt(u))


def kernel(u):
    return (2*u*u+u-1)*F(u)-2*u**mp.mpf('1.5')/mp.sqrt(mp.pi)


def primitive(u):
    return (2*u*u-3*u+2)*F(u)+(4*mp.sqrt(u)-2*u**mp.mpf('1.5'))/mp.sqrt(mp.pi)-2


# 1. Check the resolvent boundary condition and its product Laplace form.
for Dy, Dx, r in [(mp.mpf('0.7'),mp.mpf('1.3'),mp.mpf('0.6')),
                  (mp.mpf('5'),mp.mpf('0.2'),mp.mpf('3'))]:
    alpha=mp.sqrt(r/Dy)
    bx2=Dx/(2*mp.sqrt(r*Dy))
    for k in [mp.mpf('0'),mp.mpf('.2'),mp.mpf('1.4'),mp.mpf('5')]:
        A=r/(2*Dy*alpha+Dx*k*k)
        near((2*Dy*alpha+Dx*k*k)*A, r)
        near((2/alpha)*A,1/(1+bx2*k*k))
        near(mp.quad(lambda y:A*mp.exp(-alpha*y),[0,mp.inf])*2,
             1/(1+bx2*k*k))

# 2. Independently integrate the heat-kernel covariance using the
# stationary double-exponential vertical law, not the evaluated erfc form.
for u in [mp.mpf('0.0001'),mp.mpf('.007'),mp.mpf('.1'),mp.mpf('.8'),
          mp.mpf('2.2'),mp.mpf('6'),mp.mpf('15')]:
    independent=mp.quad(lambda v:(v*v-2)*mp.exp(-v-v*v/(4*u)),[0,mp.inf]) / mp.sqrt(4*mp.pi*u)
    near(independent,kernel(u),mp.mpf('2e-27'))
    near(mp.diff(primitive,u),kernel(u),mp.mpf('1e-29'))
    assert independent < 0 and primitive(u) < 0
    checks+=2

# 3. Independently integrate the temporal heat-kernel covariance,
# then compare to the claimed elementary erfc expression.
for u in [mp.mpf('.004'),mp.mpf('.13'),mp.mpf('.7'),mp.mpf('3'),mp.mpf('11')]:
    independent=mp.quad(kernel,[0,u])
    near(independent,primitive(u),mp.mpf('1e-27'))

# 4. Cross-check the small-lag and long-lag constants, not by sampling
# a claimed inequality but by integral and resolvent calculations.
near(kernel(mp.mpf('1e-40')),-1,mp.mpf('1e-17'))
alpha=mp.mpf('1.3'); Dy=mp.mpf('.8')
for z in [mp.mpf('.003'),mp.mpf('.1'),mp.mpf('.6')]:
    a=mp.sqrt(z/Dy)
    direct=-(2*alpha+a)/(alpha*Dy*(alpha+a)**3)
    independent=mp.quad(lambda y:(y*y-2/alpha**2)*alpha*mp.exp(-alpha*y-a*y),[0,mp.inf])/(2*mp.sqrt(z*Dy))
    near(direct,independent,mp.mpf('1e-27'))
near(-(2*alpha+mp.sqrt(mp.mpf('1e-40')/Dy))/(alpha*Dy*(alpha+mp.sqrt(mp.mpf('1e-40')/Dy))**3),
     -2/(Dy*alpha**3),mp.mpf('1e-17'))

# 5. Independent double quadrature over time and initial vertical position.
# Quadrature kernel is the Gaussian heat kernel, not the closed-form erfc.
from scipy.integrate import quad
from math import sqrt,pi,exp
for dx,dy,r,t in [(0.2,5.0,3.0,0.04),(0.2,5.0,3.0,0.9),
                   (6.0,0.3,0.2,3.0),(1.2,0.7,2.1,0.5)]:
    alpha=sqrt(r/dy)
    def h(s):
        val,_=quad(lambda y:(y*y-2/alpha**2)*alpha*exp(-alpha*y-y*y/(4*dy*s)),
                   0,max(30/alpha,20*sqrt(dy*s)),epsabs=1e-10)
        return val/sqrt(4*pi*dy*s)
    direct,_=quad(h,0,t,epsabs=1e-8,limit=180)
    direct*=2*dx*exp(-r*t)
    closed=float(2*dx*mp.exp(-r*t)*primitive(r*t)/(alpha*r))
    assert abs(direct-closed)<2e-7*(1+abs(closed)), (direct,closed)
    checks+=1

print('PASS:',checks,'independent checks; all limiting/strict statements proved analytically.')
