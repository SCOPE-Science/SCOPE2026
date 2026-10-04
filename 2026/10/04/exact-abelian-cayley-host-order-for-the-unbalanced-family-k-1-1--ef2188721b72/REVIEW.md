# Same-model review

## Correctness
PASS. Normalize one singleton to \(0\), write \(A\) for the labels of the \(n\)-part and \(z\) for the other singleton. The exact induced-difference criterion forces \(A-A\), \(-A\), and \(z-A\) to be pairwise disjoint. Their sizes are at least \(n\), \(n\), and \(n\), respectively, so every host has order at least \(3n\). The explicit \(\mathbb Z_3\times\mathbb Z_n\) complete-tripartite host gives equality. The proof does not rely on finite enumeration. The bundled checker independently exhausts smaller abelian hosts for \(2\le n\le5\) and verifies the construction through \(n=50\).

## Originality
PASS. The full text of arXiv:2609.01486 was inspected at the exact difference criterion, the complete-bipartite theorem, Remark 12, the exact-value tables, and the open-problem discussion. Remark 12 explicitly gives only an upper bound for complete multipartite graphs, says the unbalanced case is open, and highlights \(K_{1,1,5}\) with a lower floor \(10\) and construction \(15\). The new three-disjoint-difference-set lower bound is not supplied there. The 2012 complete-multipartite representation-number paper was also inspected; its invariant fixes a cyclic host and the unit connection set, so it does not imply the eta lower bound. Focused semantic searches for the exact family, the \(K_{1,1,5}\) value, difference-set aliases, and broader complete-multipartite coverage produced no covering result. Residual risk remains for older results under different terminology.

## Value
PASS. The result answers a concrete example explicitly highlighted as unresolved and closes a full natural one-parameter unbalanced family. It also exhibits a simple reusable obstruction involving several edge neighborhoods simultaneously: the published local floor is \(2n\) here, while the exact value is \(3n\). This is a structural lower-bound mechanism rather than a table recomputation or a parameter substitution.

## Closest literature and limitations
The closest source is Fokam Souop–Bitjoka, arXiv:2609.01486, which defines \(\eta\), proves the difference criterion, provides the \(3n\) complete-multipartite upper construction, and explicitly leaves the unbalanced case open. Akhtar–Evans–Pritikin (Discrete Mathematics 312 (2012), 1158–1165) solves a stricter representation-number analogue and is not implication-equivalent. The present theorem does not resolve other unbalanced part-size patterns.

Same-model review: passed. Independent audit: not yet performed.
