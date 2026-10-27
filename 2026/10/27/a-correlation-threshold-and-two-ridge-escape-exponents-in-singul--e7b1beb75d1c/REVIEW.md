# Scientific review

## Correctness — PASS
The complete-square identity is exact for the displayed three-by-two data matrix. It provides a strict global attainment dichotomy. The ridge term is coercive, and compactness of strict sublevels below the asymptotic value proves attainment below the threshold. For nonattaining parameters, all minimizing sequences have bounded penalized coordinate and divergent unpenalized coordinate. Matched variational lower and constructive upper bounds then give the fourth-root and sixth-root escape rates and exact value constants. Every quantifier concerns global minimizers for fixed parameters and positive ridge weights approaching zero. The embedded checker recomputes independent symbolic identities and representative numerical minima; the proof, not those experiments, establishes the limits.

## Originality — PASS, subject to historical uncertainty
The closest primary literature includes Nguyen–Nguyen (2026), whose nonattainment criterion and example are respected, Beck–Ben-Tal (2006), and Xia–Wang–Yang (2018). Their inspected statements address attainment criteria and solution algorithms, not the singular small-ridge asymptotic exponent change at a column-correlation threshold. The present result is not a corollary of the stated sufficient finite-attainment condition: the two data regimes at and below the boundary have the same nullspace spectral diagnostic when \(\beta\ge1\). An older unindexed perturbation analysis might contain an equivalent special case; the 2006 full text was not inspected, and this remains a bibliographic risk. Broad generic semi-algebraic asymptotic theory does not by itself supply these precise constants and the two-sided attainment classification.

## Mathematical value — PASS
Rank-one singular regularization is the smallest model in which the penalty leaves a free direction. Correlated data columns create a nontrivial cancellation that shifts the conditioning of regularized solutions from one fourth-power law to one sixth-power law. The exact constants give numerical scales for choosing a ridge parameter, while the attainment threshold distinguishes problems for which vanishing ridge converges to finite solutions from those for which it provably cannot. The result applies to an entire continuous data family rather than a numerical curiosity.

## Closest literature and limitations
Nguyen–Nguyen, arXiv:2610.22880v1; Xia–Wang–Yang, arXiv:1810.11972; Beck–Ben-Tal, DOI 10.1137/050624418; Golub–Hansen–O'Leary, DOI 10.1137/S0895479897326432. The first two primary full texts were materially inspected. The latter two were inspected through accessible publication records/abstracts; inaccessible detailed historical equivalents remain possible. The theorem makes no assertion about unmodeled stochastic noise, floating-point algorithms, or arbitrary singular penalties.

Self-review: passed. Independent audit: not yet performed.
