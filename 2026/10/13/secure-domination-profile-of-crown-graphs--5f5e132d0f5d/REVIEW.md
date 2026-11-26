# Independent mathematical audit

## correctness

PASS

Reconstructed the defender exchange proof for ordinary domination (closed neighborhoods). Both predicates guarantee initial domination: each vertex outside a shore's selection has an adjacent selected opposite-side vertex, including in the unique-defender case. In line 42 the p=0 swap argument uses initial domination, which forces the entire B shore selected if p=0; thus b_i really is still selected after exchanging b_j for a_i with j≠i. With p≥1 the exchange leaves at least two selected vertices in A, so in either case the B side is safe. On A, after losing a defender, q≥3 leaves at least two selected in B; for q=2, a 00 attack needs a retained defender from a 11 pair, while a 01 attack can retain its own matched B vertex. When q=1 and an A vertex is outside, it must be the sole such vertex and adjacent to the defender, exactly (a,c,d)=(1,0,1); q=0 requires no outside A vertex. Reflecting gives the other predicate. Multinomial counting is valid by labeled pair assignments. At n≥5 and size at most four neither shore can be full, and one selected vertex on a shore would force n−1 on the other; therefore both occupancies must be two and d≥1. The two stated profiles then give the stated minimum-set count. A fresh adjacency-mask replay at /workspace/branches/audit_crown.py checked the predicate and every bivariate coefficient for each n=3,…,8; minimum size and count outputs were (3,14), (4,62), (4,70), (4,135), (4,231), (4,364). Exhaustion on this range checks the implementation and small boundaries, not the infinite proof.

## originality

PASS

The retained claim is the ordinary secure-domination all-set classification and side-size enumerator for crowns. The scalar minimum is explicitly excluded from priority, and the small-set counts are consequences and comparison context. The closest inspectable same-graph results use different predicates; material similarities are credited below.

## value

PASS

The result isolates how the deleted matching affects defender exchanges and counts all sets by side sizes, including which rare marginal occupancies can be secure. This is a natural refinement of the scalar invariant on a standard graph family and gives more information than the stricter same-graph analogues or the single shared coefficient with complete prisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
