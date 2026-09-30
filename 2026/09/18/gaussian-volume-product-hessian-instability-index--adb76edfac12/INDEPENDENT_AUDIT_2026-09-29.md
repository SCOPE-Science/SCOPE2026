# Independent audit — 2026-09-29

**Record:** `2026/09/18/gaussian-volume-product-hessian-instability-index--adb76edfac12`  
**Title:** Exact spherical-harmonic Hessian and instability index for the Gaussian volume product  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `e5c43003b954efcc9e646e1218f3222bfdefd0f1`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The second variation is correct. For h=1+tf, the first Gaussian-volume factor contributes a[-∫|∇f|²+(n-1-σ^{-2})∫f²], the polar/radial factor contributes a(n+1-σ^{-2})∫f², and the product rule adds the stated negative rank-one mean term. On spherical harmonics the nonconstant coefficient is 2(n-σ^{-2})-ℓ(ℓ+n-2): degree 1 is n+1-2/σ², degree 2 is -2/σ², and all higher degrees are negative. The constant coefficient is negative by the radial integration identity. Thus the threshold σ²=2/(n+1), n-dimensional translation nullspace at equality, and positive index n above it are all correct.

## Originality

**PASS** — The September 2026 Artstein-Avidan–Fradelizi–Wyczesany preprint proves ball maximality for σ²≤1/n and non-maximality above 2/(n+1); its displayed instability calculation tests translated balls and recovers the degree-1 threshold. I found no full support-function Hessian diagonalization or complete spherical-harmonic Morse index there. The record therefore supplies a genuine local variational refinement, subject to the usual near-simultaneous-work caveat.

## Scientific value

**PASS** — The full Hessian identifies exactly which modes destabilize, proves all ℓ≥2 modes remain strictly negative, and isolates the unresolved gap as a translation-mode phenomenon at quadratic order. This is materially more informative than the source's one-parameter translated-ball instability test while remaining appropriately local.

## Findings

- The full second-variation formula and spherical-harmonic diagonalization reproduce exactly.
- Only degree-1 modes change sign, at σ²=2/(n+1); degree-2 and higher modes stay negative.
- At the critical value the Hessian nullspace is exactly the n-dimensional translation space.
- The primary preprint's instability proof uses translated balls, not the complete Hessian spectrum.

## Independent checks

- Independently differentiated the Gaussian measure of support-function and polar-radial perturbations.
- Diagonalized the quadratic form on spherical harmonics.
- Checked the constant mode via radial integration by parts.
- Inspected the motivating preprint's translated-ball second-order calculation.

## Sources

- https://arxiv.org/abs/2609.18472 — Artstein-Avidan–Fradelizi–Wyczesany 2026 motivating Gaussian volume-product preprint.
- https://doi.org/10.1016/j.aim.2021.107769 — Background on Gaussian Santaló/volume-product geometry cited by the record.

## Limitations

- This is a local second-variation theorem for smooth support perturbations, not a global maximization theorem.
- Higher-order behavior at the critical translation modes is not resolved.
- The motivating preprint is recent enough that unindexed parallel calculations remain possible.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
