# Scientific review: two-target mean-first-passage tomography

## Correctness — PASS

The renewal derivation establishes the exact MFPT from a fixed known initial position, with independently resampled sources and no moment assumptions. The transform \(\Phi_c(s)\) is positive for every \(s>0\). Its values on a set with an interior accumulation point uniquely fix the folded measure by analytic uniqueness; two folded measures uniquely fix the original finite source by antisymmetry under two reflections and the impossibility of a nonzero finite translation-invariant signed measure. The constructive Fourier formulas have the correct determinant and continuous extension at resonances. Arbitrary finite measurement collections fail injectivity by a normalized linear-nullspace construction, and oscillatory densities establish a nonvanishing total-variation separation with vanishing bounded-rate data difference. A standalone numerical reproduction file passed 95 independent deterministic and statistical assertions; the written proof, not those checks, supports the universal quantifiers.

## Originality — PASS, with residual risk

Méndez–Flaquer-Galmés–Campos (arXiv:2401.01125) already provide the forward first-passage transform, which is credited explicitly. Toledo-Marín–Boyer (arXiv:2206.14387) analyze forward reset-source first passage and information; Julián-Salgado–Dagdug–Boyer (arXiv:2311.11897) work with multiple reset points; Abundo (arXiv:2410.16889) studies inverse first passage under different sampling specifications. Their inspected full-text sections do not formulate the exact two-target arbitrary-measure recovery and its finite-sampling/instability limits. Published-record searches for the source, two-target reconstruction, reflection equivalences and inversion were compared at the scientific implication level. Closest subject-related records concern general restart variance or stationary ring-membrane current, not this theorem. A broad published two-centered measure-tomography or inverse-source theorem could imply the result; publication priority is not certified.

## Value — PASS

An unknown stochastic-reset source is a natural physical parameter; first-passage observations are widely accessible response quantities. The result gives an exact minimum number of target sites for ideal response-curve identifiability without artificial moment/density priors, and proves a finite-measurement impossibility and instability boundary rather than implying a misleading estimator. These facts make the precise object and measurements mathematically motivated even without a finite-noise reconstruction theorem.

## Limits and relationship to the literature

Known diffusivity and starting point, two distinct absorbing points, independent draws at every reset, exact population MFPTs, and each site's set of rates having an interior positive accumulation point are essential stated assumptions. The established Brownian renewal formula and harmonic/Fourier-Laplace uniqueness are not credited as novel. No independent audit or publication-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
