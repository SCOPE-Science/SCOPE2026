# Scientific review: spectral-whitening robustness radius

## Correctness
**PASS.** Positivity for all perturbations in the claimed closed ball follows from the strict inequality \(t_*<\lambda_1\). The condition-number statement is converted to inequalities for every orthonormal pair; Frobenius duality is exact for the symmetric rank-two test matrix. The two-dimensional compression calculation is a convex quadratic and the min-max principle identifies the maximum using the two largest eigenvalues of \(A^{-1}\). An explicit rank-two commuting perturbation attains the endpoint, and scaling it establishes failure at every larger radius. The algebraic two-dimensional witness and 8,472 reproducible finite checks agree with the proof. No test is treated as an infinite proof.

## Originality
**PASS under inspected-source comparison.** The October 2026 Diouane–Gürol–Mouhtal–Orban article derives fixed-direction, first-order PCG-versus-deflation estimates and expressly identifies varying perturbation directions as a further direction; its 2026 precursor treats finite-step energy error under cluster placement. Giraud–Gratton (2006) studies first-order perturbation of approximate eigenpairs, including pointwise eigenvalue sensitivity, not the exact Frobenius-ball condition-number tolerance. Rump (2003) studies distance to singularity and perturbation condition numbers rather than the finite conditioning cap here. Focused semantic searches of published findings identified no dominating theorem. The components of the proof use classical matrix inequalities, and the possibility of an unlocated equivalent optimization result remains a residual priority risk.

## Value
**PASS.** In recycled preconditioning, a uniform tolerance over perturbation directions is needed before spectral data from a reference system can be trusted. The exact formula is a finite, dimension-independent certificate depending only on the smallest two eigenvalues; the extremizing perturbation surprisingly commutes with the reference matrix even when arbitrary noncommuting perturbations are allowed. It strictly improves the usual norm-only Weyl condition bound and covers repeated smallest eigenvalues. This is a benchmark for full whitening, not a claim of practical low-rank efficiency or nonlinear generality.

## Limits
Only real SPD matrices, exact full spectral whitening, symmetric Frobenius perturbations, and spectral condition number are covered. The quantitative error bounds for restarted or deflated Krylov iterates are not addressed. Independent mathematical scrutiny and comprehensive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
