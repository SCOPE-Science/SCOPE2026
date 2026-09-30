# Independent Audit — 2026/09/18/all-p-logarithmic-obstruction-strong-maximal--cec7237f693b

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `2683a0fcd9cc587d497c86a6642a3d3b68f8e772`
- Disposition: **PASSED**

## Correctness

**PASS** — The all-p extension of Lerner's construction is algebraically consistent. With w=σ^{-(p-1)}, the dual weight is exactly σ. The anchored A_p estimate reduces to a two-parameter geometric series with ratio 3^(p-1)/2^(2p-1)<1 for every p>1; Lerner's function-independent comparison of arbitrary rectangular averages with anchored averages then transfers the bound to the full rectangular characteristic. The two-cell rectangle R_{1,0} gives the matching lower characteristic scale θ^{-(p-1)}. The test f=σ1_Q has unit L^p(w) norm, while on C_{r,s} the anchored rectangle gives M_s f≥|R_{r,s}|^{-1}. Summing over rs≤D, where Lerner's recurrence has S_{r,s}<2, produces θ^{-p}log(1/θ) at the pth-power level and hence θ^{-1}(log(1/θ))^{1/p}. Substituting A≈θ^{-(p-1)} gives the stated A^{1/(p-1)}(log A)^{1/p} obstruction. Reflection to R^2 and tensoring inert coordinates preserve the relevant rectangular averages, so the d≥2 extension is valid.

## Originality

**PASS** — Lerner's preprint proves the lower obstruction only for p=2 in R^2; the contemporaneous Ombrosi-Rey paper develops all-p upper bounds and still cites the lower obstruction in the p=2 form. Targeted searches found no earlier theorem using w=σ^{-(p-1)} to obtain the explicit all-p logarithmic endpoint obstruction. The record properly claims only this extension, not Lerner's mass recurrence or averaging device.

## Scientific value

**PASS** — The result closes a natural endpoint question simultaneously for every 1<p<∞ and every dimension d≥2, showing that the Buckley-type pure exponent 1/(p-1) is unattainable even though it may remain the infimum exponent. The explicit logarithmic lower factor is directly useful when judging sharpness of current all-p upper bounds.

## Sources

- Failure of the linear A_2 bound for the strong maximal operator (Andrei K. Lerner): https://arxiv.org/abs/2609.14008 — Provides the p=2,R^2 mass recurrence, logarithmic lower obstruction, and arbitrary-to-anchored rectangle comparison.
- Improved weighted bounds for the strong maximal function (Sheldy Ombrosi; Guillermo Rey): https://arxiv.org/abs/2609.17246 — Contemporaneous all-p upper-bound work; no matching all-p lower logarithmic construction was located.
- Reverse Hölder Property for strong weights and general measures (Teresa Luque; Carlos Pérez; Ezequiel Rela): https://arxiv.org/abs/1512.01112 — Earlier strong-weight background and sharp-dependence context.

## Limitations

- The theorem rules out the endpoint pure-power estimate but does not show the infimum admissible power exponent is strictly larger than 1/(p-1).
- No optimality claim is made for the logarithmic exponent 1/p.
- The proof is specific to the strong maximal operator over axis-parallel rectangles.

## Independent checks

```json
{
  "method": "symbolic reconstruction of the A_p and test-function estimates",
  "geometric_series_ratio_verified_for_all_p_gt_1": true,
  "input_norm_exactly_one": true,
  "characteristic_scale": "theta^{-(p-1)}",
  "output_scale": "theta^{-1}(log(1/theta))^{1/p}",
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; Oxford Download was not needed in this record.
