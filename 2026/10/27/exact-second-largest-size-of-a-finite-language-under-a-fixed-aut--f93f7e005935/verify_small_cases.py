"""Finite sanity check for the extremal finite-language DFA theorem.

Enumerates all topologically ordered complete acyclic transition tables with
n non-dead states over alphabets of size q, all accepting-state sets, and
filters to accessible, coaccessible, minimal automata.  It compares the two
largest accepted-language cardinalities for each feasible final-state count.
This checks only the stated finite parameter ranges; the proof in RESULT.md
is analytic and does not rely on exhaustive enumeration.
"""
from itertools import product


def predicted_gap(q, n, f):
    if n == 2 and f == 1:
        return 1
    if f == 1:
        return (q - 1) * q ** (n - 3)
    if f < n:
        return (q - 1) * q ** (n - f - 1)
    return q ** (n - 2)


def enumerate_case(q, n):
    # State n is the dead sink. Topological order is 0,...,n-1,dead.
    choices = [list(range(i + 1, n + 1)) for i in range(n)]
    transition_rows = [list(product(choices[i], repeat=q)) for i in range(n)]
    all_transitions = product(*transition_rows)
    observed = {f: set() for f in range(1, n + 1)}
    for trans in all_transitions:
        for mask in range(1 << n):
            f = mask.bit_count()
            if f == 0:
                continue
            # Every non-dead state must be reachable from the initial state.
            reachable = {0}
            stack = [0]
            while stack:
                i = stack.pop()
                for j in trans[i]:
                    if j < n and j not in reachable:
                        reachable.add(j)
                        stack.append(j)
            if len(reachable) != n:
                continue
            # Every non-dead state must have a path to an accepting state.
            coreachable = {i for i in range(n) if (mask >> i) & 1}
            changed = True
            while changed:
                changed = False
                for i in range(n):
                    if i not in coreachable and any(j in coreachable for j in trans[i]):
                        coreachable.add(i)
                        changed = True
            if len(coreachable) != n:
                continue
            # Distinct right-language signatures characterize minimality here.
            signatures = [None] * n
            dead_signature = ("dead",)
            for i in range(n - 1, -1, -1):
                signatures[i] = (
                    (mask >> i) & 1,
                    tuple(signatures[j] if j < n else dead_signature for j in trans[i]),
                )
            if len(set(signatures)) != n:
                continue
            # Number of accepted suffixes from each state, by backward DP.
            counts = [0] * n
            for i in range(n - 1, -1, -1):
                counts[i] = ((mask >> i) & 1) + sum(
                    counts[j] if j < n else 0 for j in trans[i]
                )
            observed[f].add(counts[0])
    for f, sizes in observed.items():
        ordered = sorted(sizes, reverse=True)
        maximum = sum(q ** j for j in range(n - f, n))
        gap = predicted_gap(q, n, f)
        if len(ordered) < 2 or ordered[0] != maximum or ordered[1] != maximum - gap:
            raise AssertionError(
                f"Mismatch q={q}, n={n}, f={f}: top={ordered[:3]}, "
                f"expected maximum={maximum}, second={maximum-gap}"
            )
    return len(observed)


def main():
    cases = []
    for q, max_n in ((2, 5), (3, 4)):
        for n in range(2, max_n + 1):
            count = enumerate_case(q, n)
            cases.append((q, n, count))
    print(f"PASS: {len(cases)} (q,n) cases; final-state strata all match.")
    print("Ranges: q=2, n=2..5; q=3, n=2..4. Finite check only.")


if __name__ == "__main__":
    main()
