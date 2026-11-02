# Review of maximal nilpotency index in triangular matrix products

## Correctness — PASS
The necessary and sufficient diagonal-zero and superdiagonal-nonzero tests are algebraic identities. A compatible diagonal tuple is encoded by a word in \(L,R,Z\); the allowed words are exactly \(L^kR^{n-k}\) and \(L^kZR^{n-k-1}\). Their weighted sum is \((q-1)^{n-1}((n+1)q-1)\). Independent uniform superdiagonal coordinates supply the factor \(((q-1)/q)^{n-1}\). These steps prove the universal claim without extrapolating from finite tests. The standalone verifier exhaustively checks six prime-field instances, including all ordered pairs for \(n=4,q=2\), and tests the weighted words separately. The remaining scientific limitation is that the full Jordan distribution is not derived.

## Originality — PASS (qualified)
The closest primary result, Sarma–Subedi (2026), arXiv:2610.07892v1, Theorem 2.24, yields only the total nilpotent-product probability, whereas the claim counts the proper maximal-index stratum within that event. Fuchs–Kirillov (2022), Van Peski (2024), and Yip (2018) concern uniformly chosen strictly upper triangular matrices, which have a different measure from a product of uniform triangular factors. These distinctions were checked at the level of sampling law and exact implication, not paper titles. Targeted published-record searches found no explicit equivalent formula. An older factorization-weighted Jordan-type formula could imply the result; absolute priority is not certified.

## Value — PASS
The nilpotency index is the size of the largest Jordan block and measures the nilpotent product's extremal behavior, rather than just its membership in the nilpotent cone. A single exact theorem covers **all** prime powers and dimensions, includes the number of maximal-index factorizations, and reveals an exponentially strong departure from the uniform nilpotent ensemble. This is a natural quantitative refinement of the newly studied nilpotent-product probability, not a small unmotivated parameter slice. It does not attempt the harder full-index distribution.

Self-review: passed. Independent audit: not yet performed.
