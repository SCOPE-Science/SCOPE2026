# Scientific review: exact spectral covariance and sharp fixed-dissipation transport bound

## Correctness: PASS

The result is an exact two-particle statement. Subtracting the two stochastic equations cancels the common nonreciprocal drift, leaving stationary circular Brownian motion with diffusivity \(D_1+D_2\). Conditioning on both Brownian noise paths and integrating over independent Haar-uniform initial separation removes the otherwise nontrivial cross-terms between the common additive-force integral and either Brownian endpoint. The Fourier heat semigroup then gives the exact all-time covariance matrix; Parseval and elementary spectral limits prove the entropy identity, inverse power-spectrum statement, and long-time diffusivity. The strict decrease of \(\int_0^t(t-s)e^{-\lambda s}ds\) with \(\lambda\) establishes the finite-time and asymptotic sharp bounds and identifies all equality cases. An executable deterministic normalization/quadrature test and independent SDE simulation passed. Risks: the physical interpretation assumes unwrapped displacement observations, stationary initialization and full microscopic entropy production; finite-sample inversion is ill-conditioned.

## Originality: PASS, subject to stated residual risks

Zhang and Garcia-Millan (arXiv:2209.09721, full HTML, particularly Eqs. (1), (4), (8), (9)) previously established the underlying stationary chase-and-run model and entropy formula. Those are not newly asserted. Benois et al. (arXiv:2307.05408, full HTML, especially the two-body and tracer-diffusivity sections) previously studied diffusion enhancement in nonreciprocal mixtures; long-time diffusion is therefore not by itself an adequate novelty claim. The assessed single contribution is the exact **joint, all-time** unwrapped cross-covariance together with phase-blind spectral identification and the sharp time-uniform entropy-constrained waveform optimum in the actual two-particle model. The inspected text did not state this theorem or a dominating bound. Possible equivalence with general periodic-shear/Taylor-dispersion spectral techniques (e.g. arXiv:2101.05406, abstract inspected only) remains a meaningful literature risk, as do unindexed results. Searches and published-paper comparisons cannot prove global uniqueness.

## Mathematical value: PASS

The result connects a directly measurable two-particle motion statistic to the complete Fourier interaction *power* and to thermodynamic dissipation. It gives an exact, achievable design frontier for maximizing pair transport at a prescribed irreversible cost, simultaneously at every observation time, rather than a small-amplitude expansion or a merely numerical optimization. Both the inverse and optimization questions are natural in periodic nonreciprocal active-particle models. The result is restricted to an exactly solvable two-particle subfamily and does not purport to settle general mixtures, arbitrary interactions, or robust inversion under measurement noise.

## Limits and closest literature

The two original scientific dependencies are arXiv:2209.09721 (stationary uniform chase-and-run entropy) and arXiv:2307.05408 (related tracer diffusivity). General shear dispersion is a plausible mathematical reduction; arXiv:2101.05406 was available at abstract level only and must not be described as comprehensively excluded. Fourier phases are not identifiable and independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
