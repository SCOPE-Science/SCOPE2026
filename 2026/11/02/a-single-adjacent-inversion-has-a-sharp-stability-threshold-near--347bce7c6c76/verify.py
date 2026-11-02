"""Exact independent enumeration for the one-adjacent-inversion stable-roommates law.

Only standard-library Python is required: python verify.py
All preferences are strict and complete. This finite checker complements the proof.
"""
from itertools import combinations


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        remaining = tuple(v for v in vertices[1:] if v != b)
        for tail in matchings(remaining):
            yield ((a, b),) + tail


def stable(rank, matching):
    partner = {}
    for a, b in matching:
        partner[a], partner[b] = b, a
    for a, b in combinations(range(len(rank)), 2):
        if partner[a] == b:
            continue
        if rank[a][b] < rank[a][partner[a]] and rank[b][a] < rank[b][partner[b]]:
            return False
    return True


def predicted_matching(n, agent, position):
    base = [tuple((j, j+1)) for j in range(0, n, 2)]
    row = [a for a in range(n) if a != agent]
    left, right = row[position:position+2]
    # The only changes to the canonical pairing occur when the deviator is
    # the first member of a canonical pair and trades their partner for the
    # first member of the next pair.
    if agent % 2 == 0 and left == agent + 1 and right == agent + 2:
        base[agent//2: agent//2+2] = [(agent, agent+2), (agent+1, agent+3)]
    return frozenset(frozenset(p) for p in base)


def run():
    for n in (4, 6, 8, 10):
        all_matchings = list(matchings(tuple(range(n))))
        profiles = failures = changed = nonunique = 0
        for agent in range(n):
            for position in range(n-2):
                profiles += 1
                lists = [[j for j in range(n) if j != i] for i in range(n)]
                lists[agent][position], lists[agent][position+1] = (
                    lists[agent][position+1], lists[agent][position]
                )
                ranks = [{j: index for index, j in enumerate(row)} for row in lists]
                valid = [frozenset(frozenset(pair) for pair in matching)
                         for matching in all_matchings if stable(ranks, matching)]
                expected_failure = (agent % 2 == 1 and agent < n-1
                                    and position == agent-1)
                assert (not valid) == expected_failure, (n, agent, position)
                if expected_failure:
                    failures += 1
                else:
                    if len(valid) != 1:
                        nonunique += 1
                    assert len(valid) == 1, (n, agent, position, valid)
                    expected = predicted_matching(n, agent, position)
                    assert valid[0] == expected, (n, agent, position, valid, expected)
                    standard = frozenset(frozenset((j,j+1)) for j in range(0,n,2))
                    changed += valid[0] != standard
        assert failures == n//2 - 1
        assert changed == n//2 - 1
        assert profiles == n*(n-2)
        print('n=%d profiles=%d no_stable=%d changed_unique=%d nonunique=%d perfect_matchings=%d' %
              (n, profiles, failures, changed, nonunique, len(all_matchings)))
    print('PASS: all complete one-swap profiles for n=4,6,8,10')

if __name__ == '__main__':
    run()
