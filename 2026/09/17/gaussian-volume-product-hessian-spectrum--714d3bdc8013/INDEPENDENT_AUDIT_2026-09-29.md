# Independent audit — 2026-09-29

**Record:** `2026/09/17/gaussian-volume-product-hessian-spectrum--714d3bdc8013`  
**Audited source tree:** `6abb369a4f3fa8f7559dff3112cf27ec15826465`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The support-function variation was independently rederived. For h_t=1+tφ, strict convexity holds for sufficiently small t. Differentiating the Gaussian surface-area formula gives the primal second variation a[-∫|∇_Sφ|^2+(n-1-1/σ^2)∫φ^2]. The polar identity ρ_{K_t^∘}=1/h_t gives the polar second variation a(n+1-1/σ^2)∫φ^2, and the two first variations contribute the cross term -2a^2(∫φ)^2. This reproduces the boxed Hessian exactly. Spherical harmonics then give λ_l=Ma(2n-2/σ^2-l(l+n-2)) for l>=1; l=2 is -2Ma/σ^2 and all higher modes are even more negative, while l=1 changes sign exactly at σ^2=2/(n+1). For the constant mode, integrating d[r^n exp(-r^2/(2σ^2))]/dr gives aΩ/M=n-J/(σ^2 I)>n-1/σ^2, which makes λ_0 strictly negative. The degree-one coefficient agrees with the translated-ball instability threshold in the motivating paper.

## Originality — PASS

The September 2026 Artstein-Avidan–Fradelizi–Wyczesany paper establishes the ball's optimality in the small-variance range and loss of optimality at the threshold using translations, but the located source descriptions and targeted searches do not supply a full support-function Hessian or spherical-harmonic spectrum. The present calculation upgrades the known degree-one perturbation to the complete local spectral decomposition. The priority judgment is necessarily qualified because the motivating preprint is extremely recent.

## Scientific value — PASS

The result identifies the exact local mechanism of the phase transition: translations are the only directions whose Hessian sign can change, and they form the entire positive eigenspace above the threshold. In the unresolved global window 1/n<σ^2<2/(n+1), it rules out every second-order shape-mode instability at the ball. That is meaningful structural information even though it does not solve the global maximization problem.

## Sources used in the independent comparison

- https://arxiv.org/abs/2609.18472 — Artstein-Avidan–Fradelizi–Wyczesany, Uncentered Blaschke–Santaló inequalities for the Gaussian measure; motivating threshold and translated-ball instability.
- https://doi.org/10.1016/S1631-073X(02)02328-2 — Cordero-Erausquin, classical Santaló context cited by the record; it does not cover the Gaussian Hessian spectrum.

## Limitations and residual uncertainty

- This is a local second-variation statement and does not settle global maximization in the unresolved variance window.
- It does not determine the nonlinear behavior of the degree-one kernel at the exact threshold or prove a uniform Banach-neighborhood stability theorem.
- The motivating preprint is very recent, so concurrent spectral calculations remain a residual priority risk.

This independent audit is scoped to correctness, originality, and scientific value. Repository material was used as evidence only; no GitHub modification was made during the audit.
