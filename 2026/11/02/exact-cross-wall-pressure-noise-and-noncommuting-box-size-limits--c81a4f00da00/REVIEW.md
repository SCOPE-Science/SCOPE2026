# Scientific assessment: two-wall force fluctuations

## Correctness — PASS

The claim fixes the hard-wall process, outward-orientation pinning convention, flip-rate normalization, force scale, initial stationary law, and the exact order of limits. The stationary law follows from equal bulk densities and the wall flux balance, and is normalized. A centered Poisson equation for the *sum* wall-occupation observable has an explicit bounded quadratic solution satisfying both boundary equations and the stationary centering. Its bracket identity gives the full variance rate, not merely a simulation estimate. A separate exact position-displacement identity reduces the *difference* wall occupation to the integrated autonomous telegraph spin plus a bounded endpoint. Reflection symmetry forces the mixed sum/difference covariance to vanish. These arguments yield the exact covariance matrix for every strictly positive finite parameter choice. In the wide-box reversed limit, the bound on the second moment of finite-time pinned occupation rigorously gives zero. The attached standard-library verifier independently resolves finite-state approximants using rational arithmetic and passed 117 checks; its finite approximants are not used as an infinite-system proof.

## Originality — PASS (qualified best-knowledge)

The nearest first-public motivating work, Li–Eichhorn–Dabelow (arXiv:2610.01287v1, October 1, 2026), treats a finite-box active ideal-gas law and mean wall pressure. Its abstract was read, but the complete PDF and supplement were not accessible in this review. Angelani's full accessible 2017/2022 hard-wall analysis studies the same generator, one-point time-dependent wall populations and mean pressure; it was inspected at its model, wall-balance, stationary-pressure, modified-wall-rate and escape sections. The 2023 general-boundary RTP analysis concerns boundary laws and exit times; the 2024 Mukherjee–Le Doussal–Smith full text treats additive occupation statistics in non-sticky, unbounded geometry. The present statement is not a restatement of their presented mean pressure, scalar local-time, or exit-time formulas: it gives the *joint* two-wall asymptotic force covariance, an exact strict anticorrelation interval, and two noncommuting stationary-box limits. Publicly retrievable comparable research records and accessible prior claims were screened by scientific implication, including related sticky-run-and-tumble resetting and active ideal-gas shape results. There is a residual risk of prior coverage in older general occupation-fluctuation literature or inaccessible supplementary material. No absence-of-search-result is taken as proof of priority.

## Value — PASS

The same steady ideal-gas pressure and wall atom probabilities do not by themselves quantify the variability of accumulated forces applied simultaneously at two confining surfaces. The exact finite-width matrix gives a physically meaningful transport-noise observable, a strictly negative cross-wall correlation, a width-independent fluctuation of net momentum transfer, and a singular thermodynamic/observation-order boundary. Such joint statistics are directly relevant to pressure measurement over long time windows, stress transmission, and interpreting stationary pressure in dilute wide boxes. The result is specific and structural rather than an arbitrary parameter sample or a small numerical improvement.

## Closest literature and limitations

- L. Angelani, *Confined run-and-tumble swimmers in one dimension*, https://arxiv.org/abs/2206.03123 : same sticky-wall process and steady wall pressure, but no inspected formula for the long-time two-wall integrated-force covariance.
- S. Li, R. Eichhorn, L. Dabelow, *Ideal gas of active particles in a box*, https://arxiv.org/abs/2610.01287 : active ideal-gas pressure and same one-dimensional model; complete 2026 PDF/supplement inaccessible for decisive full-text comparison.
- S. Mukherjee, P. Le Doussal, N. R. Smith, *Large deviations in statistics of the local time and occupation time for a run and tumble particle*, https://arxiv.org/abs/2405.07032 : general local/occupation-time fluctuation methods, but not the reflecting sticky two-wall force matrix.
- P. C. Bressloff, S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, https://doi.org/10.1103/dcnh-bhwc : a resetting half-line sticky model, materially different from two stationary walls without resetting.

No independent mathematical or publication-priority audit has been conducted. The theorem excludes particle interactions, translational thermal diffusion and heterogeneous boundary detachment rates.

Self-review: passed. Independent audit: not yet performed.
