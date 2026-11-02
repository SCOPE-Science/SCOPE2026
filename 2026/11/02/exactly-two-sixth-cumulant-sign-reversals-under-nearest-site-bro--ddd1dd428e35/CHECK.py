"""Reproducibility checks for the sixth-cumulant transitions in local resetting.
Run: python3 CHECK.py (requires sympy and mpmath).
Finite numerical tests complement the analytical root-count proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as s
import mpmath as mp

checks=0
def check(cond,msg):
    global checks
    assert cond,msg
    checks+=1

# Exact coefficient formula: (2n)![a^(2n)]N(a) for n>=2.
def bn(n):
    return (Q(36**n,2)-3*n*25**n +
            (Q(27)+Q(45*n,16)+Q(135*n*(2*n-1),64))*16**n -
            135*n*9**n +
            (Q(135,2)+Q(135*n,4)+135*n*(2*n-1))*4**n -870*n)

expected = [2880,-7061040,-627207840,-29245798800,
            -997196607360,-26909026832880,-536349344438880,
            -3322432609292880,403937372282846400]
for n,val in zip(range(4,13),expected):
    check(bn(n)==val,f'b_{n}')
check(Q(36,25)**12 > 6*12,'first tail inequality at n=12')
check(Q(16,9)**12 > 5*12,'second tail inequality at n=12')
check(Q(135,2)*4**12>870*12,'third tail inequality at n=12')

# Verify exact hyperbolic polynomial from independently expanded implicit root.
a,z=s.symbols('a z',positive=True)
S=(z-z**-1)/2; H=(z+z**-1)/2
L=2*S**2; k=4*a*a
L1=S*H/(2*a)
L2=(2*a*(z*z+z**-2)/2-(z*z-z**-2)/2)/(32*a**3)
H1=S/(8*a); H2=(a*H-S)/(64*a**3)
A=a*a*H/S**2
B=(A/2+k*H/24+k*H1*A/2-A*A*L1)/L
C=(B/2+A/24+k*(H/720+H1*A/24+H1*B/2+H2*A*A/4)-2*A*B*L1-A**3*L2/2)/L
poly=(4*z**12+216*z**10+540*z**8-1520*z**6+540*z**4+216*z**2+4
      +a*(-60*z**11+45*z**10-1620*z**9+270*z**8-3480*z**7+3480*z**5-270*z**4+1620*z**3-45*z**2+60*z)
      +a*a*(135*z**10+2160*z**8+5490*z**6+2160*z**4+135*z**2))
N=poly/(16*z**6)
check(s.cancel(C*5760*S**8/(a*a*H)-N)==0,'sixth coefficient identity')

# A rational certificate of N(1)<0:  e lower/upper by positive series.
e_lo=sum((Q(1,factorial(i)) for i in range(21)),Q(0))
e_hi=e_lo+Q(1,20*factorial(20))
P={12:4,11:-60,10:396,9:-1620,8:2970,7:-3480,
   6:3970,5:3480,4:2430,3:1620,2:306,1:60,0:4}
P_hi=sum(Q(coeff)*(e_hi if coeff>0 else e_lo)**p for p,coeff in P.items())
check(P_hi<0,'rational certificate of N(1)<0')

# The function N(a) and the rate coefficient can be evaluated at high precision.
mp.mp.dps=80
def coeff(a0):
    aa=mp.mpf(a0); ss=mp.sinh(aa); hh=mp.cosh(aa)
    p= (mp.mpf('0.5')*mp.cosh(6*aa)+27*mp.cosh(4*aa)
        +mp.mpf('67.5')*mp.cosh(2*aa)-95
        +aa*(-mp.mpf('7.5')*mp.sinh(5*aa)+mp.mpf('5.625')*mp.sinh(4*aa)
              -mp.mpf('202.5')*mp.sinh(3*aa)+mp.mpf('33.75')*mp.sinh(2*aa)
              -435*mp.sinh(aa))
        +aa**2*(mp.mpf('16.875')*mp.cosh(4*aa)+270*mp.cosh(2*aa)+mp.mpf('343.125')))
    return p,aa**2*hh*p/(5760*ss**8)
for a0,sgn in [('0.1',1),('0.5',-1),('1',-1),('4',1),('10',1)]:
    n,c=coeff(a0)
    check(sgn*c>0,'sign at a='+a0)
left=mp.findroot(lambda x:coeff(x)[0],(mp.mpf('.18'),mp.mpf('.2')))
right=mp.findroot(lambda x:coeff(x)[0],(mp.mpf('3.7'),mp.mpf('3.9')))
check(mp.mpf('.1893')<left<mp.mpf('.18931'),'first root bracket')
check(mp.mpf('3.79624')<right<mp.mpf('3.79626'),'second root bracket')

# Directly solve the independent renewal-root equation for small tilted parameter.
def laglambda(aa,uu):
    kk=4*aa**2
    def f(ll):
        root=mp.sqrt(kk+ll)
        return ll*(mp.cosh(root)-mp.cosh(uu))-kk*mp.cosh(root/2)*(mp.cosh(uu)-1)
    return mp.findroot(f,(mp.mpf('0'),mp.mpf('0.01')))
for a0 in ['0.3','1','5']:
    aa=mp.mpf(a0); ss=mp.sinh(aa); hh=mp.cosh(aa)
    aa2=aa**2*hh/ss**2
    bb=aa2*(2*ss*(3+ss**2)-3*aa*(2+ss**2))/(24*ss**3)
    cc=coeff(aa)[1]
    for uu in ['0.03','0.02','0.01']:
        t=mp.mpf(uu)
        exact=laglambda(aa,t)
        approx=aa2*t**2+bb*t**4+cc*t**6
        check(abs(exact-approx)<mp.mpf('100')*t**8,'renewal root Taylor check')
print('PASS',checks,'checks')
print('threshold alpha=',mp.nstr(left,40),mp.nstr(right,40))
print('threshold rate*rL²/D=',mp.nstr(4*left**2,40),mp.nstr(4*right**2,40))
