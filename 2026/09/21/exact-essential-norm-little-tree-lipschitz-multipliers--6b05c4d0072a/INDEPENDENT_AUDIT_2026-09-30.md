# Independent audit — 2026-09-30

**Record:** `2026/09/21/exact-essential-norm-little-tree-lipschitz-multipliers--6b05c4d0072a`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `b15e6c90caa6030f4e3c0b6767f557b6ca20e487`  
**Disposition:** **PASSED**

## Correctness

**PASS.** Weighted difference coordinates identify the max-norm little space with c0(T) and the sum-norm little space with C⊕_1 c0(T*). Re-expanding Δ(ψf) gives exactly the stated row coefficients. Their dual norms are |ψ(v)|+c_v|Δψ(v)|(1+H_c(v)) and max{c_v|Δψ(v)|, |ψ(v)|+c_v|Δψ(v)|H_c(v)}. For a bounded operator into either c0-type target, finite-radius output projections are finite rank by local finiteness and compact images have uniformly vanishing coordinate tails; this proves the tail-row essential-norm identity used for both upper and lower bounds. The c_v=1 and c_v=|v| specializations and the harmonic-number factor were checked algebraically.

## Originality

**PASS (literature-bounded).** Allen–Colonna–Easley explicitly describe their weighted-tree results as essential-norm estimates, not exact formulas. The 2026 infinite-graph extension likewise frames its essential-norm results as estimates. No checked source states the arbitrary positive-edge-weight formulas or the harmonic-number exact formula. Rachel Locke's 2016 dissertation and the cited unpublished 2023 Colonna–Locke graph preprint were not available in fully inspectable text in this run, so priority is bounded by that concrete literature gap.

## Scientific value

**PASS.** The result upgrades a lower/upper essential-norm bracket to an exact vertexwise limsup and retains correlation between the symbol and derivative tails; the arbitrary-edge-weight form is also reusable beyond the classical |v|-weight.

## Literature and evidence

- Allen, Colonna and Easley, Multiplication operators on the weighted Lipschitz space of a tree: https://arxiv.org/abs/2207.12616
- Issa-Barbará and Martínez-Avendaño, Multiplication Operators on the Lipschitz Space of an Infinite Graph: https://arxiv.org/abs/2602.13534
- Allen, Colonna and Easley, Multiplication Operators on the Lipschitz Space of a Tree: https://doi.org/10.1007/s00020-010-1824-5

## Limitations

- The theorem concerns little spaces, not the corresponding big ℓ∞-type spaces.
- The Locke dissertation and unpublished Colonna–Locke preprint remain incompletely inspected priority risks.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
