from collections import deque
from math import ceil, log2


def jm_core(k, N):
    """Visible chain from the finite-language witness of Jiraskova--Masopust."""
    t = ceil(log2(k))
    m = N // (t + 1)
    S = {
        i: {a for a in range(k) if a % (2**i) >= 2 ** (i - 1)}
        for i in range(1, t + 1)
    }
    trans = {}
    for q in range(N - 1):
        position_from_end = N - 1 - q
        allowed = set(range(k))
        for i in range(1, t + 1):
            if position_from_end == i * m:
                allowed &= S[i]
        for a in allowed:
            trans[(q, a)] = q + 1
    return trans, N - 1, m


def prefix_tree(L, h):
    """An h-ary prefix tree with L leaves and the minimum number of nonroot internal nodes."""
    if L <= h:
        return [], [(a,) for a in range(L)]
    leaves = [(a,) for a in range(h)]
    internal = []
    while len(leaves) < L:
        p = leaves.pop(0)
        internal.append(p)
        d = min(h, L - len(leaves))
        leaves.extend(p + (a,) for a in range(d))
    return internal, leaves


def compressed_input_dfa(k, N, h):
    visible, final, m = jm_core(k, N)
    L = N - m - 1
    internal_paths, leaf_paths = prefix_tree(L, h)
    internal_state = {p: N + i for i, p in enumerate(internal_paths)}
    leaf_state = {p: i + 1 for i, p in enumerate(leaf_paths)}

    def state_of(path):
        if not path:
            return 0
        if path in internal_state:
            return internal_state[path]
        return leaf_state[path]

    trans = dict(visible)
    for path in list(internal_paths) + list(leaf_paths):
        trans[(state_of(path[:-1]), k + path[-1])] = state_of(path)

    return N + len(internal_paths), trans, 0, {final}, m


def direct_projected_dfa(k, N):
    visible, final, m = jm_core(k, N)
    start = frozenset(range(N - m))
    queue = deque([start])
    seen = {start: 0}
    finals = set()
    trans = {}
    while queue:
        S = queue.popleft()
        i = seen[S]
        if final in S:
            finals.add(i)
        for a in range(k):
            T = frozenset(visible[(q, a)] for q in S if (q, a) in visible)
            if not T:
                continue
            if T not in seen:
                seen[T] = len(seen)
                queue.append(T)
            trans[(i, a)] = seen[T]
    subsets = {i: S for S, i in seen.items()}
    return len(seen), trans, finals, m, subsets


def projected_from_compressed(k, N, h):
    n, trans, start, finals, m = compressed_input_dfa(k, N, h)
    hidden = range(k, k + h)

    def eps_closure(S):
        out = set(S)
        queue = deque(S)
        while queue:
            q = queue.popleft()
            for a in hidden:
                if (q, a) in trans:
                    r = trans[(q, a)]
                    if r not in out:
                        out.add(r)
                        queue.append(r)
        return frozenset(out)

    start_set = eps_closure({start})
    queue = deque([start_set])
    seen = {start_set: 0}
    dfa_finals = set()
    dfa_trans = {}
    while queue:
        S = queue.popleft()
        i = seen[S]
        if S & finals:
            dfa_finals.add(i)
        for a in range(k):
            moved = {trans[(q, a)] for q in S if (q, a) in trans}
            if not moved:
                continue
            T = eps_closure(moved)
            if T not in seen:
                seen[T] = len(seen)
                queue.append(T)
            dfa_trans[(i, a)] = seen[T]
    subsets = {i: S for S, i in seen.items()}
    return len(seen), dfa_trans, dfa_finals, m, subsets


def minimal_incomplete_size(n, trans, start, finals, alphabet):
    dead = n
    states = set(range(n + 1))
    total = {}
    for q in states:
        for a in alphabet:
            total[(q, a)] = dead if q == dead else trans.get((q, a), dead)

    reachable = {start}
    queue = deque([start])
    while queue:
        q = queue.popleft()
        for a in alphabet:
            r = total[(q, a)]
            if r not in reachable:
                reachable.add(r)
                queue.append(r)

    blocks = [set(finals) & reachable, reachable - set(finals)]
    blocks = [B for B in blocks if B]
    while True:
        block_of = {q: i for i, B in enumerate(blocks) for q in B}
        refined = []
        changed = False
        for B in blocks:
            buckets = {}
            for q in B:
                signature = tuple(block_of[total[(q, a)]] for a in alphabet)
                buckets.setdefault(signature, set()).add(q)
            refined.extend(buckets.values())
            changed |= len(buckets) > 1
        blocks = refined
        if not changed:
            break

    return len(blocks) - (1 if dead in reachable else 0)


def run_checks():
    cases = 0
    for k in (3, 4, 5):
        for h in (2, 3, 4):
            for N in range(6, 13):
                n, trans, start, finals, m = compressed_input_dfa(k, N, h)
                min_n = minimal_incomplete_size(n, trans, start, finals, range(k + h))
                assert min_n == n, (k, h, N, n, min_n)

                direct_count, direct_trans, direct_finals, _, direct_subsets = direct_projected_dfa(k, N)
                tree_count, tree_trans, tree_finals, _, tree_subsets = projected_from_compressed(k, N, h)
                assert tree_count == direct_count, (k, h, N, tree_count, direct_count)

                # The compressed projected automaton has routing states only in its
                # initial epsilon-closure. Removing those inert states must identify
                # every reachable subset and visible transition with the original
                # direct-fanout projected automaton.
                direct_id = {S: i for i, S in direct_subsets.items()}
                stripped_to_tree = {}
                for i, S in tree_subsets.items():
                    core = frozenset(q for q in S if q < N)
                    assert core in direct_id, (k, h, N, i, core)
                    assert core not in stripped_to_tree, (k, h, N, core)
                    stripped_to_tree[core] = i
                assert set(stripped_to_tree) == set(direct_id), (k, h, N)
                for core, di in direct_id.items():
                    ti = stripped_to_tree[core]
                    assert (di in direct_finals) == (ti in tree_finals), (k, h, N, core)
                    for a in range(k):
                        dj = direct_trans.get((di, a))
                        tj = tree_trans.get((ti, a))
                        assert (dj is None) == (tj is None), (k, h, N, core, a)
                        if dj is not None:
                            target_core = direct_subsets[dj]
                            tree_target_core = frozenset(q for q in tree_subsets[tj] if q < N)
                            assert tree_target_core == target_core, (k, h, N, core, a)

                lower = (k ** (m + 1) - 1) // (k - 1) - 1
                assert tree_count >= lower, (k, h, N, tree_count, lower)
                cases += 1

    print(f"verified_cases={cases}")
    print("k_values=3,4,5")
    print("hidden_alphabet_sizes=2,3,4")
    print("core_state_counts=6..12")
    print("all_input_dfas_minimal=true")
    print("compressed_projection_equals_direct_fanout_projection=true")
    print("all_projected_state_counts_meet_JM_geometric_lower_bound=true")


if __name__ == "__main__":
    run_checks()
