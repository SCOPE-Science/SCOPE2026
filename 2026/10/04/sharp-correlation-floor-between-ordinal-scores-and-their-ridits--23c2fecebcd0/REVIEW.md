# Independent mathematical audit

## correctness

PASS

Ridit scores are the midpoints of the probability cells, so E[Q]=1/2 and the law-of-total-variance calculation gives Var(Q)=(1-sum p_i^3)/12. For each cut j, the centered upper-block indicator H_j has variance P_j(1-P_j) and covariance with Q equal to P_j(1-P_j)/2. Every centered strictly increasing score decomposes as sum d_j H_j with all adjacent gaps d_j>0. Taking the minimum cut correlation, linearity of covariance and the L2 triangle inequality give the stated lower bound; for m>=3 the triangle inequality is strict because distinct cut indicators are not positive scalar multiples. A single dominant gap approaches any minimizing cut, proving sharpness; Cauchy--Schwarz gives the upper endpoint and positive-affine ridit scoring is its equality case; connectedness of the strict-score cone gives the full attainable interval. An independent exact-rational replay on random profiles confirmed the lower inequality and the equal-mass specialization; the package verifier performs a substantially larger exact-rational stress test.

## originality

PASS

Chen--Wang's complete open article defines ridit scores as the probability-cell midpoints, develops alternative ordinal scoring systems, and demonstrates that score choice changes correlation-based conclusions; it does not state a profile-dependent sharp correlation floor relative to ridits. Kimeldorf--Sampson--Whitaker study minimum and maximum monotone scores for a two-sample ordinal testing problem, a different observed-data objective. Open descriptions were compared and an authorized full-text request found no verified PDF, so that same-topic source remains an explicit residual risk rather than being treated as covered. Targeted Resultary search did not locate the displayed lower constant or complete attainable interval. The accepted originality is the intrinsic fixed-marginal cone geometry of score-vs-ridit Pearson correlation, not the general fact that ordinal-score choice matters.

## value

PASS

Ridits are a standard probability-determined coding of ordered categories, while arbitrary increasing numerical codings are ubiquitous. The theorem gives the exact worst possible linear alignment for a fixed probability profile, identifies the limiting two-level extremizers, characterizes the unique upper equality case, and determines the whole attainable interval. This is a natural robustness invariant of ordinal scoring rather than an arbitrary score example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
