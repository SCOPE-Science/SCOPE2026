"""Reproducible symbolic checks for the acute-facet metric moment identities.

Requires sympy==1.14.0. The exact integrations below are a finite symbolic
certificate supplementing, rather than replacing, the geometric derivation.
"""
import sympy as sp

x, y, n = sp.symbols('x y n', positive=True, real=True)
s = sp.sin(x)*sp.sin(y)*sp.sin(x+y)
full = {1: 3*sp.pi/8, 2: 3*sp.pi**2/64, 3: 35*sp.pi/512}
acute = {1: 3*sp.pi/16,
         2: 3*sp.pi**2/256 + sp.Rational(3,16),
         3: 53*sp.pi/1024}
for power in (1,2,3):
    f = sp.expand_trig(s**power)
    jf = sp.simplify(sp.integrate(sp.integrate(f, (y, 0, sp.pi-x)), (x, 0, sp.pi)))
    ja = sp.simplify(sp.integrate(sp.integrate(f, (y, sp.pi/2-x, sp.pi/2)), (x, 0, sp.pi/2)))
    assert sp.simplify(jf-full[power]) == 0, ('full',power,jf)
    assert sp.simplify(ja-acute[power]) == 0, ('acute',power,ja)
    print('integrals', power, jf, ja)

ratios = (sp.Rational(1,2), sp.Rational(1,4)+4/sp.pi**2, sp.Rational(53,70))
for j in range(3):
    assert sp.simplify(acute[j+1]/full[j+1]-ratios[j]) == 0

# For a uniformly sampled facet, U=(1+H)/2 has Beta(n-1,2) density;
# E[(1-H^2)^j] = 4^j (n-1)_j (2)_j/(n+1)_{2j}.
def beta_radius_moment(j, k):
    return sp.factor(4**j*sp.rf(k-1,j)*sp.rf(2,j)/sp.rf(k+1,2*j))

def shape_moment(j, restrict=False):
    return sp.simplify(2**j*(acute if restrict else full)[j+1]/full[1])

for k in (4,5,7,12,40):
    H1=beta_radius_moment(1,k)
    H2=beta_radius_moment(2,k)
    A1=sp.factor((2*k-4)*H1*shape_moment(1))
    A1c=sp.factor((2*k-4)*H1*shape_moment(1,True))
    A2=sp.factor((2*k-4)*H2*shape_moment(2))
    A2c=sp.factor((2*k-4)*H2*shape_moment(2,True))
    assert sp.simplify(A1-4*sp.pi*(k-1)*(k-2)/((k+1)*(k+2))) == 0
    assert sp.simplify(A1c-(sp.pi**2+16)*(k-1)*(k-2)/(sp.pi*(k+1)*(k+2))) == 0
    assert sp.simplify(A2-140*k*(k-1)*(k-2)/((k+1)*(k+2)*(k+3)*(k+4))) == 0
    assert sp.simplify(A2c-106*k*(k-1)*(k-2)/((k+1)*(k+2)*(k+3)*(k+4))) == 0
    assert sp.simplify(A1c/A1-ratios[1]) == 0
    assert sp.simplify(A2c/A2-ratios[2]) == 0
    print('size',k,'S1',A1,'S1acute',A1c,'S2',A2,'S2acute',A2c)

# Independent triangular-domain quadrature using mpmath, not symbolic identities.
import mpmath as mp
mp.mp.dps=30
for power in (1,2,3):
    f=lambda t,u: (mp.sin(t)*mp.sin(u)*mp.sin(t+u))**power
    integral = mp.quad(lambda t:mp.quad(lambda u:f(t,u),[0,mp.pi-t]),[0,mp.pi])
    acint = mp.quad(lambda t:mp.quad(lambda u:f(t,u),[mp.pi/2-t,mp.pi/2]),[0,mp.pi/2])
    assert abs(integral-mp.mpf(str(sp.N(full[power],35)))) < mp.mpf('1e-23')
    assert abs(acint-mp.mpf(str(sp.N(acute[power],35)))) < mp.mpf('1e-23')
print('ALL_SYMBOLIC_AND_QUADRATURE_CHECKS_PASSED')
