"""Reproduce symbolic identities and numerical stress tests for the sharp
orthogonal-system mean-square momentum frontier of randomized multi-reflection DR.
Requires sympy and numpy. Run: python verify.py
"""
import itertools
import math
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0

def check(x, label):
    global checks
    if not bool(x):
        raise AssertionError(label)
    checks += 1

alpha, beta, q, z = sp.symbols('alpha beta q z')
mu = 1 - 2 * alpha*q
v = 1 - 4 * alpha * (1-alpha)*q
sig2 = sp.expand(v - mu**2)
check(sp.simplify(sig2 - 4*alpha**2*q*(1-q)) == 0, 'Bernoulli variance')

M = sp.Matrix([
    [v + 2*beta*mu + beta**2, -2*beta*(mu+beta), beta**2],
    [mu+beta, -beta, 0],
    [1, 0, 0],
])
p = sp.Poly(sp.expand(M.charpoly(z).as_expr()), z)
check(sp.factor(p.eval(1) - 4*alpha*q*(1-alpha-beta**2+alpha*beta*(2*q-1)))==0,
      'covariance characteristic value at unity')
B = sp.Matrix([[mu+beta, -beta], [1, 0]])
x, y, w = sp.symbols('x y w')
W = sp.Matrix([[x,y],[y,w]])
Eq = B*W*B.T + sp.diag(1,0)-W
sol = sp.solve([Eq[0,0],Eq[0,1],Eq[1,1]], [x,y,w], dict=True)[0]
G = sp.factor(sol[x]); G_formula = sp.factor((1+beta)/((1-beta)*(1-mu)*(1+mu+2*beta)))
check(sp.simplify(G-G_formula)==0, 'discrete Lyapunov impulse energy')
check(sp.simplify((1-sig2*G)*((1-beta)*(1-alpha*q+beta))-(1-alpha-beta**2+alpha*beta*(2*q-1)))==0,
      'rank-one small-gain stability identity')

# Enumerating independent reflection choices checks the parity reduction
# directly against the probability formula for every coordinate.
for n in (2,3,4):
    for r in range(1,6):
        expectation = Fraction(0,1)
        for sample in itertools.product(range(n), repeat=r):
            parity = sum(j==0 for j in sample)%2
            expectation += Fraction(parity, n**r)
        predicted = (1-Fraction(n-2,n)**r)/2
        check(expectation==predicted, f'parity n={n}, r={r}')

# Nonasymptotic matrix-moment recurrence tested against exact enumeration
# through three time steps for one coordinate and arbitrary memory.
for n,r in ((2,1),(2,3),(3,2),(4,4)):
    qr=float((1-Fraction(n-2,n)**r)/2)
    for a in (0.2,0.5,0.8):
        for b in (0.0,0.2,0.6):
            aa=float(1-2*a*qr)
            vv=float(1-4*a*(1-a)*qr)
            T=np.array([[vv+2*b*aa+b*b,-2*b*(aa+b),b*b],
                        [aa+b,-b,0],[1,0,0]],float)
            # at each stage t_1=t_0=1 and all subsequent steps independent
            states=[(1.,1.,1.)]
            for k in range(3):
                states2=[]
                for prob,cur,old in states:
                    for weight,c in ((1-qr,1.),(qr,1-2*a)):
                        nex=(c+b)*cur-b*old
                        states2.append((prob*weight,nex,cur))
                states=states2
                vec=np.array([sum(prob*cur*cur for prob,cur,old in states),
                              sum(prob*cur*old for prob,cur,old in states),
                              sum(prob*old*old for prob,cur,old in states)])
                if k==0:
                    run=T@np.array([1.,1.,1.])
                else:
                    run=T@run
                check(np.allclose(vec,run,rtol=5e-12,atol=5e-12),f'moment n={n} r={r} a={a} b={b} k={k}')

for n in (2,3,4,7,15):
    for r in (1,2,3,6,12):
        qr=(1-(1-2/n)**r)/2
        for a in (0.08,0.25,0.5,0.75,0.93):
            critical=(-a*(1-2*qr)+math.sqrt(a*a*(1-2*qr)**2+4*(1-a)))/2
            check(0<critical<1,'strict threshold')
            check(abs(1-a-critical**2+a*critical*(2*qr-1))<1e-12,'root equation')
            for fraction,desired in ((0.,True),(.2,True),(.9,True),(1.1,False),(1.3,False)):
                b=fraction*critical
                mu1=1-2*a*qr
                vv=1-4*a*(1-a)*qr
                T=np.array([[vv+2*b*mu1+b*b,-2*b*(mu1+b),b*b],
                            [mu1+b,-b,0],[1,0,0]],float)
                rho=max(abs(np.linalg.eigvals(T)))
                check((rho<1)==desired,f'boundary n={n},r={r},a={a},b={b},rho={rho}')

# Sharp local acceleration sign as relaxation crosses one half.
lam0 = v
p_deriv_beta = sp.diff(p.as_expr(),beta)
p_deriv_z = sp.diff(p.as_expr(),z)
lamprime = sp.factor(-p_deriv_beta.subs({beta:0,z:lam0}) / p_deriv_z.subs({beta:0,z:lam0}))
expected_first = 4*alpha*q*(1-2*alpha*q)*(2*alpha-1)/v
check(sp.factor(lamprime-expected_first)==0,'local spectral radius derivative')
lamsecond = sp.factor(-(
    sp.diff(p.as_expr(),beta,2).subs({beta:0,z:lam0})
    + 2*sp.diff(p.as_expr(),beta,z).subs({beta:0,z:lam0})*lamprime
    + sp.diff(p.as_expr(),z,2).subs({beta:0,z:lam0})*lamprime**2
    ) /p_deriv_z.subs({beta:0,z:lam0}))
check(sp.factor(lamsecond.subs(alpha,sp.Rational(1,2))-2*q/(1-q))==0,
      'quadratic strict worsening at half relaxation')

qhalf=sp.Rational(1,2)
special=sp.factor(p.eval(1).subs({alpha:sp.Rational(1,2),q:qhalf}))
check(sp.simplify(special-(sp.Rational(1,2)-beta**2))==0, 'two-row critical polynomial')
b0=(sp.sqrt(3)-1)/4
check(sp.N(b0)<sp.N(1/sp.sqrt(2)),'source sufficient condition is strict subset')
check(sp.simplify((sp.Rational(1,2)+4*b0**2+2*b0)-1)==0,'source sufficient cutoff')
print(f'PASS: {checks} deterministic assertions; symbolic identities, enumerations, exact moments, stability margins')
print('Example: alpha=1/2, m=2, all r, critical beta=1/sqrt(2)=',float(1/math.sqrt(2)))
print('Source Theorem 4.1 sufficient beta cutoff=',float(b0))
