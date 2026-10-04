# Review

## Correctness

PASS. The ridit variance is exactly
\[
\frac{1-\sum_i p_i^3}{12}.
\]
Every increasing score decomposes into a positive linear combination of centered cumulative-cut indicators. For the cut after category \(j\), the exact covariance with the ridit score is
\[
\frac{P_j(1-P_j)}2,
\]
so its correlation is the stated cut constant.

The lower bound follows by applying the minimum ray correlation before the triangle inequality. Strictly positive score gaps make the triangle inequality strict when there are at least three categories. A one-dominant-gap sequence proves sharpness. Cauchy--Schwarz gives the upper endpoint, with equality exactly for positive affine ridit scoring. Connectedness gives every intermediate value.

## Originality

PASS, with a residual older isotonic/scoring-literature risk. Chen and Wang's complete open article was inspected through its scoring-system section, uniform-latent ridit corollary, examples, conclusion, and appendix. It defines the same ridit scores and discusses sensitivity of correlation analyses to score choice, but does not give a universal profile-dependent correlation floor.

Graubard--Korn and the Kimeldorf--Sampson--Whitaker line address consequences of score choice for ordinal tests. Their optimized objects depend on a two-sample or contingency-table testing problem rather than the intrinsic Pearson angle between one arbitrary increasing coding and its probability-determined ridit coding.

The closest prior fixed-profile Gini result gives only the upper, ridit-affine equality direction through a dispersion inequality. It does not imply the lower endpoint, lower extremizers, or complete attainable interval.

Targeted semantic database and web searches for ridit correlation floors, arbitrary monotone scores, midrank-score robustness, and fixed category probabilities did not locate the displayed constant.

## Value

PASS. Assigning numerical values to ordinal categories is a basic modeling choice, and the literature explicitly warns that conclusions can depend on that choice. The result gives a complete robustness envelope for one canonical probability-based scoring system: it quantifies exactly how weak linear agreement with ridits can become while the ordering is preserved, and identifies both the worst collapse pattern and the unique perfect-alignment scoring.

For equally frequent categories the floor simplifies to
\[
\sqrt{\frac3{m+1}},
\]
which gives an immediate category-count benchmark without numerical optimization.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK variance_checks=44000 cut_checks=175354 lower_checks=40827 upper_equality_checks=22000 boundary_checks=18827 equal_mass_checks=98`.
