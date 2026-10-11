# Same-model review

## Correctness
**PASS.** The proof fixes the exact definition and parameter range, reduces the convex optimization to the 36 hexagon-vertex pairs, and then uses explicit isometries plus \(y\mapsto-y\) invariance to obtain two exhaustive pair classes. The two representative evaluations are elementary and valid on the entire interval \(0\le m\le1/2\). The exact verifier independently checks the orbit partition and rational test values, including \(41/32\) at \(m=3/8\).

## Originality
**PASS.** The defining source arXiv:2110.15741 was inspected for the four-term definition, symmetry, bounds, and worked examples. It does not state this Day–James profile. Searches for aliases, the exact quadratic, same-space computations, and broader four-term formulas returned only different invariants or different spaces. Closest literature is recorded in `AUDIT.json` with the implication comparison and residual risk.

## Value
**PASS.** This is a natural exact invariant on a canonical Day–James plane, not an arbitrary slice. It gives the full parameter dependence and shows that the global parameter maximum occurs away from \(\lambda=1/2\), a structural feature not visible from the balanced value alone.

## Limitations
The theorem is specific to the real hexagonal Day–James norm. It does not claim a formula for other Day–James spaces or complex scalars. An obscure unindexed duplicate calculation cannot be excluded absolutely.

Same-model review: passed. Independent audit: not yet performed.
