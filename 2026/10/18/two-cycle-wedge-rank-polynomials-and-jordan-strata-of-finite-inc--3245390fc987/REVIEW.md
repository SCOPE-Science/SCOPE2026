# Mathematical assessment: two-cycle wedge rank polynomials

## Correctness: PASS

For every prime-power \(q\) and \(n,m\ge2\), the theorem counts every edge-weight specialization exactly once. A weighted forest biadjacency matrix has rank equal to the support matching number because the minor supported on a maximum matching has a unique perfect matching and hence a single nonzero determinant term. Deleting the gluing row leaves two independent paths, each governed by the stated two-state recurrence. The dimension of the path rowspace intersected with the deleted row's two-coordinate support is exactly the rank drop upon deleting the other columns, so the polynomial \(Q_n\) counts rank-neutral row extensions. A common row is rank-neutral exactly when both its restrictions are individually rank-neutral, proving \(\mathcal W=zF_GF_H+(1-z)D_GD_H\). The single-cycle determinant has exactly two alternating monomials, giving the full-support correction. The incidence radical has square zero, so a rank-\(r\) element has Jordan type \((2^r,1^{N-2r})\). Independent brute-force ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) verify all small stated cases and total-mass tests.

## Originality: PASS within examined coverage

The 2026 published-finding corpus single-cycle rank enumerator supplies \(S_n\) and must not be counted as new; its full result and proof were checked. The published-finding corpus tree character-degree enumerator supplies the support-forest rank mechanism and is likewise prior art. The new claim is the **shared-root rowspace-intersection gluing identity** and the complete two-even-cycle wedge specialization, which involves simultaneous cancellation constraints. The 2022 Fuchs–Kirillov triangular-matrix Jordan-type counts aggregate unrestricted nilpotent triangular matrices and do not determine this restricted height-two incidence-algebra distribution. Searches for bipartite cycle wedges, cut-vertex rank-polynomial gluing, finite-field matrix zero patterns, and the same result under Jordan/incidence-algebra terminology did not identify equivalent published coverage. The argument does not establish absolute novelty; an unindexed or older rooted-rank formula is a stated residual priority risk.

## Value: PASS

This is a natural exact rank/Jordan census for the first articulation-coupled pair of cyclic support components, beyond standalone trees and cycles. It computes every rank stratum uniformly for all \(n,m,q\), distinguishes shared-vertex dependence from disjoint-cycle independence, and isolates a sharp characteristic-two full-support rank obstruction. The relation between these sparse matrices and the radicals of natural height-two incidence algebras makes the coefficients interpretable as intrinsic finite-algebra counts. The rooted gluing lemma is reusable on other cut-vertex-supported bipartite matrix families; no unstated downstream theorem is required for the complete census to be mathematically worthwhile.

## References and limits

Primary source: Fuchs and Kirillov, arXiv:2204.00066 (first posted 2022-03-31). Published mathematical records compared: *Cycle graphical groups have an explicit character-degree enumerator* and *Tree graphical groups have matching-support character polynomials* (published-finding corpus, 2026). Proof concerns finite fields, two even cycles sharing one bipartition vertex, labelled radical elements, and Jordan type only; no assertion of global historical uniqueness or classification of arbitrary incidence posets. The standalone finite checker supports but cannot certify infinite-parameter claims. Independent external review remains open.

Self-review: passed. Independent audit: not yet performed.
