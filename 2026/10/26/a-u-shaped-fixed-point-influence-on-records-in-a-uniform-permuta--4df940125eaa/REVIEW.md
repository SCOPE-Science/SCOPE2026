# Review: U-shaped fixed-point influence on records

## Correctness
**PASS.** One-position conditioning is exact because the remaining permutation is uniform over the remaining values. The three disjoint cases of a specified fixed position lying before, at, or after a candidate record yield the complete cross-covariance kernel. Summation gives the conditional-mean identity. Binomial unimodality yields the complete sign classification for all sizes, and the boundary terms determine the aggregate asymptotic. The independently enumerated permutations through size eight agree with all formulas. The finite experiments supplement, but do not replace, the all-size counting argument.

## Originality
**PASS on inspected evidence, subject to priority uncertainty.** Dubach, *A geometric approach to conjugation-invariant random permutations* (arXiv:2402.10116), develops asymptotic record laws in permutation classes where the fixed-point count matters; the inspected records sections do not state the present finite-size conditioning on a fixed point at a specified position or the resulting U-shaped sign law. Grübel, *Ranks, copulas, and permutons* (2023), treats ranks and cycles and recalls Foata's distributional correspondence, without this same-permutation cross-covariance. The published fixed-point/descent covariance formula and published cycle-count/inversion law apply to different statistic pairs and do not imply the fixed-point/record calculation. An older implicit first-moment identity remains possible.

## Value
**PASS.** The fixed-point and record statistics are intrinsic and separately classical, but their joint dependence is not determined by the marginals or by Foata's correspondence. The result identifies a sharp all-size U-shaped influence profile: conditioning on a fixed point in the middle suppresses records whereas a fixed point near either edge enhances them. Exact cancellation leaves an aggregate positive covariance of order \(n^{-2}\). This makes precise a finite-location contrast complementary to prior work on large numbers of fixed points and record-count phase transitions.

## Remaining scientific boundaries
This is a statement about first mixed moments of a uniform permutation, not higher dependence, not conditioning on the complete fixed-point set, and not a full joint distribution. The derivation is elementary once the conditioning is recognized, so historical originality remains the main residual risk.

Self-review: passed. Independent audit: not yet performed.
