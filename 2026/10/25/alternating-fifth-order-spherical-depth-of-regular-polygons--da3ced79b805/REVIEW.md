# Scientific review: alternating spherical depth of regular polygons

## Correctness — PASS

The theorem specifies an integer side count, independent uniform-area sampling, a fixed center, and the closed-diameter-disk event. The angular marginal is derived directly from the radial function of each side sector. The finite cyclic count is valid for every odd side count including three, and exact symmetries handle even side counts. The strict sign follows from an outward-mixture representation and a four-case proof of the universal central-rectangle strip inequality. Polynomial integration gives the coefficient \(-5/96\), and a uniform angular-density expansion with exactly vanishing linear terms yields the stated \(n^{-5}\) limit and \(O(n^{-7})\) error. The elementary expression has the correct logarithmic limit at \(n=3\). The supplied script verifies critical exact algebra and independent numerical integrations; no finite experiment is used in place of an infinite proof.

## Originality — PASS, with disclosed limits

Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk* (arXiv:2608.27491v1), supplies the general directional transfer and the triangular formula, including the \(n=3\) instance. Those statements do not determine the regular-polygon sign pattern, nor do they imply the fourth-order cancellation inside a sector or the resulting fifth-order side-count asymptotic. Bremner–Shahsavarifar (arXiv:1702.07399) concerns computational spherical-depth algorithms; only its abstract was available for inspection, so no whole-paper novelty assertion is made about it. Relevant indexed records on random center-passing chords, directional perimeter cuts, and normal-count deficits treat distinct observables. These are implication comparisons, not merely title comparisons. Priority uncertainty remains for older or unindexed analytic point-pair geometry and uninspected portions of the motivating paper.

## Value — PASS

The 2026 triangular incenter problem has a natural extension to regular tangential polygons. Central symmetry makes all even orders exactly one half, but the noncentrally-symmetric odd orders require analysis. The result is a complete strict classification by side-count residue modulo four, an elementary exact formula for every odd count, and a sharp fifth-order limiting law. The main anti-concentration lemma explains the geometry behind the sign instead of relying on an isolated numerical calculation. The known equilateral case and trivial centrally symmetric case are identified as background, not presented as new.

Self-review: passed. Independent audit: not yet performed.
