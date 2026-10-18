# Mathematical assessment

## Correctness

**PASS.** Conditioning on the last vacant parking place yields two smaller independent parking subproblems and a signed binary interleaving. The adjacent-pair involution computes the interleaving sign sum exactly. Parity-separated recurrences yield a formal differential identity whose coefficient induction is strictly positive at every degree. The normalization uses the classical count of parking functions. The standalone script implements independent exact checks with exhaustive preference vectors through six cars and independent dynamic programming through thirteen cars; these checks do not replace the general proof.

## Originality

**PASS on the inspected material, subject to a historical-priority risk.** Pinsky, arXiv:2404.11529, Theorem 1, gives the full outcome-permutation mass function. This mathematically determines a parity probability by a sum, and is credited as the dominating prior pointwise distribution; it does not state the strict parity sign theorem or a coefficientwise-positive generating differential identity in the examined statement/proof. Stanley and Yin, arXiv:2306.08681, Section 2, track descent statistics rather than parity of outcome inversions. Celano et al., arXiv:2508.11587, Section 1, count inversions of preference lists, which are not the same as outcome inversions. A different older signed-enumeration identity could still recover the present result; no independent priority certification has been performed.

## Value

**PASS.** Parity is an intrinsic coarse invariant of the highly nonuniform induced permutation law. The strict majority of even outcomes for *every* sample size is not determined qualitatively by marginal permutations or by a finite list of examples. The reduction from factorial-size signed summation to a quadratic-arithmetic recurrence, together with a positivity explanation through a formal ODE, provides a reusable structural description of cancellation in parking outcomes. It leaves the asymptotic size of the positive bias open.

Self-review: passed. Independent audit: not yet performed.
