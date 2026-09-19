"""Monte Carlo check for the entropy-scale distinct-substring deficit theorem.

The distinct-substring count of each sampled word is exact: it is computed by a
suffix automaton. Only the Monte Carlo averaging is approximate. The fixed seed
makes the reported run reproducible with the Python standard library.
"""

import math
import random
import statistics


def distinct_substrings_suffix_automaton(seq):
    transitions = [{}]
    link = [-1]
    length = [0]
    last = 0

    for symbol in seq:
        cur = len(transitions)
        transitions.append({})
        length.append(length[last] + 1)
        link.append(0)

        p = last
        while p >= 0 and symbol not in transitions[p]:
            transitions[p][symbol] = cur
            p = link[p]

        if p == -1:
            link[cur] = 0
        else:
            q = transitions[p][symbol]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = len(transitions)
                transitions.append(transitions[q].copy())
                length.append(length[p] + 1)
                link.append(link[q])
                while p >= 0 and transitions[p].get(symbol) == q:
                    transitions[p][symbol] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur

    return sum(
        length[state] - length[link[state]]
        for state in range(1, len(transitions))
    )


def run_source(probabilities, sizes, repetitions, seed):
    rng = random.Random(seed)
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    target = 1.0 / entropy
    print(f"p={probabilities}")
    print(f"H={entropy:.12f}")
    print(f"1/H={target:.12f}")
    print("n  mean[R/(n log n)]  standard_error  mean[(R-n log n/H)/n]")

    for n in sizes:
        ratios = []
        remainders = []
        for _ in range(repetitions):
            word = rng.choices(
                range(len(probabilities)), weights=probabilities, k=n
            )
            distinct = distinct_substrings_suffix_automaton(word)
            total = n * (n + 1) // 2
            deficit = total - distinct
            ratios.append(deficit / (n * math.log(n)))
            remainders.append((deficit - n * math.log(n) / entropy) / n)

        mean_ratio = statistics.fmean(ratios)
        se = statistics.stdev(ratios) / math.sqrt(repetitions)
        mean_remainder = statistics.fmean(remainders)
        print(
            f"{n:<6d} {mean_ratio:.12f}  {se:.12f}  {mean_remainder:.12f}"
        )
    print()


def main():
    sizes = [3000, 10000, 30000]
    repetitions = 80
    run_source([0.9, 0.1], sizes, repetitions, seed=1729)
    run_source([0.6, 0.3, 0.1], sizes, repetitions, seed=2718)


if __name__ == "__main__":
    main()
