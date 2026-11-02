#!/usr/bin/env python3
"""Reproduce exact symbolic identities and numerical sanity checks for LR1 burn-in ages.

Dependencies: sympy >= 1.10 and mpmath >= 1.2.
The infinite-domain theorem is proved analytically; this code is not a proof by sampling.
"""
import sympy as sp
import mpmath as mp

checks = 0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1

x, a, ell = sp.symbols('y A lambda', positive=True)
F = x**2 + 4*x + 6
G = 3*x**3 + 15*x**2 + 32*x + 32
P = 1 + x + x**2/sp.Integer(2) + x**3/sp.Integer(6)
H = (4*a + x**3/sp.Integer(6))/(a + P)
Hd_num = sp.together(sp.diff(H,x) - 3*a*sp.diff(H,a))*(a+P)**2
check(sp.simplify(Hd_num-(x**2*F-6*a*G)/12)==0, 'hazard derivative identity')
Q = sp.exp(3*x)*x**2*F/(6*G)
T = sp.expand(3*F*G + sp.diff(F,x)*G-F*sp.diff(G,x))
check(sp.simplify(T-(9*x**5+78*x**4+306*x**3+668*x**2+844*x+512))==0, 'monotonicity polynomial')
for c in sp.Poly(T,x).all_coeffs():
    check(c>0,'strictly positive polynomial coefficient')
check(sp.limit(Q/x**2,x,0)==sp.Rational(1,32), 'small-argument leading term')
check(sp.limit(Q/(x*sp.exp(3*x)),x,sp.oo)==sp.Rational(1,18), 'large-argument leading term')
check(sp.series(Q,x,0,4).removeO().coeff(x,3)==sp.Rational(1,12), 'small-argument cubic term')
root_asym=4*sp.sqrt(2)*ell-sp.Rational(128,3)*ell**2
check(sp.series(Q.subs(x,root_asym)-ell**2,ell,0,4).removeO()==0,'small-parameter inverse through cubic order')
As=ell**2*sp.exp(-3*root_asym)
Hs=(4*As+root_asym**3/sp.Integer(6))/(As+(1+root_asym+root_asym**2/2+root_asym**3/6))
series_h=sp.series((ell/2)*Hs,ell,0,5).removeO()
check(sp.expand(series_h-2*ell**3+sp.Rational(64,3)*sp.sqrt(2)*ell**4)==0,'small-parameter minimum hazard correction')

mp.mp.dps=75

def QQ(z):
    return mp.exp(3*z)*z*z*(z*z+4*z+6)/(6*(3*z**3+15*z*z+32*z+32))

def inverse(la):
    lo=mp.mpf('0'); hi=mp.mpf('1')
    while QQ(hi)<la*la:
        hi*=2
    for _ in range(320):
        mid=(lo+hi)/2
        if QQ(mid)>la*la:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def normalized_h(z, la):
    A=la*la*mp.exp(-3*z)
    return (4*A+z**3/6)/(A+1+z+z*z/2+z**3/6)

values=['1e-8','1e-6','1e-4','0.001','0.01','0.1','0.3','1','2','5','10','100','10000','1e8','1e20','1e40']
last=None
for val in values:
    la=mp.mpf(val); y=inverse(la); age=2*y/la
    check(abs(QQ(y)/(la*la)-1)<mp.mpf('1e-65'),f'root residual {val}')
    if last is not None:
        check(age<last,f'age monotonicity {val}')
    last=age
    A=la*la*mp.exp(-3*y)
    for t in [y/3,y*mp.mpf('0.9')]:
        AA=la*la*mp.exp(-3*t)
        check(t*t*(t*t+4*t+6)-6*AA*(3*t**3+15*t*t+32*t+32)<0,f'left derivative {val}')
    for t in [y*mp.mpf('1.1'),y*3]:
        AA=la*la*mp.exp(-3*t)
        check(t*t*(t*t+4*t+6)-6*AA*(3*t**3+15*t*t+32*t+32)>0,f'right derivative {val}')
    h=la/2*normalized_h(y,la)
    check(h<min(la/2,2*la**3/(1+la**2)),f'minimum below boundaries {val}')

for val in ['1e-8','1e-7','1e-6']:
    la=mp.mpf(val); y=inverse(la); age=2*y/la
    ageasym=8*mp.sqrt(2)-mp.mpf(256)/3*la
    check(abs(age-ageasym) < 1200*la*la,f'small age expansion {val}')
    h=la/2*normalized_h(y,la)
    hasym=2*la**3-64*mp.sqrt(2)/3*la**4
    check(abs(h-hasym) < 600*la**5,f'small hazard expansion {val}')

for val in ['1e15','1e30','1e60']:
    la=mp.mpf(val); y=inverse(la); L=mp.log(la)
    yasym=2*L/3-mp.log(L)/3+mp.log(3)
    check(abs(y-yasym)<mp.mpf('0.05'),f'large age expansion {val}')
    h=la/2*normalized_h(y,la)
    hasym=1-mp.mpf(9)/(2*L)
    check(abs(h/(la/2)-hasym)<mp.mpf('0.01'),f'large hazard expansion {val}')

print(f'PASS: {checks} exact symbolic and numerical checks')
print('Illustrative parameter, minimum age, minimum hazard:')
for val in ['0.01','1','100']:
    la=mp.mpf(val); y=inverse(la)
    print(val,mp.nstr(2*y/la,15),mp.nstr(la/2*normalized_h(y,la),15))
