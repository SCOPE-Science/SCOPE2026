# Review of finite-chain involution matchings

## Correctness
PASS. The mathematical reduction from mutual semigroup inverses to two ordered transversal tests is proved in `RESULT.md`. The certificate verifies every pair, every unused vertex, the complete rank indexing, and the finite cutoff \(1\le n\le10\). The standalone verifier also composes actual maps for \(n\le5\). Its accepted finite domain is exhaustive, not a heuristic sample. No theorem for unbounded \(n\) is asserted.

## Originality
PASS at the finite, stronger-than-permutation level, with a residual priority risk. Higgins (2018/2019) proves involution matching for orientation-preserving and reversing maps of cycles, not the order-preserving chain submonoid; Higgins (2024) explicitly notes that even an arbitrary permutation matching of the latter had only been checked through four points. Higgins (2026) proves arbitrary permutation matchings at every chain length but does not establish order-two inverse matchings. The latter implication would require additional argument and is not assumed here. Literature and database searches did not identify an earlier direct ten-point involution certificate. The residual risk is an equivalent computational certificate or general involution theorem under other terminology.

## Value
PASS. The distinction between permutation matchings and involution matchings is an explicit question in the primary semigroup literature. The finite result strengthens the newly proved all-size permutation statement by supplying honest mutual-inverse two-cycle witnesses simultaneously on all rank classes through ten points, including a 92,378-element monoid. It is a motivated finite cutoff, not an arbitrary invariant or a claimed infinite solution.

## Limitations and closest references
The proof is certificate-based, with no uniform degree-parameter construction; nothing is asserted for \(n\ge11\). The closest published sources are Higgins (2019, 2024) and his October 2026 preprint; none of the examined statements supplies this finite involution conclusion. The originality check cannot rule out unindexed prior computations.

Self-review: passed. Independent audit: not yet performed.
