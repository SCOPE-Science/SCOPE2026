"""Direct six-point witness and coarsest-equitable-partition certificate."""
from collections import Counter

f = (1, 0, 3, 2, 5, 4)
g_commuting = (2, 3, 4, 5, 0, 1)
g_noncommuting = (2, 4, 1, 5, 3, 0)


def cycles(p):
    seen = set()
    answer = []
    for start in range(len(p)):
        if start in seen:
            continue
        current, cycle = start, []
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = p[current]
        assert current == start
        answer.append(tuple(cycle))
    return tuple(answer)


def signatures(f, g):
    n = len(f)
    point_signatures = []
    for a in range(n):
        histogram = Counter()
        for b in range(n):
            histogram[(a == b,
                       f[a] == b, f[b] == a,
                       g[a] == b, g[b] == a)] += 1
        point_signatures.append(tuple(sorted(histogram.items())))
    return point_signatures


def main():
    assert sorted(f) == list(range(6))
    for g in (g_commuting, g_noncommuting):
        assert sorted(g) == list(range(6))
    assert all(f[g_commuting[x]] == g_commuting[f[x]] for x in range(6))
    assert f[g_noncommuting[0]] == 3
    assert g_noncommuting[f[0]] == 4
    assert any(f[g_noncommuting[x]] != g_noncommuting[f[x]] for x in range(6))
    a = signatures(f, g_commuting)
    b = signatures(f, g_noncommuting)
    assert len(set(a)) == len(set(b)) == 1
    assert a[0] == b[0]
    assert dict(a[0]) == {
        (True,False,False,False,False):1,
        (False,True,True,False,False):1,
        (False,False,False,True,False):1,
        (False,False,False,False,True):1,
        (False,False,False,False,False):2,
    }
    print('f_cycles=',cycles(f))
    print('commuting_g_cycles=',cycles(g_commuting))
    print('noncommuting_g_cycles=',cycles(g_noncommuting))
    print('identical_per_vertex_pair_atomic_profiles=',a[0])
    print('one_equitable_color_class_of_size_six_in_both_models=True')
    print('composition_disagreement_at_x0=',f[g_noncommuting[0]],g_noncommuting[f[0]])
    print('WITNESS_PASS')


if __name__ == '__main__':
    main()
