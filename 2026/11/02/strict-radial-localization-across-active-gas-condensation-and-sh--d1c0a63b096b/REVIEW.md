# Scientific review

## Correctness

**PASS (self-review).** The finding is a statement about the explicit symmetric stationary mean-field density of a one-dimensional locally reset interacting run-and-tumble gas. For the dilute phase the source ODE gives the conserved tail coordinate \(R_m(g)=g-g^2/m\) and the exact inverse-mass quantile integral. The liquid density and fixed exterior gas mass give the piecewise quantile formula across condensation. Differentiating those formulas proves strict physical-radius order; subtracting them at the transition proves a quantile-independent one-sided slope jump. Subtracting the coexisting quantile formulas yields positive integrands. Translation of the exterior gas gives the exact strong-reset total-variation constant. The analytic inverse at small density gives the sharp weak-reset total-variation coefficient. All critical steps and boundaries, including \(m=4\), are written in the proof. The independent numerical profile inversion in `verify_quantile.py` passed 3,123 deterministic assertions, but these finite tests are not an infinite proof.

## Originality

**PASS (qualified best-knowledge).** Grange (arXiv:2610.26149, October 2026) already derives the exact gas and droplet stationary densities, phase boundaries, droplet mass, and nonmonotone width. The present result does not reclaim those formulas. Its additional statements are the full radial stochastic order through the phase change, the level-independent quantile kink, the strict concentration comparison of coexisting stationary phases, and the sharp weak/strong exponential total-variation laws. The primary source's Sections 2–4, Table 1, conclusion and relevant technical appendix were examined; these statements were not identified as assertions there. Comparison with local-resetting and run-and-tumble literature found different single-particle and boundary-conditioned problems, not a dominating law for this interacting two-phase stationary family. There remains priority risk from implicit implications of more general order theorems and from publication not located by the finite search.

## Value

**PASS.** A growing dense-droplet half-width does not order mass concentration. This theorem resolves the distinction for *every radial quantile*, not just a mean, and identifies a nonanalytic signature shared by every fixed quantile at condensation. The exact high-reset total-variation discrepancy isolates the mass of the non-exponential exterior gas. These outputs are useful for selecting spatial observables of dense active matter and for checking approximation errors. They concern normalized continuum stationary profiles rather than stochastic microscopic dynamics.

## Limitations and closest literature

The result depends on the particular piecewise-density-dependent speed law and the symmetric single-droplet stationary branch. It does not establish microscopic particle couplings, uniqueness of all weak steady states, or dynamical phase stability. The closest full-text source is Pascal Grange (2026), https://arxiv.org/html/2610.26149v2 , especially equations (22), (25), (31)–(44). Bressloff and Linn (2026), https://doi.org/10.1103/dcnh-bhwc , instead study a single run-and-tumble particle with a sticky boundary. Independent mathematical and literature-priority review has not been performed.

Self-review: passed. Independent audit: not yet performed.
