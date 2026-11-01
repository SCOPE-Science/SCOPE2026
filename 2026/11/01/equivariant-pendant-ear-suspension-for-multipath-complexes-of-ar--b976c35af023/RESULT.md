# Equivariant pendant-ear suspension for multipath complexes of arbitrary digraphs

## Finding
Let \(D=(V,A)\) be a finite loopless digraph, with at most one arc of each ordered pair. Let \(m\ge1\), and choose roots \(r_1,\ldots,r_m\in V\), allowing repetitions. Form \(E_m(D;\mathbf r)\) by adjoining pairwise distinct vertices \(v_i,w_i\) and the four arcs
\[
 p_i:r_i\to v_i,\qquad q_i:v_i\to r_i,\qquad
 a_i:v_i\to w_i,\qquad b_i:w_i\to v_i
 \quad(1\le i\le m),
\]
with no other arcs incident to the new vertices. Write \(X(D)\) for the simplicial multipath complex, whose vertex set is \(A\) and whose simplices are arc sets inducing disjoint unions of directed vertex-simple paths and isolated vertices.

**Theorem.** The inclusion of the explicit subcomplex
\[
 Y=X(D)*\bigast_{i=1}^{m}\{a_i,b_i\}
 \ \longhookrightarrow\ X(E_m(D;\mathbf r))
\]
is a **strong deformation retract** on geometric realizations. Here \(\{a_i,b_i\}\) denotes a discrete two-vertex complex, not its edge. In addition, \(X(E_m(D;\mathbf r))\) simplicially collapses onto \(Y\) through elementary collapse pairs. Consequently, with the augmented convention when \(D\) has no arcs,
\[
 \boxed{\quad |X(E_m(D;\mathbf r))|\simeq\Sigma^m|X(D)|,\qquad
 \widetilde H_{j+m}(X(E_m(D;\mathbf r));\mathbb Z)
 \cong\widetilde H_j(X(D);\mathbb Z).\quad}
\]
The displayed suspension of an empty realization means the join with \(m\) discrete two-point complexes; for the empty-arc base the resulting realization is \(S^{m-1}\).

The retraction is natural under automorphisms of \(D\) that permute the ordered attachment data. It also respects global arrow reversal whenever the base digraph is reverse-closed (and otherwise provides the corresponding map to its opposite digraph). A permutation \(\pi\in S_m\) of identically rooted ears acts on the suspension-orientation line by \(\operatorname{sgn}(\pi)\); reversing every arc acts on that line by \((-1)^m\), in addition to its action on the base homology.

**Canonical symmetric family.** Let \(T_m\) be the tree formed by subdividing every edge of the \(m\)-leaf star exactly once. For \(m\ge2\), bidirect every edge to obtain \(\overleftrightarrow{T_m}\). Then
\[
 \boxed{\quad X(\overleftrightarrow{T_m})\simeq S^{m-1},\qquad
 \widetilde H_{m-1}(X(\overleftrightarrow{T_m});\mathbb Z)
 \cong \operatorname{sgn}_{S_m}\otimes\varepsilon^{\otimes m}.\quad}
\]
Here \(S_m\) permutes the arms and \(\varepsilon\) is the sign line of the independent global arrow-reversal involution. All other reduced integral homology groups vanish. These are statements about the indicated \(S_m\times C_2\) action, not an assertion about larger automorphism groups in degenerate cases.

## Assumptions and scope
An arc subset belongs to \(X(D)\) exactly when every vertex has indegree and outdegree at most one *within that subset*, and the subset has no directed cycle, including two-cycles. The original digraph \(D\) may itself contain arbitrarily many directed cycles or opposite-arc pairs. The roots may coincide. The new vertices have no other incident arcs. The theorem applies to every finite such \(D\) and every \(m\ge1\); no assumptions about connectedness, source/sink status or orientation are needed.

The symbol \(*\) denotes simplicial join. The complex \(\{a_i,b_i\}\) has faces \(\varnothing,\{a_i\},\{b_i\}\). The empty-arc base has augmented simplicial complex \(\{\varnothing\}\), whose reduced homology is by convention \(\widetilde H_{-1}\cong\mathbb Z\). This handles the one-vertex example without misleadingly calling the ordinary topological suspension of the empty set a nonempty sphere.

