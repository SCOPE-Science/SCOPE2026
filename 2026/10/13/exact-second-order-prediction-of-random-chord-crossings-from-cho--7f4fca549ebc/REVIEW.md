# Self-review

## Correctness — PASS

The object is the geometric crossing count of \(n\ge2\) independently and uniformly sampled endpoint-paired chords in a unit circle. A short-arc fraction is determined by each chord's Euclidean length. Rotation of the second chord against a fixed first chord gives conditional crossing probability \(2\min(r,s)\) by a symmetric-difference arc calculation. Distinct crossing indicators, even when sharing one chord, are pairwise independent once the complete chord-length vector is fixed, because conditional success probabilities do not depend on the shared chord's rotation. This justifies the exact conditional variance as a sum of Bernoulli variances. Independent short-arc fractions have density \(2\); four explicit integrals and a count of overlapping pairs give the unconditional variance decomposition. The attached script verifies identities symbolically and provides independent geometric simulations; the universal proof is analytic and does not rely on finite testing.

## Originality — PASS, with residual historical uncertainty

Acan (arXiv:1501.01489v1), Flajolet and Noy (INRIA RR-3914), Bortolotto and Souza (arXiv:2504.12866v1), and Bortolotto and Ramos (DOI 10.1112/mtk.70024) were compared at the level of objects, hypotheses, and conclusions. Flajolet and Noy explicitly establish the unconditional crossing mean and variance; these are *not* claimed as original. Acan's chord length is a discrete number of intervening endpoints, rather than the Euclidean length produced by random endpoint spacing. The geometric papers treat intersection positions or one-pair probabilities, not an exact formula for \(\mathbb E[X_n\mid L_1,\dots,L_n]\), its conditional variance, or the sharp full-vector explained fraction. Targeted public and mathematical-record searches found no same-statement coverage, although that does not prove absolute priority. A direct older short-arc intersection identity, or a combination of general conditional \(U\)-statistic projection principles, could imply a part of the result and remains an explicit residual risk.

## Mathematical value — PASS

The crossing count records the topology of a full circular arrangement, whereas measured chord lengths provide purely geometric information. The result establishes the *optimal* predictor from all lengths and its exact, nonasymptotic residual mean-square error, then shows length information explains a fraction tending to 100% of the entire \(O(n^3)\) crossing-count variance. The sharp formula \((4n-3)/(4n+12)\) is a natural dimensionless measure of how much random orientation still matters at each sample size; the residual conditional variance is only \(O(n^2)\). This is stronger and more structurally motivated than a small numerical gain or a single marginal moment.

## Source and proof limitations

The result applies only to independent uniform endpoint chords, not other Bertrand models. Pairwise conditional independence does not yield mutual independence or a conditional distribution. Prior literature contains the unconditional crossing-count moments, and may contain an unlocated implication of the conditional identity. All computations in `verify.py` are corroborative, not substitutes for the displayed argument.

Self-review: passed. Independent audit: not yet performed.
