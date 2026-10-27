"""Reproduce the three-hyperplane weighted-reflection spectral identities.

Requires Python 3, NumPy, and SymPy; run: python check.py
The numerical samples are diagnostics; the universal conclusion is analytic.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def optimum(c, d):
    assert 0 < d < 1 and 0 < c and 2*c*c < 1+d
    h = 1+d
    if c*c <= 2*d*d/h:
        z = d*(1-d)/(d-c*c)
        q = (2*d*d-(3*d-1)*c*c)/(2*d-h*c*c)
    else:
        z = h
        q = c*math.sqrt(2/h)
    H = np.array([[1, c, c], [c, 1, d], [c, d, 1]])
    B = np.sqrt([z, 1, 1])[:, None] * H * np.sqrt([z, 1, 1])[None, :]
    spectrum = np.linalg.eigvalsh(B)
    tau = 2/(spectrum[0]+spectrum[-1])
    return z, tau, q


def contraction(c, d, weights):
    H = np.array([[1,c,c],[c,1,d],[c,d,1]], dtype=float)
    weights = np.array(weights)
    eig = np.linalg.eigvalsh(np.sqrt(weights)[:,None]*H*np.sqrt(weights)[None,:])
    return max(abs(1-eig[0]),abs(1-eig[-1]))


def run():
    c,d,z = sp.symbols('c d z', real=True)
    G = sp.Matrix([[1,c,c],[c,1,d],[c,d,1]])
    assert sp.factor(G.det()) == (d-1)*(2*c*c-d-1)
    h = 1+d
    tauq = (2*d*d-(3*d-1)*c*c)/(2*d-h*c*c)
    z0 = d*(1-d)/(d-c*c)
    assert sp.simplify((z0+3*d-1)/(z0+d+1)-tauq) == 0
    threshold=2*d*d/h
    assert sp.simplify(tauq.subs(c*c,threshold)-2*d/h)==0

    d0=sp.Rational(1,2); c0=sp.Rational(1,4); z0x=sp.Rational(4,7)
    DD=sp.diag(sp.sqrt(z0x),1,1)
    eig=(DD*G.subs({c:c0,d:d0})*DD).eigenvals()
    assert eig=={sp.Rational(1,2):2,sp.Rational(11,7):1}, eig
    # Optimal weights are exactly (16,28,28)/29.
    exactweights=[sp.Rational(16,29),sp.Rational(28,29),sp.Rational(28,29)]
    assert set((sp.eye(3)-sp.diag(*[sp.sqrt(x) for x in exactweights]) * G.subs({c:c0,d:d0}) * sp.diag(*[sp.sqrt(x) for x in exactweights])).eigenvals())=={sp.Rational(15,29),-sp.Rational(15,29)}
    baseline=(3+sp.sqrt(3))/(7+sp.sqrt(3))
    assert sp.simplify(baseline-sp.Rational(15,29))>0

    random=np.random.default_rng(230519)
    checks=0
    for _ in range(350):
        dd=float(random.uniform(.02,.98)); cc=float(random.uniform(.001,.99*math.sqrt((1+dd)/2)))
        zz,tau,formula=optimum(cc,dd)
        achieved=contraction(cc,dd,(tau*zz,tau,tau))
        assert abs(achieved-formula)<5e-12,(dd,cc,formula,achieved)
        for _ in range(12):
            # Arbitrary strictly positive weights and global scalar relaxation.
            trial=np.exp(random.uniform(-4,4,size=3))
            Gnum=np.array([[1,cc,cc],[cc,1,dd],[cc,dd,1]])
            E=np.linalg.eigvalsh(np.sqrt(trial)[:,None]*Gnum*np.sqrt(trial)[None,:])
            adjusted=2/(E[0]+E[-1])
            competing=contraction(cc,dd,adjusted*trial)
            assert competing>=formula-2e-11,(dd,cc,formula,competing)
            checks+=1
        # A real nonsingular row matrix is realized by its Gram matrix.
        rows=np.linalg.cholesky(np.array([[1,cc,cc],[cc,1,dd],[cc,dd,1]]))
        iteration=np.eye(3)-rows.T @np.diag([tau*zz,tau,tau])@rows
        assert abs(np.linalg.norm(iteration,2)-formula)<5e-12
    print('PASS: exact determinant, transition identity, rational witness,',checks,'independent arbitrary-weight competitors, and 350 physical row-matrix checks')

if __name__ == '__main__':
    run()
