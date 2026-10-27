# Scientific assessment: directional regularity of matrix-reset Brownian equilibria

## Correctness — PASS

The specified stable deterministic matrix and positive-definite Brownian covariance make the backward Poisson series square-summable. Its characteristic function is the product of Gaussian-exponential mixtures. For every projection, positivity of the coefficient indexed by \(j\) is equivalent to the nonvanishing of \((A^\mathsf T)^jv\). Infinitely many coefficients give arbitrarily fast Fourier decay; finitely many yield an exact finite convolution of Laplace kernels. The differential fundamental-solution identity proves the nonzero derivative jump, not merely an asymptotic estimate. For the full joint law, invertibility supplies uniform decay, whereas a singular reset creates a singular measure in the stationary Fokker–Planck source, ruling out a globally \(C^2\) density. The independent exact-rational checker verified 104 finite-dimensional structural identities. The proof does not mistake finite checks for an infinite assertion.

## Originality — PASS, with residual risk

The motivating affine-reset paper arXiv:2610.01363 provides general moment formulas but not the exact nilpotent-direction regularity classification. arXiv:2205.03363 explicitly covers the scalar infinite Laplace convolution and product, and arXiv:2412.15626 establishes stationary smoothness for multivariate scalar-factor resetting. Accordingly, neither the product formula nor the invertible scalar special case is claimed separately as new. The claimed structural advance is classification by the *first annihilating matrix power*, including the exact derivative jump and singular-versus-invertible joint regularity. Searches for matrix resets, singular rank, nilpotent directions, and equivalent stationary-density smoothing statements found no directly covering result. Broader general Fokker–Planck or smoothing literature may imply some conclusions implicitly; a domain-expert literature assessment has not been performed.

## Mathematical value — PASS

Deterministic linear resets are a natural anisotropic form of the affine-reset mechanism: some state coordinates can be destroyed at a reset while others survive. The theorem locates a sharp transition in stationary regularity controlled solely by the algebraic nilpotence depth of a **direction**, not by scalar contraction magnitude. It supplies every finite smoothness order, an exact quantitative cusp strength, and a universal global obstruction when the reset loses rank. These facts distinguish rank-deficient reset dynamics even under full-rank diffusion, and give observable signatures in one-dimensional projections.

## Limitations and closest work

Conditions: \(\rho(A)<1\), positive-definite constant covariance, linear deterministic reset, independent Poisson clock, finite dimension. The earlier scalar product and scalar-smoothness results are not new. No extension to nonlinear/random resets is claimed. The exact theorem is established by a supplied proof and self-review; no independent validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
