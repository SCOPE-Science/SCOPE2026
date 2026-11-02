# Scientific review

## Correctness — PASS

The variance objective follows by a covariance/absolute-distance identity, using independent reflected Gaussian pairs. The exact Gaussian kernel second derivative has one curvature sign transition at \(2\sigma\sqrt{\log2}\). Strict exchange inequalities imply unique rank and reverse-rank optima in their respective domains. A two-pair family proves the limiting zero approximation ratio analytically. All assumptions are stated explicitly, and the standalone numerical checker passes 2,492 checks. No finite experiment is used to infer a universal result.

## Originality — PASS (with residual priority risk)

Abkin and Daripa's 2026 paper supplies the fixed-matching gain and the rank matching partner-distance inequality. The published arguments do not optimize the *sum* of Gaussian gains across arbitrary pairings or derive its curvature phase or unbounded rank-gain loss. Peyre's optimal-matching notes contain the standard convex/concave exchange framework, credited here, but not this Gaussian kernel threshold and counterexample in reflected particle variance. Semantic literature and mathematical-result searches have not located an equivalent specialized theorem. Classical/general rearrangement may imply the exchange half of the claim when instantiated, so the contribution is only the application-specific exact threshold and failure of a natural pairing guarantee; complete historical priority is not certified.

## Value — PASS

Rank matching is computationally natural and explicitly motivated in the source by minimum total partner distance. The theorem identifies when it is variance-optimal, when it is variance-worst, and shows that the partner-distance proxy has no multiplicative reliability guarantee even for all-positive particles. The statements give a reproducible diagnostic for choosing matching strategies before diffusion and have a sharp, algorithmically interpretable threshold. Their scope remains conditional and one-stage; no global nonlinear performance claim is made.

## Closest literature and limitations

Abkin--Daripa, arXiv:2610.01120v2, Sections 3.1--3.3 and 4.4, supplies the exact reduction expression and rank-distance rearrangement. Peyre, *Optimal Matching between Point Clouds*, supplies standard one-dimensional convex/concave matching exchanges. A specialized older antithetic-matching result not recovered by the comparisons remains possible. The result assumes equal positive masses and independent matching pairs.

Self-review: passed. Independent audit: not yet performed.
