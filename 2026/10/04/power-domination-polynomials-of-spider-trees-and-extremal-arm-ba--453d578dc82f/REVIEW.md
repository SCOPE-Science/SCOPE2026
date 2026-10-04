# Review of Power domination polynomials of spider trees and extremal arm balances

## Correctness
PASS. The proof separates center-containing sets from center-free sets. For a center-free choice, every selected arm propagates to the center; the process succeeds exactly when at most one arm is untouched, while two untouched arms block the center permanently. This gives the exact polynomial. For extremality, with all other arms fixed, the center-free contribution for two lengths \(a,b\) is an affine strictly decreasing function of \(t^a+t^b\) for \(t=1+x>1\). Balancing therefore strictly increases and concentration strictly decreases the polynomial. The included definition-level exhaustive checker agrees on all tested spiders and the finite extremal census.

## Originality
PASS. The foundational 2018 source introduces the polynomial and computes several standard families but does not state the spider formula; its relevant path-attachment theorem explicitly excludes endpoint attachment. The 2022 spider paper concerns minimum power domination and Mycielskian constructions rather than all-set enumeration. The inspected 2025 polynomial-entropy paper treats additional named families but no spiders. Targeted exact and semantic searches using spider, starlike-tree, and subdivided-star terminology did not locate the all-set formula or the strict arm-balance extremal theorem. Residual risk remains for differently phrased or non-indexed prior work.

## Value
PASS. The ordinary power domination number of every spider is one, so it discards all arm-length geometry. The polynomial records the full size distribution of feasible monitoring sets, while the extremal theorem identifies, uniformly for every positive activity \(x\), the unique arm profiles with greatest and least redundancy at fixed size and branch count. This is a structural counting refinement of a standard graph-monitoring invariant rather than a routine restatement of the minimum parameter.

Same-model review: passed. Independent audit: not yet performed.
