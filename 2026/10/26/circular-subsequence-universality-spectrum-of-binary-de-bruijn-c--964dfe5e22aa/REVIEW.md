# Review of the order-five circular subsequence-universality classification

## Correctness
The precise domain is all binary de Bruijn cycles of order five, modulo rotations only. The Hamiltonian-window traversal exhausts all uniquely zero-window-rooted cycles; the independent Euler-edge traversal produces the same canonical set. Each of the \(2048\) distinct cycles has all length-five cyclic factors verified. The backward shortest-absent-subsequence recurrence follows by factoring at the earliest occurrence of the initial letter; comparing it with the independently implemented greedy arch computation verifies all \(32\) rotations of every cycle. The exact counts \(512\) and \(1536\), canonical joint table, and complementation/reversal orbit refinement are rechecked by `verify.py`, including the entire supplied certificate. The result is exact finite enumeration, not an infinite inference from experiments.

## Originality
Hébrard (1991) introduced the arch method. Barker et al. (2020) introduced circular scattered-factor universality and explicitly mention de Bruijn sequences as motivation; their Section 4 gives general bounds and computational principles rather than this order-five conditional enumeration. Fleischmann et al. (2021) and Schnoebelen–Veron (2023) further analyze circular indices and algorithms. A published finite-length distribution of ordinary binary words by subsequence-universality index does not count only de Bruijn cycles or their maximizing rotations. No exact order-five tally was found in the inspected primary materials or targeted semantic/database searches. The 1991 full text was inaccessible; equivalent unindexed or otherwise unexamined tables remain a priority risk.

## Value
A de Bruijn cycle is optimal for contiguous factor coverage, but cyclic **scattered** coverage after deletions is a different natural measure. At the first order with more than a small handful of inequivalent cycles and a nonuniform index split, the theorem establishes that exactly one quarter of all cycles reach only index \(10\), while three quarters attain \(11\). This is a natural complete finite classification useful for selecting de Bruijn test patterns when deletion-robust diversity is relevant, and as a benchmark for exact circular-universality algorithms. Neither uniqueness of the count nor proof reproducibility alone is being used as its value argument.

## Remaining risks
The theorem does not generalize to arbitrary de Bruijn order. Its proof is computer-assisted and awaits independent audit. A closed-form count for every order, a table contained in an inaccessible specialized source, or a previously tabulated equivalent orbit distribution could subsume the historical novelty. No such implication was verified during this review.

Self-review: passed. Independent audit: not yet performed.
