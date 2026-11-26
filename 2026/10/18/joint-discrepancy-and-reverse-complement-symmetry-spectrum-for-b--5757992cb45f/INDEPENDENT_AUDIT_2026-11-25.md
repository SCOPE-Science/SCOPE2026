# Independent mathematical audit

## correctness

PASS

A valid length-32 cycle traverses all 32 five-bit states via a permutation. For each four-bit tail the two incoming first-bit choices must append opposite bits, giving a unique feedback truth table. A full orbit from 00000 is therefore both necessary and sufficient, without duplicate rotations. The balance of the period makes its maximum absolute circular-factor imbalance the prefix-sum range, including when a factor wraps. Independently, exhaustive Euler-tour traversal of the four-bit graph, with five-bit edges and 00000 first, reproduced the claim using direct circular-factor discrepancy. Every cyclic class has this single anchor, and the search tries each unused outgoing edge and requires closure after all 32 edges. It visited 92,636 search nodes and accepted 2,048 tours, with a direct five-factor check on each. At D=5,6,7,8 it obtained total counts (224,688,912,224), CR counts (16,16,24,8), and no individually complement- or reversal-fixed cycle; direct orbit deduplication gave sizes 2 and 4 with counts (8,8,12,4) and (52,168,222,54), respectively. Equivalently the order-four action has stabilizer {1,cr} precisely for CR-fixed classes, and otherwise trivial stabilizer. The total is 528. All four literal witness strings in RESULT.md also passed direct tests. Replay the bounded independent enumeration with `python3 /workspace/branches/4c3a7688-cbdf-4235-8dab-7616449dde75/independent_edge_census.py` (without --limit); the saved output is independent_edge_census.txt next to that file. The supplied scripts were inspected, not executed. The half-word enumeration relies on the fixed-point-free reflected index involution for a CR period (its reflection parameter is odd, hence can be shifted to 31), and exhausts only the CR subset. No claim at another order follows.

## originality

PASS

The unrestricted order-five marginal and the D=5 orbit split are explicitly covered by the earlier exact census, and the CR characterization is prior work. Accept the remaining cross-classification: the nonminimal discrepancy strata conditioned on CR and their orbit counts. None of the strongest examined statements gives those cells or fixes them via its stated marginal data.

## value

PASS

Reverse-complement symmetry selects an established class of de Bruijn cycles, and circular discrepancy is a natural quantitative balance criterion within that class. The nonminimal cells tell how many distinct symmetry-constrained cycles and orbits exist at each feasible imbalance, information that neither an optimal witness nor the unrestricted marginal supplies. This is a useful complete finite benchmark at a specified natural order, not a claim that the previously known minima or marginals are new or that the pattern persists at larger orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
