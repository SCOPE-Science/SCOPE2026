# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness — PASS

The claimed extremal value is
\[
f(n)=n-1+6\left\lfloor\frac{n-1}{4}\right\rfloor
+\binom{(n-1)\bmod4}{2}.
\]

The proof was checked against the defining characterization of \(K_{2,4}\)-freeness: no pair of vertices may have four common neighbors.

The main points are:

1. \(K_1\vee(qK_4\cup K_r)\) is \(K_{2,4}\)-free because a pair involving the universal vertex has at most three common neighbors, and a pair outside it has at most the universal vertex plus two common neighbors inside one \(K_4\).
2. A connected cograph of order at least seven with no universal vertex has a root join with one side of size at least two and the other of size at least four, immediately creating \(K_{2,4}\).
3. If \(G=K_1\vee H\), then \(K_{2,4}\)-freeness is exactly the conjunction \(\Delta(H)\le3\) and \(H\) being \(K_{2,3}\)-free. The join decomposition of any connected component of \(H\) then forces that component to have order at most four.
4. Packing components of order at most four maximizes the edge count by using as many \(K_4\)'s as possible, with one clique for the residue.
5. The only non-universal connected boundary case not covered by the order-at-least-seven argument is \(n=6\). Its root join must be \(3+3\), each side has at most one edge, and equality yields exactly \((K_2\cup K_1)\vee(K_2\cup K_1)\).
6. Strict superadditivity of the resulting bound excludes disconnected extremal graphs.

The arguments cover all residue classes and all positive orders. No computational assertion is needed for the proof.

## Originality — PASS, to the best of our knowledge

The closest source inspected is Zimmermann, *Bipartite Turán problem on cographs*, arXiv:2601.07406v2. Its relevant statements establish:

- eventual periodic linearity for every fixed \(K_{s,t}\);
- asymptotic coefficient \(s-1+(t-1)/2\), which gives \(5/2\) for \(K_{2,4}\);
- a complete all-order product structure for \(K_{2,t}\) only when \(t\in\{2,3\}\);
- the existence of exceptional small non-universal extremal graphs for some larger \(t\);
- a dynamic-programming method and precomputed data for small orders.

The associated public repository documents precomputed small-order extremal data and contains an `extremal_K24.json` export pointer. The underlying large-file contents were not inspected here. The existence of precomputed \(K_{2,4}\) data is therefore treated conservatively as prior coverage of individual small cases, not as evidence for the closed formula.

Searches covered the formulations “\(K_{2,4}\)-free cographs,” “\(K_{2,4}\) cograph Turán number,” “Zarankiewicz problem on cographs,” the induced-Turán notation \(\operatorname{ex}(n,\{K_{2,4},P_4\text{-ind}\})\), universal/complete-vertex descriptions, and equivalent exact-formula wording. No source was located stating the formula for every \(n\) or the extremal classification above, and no stronger theorem was found that immediately implies them.

No plausibly covering source was identified whose relevant statement could not be inspected. Residual risk remains from unpublished, unindexed, or differently formulated work, as with any literature search. Accordingly, originality is asserted only to the best of our knowledge.

## Value — PASS

This is the first parameter beyond \(t=2,3\) not covered by the prior all-order \(K_{2,t}\) structure theorem. It turns the known asymptotic coefficient for \((2,4)\) into an exact formula for every order and identifies all extremal isomorphism types, including the unique exceptional phenomenon at \(n=6\). The proof also isolates a simple threshold mechanism: from seven vertices onward, \(K_{2,4}\)-freeness forces every connected cograph to have a universal vertex, after which the problem reduces to packing clique components of order at most four.

## Sources inspected

- Jakob Paul Zimmermann, *Bipartite Turán problem on cographs*, arXiv:2601.07406v2. The introduction, cograph definitions, Theorems 1 and 3, the discussion immediately following Theorem 3, and the small-instance computational framework were inspected.
- The public repository accompanying Zimmermann's paper was inspected for its documented dynamic-programming scope and the presence of a \(K_{2,4}\) small-instance export.
- D. G. Corneil, H. Lerchs, and L. Stewart Burlingham, *Complement reducible graphs*, Discrete Applied Mathematics 3 (1981), 163–174, was checked as the foundational cograph reference.

The review does not constitute independent validation or peer review.