## Proof
**1. Define a simplicial retraction.** Keep every original arc of \(D\) fixed and keep \(a_i,b_i\) fixed. On the two new arcs incident to the root set
\[
 \rho(p_i)=a_i,\qquad \rho(q_i)=b_i.
\]
For a face \(\sigma\) of \(X(E_m(D;\mathbf r))\), let \(\rho(\sigma)\) be its image under this vertex map. We prove the stronger statement that
\[
 \sigma\cup\rho(\sigma)\in X(E_m(D;\mathbf r))
 \quad\text{for every face }\sigma.
\]
If \(p_i\in\sigma\), then \(v_i\) already has one incoming arc and hence \(b_i\notin\sigma\). Also \(q_i\notin\sigma\), since \(p_i,q_i\) form a directed two-cycle. The only outgoing possibilities from \(v_i\) are \(q_i,a_i\), so adjoining \(a_i:v_i\to w_i\) cannot exceed any in/out-degree bound. It cannot create a directed cycle because \(w_i\) has no other incident selected arc. Similarly, if \(q_i\in\sigma\), then \(v_i\) already has one outgoing arc and \(p_i,a_i\notin\sigma\). Adjoining \(b_i:w_i\to v_i\) extends a path at a new leaf and cannot create a cycle. Additions for different indices are compatible because the fresh vertices \(v_i,w_i\) are distinct and **none of the added arcs touches an old root**. Hence all replacements may be adjoined simultaneously, even when several roots coincide. This establishes the displayed face property.

It follows at once that \(\rho\) is simplicial. The image is exactly \(Y\): after deleting all \(p_i,q_i\), the original arcs and the \(m\) independent opposite-arc pairs on \(v_i,w_i\) are disjoint, and each pair can contribute at most one arc to a multipath. Moreover \(\rho|_Y=\mathrm{id}_Y\).

**2. Homotopy, collapse, and equivariance.** The simplicial maps \(\mathrm{id}_{X(E_m)}\) and \(\iota\rho\) are contiguous, because their images of every face have a simplex as their union by Step 1. Straight-line interpolation in the realization of that simplex gives a homotopy between the identity and \(\iota\rho\). Since \(\rho\) fixes \(Y\), this is a strong deformation retraction fixing \(Y\) pointwise.

There is also a genuine elementary simplicial collapse, not just a homotopy equivalence. For each \(i\), the link of vertex \(p_i\) is a cone with apex \(a_i\): any face containing \(p_i\) can also contain \(a_i\). Pair each simplex containing \(p_i\) but not \(a_i\) with the simplex obtained by adding \(a_i\), deleting pairs from largest dimension downward. This removes all simplices containing \(p_i\). Then the link of \(q_i\) is a cone with apex \(b_i\); remove those simplices by analogous elementary collapse pairs. Iterate over all ears, giving \(Y\). Subsequent deletions cannot invalidate the cone condition on remaining ear vertices, because they merely remove incompatible faces.

If an automorphism of \(D\) maps the root multiset to itself and permutes its copies, extend it by the same permutation of ears. The map \(\rho\) commutes with this action, as does the straight-line deformation. If the base admits global arrow reversal as a simplicial involution, extend reversal over each new bidirected ear; it exchanges \(p_i\leftrightarrow q_i\) and \(a_i\leftrightarrow b_i\). Again \(\rho\) commutes with the involution. Thus these statements are equivariant, including for symmetries that interchange ears.

**3. Suspensions and integral groups.** The realization of the join of \(X(D)\) with \(m\) copies of \(S^0\) is the \(m\)-fold suspension of the base realization (with the augmented empty-base convention). The integral reduced join-chain isomorphism shifts degree by \(m\), with no torsion assumptions. This proves the claimed isomorphism for all integers \(j\) in the appropriate augmented range and preserves any existing torsion subgroup of the base.

The top reduced chain of \(\bigast_i\{a_i,b_i\}\cong S^{m-1}\) has canonical orientation cycle
\[
 z_m=([a_1]-[b_1])*\cdots*([a_m]-[b_m]).
\]
Permuting factors by \(\pi\) introduces the Koszul join sign \(\operatorname{sgn}(\pi)\), since each factor has shifted degree one. Global reversal switches \([a_i]-[b_i]\) to its negative in each factor, contributing \((-1)^m\). This proves the stated symmetry character and its tensor-product action with any base homology.

