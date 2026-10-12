from math import comb, factorial

def ordered_matchings(labels):
    labels = tuple(labels)
    if len(labels) <= 1:
        return {()}
    out = set()
    # The first pair is an unordered pair, but the sequence of pairs is ordered.
    for ai in range(len(labels)):
        for bi in range(ai + 1, len(labels)):
            a, b = labels[ai], labels[bi]
            pair = tuple(sorted((a, b)))
            rest = labels[:ai] + labels[ai+1:bi] + labels[bi+1:]
            for tail in ordered_matchings(rest):
                out.add((pair,) + tail)
    return out

brute_checks = 0
for n in range(2, 11):
    pts = ordered_matchings(tuple(range(n)))
    expected = factorial(n) // (2 ** (n // 2))
    assert len(pts) == expected, (n, len(pts), expected)
    # Every label occurs once, except one residual label in odd dimension.
    for seq in pts:
        used = [x for pair in seq for x in pair]
        assert len(used) == 2 * (n // 2)
        assert len(set(used)) == len(used)
    brute_checks += 1

rec = {0: 1, 1: 1}
recurrence_checks = 0
for n in range(2, 81):
    rec[n] = comb(n, 2) * rec[n-2]
    expected = factorial(n) // (2 ** (n // 2))
    assert rec[n] == expected, (n, rec[n], expected)
    recurrence_checks += 1

# Distinct pair weights for the binary-separated one-parameter subgroup.
weight_checks = 0
for n in range(2, 31):
    weights = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            w = (2 ** i) + (2 ** j)
            assert w not in weights, (n, i, j, weights.get(w))
            weights[w] = (i, j)
            weight_checks += 1

print('VERIFY_OK', brute_checks, recurrence_checks, weight_checks)
