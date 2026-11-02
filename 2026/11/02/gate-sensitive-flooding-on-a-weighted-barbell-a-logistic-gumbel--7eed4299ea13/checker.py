"""Reproducible exact checks for first-passage flooding on a one-bridge barbell.
Only the Python standard library is required.
"""
from fractions import Fraction
from functools import lru_cache
from math import gamma, log


def graph_expectation(n, beta, source_gate=False):
    """Exact mean from infected-count states and the marked bridge endpoint."""
    beta = Fraction(beta)
    @lru_cache(None)
    def e(k, g, j):
        if k == n and j == n:
            return Fraction(0)
        transitions = []
        left_rate = Fraction(k * (n - k), n)
        if k < n:
            if not g:
                transitions += [(Fraction(k, n), (k + 1, True, j)),
                                (Fraction(k * (n - k - 1), n), (k + 1, False, j))]
            else:
                transitions.append((left_rate, (k + 1, True, j)))
        if j == 0 and g:
            transitions.append((beta, (k, True, 1)))
        if 0 < j < n:
            transitions.append((Fraction(j * (n-j), n), (k, g, j + 1)))
        positive = [(rate, state) for rate, state in transitions if rate > 0]
        total = sum((rate for rate, _ in positive), Fraction(0))
        return (1 + sum((rate * e(*state) for rate, state in positive), Fraction(0))) / total
    return e(1, bool(source_gate), 0)


def rank_conditioned_expectation(n, beta, target_rank):
    """Exact mean via independent clique discovery processes and fixed gate rank."""
    beta = Fraction(beta)
    q = target_rank
    @lru_cache(None)
    def e(k, right):
        if k == n and right == n:
            return Fraction(0)
        transitions = []
        if k < n:
            transitions.append((Fraction(k*(n-k), n), (k+1, right)))
        if k >= q and right == 0:
            transitions.append((beta, (k, 1)))
        if right > 0 and right < n:
            transitions.append((Fraction(right*(n-right), n), (k, right+1)))
        total = sum((rate for rate, _ in transitions), Fraction(0))
        return (1 + sum((rate * e(*state) for rate, state in transitions), Fraction(0))) / total
    return e(1, 0)


def finite_mgf_clique(n, s):
    """Exact product evaluated in float, centered at 2 log(n)."""
    terms = [k * (n-k) / n for k in range(1, n)]
    return __import__('math').exp(sum(-__import__('math').log1p(-s/r) for r in terms)-2*s*log(n))


def finite_mgf_gate(n, s):
    """Centered target-hitting transform, average over uniform infection ranks."""
    from math import exp, log1p
    terms = [k*(n-k)/n for k in range(1,n)]
    partial = 0.
    logs = []
    for r in terms:
        partial += -log1p(-s/r)
        logs.append(partial)
    shift = max(logs)
    return exp(shift - s*log(n))*sum(exp(v-shift) for v in logs)/(n-1)


def main():
    count=0
    for n in range(2,9):
        for b in (Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(3)):
            direct = graph_expectation(n, b, False)
            by_rank = sum((rank_conditioned_expectation(n,b,j) for j in range(2,n+1)), Fraction(0))/(n-1)
            assert direct == by_rank, ('source', n, b, direct, by_rank)
            count += 1
            assert graph_expectation(n,b,True) == rank_conditioned_expectation(n,b,1)
            count += 1
            harmonic=sum((Fraction(1,k) for k in range(1,n)), Fraction(0))
            lower=Fraction(n,n-1)*harmonic+Fraction(1,b)+2*harmonic
            assert direct >= lower
            count += 1
    for n in (100,1000,10000):
        for s in (-.25,.25):
            h=finite_mgf_gate(n,s)
            f=finite_mgf_clique(n,s)
            hlim=gamma(1-s)**2*gamma(1+s)
            flim=gamma(1-s)**2
            assert abs(h-hlim)<0.034
            assert abs(f-flim)<0.01
            count+=2
    print('CHECKS_PASS',count)
    print('n=6, beta=1, non-gate mean=',graph_expectation(6,1))
    print('n=6, beta=1, gate mean=',graph_expectation(6,1,True))
    print('limit mean shift=',3*0.5772156649015329+1)
    print('limit variance=',5*3.141592653589793**2/6+1)

if __name__=='__main__': main()
