# Review: A quantitative log-Beta law for harmonic run-and-tumble trapping times

## Correctness — PASS

The argument transforms the first entry into the first crossing of a nondecreasing exponential occupation functional. A stationary two-sided telegraph filter has the beta density by exact state-resolved zero-flux balance. Its finite-time truncation differs by an explicitly bounded past-memory term; this yields the all-real-time stochastic sandwich and quantile control without assuming temporal independence. Moment and atom statements follow by beta integrals and the exact zero-switch clock. The separately executable checker passed 22,808 finite assertions, including comparisons to the independently published hypergeometric exact mean; it does not stand in for the complete analytic proof. Boundaries, initial orientation, all parameters, the precise hitting target, and the limit order are explicit.

## Originality — PASS, qualified

The closest source, Guéneau–Majumdar–Schehr, arXiv:2409.16951v1, Section V.2 and Appendix B, determines the harmonic first-entry mean and provides a higher-moment recursion but does not present the log-beta first-entry fluctuation law or finite-distance stochastic quantile bounds in the material inspected. Their 2026 stationary beta law, arXiv:2602.08436v1, is for a position marginal, not the entrance time from outside support. The abstract and introduction of Bogachev–Ratanov, arXiv:1007.3139, concern a different telegraph occupation observable; the complete theorem and appendix sections were not inspected. Searches covering inverse exponential occupation, log-beta trapping times, and broader telegraph hitting-time theory yielded no explicit covering statement. A stronger result in general Markov additive-functional literature remains a genuine priority risk; novelty is not independently certified.

## Mathematical value — PASS

The 2024 first-passage problem motivates understanding random trapping times rather than their average alone. This result yields an entire new candidate universal limit law depending on switching-to-confinement ratio, its exact moment profile, a finite-distance quantile uncertainty of at most \(\mu^{-1}\log(1+C^{-1})\), and an exact fastest-entry atom. The stochastic comparison is a structural, non-asymptotic statement, not a routine evaluation of the known mean or a numerical special case.

## Scope and limitations

The theorem assumes a symmetric, athermal, two-sign Markov orientation begun at equilibrium; deterministic initial position above the positive stationary-support edge; and \(C\geq1\). It describes first entry into the compact support, not first passage to the origin; nonlinear trapping, biased switching and thermal diffusion are not covered. Comparisons with general telegraph exponential-functional theorems may need further independent priority checking. No external verification is claimed.

Self-review: passed. Independent audit: not yet performed.
