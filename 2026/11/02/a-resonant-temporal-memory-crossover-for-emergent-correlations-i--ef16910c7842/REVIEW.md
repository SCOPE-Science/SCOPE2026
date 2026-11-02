# Review: resonant temporal-memory crossover

## Correctness

**PASS.** Conditioning on the common switching history yields a bounded variance process with deterministic affine drift between stiffness switches. Its generator closes exactly on the stationary second moments and the two lagged functions. A forced second-order ODE and its Laplace transform give the three poles; strict derivative negativity follows from a positive Green kernel. The harmonic-mean equation is the sole pole crossing and the critical double-pole amplitude is nonzero. An independently propagated moment matrix and 162 standalone checker comparisons corroborate the formulas without replacing the proof. The proof does not cover independent-switching or interacting particles.

## Originality

**PASS, with explicit priority risk.** The base stationary Gaussian mixture and zero-lag cross-particle covariance are previously known in arXiv:2312.02570. The later optical-trap experiment arXiv:2508.07199 reports equal-time squared-position correlations and lagged **linear-position** hydrodynamic correlations, not the lagged squared-position observable here. The on/off specialization arXiv:2407.12213 lacks the interior positive-stiffness resonance. General Markov-modulated Ornstein–Uhlenbeck covariance operators are known, notably arXiv:2407.05866, but the exact strict-decay classification, harmonic-mean crossover, and double-pole positive amplitude are not stated there. Search and primary-text comparisons are detailed in AUDIT.json. Broader general-purpose stochastic-volatility machinery might streamline a derivation and remains a priority risk.

## Mathematical value

**PASS.** Stationary interparticle correlation alone cannot identify its persistence time. A measurable two-time energy observable has two distinct competing relaxation mechanisms and a unique, explicit resonance boundary at the harmonic mean of trap stiffnesses, valid for all positive symmetric switching rates and every finite particle number above one. The result distinguishes trap-switch memory from conditional-variance relaxation without mistaking an eigenvalue collision for a thermodynamic phase transition. It is a complete natural temporal classification under the stated assumptions rather than an arbitrary fixed-size computation.

## Restrictions

Symmetric switching, strict positive and distinct confinement strengths, independent driving noises, and full stationarity are essential here. Independent publication-priority review has not taken place. All numerical checks are finite consistency tests; the all-parameter conclusions rest on analytical arguments.

Self-review: passed. Independent audit: not yet performed.
