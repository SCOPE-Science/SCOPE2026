# Scientific review

## Correctness (PASS)

The process is explicitly defined as a symmetric half-line walk time-changed by independent blockwise rates. The killed-walk sine spectral kernel and independence give an exact epoch survival integral. Integration of the rate-tail survival proves the explicit \(\sqrt{s}[\log(1/s)]^\beta\) Laplace asymptotic; the spectral scaling and Potter-dominated convergence then give the full survival constant and correct physical-time normalization. Moment and product-Pareto claims follow from convergent tail integrals and the exact Gamma tail. The accompanying Python verifier checks finite instances and numerical asymptotics, but these tests are not offered as a substitute for the proof.

## Originality (PASS, qualified best-knowledge)

The closest primary antecedent is Levit and Reuveni, arXiv:2609.26925: the half-line method and pure-power rate-tail exponent are already established. Its pure-power small-Laplace asymptotic is not sufficient to decide whether the mean is finite at the critical exponent. The present claim identifies the logarithmic boundary and exhibits the exact number of independent multiplicative Pareto factors that crosses it. Arutkin and Reuveni, arXiv:2302.07041, provide the broader rate-modulated walk framework. Result-level semantic comparisons and accessible preceding research claims did not identify coverage of this statement. A claim of definitive world-first priority is not made; unreviewed or inaccessible mathematical physics literature on slowly varying random clocks remains a residual risk.

## Value (PASS)

Mean first passage at a marginal heavy-tail exponent is a physically meaningful transition: three independent multiplicative rate channels convert an infinite expected search time into a finite one without changing the algebraic Pareto exponent. The result gives a precise asymptotic tail constant, all positive-moment thresholds, and a mechanism for the transition rather than a routine finite numerical fact.

## Limitations

Only iid blockwise environments and symmetric half-line walks are covered; no statement about nonidentically distributed, correlated or jump-resampled rates, and no uniformity for growing start or number of factors. Numerical comparisons support finite cases but do not prove any asymptotic. Earlier general regularly varying random-clock results may imply portions of the theorem; publication priority requires independent review.

Self-review: passed. Independent audit: not yet performed.
