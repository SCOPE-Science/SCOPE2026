"""Independent finite exact-coefficient and high-precision mgf checks.

The finite checks are not an infinite proof; the theorem's coefficient inequality is analytical.
Run: python verify.py
"""
from fractions import Fraction as Q
from math import factorial, sqrt, log
from scipy.optimize import minimize_scalar
import mpmath as mp

mp.mp.dps = 70
counts = {'exact_coefficients':0, 'phase_examples':0, 'near_critical':0}

def threshold(b):
    b=mp.mpf(str(b))
    return (5*b+3+mp.sqrt(9*b*b+30*b+9))/(8*(1+b))

def M(b,p,t):
    b=mp.mpf(str(b));p=mp.mpf(str(p));t=mp.mpf(str(t))
    if abs(t)<mp.mpf('0.0001'):
        return mp.fsum([2*(p+(1-p)*(-b)**n)*t**n/mp.factorial(n+2) if n else mp.mpf(1) for n in range(24)])
    k=p*(mp.exp(t)-1-t)+(1-p)*(t*t/2 if b==0 else mp.expm1(-b*t)/b**2+t/b)
    return 2*k/t**2

def F(b,p,t):
    z=M(b,p,t)
    return (1-1/z)/t

for b in [Q(0),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10),Q(1)]:
    pb=float(threshold(str(b)))
    for p in [Q(19,20),Q(97,100),Q(99,100),Q(1)]:
        if float(p)+1e-8 < pb: continue
        m=((1+b)*p-b)/3
        assert m>0
        a=lambda n: Q(2)*(p+(1-p)*(-b)**n)/factorial(n+2)
        for n in range(1,61):
            assert a(n)>0 and a(n)<=m**n, (b,p,n)
            counts['exact_coefficients']+=1
    for mult, expect_local in [(0.82,False),(0.97,False),(1.01,True)]:
        p=pb*mult
        if p>=1:continue
        m=(p-(1-p)*float(b))/3
        res=minimize_scalar(lambda t: -float(F(b,p,mp.mpf(t))),bounds=(0.025,35),method='bounded',options={'xatol':1e-9})
        maximum=-res.fun
        if expect_local:assert maximum <= max(0,m)+5e-5,(b,p,maximum,m)
        else:assert maximum>max(0,m)+1e-8,(b,p,maximum,m)
        counts['phase_examples']+=1

for b in [0,.25,.5,.8,1]:
    pc=threshold(b)
    m=(pc-(1-pc)*b)/3
    Aprime=(1-b*b)/12-2*m*(1+b)/3
    B=(pc-(1-pc)*b**3)/60-m**3
    assert Aprime<0 and B<0
    for d in ['0.0002','0.0001']:
        p=pc-mp.mpf(d)
        approximate=(-Aprime)/(-2*B)*mp.mpf(d)
        root=mp.findroot(lambda t: mp.diff(lambda x: F(b,p,x),t), (approximate*.8,approximate*1.2))
        assert abs(root/approximate-1)<.05,(b,d,root,approximate)
        increase=F(b,p,root)-(p-(1-p)*b)/3
        target=Aprime**2/(-4*B)*mp.mpf(d)**2
        assert abs(increase/target-1)<.05,(b,d,increase,target)
        counts['near_critical']+=1
print('PASS',counts)
print('critical examples:',[(b,float(threshold(b))) for b in [0,.25,.5,.75,1]])
