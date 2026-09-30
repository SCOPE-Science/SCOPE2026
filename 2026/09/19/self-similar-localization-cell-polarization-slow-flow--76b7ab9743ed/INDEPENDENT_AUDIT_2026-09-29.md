# Independent Audit — 2026-09-30

**Record:** `2026/09/19/self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed`  
**Title:** A localization clock and self-similar rates for the cell-polarization slow flow  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `dbe4d57cf11a5a14ed572befb3512e96024c776c`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS**: The exact positive-part representation implies the two support inclusions and squeezes conserved mass to (t+Φ)G(σ)→1. Since the source proves α(t)↓α* and hence Φ=o(t), this gives tG(σ)→1. Regular-variation inversion and monotonicity of φ=Φ′ yield the claimed time exponents and coefficient, and homogeneous local scaling gives the support and similarity-profile formulas.
- **Originality — PASS**: The current Niethammer–Röger–Velázquez v1 supplies the representation formula, monotonicity, limiting-measure description, and static small-threshold asymptotics of G, but does not state the full-time clock tG(σ(t))→1, the resulting temporal power laws, or the dynamic local similarity profile. The nearby stationary small-mass paper treats a different obstacle problem and different scaling.
- **Scientific value — PASS**: The result converts the source’s qualitative localization into an explicit physical clock linking signal geometry to multiplier decay, support size, peak height and spatial width; the Morse case gives concrete t^{-1/4}, t^{-1/2}, and t^{1/2} laws with Hessian-dependent constants.

## Independent checks

- Re-derived the localization-clock inequality from the exact representation without using the repository verifier.
- Checked the source full text for Corollary 3.3, Corollary 3.4, and Section 4 homogeneous sublevel asymptotics.
- Checked the local scaling and layer-cake constant ∫(1−v)_+=m/(m+2)|{v<1}|.

## Findings

- The source representation formula and monotonicity of α are explicit in Section 3.1 of arXiv:2609.20609v1.
- For finite maximizers, F(s)=|{H<s}|→0, so the bounded u0 correction is negligible in the mass squeeze.
- For G(s)~Cs^q with q>1, monotone-density regular variation gives φ(t)~(1−1/q)C^{-1/q}t^{-1/q}.
- For homogeneous degree m maxima on the two-dimensional surface, q=1+2/m and the filed Morse constants follow from a quadratic change of variables.

## Sources

- https://arxiv.org/abs/2609.20609 — Current v1; representation formula, multiplier monotonicity and static localization geometry.
- https://arxiv.org/abs/2605.03553 — Related stationary small-mass obstacle problem with different spatial scaling.
- https://arxiv.org/abs/2402.03034 — Earlier interface-behavior work on the same model family, not the dynamic clock theorem.

## Limitations

- Applies to the D=∞ zero-membrane-diffusion slow-time limit, not the original parabolic problem or finite cytosolic diffusion.
- Power laws require isolated maxima with regular homogeneous asymptotics.
- No quantitative convergence rate to the local similarity profile is established.

Repository evidence was checked against current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the assigned source-tree SHA still matches the current record tree. GitHub was used only as read-only evidence; no repository writes were made.
