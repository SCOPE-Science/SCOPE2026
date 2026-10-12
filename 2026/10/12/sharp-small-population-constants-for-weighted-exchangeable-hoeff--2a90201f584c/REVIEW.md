# Scientific assessment

## Correctness — PASS
The exact variational reduction is Theorem 1/Remark 1 of Lee and Kim (arXiv:2608.04900), read in full. The sharp Bernoulli log-MGF coefficient is the Kearns--Saul inequality (Schlemm, arXiv:1405.4496). The remaining cases are covered by the detailed hypergeometric polynomial and tilted-variance bounds in RESULT.md; all normalization factors and endpoint cases were checked. The symbolic checker passed on the packaged source. The higher-dimensional reduction is cited rather than independently reproved here, and no finite calculation is used as an infinite proof.

## Originality — PASS, with priority risk
The lead 2026 article states the variational characterization for every population size and global nonsharp bounds, but no values for sizes 3, 4, 5, or 6. Four exact evaluations with nonzero-tilt versus variance-extremizer distinction are not implied by the numerical upper/lower envelopes. Kearns--Saul supplies the one-point cases, but not the two- and three-point hypergeometric cases. Searches of related published mathematical records and concentration literature did not identify an equivalent evaluation. An unindexed earlier evaluation remains possible; the original formula is expressly credited and not a new claim.

## Value — PASS
The optimal inflation coefficient is a natural invariant explicitly left unsolved in a recent foundational inequality. Four consecutive exact values resolve its first nontrivial sizes, exhibit distinct odd/even mechanisms, and replace loose sufficient constants in finite-population concentration. The tilted-variance positivity identities supply reusable analytic controls. No extrapolation to arbitrary population sizes is claimed.

## Closest literature and limitations
Lee and Kim (2026), arXiv:2608.04900, Remark 1 and Proposition 2 (full HTML examined); Schlemm (2014), arXiv:1405.4496 (Bernoulli sharp coefficient); Barber (2024), arXiv:2404.06457 (weaker exchangeable concentration). Limitations and residual priority risk are explained in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
