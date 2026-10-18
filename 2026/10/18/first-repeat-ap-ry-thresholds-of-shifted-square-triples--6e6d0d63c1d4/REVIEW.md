# Scientific review

## Correctness — PASS
The claim concerns the first integer in every residue class with at least two distinct nonnegative representations. The proof constructs an exact bijection between representations and pairs of height and fourth-offset coefficient, orders the two cheapest costs with a nondecreasing-height lemma, then derives genus and Frobenius number by residue counting. The four-branch simplification and the twelve small-base entries follow from explicit algebra. The independent capped coin-change verifier checks 80,199 residue thresholds through base 400 and both numerical formulas through base 1100. No extrapolation from these finite checks is used in the proof.

## Originality — PASS with residual risk
The original shifted-square source [1] computes only the classical \(p=0\) Frobenius invariant. The closest \(p\)-numerical-semigroup paper [3] proves arithmetic-progression formulas, not the offset pattern \((0,1,4)\). The broader explicit triple theorem [5] requires divisibility conditions absent for \(a\ge14\); the general Apéry machinery [4] computes invariants only after their residue sets have been independently determined. Related mathematical statements found in literature and database searches were compared for exact implications; inspected results do not imply the second-cost classification. Residual possibility of earlier unindexed equivalent formulas is expressly retained. The preceding facts support originality within the checked scope, not a universal uniqueness assertion.

## Mathematical value — PASS
The natural shifted-square family is already motivated by the classical Frobenius literature, but the first repeated-representation boundary is a different structural problem. The result supplies the complete first-repeat Apéry set, two standard multiplicity invariants, a sharp eventual period-four quadratic law, and the complete smaller-base table. This resolves a motivated infinite family rather than an arbitrary finite slice, trivial renaming, or unmotivated numerical table.

## Limitations and closest sources
Most relevant: Liu–Xin's shifted-power Frobenius manuscript (arXiv:2210.02722v1), Komatsu–Ying's arithmetic progression \(p\)-Frobenius manuscript (arXiv:2206.13052), Komatsu's general \(p\)-Apéry method (arXiv:2111.11021), and Subwattanachai's conditional three-variable theorem (arXiv:2309.09149). General bibliographic coverage may be incomplete. The standalone verifier checks finite instances and cannot replace the infinite proof. The theorem does not cover \(p\ge2\) or longer shifted-square sequences.

Self-review: passed. Independent audit: not yet performed.
