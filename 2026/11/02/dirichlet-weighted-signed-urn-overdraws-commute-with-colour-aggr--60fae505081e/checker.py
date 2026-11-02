"""Exact-rational checks for Dirichlet-weighted signed urn draws.

No external dependencies; uses only the Python standard library. The analytic
proof is separate, and these tests are finite consistency checks only.
"""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def compositions(n, total):
    if n == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(n - 1, total - a):
                yield (a,) + tail


def rising(a, r):
    z = 1
    for i in range(r):
        z *= a + i
    return z


def moment(alpha, powers):
    num = 1
    for a, p in zip(alpha, powers):
        num *= rising(a, p)
    return F(num, rising(sum(alpha), sum(powers)))


def multi(v):
    z = factorial(sum(v))
    den = 1
    for t in v:
        den *= factorial(t)
    return z // den


def solve(a, rhs):
    n = len(a)
    a = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(a)]
    for j in range(n):
        i = next(k for k in range(j, n) if a[k][j])
        a[j], a[i] = a[i], a[j]
        factor = a[j][j]
        a[j] = [v / factor for v in a[j]]
        for i in range(n):
            if i == j: continue
            factor = a[i][j]
            if factor:
                a[i] = [v - factor * w for v, w in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


@lru_cache(None)
def signed_hist(alpha, beta, k):
    n = len(alpha)
    m = sum(beta)
    basis = tuple(compositions(n, m))
    gram = [[multi(a)*multi(b)*moment(alpha,tuple(x+y for x,y in zip(a,b))) for b in basis] for a in basis]
    coefficients = solve(gram, [F(a == beta) for a in basis])
    result = {}
    for gamma in compositions(n, k):
        result[gamma] = sum((c*multi(a)*multi(gamma)*moment(alpha, tuple(x+y for x,y in zip(a,gamma)))
            for a,c in zip(basis,coefficients)), F(0))
    return result


def aggregate(h, groups):
    ans = {}
    for gamma, w in h.items():
        delta = tuple(sum(gamma[i] for i in group) for group in groups)
        ans[delta] = ans.get(delta, F(0)) + w
    return ans


def merged(v, groups):
    return tuple(sum(v[i] for i in g) for g in groups)


def check():
    assertions = 0
    for n, alpha, mm in [
        (3, (1,1,1), 3), (3, (1,2,3), 3),
        (3, (2,3,1), 3), (4, (1,1,1,1), 2),
        (4, (2,1,2,1), 2),
    ]:
        groups = ((0,1),) + tuple((i,) for i in range(2,n))
        a2 = merged(alpha,groups)
        for m in range(mm+1):
            for beta in compositions(n,m):
                for k in range(0,m+3):
                    h = signed_hist(alpha,beta,k)
                    assert sum(h.values()) == 1
                    assertions+=1
                    if k <= m:
                        for gamma,prob in h.items():
                            expected = F(1, comb(m,k))
                            for b,g in zip(beta,gamma):
                                expected *= comb(b,g) if g<=b else 0
                            assert prob == expected
                            assertions+=1
                    got = aggregate(h,groups)
                    goal = signed_hist(a2,merged(beta,groups),k)
                    assert got == goal, (n,alpha,beta,k,got,goal)
                    assertions+=1
    # Intrinsic choice alpha=beta stays consistent on full-support urns.
    for beta in [(1,1,1),(2,1,1),(1,2,2),(1,1,1,1)]:
        n=len(beta)
        groups=((0,1),)+tuple((i,) for i in range(2,n))
        for k in range(sum(beta)+3):
            fine=signed_hist(beta,beta,k)
            coarse=signed_hist(merged(beta,groups),merged(beta,groups),k)
            assert aggregate(fine,groups)==coarse
            assertions+=1
    # Sharp all-positive full-support first-overdraw obstruction.
    fine = aggregate(signed_hist((1,1,1),(1,1,1),4), ((0,1),(2,)))
    corrected = signed_hist((2,1),(2,1),4)
    unweighted = signed_hist((1,1),(2,1),4)
    expected_fine = [F(1,18),F(-2,9),F(1,3),F(10,9),F(-5,18)]
    expected_unweighted = [F(17,210),F(-34,105),F(17,35),F(106,105),F(-53,210)]
    assert [fine[(j,4-j)] for j in range(5)] == expected_fine
    assert [unweighted[(j,4-j)] for j in range(5)] == expected_unweighted
    assert corrected == fine
    assert sum(abs(fine[k]-unweighted[k]) for k in fine)/2 == F(64,315)
    assertions+=4
    # Orthogonal-projection short certificate for the single-colour event.
    for alpha,expected in [((1,2),F(1,18)),((1,1),F(17,210))]:
        H = [[moment(alpha,(i+j,0)) for j in range(4)] for i in range(4)]
        c = solve(H,[-moment(alpha,(i+4,0)) for i in range(4)])
        assert -c[0]-c[1]/3 == expected
        assertions += 1
    print(f"PASS: {assertions} exact-rational assertions; weighted aggregation, hypergeometric conservativity, normalization, and sharp obstruction")


if __name__ == '__main__':
    check()
