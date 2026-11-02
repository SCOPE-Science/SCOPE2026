"""Reproduce algebraic and numerical checks for priced biclique conductance allocation.

Run: python check_biclique.py
Dependencies: numpy, scipy, sympy. All random draws have a fixed seed.
These tests corroborate, but do not replace, the proof for arbitrary p and q.
"""
import numpy as np
from scipy.optimize import brentq, minimize
from sympy import Matrix, Rational


def solve(p, q, prices, budget=1.0):
    prices = np.asarray(prices, dtype=float)
    assert p >= 2 and q >= 2 and len(prices) == p
    assert np.all(prices > 0) and budget > 0
    n = p + q
    target = n * q * (q - 1) / (n - 1)
    low = min(prices)
    def equation(alpha):
        return alpha * np.sum((prices - alpha) ** (-0.5)) ** 2 - target
    alpha = brentq(equation, 0., np.nextafter(low, 0.), xtol=1e-14)
    v = (prices - alpha) ** (-0.5)
    total = np.dot(prices, v)
    conductances = budget * v / (q * total)
    optimum = (n - 1) * total ** 2 / budget
    return alpha, conductances, optimum


def laplacian(matrix):
    p, q = matrix.shape
    n = p + q
    L = np.zeros((n,n))
    for i in range(p):
        for j in range(q):
            w = matrix[i,j]
            L[i,i] += w
            L[p+j,p+j] += w
            L[i,p+j] -= w
            L[p+j,i] -= w
    return L


def total_resistance(matrix):
    eig = np.linalg.eigvalsh(laplacian(matrix))
    if eig[1] < 1e-13:
        return float('inf')
    return len(eig) * np.sum(1/eig[1:])


def exact_identity():
    p, q = 3, 4
    aa = [Rational(1,3), Rational(2,5), Rational(4,7)]
    s = sum(aa)
    n = p + q
    L = Matrix.zeros(n)
    for i in range(p):
        for j in range(q):
            z = p+j
            L[i,i] += aa[i]
            L[z,z] += aa[i]
            L[i,z] -= aa[i]
            L[z,i] -= aa[i]
    P = Matrix.ones(n) / n
    pinv = (L+P).inv()-P
    observed = sum(pinv[i,i]+pinv[j,j]-2*pinv[i,j]
                   for i in range(n) for j in range(i+1,n))
    derived = Rational(n-1,q)*sum(1/t for t in aa) + Rational(n*(q-1),1)/s
    assert observed == derived == Rational(29559,1096)
    return str(observed)


def main():
    print('Exact-rational K_3,4 resistance:', exact_identity())
    rng = np.random.default_rng(20261026)
    spectra = 0
    budget_tests = 0
    asym_tests = 0
    for p in range(2,6):
        for q in range(2,6):
            for rep in range(6):
                prices = np.exp(rng.normal(size=p))
                budget = float(np.exp(rng.normal()))
                alpha, ai, predicted = solve(p,q,prices,budget)
                assert 0 < alpha < min(prices)
                assert abs(q*np.dot(prices,ai)-budget)<1e-10*budget
                matrix = np.tile(ai[:,None],(1,q))
                actual = total_resistance(matrix)
                assert abs(predicted/actual-1)<1e-9
                spectra += 1
                # A feasible perturbation that changes each edge separately.
                for _ in range(25):
                    raw = rng.uniform(0.1,1.8,size=(p,q))
                    raw *= budget/np.sum(prices[:,None]*raw)
                    observed = total_resistance(raw)
                    assert observed >= predicted*(1-1e-9)
                    asym_tests += 1
                # Directional derivative against classwise constraints.
                A=(p+q-1)/q
                C=(p+q)*(q-1)
                marginal = (A/ai**2+C/sum(ai)**2)/prices
                assert np.max(marginal)-np.min(marginal) < 1e-7*max(marginal)
                budget_tests += 1
    print('Spectral class checks:',spectra)
    print('Independent asymmetric feasible comparisons:',asym_tests)
    print('Budget and KKT checks:',budget_tests)
    solves=0
    for p,q,prices in [(2,2,[1,4]),(3,4,[1,4,9]),(4,3,[2,3,5,11]),(3,3,[1,2,4])]:
        alpha, ai, predicted = solve(p,q,prices)
        price_matrix=np.repeat(np.asarray(prices)[:,None],q,axis=1)
        def objective(x):return total_resistance(x.reshape(p,q))
        x0=np.ones(p*q)/np.sum(price_matrix)
        result=minimize(objective,x0,method='SLSQP',bounds=[(1e-9,None)]*(p*q),
                        constraints=[{'type':'eq','fun':lambda x:np.dot(price_matrix.ravel(),x)-1}],
                        options={'ftol':1e-11,'maxiter':600})
        assert result.success and abs(result.fun/predicted-1)<1e-8
        solves += 1
    print('Unrestricted numerical optimizer comparisons:',solves)
    p=3;price=np.array([1.,4.,9.]);budget=1.
    for q in [100,1000,3000]:
        alpha,aa,val=solve(p,q,price,budget)
        print('asymptotic q=',q,'q^2*(rho_min-alpha)=',q*q*(1-alpha),
              'min-price budget fraction=',q*aa[0],
              'q^2 other conductances=',list(q*q*aa[1:]),
              'optimum/q^3=',val/q**3)
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
