"""Reproduce the exact stationary quantile moment identities.

The mathematical theorem is proved in RESULT.md; these finite tests
check algebra and quadrature only and do not certify an infinite-dimensional limit.
"""
import sympy as sp
import mpmath as mp

w=sp.symbols('w', real=True)
a=1+w/2
B=[sp.factor(sum(sp.binomial(k,j)*2**j*(-1)**(k-j)*sp.rf(a,j)/sp.rf(2,j) for j in range(k+1))) for k in range(5)]
assert all(sp.simplify(left-right)==0 for left,right in zip(B[:4],[sp.Integer(1),w/2,(w*w+2)/6,w*(w*w+8)/24]))
pi=sp.pi
t=sp.symbols('t', real=True)
m2=sp.Rational(1,3)+t+pi**2*t**2/12
m4=sp.Rational(1,5)+sp.Rational(4,3)*t+(2+pi**2/6)*t**2+pi**2*t**3/2+7*pi**4*t**4/240
k4=pi**4*t**4/120-t**2-sp.Rational(2,3)*t-sp.Rational(2,15)
assert sp.simplify(m4-3*m2*m2-k4)==0
assert sp.simplify(sp.factor(m4.subs(t,0))-sp.Rational(1,5))==0

mp.mp.dps=55

def quant(u,b):
    if b<1:
        edge=2*b-1
        z=min(u,edge)
        return z+(b*b-1)*mp.atanh(z)
    if b==1: return u
    return u+(b*b-1)*mp.atanh(u)

def raw(b,order):
    if b<1:
        edge=2*b-1
        q=quant(edge,b)
        return mp.quad(lambda u:quant(u,b)**order,[0,edge])+(1-edge)*q**order
    if b==1:return 1/mp.mpf(order+1)
    # u=tanh(z): integration using exponential tail; no endpoint atanh(1).
    return mp.quad(lambda z:(mp.tanh(z)+(b*b-1)*z)**order/mp.cosh(z)**2,[0,1,3,7,20,60,mp.inf])

bvals=[mp.mpf('0.501'),mp.mpf('0.55'),mp.mpf('0.7'),mp.mpf('0.95'),mp.mpf('1'),mp.mpf('1.1'),mp.mpf('1.4'),mp.mpf('1.54359383379446877917'),mp.mpf('1.8'),mp.mpf('2.7'),mp.mpf('5')]
rat=[]
for b in bvals:
    v2,v4=raw(b,2),raw(b,4)
    assert v2>0 and v4>0
    excess=v4/v2**2-3
    rat.append(v4/v2**2)
    if b>=1:
        tt=b*b-1
        vv=mp.mpf(str(sp.N(m2.subs(t,sp.Float(str(tt),50)),52)))
        ww=mp.mpf(str(sp.N(m4.subs(t,sp.Float(str(tt),50)),52)))
        assert abs(v2-vv)<mp.mpf('1e-35')*max(1,abs(v2))
        assert abs(v4-ww)<mp.mpf('1e-35')*max(1,abs(v4))
    print('b=',mp.nstr(b,20),'std_m4=',mp.nstr(v4/v2**2,30),'excess=',mp.nstr(excess,30))
assert all(rat[i]<rat[i+1] for i in range(len(rat)-1))
root=mp.findroot(lambda tt:mp.pi**4*tt**4/120-tt**2-mp.mpf(2)*tt/3-mp.mpf(2)/15,[1,2])
assert abs(mp.sqrt(1+root)-mp.mpf('1.54359383379446877917'))<mp.mpf('1e-18')
assert mp.mpf('1.3826')<root<mp.mpf('1.3828')
print('unique_positive_k4_root_t=',mp.nstr(root,40))
print('unique_positive_k4_root_b=',mp.nstr(mp.sqrt(1+root),40))
print('symbolic_and_numeric_checks=PASS')
