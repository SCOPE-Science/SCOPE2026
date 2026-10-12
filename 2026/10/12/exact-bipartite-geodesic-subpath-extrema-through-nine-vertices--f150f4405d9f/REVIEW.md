# Review: exact small-order bipartite geodesic extrema

## Correctness — PASS

Every connected bipartite graph with \(n\in\{7,8,9\}\) arises from an \(a\times(n-a)\) binary incidence matrix for some \(1\le a\le\lfloor n/2\rfloor\). All possible masks are enumerated, not randomly sampled. The BFS path count recurrence is mathematically exact by induction on distance. A separate Floyd--Warshall distance computation with distance-layer path counting reproduces every shore maximum and every equality profile. A third independent BFS classification reproduces the \(120+240+60=420\) order-nine equality masks. The missing-edge degree profiles force the listed isomorphism types. The explicit two-star graph count is \(9+16+20+36+24=105\). Risk: the universal assertion has only finite-domain quantifiers; there is no proof for order ten and above and no independent external audit.

## Originality — PASS with residual risk

The original 2026 full text introduces the invariant and poses the complete bipartite extremal classification as Problem 15. The public diameter-two theorem proves only a bound for graphs of diameter two; it cannot control the new diameter-four equality graph. A separate published path-blow-up construction determines neither global maxima nor equality types at the three orders. Counting only matching-deletion candidates does not imply a global extremal bound. Searches of the public mathematical record for equivalent names, the exact values, profiles and stronger coverage found no complete classification. Risk: an equivalent unindexed or inaccessible enumeration may exist; absence from searchable indexes is not a novelty proof.

## Value — PASS

This is an exact global classification at the first three orders beyond the small examples discussed by the motivating article, not an arbitrary graph-family sample. In addition to exact extremal values, it identifies the first diameter-four extremizer at order nine, establishes three distinct equality types there, and demonstrates why matching-only investigations miss a genuine maximizer. The finite certificate is complete and re-runnable, although no claim is made for arbitrary graph order.

Self-review: passed. Independent audit: not yet performed.
