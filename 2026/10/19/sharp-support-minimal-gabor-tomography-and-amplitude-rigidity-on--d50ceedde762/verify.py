"""Finite checks for the minimal-support Gabor operator-frame theorem.

Run with Python 3 standard library: python verify.py
The proof in RESULT.md applies beyond these checked examples.
"""
import cmath
import itertools
import math


DIFFERENCE_SETS = {
    7: (1, 2, 4),
    13: (0, 1, 3, 9),
    31: (0, 1, 3, 8, 12, 18),
}


def ambiguity(window, shift, modulation):
    n = len(window)
    root = cmath.exp(2j * math.pi / n)
    return sum(window[x].conjugate() * root ** (modulation * x)
               * window[(x - shift) % n] for x in range(n))


def make_window(n, support, magnitudes):
    w = [0j] * n
    for i, x in enumerate(support):
        w[x] = math.sqrt(magnitudes[i]) * cmath.exp(1j * (x*x + 3*x + 2*i) / 3)
    return w


def close(a, b, tol=3e-9):
    return abs(a-b) < tol


def check_operator_action(w):
    n = len(w)
    root = cmath.exp(2j * math.pi / n)
    errors = 0
    # Check the eigen-equation on every Weyl matrix, against all projector measurements.
    projectors = []
    for s, m in itertools.product(range(n), repeat=2):
        f = [root ** (m*x) * w[(x-s) % n] for x in range(n)]
        projectors.append([[f[x]*f[y].conjugate() for y in range(n)] for x in range(n)])
    for t, b in itertools.product(range(n), repeat=2):
        target = [[(root ** (b*x) if (x-y) % n == t else 0j)
                   for y in range(n)] for x in range(n)]
        eig = n * abs(ambiguity(w, t, b))**2
        output = [[0j for _ in range(n)] for _ in range(n)]
        for P in projectors:
            coeff = sum(P[y][x] * target[x][y] for x in range(n) for y in range(n))
            for x in range(n):
                for y in range(n):
                    output[x][y] += coeff * P[x][y]
        for x in range(n):
            for y in range(n):
                assert close(output[x][y], eig*target[x][y]), (n,t,b,x,y,output[x][y],eig*target[x][y])
                errors += 1
    return errors


def run():
    checks = 0
    for n, support in DIFFERENCE_SETS.items():
        k = len(support)
        assert n == k*(k-1)+1
        differences = [(x-y) % n for x in support for y in support if x != y]
        assert sorted(differences) == list(range(1,n)), (n, differences)
        weights = [1/k] * k
        w = make_window(n,support,weights)
        data = [n*abs(ambiguity(w,t,b))**2 for t in range(n) for b in range(n)]
        for t in range(n):
            for b in range(n):
                target = n if (t,b)==(0,0) else n*(k-1)/k**2 if t==0 else n/k**2
                assert close(data[t*n+b],target), (n,t,b,data[t*n+b],target)
                checks += 1
        # A non-flat probability distribution with all positive entries has strictly worse stability.
        p = [1/k + (k-1)/(4*k)] + [1/k-1/(4*k)]*(k-1)
        assert close(sum(p),1)
        g = make_window(n,support,p)
        eig = [n*abs(ambiguity(g,t,b))**2 for t in range(n) for b in range(n)]
        variance = sum((u-1/k)**2 for u in p)
        bound = n/k**2 - n*variance/(k*(k-1))
        assert min(eig) <= bound + 2e-9 and min(eig)<n/k**2-1e-8
        for t in range(1,n):
            pair = next((x,y) for x in support for y in support if (x-y)%n == t)
            prod = p[support.index(pair[0])] * p[support.index(pair[1])]
            for b in range(n):
                assert close(abs(ambiguity(g,t,b))**2,prod)
                checks += 1
        # The sharp variance coefficient is witnessed asymptotically by concentrated weights.
        epsilon=1e-6
        pc = [1-(k-1)*epsilon] + [epsilon]*(k-1)
        concentrated = make_window(n,support,pc)
        eigsmall = min(n*abs(ambiguity(concentrated,t,b))**2 for t in range(n) for b in range(n))
        assert close(eigsmall,n*epsilon**2, tol=1e-9), (n,eigsmall)
        var = sum((u-1/k)**2 for u in pc)
        ratio = (n/k**2-eigsmall)/(n*var)
        assert abs(ratio-1/(k*(k-1)))<3e-5
        print(f"v={n} k={k} ambiguity_eigenvalues={n*n} difference_test=PASS variance=PASS")
    n=7
    w=make_window(n, DIFFERENCE_SETS[n],[1/3]*3)
    entries=check_operator_action(w)
    print(f"VERIFY_OK ambiguity_comparisons={checks} exact_difference_families=3 operator_entries={entries} eigen_equations=49")


if __name__=='__main__':
    run()
