# Scientific review

## Correctness — PASS

The normalization uses Brownian generator \(D\partial_{xx}\), initial distance \(d>0\), and \(t_0=d^2/(4D)\). The reciprocal hitting-time variable is exactly Gamma with shape \(1/2\) and rate one. The single-attempt success is \(\mathbb E\exp[-a(\log N)^2/Y_{(N)}]\). The subcritical constant follows from the Gamma maximum's centered Gumbel law and a uniform exponential-moment bound valid precisely for \(0<a<1\). The exact tilted-Gamma moment-generating function gives a normal saddle with variance \(\sqrt a/2\), correctly locating the \(a=1\) prefactor and the \(a_N=1+z/\sqrt{\log N}\) crossover. A direct renewal transform gives both the mean and asymptotic exponential completion law. Two independent finite-N quadratures and asymptotic diagnostics in `verify.py` passed 101 assertions. Such tests are diagnostics; the limit claims use the written analytic proof.

## Originality — PASS (qualified best-knowledge)

Biroli, Majumdar and Schehr, *Physical Review E* **107** (2023), 064141, give the same shared-clock finite-N mean renewal integral; that identity is explicitly not claimed as new. Their Sections III–V and Appendix B focus on finite-N optimization and the small-reset-rate expansion, not a joint regime with population and rate both diverging. Vatash, Goldfarb, Rudyak and Roichman, arXiv:2609.23542 (2026), analyze rank-dependent optimal resetting and discuss globally resetting searchers, but their inspected asymptotic result concerns rank fractions for the independently resetting reference. Linn and Lawley (2023) give the general frequent-resetting renewal mechanism, not the explicit Gamma-versus-Gumbel phase transition or critical Gaussian factor for a shared population reset. The assessed mathematical addition is the three-regime rare-success probability, its crossover and consequent mean-time scaling. A broad search and accessible prior-claim comparison did not identify a statement implying this full classification; absence of a search hit is not proof of novelty.

Residual risk: general extreme-value tilting or rare-event renewal machinery could subsume parts of the proof in a different formulation. The complete review of every possible prior source and independent priority audit remains outstanding.

## Value — PASS

The shared clock induces a fundamentally different common-rare-excursion mechanism from independent-clock resetting: below the threshold the successful excursion is organized by a Gumbel extreme, above it by a Gaussian saddle, and at the boundary both mechanisms compete on the natural \((\log N)^{-1/2}\) parameter scale. This determines a nontrivial, explicit change of polynomial mean-search-time exponent and the exact critical amplitude. The result is relevant to synchronized batch-restart experiments and noninteracting baselines for collective first passage, not merely a formula substitution or a small numerical improvement.

## Relationship, limits, and audit status

The proof covers independent Brownian paths between resets, a single shared Poisson clock, fixed positive \(a\) or fixed critical parameter \(z\), and one earliest absorption. It does not establish uniform critical errors, later arrival ranks, interacting-searcher effects, or independence from all other literature. The verified standalone program checks finite numerical identities; no numerical experiment certifies infinite-population convergence.

Self-review: passed. Independent audit: not yet performed.
