# Same-model review

## Correctness
PASS. The Hermite formula is rewritten exactly in nonnegative data increments. For \(0\le\sigma\le1/2\), the increment coefficients satisfy \(q_0\ge1\), \(0\le q_1\le1\), and \(q_2\le0\). Linear optimization over the admissible increment simplex therefore selects a single vertex for each side of the range. The remaining two cubic shape factors have exact maximum \(4/27\), proving both sharp constants and their equality cases. The strictly increasing witness follows by direct substitution. The packaged exact-rational polynomial replay returns `VERIFY_OK`.

## Originality
PASS with explicit residual risk. Qualitative Catmull–Rom overshoot and classical monotonicity-preserving cubic Hermite methods are prior-covered and are excluded from the novelty claim. published-finding corpus and literature searches under Catmull–Rom, cardinal-cubic, overshoot, range-preservation, four-point monotonicity, tension, and exact-\(2/27\) aliases found no implication-equivalent sharp theorem. The inspected sources do not state the exact two-sided bounded-data range, the extremizers, the linear tension law, or the strictly increasing positive witness. Full-text institutional retrieval of the most relevant Catmull–Rom papers was unavailable, and older graphics literature could encode the same constant under another norm or basis formulation; these remain explicit risks.

## Value
PASS. Overshoot is a documented global-stability problem for Catmull–Rom interpolation, and monotonicity filters are widely used to avoid it. The result converts that qualitative concern into a complete, dimensionless worst-case law for the minimal four-sample local operator: exactly \(2/27\) for standard Catmull–Rom, with sharp data and locations and a full tension tradeoff. The strictly increasing positive witness shows that the defect is not caused only by tied or zero samples, making the bound useful as a regression and safeguard benchmark.

Same-model review: passed. Independent audit: not yet performed.
