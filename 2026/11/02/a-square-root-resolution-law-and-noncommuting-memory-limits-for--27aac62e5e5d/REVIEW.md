# Scientific review: noisy rotational-diffusion time reversal

## Correctness — PASS

The theorem is conditional on an exactly specified stationary planar OU diffusion, independent Gaussian observation noise, a fixed observation spacing, and ordinary stationary path-order reversal. The OU covariance is explicit, and its Fourier decomposition gives two scalar spectral densities. Since their eigenvectors are common and fixed, the Gaussian trace formula reduces to the stated scalar frequency integral. Geometric covariance decay and a strictly positive spectral floor justify the block-Toeplitz to circulant limit. The Poisson-kernel convolution evaluates the integral in closed form. A Puiseux expansion at fixed positive observation-noise variance yields the square-root coefficient. At every fixed observation-block length the finite covariance remains strictly positive definite at zero sampling interval, and Gaussian relative entropy is quadratic in the forward/reverse covariance difference. These observations prove the noncommuting limits. A standalone numerical program independently tests the spectral integral and finite-block covariance formula. Limits and caveats appear in RESULT.md.

## Originality — PASS, qualified

The central challenge is not the general definition of pathwise Gaussian entropy production, the familiar stationary OU current, or the fact that noisy observations are non-Markovian. Those are prior results. Sagawa (arXiv:2604.07867, Sec. VI) develops general Kalman-innovation Gaussian path-reversal formulas; its generality overlaps the first step of the derivation, but the inspected Gaussian section does not state the present rotational closed expression, the fixed-positive-localization-error square-root temporal-resolution law, or the mutually singular orders of history and temporal resolution. Gingrich et al. (arXiv:2606.23619, Secs. II–IV) establish noise-induced memory, entropy-production bounds, and finite-resolution effects, but their inspected analyses do not furnish this special Gaussian full-path asymptotic with the exact coefficient. Standard nonreversible OU work provides the continuous-time benchmark. The novelty claim is limited to the explicit coefficient and exact resolution/memory interplay, not the general background machinery. A broader published Gaussian spectral-entropy result could still imply the specialization, and publication-priority assessment is not independently certified.

## Value — PASS

The source literature identifies a practically motivated inferential conflict: measurement noise can make more frequent short-history observations look *less* irreversible, even though the physical trajectory has unchanged dissipation. The new theorem resolves this conflict sharply in the smallest rotational Gaussian model by separating full-history inference from every fixed observation length. Its nonanalytic \(h^{1/2}\) coefficient quantifies the loss from fixed independent localization noise, and its zero versus positive iterated limits show why a finite-order proxy cannot simply extrapolate to the full time-series answer. The precise coefficient, as distinct from mere existence of memory, can guide sampling and model-checking arguments. The contribution does not claim a general data-analysis algorithm or non-Gaussian extension.

## Closest literature and risks

- T. Sagawa, *Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective*, arXiv:2604.07867 (2026). The Gaussian innovation and reversed-path KL framework is credited as prior work.
- T. R. Gingrich et al., *Thermodynamic inference from noisy single-molecule time series*, arXiv:2606.23619 (2026). Noise-induced non-Markovianity and the general temporal/spatial resolution trade-off are credited as prior work.
- D. da Costa and G. A. Pavliotis, *The entropy production of stationary diffusions*, arXiv:2212.05125; C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes*, arXiv:1807.00694. These inform the established continuous-time OU calculation.

Limits: isotropic planar linear Gaussian stationary dynamics; independent instant-read Gaussian localization errors; no finite-window statistical efficiency theorem. Related general state-space representations may yield parts of the formulas upon specialization. No independent audit or human literature-priority decision is represented.

Self-review: passed. Independent audit: not yet performed.
