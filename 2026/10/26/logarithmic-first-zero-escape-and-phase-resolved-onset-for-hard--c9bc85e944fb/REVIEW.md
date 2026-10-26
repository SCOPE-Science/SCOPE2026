# Scientific review: truncated-Gaussian first-zero onset

## Correctness
**PASS (self-review).** The exact Gaussian-tail decomposition is checked against its error-function representation. The rescaled Laplace integral has an absolute remainder at most \(1/(4L^2)\) in the bracket, uniformly for all real frequencies; one differentiated estimate controls compact \(C^1\) convergence. A global full-Gaussian-versus-tail comparison excludes earlier zeros, while one full oscillation of the endpoint term guarantees a negative value within the claimed boundary layer. The elementary zero-geometry argument establishes the sole exceptional phase. Fixed-cutoff integration by parts establishes one simple zero in every sufficiently distant sine lobe. High-precision checks support, but do not substitute for, these arguments.

## Originality
**PASS with historical-access risk (self-review).** The closest full text is Lonke (2021), whose sector positivity already supplies \(|\xi|\le 2L\) as a zero-free band and whose error-function bounds inform part of the lower-tail comparison. Neither its proposition nor its proof constructs a first zero beyond that band or a logarithmic/phase-resolved onset law. Csordas (2013) treats entire Fourier-transform zeros through positive definite kernels, not this moving truncation limit. NIST DLMF Section 7.13 tabulates complex zeros of \(\operatorname{erf}\) and \(\operatorname{erfc}\), not zeros of \(\operatorname{Re}\operatorname{erf}(L+i\xi/2)\). Earlier partial material by Ross, Fiddy and Nieto-Vesperinas illustrates finite-Gaussian-transform zero geometry, and Tallis establishes truncated-normal moment transforms; their full texts were not available, so potentially unindexed equivalent asymptotics remain a substantive priority risk. No independence or exhaustive literature certification is asserted.

## Value
**PASS (self-review).** Hard truncation is natural in Fourier windowing and compact-support probability kernels. The theorem determines a singular first-real-zero threshold on a logarithmically thin frequency scale, gives its complete leading oscillatory profile, and isolates an exceptional phase tangency. This distinguishes mere zero-free-sector bounds from the actual frequency at which cancellation begins. The result is an analytic asymptotic classification, not merely a numerical table or a routine finite-mode extrapolation.

## Scope and outstanding risks
The first-zero result requires \(L\to\infty\); the phase-selected convergence excludes one explicitly characterized phase. No full classification of low real or complex zeros at fixed cutoff is claimed. The 1980 finite-Gaussian-transform treatment and the 1961 truncated-normal paper were accessible only in part, limiting historical priority assessment. The conclusions rely on a finite Gaussian tail and do not transfer automatically to smooth apodization or other window profiles.

Self-review: passed. Independent audit: not yet performed.
