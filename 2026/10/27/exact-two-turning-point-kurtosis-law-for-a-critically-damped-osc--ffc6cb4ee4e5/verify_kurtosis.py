#!/usr/bin/env python3
"""Exact moment and optional regenerative covariance checks for a critically damped oscillator."""
import sympy as sp

q, u, z, rho = sp.symbols('q u z rho', positive=True)
D = sp.Integer(1)
monomials = (q, u, z)
moments = {(0, 0, 0): sp.Integer(1)}
determinants = {}

# L = u d_q + (-q-2u+z) d_u + d_{zz} + rho(reset z to zero - I).
for degree in (1, 2, 3, 4):
    powers = [(a, b, degree-a-b) for a in range(degree+1) for b in range(degree-a+1)]
    matrix = sp.zeros(len(powers))
    rhs = sp.zeros(len(powers), 1)
    for row, (a,b,c) in enumerate(powers):
        f = q**a*u**b*z**c
        generator = sp.Poly(sp.expand(u*sp.diff(f,q) + (-q-2*u+z)*sp.diff(f,u)
                                    + sp.diff(f,z,2) + rho*(f.subs(z,0)-f)), q,u,z)
        for exp, coefficient in generator.terms():
            if sum(exp) == degree:
                matrix[row, powers.index(exp)] += coefficient
            else:
                rhs[row] -= coefficient * moments[exp]
    if degree in (2,4):
        determinants[degree] = sp.factor(matrix.det())
    solution = list(next(iter(sp.linsolve((matrix, rhs)))))
    for exp, value in zip(powers, solution):
        moments[exp] = sp.factor(value)

assert determinants[2] == 8*rho*(rho+1)**2
assert determinants[4] == -1024*rho*(rho+1)**2*(rho+2)**3*(rho+3)**4
A = 4*rho**7+173*rho**6+1217*rho**5+3722*rho**4+6112*rho**3+5739*rho**2+2835*rho+486
B = 105*rho**7+838*rho**6+2603*rho**5+3942*rho**4+2995*rho**3+1230*rho**2+729*rho+486
P = 105*rho**9+311*rho**8-2675*rho**7-17181*rho**6-39613*rho**5-42611*rho**4-16077*rho**3+8901*rho**2+10692*rho+2916
v2 = moments[(0,2,0)]
v4 = moments[(0,4,0)]
assert sp.simplify(v2-1/(1+rho)**2) == 0
assert sp.simplify(v4 - 3*A/(4*rho*(rho+1)**3*(rho+2)**3*(rho+3)**4)) == 0
# Two independent half-amplitude wall contributions, each with the same law.
two_var = sp.factor(v2/2)
two_fourth = sp.factor((2*v4+6*v2**2)/16)
kurtosis = sp.factor(two_fourth/two_var**2-3)
assert sp.simplify(kurtosis - 3*B/(8*rho*(rho+2)**3*(rho+3)**4)) == 0
assert sp.simplify(sp.diff(kurtosis,rho) + 3*P/(8*rho**2*(rho+2)**4*(rho+3)**5)) == 0
assert sp.limit(rho*kurtosis,rho,0,dir='+') == sp.Rational(9,32)
assert sp.limit(rho*kurtosis,rho,sp.oo) == sp.Rational(315,8)
assert P.subs(rho,sp.Rational(1,4))>0 and P.subs(rho,2)<0 and P.subs(rho,10)>0
signs = [sp.sign(c) for c in sp.Poly(P,rho).all_coeffs()]
assert sum(x!=y for x,y in zip(signs,signs[1:])) == 2
roots = [float(sp.re(z)) for z in sp.nroots(P,maxsteps=300) if abs(float(sp.im(z)))<1.e-8 and float(sp.re(z))>0]
assert len(roots)==2 and .59<roots[0]<.60 and 6.48<roots[1]<6.49
print('Exact homogeneous moment matrices and rational moment formulas: PASS')
print('Two-wall fourth-cumulant and derivative identities: PASS')
print('Exactly two positive roots by Descartes plus three sign tests: PASS')
print('Small/large reset-rate asymptotics: PASS')
for root in roots:
    print(f'critical rate={root:.12f}, excess kurtosis={float(kurtosis.subs(rho,root)):.12f}')

try:
    import numpy as np
except ImportError:
    print('Independent regenerative Monte Carlo: NOT RUN (numpy unavailable)')
else:
    # Independent conditional-Gaussian method; evolves covariance over exact jump intervals.
    # This does not use any fourth-moment recurrence.
    proj = np.diag([1.,1.,0.])
    def FQ(t):
        e = np.exp(-t); e2=e*e
        F = np.array([[(1+t)*e,t*e,1-(1+t)*e],[-t*e,(1-t)*e,t*e],[0.,0.,1.]])
        qxx=(-2*t*t-6*t-5)*e2/2+4*(t+2)*e+(4*t-11)/2
        qxv=(t*t+2*t+1)*e2-2*(t+1)*e+1
        qxz=2*(t*e+t-2+2*e)
        qvv=.5-(t*t+t+.5)*e2
        qvz=2*(1-(t+1)*e)
        Q=np.array([[qxx,qxv,qxz],[qxv,qvv,qvz],[qxz,qvz,2*t]])
        return F,Q
    for rate in (.30,6.4842):
        rng=np.random.default_rng(456)
        cov=np.zeros((3,3)); variances=[]
        for epoch in range(15000):
            wait=float(rng.exponential(1/rate))
            F,Q=FQ(wait)
            cov=F@cov@F.T+Q
            if epoch>=1000:variances.append(float(cov[1,1]))
            cov=proj@cov@proj
        arr=np.asarray(variances)
        sample_k=3*arr.var()/arr.mean()**2
        theoretical=float((2*kurtosis).subs(rho,rate))
        assert abs(sample_k-theoretical)/theoretical < .11, (rate,sample_k,theoretical)
        print(f'Independent conditional-covariance MC rate={rate:g}: {sample_k:.6f} vs exact {theoretical:.6f}: PASS')
