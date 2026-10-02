# Independent scientific audit — SCOPE-20260917-714d3bdc8013

Date (UTC): 2026-10-01

## Final claim

For the uncentered Gaussian volume product at the Euclidean ball, the full support-function Hessian diagonalizes in spherical harmonics; every constant or degree-at-least-two mode is strictly negative for every positive variance parameter, while the degree-one translation space changes sign exactly at variance 2/(n+1).

## Correctness

**PASS** — The support-coordinate first and second variations were reconstructed. The primal factor contributes the spherical-gradient term and the expected radial-density coefficient; the polar factor follows from the exact radial identity rho=1/h. Combining the factors gives the stated quadratic form. On a degree-l spherical harmonic, the Laplace eigenvalue l(l+n-2) gives the displayed spectrum. Degree at least two is strictly negative, degree one crosses precisely at variance 2/(n+1), and the constant-mode integral identity proves strict negativity. Fresh numerical checks of the constant-mode inequality across several dimensions and variance scales agreed with the analytic sign argument.

## Originality

**PASS** — The closest motivating preprint establishes criticality of the ball and detects loss of optimality using translated balls. The inspected material does not state the complete support-function Hessian or its full spherical-harmonic spectrum. Published-results search returned this record as the exact match; later SCOPE records repeat or refine the spectral result but postdate this record. No earlier exact full-spectrum statement was located.

### Equivalent formulations

No earlier equivalent statement of the entire support-function Hessian spectrum was found.

### Broader coverage

The broader source does not imply the audited all-mode spectrum without the new second-variation calculation.

### Exact database or table

This is an analytic variational theorem rather than a tabulated invariant.

### Claim versus prior implication

A single restricted perturbation cannot by itself imply the complete Hessian spectrum.

## Scientific value

**PASS** — The full Hessian identifies the exact local instability mechanism at a natural phase transition: translations are the only modes that can destabilize the ball, while all genuine higher shape modes remain second-order stable. This sharpens the motivating translated-ball calculation in a mathematically reusable way.

## Source inspections

- **Uncentered Blaschke--Santaló inequalities for the Gaussian measure** — https://arxiv.org/abs/2609.18472. Accessible record and the translated-ball/criticality material available in the source inspection Assessment: PARTIAL_COVERAGE. It supplies the degree-one translation calculation but not the full all-mode Hessian stated here.
- **Exact Hessian spectrum of the uncentered Gaussian volume product at the ball** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-gaussian-volume-product-hessian-spectrum--714d3bdc8013. Title and summary Assessment: SELF_MATCH. Exact same spectral claim.
- **Exact spherical-harmonic Hessian and instability index for the Gaussian volume product** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-gaussian-volume-product-hessian-instability-index--adb76edfac12. Title and summary Assessment: LATER_COVERAGE. It postdates the audited 2026-09-17 record and repeats/refines the same spectrum.

## Limitations and residual risks

- This is a local second-variation theorem. It does not settle the higher-dimensional global maximization gap, the nonlinear behavior at the translation threshold, or uniform neighborhood stability.
- The motivating preprint is extremely recent, so unindexed concurrent work remains possible.
- The result is local and second-order only.

## Disposition

**PASS**
