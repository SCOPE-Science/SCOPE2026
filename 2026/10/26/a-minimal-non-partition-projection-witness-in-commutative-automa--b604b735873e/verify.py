from itertools import product


def compose(f, g):
    """Transformation obtained by applying f and then g."""
    return tuple(g[f[q]] for q in range(len(f)))


def commute(a, b):
    return compose(a, b) == compose(b, a)


def hidden_closure(states, hidden_maps):
    out = set(states)
    todo = list(states)
    while todo:
        q = todo.pop()
        for h in hidden_maps:
            r = h[q]
            if r not in out:
                out.add(r)
                todo.append(r)
    return frozenset(out)


def reachable_closure_states(a, hidden_maps, start, n):
    first = hidden_closure({start}, hidden_maps)
    seen = {first}
    todo = [first]
    while todo:
        S = todo.pop()
        image = {a[q] for q in S}
        T = hidden_closure(image, hidden_maps)
        if T not in seen:
            seen.add(T)
            todo.append(T)
    return seen


def is_partition(subsets, n):
    if not subsets or set().union(*subsets) != set(range(n)):
        return False
    seq = list(subsets)
    return all(not (seq[i] & seq[j]) for i in range(len(seq)) for j in range(i))


def projected_accepting_states(hidden_maps, final, n):
    return {q for q in range(n) if hidden_closure({q}, hidden_maps) & final}


def reachable_states(a, start):
    seen = {start}
    todo = [start]
    while todo:
        q = todo.pop()
        r = a[q]
        if r not in seen:
            seen.add(r)
            todo.append(r)
    return seen


def minimal_unary_state_count(a, start, accepting):
    reach = reachable_states(a, start)
    blocks = [set(q for q in reach if q in accepting),
              set(q for q in reach if q not in accepting)]
    blocks = [B for B in blocks if B]
    while True:
        index = {q: i for i, B in enumerate(blocks) for q in B}
        groups = {}
        for q in reach:
            signature = (q in accepting, index[a[q]])
            groups.setdefault(signature, set()).add(q)
        new_blocks = list(groups.values())
        old = {frozenset(B) for B in blocks}
        new = {frozenset(B) for B in new_blocks}
        blocks = new_blocks
        if old == new:
            return len(blocks)


def unary_language_infinite(a, start, accepting):
    first_seen = {}
    path = []
    q = start
    while q not in first_seen:
        first_seen[q] = len(path)
        path.append(q)
        q = a[q]
    cycle = path[first_seen[q]:]
    return any(s in accepting for s in cycle)


def test_two_state_binary_lower_bound():
    maps = list(product(range(2), repeat=2))
    checked = 0
    commutative = 0
    counterexamples = []
    for a in maps:
        for b in maps:
            for start in range(2):
                for mask in range(4):
                    checked += 1
                    final = {q for q in range(2) if (mask >> q) & 1}
                    if not commute(a, b):
                        continue
                    commutative += 1
                    accepting = projected_accepting_states([b], final, 2)
                    if minimal_unary_state_count(a, start, accepting) != 2:
                        continue
                    if not unary_language_infinite(a, start, accepting):
                        continue
                    subsets = reachable_closure_states(a, [b], start, 2)
                    if not is_partition(subsets, 2):
                        counterexamples.append((a, b, start, final, accepting, subsets))
    assert not counterexamples, counterexamples
    return checked, commutative, len(counterexamples)


def test_three_state_witness():
    # State order is 0, 1, 2; each tuple gives the image of that state.
    a = (1, 0, 0)
    b = (0, 1, 1)
    start = 2
    final = {0, 2}
    n = 3

    assert commute(a, b)
    accepting = projected_accepting_states([b], final, n)
    assert accepting == {0, 2}
    assert minimal_unary_state_count(a, start, accepting) == 3
    assert unary_language_infinite(a, start, accepting)

    sequence = []
    q = start
    for _ in range(9):
        sequence.append(q in accepting)
        q = a[q]
    assert sequence == [True, True, False, True, False, True, False, True, False], sequence

    subsets = reachable_closure_states(a, [b], start, n)
    expected = {frozenset({1, 2}), frozenset({0}), frozenset({1})}
    assert subsets == expected, subsets
    assert not is_partition(subsets, n)

    # The original language is also minimal: all states are reachable;
    # 0 and 1 differ by epsilon, while 0 and 2 differ after b.
    assert len(reachable_states(a, start)) == 3
    assert (0 in final) != (1 in final)
    assert (compose((0, 1, 2), b)[0] in final)  # sanity check for b fixing 0
    assert (b[2] in final) is False


if __name__ == "__main__":
    checked, commutative, counterexamples = test_two_state_binary_lower_bound()
    test_three_state_witness()
    print(f"VERIFY_OK: checked {checked} labeled two-state binary DFAs; "
          f"{commutative} were commutative; {counterexamples} counterexamples; "
          "the three-state witness passed.")
