#!/usr/bin/env python3
"""Deterministic cross-checks for a fixed-budget telegraph-resetting optimum.

Uses independent backward-equation residuals, exact calculus identities,
and high-precision root/optimization checks. Numerical checks are not proofs.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
checks = 0

def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1

p, q, b = sp.symbols('p q b', positive=True)
a = sp.sqrt(p*(2-p))
f = (sp.exp(q*a)-1)/p
scaled = sp.factor((sp.diff(f,p) * p*p / sp.exp(q*a)) - (q*p*(1-p)/a - (1-sp.exp(-q*a))))
check(sp.simplify(scaled)==0, 'derivative equation')
# Poisson thinning of exponential decision clock: r=lambda*p and kappa=lambda*(1-p).
# For the no-reset hitting transform h_+(x)=exp[z(x-L)]:
s, k, v, x, L = sp.symbols('s k v x L', positive=True)
z=sp.sqrt(s*(s+2*k))/v
hp=sp.exp(z*(x-L)); hm=(s+k-v*z)/k*hp
check(sp.simplify(v*sp.diff(hp,x)+k*(hm-hp)-s*hp)==0,'positive velocity backward equation')
check(sp.simplify(-v*sp.diff(hm,x)+k*(hp-hm)-s*hm)==0,'negative velocity backward equation')
check(sp.simplify(hp.subs(x,L)-1)==0,'outgoing boundary condition')

psi=lambda b: -mp.expm1(-b)/b
A=lambda b: 1-(b+1)*mp.exp(-b)
D=lambda b: -mp.expm1(-b)
B=lambda b: b-1+mp.exp(-b)
C=lambda b: b-2+2*mp.exp(-b)
H=lambda b: A(b)*D(b)/(B(b)*C(b))
qcurve=lambda b: b*(1-psi(b))/mp.sqrt(1-2*psi(b))
ptheta=lambda b: (1-2*psi(b))/(1-psi(b))
F=lambda t,Q: mp.expm1(Q*mp.sqrt(t*(2-t)))/t
g=lambda t,Q: Q*mp.sqrt(t*(2-t))*(1-t)/(2-t)-(-mp.expm1(-Q*mp.sqrt(t*(2-t))))
b0=mp.findroot(lambda x: 2*(1-mp.exp(-x))-x,(mp.mpf('1.5'),mp.mpf('1.8')))
bs=mp.findroot(lambda x:H(x)-1,(mp.mpf('2.2'),mp.mpf('2.25')))
qs=qcurve(bs); ps=ptheta(bs)
check(mp.mpf('1.5936')<b0<mp.mpf('1.5937'),'b0 bracket')
check(mp.mpf('2.9938')<qs<mp.mpf('2.9939'),'fold bracket')
check(abs(H(bs)-1)<mp.mpf('1e-58'),'fold root')
check(abs(g(ps,qs))<mp.mpf('1e-58'),'fold stationary')

def stationary_roots(Q):
    if Q<=qs:return []
    lo=b0+mp.mpf('1e-50'); hi=bs
    for _ in range(230):
        mid=(lo+hi)/2
        if qcurve(mid)>Q:lo=mid
        else:hi=mid
    blo=(lo+hi)/2
    lo=bs;hi=Q+5
    for _ in range(230):
        mid=(lo+hi)/2
        if qcurve(mid)<Q:lo=mid
        else:hi=mid
    bhi=(lo+hi)/2
    return [ptheta(blo),ptheta(bhi)]

pc,qc=mp.findroot((lambda t,Q:g(t,Q),lambda t,Q:F(t,Q)-F(1,Q)),(mp.mpf('0.12'),mp.mpf('3.73')))
check(mp.mpf('3.72957')<qc<mp.mpf('3.72958'),'switch threshold bracket')
check(mp.mpf('0.12046')<pc<mp.mpf('0.12047'),'switch fraction bracket')
check(abs(g(pc,qc))<mp.mpf('1e-55'),'switch stationary')
check(abs(F(pc,qc)-F(1,qc))<mp.mpf('1e-55'),'switch global tie')

for Q in [mp.mpf(v) for v in ['0.25','1','2.99','3.0','3.2','3.7','3.729','3.730','3.75','4','5','6','10','20','30','50']]:
    roots=stationary_roots(Q)
    check(len(roots)==(2 if Q>qs else 0), 'root count at Q='+str(Q))
    for t in roots:
        check(0<t<1,'interior fraction')
        check(abs(g(t,Q))<mp.mpf('1e-45'),'stationary eq at Q='+str(Q))
    if roots:
        tlo,thi=roots
        check(tlo<thi,'ordered extrema')
        check(F(tlo,Q)<F(thi,Q),'minimum then maximum')
        check((F(tlo,Q)>F(1,Q))==(Q<qc),'global selection branch')

# Monotonic H is established analytically in RESULT.md; numerically sample.
prev=H(b0+mp.mpf('1e-5'))
for i in range(1,201):
    z=b0+mp.mpf('1e-5')+(mp.mpf(i)*mp.mpf('0.15'))
    h=H(z)
    check(h<prev,'H decreasing')
    prev=h

# Asymptotic coefficient, normalized optimizer and objective.
for Q in [mp.mpf(v) for v in ['20','40','80','160','320']]:
    opt=stationary_roots(Q)[0]
    ctheta=opt*Q**2
    ctime=F(opt,Q)/Q**2
    check(abs(ctheta-b0*b0/2)<mp.mpf('0.6'),'optimizer scale')
    check(abs(ctime-2*mp.expm1(b0)/b0**2)<mp.mpf('0.13'),'time scale')

print('PASS',checks,'deterministic checks')
for key,val in [('b0',b0),('fold_q',qs),('fold_theta',ps),('switch_q',qc),('switch_theta',pc),('asymptotic_theta_const',b0*b0/2),('asymptotic_time_const',2*mp.expm1(b0)/b0**2)]:
    print(key,mp.nstr(val,42))
