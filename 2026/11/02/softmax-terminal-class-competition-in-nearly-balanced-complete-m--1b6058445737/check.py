"""Independent finite-state and asymptotic checks for multipartite cover competition.

Run with Python 3 using only the standard library. These finite checks do not
replace the probability proof of the asymptotic statements.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import math
import random

ASSERTIONS = 0

def check(condition, explanation):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(explanation)


def linear_solve(A, B):
    """Exact Gaussian elimination, A square; B multiple right-hand sides."""
    n = len(A)
    m = len(B[0])
    tab = [list(A[i]) + list(B[i]) for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if tab[i][c] != 0)
        tab[c], tab[p] = tab[p], tab[c]
        scale = tab[c][c]
        tab[c] = [z / scale for z in tab[c]]
        for i in range(n):
            if i != c:
                mul = tab[i][c]
                tab[i] = [u-mul*v for u,v in zip(tab[i],tab[c])]
    return tuple(tuple(tab[i][n:]) for i in range(n))


def exact_last_class(part_sizes, starting_class=0):
    """Exact last-discovered class law, by visited-count Markov states."""
    sizes = tuple(part_sizes)
    k = len(sizes)
    total = sum(sizes)
    @lru_cache(None)
    def get(v):
        A = [[F(int(i == j)) for j in range(k)] for i in range(k)]
        B = [[F(0) for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if i == j:
                    continue
                denom = total - sizes[i]
                A[i][j] -= F(v[j], denom)
                if v[j] == sizes[j]:
                    continue
                w = F(sizes[j]-v[j], denom)
                v2 = list(v)
                v2[j] += 1
                v2 = tuple(v2)
                if sum(v2) == total:
                    B[i][j] += w
                else:
                    rest = get(v2)[j]
                    for h in range(k):
                        B[i][h] += w * rest[h]
        return linear_solve(A, B)
    initial = tuple(int(i == starting_class) for i in range(k))
    return get(initial)[starting_class]


def brute_walk(sizes, start, rng):
    k = len(sizes)
    total = sum(sizes)
    visited = [set() for _ in sizes]
    visited[start].add(0)
    seen = 1
    current = start
    while seen < total:
        z = rng.randrange(total - sizes[current])
        nextpart = next(i for i in range(k) if i != current and
                        (z := z - sizes[i]) < 0)
        vertex = rng.randrange(sizes[nextpart])
        if vertex not in visited[nextpart]:
            visited[nextpart].add(vertex)
            seen += 1
            if seen == total:
                return nextpart
        current = nextpart
    raise RuntimeError('impossible')


def test():
    for sizes,expected in [
        ((1,1,1),(F(0),F(1,2),F(1,2))),
        ((2,2,2),(F(23,105),F(41,105),F(41,105))),
        ((1,2,3),(F(0),F(45879,198835),F(152956,198835))),
    ]:
        actual = exact_last_class(sizes)
        check(actual == expected, f'exact law failed: {sizes}: {actual}')
        check(sum(actual) == 1, f'not normalized: {sizes}')
        rng = random.Random(221902)
        nsim = 15000
        counts = [0]*len(sizes)
        for _ in range(nsim):
            counts[brute_walk(sizes,0,rng)] += 1
        for i,prob in enumerate(actual):
            check(abs(counts[i]/nsim - float(prob)) < .019,
                  f'Monte Carlo for {sizes}, class {i} inconsistent')
    for k in range(3,8):
        for n in [100,500,10000]:
            sizes = [n + (j*17 % 19) for j in range(k)]
            N = sum(sizes)
            S = sum(q*(N-q) for q in sizes)
            pi = [F(q*(N-q), S) for q in sizes]
            P = [[F(0) if i==j else F(sizes[j],N-sizes[i])
                  for j in range(k)] for i in range(k)]
            check(sum(pi) == 1,'stationary vector total')
            for j in range(k):
                check(sum(pi[i]*P[i][j] for i in range(k)) == pi[j],
                      'stationary class chain')
    for k in range(3,7):
        theta = [-.5, 0., 1.] + [0.]*(k-3)
        Th = sum(theta)
        A = (k-2)*Th/(k*(k-1))
        errors = []
        for n in (10**5,10**7,10**9):
            sizes = [round(n + q*n/math.log(n)) for q in theta]
            N = sum(sizes)
            S = sum(q*(N-q) for q in sizes)
            pi = [q*(N-q)/S for q in sizes]
            x=.33
            t = k*n*(math.log(n)+A+x)
            off = [(p*t-q*math.log(q))/q for p,q in zip(pi,sizes)]
            err = max(abs(a-(x-v/(k-1))) for a,v in zip(off,theta))
            errors.append(err)
        check(errors[0] > errors[1] > errors[2],
              f'critical-window analytic normalization failed: {k}')
        check(errors[2]<.052, 'critical-window offset too large')
        weights=[math.exp(q/(k-1)) for q in theta]
        check(abs(sum(q/sum(weights) for q in weights)-1)<1e-14,
              'softmax probabilities do not normalize')
    print(f'PASS: {ASSERTIONS} exact, stochastic and asymptotic checks')

if __name__ == '__main__':
    test()
