# Scientific review: Gaussian-edge leakage under common Poisson resets

## Correctness — PASS

The claim concerns stationary maxima, not temporal maxima, in the exact common-reset Ornstein–Uhlenbeck model. The conditional Gaussian representation gives independent standard normals multiplied by the common factor \(\sigma\sqrt{1-e^{-2\mu A}}\), where \(A\) is exponential with rate \(r\). The exact distribution of \(V_N=(\log N)e^{-2\mu A}\) is beta-weighted, and conditioning on it reduces both exceedance probabilities to one-dimensional integrals. Gaussian Mills ratios, the classical centered Gumbel limit, and an explicit integrable normal-tail envelope justify dominated convergence for all \(\beta>0\) and fixed \(x\in\mathbb R\). The separate uncorrected-edge calculation uses a vanishing single-Gaussian exceedance probability and yields the extra half-power. Conditional age selection follows from convergence of the normalized finite measures and continuity of \(-\log\) on the strictly positive limiting support.

The precise boundaries, stationarity, and normalizations are documented in `RESULT.md`. The standalone `verify.py` passed 94 exact-identity and numerical diagnostics. These finite diagnostics do not replace the proof; no finite-size relative error or uniformly changing-\(x\) statement is asserted.

## Originality — PASS (qualified best-knowledge)

The closest source is de Mauro–Majumdar–Schehr, arXiv:2606.31634, Sec. VI.1.1, Eqs. (115)–(136). That publication already derives the leading compact-support harmonic-trap maximum law, the conditional Gaussian mixture, the improved finite-size centering, and an order-of-magnitude boundary cutoff near \(1-1/(4\log N)\). These are explicitly prior results. The present theorem identifies the *resolved boundary-layer probability coefficient*, the limiting conditional reset-age mark, and the *sharp leakage law above the nominal edge*. These statements are not in the inspected relevant sections. The source's exact finite-\(N\) mixture is strong enough to serve as the starting point of the derivation, but does not itself give the asymptotic coefficients or the conditional selection law.

Biroli–Kulkarni–Majumdar–Schehr, arXiv:2312.02570, main-text EVS section and related appendix, derives a leading bounded-support maximum for a switching harmonic trap but does not resolve this Poisson-reset finite-size Gumbel smoothing. De Mauro–Biroli–Majumdar–Schehr, arXiv:2509.06658, studies arbitrary-renewal simultaneous resets for *free* Brownian particles, giving general conditional-independence principles and leading extreme statistics, rather than the finite harmonic compact-edge layer. Related mathematical-record claims on Gaussian pinning and random-sensor Gumbel windows have different observable objects and conditioning mechanisms.

Residual priority risk: a more general published theorem on endpoint mixtures of Gaussian maxima might subsume the displayed asymptotic integrals. Search absence does not establish uniqueness. No independent priority audit is claimed.

## Value — PASS

The motivating confinement paper quantitatively estimates the width of the finite-\(N\) edge layer and notes that its shape transition is obscured by finite-population effects. The present calculation resolves the rare-event probability **inside** that layer, identifies which unobserved reset ages produce those extremes, and computes the sharp leakage *beyond* the apparent limiting support. The extra half-power in the nominal-edge exceedance is a physically interpretable distinction between fluctuations of the shared reset clock and intrinsic Gaussian extremes. The result is not a routine restatement of the leading stationary edge density and is a potentially useful benchmark for finite-population resetting experiments.

## Scope and scientific limitations

The theorem is exact only for one-dimensional independent Ornstein–Uhlenbeck particles with perfect simultaneous Poisson resets to the origin and fixed positive physical parameters. It treats stationary spatial maxima, not first-passage times or temporal maxima. There are no finite-population error guarantees and no extension to non-Poisson renewal clocks. The claim's originality is a best-knowledge assessment of the inspected relevant literature and does not represent exhaustive independent certification.

Self-review: passed. Independent audit: not yet performed.
