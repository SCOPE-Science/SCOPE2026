# Complete monophonic-position and facet polynomials of cycles with private cliques

## Finding

Fix an integer \(n\ge5\) and positive integers \(t_0,\ldots,t_{n-1}\). Construct \(H(\mathbf t)\) from a cycle with ordered core vertices \(v_0,\ldots,v_{n-1}\) by adjoining, at each \(v_i\), a private clique \(Q_i\) of \(t_i\) vertices, making every vertex of \(Q_i\) adjacent to \(v_i\), and adding no other edges. Subscripts are modulo \(n\). A subset is in *monophonic position* if no induced (chordless) path contains three of its vertices. Write \(T=\sum_i t_i\), and let \(A_i(z)=(1+z)^{t_i}-1\).

Let \(\Psi_{\mathbf t}(z)\) count every monophonic-position subset by its size, including the empty set, and let \(\Phi_{\mathbf t}(z)\) count the inclusion-maximal such subsets (the facets) by their size. Both polynomials are determined by

\[
\begin{aligned}
\Psi_{\mathbf t}(z)
={}&(1+z)^T+nz+\binom n2z^2\\
&+nz\sum_{i=0}^{n-1}A_i(z)
+z^2\sum_{i=0}^{n-1}A_i(z)
+(n-2)z\sum_{i=0}^{n-1}A_i(z)A_{i+1}(z),
\end{aligned}
\]

\[
\boxed{\displaystyle
\Phi_{\mathbf t}(z)
=z^T+\left(\binom n2-n\right)z^2
+\sum_{i=0}^{n-1}\bigl(z^{t_i+1}+z^{t_i+2}\bigr)
+(n-2)\sum_{i=0}^{n-1}z^{1+t_i+t_{i+1}}.
}
\]

In particular, there are exactly \(\binom n2+n(n-1)+1\) inclusion-maximal monophonic-position sets, **independently of all private clique sizes**. The unique maximum set is \(\bigcup_i Q_i\), of size \(T\). Every such simplicial complex has facets of size two and \(T\), hence is nonpure, with unbounded facet-size disparity. When all \(t_i=t\ge2\), the facet sizes are exactly \(2,t+1,t+2,2t+1,nt\), five distinct values.

## Assumptions and scope

All graphs are finite, undirected and simple; the \(Q_i\) are disjoint. The core is an induced cycle of length at least five; every private clique is nonempty. An induced path is a simple path with no edge joining nonconsecutive vertices on it. “Inclusion-maximal” differs from “maximum-cardinality.” Sets are counted as subsets of the fixed graph's distinguishable vertices; no division by symmetries is made. The result makes no claim for cycles of length three or four, arbitrary attachments, or geodesic general position.

## Proof

**Induced-path localization.** Every vertex in \(Q_i\) is simplicial: its neighborhood is the clique \(Q_i\cup\{v_i\}\) with that vertex removed. Consequently such a vertex can only occur as an endpoint, never as an internal vertex, of an induced path with at least three vertices. In particular any subset of \(Q=\bigcup_iQ_i\) is in monophonic position. Every induced path containing two vertices from different private cliques has those vertices as its endpoints and projects to an induced core path between their attachment indices. Two vertices from the same private clique are adjacent and have only their connecting edge as an induced path.

**The core restriction.** Every three core vertices lie on an induced path of the cycle: among the three cyclic gaps, choose one of length at least two, and traverse the complementary core arc. The endpoints of that arc are nonadjacent, so the arc is chordless. Thus a monophonic-position set contains at most two core vertices.

**Exactly one core vertex.** Suppose the core vertex \(v_k\) is selected and private vertices occupy attachment index set \(I\). If \(I\) contains two nonadjacent cycle indices, the two induced arcs between those indices jointly contain every core vertex, and their extensions to private endpoints force \(v_k\) onto an induced path. Hence \(I\) is empty, a singleton, or a pair of adjacent indices. In the adjacent-pair case, the only induced path between private vertices in those two cliques uses the core edge joining them; therefore \(v_k\) must be neither endpoint of that core edge. Conversely these conditions suffice: private vertices cannot be internal to induced paths, and the only possible violating triple consists of the selected core vertex and two private endpoints. For empty support the contribution is \(nz\). Singleton support contributes \(nz\sum_i A_i(z)\), since any core vertex may be chosen. An adjacent pair contributes \((n-2)z\sum_i A_i(z)A_{i+1}(z)\).

