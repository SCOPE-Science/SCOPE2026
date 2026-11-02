# Scientific review: parity-refined comparison shattering

## Correctness

**PASS.** The forest necessity follows from a directed-cycle assignment. The positive direction uses a proof of connectivity of the linear-extension graph by adjacent incomparable swaps, and a unique-extension lemma identifying precisely the consistently oriented spanning paths. The maximal-support count then uses Cayley's formula and a parity-swapping label transposition. The finite Littlestone table is supported by the exact induction recurrence, 1,322 leaf witnesses in full adaptive trees, and a replayed 121,279-state impossibility search for depth eleven at seven labels. All support classifications through six labels were checked by independent Boolean trace enumeration. Risks: the finite upper result depends on a correct software implementation and has no independent formal or expert certification; there is no claim beyond seven labels for adaptive depth.

## Originality

**PASS on accessible evidence, with residual priority risk.** Maass–Turán (1992, p. 139) proves that unrestricted linear orders shatter exactly the forests, which is explicitly acknowledged, but unrestricted shattering does not imply the parity condition or the count for even permutations. Walker (2022) proves general tree-dimension bounds, not a restricted permutation-class classification. Raz (2000) uses another permutation VC notion. Berendsohn–Kozma–Marx (2019) studies pattern algorithms rather than binary pairwise-comparison shattering. The unrestricted-order result does not imply the new parity-constrained bounds; semantic database queries did not surface a stronger implication. Historical coverage is not guaranteed.

## Value

**PASS.** Alternating permutations form the index-two subgroup of the natural total-order family. Restricting the allowed orders changes the parity of singleton extensions and creates a modulo-four variation in the number of maximal shattered query supports while preserving the static dimension for all orders at least four. The finite adaptive calculation also gives the first exact cardinality-bound obstruction in this restricted family, supplying a precise boundary for a natural learning invariant rather than an arbitrary graph slice.

## Limitations and closest literature

The exhaustive adaptive result ends at seven labels; the all-order VC characterization does not. Maass–Turán's full-class forest characterization is the nearest direct predecessor. Potentially relevant work on permutation learning under parity restrictions outside the inspected sources is a residual novelty risk. Computer replay is not independent external validation.

Self-review: passed. Independent audit: not yet performed.
