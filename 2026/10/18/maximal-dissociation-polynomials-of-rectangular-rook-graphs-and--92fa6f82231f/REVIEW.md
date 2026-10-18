# Review of the maximal-dissociation enumerator

## Correctness — PASS

The labelled bijection \(R_{m,n}=L(K_{m,n})\) converts selected rook vertices inducing maximum degree at most one into vertex-disjoint bipartite components \(K_2\) and \(K_{1,2}\). This follows from the selected-line-graph degree formula \(d_F(i)+d_F(j)-2\le1\) and exhausts all component types. Inclusion-maximality is proved equivalent to either (a) star-only occupation of every row or column, or (b) at least one isolated edge together with occupation of all rows and columns. Both necessity and sufficiency are reconstructed by checking permitted one-vertex extensions, not inferred from finite data. Disjoint labelled-exponential counting then proves the exact generating function. The \(n\ge2m\) support and coefficient statements follow by an exact column-capacity argument and counting the forced row-covering star families. An independent brute-force graph predicate matches every coefficient on 21 small boards (1,501,518 subsets); it supports but does not replace the proof.

## Originality — PASS (subject to specified priority risks)

Orlovich et al. (2011) provide the general line-graph path/edge interpretation and maximum-cardinality and minimum-maximal dissociation optimization; **the correspondence itself is acknowledged as established**. Their inspected pertinent Claim 1 and Theorem 7 do not determine the entire inclusion-maximal polynomial of \(L(K_{m,n})\) nor its odd-cardinality gaps. The 2026 work of Wang, Xu and Zhang concerns extremal numbers of maximal dissociation sets in trees, not this dense line-graph family. Zhou et al. (2024) count *all* dissociation sets in grid graphs \(P_m\square P_n\). The published rook general-position enumerator allows star forests of unrestricted degree and does not impose inclusion-maximality. Targeted mathematical-record queries for maximal dissociation, 2-component independent sets, rook graphs, line graphs and equivalent star-packing formulations identified no covering statement. Residual risk: an older result may count the identical objects under alternate terminology or in a general maximal-subgraph framework; no claim of a definitive priority certificate is made.

## Value — PASS

The result determines a *complete natural inclusion-maximal-set cardinality invariant* across the entire two-parameter family of rook graphs. Maximality is not simply a coefficient of the all-set dissociation polynomial: it demands a global occupation classification. Its sharp imbalance theorem supplies an infinite family with prohibited odd cardinalities between attained even sizes, giving both the lower and upper maximal-dissociation numbers and exact multiplicities. This is motivated enumerative and structural information beyond a mere small numerical value or a known general upper bound.

## Verification status and limitations

The proof is self-contained and the checker executable with Python's standard library. This review is a self-review, not independent certification. Older equivalence literature and incomplete access to some historical full texts leave publication-priority uncertainty. The theorem is limited to rectangular rook graphs, with the parity-support refinement applying to \(n\ge2m\).

Self-review: passed. Independent audit: not yet performed.
