# Review of Three visibility polynomials of complete multipartite graphs

## Correctness
PASS. In a complete multipartite graph, the only nonadjacent pairs are same-part pairs, and every geodesic between such a pair has one internal vertex outside the part. Thus a same-part pair is \(X\)-visible exactly when the complement of \(X\) contains a vertex outside that part. Applying this to the pair types required by ordinary, outer, and dual visibility yields the three complement classifications. The invalid complement families are disjoint except for the empty complement, handled separately, so the polynomial coefficients follow exactly. Exhaustive direct geodesic checks on all complete multipartite isomorphism types through order \(9\) match every classification and coefficient.

## Originality
PASS. The 2023 defining source for outer and dual visibility contains no complete-multipartite or bipartite treatment in its searchable text. The 2024 diameter-two source covers cograph scalar behavior but not all-set enumerators. The 2025 visibility-polynomial paper gives all four polynomials for balanced complete bipartite graphs and explicitly notes that general bipartite graphs require more cases, but contains no multipartite treatment. The 2026 complete-multipartite game paper gives the ordinary scalar value and maximal ordinary structures, not the three all-cardinality polynomials. Targeted semantic searches found no equivalent arbitrary-part-size theorem.

## Value
PASS. The theorem gives the complete feasible-set structure and every cardinality count for three distinct visibility notions on a standard graph family, not merely their extremal sizes. It explains the different thresholds caused by singleton and two-vertex parts, specializes to the published balanced-bipartite formulas, and complements the separately known total visibility enumeration without duplicating it.

Self-review: passed. Independent audit: not yet performed.
