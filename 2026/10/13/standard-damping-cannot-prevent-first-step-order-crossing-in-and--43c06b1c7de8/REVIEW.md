# Self-review

## Correctness — PASS
The least-squares problem is a strictly convex scalar quadratic. Its unique minimizer is reconstructed explicitly, and substitution yields the exact factorization
\[
x_{2,i}^{(\omega)}-x_i^\star=(1-\omega a_i)e_i\left(1-\frac{a_i}\tau\right).
\]
Because \(\tau\) is a strict weighted mean of the active gaps whenever more than one gap occurs, the coordinatewise sign split follows analytically. The exact-rational replay checks the explicit witness and a family of rational instances; those computations are corroborative and are not used as an infinite proof.

## Originality — PASS
The closest full-text source is Potra--Engler, arXiv:1102.0796, which gives a broad characterization of Anderson acceleration on linear problems and its relation to GMRES. The inspected text treats Krylov spaces, residual minimization, stagnation, and convergence, but contains no positivity, coordinatewise order, diagonal sign-splitting, or damping-invariance statement. Walker--Ni provides the standard residual least-squares formulation and primary MSC 65H10. The Anderson--Jacobi application is a plausible same-object source, but only metadata and abstract were readable here; those materials discuss convergence speed and scaling rather than order preservation.

Published-database searches using diagonal contraction, two-rate crossing, weighted-gap coefficient, Anderson--Jacobi positivity, and GMRES sign-change formulations returned norm-transient and scalar-acceleration results, not an implication-equivalent theorem. Current and immediately prior own ledgers were checked for claim/ID overlap and contain no Anderson-acceleration result.

Residual risk remains that older DIIS, Pulay mixing, or vector-extrapolation literature may contain the same sign law under different language, and the inaccessible body of the Anderson--Jacobi paper could contain a related observation.

## Value — PASS
The theorem separates two stabilization issues that are often conflated: reducing the final fixed-point correction by a scalar mixing parameter does not repair a coordinatewise crossing that has already occurred in the Anderson least-squares prediction. This is established exactly on a natural positive-contraction model, in every dimension, with dimension two minimal and with a positive two-dimensional witness that loses positivity for the entire standard mixing interval. The result gives a concrete mathematical reason to use coefficient constraints or explicit safeguards when positivity or order intervals are invariants of the base fixed-point method.

## Closest literature and limitations
The main scientific comparison is Potra--Engler's general linear Anderson/GMRES characterization. It supplies algorithmic structure but not the new sign classification. Walker--Ni supplies the canonical Anderson formulation. The Jacobi-acceleration paper is close in application but was only partly accessible. The claim is limited to the first depth-one step for diagonal affine contractions in exact arithmetic and does not cover nonlinear maps, later steps, finite precision, or coefficient-constrained/safeguarded variants.

Self-review: passed. Independent audit: not yet performed.
