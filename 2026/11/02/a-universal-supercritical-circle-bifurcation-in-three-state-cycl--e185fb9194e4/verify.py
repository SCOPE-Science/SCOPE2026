"""Standalone algebraic and finite numerical checks for a cyclic softmax map.

Run with Python 3, NumPy and SymPy. Finite tests supplement, not replace,
the analytic local bifurcation argument.
"""
import math
import numpy as np
import sympy as sp

omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
z, w = sp.symbols('z w')
y = [(z * omega ** (-j) + w * omega ** j) / 3 for j in range(3)]
weighted = lambda values: sp.simplify(sum(omega ** j * values[j] for j in range(3)))
q = sp.simplify(sum(t * t for t in y))
checks = 0
assert sp.simplify(q - 2*z*w/3) == 0; checks += 1
assert sp.simplify(weighted(y) - z) == 0; checks += 1
assert sp.simplify(weighted([v*v for v in y]) - w*w/3) == 0; checks += 1
assert sp.simplify(weighted([v**3-q*v for v in y]) + q*z/2) == 0; checks += 1

# This is the normal-form coefficient after elimination of a nonresonant
# quadratic conjugate mode. All tests use exact arithmetic.
for eps in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4)):
    lam = (1-eps)+eps*omega
    rr2 = sp.simplify(sp.expand_complex(lam*sp.conjugate(lam)))
    rr = sp.sqrt(rr2)
    a = sp.simplify(lam/rr)
    b = a/(2*rr)
    c = -a/(2*rr2)
    assert sp.simplify(a*sp.conjugate(a)-1) == 0; checks += 1
    pp = sp.simplify(b/(sp.conjugate(a)**2-a))
    d = sp.simplify(c+2*b*sp.conjugate(pp))
    assert sp.simplify(sp.re(sp.expand_complex(d/a)) + sp.Rational(3,4)/rr2) == 0; checks += 1

# Exact special half-rotation: multiplier e^(i*pi/3), quadratic change -1/2,
# resonant cubic coefficient -3 times the linear rotation.
eps = sp.Rational(1,2)
lam = (1-eps)+eps*omega
rot = sp.simplify(lam/sp.sqrt(lam*sp.conjugate(lam)))
coef_b = rot
p = sp.simplify(coef_b/(sp.conjugate(rot)**2 - rot))
g = sp.simplify(-2*rot + 2*coef_b*sp.conjugate(p))
assert sp.simplify(rot-(sp.Rational(1,2)+sp.I*sp.sqrt(3)/2)) == 0; checks += 1
assert sp.simplify(p+sp.Rational(1,2)) == 0; checks += 1
assert sp.simplify(g+3*rot) == 0; checks += 1

omega_num = np.exp(2j*np.pi/3)
P = np.roll(np.eye(3),1,axis=0)
# P x=(x_2,x_0,x_1), and z(Px)=omega*z(x).
assert np.max(np.abs(P@np.array([1.,2.,3.])-np.array([3.,1.,2.])))<1e-15; checks += 1

def softmax_map(x, beta, eps):
    e = beta*np.asarray(x)
    v = np.exp(e-e.max()); v /= v.sum()
    return ((1-eps)*np.eye(3)+eps*P)@v

def z_of(x):
    return x[0] + omega_num*x[1] + omega_num**2*x[2]

for eps in (.2,.5,.8):
    r = math.sqrt(1-3*eps+3*eps*eps)
    beta0 = 3/r
    xeq=np.ones(3)/3
    for beta in (.99*beta0, beta0, 1.01*beta0):
        assert np.max(np.abs(softmax_map(xeq,beta,eps)-xeq))<2e-15; checks += 1
        val=beta*r/3
        assert abs(val - (beta/beta0))<1e-14; checks += 1
    # Independent complex Taylor comparison at small nonzero Fourier coordinate.
    for zz in (.001+.0003j, -.0008+.0012j):
        yy=np.array([(zz*omega_num**(-j)+zz.conjugate()*omega_num**j).real/3 for j in range(3)])
        xx=xeq+yy
        zz2=z_of(softmax_map(xx,beta0,eps))
        target=((1-eps)+eps*omega_num)*(
            (beta0/3)*zz + (beta0**2/18)*zz.conjugate()**2
            -(beta0**3/54)*zz*abs(zz)**2)
        assert abs(zz2-target)<10*abs(zz)**4; checks += 1

# A numerical check of critical n^{-1/2} and of supercritical radius, only
# in the epsilon=1/2 specialization; the theorem uses normal-form theory.
for beta in (6., 6.02, 6.05):
    x=np.array([1/3+.03,1/3-.015,1/3-.015])
    radii=[]
    for n in range(70000):
        x=softmax_map(x,beta,.5)
        if n>=69000:
            radii.append(abs(z_of(x)))
    if beta==6.:
        measured=math.sqrt(6*70000)*radii[-1]
        assert .93<measured<1.07, measured; checks += 1
    else:
        ratio=np.mean(np.array(radii)**2)/(beta-6)
        assert abs(ratio-1/18)<.003, (beta,ratio); checks += 1

print('PASS: {} exact/symbolic and finite numerical assertions'.format(checks))
