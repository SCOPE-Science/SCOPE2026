"""Finite Hurwitz passport scoping for RS-pullback degrees d <= 10.

RS-pullback picture used here (Kitaev/Doran/Vidunas): a rational map
phi: P1 -> P1 of degree d with R-part branching partitions over 3 points,
plus extra critical values ("m-parameter" in Kitaev). For the TARGET we
only need a SCOPING count: enumerate integer ramification profiles that
satisfy Riemann-Hurwitz for genus-0 covers of degree d<=10 with <=4
critical values, and count how many survive the order-7 local-monodromy
constraint (some ramification index divisible by 7 in the relevant fibre).
This bounds the search space; it does not itself construct or rule out maps.

Output: per-degree counts of admissible profiles, and the surviving list.
"""
from itertools import combinations_with_replacement


def partitions_of(n, max_part=None):
    if n == 0:
        yield []
        return
    if max_part is None:
        max_part = n
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions_of(n - first, first):
            yield [first] + rest


def ramification_contrib(part):
    return sum(e - 1 for e in part)


def admissible_profiles(d, nvals=4):
    """Profiles = list of nvals partitions of d with total RH defect 2d-2
    (genus 0) — necessary condition for rational phi."""
    parts = list(partitions_of(d))
    out = []
    # iterate over multisets of partitions (order of critical values ignored)
    for combo in combinations_with_replacement(parts, nvals):
        if sum(ramification_contrib(p) for p in combo) == 2 * d - 2:
            out.append(combo)
    return out


def has_seven(prof):
    return any(7 in p for p in prof)


for d in range(2, 11):
    profs = admissible_profiles(d)
    sev = [p for p in profs if has_seven(p)]
    print(f"d={d}: total genus-0 4-critical-value profiles={len(profs)}, "
          f"with a ramification index 7 (order-7 compatible)={len(sev)}")
    for p in sev[:12]:
        print("   ", p)
    if len(sev) > 12:
        print(f"    ... ({len(sev)-12} more)")
