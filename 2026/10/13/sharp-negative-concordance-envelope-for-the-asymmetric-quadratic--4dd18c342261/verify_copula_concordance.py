"""Reproduce symbolic and numerical checks for the sharp concordance envelope.
Run with: python verify_copula_concordance.py
"""
import sympy as sp
import mpmath as mp
u,v=sp.symbols('u v', real=True)
D=sp.Function('D')(v)
C=u*v-u*(1-u)*D
c=sp.diff(sp.diff(C,u),v)
inner=sp.integrate(sp.expand(C*c),(u,0,1))
expected=v/sp.Integer(2)-D/sp.Integer(6)+v*sp.diff(D,v)/6
assert sp.simplify(inner-expected)==0
integral=sp.integrate(v,(v,0,sp.exp(-1)))+sp.integrate(-v*sp.log(v),(v,sp.exp(-1),1))
assert sp.simplify(integral-(1-sp.exp(-2))/4)==0

eps=sp.symbols('eps',positive=True)
T=(sp.exp(1/eps)-1)*v**(1/eps)
phi=eps*sp.log(1+T)
assert sp.simplify(v*sp.diff(phi,v)-T/(1+T))==0
assert sp.simplify(phi.subs(v,1)-1)==0

mp.mp.dps=65
bound=-(1-mp.exp(-2))/2
assert abs(bound+mp.mpf('0.432332358381693654')) < mp.mpf('1e-18')

def phi_eps(t,e):
    if t==0:return mp.mpf('0')
    return e*mp.log1p(mp.expm1(1/e)*t**(1/e))

def rho(e):
    cutoff=mp.exp(-1)
    return -2*(mp.quad(lambda t:t*(1-phi_eps(t,e)),[0,cutoff])+
               mp.quad(lambda t:t*(1-phi_eps(t,e)),[cutoff,1]))

rs=[]
for e0 in ['0.5','0.2','0.1','0.05','0.02']:
    e=mp.mpf(e0)
    r=rho(e)
    assert bound < r < 0
    rs.append(r)
    for t in [mp.mpf('0.001'),mp.exp(-1),mp.mpf('0.85')]:
        val=phi_eps(t,e)
        slope=mp.expm1(1/e)*t**(1/e)
        derivative_product=slope/(1+slope)
        assert 0<=val<=1
        assert 0<derivative_product<1
        assert val>=max(0,1+mp.log(t))-mp.mpf('1e-58')
assert all(rs[j+1]<rs[j] for j in range(len(rs)-1))
assert abs(rs[-1]-bound) < mp.mpf('2e-4')

# For a large epsilon, pointwise phi approaches 1 away from the endpoint 0,
# so Spearman rho approaches 0. Numerical evaluation supplements DCT.
assert -mp.mpf('0.12')<rho(mp.mpf('20'))<0
print('VERIFY_OK')
print('sharp_rho_infimum',mp.nstr(bound,30))
print('sharp_tau_infimum',mp.nstr(bound*mp.mpf(2)/3,30))
for e,r in zip(['0.5','0.2','0.1','0.05','0.02'],rs):
    print('epsilon',e,'rho',mp.nstr(r,23),'tau',mp.nstr(2*r/3,23))
