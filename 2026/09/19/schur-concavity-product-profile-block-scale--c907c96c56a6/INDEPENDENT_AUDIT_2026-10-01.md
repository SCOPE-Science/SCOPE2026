# Independent mathematical audit — SCOPE-20260919-c907c96c56a6

Final disposition: **PASS**.

## Correctness
**PASS** — At fixed pair sum, every term involving both selected coordinates increases with their product, and each exactly-one paired contribution has square \(RS+2T+2\sqrt{T(R^2+RS+T)}\), strictly increasing in \(T=xy\); this proves strict pairwise balancing and hence Schur concavity. Splitting a block strictly increases the corresponding paired terms. Cauchy-Schwarz gives \(W_d^2\le {q\choose d-1}\sum A_I^2\), and direct counting gives \(\sum A_I^2=d e_d\). Maclaurin then yields the sharp continuous envelope, while the comparison with \(e_2\) gives the stated variance stability. The integer maximizer follows by repeated splitting and balancing.

## Originality
**PASS** — The complete Abakumov-Friedland-Yomdin source was inspected. It introduces the product-profile scale, evaluates equal blocks, and proves only a coarse block-count reduction; it explicitly does not claim optimality for the scale when the number of blocks exceeds the degree. It does not contain strict Schur concavity, refinement monotonicity, the exact integer envelope, elementary-symmetric compression, or the quantitative variance rigidity estimate. published-record database search found no earlier equivalent theorem; later block-product records address different concentration constants rather than this structural optimization.

### Equivalent formulations
The equivalent block-size formulation was compared directly with the source invariant.

### Broader coverage
No inspected result dominates the exact finite envelope or stability theorem.

### Exact database or table
The claim is a continuous/discrete extremal theorem, not a database lookup; search was used only for prior coverage.

### Claim versus prior implication
The assigned result requires a new pairwise-balancing argument and an elementary-symmetric compression.

## Value
**PASS** — The theorem solves the natural extremal problem for a newly introduced structural invariant for every finite block count, gives exact integer extremizers, and quantifies near-equality. Those results immediately sharpen several source corollaries while carefully avoiding an unsupported claim about optimal concentration itself. This is a motivated complete classification of a natural invariant.

## Source inspections
- **Product-profile anti-concentration for block-structured multi-affine polynomials** (https://arxiv.org/abs/2609.19473): complete 26-page primary preprint, including the definition of the block scale, the equal-block computation, the block-count corollaries, and the source limitations on optimality Assessment: PRIMARY_SOURCE_NOT_COVERING_STRUCTURAL_OPTIMIZATION. Evidence: The source defines the invariant and gives a coarse at-most-q estimate but does not prove the assigned majorization or rigidity results.

## Residual risks
- The source preprint is very recent, so simultaneous unindexed observations remain possible.
- The theorem optimizes the structural scale only; it does not prove optimality of the actual concentration function for \(q>d\).
