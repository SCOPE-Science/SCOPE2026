# Scientific assessment

## Correctness — PASS

The three normalized measurement rows have exact determinant \(\varepsilon^2(1-\varepsilon)/3\), so uniqueness holds precisely on the stated open parameter interval. Expressing the original overlapping integrals through three disjoint cell means allows an exact operator-norm calculation rather than an unjustified assumption of independent overlapping data. The proof shows analytically that the maximum is reached at the center or an endpoint; the two exact branches cross at the unique minimizer, and the original-measurement coefficient bound has equality at an endpoint. Exact-rational reproduction and kernel identities were checked in the attached verifier (414575 check groups). Risk: finite tests alone do not establish continuum assertions; all continuum claims depend on the written inequalities, reviewed term by term.

## Originality — PASS, with priority limitation

The full arXiv manuscript of Bruni Bruno–Erb (2023), especially §§2–4, establishes the *general* segmental Vandermonde framework, the inequality \(\|\Pi\|\le\Lambda\), and equality for non-overlapping segments; its listed special families are concatenated segments, equal arc-length segments and common-left-endpoint segments. Our three rows (full interval plus a left and right truncation) are not one of those special families. Nor do its stated general results supply an exact shared-input \(L^\infty\) norm, the unique optimal trimming parameter or the unbounded slack ratio. The 2024 Fekete paper investigates determinant-optimal segment sets and generalized constants; the 2024 mock-Chebyshev paper studies other support layouts and related stability bounds. Relevant semantic research-record queries found interpolation, norm and three-interval results for different operators but no implication or numerical table covering the claim. Risk: a specialized equivalent three-average projection design may predate the checked sources; absence from ranked retrieval is not a uniqueness proof.

## Value — PASS

This is a naturally motivated first quadratic case in which all measured intervals overlap and the generalized Lebesgue number is not the true shared-function stability constant. The theorem gives a *unique implementable design*, a sharp explicit worst-case norm and extremizers, and a quantitative arbitrarily loose bound, not an arbitrary sampled numerical example. Its relevance is to selecting overlapping measurement supports and distinguishing input-function uncertainty from independent errors in individual sensors. It is a small, fully classified model rather than a general higher-degree theory.

## Scope and risk

The result assumes bounded measurable real input, precise interval means, exact arithmetic and degree at most two. It is not a bound for independent measurement noise, floating-point reconstruction or all interpolation geometries. Specialized publication-priority overlap is a residual risk.

Self-review: passed. Independent audit: not yet performed.
