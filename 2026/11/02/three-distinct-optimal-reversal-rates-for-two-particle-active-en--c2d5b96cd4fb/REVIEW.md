# Scientific review

## Correctness — PASS

The second-moment Poisson hierarchy follows from the finite-state velocity jump generator and deterministic separation drift. For every positive reversal rate, absorption has finite moments by a uniform favorable-flip pattern bound. The exact conditional polynomial passes both differential equations and the incoming absorbing boundary. Integrating the polynomial over uniform separation/four velocities yields the displayed second moment and variance; polynomial differentiation plus Descartes' rule proves three unique optimizers and their strict order. `CHECKER.py` solves independent killed-generator lattice systems and verifies first/second moments at four parameter sets and three grid resolutions, all with first-order mesh convergence. Finite discretization alone is not an infinite proof; the algebraic ODE solution is.

## Originality — PASS on examined sources, with residual priority risk

The 2016 Slowman--Evans--Blythe Appendix B contains exact **mean** collision times for precisely the same two-particle model. These means are treated as prior art. Its Appendix B and the rest of the inspected primary text do not present encounter-time second moments, variances, the quartic minimizers, or their ordering. The 2015 Angelani--Di Leonardo--Paoluzzi source treats a single run-and-tumble particle with a reflecting/absorbing interval and external fields. The 2021 Mercado-Vásquez--Boyer source has a single active searcher and independent gated target, and calculates relative variance in a different generator and geometry. The 2018 Mallmin--Blythe--Evans paper focuses on generator spectral relaxation of two interacting *lattice* particles, not the specified absorbing collision-risk optimization; its full text was not inspected here. Targeted published-index searches, previously recorded scientific claims and web searches found no implication-level duplicate. Broader unpublished first-passage transform results remain a possible priority risk.

## Value — PASS

Collision-time uncertainty matters in active transport and reaction systems where minimizing average delay does not necessarily minimize run-to-run variability. The precise result quantifies a genuine three-way operational tradeoff; the variance-minimizing reversal rate exceeds the mean-time optimum, and the relative-variance optimum is higher still. The transition from high variability at low tumbling through sub-Poissonian relative variance and back to larger high-tumbling variability is nontrivial and scale independent. Unlike a mere higher-moment numerical table, it gives exact unique tuning laws and a qualitative reliability regime.

Self-review: passed. Independent audit: not yet performed.
