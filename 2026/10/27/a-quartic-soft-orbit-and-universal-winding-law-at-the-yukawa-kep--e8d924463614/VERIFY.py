"""Reproducible symbolic and numerical checks of Yukawa–Kepler cusp formulas."""
import sympy as s
import mpmath as mp

x, al, p = s.symbols('x al p', positive=True, real=True)
ac = s.exp(3)/5
H = x*(1 + al*(1+x)*s.exp(-x))
V = p/(2*x*x) - (1 + al*s.exp(-x))/x
checks = 0

def ok(condition, message):
    global checks
    assert condition, message
    checks += 1

ok(s.simplify(s.diff(H,x) - (1+al*s.exp(-x)*(1+x-x*x))) == 0, 'circular curve derivative')
for order, target in [(0,s.Rational(27,5)),(1,0),(2,0),(3,s.Rational(3,5))]:
    ok(s.simplify(s.diff(H,x,order).subs({al:ac,x:3})-target)==0, f'H order {order}')
for order in (1,2,3):
    ok(s.simplify(s.diff(V,x,order).subs({al:ac,p:s.Rational(27,5),x:3})) == 0, f'V order {order}')
ok(s.simplify(s.diff(V,x,4).subs({al:ac,p:s.Rational(27,5),x:3})-s.Rational(1,45))==0,'V fourth')
mp.mp.dps = 60
AC = mp.exp(3)/5
PH = (1+mp.sqrt(5))/2
BETA=mp.beta(mp.mpf('0.25'),mp.mpf('0.5'))

def hh(a,y):
    return y*(1+a*(1+y)*mp.exp(-y))

def hprime(a,y):
    return 1+a*mp.exp(-y)*(1+y-y*y)

for eta in [mp.mpf('0.1'),mp.mpf('0.01'),mp.mpf('0.001'),mp.mpf('0.0001')]:
    a=AC*(1+eta)
    xm=mp.findroot(lambda y:hprime(a,y),(mp.mpf('1.7'),3))
    xp=mp.findroot(lambda y:hprime(a,y),(3,mp.mpf('4.0')))
    pm,pp=hh(a,xp),hh(a,xm)
    ok(PH<xm<3<xp and pm<pp,'ordered extrema')
    ok(abs(hprime(a,xm))<mp.mpf('1e-45') and abs(hprime(a,xp))<mp.mpf('1e-45'),'fold equations')
    ok(abs((pp-pm)/eta**mp.mpf('1.5')-mp.mpf(4)/3*mp.sqrt(mp.mpf(10)/3)) < 2*mp.sqrt(eta),'cusp width scaling')
    if eta==mp.mpf('0.1'):
        q=(pm+pp)/2
        roots=[mp.findroot(lambda y:hh(a,y)-q,(mp.mpf('1.8'),mp.mpf('2.4'))),mp.findroot(lambda y:hh(a,y)-q,(3,mp.mpf('3.2'))),mp.findroot(lambda y:hh(a,y)-q,(4,mp.mpf('4.6')))]
        ok(roots[0]<xm<roots[1]<xp<roots[2],'three circular roots')
        ok(hprime(a,roots[0])>0 and hprime(a,roots[1])<0 and hprime(a,roots[2])>0,'stable-unstable-stable')

pc=mp.mpf(27)/5

def ve(y):
    return pc/(2*y*y) - (1+AC*mp.exp(-y))/y

for A in [mp.mpf('0.1'),mp.mpf('0.03')]:
    right=3+A
    energy=ve(right)
    left=mp.findroot(lambda y:ve(y)-energy,(3-A*mp.mpf('1.2'),3-A*mp.mpf('0.8')))
    middle=(left+right)/2
    width=(right-left)/2
    tiny=mp.mpf('1e-7')
    def integrate(angular=False):
        def fun(theta):
            y=middle+width*mp.cos(theta)
            speed2=2*(energy-ve(y))
            val=2*width*mp.sin(theta)/mp.sqrt(speed2)
            if angular:
                val*=mp.sqrt(pc)/(y*y)
            return val
        return mp.quad(fun,[tiny,mp.pi/2,mp.pi-tiny])
    period=integrate()
    sweep=integrate(True)
    ok(abs(A*period/(mp.sqrt(540)*BETA)-1)<mp.mpf('0.05'),'radial period asymptotic')
    ok(abs(A*sweep/(6*BETA)-1)<mp.mpf('0.05'),'angular winding asymptotic')

print(f'VERIFY_OK: {checks} symbolic/numerical assertion groups; beta={mp.nstr(BETA,16)}; cusp coupling={mp.nstr(AC,16)}')
