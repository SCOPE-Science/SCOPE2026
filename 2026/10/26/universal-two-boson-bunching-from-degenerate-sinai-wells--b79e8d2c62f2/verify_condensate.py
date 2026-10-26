"""Reproducible arithmetic checks for the random-well bosonic bunching law.

This program tests finite Markov detailed balance, Catalan decompositions, and
canonical occupation moments. It does not replace the infinite-limit proofs.
"""
from fractions import Fraction
from itertools import product
from math import comb
from decimal import Decimal, localcontext

CHECKS = 0

def ck(test, label):
    global CHECKS
    assert test, label
    CHECKS += 1

def comps(n, l):
    if l == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for rem in comps(n - j, l - 1):
                yield (j,) + rem

def steps_to_w(steps):
    xs = [0]
    for d in steps:
        xs.append(xs[-1] + d)
    low = min(xs)
    return tuple(Fraction(1, 2 ** (x - low)) for x in xs), sum(x == low for x in xs)

def detailed_balance(steps, n):
    ws, k = steps_to_w(steps)
    l = len(ws)
    energies = {eta: __import__('math').prod(w ** j for w, j in zip(ws, eta))
                for eta in comps(n, l)}
    Z = sum(energies.values(), Fraction(0, 1))
    corr = sum(weight * sum(j * (j - 1) for j in eta)
               for eta, weight in energies.items()) / (Z * n * (n - 1))
    for eta, a in energies.items():
        for edge, d in enumerate(steps):
            if eta[edge] > 0:
                out = list(eta)
                out[edge] -= 1
                out[edge + 1] += 1
                out = tuple(out)
                # Set h = log(2)/2, Q arbitrary: r_right/r_left=2^-d.
                check_ratio = Fraction(1, 2) if d == 1 else Fraction(2, 1)
                ck(a * check_ratio == energies[out], 'reversible ratio')
    ck(0 <= corr <= 1, 'pair probability bounds')
    return corr, k

def ext_min_count(steps):
    s = 0
    path = [s]
    for d in steps:
        s += d
        path.append(s)
    return path.count(min(path))

# The generating polynomial recursion F(t,z)=z(1-E(t))/((1-2t)(1-zE(t))).
# E(t)=sum_{m>=1}Catalan(m-1)*t^(2m).
for n in range(0, 13):
    empirical = {}
    for steps in product((-1, 1), repeat=n):
        k = ext_min_count(steps)
        empirical[k] = empirical.get(k, 0) + 1
    # Compute exact coefficients of the convolution (1-E) sum_j z^(j+1) E^j.
    N = n
    E = [0] * (N + 1)
    for m in range(1, N // 2 + 1):
        E[2 * m] = comb(2 * (m - 1), m - 1) // m
    poly = [1] + [0] * N
    result = {}
    for k in range(1, N + 2):
        # Coefficient of z^k: E^(k-1)*(1-E)/(1-2t)
        dis = [poly[i] - sum(poly[i - j] * E[j] for j in range(1, i + 1))
               for i in range(N + 1)]
        result[k] = sum(dis[i] * (2 ** (N - i)) for i in range(N + 1))
        newpoly = [0] * (N + 1)
        for i in range(N + 1):
            newpoly[i] = sum(poly[i - j] * E[j] for j in range(1, i + 1))
        poly = newpoly
    for k in range(1, N + 2):
        ck(result[k] == empirical.get(k, 0), 'Catalan minimum-visit polynomial')
    ck(sum(empirical.values()) == 2 ** n, 'sample-space count')

# Exact canonical detailed balance and pair probability for finite boson number.
for l in (2, 3, 4):
    for disorder in product((-1, 1), repeat=l-1):
        for N in (2, 3, 5, 8):
            exact, k = detailed_balance(disorder, N)
            ck(Fraction(0) <= exact <= 1, 'exact canonical expectation')

# Uniform-rate case has uniform weak-composition measures, yielding 2/(L+1).
for l in range(2, 9):
    n = 7
    Z = comb(n + l - 1, l - 1)
    pairnumer = sum(sum(j*(j-1) for j in eta) for eta in comps(n, l))
    ck(Fraction(pairnumer, Z*n*(n-1)) == Fraction(2, l+1), 'clean Dirichlet law')

# The disorder-averaged thermodynamic constant follows geometric(1/2) min multiplicity.
for cutoff in (20, 40, 80):
    v = sum(Fraction(2, (2**k)*(k+1)) for k in range(1, cutoff+1))
    with localcontext() as ctx:
        ctx.prec = 110
        error = 4 * Decimal(2).ln() - 2 - Decimal(v.numerator) / Decimal(v.denominator)
        ck(Decimal(0) < error < Decimal(2) ** (2-cutoff), 'geometric tail bound')

# Explicit high-density finite-L convergence for several sample configurations.
for disorder in ((1,1),(-1,-1),(1,-1),(-1,1)):
    vals=[]
    for N in (20,40,80,160):
        val, k = detailed_balance(disorder, N)
        vals.append(float(val))
    ck(abs(vals[-1]-2/(k+1)) < abs(vals[0]-2/(k+1)), 'large N convergence')
print(f'PASS: {CHECKS} exact or deterministic assertions')
