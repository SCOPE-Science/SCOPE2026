#!/usr/bin/env python3
"""Exhaustive finite transition certificate for synchronous random-tie majority.

Uses only the Python standard library. The majority supports are checked by
both a constructive tie expansion and a direct all-candidate-state test.
Closed communicating classes are checked by independent Tarjan and bitset
transitive-closure computations. No random sampling is involved.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations


def connected(n, edges):
    seen = {0}
    while True:
        grown = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if grown == seen:
            break
        seen = grown
    return len(seen) == n


def transition_support(n, edges):
    neighbors = [tuple(v if u == i else u for u, v in edges if u == i or v == i)
                 for i in range(n)]
    result = []
    for state in range(1 << n):
        fixed, tied = 0, []
        for i, adjacent in enumerate(neighbors):
            blue = sum((state >> j) & 1 for j in adjacent)
            if 2 * blue > len(adjacent):
                fixed |= 1 << i
            elif 2 * blue == len(adjacent):
                tied.append(i)
        possible = [fixed]
        for i in tied:
            possible = possible + [out | (1 << i) for out in possible]
        result.append(frozenset(possible))
    return result


def transition_direct(n, edges):
    neighbors = [tuple(v if u == i else u for u, v in edges if u == i or v == i)
                 for i in range(n)]
    result = []
    for state in range(1 << n):
        correct = set()
        for target in range(1 << n):
            permitted = True
            for i, adjacent in enumerate(neighbors):
                blue = sum((state >> j) & 1 for j in adjacent)
                if 2 * blue != len(adjacent) and ((target >> i) & 1) != int(2 * blue > len(adjacent)):
                    permitted = False
                    break
            if permitted:
                correct.add(target)
        result.append(frozenset(correct))
    return result


def terminal_tarjan(support):
    nstates = len(support)
    ind = [-1] * nstates
    low = [0] * nstates
    on = [False] * nstates
    stack = []
    components = []
    counter = 0

    def visit(v):
        nonlocal counter
        ind[v] = low[v] = counter
        counter += 1
        on[v] = True
        stack.append(v)
        for w in support[v]:
            if ind[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on[w]:
                low[v] = min(low[v], ind[w])
        if low[v] == ind[v]:
            component = set()
            while True:
                w = stack.pop()
                on[w] = False
                component.add(w)
                if w == v:
                    break
            components.append(frozenset(component))

    for v in range(nstates):
        if ind[v] < 0:
            visit(v)
    return frozenset(comp for comp in components
                     if all(support[s] <= comp for s in comp))


def terminal_closure(support):
    n = len(support)
    reach = [sum(1 << x for x in targets) | (1 << i)
             for i, targets in enumerate(support)]
    for k in range(n):
        rk = reach[k]
        for i in range(n):
            if (reach[i] >> k) & 1:
                reach[i] |= rk
    unseen = set(range(n))
    terminal = set()
    while unseen:
        x = min(unseen)
        comp = frozenset(j for j in range(n)
                         if (reach[x] >> j) & 1 and (reach[j] >> x) & 1)
        unseen.difference_update(comp)
        if all(support[s] <= comp for s in comp):
            terminal.add(comp)
    return frozenset(terminal)


def canon_mask(n, edges, perms, edge_map):
    best = 1 << (n*(n-1)//2)
    for p in perms:
        bits = 0
        for u, v in edges:
            bits |= 1 << edge_map[tuple(sorted((p[u], p[v])))]
        best = min(best, bits)
    return best


def check():
    expected_connected = [1, 4, 38, 728]
    expected_undirected_classes = [1, 2, 6, 21]
    nbad = [0, 0, 0, 135]
    for n in range(2, 6):
        pairs = tuple(combinations(range(n), 2))
        positions = {edge: i for i, edge in enumerate(pairs)}
        perms = tuple(permutations(range(n)))
        connected_count = bad_count = 0
        class_labels = set()
        bad_classes = set()
        bad_label_hist = Counter()
        terminal_hist = Counter()
        bad_representatives = {}
        for gmask in range(1 << len(pairs)):
            edges = tuple(p for k, p in enumerate(pairs) if (gmask >> k) & 1)
            if not connected(n, edges):
                continue
            connected_count += 1
            support = transition_support(n, edges)
            assert support == transition_direct(n, edges), (n, edges, 'transition mismatch')
            tarjan = terminal_tarjan(support)
            closure = terminal_closure(support)
            assert tarjan == closure, (n, edges, 'SCC mismatch')
            largest = max(len(comp) for comp in tarjan)
            terminal_hist[largest] += 1
            # A stochastic terminal class contains a state with at least two
            # genuinely different successors, hence ongoing random choices.
            stochastic = any(any(len(support[s]) > 1 for s in comp) for comp in tarjan)
            if n <= 4:
                assert not stochastic and largest <= 2, (n, edges)
            if n == 5:
                assert (largest > 2) == stochastic, (n, edges)
                assert largest in (1, 2, 4), (n, edges, largest)
            key = canon_mask(n, edges, perms, positions)
            class_labels.add(key)
            if stochastic:
                bad_count += 1
                bad_classes.add(key)
                bad_label_hist[key] += 1
                bad_representatives.setdefault(key, (edges, tarjan, support))
        assert connected_count == expected_connected[n-2], (n, connected_count)
        assert len(class_labels) == expected_undirected_classes[n-2], (n, len(class_labels))
        assert bad_count == nbad[n-2], (n, bad_count)
        if n == 5:
            assert len(bad_classes) == 3
            assert sorted(terminal_hist) == [1, 2, 4]
            expected_patterns = [
                ((0,1),(0,2),(0,4),(1,2),(2,3)),  # bull graph
                ((0,1),(0,3),(0,4),(1,2),(2,3),(3,4)),  # house graph
                ((0,1),(0,3),(0,4),(1,2),(1,4),(2,3),(2,4),(3,4)),  # wheel W5
            ]
            expected_keys = {canon_mask(5, edges, perms, positions) for edges in expected_patterns}
            assert expected_keys == bad_classes
            assert sorted(bad_label_hist.values()) == [15,60,60]
            for name, edges in zip(('bull','house','wheel'), expected_patterns):
                supp = transition_support(5, edges)
                terms = terminal_tarjan(supp)
                random_classes = [c for c in terms if any(len(supp[s]) > 1 for s in c)]
                assert len(random_classes) == 1
                c = random_classes[0]
                assert len(c) == 4 and all(len(supp[s]) == 2 for s in c)
                assert all(supp[s] <= c for s in c)
                print(name, 'edges=', edges, 'recurrent_states=', sorted(c))
        print('n=',n,'connected_labeled=',connected_count,
              'unlabeled=',len(class_labels),'random_recurrent_labeled=',bad_count,
              'max_closed_class_hist=',sorted(terminal_hist.items()))
    # Connected arbitrary-order bull expansions: add any nonnegative numbers
    # of private leaves at the two triangle vertices that already own leaves.
    for n in range(5, 17):
        for a in range(n - 4):
            b = n - 5 - a
            edges = [(0,1),(0,2),(0,4),(1,2),(2,3)]
            edges += [(0,i) for i in range(5,5+a)]
            edges += [(2,i) for i in range(5+a,n)]
            assert len(edges) == n and connected(n, edges)
            phase0 = 1 << 0  # hubs 0=blue, 2=white
            phase0 |= 1 << 3  # opposing right-hub leaf
            phase0 |= sum(1 << i for i in range(5+a,n))
            phase1 = ((1 << n) - 1) ^ phase0
            middle = 1 << 1
            candidate = frozenset([phase0 & ~middle,phase0 | middle,
                                   phase1 & ~middle,phase1 | middle])
            # Directly check four states without building a 2^n matrix.
            def local_successors(s):
                out = 0
                tie_sites = []
                for v in range(n):
                    ngh = [j if i == v else i for i,j in edges if i==v or j==v]
                    count = sum((s >> j) & 1 for j in ngh)
                    if 2*count > len(ngh): out |= 1 << v
                    elif 2*count == len(ngh): tie_sites.append(v)
                result = {out}
                for i in tie_sites: result |= {r | (1<<i) for r in tuple(result)}
                return result,tie_sites
            for state in candidate:
                successors,ties = local_successors(state)
                assert ties == [1]
                assert successors <= candidate and len(successors) == 2
                assert all(((state >> 0)&1) != ((target >> 0)&1) for target in successors)
            # The two phases both feed equally to the opposite phase;
            # hence all four states communicate and the set is closed.
        print('bull_family_verified_order=',n)
    print('CHECK_OK')


if __name__ == '__main__':
    check()
