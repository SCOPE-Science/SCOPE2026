"""Exact-integer finite checks of the three-/four-agent Global Pair bounds.

This program corroborates an independent all-metric analytical proof; finite
metric enumeration cannot establish the universal theorem by itself.
"""
from itertools import combinations, product


def pair_cost(d, reports, a, b):
    return sum(min(d[i][a], d[i][b]) for i in reports)


def mechanism_num_den(d, reports):
    num = den = 0
    for a, b in combinations(reports, 2):
        delta = d[a][b]
        den += delta
        num += delta * pair_cost(d, reports, a, b)
    return num, den


def opt_centers(d, reports):
    return min(pair_cost(d, reports, a, b)
               for a, b in combinations(range(len(d)), 2))


def valid_metric(d):
    n = len(d)
    return all(d[i][j] <= d[i][k] + d[k][j]
               for i in range(n) for j in range(n) for k in range(n))


def metric_from_edges(n, vals):
    d = [[0] * n for _ in range(n)]
    for (i, j), w in zip(combinations(range(n), 2), vals):
        d[i][j] = d[j][i] = w
    return d


def test(n, domain, include_external_center=False):
    reports = tuple(range(n - int(include_external_center)))
    examined = 0
    positive = 0
    for vals in product(domain, repeat=n*(n-1)//2):
        d = metric_from_edges(n, vals)
        if not valid_metric(d):
            continue
        examined += 1
        num, den = mechanism_num_den(d, reports)
        opt = opt_centers(d, reports)
        if opt == 0:
            assert num == 0, (n, vals, 'zero optimal cost')
            continue
        positive += 1
        if len(reports) == 3:
            assert 2 * num <= 3 * den * opt, (n, vals, num, den, opt)
        elif len(reports) == 4:
            assert num <= 2 * den * opt, (n, vals, num, den, opt)
        else:
            raise AssertionError('unexpected population')
    return examined, positive


def test_graph_shortest_paths(n, domain):
    count = positive = 0
    reports = tuple(range(4))
    for vals in product(domain, repeat=n*(n-1)//2):
        d = metric_from_edges(n, vals)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        count += 1
        num, den = mechanism_num_den(d, reports)
        opt = opt_centers(d, reports)
        if opt == 0:
            assert num == 0
        else:
            positive += 1
            assert num <= 2 * den * opt, (n, vals, num, den, opt)
    return count, positive


def tightness():
    for e in (1, 2, 5, 10, 100, 1000):
        # The n=3 line family (0,1,e+1) has ratio 3/2 -1/(e+1).
        d3 = [[0, 1, e + 1], [1, 0, e], [e + 1, e, 0]]
        num3, den3 = mechanism_num_den(d3, range(3))
        opt3 = opt_centers(d3, range(3))
        assert 2*(e+1)*num3 == (3*e+1)*den3*opt3
        # The n=4 line family (0,e,e+1,e+2), e >= 2.
        if e >= 2:
            x = (0,e,e+1,e+2)
            d4 = [[abs(u-v) for v in x] for u in x]
            num4, den4 = mechanism_num_den(d4, range(4))
            opt4 = opt_centers(d4, range(4))
            assert (num4, den4, opt4) == (12*e+13, 3*e+7, 2)

if __name__ == '__main__':
    a = test(3,range(5))
    b = test(4,range(5))
    c = test_graph_shortest_paths(5,range(1,4))
    tightness()
    print(f'VERIFY_OK three_report_metrics={a} four_report_metrics={b} '
          f'five_location_graph_metrics={c} sharp_families=verified')
