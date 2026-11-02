# Scientific review

## Correctness — PASS

The drift is strictly stable for every nonnegative reciprocal coupling. Its stationary Lyapunov equation produces an explicitly factored nonnegative covariance determinant. The rank-one condition is necessary and sufficient for Pearson correlation one because the component variances and covariance are positive. Direct stationary-mode estimates establish the large-coupling limit. The rational example's derivative factors into a linear term and a cubic with exactly one positive root (Descartes and endpoint signs); the full-rank witness has a quartic with exactly two positive roots (Descartes and two disjoint sign changes). The covariance formulas and both factorizations were independently checked using `verify.py`. Limits: no nonlinear ecological claim and no generic uniqueness assertion for arbitrary parameters.

## Originality — PASS, provisional historical priority

Kendall et al., *American Naturalist* 155 (2000), DOI 10.1086/303350, were inspected through the author-uploaded full article (model, equations (1)–(9), discussion). They assume equal local return coefficients and equal noise variances, proving monotonicity in their discrete-time model, so the claim that heterogeneous local rates and forcing can create a finite perfect-synchrony point and then a correlation drop is not a result of their exact stated hypotheses. Liebhold, Johnson and Bjørnstad, *Population Ecology* 48 (2006), DOI 10.1007/s10144-005-0248-6, were inspected via a complete eight-page publicly hosted PDF, especially their model and synchrony simulations. They study local-rate heterogeneity in a second-order discrete-time model, but do not prove the proposed continuous-time exact parameter identity or complete two-extrema classification. The closest structured research records concerned different covariance identities and dynamical systems; none matched these premises and conclusions. The matrix-Gramian rank criterion is acknowledged as established linear systems theory, not presented as new. Ripa (2000) and Ly–Ermentrout (2010) remain partially inspected, posing a residual historical-priority risk. Failed targeted searches alone are not taken as proof of novelty.

## Value — PASS

Geographical variation in return rates is documented in the motivating population-ecology literature, and shared climatic forcing with unequal patch sensitivities is a natural two-patch idealization. Spatial synchrony affects metapopulation fluctuation risk. The result supplies a sharp, physically interpretable tuning rule and demonstrates a qualitative failure of the tempting monotonic-dispersal extrapolation from homogeneous models. The strictly positive-definite forcing example shows that the reversal is not an artifact restricted to perfectly common noise; its two extrema are globally classified and structurally stable. This is a structural boundary with ecological interpretation, not a routine numerical optimization or a claim about population persistence.

## Closest literature and limitations

The closest fully inspected studies are Kendall et al. (2000) and Liebhold et al. (2006). Ripa (2000) was available in abstract and bibliographic form, and the Ly–Ermentrout (2010) paper could not be accessed in full; their possible implications should be revisited by independent researchers. The result is mathematically restricted to centered linear Gaussian fluctuations and stationary equal-time correlation.

Self-review: passed. Independent audit: not yet performed.
