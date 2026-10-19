# Scientific review

## Correctness

PASS. The renewal-age calculation gives the exact Lomax equilibrium age; Brownian scaling gives an exact bivariate Gaussian scale-mixture representation. Conditioning on the Gaussian coordinates and using domination by finite Gaussian moments validates every tail limit. The conditional Gaussian regression \(H\mid Z=z\) has mean \(\sqrt3 z/2\) and variance \(1/4\), establishing the reverse-sign integral. Strict monotone likelihood ratio, Gaussian quadrant probability and one integration-by-parts identity prove all endpoint and exact special-value assertions. The gamma age moment integral gives a necessary **and** sufficient mixed-moment frontier. Quantile normalization proves joint extreme co-exceedance. `checks.py` supplies finite corroborating calculations; the proof does not appeal to simulation.

## Originality

PASS at the level of the explicitly conditional joint-kinematic claim, with material residual priority risk. Singh's 2020 full preprint gives the Poisson-reset joint law, not the Lomax renewal conditional reversal fraction. Bodrova–Chechkin–Sokolov's 2018 full preprint studies power-law renewal position marginals for scaled Brownian motion; its universal Gaussian position marginal coverage **does** subsume the exponent of the present displacement marginal, which is therefore expressly treated as known context. Montero–Palassini–Masoliver's full 2023 preprint describes the joint Gaussian inertial-propagator model and specializes reset calculations to Poisson interarrivals. Published research-record searches for integrated Brownian heavy-tail reset, conditional velocity reversal, and co-extremes did not return an equivalent statement. The Gaussian scale-mixture representation plus standard multivariate product-tail theory may render parts a specialization of general probability theory; this limitation is acknowledged rather than conflated with a proof of novelty.

## Scientific value

PASS. A physically relevant question not addressed by position marginals is whether extremely displaced randomly accelerating searchers still move toward their origin. The theorem determines the asymptotic answer for every renewal-tail exponent, with a nontrivial exact \(6.6987\%\) fraction at a natural exponent and a strict monotone dependence on tail heaviness. Its joint-tail dependence coefficient and anisotropic mixed-moment frontier quantify information lost when position and velocity are analyzed separately. The mathematical value is a motivated complete classification for one model, not the mere reuse of a marginal tail exponent.

## Closest sources and limitations

Full texts examined: arXiv:2007.05576v1, arXiv:1812.05667v2, arXiv:2312.13968v1. Closest published-record hits about stationary renewal age/residual power correlations address different observables. General multivariate regular-variation reductions remain a priority risk; no independent literature audit is claimed. All scientific scope restrictions are in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
