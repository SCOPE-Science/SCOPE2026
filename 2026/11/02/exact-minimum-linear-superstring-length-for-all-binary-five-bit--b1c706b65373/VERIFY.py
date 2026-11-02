#!/usr/bin/env python3
"""Exact finite proof for the shortest superstring of all binary five-bit squares.

Requires Python 3.9+ standard library only. Integer arithmetic throughout.
"""
from itertools import permutations

N = 5
TARGET_COUNT = 1 << N
WINDOW = 2 * N
WITNESS = (
    "0000000000110001100010000100001010010100101111011110110101101011100111001111111111"
)


def roots_and_costs():
    roots = [format(i, "05b") for i in range(TARGET_COUNT)]
    squares = [r + r for r in roots]
    cost = [[100] * TARGET_COUNT for _ in roots]
    for i, a in enumerate(squares):
        for j, b in enumerate(squares):
            if i != j:
                overlap = max((k for k in range(1, WINDOW)
                               if a[-k:] == b[:k]), default=0)
                cost[i][j] = WINDOW - overlap
    return roots, squares, cost


def necklace_groups(roots):
    grouped = {}
    for i, root in enumerate(roots):
        key = min(root[j:] + root[:j] for j in range(N))
        grouped.setdefault(key, []).append(i)
    return [grouped[k] for k in sorted(grouped)]


def q7_optimum(groups, costs):
    """Exact weighted path DP with one contiguous block for each necklace."""
    # Enumerate every possible internal Hamilton path per necklace.
    # For fixed start/end, keep only the least internal cost.
    opts = []
    for group in groups:
        best = {}
        for path in permutations(group):
            internal = sum(costs[a][b] for a, b in zip(path, path[1:]))
            endpoints = path[0], path[-1]
            if endpoints not in best or internal < best[endpoints][0]:
                best[endpoints] = internal, path
        opts.append([(start, end, data[0], data[1])
                     for (start, end), data in sorted(best.items())])

    group_count = len(groups)
    dp = [dict() for _ in range(1 << group_count)]
    for group in range(group_count):
        for variant, (start, end, internal, path) in enumerate(opts[group]):
            dp[1 << group][(group, variant)] = WINDOW + internal
    for mask in range(1, 1 << group_count):
        for (previous, old_variant), value in dp[mask].items():
            endpoint = opts[previous][old_variant][1]
            for group in range(group_count):
                if mask & (1 << group):
                    continue
                next_mask = mask | (1 << group)
                for variant, (start, end, internal, path) in enumerate(opts[group]):
                    candidate = value + costs[endpoint][start] + internal
                    key = (group, variant)
                    if candidate < dp[next_mask].get(key, 10**9):
                        dp[next_mask][key] = candidate
    return min(dp[-1].values()), opts


def q8_zero_excess_possible(groups, costs):
    """Test every 9-block equality case at eight necklace crossings.

    All intra-necklace transitions would have cost one and all cross-necklace
    transitions cost six. One primitive necklace must be split into two
    nonempty directed arcs; all other necklaces are contiguous blocks.
    """
    group_cycles = {}
    for gi, group in enumerate(groups):
        if len(group) == 1:
            continue
        successor = {}
        for i in group:
            matches = [j for j in group if costs[i][j] == 1]
            if len(matches) != 1:
                raise AssertionError("intra-necklace unit steps are not unique")
            successor[i] = matches[0]
        for start in group:
            path = [start]
            for _ in range(len(group) - 1):
                path.append(successor[path[-1]])
            if set(path) != set(group) or successor[path[-1]] != start:
                raise AssertionError("intra-necklace edges are not a directed cycle")
            group_cycles[gi, start] = tuple(path)

    def feasible(split, first, second):
        blocks, necklace_of = [], []
        for gi, group in enumerate(groups):
            if gi == split:
                blocks.append([(first[0], first[-1])])
                necklace_of.append(gi)
                blocks.append([(second[0], second[-1])])
                necklace_of.append(gi)
            else:
                if len(group) == 1:
                    blocks.append([(group[0], group[0])])
                else:
                    blocks.append([(seq[0], seq[-1])
                                   for (jj, st), seq in group_cycles.items() if jj == gi])
                necklace_of.append(gi)
        size = len(blocks)
        if size != 9:
            raise AssertionError("expected nine blocks")
        reachable = [set() for _ in range(1 << size)]
        for i in range(size):
            for a in range(len(blocks[i])):
                reachable[1 << i].add((i, a))
        for mask in range(1, 1 << size):
            for i, a in reachable[mask]:
                last = blocks[i][a][1]
                for j in range(size):
                    if mask & (1 << j) or necklace_of[i] == necklace_of[j]:
                        continue
                    for b, (first_word, last_word) in enumerate(blocks[j]):
                        if costs[last][first_word] == 6:
                            reachable[mask | (1 << j)].add((j, b))
        return bool(reachable[-1])

    cases = 0
    matches = 0
    for gi, group in enumerate(groups):
        if len(group) == 1:
            continue
        for start in group:
            cycle = group_cycles[gi, start]
            for cut in range(1, len(cycle)):
                cases += 1
                if feasible(gi, cycle[:cut], cycle[cut:]):
                    matches += 1
    return cases, matches


def main():
    roots, squares, costs = roots_and_costs()
    groups = necklace_groups(roots)
    if len(groups) != 8 or sorted(map(len, groups)) != [1, 1, 5, 5, 5, 5, 5, 5]:
        raise AssertionError("incorrect necklace partition")
    orbit_of = {i: gi for gi, group in enumerate(groups) for i in group}
    for i in range(TARGET_COUNT):
        for j in range(TARGET_COUNT):
            if i != j:
                if costs[i][j] < 1:
                    raise AssertionError("distinct square overlap cost zero")
                if orbit_of[i] != orbit_of[j] and costs[i][j] < 6:
                    raise AssertionError("cross-orbit overlap exceeds four")
    q7, variants = q7_optimum(groups, costs)
    if q7 != 82:
        raise AssertionError(f"unexpected seven-crossing optimum: {q7}")
    cases, matches = q8_zero_excess_possible(groups, costs)
    if (cases, matches) != (120, 0):
        raise AssertionError(f"eight-crossing equality cases: {cases}, {matches}")
    if len(WITNESS) != 82 or set(WITNESS) - {"0", "1"}:
        raise AssertionError("wrong witness length or alphabet")
    factors = {WITNESS[p:p + WINDOW] for p in range(len(WITNESS) - WINDOW + 1)}
    if not set(squares).issubset(factors):
        raise AssertionError("missing a required square")
    # At q>=9 the baseline 10+(31-q)*1+6*q is >=86;
    # at q=8 length<=81 requires one of the excluded equality cases;
    # at q=7 the exact block DP yields >=82. Every path has q>=7.
    print("Q7_OPT=82")
    print(f"Q8_EQUALITY_CASES={cases} Q8_FEASIBLE={matches}")
    print("WITNESS_LENGTH=82 DISTINCT_SQUARES=32")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