**4. Subdivided stars.** Take \(D\) to be a single isolated root vertex and attach \(m\) bidirected two-edge ears at it. The underlying undirected graph is exactly \(T_m\). Its original arc complex is \(\{\varnothing\}\), so the deformation retract is \(\bigast_{i=1}^m S^0=S^{m-1}\) as a simplicial sphere. The preceding chain cycle computes the full action of permutations of arms and global arrow reversal. This proves the canonical family for every \(m\ge2\). \(\square\)

## Verification
The standalone `verify.py` uses only the Python 3 standard library. It independently enumerates valid multipath faces by checking selected in/out-degrees and directed cycles; constructs the retraction and exact target join; and tests simpliciality, the stronger contiguity condition, and equality of the retraction image with the predicted target. The tested bases include an isolated vertex, a single directed arc, a directed two-cycle, a directed triangle, a bidirected length-two path, and a fully bidirected triangle. Attachment roots are both distinct and repeated.

For the subdivided-star family with \(1\le m\le4\), an independent reduced mod-two chain-boundary computation gives precisely one homology generator in degree \(m-1\). The same checker enumerates all \(2m!\) combinations of arm permutations and global reversal for \(1\le m\le4\), checks equivariance of the retract on **every** multipath simplex, and verifies the claimed sign character on the explicit sphere cycle. Its successful final marker is `BIDIRECTED_EAR_EQUIVARIANT_SUSPENSION_CHECKS_OK`. These finite calculations are corroboration; the universal integral and equivariant theorem is established by Steps 1–4, not finite extrapolation.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (arXiv:2208.04656v1, publicly posted August 9, 2022) define multipath complexes and analyze decompositions and several graph families. Their Proposition 5.4 suspends the multipath complex after attaching two common directed sinks to a graph with a specified existing sink; it does not construct the four-arc bidirected ear at an arbitrary root or the simplicial retraction above. Their dynamical-module join theorem requires a particular decomposition and does not by itself give this local cyclic ear cancellation.

Caputi, Collari and Smith (arXiv:2601.05670v1, January 9, 2026), Proposition 2.3 and its extension, describe a different T-operation. The appended local arcs and the source/sink hypothesis in that construction differ from the fully bidirected two-edge ear here. In particular, the present operation needs no root source/sink assumption and yields an explicit strong deformation retract with a functorial symmetry character, neither asserted there.

Caputi, Collari and Di Trani (2022/2023) give a related path-poset suspension construction by attaching a directed source or sink at an existing univalent vertex; their hypotheses and attachment differ from a fully bidirected two-edge ear at an arbitrary root, and the earlier construction does not imply the natural retraction claimed here.

The published study *Homotopy classification of bidirected double-star multipath complexes* (public mathematical finding, October 2026) classifies bidirected trees with two adjacent branching centres. That family is not the fully subdivided star (with its degree-two intermediate vertices), and its argument does not state the universal arbitrary-base pendant-ear retraction. The present statement is compared against that stronger nearby family result, rather than treating a title mismatch as proof of originality.

## Limitations
This theorem concerns exactly the local four-arc ear specified above, with its two new vertices of total undirected degrees two and one. It does not assert the same cancellation for longer bidirected ears, missing reverse arcs, or ears whose new vertices have further neighbors. The homology isomorphism transfers the base's torsion but does not compute the base homology from scratch. The indicated group action is on the explicit ear-permutation and arrow-reversal symmetries, and does not claim the full graph automorphism group for every base. The originality comparison is evidence-based rather than a proof of global absence in inaccessible or unindexed literature; independent scientific validation has not been performed.

## References
1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (2022-08-09), https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (2026-01-09), https://arxiv.org/abs/2601.05670.
3. *Homotopy classification of bidirected double-star multipath complexes* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-homotopy-classification-of-bidirected-double-star-multipath-comp--9525e342e100.
4. L. Caputi, C. Collari, and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, *Journal of Algebraic Combinatorics* 57 (2023), published online November 10, 2022, https://doi.org/10.1007/s10801-022-01180-9.
5. A. Björner, *Topological methods*, in *Handbook of Combinatorics* (1995), for simplicial contiguity and elementary collapses.
