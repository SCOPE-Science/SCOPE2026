"""Supplementary finite sanity checks for the radial-complexity theorem.

The all-degree bounds and the arbitrary-node lower bound require the
analytical proof in RESULT.md; finite checks are not substitutes.
"""
import cmath
import math
import random

rng = random.Random(137)
checks = 0


def test(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def poisson_pmf(t, k):
    if t == 0:
        return float(k == 0)
    return math.exp(-t + k * math.log(t) - math.lgamma(k + 1))


def weights(N):
    J = math.isqrt(N)
    if J * J < N:
        J += 1
    return [(j, 2*j+1) for j in range(J+1)]


def eigenvalues(N):
    rings = weights(N)
    return [sum(weight * poisson_pmf(j*j, k) for j, weight in rings)
            for k in range(N+1)]


for N in [1, 2, 3, 4, 7, 9, 16, 31, 64, 100, 256, 512, 1000, 4096]:
    lam = eigenvalues(N)
    test(min(lam) > 0.2, 'lower eigenvalue')
    test(max(lam) < 8.0, 'upper eigenvalue')
    for k, eig in enumerate(lam):
        test(0.2 <= eig <= 8, f'eigenvalue N={N}, k={k}')

for N in range(1, 12):
    lam = eigenvalues(N)
    M = N+1
    samples = []
    for j, weight in weights(N):
        if j == 0:
            samples.append((0j, 1.0))
        else:
            for s in range(M):
                z = j * cmath.exp(2j*math.pi*s/M)
                samples.append((z, weight*math.exp(-j*j)/M))
    for trial in range(7):
        coefficients = [complex(rng.uniform(-1,1),rng.uniform(-1,1))
                        for _ in range(N+1)]
        def evalpoly(z):
            return sum(coefficients[k]*z**k/math.sqrt(math.factorial(k))
                       for k in range(N+1))
        discrete = sum(w*abs(evalpoly(z))**2 for z,w in samples)
        exact = sum(lam[k]*abs(coefficients[k])**2 for k in range(N+1))
        test(abs(discrete-exact) < 1e-7*(1+exact),
             f'angular diagonalization N={N}')
        norm = sum(abs(c)**2 for c in coefficients)
        test(0.2*norm < discrete < 8*norm, f'frame N={N}')

# Check the uniform single-Poisson truncated mass-to-maximum comparison.
for N in [1,2,3,5,10,25,100,400]:
    for t in [0, 0.2, 1, 2, N/2, N, N+1, 2*N, 10*N]:
        pmf = [poisson_pmf(t,k) for k in range(N+1)]
        test(sum(pmf) <= 3*math.e*math.sqrt(N+1)*max(pmf)+1e-13,
             f'Poisson width N={N}, t={t}')

print('PASS: ',checks,'finite assertions; all-degree proof is analytical.')
