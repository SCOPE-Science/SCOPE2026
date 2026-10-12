# Scientific review: proportional-beta mean-tail monotonicity

## Correctness — PASS

The proof covers every real beta concentration \(\tau>0\) and every \(p\in(0,1)\), with the strict and symmetric cases separated. It reduces the sign to an explicit rational derivative calculation for the paired Bernoulli-relative-entropy branches: \(J_r(w)>0\) throughout the necessary parameter range. The ratio-of-integrals comparison proves that the relative branch displacement decreases at every positive energy. Transforming the beta density to log-odds gives an exact positive exponential-tilt representation, not an asymptotic approximation. The two limiting values follow from the integrability properties of the transformed density; the binomial assertion follows from the exact regularized-beta identity. The bundled exact rational checks returned 600 tail values, 576 comparisons, and 3,469 derivative checks. Finite checks corroborate rather than establish the universal theorem.

## Originality — PASS, with residual priority risk

Babichenko, Feldman, Holzman, and Narayan explicitly leave the exact binomial infimum as a conjecture (arXiv:2312.01874v1, Remark 2). The available expanded author-hosted treatment also retains it as a conjecture. The closest source on beta CDF monotonicity is Hornik (2024), Theorems 1–2, which varies one shape while keeping the second fixed. Leobacher and Steinicke (2026), Lemma 18, likewise vary one shape and its threshold while keeping the other fixed. Karp (2015) treats log-concavity in individual shape coordinates, not this sign along a proportional-shape ray. Direct implication checks distinguish these results from the claim, despite similar vocabulary and beta-function notation. Independent historical priority remains a legitimate risk; searches cannot establish absolute novelty.

## Value — PASS

The specific exact finite-agent threshold was posed as an open quantitative conjecture in a substantial fair-division result. Its determination gives a necessary-and-sufficient finite-\(n\) quantile-share threshold for the matroid-rank class under the established interpretation in that source. The proof's stronger analytic statement gives a strict, all-concentration order for probability mass to one side of the mean of a natural two-parameter beta family. This is a structured infinite-family result rather than a numerical slice, a reparameterization, or a routine special case of the inspected coordinatewise results.

## Closest literature and limits

Primary sources: Babichenko et al., arXiv:2312.01874v1, Remark 2; Hornik, *Entropy* 26 (2024), 938, Theorems 1–2; Leobacher–Steinicke, arXiv:2605.21424v1, §2 and Lemma 18; Karp, arXiv:1509.05120v1, §2. The result does not prove universal quantile feasibility, the Erdős matching conjecture, or distributional ordering of beta variables away from their mean. Historical equivalent formulations may exist in beta-function, gamma-ratio, or binomial-tail literature.

Self-review: passed. Independent audit: not yet performed.
