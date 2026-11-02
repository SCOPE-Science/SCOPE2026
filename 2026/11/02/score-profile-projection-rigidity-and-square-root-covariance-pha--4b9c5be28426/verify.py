"""Independent exact enumeration for score-class and directed-cycle covariance.

Python 3 standard library only. This verifies finite cases, not the general proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, isqrt


def falling(n, r):
    return factorial(n) // factorial(n-r)


def expected_cycles(n, r):
    return Fraction(falling(n, r), r * 2**r)


def target_covariance(n, r, k):
    N = n - 1
    return (Fraction(falling(n, r), 2**r)
            * Fraction(comb(N, k), 2**N)
            * Fraction(N - (2*k-N)**2, N*(N-1)))


def target_coefficient(n, r):
    return Fraction(falling(n-3, r-3), 2**(r-3))


def enumerate_case(n):
    edges = list(combinations(range(n), 2))
    cycles = {}
    for r in range(3, n+1):
        cr = []
        for nodes in combinations(range(n), r):
            x = nodes[0]
            for tail in permutations(nodes[1:]):
                sequence = (x,) + tail
                cr.append(tuple(zip(sequence, sequence[1:] + (x,))))
        assert len(cr) == falling(n, r)//r
        cycles[r] = cr

    total = 1 << len(edges)
    d_sum = [0]*n
    c_sum = {r:0 for r in cycles}
    cd_sum = {(r,k):0 for r in cycles for k in range(n)}
    sample_assertions = 0
    examples = defaultdict(lambda: [0,0])
    for mask in range(total):
        directed = [[False]*n for _ in range(n)]
        deg = [0]*n
        for bit, (i,j) in enumerate(edges):
            if mask & (1<<bit):
                directed[i][j] = True
                deg[i] += 1
            else:
                directed[j][i] = True
                deg[j] += 1
        hist = [deg.count(k) for k in range(n)]
        tri = comb(n,3) - sum(comb(s,2) for s in deg)
        counts = {r:sum(all(directed[a][b] for a,b in cycle)
                      for cycle in cc) for r,cc in cycles.items()}
        assert tri == counts[3]
        sample_assertions += 1
        for k in range(n):
            d_sum[k] += hist[k]
        for r, val in counts.items():
            c_sum[r] += val
            for k in range(n):
                cd_sum[r,k] += val * hist[k]
        if n==4:
            key = tuple(sorted(deg))
            examples[key][0] += 1
            examples[key][1] += counts[4]
    for r in cycles:
        assert Fraction(c_sum[r], total) == expected_cycles(n,r)
        for k in range(n):
            empirical = (Fraction(cd_sum[r,k],total)
                        - Fraction(c_sum[r]*d_sum[k],total**2))
            assert empirical == target_covariance(n,r,k), (n,r,k,empirical,target_covariance(n,r,k))
            identity = target_coefficient(n,r) * target_covariance(n,3,k)
            assert empirical == identity
            sample_assertions += 2
    if n==4:
        assert Fraction(*examples[(0,1,2,3)][::-1]) == 0
        assert (expected_cycles(4,4)
                + target_coefficient(4,4)*(0-expected_cycles(4,3))) == Fraction(-1,8)
        sample_assertions += 2
    return sample_assertions


def verify_arithmetic_signs():
    checks = 0
    for n in range(3,121):
        N = n-1
        roots = []
        for k in range(n):
            polynomial = N-(2*k-N)**2
            exact = target_covariance(n,n,k)
            assert (exact>0)-(exact<0) == (polynomial>0)-(polynomial<0)
            if exact == 0: roots.append(k)
            checks += 1
        square = isqrt(N)
        expected = sorted([(N-square)//2,(N+square)//2]) if square*square==N else []
        assert roots == expected, (n,roots,expected)
        checks += 1
    return checks

if __name__ == '__main__':
    count = 0
    for n in range(3,7):
        checks=enumerate_case(n)
        print(f'complete tournament enumeration n={n}: {1<<(n*(n-1)//2)} orientations, {checks} assertions')
        count += checks
    sign_checks=verify_arithmetic_signs()
    count+=sign_checks
    print(f'sign and square-boundary checks: {sign_checks}')
    print(f'PASS: {count} exact assertions; all n<=6 tournaments exhausted, arithmetic signs n<=120')
