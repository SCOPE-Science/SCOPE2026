"""Exact finite checks for a one-step random-walk attachment tree rare event."""
from collections import defaultdict
from fractions import Fraction
from math import isclose


def state_step(state):
    parents, old_center, new_center = state
    n = len(parents)
    neighbors = [set() for _ in range(n)]
    for v in range(1, n):
        u = parents[v] - 1
        neighbors[u].add(v)
        neighbors[v].add(u)
    distribution = {}
    for u in range(n):
        distribution[u] = sum((Fraction(1, n * len(neighbors[v])) for v in neighbors[u]), Fraction(0))
    assert sum(distribution.values()) == 1
    for v, weight in distribution.items():
        nxt = parents + (v + 1,)
        if n == 2:
            a, b = v + 1, 0
        elif new_center == 0 and v + 1 != old_center:
            a, b = old_center, v + 1
        elif new_center > 0 and v + 1 not in (old_center, new_center):
            a, b = old_center, -1
        else:
            a, b = old_center, new_center
        yield (nxt, a, b), weight


def enumeration(max_n=8):
    current = {((0, 1), 0, 0): Fraction(1)}
    outputs = {}
    for n in range(2, max_n + 1):
        if n >= 3:
            star = Fraction(0)
            small = defaultdict(Fraction)
            for (parents, old, new), probability in current.items():
                degrees = [0] * n
                for v in range(1, n):
                    u = parents[v] - 1
                    degrees[u] += 1
                    degrees[v] += 1
                nonleaves = [v for v, d in enumerate(degrees) if d > 1]
                if len(nonleaves) == 1:
                    star += probability
                    assert old == nonleaves[0] + 1 and new == 0
                if len(nonleaves) == 2:
                    assert new > 0 and old > 0
                    assert {old, new} == {x + 1 for x in nonleaves}
                    b = degrees[new - 1] - 1
                    assert b >= 1
                    small[b] += probability
                if new == -1:
                    assert len(nonleaves) >= 3
            outputs[n] = (star, dict(small))
            assert star == Fraction(2, n - 1)
            assert sum(current.values()) == 1
        if n == max_n:
            break
        later = defaultdict(Fraction)
        for state, probability in current.items():
            for nxt, weight in state_step(state):
                later[nxt] += probability * weight
        current = later
    return outputs


def recursion(max_n=8):
    q = {3: {}}
    for n in range(3, max_n):
        next_q = defaultdict(Fraction)
        for b, mass in q[n].items():
            a = n - 2 - b
            assert a >= 1
            next_q[b] += mass * (Fraction(a, n) + Fraction(1, n * (b+1)))
            next_q[b+1] += mass * (Fraction(b, n) + Fraction(1, n * (a+1)))
        next_q[1] += Fraction(2, n*(n-1))
        q[n+1] = dict(next_q)
    return q


def main():
    observations = enumeration(8)
    theory = recursion(8)
    checks = 0
    for n, (star, small) in observations.items():
        assert star == Fraction(2, n-1); checks += 1
        for b in range(1, n-2):
            assert small.get(b, 0) == theory[n].get(b, 0); checks += 1
        print(f'n={n}: star={star}, double_star={sum(small.values()):.10f}, diameter_at_most_3={float(star+sum(small.values())):.10f}')
    # Independent floating-point recurrence probes the two limits, not proof of them.
    limit = 5000
    q = [0.0] * limit
    for n in range(3, limit):
        nxt = [0.0] * limit
        for b in range(1, n-2):
            a = n-2-b
            nxt[b] += q[b] * (a + 1/(b+1)) / n
            nxt[b+1] += q[b] * (b + 1/(a+1)) / n
        nxt[1] += 2/(n*(n-1))
        q = nxt
    n = limit
    assert abs(n*(2/(n-1) + sum(q)) - 5) < .01; checks += 1
    for b in range(1, 8):
        assert abs(n*q[b] - 4/(b*(b+2))) < .003; checks += 1
    print('large_n=',limit,'nP(diam<=3)=',n*(2/(n-1)+sum(q)))
    print('exact checks and asymptotic probes:', checks)

if __name__ == '__main__':
    main()
