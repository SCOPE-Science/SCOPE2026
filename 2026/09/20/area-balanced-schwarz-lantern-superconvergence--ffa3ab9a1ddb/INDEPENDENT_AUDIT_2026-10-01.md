# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-ffa3ab9a1ddb`

## Correctness — PASS

The theorem follows rigorously from the classical exact area formula. For fixed \(n\), the normalized area is strictly increasing in the relaxed band count, starts below one, and diverges, so the balance point is unique and solving the equation gives the displayed closed form. Independent symbolic expansion reproduces \(2/(\sqrt3 x)+11\sqrt3\,x/90+589\sqrt3\,x^3/37800\), the unique linear bias-cancelling slope, the quartic real-relaxation term \(-11x^4/180\), and, after writing \(m=m_*(n)+\delta\), the rounded leading terms \(\sqrt3\,ho\delta x^3/6+ho^2\delta^2x^4/8-19\sqrt3\,ho\delta x^5/360\). Substituting \(x=\pi/n\) gives exactly the stated \(n^{-3}\) integer law and face-count rate.

### Correctness sources

- assigned RESULT.md
- Kobayashi–Tsuchiya arXiv:1610.06054 primary text
- independent symbolic series expansion

### Correctness risks

- The optimized quantity is only total lateral area.
- The exact balance point is a real relaxation; integer meshes incur rounding.

## Originality — PASS

The primary Schwarz-lantern source was inspected at the exact-area discussion: it gives the classical triangle-area formula and the standard convergence behavior, but it does not state the finite-resolution balancing root, the unique linear cancellation slope, or the integer \(n^{-3}\) rounding law. Fresh Resultary searches found no broader/current theorem covering those optimization statements. Because the derivation is elementary, older folklore under different terminology remains a real residual risk, but unsuccessful search is not being treated as proof of priority.

### equivalent_formulations

Searches:
- Resultary: Schwarz lantern exact area threshold balanced aspect ratio cubic rounding
- primary arXiv full-text search around the Schwarz–Peano example
- web searches for the explicit slope \(2H/(\sqrt3\pi R)\) and balance equation

Evidence:
- The exact Resultary match is the audited theorem.
- Kobayashi–Tsuchiya give the classical exact lantern area and convergence discussion, not the balance/rounding optimization.

Reasoning:
Equivalent formulations as zero of the finite-\(n\) area error, cancellation of the linear-regime \(n^{-2}\) coefficient, and nearest-integer superconvergence were checked.

### broader_coverage

Searches:
- Kobayashi–Tsuchiya 2017
- Brewin 2015 curvature-corrected estimates
- modern corrected curvature-measure literature

Evidence:
- Brewin changes the geometric estimator rather than tuning the ordinary lantern's band count; the primary interpolation paper treats convergence conditions.

Reasoning:
Those broader approximation results do not imply the specific optimal ordinary-lantern aspect ratio and rounding expansion.

### exact_database_or_table

Searches:
- current Resultary geometry records
- classical Schwarz-lantern references

Evidence:
- No exact table/database of balance thresholds or optimal integer band counts was located.

Reasoning:
The result is an asymptotic optimization of a classical formula, not a known finite table.

### claim_vs_prior_implication

Searches:
- direct implication comparison with the classical \(m/n^2	o0\) criterion

Evidence:
- The classical criterion permits every linear \(m\sim cn\); it does not single out the unique \(c\) cancelling the first nonzero bias nor quantify integer rounding about the exact root.

Reasoning:
The audited boundary requires additional asymptotic optimization beyond convergence itself.

### source_inspections

- **Approximating surface areas by interpolations on triangulations** — https://arxiv.org/abs/1610.06054. Trigger: Primary modern source recording the exact Schwarz-lantern area formula and convergence discussion. Material read: Full accessible arXiv HTML around the introduction's Schwarz–Peano construction and exact triangle-area formula. Method: Primary formula and statement comparison. Assessment: NOT COVERING the balancing and superconvergence claims. Evidence: The source derives the ordinary lantern area and discusses geometric convergence conditions, without an exact zero-error band count or optimized integer rounding law.
- **Assigned balance theorem** — assigned RESULT.md. Trigger: Exact optimization and asymptotics. Material read: Complete file. Method: Independent calculus and symbolic-series reconstruction. Assessment: All coefficients reproduce. Evidence: The finite-\(n\) root, \(c_*\), quartic cancellation, and cubic rounded error follow from the exact normalized area formula.

### checked_sources

- https://arxiv.org/abs/1610.06054 full text
- https://arxiv.org/abs/1512.03461
- current Resultary Schwarz-lantern search
- assigned RESULT.md

### residual_risks

- The calculation is elementary enough that an equivalent optimization may exist in older finite-element or approximation folklore under different terminology.

## Scientific value — PASS

The Schwarz lantern is a canonical warning example in surface approximation, and the theorem identifies an exact under/over-estimation boundary inside the ordinary construction rather than modifying the estimator. The unique bias-cancelling aspect ratio and the \(O(F^{-3/2})\) nearest-integer area law give a natural, practically interpretable superconvergent regime. This is a motivated exact boundary, not an arbitrary parameter slice.

### Value sources

- classical Schwarz-lantern area problem
- Kobayashi–Tsuchiya exact formula
- audited balancing asymptotics

### Value risks

- No claim is made about normals, curvature, Hausdorff error, or optimal triangulations beyond the standard lantern family.

## Limitations

- Only the standard staggered Schwarz lantern on a circular cylinder is treated.
- Only total lateral area is optimized.
- The exact balance count is real-valued; integer meshes use nearest-integer rounding.
- Originality is best-of-knowledge with explicit folklore risk.

## Disposition

**PASSED**
