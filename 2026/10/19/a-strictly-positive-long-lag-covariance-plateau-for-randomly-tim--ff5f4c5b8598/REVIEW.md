# Self-review

**Correctness — PASS.** The periodic orbit is an affine contraction. Integrating its two light/dark phases yields an exact mean formula; strict decrease follows from the increasing function \(h\coth(kh)\). For every fixed lag, bounded uniformly Lipschitz rescaled trajectories permit Fejér approximation and Fourier dephasing against any absolutely continuous period law. Parseval and dominated convergence remove all nonzero lag harmonics. The resulting positive plateau follows from the nondegenerate distribution of a strictly monotone quantity. The included standalone checker passed 78 supporting computations; those are not proofs of infinite limits.

**Originality — PASS, with acknowledged broader-method risk.** Andreu-Vilarroig et al. (2026), DOI 10.1007/s11538-026-01609-3, derive one-time mean and variance limits but not this lag covariance law or strict positive plateau. Relevant random-frequency, photobioreactor, and persistent-covariance searches found no exact same-model result. The mechanism belongs to established harmonic analysis/quenched-mixture theory, and a more general prior theorem may encompass it.

**Mathematical value — PASS.** The theorem distinguishes phase dephasing from genuinely vanishing long-lag fluctuation memory; the strictly decreasing biochemical cycle mean forces the difference throughout the physical parameter range. This answers a motivated two-time statistical question absent from the paper's single-time analysis, without claiming empirical reactor optimization.

**Limitations.** The random period is drawn once, not independently regenerated between cycles; the law must be absolutely continuous; the scalar reduction is used; the \(t\to\infty\) limit precedes the large-lag limit. An independent examination of the scientific result is not available.

Self-review: passed. Independent audit: not yet performed.
