"""Exact local expansions and high-precision trajectory checks for the symmetric Ricker map.
Requires Python 3, sympy, mpmath. Finite checks do not certify global dynamics.
"""
import sympy as sp
import mpmath as mp

z=sp.symbols('z')
f_series=sp.series((2+z)*sp.exp(-z)-2,z,0,10).removeO()
F=sp.series(f_series.subs(z,f_series),z,0,7).removeO().expand()
assert sp.expand(F-(z-z**3/sp.Integer(3)+z**5/sp.Integer(30)+z**6/sp.Integer(72)))==0,F
v=sp.series((F/z)**-2,z,0,6).removeO().expand()
assert sp.simplify(v.coeff(z,2)-sp.Rational(2,3))==0
assert sp.simplify(v.coeff(z,4)-sp.Rational(4,15))==0
assert sp.simplify(v.coeff(z,5)+sp.Rational(1,36))==0

mp.mp.dps=75

def step(gamma,q,w):
    k=(1-gamma)/(1+gamma)
    a=mp.exp(-q)
    return a*((2+q)*mp.cosh(k*w)-w*mp.sinh(k*w))-2, a*(w*mp.cosh(k*w)-(2+q)*mp.sinh(k*w))

def rawstep(gamma,x,y):
    return x*mp.exp(2-x-gamma*y),y*mp.exp(2-y-gamma*x)

for gs in ['0.2','0.33333333333333333333333333333','0.5','0.8']:
    gamma=mp.mpf(gs)
    k=(1-gamma)/(1+gamma)
    eta=(3*gamma-1)/(1+gamma)
    assert abs(eta)<1
    a=(k*k-k)/(1+eta*eta)
    # Exact graph coefficient from quadratic invariance.
    assert abs(a*(1+eta*eta)-(k*k-k))<mp.mpf('1e-60')
    for qs,ws in [('0.1','0.03'),('-0.08','0.04')]:
        q=mp.mpf(qs);w=mp.mpf(ws)
        x=(q+2+w)/(1+gamma); y=(q+2-w)/(1+gamma)
        for it in range(20):
            qn,wn=step(gamma,q,w)
            xn,yn=rawstep(gamma,x,y)
            assert abs(qn-((1+gamma)*(xn+yn)/2-2))<mp.mpf('1e-65')
            assert abs(wn-((1+gamma)*(xn-yn)/2))<mp.mpf('1e-65')
            q,w=qn,wn;x,y=xn,yn
        # compare even-time reciprocal square and logarithmic corrections
        q,w=mp.mpf(qs),mp.mpf(ws)
        r=[]
        for it in range(4002):
            if it in (2000,4000):
                n=it//2
                r.append(1/q**2 - mp.mpf(2)*n/3 - mp.mpf(2)*mp.log(n)/5)
                # universal leading amplitude
                assert abs(abs(q)*mp.sqrt(it)-mp.sqrt(3))<mp.mpf('0.5'),(gs,qs,it,q)
            q,w=step(gamma,q,w)
        assert abs(r[1]-r[0])<mp.mpf('0.5'),(gs,qs,r)
    print('PASS gamma',gs, 'eta',mp.nstr(eta,10),'graph-curvature',mp.nstr(a,12))
print('PASS symbolic and numeric checks')
