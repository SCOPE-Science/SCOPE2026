# Same-model scientific review

## Correctness — PASS
The proof uses only unique nonnegative simplex barycentric coordinates. The central sparse-splitting lemma removes exactly \(r\) exhausted entries at each inductive stage, choosing a length-\(r\) window of total mass at most one and an adjacent donor with enough residual mass. For \(i=1\), the average of the first \(r+1\) masses exceeds one because \(k>1\); for \(i>1\), the prior length-\(r\) window exceeded one. The induction leaves precisely \((k-1)r+1\) entries and total mass \(k-1\). The necessity witness has total off-vertex mass \(k\varepsilon<1\), forcing all summands to include the same vertex and yielding the strict capacity bound \(kr<d\). The exact rational verifier checks 4410 decompositions; the proof covers all real barycentric vectors, not just rational tests.

## Originality — PASS, with historical risk
The closely related 2015 source arXiv:1512.03718v2 was inspected in full, including theorems on volume-deficit failure, Schneider index, and eventual Hausdorff-distance monotonicity. The later extensive arXiv:1704.05486v3 was examined for simplex and skeleton terminology and its convexification theorems; none of the inspected relevant claims imply an exact all-skeleton finite saturation threshold. Classical Shapley–Folkman–Starr results give asymptotic approximation; they do not state this equality. A separate existing simplex-centroid equal-average result is limited to one fixed point and a fixed count, not all simplex points or all skeleton orders. An equivalent sparse-transport theorem outside the searched literature remains a concrete historical risk.

## Value — PASS
The result gives the exact minimal number of equal-weight summands for **every** dimensional simplex skeleton, not merely a narrow isolated computation. Its constructive mass-splitting procedure and sharp near-vertex obstruction explain the transition geometrically. This supplies a natural finite-time benchmark for Minkowski convexification, where the literature often supplies only asymptotic convergence and quantitative nonconvexity rates.

## Scope and independence
The statement is limited to full-dimensional affine simplices and closed proper skeleta; it is not an arbitrary-convex-body theorem. Numeric checks are supplementary and no third-party validation is asserted. Potential older equivalent formulations have not been categorically excluded.

Same-model review: passed. Independent audit: not yet performed.