**Exactly two core vertices.** Choose distinct core vertices \(v_a,v_b\). If private vertices are selected from an attachment clique \(Q_i\), then \(a,b\ne i\), since a private endpoint attached at a selected core yields an induced path using it internally. Further, \(v_a,v_b\) must be the two neighbors \(v_{i-1},v_{i+1}\) of \(v_i\). Indeed, unless both are those neighbors, an induced core arc from \(v_i\) to one of the selected core vertices passes through the other; adjoining a private endpoint creates a forbidden triple. Conversely if the two selected core vertices are precisely those neighbors, no induced path from any private endpoint at \(Q_i\) contains both: an arc starting at \(v_i\) that traverses one neighbor before reaching the other is chorded by the edge from \(v_i\) to its other neighbor. More than one occupied private clique is impossible because each nonempty private clique would require its attachment core vertex to be the unique common neighbor of \(v_a,v_b\). In a cycle of length at least five, a pair of vertices at distance two has exactly one common neighbor, while other pairs have none. Consequently empty support contributes \(\binom n2z^2\), and nonempty support contributes \(z^2\sum_i A_i(z)\).

Combining the zero-core (arbitrary subsets of \(Q\)), one-core, and two-core cases proves the stated formula for \(\Psi_{\mathbf t}\). These cases are disjoint and exhaustive.

**Facet classification.** The unique maximal zero-core set is the whole private vertex set \(Q\): every proper private-only subset can add a private vertex, and \(Q\) cannot add a core vertex because it occupies two nonadjacent modules. For one core vertex, singleton support in its own private clique is maximal exactly when that entire clique is selected, yielding \(\sum_i z^{t_i+1}\); singleton support in another clique can always be enlarged into an adjacent second clique without using the selected core, so it is not maximal. Each choice of two adjacent occupied private cliques avoiding the selected core is maximal exactly when both cliques are fully occupied, yielding \((n-2)\sum_i z^{1+t_i+t_{i+1}}\). For two core vertices, a nonempty private support must be their unique common-neighbor clique and is maximal precisely when fully occupied, giving \(\sum_i z^{t_i+2}\). A pair of core vertices without private vertices is maximal precisely when the pair is not at distance two, giving \(\bigl(\binom n2-n\bigr)z^2\). These exhaust all facets and prove \(\Phi_{\mathbf t}\).

Evaluating \(\Phi_{\mathbf t}(1)\) proves the size-independent facet count. Since the core-free set has size \(T\), while every core-containing facet has size at most \(T-1\) (in fact the positivity of all other clique sizes gives a gap of at least two for \(n\ge5\)), it is the unique maximum set. The classification includes both size-two and size-\(T\) facets, proving nonpurity and unbounded disparity. When \(t_i=t\ge2\), the five indicated exponents are pairwise distinct.

## Verification

The companion standalone `verify.py` constructs each graph, independently enumerates all simple induced paths and their forbidden vertex triples, exhaustively tests all subsets, and determines inclusion-maximal subsets by one-vertex extension. It then compares the observed coefficients against the two formulas, using exact integers and binomial coefficients. Seven labeled profiles were checked: three ordinary sunlets (five, six, and seven core vertices), the five-cycle with two vertices per private clique, and three nonuniform profiles. The output in `verification_output.txt` reports `VERIFICATION_OK cases=7 subsets=78848`.

For instance, with \(n=5\) and all \(t_i=1\), the formulas yield
\[
\Psi(z)=1+10z+45z^2+30z^3+5z^4+z^5,
\qquad\Phi(z)=10z^2+20z^3+z^5.
\]
The finite checks do not establish the unrestricted identities; the proof above does.

## Relationship to prior work

Thomas, Chandran, Tuite and Di Stefano [1] introduced and studied monophonic-position sets, and their Proposition 3.7 proves the maximum-cardinality parameter for ordinary corona products. That result gives \(\operatorname{mp}(C_n\odot K_t)=nt\), but neither all-cardinality counts nor inclusion-maximal-set counts, and it does not cover unequal private clique orders. Its relevant proofs and hypotheses were checked against this statement. Iršič, Klavžar, Rus and Tuite [2] studied *geodesic* general-position polynomials, a different admissibility relation, and explicitly suggested studying counting polynomials for monophonic-position sets. Their full article does not supply the present formulas. Existing related graph-family enumerations and indexed mathematical research records did not reveal a theorem implying both formulas. This does not exclude an unindexed equivalent result.

## Limitations

The conditions \(n\ge5\) and \(t_i\ge1\) are essential to the presented classification: four-cycles have two common neighbors for an antipodal core pair, changing the facet formula. The theorem is specialized to an induced cycle core and private complete attachments, and says nothing about arbitrary corona factors or shortest-path general position. Source coverage and novelty were assessed from the cited full texts and targeted searches, not a comprehensive review of all unpublished work. Independent scientific validation has not been performed.

## References

[1] E. J. Thomas, U. Chandran S. V., J. Tuite, G. Di Stefano, *On monophonic position sets in graphs*, arXiv:2012.10330, first submitted 18 December 2020; Discrete Applied Mathematics 354 (2024), 72–82; DOI: 10.1016/j.dam.2023.02.021. https://arxiv.org/abs/2012.10330 and https://arxiv.org/pdf/2012.10330 .

[2] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110; DOI: 10.1007/s00025-024-02133-3, first arXiv submission 11 January 2024. https://link.springer.com/article/10.1007/s00025-024-02133-3 .
