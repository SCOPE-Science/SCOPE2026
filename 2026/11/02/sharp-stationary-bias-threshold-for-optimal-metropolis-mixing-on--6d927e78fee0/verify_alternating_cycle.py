"""Independent finite-dimensional checks for the alternating-cycle mixing theorem.

Requires NumPy. Run: python verify_alternating_cycle.py
Exact all-dimension proof is in RESULT.md; these tests do not establish it.
"""
import math
import random
import numpy as np

SEED = 78131
R = random.Random(SEED)

def formula(m, r):
    s2 = math.sin(math.pi / m)**2
    delta = (1+r) - math.sqrt((1+r)**2 - 4*r*s2)
    threshold = 1 - s2/2
    alpha0 = 2 / (2*(1+r)+delta)
    alpha = min(.5, alpha0)
    mu = max(1-delta*alpha, abs(1-2*(1+r)*alpha))
    return alpha, mu, threshold, delta


def matrix(m, r, edge_flows):
    # Choose unnormalized masses r at even sites, 1 at odd sites.
    n = 2*m
    pi = np.array([r if j%2 == 0 else 1 for j in range(n)])
    P = np.zeros((n,n))
    for j,c in enumerate(edge_flows):
        k = (j+1)%n
        P[j,k] += c/pi[j]
        P[k,j] += c/pi[k]
    for j in range(n):
        P[j,j] = 1 - sum(P[j,:])
    assert np.min(P) >= -1e-10
    assert np.max(np.abs(P @ np.ones(n) - np.ones(n))) < 1e-10
    assert np.max(np.abs(pi @ P - pi)) < 1e-10
    S = np.sqrt(pi)[:,None] * P / np.sqrt(pi)[None,:]
    assert np.max(np.abs(S-S.T)) < 1e-11
    vals = np.linalg.eigvalsh(S)
    assert abs(vals[-1]-1) < 1e-10
    return max(abs(vals[:-1])), vals


def run_checks():
    checks = 0
    # Direct finite-dimensional diagonalization over widely varied dimensions and masses.
    for m in range(2,25):
        for r in [0.01,0.1,0.25,0.5,0.67,0.78,0.9,0.99,1.0]:
            alpha,mu,threshold,g = formula(m,r)
            val, ev = matrix(m,r,[r*alpha]*(2*m))
            assert abs(val-mu) < 5e-11, (m,r,val,mu)
            checks += 1
            # Independent scalar exhaustive grid approximation to the one-variable minimum.
            grid = np.linspace(0,0.5,1001)
            brute = min(max(1-g*a,abs(1-2*(1+r)*a)) for a in grid)
            assert mu <= brute+1e-11
            assert brute-mu < 0.0025
            checks += 1
            # Metropolis is the optimum precisely on the predicted side.
            metro,_=matrix(m,r,[r/2]*(2*m))
            if r<=threshold+1e-13:
                assert abs(metro-mu)<5e-11
            else:
                assert metro>mu+1e-12
            checks += 1

    # Independent random *asymmetric* reversible chains; no random trial beats the theorem.
    for m in range(2,13):
        n=2*m
        for r in [0.13,0.57,0.83,0.995]:
            optimum=formula(m,r)[1]
            for k in range(90):
                # Raw positive conductances and a global feasibility scaling.
                c=[R.random()*R.random() for _ in range(n)]
                masses=[r if j%2==0 else 1.0 for j in range(n)]
                scale=min(masses[j]/(c[j-1]+c[j]) for j in range(n))
                c=[(0.01+.99*R.random())*scale*x for x in c]
                trial,_=matrix(m,r,c)
                assert trial>=optimum-1e-10, (m,r,k,trial,optimum)
                checks+=1

    # Exact rational checks of the boundary ratio for m=2,3,4,6.
    from fractions import Fraction
    sin2={2:Fraction(1),3:Fraction(3,4),4:Fraction(1,2),6:Fraction(1,4)}
    for m,s2 in sin2.items():
        threshold=1-s2/2
        assert abs(formula(m,float(threshold))[2]-float(threshold))<1e-14
        checks+=1

    print(f'PASSED: {checks} reproducible finite-dimensional checks')


if __name__ == "__main__":
    run_checks()
