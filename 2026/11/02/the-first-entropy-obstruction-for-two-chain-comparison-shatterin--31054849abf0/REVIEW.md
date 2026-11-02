# Scientific review: first entropy obstruction for two-chain comparisons

## Correctness
PASS. The gap-vector encoding is bijective. The VC formula follows from the antichain criterion for the ideals of the rectangle. The root-branch counts follow from the explicit binomial sum, and their maximum smaller side is exactly fifteen for the exceptional three-by-four profile, excluding any depth-five shattered tree. Four full labeled decision-tree certificates give the matching lower bounds and the smaller-profile saturation; threshold monotonicity and extension embeddings fill the remaining profiles. Independent gap-vector verification reproduces all finite numbers. The limited claims are not extrapolated to arbitrary parameters.

## Originality
PASS under accessible evidence, with historical-priority risk. Searches of published mathematical records, available preceding claims, and general query-learning/linear-extension literature did not identify a theorem giving these exact first entropy obstructions. A previously available result on VC dimension of linear extensions addresses static shattering. A separate preceding result gives the complete two-row ideal Littlestone recurrence, and hence covers the two-element-chain case; that covered result is expressly excluded from the present new claim. Neither implies the three-by-four threshold. The inspected Chase–Freitag query-learning full text develops general bounds, not this exact value; the Eiben et al. full text concerns counting extensions. The significant residual risk is an older equivalent result for the three-row grid expressed using merging-comparison games or rectangular-order-ideal adversary ranks.

## Mathematical value
PASS. The natural information bound \(\lfloor\log_2|\mathcal C|\rfloor\) is a compelling benchmark for adaptive shattering. The theorem proves the first sharp counterexample, with uniqueness at its minimum total size, within the natural two-chain merge family; the root-balance obstruction explains its failure rather than a bare enumeration. It precisely distinguishes count-based capacity from permissible comparison-query geometry.

## Scope and limitations
Results concern exactly two disjoint chain orders and their cross-comparison concepts. No general Littlestone formula for all chain lengths, historical uniqueness beyond the searched literature, or external certification is asserted.

Self-review: passed. Independent audit: not yet performed.
