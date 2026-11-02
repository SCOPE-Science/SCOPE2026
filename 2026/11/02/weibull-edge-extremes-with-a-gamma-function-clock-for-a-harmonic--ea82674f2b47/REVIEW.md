# Scientific assessment of the rare-edge hit theorem

## Correctness — PASS

The result concerns a stationary three-state piecewise-deterministic process, with strictly positive fixed rates and a near-edge target approached from inside. The stationary generator gives the exact run-entrance even moments. A product of two beta variables matches these moments and determines the entrance law by compact support. Gauss summation, with excess one, evaluates the finite negative moment to the claimed Gamma-function quotient. An independently sampled exponential run exceeds the target with the stated exact hazard. A uniform minorization for the embedded entrance chain, a vanishing upper bound for the conditional hazard in every later episode, and a blocking argument establish asymptotically exponential marked-run counts. Renewal conversion, uniformly integrable geometric run-count bounds, Wald's identity and the stationary initial-cycle estimate yield the time and mean assertions. The maximum law follows by the event identity with first hitting. The standalone reproducibility code verifies rational moment recurrences and finite Gamma identities, not the asymptotic theorem. Potentially delicate points—uniform mixing, rare-event clustering, stationary initial conditions, and stopped-cycle expectations—are addressed explicitly in the proof.

## Originality — PASS, qualified

The closest 2026 paper by Sun, Ye and Chen computes **position/velocity stationary laws** for the finite-tumble harmonic process, but the inspected conditional-distribution and appendix sections do not establish a near-hard-edge **temporal first-hit/maximum law**. Sun, Ye and Podgornik (2024) obtain stationary moments, and Basu and collaborators (2019) give the symmetric three-state stationary law. Guéneau, Majumdar and Schehr (2024) derive first-passage expressions for an **instantaneous two-state** run-and-tumble process; Grange and Yuan (2025) allow finite tumble time under **constant drift**, not harmonic confinement. None of these statements implies this specific two-rate rare-hit amplitude and Poisson/Weibull law without new anti-clustering and entrance-cycle analysis. Semantic searches of the published mathematical research index (including source aliases and threshold/extreme formulations), plus accessible historical claims, found no result with the same theorem or a known stronger covering assertion. This is best-knowledge originality, not a proof of global priority.

## Value — PASS

The hard propulsion boundary is a natural singular observable in active-matter harmonic confinement. The result changes a static boundary-accumulation calculation into a measurable long-trajectory rare-hit time and temporal maximum distribution, showing that the run-termination/trap ratio controls the Weibull shape while finite tumble duration affects the exact clock. The two-parameter Gamma quotient and a complete near-edge asymptotic distinguish it from a routine restatement of stationary density power laws. The measured quantity can benchmark simulation and experiments with pauses between propulsion bouts.

## Closest literature and limits

Sun–Ye–Chen arXiv:2610.24961v1 (2026-10-18); Sun–Ye–Podgornik arXiv:2409.00578; Basu et al. arXiv:1910.10083; Guéneau–Majumdar–Schehr arXiv:2409.16951; Grange–Yuan arXiv:2509.11308. Residual risk: a broader published extreme-value/rare-event theorem for uniformly mixing Markov renewal processes could imply the limit, though it would not directly supply this evaluated entrance moment. No analysis of varying rates, nonstationary joint limits or added Brownian diffusion is asserted. Bibliographic comparisons are not an independent publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
