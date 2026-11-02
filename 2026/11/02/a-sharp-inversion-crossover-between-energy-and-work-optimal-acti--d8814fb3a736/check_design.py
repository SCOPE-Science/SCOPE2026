"""Symbolic and numerical consistency checks for two-state battery gap design."""
import sympy as sp
import mpmath as mp

z, B = sp.symbols('z B', real=True, positive=True)
u, k = sp.symbols('u k', positive=True)
P = sp.exp(B)/(sp.exp(B) + sp.exp(z))
Q = 1/(1+sp.exp(z))
Delta = sp.factor(P-Q)
K = P*sp.log(P/Q) + (1-P)*sp.log((1-P)/(1-Q))
# The derivatives use the exact log-odds difference B.
Kd = sp.factor(sp.diff(P,z)*B + (P-Q))
Kd_target = u*(k*(k-1-B)-(k*(B-1)+1)*u)/((u+1)*(u+k)**2)
assert sp.simplify(Kd.subs({sp.exp(z):u,sp.exp(B):k})-Kd_target)==0
Ud = sp.diff(z*Delta,z)
Ud_target = Delta*(1-z*(sp.tanh(z/2)-sp.tanh((B-z)/2))/2)
assert sp.simplify(sp.together((Ud-Ud_target).rewrite(sp.exp)))==0
checks=2
mp.mp.dps=70

def pq(b,t):
    a=mp.exp(b)
    w=mp.exp(t)
    return a/(a+w),1/(1+w)

def cap(b,t):
    p,q=pq(b,t)
    return p*mp.log(p/q)+(1-p)*mp.log((1-p)/(1-q))

def en(b,t):
    p,q=pq(b,t)
    return t*(p-q)

def zc(b):
    a=mp.exp(b)
    return mp.log(a*(a-1-b)/(a*(b-1)+1))

def h(b,t):
    return t*(mp.tanh(t/2)-mp.tanh((b-t)/2))/2

def zu(b):
    lo=b/2;hi=max(b+6,mp.mpf(4))
    assert h(b,lo)<1<h(b,hi)
    for _ in range(240):
        md=(lo+hi)/2
        if h(b,md)>1:hi=md
        else:lo=md
    return (lo+hi)/2

bs=[mp.mpf(x) for x in ('0.1','0.5','1','2','2.399357280515468','3','5','10','20','50')]
for b in bs:
    x=zc(b); y=zu(b)
    assert b/2<x<b<y or (b/2<x<y and x<b)
    checks+=1
    assert x<y; checks+=1
    assert abs(h(b,y)-1)<mp.mpf('1e-65'); checks+=1
    ax=cap(b,x); uy=en(b,y)
    for m in range(1,75):
        t=mp.mpf(m)*max(b,mp.mpf(3))/60
        assert cap(b,t)<=ax+mp.mpf('1e-50')
        assert en(b,t)<=uy+mp.mpf('1e-50')
        checks+=2
        # Analytic signs on both sides of the unique global maxima.
        p,q=pq(b,t)
        DA=(p-q)-b*p*(1-p)
        DU=(p-q)-t*(p*(1-p)-q*(1-q))
        assert (DA>0)==(t<x)
        assert (DU>0)==(t<y)
        checks+=2

bc=mp.findroot(lambda b:b*mp.tanh(b/2)-2,(2,3))
assert abs(bc-mp.mpf('2.399357280515468'))<mp.mpf('1e-15');checks+=1
for b in [mp.mpf('0.1'),bc,mp.mpf('10')]:
    y=zu(b)
    if b<bc:assert y>b
    elif b>bc:assert y<b
    else:assert abs(y-b)<mp.mpf('1e-60')
    checks+=1

z0=mp.findroot(lambda t:t*mp.tanh(t/2)-1,(1,2))
ratio=mp.sech(z0/2)**2
assert mp.mpf('0.58020')<ratio<mp.mpf('0.58021');checks+=1
for b in [mp.mpf('0.01'),mp.mpf('0.005'),mp.mpf('0.002')]:
    err=abs(cap(b,zu(b))/cap(b,zc(b))-ratio)
    assert err < 5*b
    checks+=1
print('PASS',checks,'assertions')
print('Bcritical =',mp.nstr(bc,30))
print('z0 =',mp.nstr(z0,30))
print('weak-drive capacity fraction at the energy optimizer =',mp.nstr(ratio,30))
