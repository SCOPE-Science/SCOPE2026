# Review of the sharp two-bit finite de Finetti projection

## Correctness

**PASS.** The exchangeable two-bit law is fully parametrized by its two diagonal masses. A direct four-atom calculation gives the exact total-variation expression. Infinite exchangeability is equivalent to a nonnegative mixing measure over Bernoulli product laws; Minkowski's inequality makes the square roots of the two diagonal masses sum to at least one, with equality only for a point-mass mixture. For a negative-covariance target, any candidate smaller than the target on either diagonal is strictly beaten by an admissible endpoint product. In the remaining quadrant the distance reduces to the sum of diagonal excesses; a strictly convex scalar minimization gives the stated unique product approximation. The urn reduction and a checked monotonicity calculation give the sharp even/odd finite-extension radius for every integer \(N\ge2\). The standard-library verifier recomputed all 1,323 finite urns for \(2\le N\le50\) and checked 9,240 sampled product or two-point-mixture competitors. These checks supplement, rather than replace, the proof.

## Originality

**PASS, with explicitly bounded bibliographic uncertainty.** The motivating 2021 Carlier–Friesecke–Vögler article characterizes finitely exchangeable extreme-point laws and their correlated corrections, but its fixed-population polynomial and total-variation order estimate do not perform the nearest-point optimization in the space of infinitely extendible two-bit laws. The 2024 Gavalakis–Johnson–Kontoyiannis full-text survey states universal finite de Finetti total-variation bounds and relative-entropy results; these do not imply the optimized three-phase projection, the unique approximating Bernoulli parameter, or the parity-dependent exact binary radius. Volfovsky–Airoldi's full-text restatement of Diaconis–Freedman gives a general sampling bound, not the optimized two-symbol radius. Relevant alternatives include finite-alphabet bound improvements, an equivalent Hausdorff-moment formulation, and the possibility that older works contain the exact binary projection; the original 1980 source was not fully accessible and its complete noncoverage cannot be asserted.

## Value

**PASS.** The binary two-marginal is the smallest nontrivial finite-exchangeability obstruction. The theorem gives a complete distance and optimizer for every negatively correlated pair, identifies an optimal approximation that is generically *not* the empirical-frequency product, and solves the natural sharp worst-case extension problem with distinct even and odd constants. The scope is mathematically natural and supplies more than a routine restatement of a generic asymptotic error bound. It does not claim extensions to more coordinates or to a fixed-mean projection.

Self-review: passed. Independent audit: not yet performed.
