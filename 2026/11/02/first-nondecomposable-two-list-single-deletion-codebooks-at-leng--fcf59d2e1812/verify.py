"""Exact integer/rational verification of binary two-list single-deletion code capacities.
Requires only Python 3 standard library and the accompanying certificate.json.
"""
import json
import pathlib
import sys
from fractions import Fraction


def deletion_sets(n):
    outputs = []
    for x in range(1 << n):
        bits = format(x, f'0{n}b')
        outputs.append(frozenset(int(bits[:j] + bits[j+1:] or '0', 2)
                                  for j in range(n)))
    return outputs


def verify_case(n, entry, list_size=2):
    k = entry['optimum']
    N = 1 << n
    M = 1 << (n - 1) if n > 1 else 1
    outputs = deletion_sets(n)
    parents = [[] for _ in range(M)]
    for x, yy in enumerate(outputs):
        for y in yy:
            parents[y].append(x)

    code = entry['witness']
    assert len(code) == k and len(set(code)) == k
    assert all(isinstance(x, int) and 0 <= x < N for x in code)
    assert all(sum(x in outputs_parents for x in code) <= list_size for outputs_parents in map(set, parents))

    num_nodes = [0]
    num_leaves = [0]

    def verify_tree(tree, fixed):
        num_nodes[0] += 1
        if 'branch' in tree:
            assert set(tree) == {'branch', 'zero', 'one'}
            x = tree['branch']
            assert isinstance(x, int) and 0 <= x < N and x not in fixed
            fixed[x] = 0
            verify_tree(tree['zero'], fixed)
            fixed[x] = 1
            verify_tree(tree['one'], fixed)
            del fixed[x]
            return
        num_leaves[0] += 1
        if 'infeasible_output' in tree:
            y = tree['infeasible_output']
            assert isinstance(y, int) and 0 <= y < M
            assert sum(fixed.get(x) == 1 for x in parents[y]) > list_size
            return
        assert set(tree) == {'dual', 'bound'}
        lam = {}
        for y, a, b in tree['dual']:
            assert isinstance(y, int) and 0 <= y < M and y not in lam
            assert isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0
            lam[y] = Fraction(a, b)
        chosen = {x for x, v in fixed.items() if v == 1}
        residual = [list_size - sum(x in chosen for x in parents[y]) for y in range(M)]
        assert min(residual) >= 0
        bound = Fraction(len(chosen))
        bound += sum(lam.get(y, 0) * residual[y] for y in range(M))
        for x in range(N):
            if x in fixed:
                continue
            reduced_price = Fraction(1) - sum(lam.get(y, 0) for y in outputs[x])
            bound += max(Fraction(0), reduced_price)
        assert bound < k + 1, (n, bound, k + 1)
        assert [bound.numerator, bound.denominator] == tree['bound']

    verify_tree(entry['upper_tree'], {})
    assert num_nodes[0] == entry['visited'][0]
    assert num_leaves[0] == entry['visited'][1] + entry['visited'][2]
    return num_nodes[0], num_leaves[0]


def main():
    source = pathlib.Path(__file__).with_name('certificate.json')
    obj = json.loads(source.read_text(encoding='utf-8'))
    assert obj['schema'] == 1
    assert set(map(int, obj['capacities'])) == set(range(1, 8))
    table = []
    for n in range(1, 8):
        entry = obj['capacities'][str(n)]
        nodes, leaves = verify_case(n, entry)
        table.append(entry['optimum'])
        print(f'n={n} optimum={entry["optimum"]} exact_upper_certificate_nodes={nodes} leaves={leaves}')
    assert table == [2, 3, 4, 7, 12, 19, 33]

    for n in range(1, 8):
        sizes = [0] * (n + 1)
        for x in range(1 << n):
            digits = format(x, f'0{n}b')
            syndrome = sum((i + 1) * int(b) for i, b in enumerate(digits)) % (n + 1)
            sizes[syndrome] += 1
        two_largest = sum(sorted(sizes, reverse=True)[:2])
        assert two_largest == table[n - 1] - (1 if n == 7 else 0)
        print(f'n={n} union_two_largest_VT_classes={two_largest}')
    unique = obj['unique_deletion_length_seven']
    assert unique['length'] == 7 and unique['list_size'] == 1
    nodes, leaves = verify_case(7, unique, list_size=1)
    assert unique['optimum'] == 16
    assert 2 * unique['optimum'] < obj['capacities']['7']['optimum']
    print(f'n=7 unique-deletion optimum=16 exact_upper_certificate_nodes={nodes} leaves={leaves}')
    print('PASS: all exact rational dual trees, witnesses, VT comparisons and nondecomposability bound')


if __name__ == '__main__':
    main()
