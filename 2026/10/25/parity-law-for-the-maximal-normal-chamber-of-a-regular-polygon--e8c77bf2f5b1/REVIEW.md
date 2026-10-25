# Review

## Correctness

**PASS.** For each edge, the orthogonal-projection criterion is exactly \(|\langle y,t_j\rangle|\le R\sin(\pi/n)\). For odd \(n\), the strip normals give a regular \(2n\)-gon; for even \(n\), opposite edge tangents duplicate the strips and give a regular \(n\)-gon. The circumradius of each chamber is no greater than the inradius of \(P_n\) for the stated ranges \(n\ge5\) odd and \(n\ge6\) even. Perimeter-times-inradius gives the exact areas, and Taylor expansion gives the parity-dependent coefficients. Numerical spot checks are supplementary, not the proof.

## Originality

**PASS, with residual bibliographic risk.** The closest polyhedral-normal literature develops normal counting and active regions but does not state this exact maximal-chamber area. The general average-normal literature concerns an integral of the count, not the area of the simultaneous all-edge projection region. An indexed result on regular odd polygons gives a mean-normal formula; a separate Estermann-area result concerns a different region. Neither implies the present parity-resolved chamber area. The search was bounded, so novelty is not claimed as globally certified.

## Value

**PASS.** The maximal-normal locus area is a natural statistic complementary to the average normal count: it answers how much of a regular polygon realizes the largest possible face-count bound. The exact parity split in the polygonal shape and the fourth-order area term is not recoverable from the maximum count alone.

## Closest literature and limitations

- Nasonov, Panina, and Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773: definitions of face-based normals, active regions, and a bound by the number of faces; the inspected text does not give the chamber-area formula.
- Domokos and Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813: general motivation and average-normal framework; the inspected sections concern the mean statistic, not the maximal chamber.
- A search-indexed result on regular odd polygons reports an exact average-normal formula; a separate regular-polygon result concerns Estermann measure. Both are close in broad object family but state different invariants.

Self-review: passed. Independent audit: not yet performed.
