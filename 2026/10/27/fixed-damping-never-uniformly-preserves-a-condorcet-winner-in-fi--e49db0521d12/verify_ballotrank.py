"""Exact-rational checks of a five-alternative BallotRank counterexample family.

Uses only Python's standard library. Run: python verify_ballotrank.py
"""
from fractions import Fraction as Q

ALTERNATIVES = "ABCDE"
RUNNERS = "BCDE"
EDGES = (("B", "C"), ("B", "D"), ("E", "B"),
         ("C", "D"), ("C", "E"), ("D", "E"))


def ballots(k):
    assert isinstance(k, int) and k >= 1
    out = []
    for x, y in EDGES:
        z = [v for v in RUNNERS if v not in (x, y)]
        gadget = (x + y + "".join(z), "".join(z[::-1]) + x + y)
        for _ in range(k):
            for ranking in gadget:
                out.extend(("A" + ranking, ranking + "A"))
    out.append("ABCDE")
    assert len(out) == 24 * k + 1
    return out


def winning_margins(votes):
    n = len(ALTERNATIVES)
    index = [{x: r.index(x) for x in ALTERNATIVES} for r in votes]
    w = [[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a, b = ALTERNATIVES[i], ALTERNATIVES[j]
            margin = sum(1 if v[a] < v[b] else -1 for v in index)
            w[i][j] = Q(max(0, margin))
            w[j][i] = Q(max(0, -margin))
    return w


def ballotrank_transition(votes):
    w = winning_margins(votes)
    n = len(ALTERNATIVES)
    wins = [sum(w[i], Q(0)) for i in range(n)]
    grand_total = sum(wins, Q(0))
    assert grand_total > 0
    for i in range(n):
        w[i][i] = wins[i] / grand_total
    col = [sum((w[i][j] for i in range(n)), Q(0)) for j in range(n)]
    assert all(x > 0 for x in col)
    L = [[w[i][j] / col[j] for j in range(n)] for i in range(n)]
    assert all(sum((L[i][j] for i in range(n)), Q(0)) == 1 for j in range(n))
    return L


def solve(a, rhs):
    n = len(rhs)
    rows = [list(a[i]) + [rhs[i]] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        fac = rows[j][j]
        rows[j] = [v / fac for v in rows[j]]
        for i in range(n):
            if i != j:
                fac = rows[i][j]
                rows[i] = [rows[i][t] - fac * rows[j][t] for t in range(n + 1)]
    return [rows[i][-1] for i in range(n)]


def ballotrank(k, d):
    assert Q(0) < d < Q(1)
    L = ballotrank_transition(ballots(k))
    n = len(ALTERNATIVES)
    A = [[Q(i == j) - d * L[i][j] for j in range(n)] for i in range(n)]
    right = [Q(1 - d, n) for i in range(n)]
    scores = solve(A, right)
    assert sum(scores, Q(0)) == 1
    assert all(x > 0 for x in scores)
    assert all(sum((L[i][j] * scores[j] for j in range(n)), Q(0)) * d + Q(1 - d, n) == scores[i] for i in range(n))
    return scores


def limiting_B(d):
    D = d**3 + 4 * d**2 + 4 * d + 4
    return (d**3 + 5 * d**2 + 6 * d + 4) / (5 * D)


def run():
    tests = 0
    for k in (1, 2, 5, 10, 25, 50, 100):
        margins = winning_margins(ballots(k))
        for i in range(1, 5):
            assert margins[0][i] == 1 and margins[i][0] == 0
            tests += 1
        for x, y in EDGES:
            i, j = ALTERNATIVES.index(x), ALTERNATIVES.index(y)
            expected = 4 * k + (1 if (x, y) != ("E", "B") else -1)
            assert margins[i][j] == expected and margins[j][i] == 0
            tests += 1
    d = Q(17, 20)
    s = ballotrank(25, d)
    difference = Q(2462202045070872571152, 1625203582777781791390465)
    assert s[1] - s[0] == difference > 0
    tests += 1
    for k, d in ((10,Q(1,4)), (10,Q(1,2)), (25,Q(17,20)), (50,Q(9,10)), (500,Q(99,100))):
        assert ballotrank(k, d)[1] > ballotrank(k, d)[0]
        tests += 1
    for d in (Q(1,100), Q(1,4), Q(1,2), Q(17,20), Q(99,100)):
        b = limiting_B(d)
        D = d**3 + 4*d**2 + 4*d + 4
        assert b - Q(1,5) == d*(d+2)/(5*D) > 0
        tests += 1
    print(f"PASS: {tests} exact-rational majority, stationarity and limiting-formula assertions")
    print(f"d=17/20, k=25, voters=601: B-A={difference}")
    print(f"d=17/20 limiting: B-A={limiting_B(Q(17,20))-Q(1,5)}")


if __name__ == '__main__':
    run()
