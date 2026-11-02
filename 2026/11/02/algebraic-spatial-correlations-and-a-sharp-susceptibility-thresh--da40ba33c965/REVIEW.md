# Scientific review: spatial correlations under global Pareto renewal resetting

## Correctness

**PASS.** The exact coalescing-dual identity reduces the connected equal-time covariance to \((1-m^2)\mathbb E[H(T_n)]\). The stationary renewal-age survival \(H\) is evaluated with the correct length-bias normalization. The walk's Laplace exponent has jump rate one **per direction**. An exact beta-integral identity proves its negative fractional moment, while a Poisson jump-count bound makes the short-age cutoff correction superpolynomial. Summability and the weighted covariance identity give the sharp susceptibility and block-variance regimes. All hypotheses and boundaries are specified; the infinite-mean case is explicitly a local-weak limit, not a stationary-age statement. A standalone numerical verifier completed 71 checks, independently probing special-function normalizations and selected finite-distance correlations; none is used as an infinite proof.

## Originality

**PASS, qualified.** Direct examination of Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting* (arXiv:2602.15495v1), Sections II–III, shows its main one-dimensional results concern the spatial mean magnetization and its renewal-time distribution, not the zero-temperature two-point spatial tail, exact coefficient, summability boundary or block-average variance. Grange, *Voter model under stochastic resetting* (arXiv:2207.08590v6), considers independent sitewise Poisson resets, a different law at the level of every dual lineage. The earlier global Poisson Ising model and classical coalescing duality supply methods but not this Pareto spatial classification. Searches over aliases and parameter reductions did not establish a dominating source; they cannot prove exhaustive novelty. A possible more general renewal/coalescence Tauberian statement is a residual priority risk.

## Mathematical value

**PASS.** The resetting tail becomes a continuously variable, precisely normalized spatial correlation exponent, and an intrinsic summability transition occurs at \(\alpha=3/2\) despite the existence of an equilibrium renewal-age distribution for all \(\alpha>1\). The block magnetization is self-averaging but can have anomalous variance scaling or a logarithmic critical factor. These observables answer a natural spatial-structure question left open by magnetization-only descriptions and provide exact benchmarks for zero-temperature nonequilibrium coarsening.

## Scope and residual risks

The proof is annealed, infinite-volume, zero-temperature and uses one spatially iid environment recalled at every global reset. It does not establish finite-temperature behavior, quenched laws, or a field-response susceptibility. Broader theorems may cover parts of the reasoning; independent correctness and priority verification remain open.

Self-review: passed. Independent audit: not yet performed.
