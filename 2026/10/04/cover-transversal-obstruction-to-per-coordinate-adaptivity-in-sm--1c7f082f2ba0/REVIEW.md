# Review

## Correctness

PASS. The defining recurrences were reconstructed separately for SM3-I and SM3-II. From zero state, an off-target support raises every target-cover accumulator to \(M^2\) exactly when that support intersects every cover set containing the target. A following target-only gradient \(\delta\) therefore produces the exact statistic \(M^2+\delta^2\). If one target-cover set is missed, its accumulator stays zero, proving the support-size lower bound. The matrix and tensor constructions attain the lower bound with two off-target coordinates.

Risk: the theorem concerns the original additive algorithms and not EMA-modified implementations.

## Originality

PASS. The defining paper proves that SM3 upper-bounds each coordinate's AdaGrad statistic, acknowledges potentially worse worst-case convergence, and motivates covers through qualitative activation-pattern compatibility. The inspected full text does not define a cover transversal, identify the exact two-spike obstruction for standard covers, or derive the exact arbitrary attenuation ratio. The reference implementation separately warns that a column accumulator can overestimate sparse-gradient statistics, but it does not imply the minimal-support theorem.

Focused published-record searches for SM3 cover transversals, row-column cross-contamination, two-spike suppression, and adversarial accumulator attenuation returned no covering statement.

Residual risk: the transversal observation may have appeared informally in optimizer discussions without being indexed under SM3 terminology.

## Value

PASS. Cover choice is the central memory-versus-adaptivity design decision in SM3. The result supplies a precise cover-quality invariant: a small transversal number means a small number of unrelated activations can suppress a coordinate's adaptive step. The fact that the standard codimension-one tensor cover has value \(2\) independently of tensor rank is a meaningful structural boundary, while singleton protection makes the corresponding memory tradeoff explicit.

Same-model review: passed. Independent audit: not yet performed.
