# Scientific review

## Correctness — PASS

The claim concerns one fixed positive reset rate and a single star-graph family. The finite generator is derived directly from vertex update clocks; its uniform limit is a two-state piecewise-deterministic process. An explicit zero-flux stationary density has been checked against both forward equations. A polynomial-moment recursion with strictly nonzero denominators proves uniqueness of all weak stationary limits, avoiding an unjustified assumption that finite-graph stationary convergence follows automatically from generator convergence. Finite-graph pairwise spin equations independently establish the stated exact covariance and limiting variance; the degree-weighted support gap is a deterministic consequence of the full joint law. The packaged rational checker reproduces nine full-labeled versus symmetry-lumped stationary distributions and 212 further identities. It does not claim to certify the infinite limit by enumeration.

## Originality — PASS (best-knowledge, qualified)

Pymar–Rivera 2021 (arXiv:2112.01478) explicitly exclude stars from their sufficient Gaussian regime, and analyze degree-weighted rather than unweighted stationary leaf density. Caligiuri–Galla 2023 (arXiv:2305.19096) give a general two-state PDMP density formula that subsumes the limiting differential-equation integration once its generator is identified. **That generic formula is not original**. The claim instead includes a microscopic endogenous-hub star model, an all-positive-noise proof of convergence of its finite stationary laws, explicit hub-conditional coupling, nonvanishing leaf variance, separated weighted-density support, and exact finite-graph covariances. No inspected source or matched research record establishes this combined star-specific theorem. Risks remain from general Markov-process theory and possibly unindexed exact star calculations. Absolute literature priority and independent mathematical validation are not asserted.

## Value — PASS

The result addresses a natural conspicuous omission in current noisy-voter density-limit results: stars have a hub whose stationary random-walk mass is one half, so finite microscopic noise at the hub need not average out as the number of leaves grows. The non-self-averaging scaled Beta law, strictly positive gap in the original degree-weighted density, and exact finite-size covariance together isolate an enduring failure of Gaussian self-averaging at fixed noise. These are structural, quantitative statements rather than incidental numerical slices.

## Limits and literature

The proof is restricted to continuous-time, unbiased, independent per-vertex noise at fixed positive rate on unweighted stars. The law's PDMP density follows a pre-existing general two-state formula after an independently justified microscopic limit. Primary material inspected includes full-text Sections 1 and main results of arXiv:2112.01478, Sections III.3.2–III.3.3 and V of arXiv:2305.19096, and the model/results sections of arXiv:1810.05643. Formal independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
