# Self-review

## Correctness
PASS. Two-step Lanczos produces a degree-one polynomial in \(A\) applied to \(b\). The projected \(2\times2\) matrix is symmetric, so the polynomial interpolates the exponential at its two Ritz values. A mean-value representation of the secant slope proves positivity throughout the full spectral interval whenever
\[
t(L-\mu)\le1.
\]
For the converse, a three-point diagonal spectrum with its middle point approaching the lower endpoint makes the extrapolated value at the upper endpoint tend to
\[
e^{-t\mu}\bigl[1-t(L-\mu)\bigr],
\]
which is negative beyond the threshold. Continuity under a positive third starting component gives an actual negative component. Two dimensions are exact, so dimension three is minimal.

The packaged checker independently reconstructs a concrete three-dimensional witness using high-precision arithmetic.

## Originality
PASS. The foundational 1990 full report gives the projected exponential formula, the Lanczos specialization, and minimal-polynomial exactness. Saad's 1992 analysis supplies the Ritz-interpolation viewpoint. Later Lanczos exponential papers recovered in the search focus on error bounds, conditioning, and preconditioning.

Targeted searches using Lanczos, Arnoldi, matrix exponential, positivity preserving, nonnegative, Ritz interpolation, spectral width, two-step, and dimension-three terminology found no implication-equivalent statement of
\[
t(L-\mu)\le1
\]
as a sharp universal componentwise-positivity frontier.

Residual risk remains that older polynomial-approximation literature contains the same secant-extrapolation observation under different terminology. The complete 1992 SIAM paper was not directly retrievable through one inspected viewer, so noncoverage was not inferred from inaccessible material.

## Value
PASS. Krylov exponential propagation was developed for parabolic evolution problems, where componentwise nonnegativity has direct physical meaning. The theorem gives a complete safety law for the first nontrivial Lanczos truncation, separates cone preservation from ordinary norm convergence, and shows that three spectral modes suffice to create a sign defect immediately beyond the sharp width-time boundary.

## Closest literature and limitations
The closest sources are Gallopoulos–Saad's full 1990 parabolic Krylov report, Saad's 1992 interpolation/error analysis, and later Lanczos exponential error-bound papers. The result is restricted to exact-arithmetic two-step Lanczos on diagonal SPD matrices and nonnegative starts; higher dimensions of the Krylov space and non-diagonal matrices are not classified.

Self-review: passed. Independent audit: not yet performed.
