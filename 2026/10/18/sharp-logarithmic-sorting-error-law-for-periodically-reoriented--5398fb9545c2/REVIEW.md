# Scientific review

## Correctness — PASS

The symmetric mobility has Schur complement \(\kappa I_2>0\). An explicit constant triangular square root establishes the exact orthogonal noise decomposition without changing the Stratonovich law. The angular coupling is the differential of \(R_\phi u\), and the independent two-dimensional rotationally mixed Brownian integral has path-conditionally deterministic covariance. This proves the one-cycle law, independence across periodic reset intervals, and the complete cumulant function. Strict convexity and a direct exponential-tilting argument establish the large-deviation rate. The wrapped normal heat kernel is smooth and positive; nondegenerate Laplace asymptotics at zero establish the exact logarithmic coefficient and constant. Finite Bessel/quadrature and original-SDE simulation checks passed; the analytical proof establishes the infinite limits.

## Originality — PASS, with residual risks

Cleuren and Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1, Section (ii) and appendix, first publicly posted 2026-03-19, derive the model and mean current but do not provide the characteristic law, sign-error exponent, or weak-noise logarithmic law. Chaki, Olsen, and Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2, Sections II and V, have independent orientation and translational Brownian noises, Poissonian angle resetting, and late-time Gaussian diffusion; their result does not entail the correlated-noise sign-error rate. Named-alias and reduction searches against published mathematical research records returned no covering claim: the closest recorded descriptions were about unrelated chiral symbol dynamics and stochastic covariance systems. The relevant complete source sections were read, not inferred from snippets. The general Cramér/Laplace tools are not themselves new; implicit specialized coverage by unlocated literature remains possible.

## Value — PASS

The parent physical paper explicitly proposes sorting by orientation resets and quantifies only average motion. Sorting reliability is controlled by wrong-sign probabilities, not only drift. The exact full one-cycle distribution determines those finite-exposure probabilities, and the asymptotic rate provides a usable device-design performance measure. Its \(\tfrac14\log(1/\epsilon)\) singularity is quantitatively surprising, reflects the quadratic tangency of the angular endpoint at the sorting boundary, and is not a simple substitution into the known mean current. The isotropic Schur complement is a motivated residual-translation-noise class; it is not claimed to represent all colloids.

## Closest literature and limitations

The statements are restricted to a positive isotropic residual mobility, perfect deterministic orientation resetting, and an iterated cycle-number/weak-residual-noise limit. A fully anisotropic Schur complement or imperfect-reset process may exhibit different rates. Some abstract general theory may implicitly include the exact model, but no decisive covering source was identified in the examined material.

Self-review: passed. Independent audit: not yet performed.
