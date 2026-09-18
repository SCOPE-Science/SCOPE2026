# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The review checks each structural step separately.

The upper bound is an explicit isometric embedding. A star coordinate assigned to a non-singleton part contributes exactly \(2\) within that part, \(1\) across its boundary, and \(0\) outside it. When at least two singleton parts exist, the additional half-edge star supplies their mutual distance \(1\) without exceeding any graph distance elsewhere. Taking the coordinatewise supremum therefore reproduces the complete-multipartite metric exactly.

For the lower bound, each non-singleton part contains a pair at graph distance \(2\), and such a pair must attain distance \(2\) in some coordinate. Two selected pairs from different parts cannot attain \(2\) in the same tree coordinate: their within-pair four-point sum is \(4\), while each alternative pairing has sum at most \(2\), contradicting the tree four-point condition. Hence distinct non-singleton parts require distinct coordinates.

When at least two singleton parts are present, equality with only those coordinates is impossible. In the coordinate realizing a chosen within-part distance \(2\), every singleton vertex must be at coordinate distance at most \(1\) from both endpoints; the triangle inequality forces it to be the unique midpoint. Thus all singleton vertices coincide in every forced coordinate, giving supremum distance \(0\), contrary to their graph distance \(1\). This proves the extra-coordinate necessity.

Boundary cases were checked against standard examples: complete graphs have rank one; stars have rank one; complete bipartite graphs with both sides non-singleton have rank two; and deleting a perfect matching from \(K_n\) gives rank \(n/2\), as in the source paper.

## Originality

**PASS, to the best of our knowledge.** The closest primary source is Ashworth–Clarke–Giansiracusa–Jones–Quijas-Aceves–Ren, arXiv:2609.19372. Its Proposition 3.5 gives rank two for complete bipartite graphs, and its Theorem 3.3 contains complete graphs minus a perfect matching among its rank-\(n/2\) examples. The paper also asks for characterizations of bounded phylogenetic rank. Its text was checked for complete-multipartite terminology and no theorem covering the full class was found.

Searches also used synonymous and equivalent formulations involving complete multipartite and complete tripartite graphs, matching-deleted complete graphs, isometric embeddings into products of metric trees, supremum/\(\ell_\infty\) products, and "tree rank". No stronger theorem implying the stated formula was located.

Cartwright and Chan's earlier "tree rank" for symmetric matrices was inspected as a possible collision. Their paper explicitly distinguishes that tropical-Grassmannian notion from the Pachter–Sturmfels phylogenetic notion, so it is not prior coverage of this result.

Residual risk is nonzero. The parameter traces back to Chapter 3 of Pachter and Sturmfels (2005), whose relevant section was not inspected in full here; an equivalent formula under older terminology could therefore have been missed. The graph-theoretic source paper is also very recent, leaving ordinary risk from unindexed or parallel work. These limitations prevent any claim stronger than "to the best of our knowledge."

## Value

**PASS.** The result gives an exact closed formula on an entire classical graph class rather than on isolated examples. It subsumes the complete-bipartite theorem and the perfect-matching-deletion example from the current source, extends the latter to deletion of an arbitrary matching, and supplies arbitrarily high-rank complete multipartite examples with an elementary structural explanation. It also provides a tractable family relevant to the source paper's bounded-rank classification question.

## Limitations

The theorem is restricted to complete multipartite graphs and does not characterize general graphs of phylogenetic rank at most \(k\). It is a metric-structure theorem, not an algorithmic complexity result. The publication records a same-model assessment only and does not assert independent verification, formal verification, expert review, or priority certainty.

**Same-model review: passed. Cross-model review: not yet performed.**
