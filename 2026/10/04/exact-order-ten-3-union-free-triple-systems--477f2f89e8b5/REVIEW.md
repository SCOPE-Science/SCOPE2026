# Same-model scientific review

## Claim
For 3-union-free 3-uniform hypergraphs on 10 vertices, \(U_3(10,3)=8\), and every 8-edge extremal family is, up to relabeling, the pair-star consisting of all triples containing one fixed pair.

## Correctness
PASS. The lower construction is the 8-edge pair-star. The upper bound is a symmetry-complete exhaustive search: after fixing the first edge, the stabilizer has exactly three second-edge orbits, and the search retains all unions of up to three selected edges. A rejected edge already creates a repeated union, a hereditary obstruction. All three target-9 searches are empty. A second exhaustive pass finds no target-8 family without a common pair; any target-8 family with a common pair is necessarily the full pair-star. The packaged verifier was replayed and returned `ALL CHECKS PASSED`.

## Originality
PASS. The closest indexed exact small-order result found covers \(4\le n\le9\), while the 2026 full-text source treats \(U_3(n,3)\) as part of an exceptional asymptotic family and the foundational paper gives asymptotic/structural results rather than the exact order-ten classification. Searches also used the historical uniquely-decipherable-code and cover-free terminology. Residual risk remains for unindexed older coding-theory tables and for a closely related published artifact whose full text was not available through the retrieval path used here.

## Value
PASS. Order ten is the immediate next finite case after the located through-nine classification, and the ambient \(U_3(n,3)\) family remains mathematically active and exceptional in recent asymptotic work. The result gives both the exact extremal number and the unique extremal type up to relabeling.

## Closest literature and limitations
The principal modern comparison is arXiv:2605.11949, first public 2026-05-12; the foundational comparison is arXiv:1103.1691. The finite claim is restricted to ten vertices and does not settle larger orders or asymptotics. Search evidence supports originality but is not treated as a proof of bibliographic uniqueness.

Same-model review: passed. Independent audit: not yet performed.
