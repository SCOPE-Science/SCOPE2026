# Scientific review: explicit super-domination enumerator on forests

## Correctness — PASS

For every finite simple forest, the proposed message contains exactly one of four local triples for each of two possible colors of a parent's vertex. The proof fixes the witness requirement of each white descendant, tracks whether the current white vertex remains unresolved, and tracks whether a black vertex could witness its white parent. The transition rejects a pending white child when its parent is white and, for a black parent, requires a unique white neighbor. The root test excludes fictitious witnesses. These local equivalences inductively prove every coefficient, including for isolated vertices and empty forests.

A standalone verifier checked 3,363,980 candidate subsets across 1442 labeled trees and 400 seeded random forests, the maximum-matching minimum degree, and relabeling and path boundary cases. Checks passed; tests are supplementary and do not replace the proof. Each numeric count comes from the actual script in the package.

## Originality — PASS, with residual literature and metatheorem risks

Section 7(d) of Ghanbari–Jäger–Lehtilä, arXiv:2209.01795, asks for the count of minimum super-dominating sets in trees. Their Section 6 enumerates minima for specific families, not all trees. Bujtás–Ghanbari–Klavžar, arXiv:2302.08862, establish minimum **size** by maximum matching, not the full distribution. Kaidash, DOI:10.1007/978-3-031-73365-9_6, introduces the polynomial and reports formulas for some families, but its full chapter text was inaccessible; this is a real unresolved overlap risk. Counting MSO-definable sets on bounded-treewidth graphs was already known to be polynomial-time possible (Courcelle–Makowsky–Rotics, 2001); mere tractability and the tree minimum-cardinality formula are **not claimed as new**.

The new mathematical claim is instead the specific explicit eight-message witness-state recurrence, exact child transitions, and reproducible coefficient algorithm for **every** forest. Targeted searches and available full-text comparisons revealed no equivalent such small-state enumerator. Search failure alone is not proof of novelty, and earlier equivalent formulations may exist.

## Value — PASS

The exact open counting question for trees motivates the concrete complete cardinality distribution, which is stronger than one minimum-size or one family-specific formula. The local witness dependency requires tracking both pending white children and potential parent witnesses, yielding a nontrivial recurrence that can calculate all coefficients and exact numbers of minimum sets on arbitrarily branching or disconnected forests. The explicit small state space provides implementable information beyond an abstract bounded-treewidth tractability guarantee.

## Main scope limits

This result does not cover graphs containing cycles, establish an optimal state count, or prove new generic polynomial-time tractability on bounded-treewidth classes. The algorithm counts integer arithmetic operations and uses coefficients of potentially \(n\) bits. The inaccessible Kaidash chapter and unindexed equivalent algorithms remain originality risks.

Self-review: passed. Independent audit: not yet performed.
