# Self-review

**Correctness: PASS.** The exact counting identity is derived by two-endpoint inclusion–exclusion. The analytic all-alphabet proof shows strict ULC for all integers \(n\ge m^2\) without extrapolating from experiments. For the six-face boundary, the only uncovered trial sizes \(4\le n\le24\) are exhausted by 84 exact-integer determinant checks against independently generated endpoint-state counts. Direct negative determinants at two and three rolls establish necessity. See `RESULT.md` and executable `check.py`.

**Originality: PASS on inspected evidence.** Badiella, del Castillo and Puig (2023, DOI 10.1016/j.spl.2023.109900) prove preservation of ultra-log-concavity by individual discrete order statistics when the parent is ULC. A discrete-uniform parent with at least three faces is not ULC, and the dependent difference of its extremes is not an order statistic; the present result cannot be deduced from their theorem. Public research on expected ranges, geometric sample ranges and order-statistic correlations does not cover this uniform-parent range-shape theorem. Searches for the algebraic counting form, the six-face threshold and the general sample-range ULC alias did not identify an equivalent. Access to the complete sequential original PDF was unavailable; some unindexed previous formulation remains possible. The originality comparisons and source-inspection limitations are detailed in `AUDIT.json`.

**Value: PASS.** The finite discrete-uniform parent is itself not ultra-log-concave, yet the nonlinear range statistic gains strict ultra-log-concavity at a provable finite sample size for every alphabet; its two-draw range remains non-ULC when there are at least four faces. The six-faced die admits a much smaller *exact* cutoff. This provides a structurally motivated boundary rather than an arbitrary finite numerical coincidence.

**Limitations.** The sufficient \(n\ge m^2\) bound is not proposed as optimal; only the six-face cutoff is sharp. Results do not cover other parent laws. Finite computation certifies only its stated finite index set; all larger cases are analytical.

Self-review: passed. Independent audit: not yet performed.
