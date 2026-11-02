"""Reproduce the one-excess global secure-set census for sunlet graphs.

Uses only Python's standard library.  Graph-security checks are made directly
from closed neighborhoods, independently of the symbolic classification.
"""
from itertools import product


def graph_neighborhoods(n):
    result = []
    for i in range(n):
        result.append(sum(1 << j for j in {i, (i - 1) % n, (i + 1) % n, n + i}))
    for i in range(n):
        result.append((1 << i) | (1 << (n + i)))
    return result


def chosen_mask(word):
    n = len(word)
    mask = 0
    for i, state in enumerate(word):
        if state in ('A', 'B'):
            mask |= 1 << i
        if state in ('A', 'C'):
            mask |= 1 << (n + i)
    return mask


def secure_direct(word):
    n = len(word)
    Ns = graph_neighborhoods(n)
    selected = chosen_mask(word)
    V = (1 << (2 * n)) - 1
    selected_vertices = [i for i in range(2 * n) if selected >> i & 1]
    # Dominating condition.
    covered = 0
    for v in selected_vertices:
        covered |= Ns[v]
    if covered != V:
        return False
    # Every nonempty attack, recomputed directly in the original 2n-vertex graph.
    # Subset DP builds the neighborhood union without any classification assumptions.
    Nunion = [0] * (1 << len(selected_vertices))
    for sub in range(1, len(Nunion)):
        bit = sub & -sub
        idx = bit.bit_length() - 1
        Nunion[sub] = Nunion[sub ^ bit] | Ns[selected_vertices[idx]]
        neigh = Nunion[sub]
        if (neigh & selected).bit_count() < (neigh & (V ^ selected)).bit_count():
            return False
    return True


def predicted(word):
    n = len(word)
    if all(x == 'B' for x in word) or all(x == 'C' for x in word):
        return True
    if word.count('A') != 1:
        return False
    root = word.index('A')
    tail = ''.join(word[(root + j) % n] for j in range(1, n))
    # Word can be empty-B first run, or empty-C first run.
    if all(x == 'B' for x in tail) or all(x == 'C' for x in tail):
        return True
    changes = [j for j in range(1, len(tail)) if tail[j] != tail[j - 1]]
    if len(changes) == 1:
        return True
    if len(changes) == 2:
        return tail[0] == 'B' and tail[-1] == 'B' and changes[1] - changes[0] == 1
    return False


def bitset_reduced_security(word):
    n = len(word)
    assert word.count('A') <= 1
    root = word.index('A') if 'A' in word else -1
    core = [i for i in range(n) if word[i] in 'AB']
    for m in range(1 << len(core)):
        U = {core[j] for j in range(len(core)) if m >> j & 1}
        closed = U.copy()
        for i in U:
            closed.add((i - 1) % n)
            closed.add((i + 1) % n)
        charge = (2 if root in U else 0) + sum(1 if word[i] in 'AB' else -1 for i in (closed - U))
        if charge < 0:
            return False
    return True


def check():
    count_original = 0
    for n in range(3, 9):
        found_n = found_n1 = 0
        for word in product('ABC', repeat=n):
            # For first two layers, domination forces at least one selected per pair.
            excess = word.count('A')
            if excess > 1:
                continue
            actual = secure_direct(word)
            predicted_answer = predicted(word)
            assert actual == predicted_answer, (n, ''.join(word), actual, predicted_answer)
            assert bitset_reduced_security(word) == actual, ('CORE-CHARGE', n, ''.join(word))
            count_original += 1
            if actual:
                if excess == 0:
                    found_n += 1
                else:
                    found_n1 += 1
        assert found_n == 2 and found_n1 == n * (3 * n - 5), (n, found_n, found_n1)
        print('ORIGINAL_GRAPH_ALL_ATTACKS_OK', n, found_n, found_n1, flush=True)
    print('DIRECT_CONFIGURATIONS_TESTED', count_original, flush=True)
    # Independent reduced boundary-charge test for larger widths.
    for n in range(9, 12):
        root = 0
        good = 0
        for tail in product('BC', repeat=n - 1):
            word = ('A',) + tail
            truth = bitset_reduced_security(word)
            expect = predicted(word)
            assert truth == expect, (n, ''.join(word), truth, expect)
            good += truth
        assert good == 3 * n - 5, (n, good)
        print('CORE_CHARGE_BOUNDARY_OK', n, good, flush=True)
    print('VERIFY_OK', flush=True)


if __name__ == '__main__':
    check()
