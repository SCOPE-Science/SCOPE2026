# Scientific review

## Correctness — PASS

The simple-eigenvalue condition and the invertibility of the Hermitian residual operator on the orthogonal complement imply the normalizations are nonzero. Analytic perturbation of the two-by-two pencil yields the linearized equation \(\Omega^*(a-Mv+Bb)=0\), which is exactly a complex-Gaussian inverse-ratio problem. The density follows with the correct complex Jacobian and the finite identity \(\mathbb E|\det G|^2=2\). Direct polar integration proves the marginal, joint, and radial tail claims; exact orthogonality identities prove the angle and refined-quotient limits. The standalone numerical verifier cross-checks complex normalization, nonzero coupling, and asymptotic eigenvalue/vector errors. Numerical checks do not establish the theorem independently of the symbolic proof.

## Originality — PASS within the inspected-source comparison

Shao (arXiv:2604.01037v3, Example 1, Algorithm 1, Theorems 2–3, and §5.3) proves high-probability rates with inverse-square-root failure-probability scaling and quadratic Hermitian refinement, but does not give the universal two-coordinate Cauchy joint density or simultaneous exceedance probability. The earlier sketched projection analysis by Nakatsukasa and Tropp (arXiv:2111.00113v2, §§1.3, 6.3–6.6) does not supply this square-sketch perturbative distribution. Semantic mathematical-record queries for Gaussian ratios, Petrov–Galerkin eigenpair errors, exact Ritz laws, and related spectral error bounds showed no dominating published finding. Known Gaussian inverse-ratio formulae are ingredients, not asserted to be new. Unexamined specialist matrix-variate Cauchy/eigenvalue literature creates a residual historical-priority risk.

## Value — PASS

The result supplies a sharp joint reliability law for a recently proposed eigenpair-extraction method, not simply a restatement of its convergence rate. It converts a worst-case high-probability estimate into all-threshold probabilities, determines the nonindependence of value and vector errors, and calibrates angle and quadratic refinement on a pathological but structurally central Hermitian example. The claim holds for all simple Hermitian eigenpairs with any fixed admissible two-dimensional trial plane, rather than only one selected numerical matrix. These calibrations inform simultaneous error tolerance and failure-budget choices.

## Scope and remaining risks

The proof is asymptotic in the trial-subspace angle and assumes an unchanged complex-Gaussian draw, exact arithmetic, and a square two-column sketch. It is not an oversampling, general-subspace-size, or uniform finite-precision theorem. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
