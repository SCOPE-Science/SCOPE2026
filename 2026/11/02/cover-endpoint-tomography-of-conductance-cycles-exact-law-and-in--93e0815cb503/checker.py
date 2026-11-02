"""Exact finite-state checks for the last-coverage law on conductance cycles.

Only Python's standard library is needed. This checker complements, but does
not replace, the general algebraic and stopping-time proofs.
"""
from fractions import Fraction as F
from random import Random
import json


def last_probability(r, start, target):
    n = len(r)
    assert n >= 3 and start != target and all(x > 0 for x in r)
    left, right = (target + 1) % n, (target - 1) % n
    path = [left]
    while path[-1] != right:
        path.append((path[-1] + 1) % n)
    assert len(path) == n - 1 and start in path
    total = sum((r[v] for v in path[:-1]), F(0))
    distance = sum((r[v] for v in path[:path.index(start)]), F(0))
    return ((total - distance) / total * r[target] / (total + r[target])
            + distance / total * r[right] / (total + r[right]))


def gauss_solve(a, b):
    n = len(b)
    aa = [list(row) + [value] for row, value in zip(a, b)]
    for k in range(n):
        p = next((i for i in range(k, n) if aa[i][k] != 0), None)
        if p is None:
            raise ArithmeticError("unexpected singular hitting-time system")
        aa[k], aa[p] = aa[p], aa[k]
        piv = aa[k][k]
        aa[k][k:] = [v / piv for v in aa[k][k:]]
        for i in range(n):
            if i != k and aa[i][k]:
                z = aa[i][k]
                for h in range(k, n + 1):
                    aa[i][h] -= z * aa[k][h]
    return [aa[i][-1] for i in range(n)]


def independent_markov_probability(r, start, target):
    """Independent first-step solve, remembering which target-neighbors were hit."""
    n = len(r)
    left, right = (target + 1) % n, (target - 1) % n
    states = [(pos, f) for pos in range(n) if pos != target for f in range(3)]
    idx = {st: i for i, st in enumerate(states)}
    m = len(states)
    a = [[F(i == j) for j in range(m)] for i in range(m)]
    b = [F(0)] * m
    for (pos, flags), row in idx.items():
        denom = 1/r[pos] + 1/r[(pos-1) % n]
        for nxt, edge in (((pos + 1) % n, pos), ((pos - 1) % n, (pos-1) % n)):
            prob = (1/r[edge]) / denom
            new = flags | (1 if nxt == left else 0) | (2 if nxt == right else 0)
            if nxt == target:
                continue
            if new == 3:
                b[row] += prob
            else:
                a[row][idx[(nxt,new)]] -= prob
    flags = (1 if start == left else 0) | (2 if start == right else 0)
    return gauss_solve(a, b)[idx[(start, flags)]]


def inverse_resistances(q):
    n = len(q)
    prod = F(1)
    for x in q:
        prod *= x
    denominator = 1 - (-1)**n * prod
    out = []
    for i in range(n):
        summand_product = F(1)
        total = F(0)
        for k in range(n):
            summand_product *= q[(i+k) % n]
            total += (-1)**k * summand_product
        out.append(total / denominator)
    return out


def main():
    rng = Random(260101)
    checks = 0
    cases = 0
    for n in range(3, 7):
        for repeat in range(5):
            r = [F(rng.randint(1, 9), rng.randint(1, 7)) for _ in range(n)]
            total = sum(r)
            q = [last_probability(r, i, (i+1) % n) for i in range(n)]
            restored = inverse_resistances(q)
            for i in range(n):
                assert q[i] == r[i] / (total - r[(i+1) % n]); checks += 1
                assert restored[i] == r[i] / total; checks += 1
                assert 0 < q[i] < 1; checks += 1
            assert sum(restored) == 1; checks += 1
            for s in range(n):
                values = [last_probability(r,s,j) for j in range(n) if j!=s]
                assert sum(values) == 1; checks += 1
                for j in range(n):
                    if j == s:
                        continue
                    expected = last_probability(r, s, j)
                    actual = independent_markov_probability(r, s, j)
                    assert expected == actual, (n,r,s,j,expected,actual)
                    checks += 1
                    cases += 1
        # Verify the inverse consistency criterion and local stability bound.
        r0 = [F(i+1) for i in range(n)]
        r1 = [F(i+2) for i in range(n)]
        q0 = [last_probability(r0,i,(i+1)%n) for i in range(n)]
        q1 = [last_probability(r1,i,(i+1)%n) for i in range(n)]
        rho0, rho1 = inverse_resistances(q0), inverse_resistances(q1)
        assert all(x>0 for x in rho0+rho1); checks += 1
        assert sum(rho0)==sum(rho1)==1; checks += 1
        dq = max(abs(a-b) for a,b in zip(q0,q1))
        dr = max(abs(a-b) for a,b in zip(rho0,rho1))
        qmax = max(q0+q1)
        assert dr <= dq/(1-qmax); checks += 1
        one = [F(1)]*n
        assert all(last_probability(one,s,j)==F(1,n-1)
                   for s in range(n) for j in range(n) if s!=j)
        checks += n*(n-1)
    nonrealizable = [F(1,2)]*4
    assert sum(inverse_resistances(nonrealizable)) != 1
    checks += 1
    return {"status":"passed", "exact_assertions":checks,
            "independent_hitting_system_cases":cases,
            "parameter_sizes":[3,4,5,6],
            "example_four_cycle":{
                "resistances":[1,1,1,2],
                "clockwise_neighbor_last_probabilities":[str(last_probability([F(1),F(1),F(1),F(2)],i,(i+1)%4)) for i in range(4)],
                "recovered_normalized_resistances":[str(z) for z in inverse_resistances([last_probability([F(1),F(1),F(1),F(2)],i,(i+1)%4) for i in range(4)])]
            }}

if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, separators=(',',':')))
