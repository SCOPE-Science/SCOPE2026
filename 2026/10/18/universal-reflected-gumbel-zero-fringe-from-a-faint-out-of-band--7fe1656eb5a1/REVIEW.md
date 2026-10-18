# Scientific assessment

## Correctness — PASS
For compactly supported nonzero integrable power spectra, the entire-function representation fixes the zero normalization and multiplicity. The derivation of the logarithmic Gaussian potential gives an explicit noncentral flux with nonnegative derivative. Endpoint Laplace concentration yields the exact all-frequency count. A demodulated, strongly mixing integer translation action establishes the almost-sure and \(L^1\) time-average limit; the covariance vanishes by the Riemann--Lebesgue lemma. Finally, the strictly monotone tone-to-noise ratio and endpoint convergence imply locally uniform reflected-Gumbel rescaling. The attached standalone 68-test checker corroborates local formulas and rates but is not the proof.

## Originality — PASS, qualified
The exact local first-intensity formula is already covered by Escudero--Koliander--Romero, arXiv:2609.18689, Theorem 1.1, and is credited as an input. Their Theorem 1.2 requires a positive-tail lower bound for slowly varying PSDs, excluding compact spectral support; its asymptotic question is different. Feldheim, arXiv:1105.3929, Theorem 1, covers centered stationary Gaussian analytic function zero laws, including the centered bandlimited case; it is not claimed as new. The compared full texts do not exhibit the out-of-band deterministic-tone zero-count identity combined with its **universal weak-tone reflected-Gumbel escape law**. The additional strong law at every fixed nonzero deterministic amplitude uses ergodicity of the demodulated noise rather than center-only stationarity. An equivalent specialization or unindexed spectral-edge calculation remains possible.

## Value — PASS
The spectral-hull law and the singular fringe address an observable discontinuity: an arbitrarily weak out-of-band tone adds a fixed number of expected zero crossings per unit time, but sends them to infinite analysis frequency, preserving all finite-frequency limiting statistics. The limit profile is independent of the detailed spectral shape and identifies an exact crossover scale. This provides a structural boundary case for spectrogram-zero detection and colored-noise limit theory, not an arbitrary numerical threshold.

## Limits and sources
This is a fixed compactly supported absolutely continuous PSD theorem. The reflected-Gumbel density concerns first intensity rather than point-process convergence. Main full texts compared: arXiv:2609.18689 (Theorems 1.1, 1.2 and their proof context), arXiv:1105.3929 (Theorem 1, centered stationary analytic-zero laws). Ancillary context: arXiv:2406.20003, arXiv:1708.00082. Independent historical-priority and correctness verification remain open.

Self-review: passed. Independent audit: not yet performed.
