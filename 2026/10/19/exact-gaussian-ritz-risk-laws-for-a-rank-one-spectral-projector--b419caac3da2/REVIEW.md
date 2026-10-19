# Review of exact Gaussian Ritz risk laws for a rank-one spectral projector

## Correctness — PASS

The square Gaussian pencil reduces, using a rotationally invariant kernel line, to a complex ratio of two independent standard Gaussian variables. This yields the complex-Cauchy density and its exact moment threshold. A separate independent gamma-sum representation yields the beta transformation of the refined Hermitian Rayleigh quotient. Integrating the beta density proves the distribution, expectation, fixed-dimension logarithmic asymptotic and the high-dimensional exponential limit. The median proves necessity in the convergence criterion. The proof explicitly covers every integer dimension \(n\ge m+1\ge3\), every trial subspace with \(0<\theta<\pi/2\), and the exact circular complex-Gaussian model. The included standalone checker verifies 432 direct generalized-eigenvector identities, CDF and mean, and finite/asymptotic samples. Such samples are corroboration, not infinite proofs.

## Originality — PASS with residual bibliographic uncertainty

The motivating primary source, N. Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization* (arXiv:2604.01037v3, 2026), gives high-probability eigenpair/refinement estimates and a numerical sharp-tail study, not the projector-family marginal distributions, exact mean, logarithmic expected-risk penalty or dimension--angle consistency classification. Its full relevant method, theorem, probability and appendix passages were compared. Nakatsukasa--Tropp (arXiv:2111.00113v2, Sections 6.3--6.8) addresses a generally oversampled randomized eigensolver and its generic accuracy bounds, not this square-pencil distribution. Searches of published mathematical finding records for Gaussian Ritz ratios, projectors, beta laws, moment thresholds, and dimensional consistency found no statement implying the theorem. Generic complex-Gaussian ratio and beta--gamma identities are acknowledged as established ingredients, not asserted novel. As with any literature comparison, incompletely indexed or inaccessible sources might contain a closely related identity.

## Value — PASS

Refinement makes the randomized Ritz value nonnegative and bounded, but the theorem shows a sharp divergence between typical quadratic accuracy and its mean: a logarithmic loss relative to ordinary Rayleigh--Ritz. The exact phase condition \((m-1)\sin^2\theta\to0\) determines when increasing the trial dimension improves rather than destroys consistency of a single square-sketch refinement. This identifies a mathematically motivated risk diagnostic directly linked to the guarantees and heavy-tail caveat of a new randomized eigenvalue-extraction method; it is not just a renamed standard beta law.

## Limitations and closest literature

The projected rank-one-complement model is sharply specified, and only complex circular Gaussian sketches, one square sketch, exact arithmetic, and Rayleigh-quotient refinement are analyzed. No claim is made for general Hermitian spectra, stopping rules, numerical sorting, or multiple independent sketches. The main source already discusses sharp Gaussian-conditioning tails; the contribution here is the exact **refined output** risk law and its distinct joint limit, which need not be a consequence of its high-probability bounds. Neither bibliographic comparison nor this self-contained proof constitutes independent external validation.

Self-review: passed. Independent audit: not yet performed.
