# Independent mathematical audit

## correctness

PASS

Condition first on the entire ordered labeled path, contract it to one component together with n−k−1 singleton components, and cancel the monomial for its fixed edges when counting excess degrees. The contracted Prüfer code contributes n−k−2 independent trials weighted by component sizes. The compulsory incidence of the path component and the additional incidences choose independent uniform endpoints on the path. This gives exactly the two PGF factors, independently of which labels form the path, so conditioning only on its length gives the same law. Covariances at distinct sites add the negative contributions from a single compulsory ball and the independent trials, and a spanning path needs no trials or attachments. For the functional limit, use uniforms independent of R to represent the site's allocation and evaluate their centered empirical process at a_n(t)=floor(tℓ_n)/ℓ_n. The difference between tR and a_n(t)R, divided by sqrt(μ_n), tends uniformly to zero since R/μ_n→1 and μ_n≤ℓ_n+1. Donsker's continuous bridge limit gives asymptotic uniform equicontinuity, so replacing a_n(t) by t changes the empirical part by o_P(1). For bounded continuous empirical-process test functions, conditional expectations given R converge to their bridge expectations because R→∞ in probability; joint tightness then gives asymptotic independence from the centered total. The binomial variance divided by μ_n tends to 1−θ; the binomial CLT applies for θ<1 and Chebyshev gives the zero total fluctuation at θ=1. Adding the two independent terms yields the stated covariance and both endpoint regimes in J1. An independent edge-set enumeration through n=5 matched the full conditional finite laws including spanning paths: python3 review_evidence/frozen_math_spot_checks.py. The frozen Prüfer verifier was inspected, not executed; neither finite check tests the functional convergence.

## originality

PASS

Credit the explicit whole-path conditional Gaussian process across all diverging distance regimes, not the finite profile as a standalone new enumeration. Pitman's forest extension law and independent uniform endpoint choices already yield the entire finite binomial–multinomial law. A prior Resultary result gives its exact single-endpoint specialization, and Oleś gives prior joint two-endpoint asymptotics, a stronger overlap than a one-endpoint marginal. The inspected prior statements do not give the moving-length whole-path bridge/total transition.

## value

PASS

This is a natural whole-geodesic statistic, unlike a single endpoint or a fixed coordinate check. Its process law distinguishes fluctuations in the number of attachments from randomness in their placement: a free endpoint of the cumulative curve in the sublinear regime becomes pinned for nearly spanning paths. Resolving the intermediate macroscopic ratios as well gives a quantitative reference for conditioned tree models. It concerns direct edge incidence only and makes no claim about sizes or shapes of attached components.

The dated certificate retains the supplied scientific assessment, sources and limitations.
