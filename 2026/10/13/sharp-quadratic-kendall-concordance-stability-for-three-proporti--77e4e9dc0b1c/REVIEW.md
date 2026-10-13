# Scientific review: sharp three-rate Kendall concordance stability

## Correctness — PASS
An exponential-racing representation separates the first arrival from the second gap, and direct integration of an exponential-difference density yields a finite rational expression for population tau. After sorting the normalized rates, a displayed positive denominator transforms the full continuous-domain inequality into a homogeneous polynomial with 40 strictly positive integer monomial coefficients; the included stand-alone exact symbolic checker reconstructs and verifies all coefficients and both endpoint computations. Strict interior equality and boundary sharpness follow. The theorem does not claim a stronger coefficient inside the open simplex or any empirical sample-size guarantee.

## Originality — PASS
Kochar (arXiv:2202.07874, Theorems 3.2–3.3) proves stronger stochastic-increasing comparison and, as a consequence, an unpenalized Kendall tau ceiling. That theorem establishes no numerical lower bound on the **concordance deficit** as a function of normalized rate dispersion and hence does not imply the exact optimal coefficient. Avérous–Genest–Kochar (2005) derive homogeneous-sample rank dependence, not three heterogeneous hazards. Kochar–Spizzichino (2023) treats exchangeably dependent time-transformed lifetimes. Genest–Kochar–Xu (2009) compare the extremes of heterogeneous samples rather than their first two order statistics and do not entail this bound. Published and mathematical-record searches on these aliases did not identify a dominating quantitative result. Priority risk remains from literature not available in full and differently parameterized formulas; an unsuccessful search is not a novelty proof.

## Value — PASS
The first two failures are natural observables in reliability and competing-risk models. Kochar's qualitative concordance comparison does not quantify the effect of unequal rates. The exact sharp quadratic deficit gives a scale-invariant, baseline-invariant global upper envelope indexed by a canonical hazard-dispersion statistic. The coefficient is optimal and forced by an interpretable two-active-component boundary, and strict equal-rate extremality holds throughout the admissible interior. The result is restricted to three components; general multicomponent stability remains unresolved here.

## Closest sources and residual risks
- S. Kochar, *Dependence comparisons of order statistics in the proportional hazards model*, 2022, arXiv:2202.07874, Theorems 3.2–3.3 (full journal HTML inspected).
- J. Avérous, C. Genest, S. C. Kochar, *On the dependence structure of order statistics*, 2005, doi:10.1016/j.jmva.2004.03.004 (author-hosted article PDF inspected).
- S. Kochar and F. Spizzichino, *Dependence among order statistics for time-transformed exponential models*, 2023, doi:10.1017/S0269964823000190 (full journal HTML inspected).
- Fuchs–Schmidt's related Kendall-order-statistics article could not be examined in complete text; its accessible description concerns parent-versus-order dependence and is not known to cover this specific sharp three-rate stability theorem.

Self-review: passed. Independent audit: not yet performed.
