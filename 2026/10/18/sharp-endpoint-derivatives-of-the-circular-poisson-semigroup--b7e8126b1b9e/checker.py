"""Reproduce algebraic identities and finite integral checks for circular Poisson endpoint norms.
Requires Python 3.9+, sympy, and mpmath. Analytical proofs in RESULT.md supply all quantifiers.
"""
import math
import sympy as sp
import mpmath as mp

COUNT = 0

def check(flag, message):
    global COUNT
    COUNT += 1
    if not flag:
        raise AssertionError(message)

def close(a,b,tol=mp.mpf('2e-19')):
    return abs(a-b) <= tol * max(mp.mpf('1'),abs(a),abs(b))

h,x,s=sp.symbols('h x s', real=True)
P=s/(h-x)
Dt=lambda expr:sp.diff(expr,h)*s+sp.diff(expr,s)*h
p1=sp.factor(Dt(P).subs(s**2,h**2-1))
p2=sp.factor(Dt(p1).subs(s**2,h**2-1))
p3=sp.factor(Dt(p2).subs(s**2,h**2-1))
expect1=(1-h*x)/(h-x)**2
expect2=s*(x*x+h*x-2)/(h-x)**3
F=4*h*h-h*x**3+(4-4*h*h)*x*x+(-h**3+4*h)*x-6
expect3=F/(h-x)**4
# The recursion's first derivative carries s**2; substitute it only after differentiation.
check(sp.simplify(p1-expect1)==0,'first derivative')
check(sp.simplify(p2-expect2)==0,'second derivative')
check(sp.simplify((p3-expect3).subs(s**2,h**2-1))==0,'third derivative')
check(sp.simplify(F.subs(x,1)+(h-1)**2*(h+2))==0,'upper-end cubic sign')
check(sp.simplify(F.subs(x,-1)-(h-2)*(h+1)**2)==0,'lower-end cubic sign')
check(sp.simplify(F.subs(x,1/h)-3*(h*h-1)**2/h**2)==0,'interior sign')
check(sp.simplify(F.subs(x,-h)+2*(h**4-2*h*h+3))==0,'external sign')

mp.mp.dps=55
pi=mp.pi

def kernel_derivative(t,theta,n):
    r=mp.exp(-t)
    z=r*mp.exp(1j*theta)
    if n==1:
        return 2*mp.re(-z/(1-z)**2)
    if n==2:
        return 2*mp.re(z*(1+z)/(1-z)**3)
    if n==3:
        return 2*mp.re(-z*(1+4*z+z*z)/(1-z)**4)
    raise ValueError('n must be 1,2,3')

def roots3(t):
    hh=mp.cosh(t)
    coeff=[-hh, 4-4*hh*hh, -hh**3+4*hh, 4*hh*hh-6]
    # High precision cubic root finding with seeded brackets on intervals where the proof forces signs.
    poly=lambda xx:coeff[0]*xx**3+coeff[1]*xx**2+coeff[2]*xx+coeff[3]
    root_hi=mp.findroot(poly,(1/hh+mp.mpf('0.03')*(1-1/hh),1-mp.mpf('0.03')*(1-1/hh)),solver='anderson')
    out=[root_hi]
    if hh<2:
        root_lo=mp.findroot(poly,(-1+mp.mpf('.1')*(1+1/hh),1/hh-mp.mpf('.1')*(1+1/hh)),solver='anderson')
        out.append(root_lo)
    return out

def exact_norm(t,n):
    hh=mp.cosh(t); ss=mp.sinh(t)
    if n==1:
        return 2/(pi*ss)
    if n==2:
        z=4/(hh+mp.sqrt(hh*hh+8))
        return 2*ss*mp.sqrt(1-z*z)/(pi*(hh-z)**2)
    if n==3:
        return 2/pi*sum(abs(mp.sqrt(1-z*z)*(2-hh*hh-hh*z)/(hh-z)**3) for z in roots3(t))
    raise ValueError(n)

def quadrature(t,n):
    if n==1:
        nodes=[mp.acos(1/mp.cosh(t))]
    elif n==2:
        hh=mp.cosh(t); nodes=[mp.acos(4/(hh+mp.sqrt(hh*hh+8)))]
    else:
        nodes=[mp.acos(z) for z in roots3(t)]
    nodes=sorted(nodes)
    return mp.quad(lambda theta:abs(kernel_derivative(t,theta,n)),[mp.mpf(0)]+nodes+[pi])/pi

for t_string in ['0.05','0.17','0.8','1','1.3','1.3169578969248167','1.4','2.8','5.3']:
    t=mp.mpf(t_string)
    for n in [1,2,3]:
        try:
            got=quadrature(t,n)
            want=exact_norm(t,n)
            check(close(got,want,mp.mpf('2e-16')),f'quadrature n={n} t={t}: {got} vs {want}')
        except ValueError as exc:
            raise AssertionError(f'n={n} t={t}: {exc}')
for t_string,expected in [('0.1',2),('1.0',2),('1.3',2),('1.4',1),('1.8',1),('4.0',1)]:
    z=roots3(mp.mpf(t_string))
    check(len(z)==expected,f'third derivative sign regions {t_string}')

for n in range(1,13):
    zeros=[(2*j+1)*pi/(2*(n+1)) for j in range((n+1)//2)]
    num=mp.factorial(n)/pi*2*sum(mp.quad(lambda u:mp.cos(u)**(n-1)*abs(mp.cos((n+1)*u)),
                                        [left,right]) for left,right in zip([mp.mpf(0)]+zeros,zeros+[pi/2]))
    closed=4*mp.factorial(n-1)/pi*sum(mp.cos(u)**(n+1) for u in zeros)
    check(close(num,closed,mp.mpf('1e-27')),f'all-order Euclidean constant n={n}')

check(close(2/pi,4/pi*mp.cos(pi/4)**2),'C1')
check(close(3*mp.sqrt(3)/(2*pi),4/pi*mp.cos(pi/6)**3),'C2')
check(close(6/pi,8/pi*(mp.cos(pi/8)**4+mp.cos(3*pi/8)**4)),'C3')
for t_string in ['0.04','0.1','0.2','0.5','1.5']:
    t=mp.mpf(t_string)
    for n in [1,2,3]:
        c=4*mp.factorial(n-1)/pi*sum(mp.cos((2*j+1)*pi/(2*(n+1)))**(n+1) for j in range((n+1)//2))
        check(t**n*exact_norm(t,n)<c,'strict finite-scale bound')

# Symbolically verify the quartic cancellation and first derivative correction.
t=sp.symbols('t',positive=True)
ht=sp.cosh(t)
zt=(-ht+sp.sqrt(ht**2+8))/2
NT2=sp.Rational(2)/sp.pi*sp.sinh(t)*sp.sqrt(1-zt*zt)/(ht-zt)**2
S=sp.series(t*t*NT2,t,0,6).removeO()
check(sp.simplify(sp.expand(S)-(3*sp.sqrt(3)/(2*sp.pi)-sp.sqrt(3)*t**4/(90*sp.pi)))==0,'quartic cancellation')
S1=sp.series(t*sp.Rational(2)/(sp.pi*sp.sinh(t)),t,0,5).removeO()
check(sp.simplify(S1-(2/sp.pi-t*t/(3*sp.pi)+7*t**4/(180*sp.pi)))==0,'first derivative correction')
print('PASS:',COUNT,'independent exact/formula/quadrature assertions')
