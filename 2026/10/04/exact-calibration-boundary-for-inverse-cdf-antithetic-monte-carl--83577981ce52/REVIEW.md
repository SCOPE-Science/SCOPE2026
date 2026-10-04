# Review: Exact calibration boundary for inverse-CDF antithetic Monte Carlo p-values

## Correctness
**PASS.** The probability-integral transform reduces the problem to uniforms; beta-binomial mixing makes the relevant count uniform on \(\{0,\ldots,B\}\) on each half of the observed rank. Combining the halves gives the doubled central atom and the exact CDF. Algebra yields the first failing support point and maximal excess. The checker confirms these identities in exact rational arithmetic.

Risk: the tie-free reduction uses a continuous strictly increasing \(F\).

## Originality
**PASS.** The primary source gives a different antithetic permutation counterexample and proves general exchangeability-based validity, but not this inverse-CDF mass law or boundary. Later non-joint-exchangeability work gives bounds rather than this exact specialization. Targeted published-finding corpus and literature searches found no covering statement.

Risk: an equivalent identity may exist under older terminology not surfaced by the searches.

## Value
**PASS.** Antithetic sampling is a standard variance-reduction idea, and the source paper makes calibration under antithetic dependence a motivated question. The result shows exactly which low levels remain safe for the canonical coupling and where global validity first fails.

Risk: the conclusion is specific to inverse-CDF reflection and does not license arbitrary dependent resampling.

Same-model review: passed. Independent audit: not yet performed.
