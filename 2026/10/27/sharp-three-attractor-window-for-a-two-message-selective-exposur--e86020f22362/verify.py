"""Standalone checks for the binary-source message-preference phase portrait.

Requires Python 3, sympy, and mpmath. Numerical assertions corroborate,
but are not substitutes for, the analytic inequalities in RESULT.md.
"""
import mpmath as mp
import sympy as sp

checks=0

def check(cond, label):
    global checks
    if not cond:
        raise AssertionError(label)
    checks += 1

x,u=sp.symbols('x u', real=True)
# Exact kernel identity at preference exponent b=1.
f=(x*(2-x))/(x*(2-x)+(1-x*x))
check(sp.simplify((f-x)*(1+2*x-2*x*x)-x*(1-x)*(1-2*x))==0,'exact fixed-point factorization')

# Exact derivative-ratio identity underlying monotone l'Hopital.
p=sp.log(x/(1-x));q=sp.log((1+x)/(2-x))
check(sp.simplify(sp.diff(p,x)/sp.diff(q,x)-(sp.Rational(1,3)+sp.Rational(2,3)/(x*(1-x))))==0,'derivative ratio')
# Exact critical center cubic coefficient.
xx=sp.Rational(1,2)+u
b=sp.Rational(3,2)
F=(xx*(2-xx))**b/((xx*(2-xx))**b+(1-xx*xx)**b)
series=sp.series(F-xx,u,0,6).removeO().expand()
check(series.coeff(u,1)==0, 'critical linear cancellation')
check(series.coeff(u,2)==0, 'critical quadratic cancellation')
check(series.coeff(u,3)==sp.Rational(16,27), 'critical cubic coefficient')
check(series.coeff(u,4)==0, 'critical quartic cancellation')

mp.mp.dps=65

def fb(b, z, prob=mp.mpf('0.5')):
    w1=(z*(2-z))**b
    w0=(1-z*z)**b
    return prob*w1/(prob*w1+(1-prob)*w0)

def K(z):
    return mp.log(z/(1-z))/mp.log((1+z)/(2-z))

def root_upper(b):
    lo=mp.mpf('0.5')+mp.mpf('1e-35')
    hi=mp.mpf('1')-mp.mpf('1e-50')
    target=b/(b-1)
    for _ in range(300):
        mid=(lo+hi)/2
        if K(mid)<target:lo=mid
        else:hi=mid
    return (lo+hi)/2

for b_s in ['1.05','1.10','1.25','1.40','1.49','1.499']:
    b=mp.mpf(b_s); r=root_upper(b)
    check(mp.fabs(fb(b,r)-r)<mp.mpf('1e-55'), 'separatrix root '+b_s)
    h=mp.mpf('1e-7')
    check(fb(b,r-h)<r-h and fb(b,r+h)>r+h, 'separatrix repulsion '+b_s)
    check(fb(b,mp.mpf('.5')+h)<mp.mpf('.5')+h, 'central attraction '+b_s)
    check(r>mp.mpf('.5') and r<1,'location '+b_s)

for b_s in ['0.4','0.9','1.0','1.5','1.6','2.0','4.0']:
    b=mp.mpf(b_s)
    for z_s in ['0.51','0.6','0.8','0.95']:
        z=mp.mpf(z_s)
        check((fb(b,z)>z)==(b>=mp.mpf('1.5')), 'global drift '+b_s+' '+z_s)
        check(mp.fabs(fb(b,1-z)+fb(b,z)-1)<mp.mpf('1e-60'),'symmetry '+b_s+' '+z_s)

for eps_s in ['0.0001','0.00001','0.000001']:
    eps=mp.mpf(eps_s);r=root_upper(mp.mpf('1.5')-eps)
    rat=(r-mp.mpf('.5'))/mp.sqrt(eps)
    check(mp.fabs(rat-mp.mpf(3)/(2*mp.sqrt(2)))<3*mp.sqrt(eps),'separatrix square root '+eps_s)

# Biased message probabilities: five hyperbolic fixed points persist.
for pr_s in ['0.495','0.505']:
    b=mp.mpf('1.25');pr=mp.mpf(pr_s)
    roots=[]
    z0=mp.mpf('1e-18');g0=fb(b,z0,pr)-z0
    N=2000
    for k in range(1,N+1):
        z1=mp.mpf(k)/N*(1-mp.mpf('1e-18'))+mp.mpf('1e-18')
        g1=fb(b,z1,pr)-z1
        if g0*g1<0:
            a=z0;c=z1
            for _ in range(220):
                m=(a+c)/2
                if (fb(b,m,pr)-m)*(fb(b,a,pr)-a)<=0:c=m
                else:a=m
            roots.append((a+c)/2)
        z0=z1;g0=g1
    check(len(roots)==3,'three interior roots '+pr_s)
    for i,z in enumerate(roots):
        slope=mp.diff(lambda t:fb(b,t,pr),z)
        check((slope<1)==(i==1),'interior alternating stability '+pr_s+':'+str(i))

# Orbit monotonicity sample; endpoints are exact fixed points.
for b_s in ['0.75','1.25','1.6']:
    b=mp.mpf(b_s)
    for z_s in ['0.01','0.10','0.45','0.55','0.90','0.99']:
        z=mp.mpf(z_s)
        first=fb(b,z)
        step_up=first>z
        for k in range(150):
            zn=fb(b,z)
            check((zn>=z)==step_up,'monotone trajectory '+b_s+' '+z_s+' '+str(k))
            z=zn
print(f'PASS: {checks} exact-symbolic and high-precision numerical assertions')
