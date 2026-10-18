# Bidirected two-edge spiders collapse to cross-polytope spheres

## Finding
For every integer \(n\ge1\), let \(T_n\) be the tree with central vertex \(o\), intermediate vertices \(u_1,\ldots,u_n\), leaves \(w_1,\ldots,w_n\), and undirected edges \(ou_i\) and \(u_iw_i\), for all \(1\le i\le n\). Let \(D_n\) replace each edge of \(T_n\) with its two opposite directed arcs. Write \(X(D_n)\) for the multipath simplicial complex of all arc sets forming disjoint unions of vertex-simple directed paths. Let \(B_n\subseteq X(D_n)\) be the subcomplex whose faces contain only arcs on the outer edges \(u_iw_i\).

**Theorem.** There is a sequence of elementary simplicial collapses
\[
X(D_n)\searrow B_n\cong\underbrace{S^0*\cdots*S^0}_{n\text{ factors}}=\partial\mathcal O_n,
\]
where \(\mathcal O_n\) is the \(n\)-dimensional cross-polytope. Consequently \(X(D_n)\simeq S^{n-1}\), integrally. The natural arm-permutation group \(S_n\) and simultaneous reversal \(\rho\) of every arc induce on the unique nonzero reduced integral homology the rank-one character
\[
(\sigma,\rho^\varepsilon)\longmapsto\operatorname{sgn}(\sigma)(-1)^{n\varepsilon}
\quad(\sigma\in S_n,\;\varepsilon\in\{0,1\}).
\]
Equivalently, \(\widetilde H_j(X(D_n);\mathbb Z)=\mathbb Z\) if \(j=n-1\), and is zero otherwise. The \(n=1\) case uses the usual reduced zero-dimensional homology convention.

The face enumerator, including the empty face, is
\[
\sum_{F\in X(D_n)}t^{|F|}=(1+2t)^n+2nt(1+t)(1+2t)^{n-1}
+n(n-1)t^2(1+t)^2(1+2t)^{n-2},
\]
where the final term is omitted for \(n=1\).

## Assumptions and scope
The two opposite arcs of an undirected edge are distinct vertices of the simplicial complex. A face has at most one incoming and one outgoing arc at each graph vertex and contains no directed cycle, including a two-cycle. Because the underlying graph is a tree, these requirements characterize multipaths. The statement applies to the undirected tree with **exactly two edges per arm**, then fully bidirected, not to an arbitrary orientation or a generic spider. For \(n\le2\), the underlying tree is a path; the new genuinely branching family begins at \(n=3\). The asserted symmetry is a statement about the induced **homology representation**. The collapse constructed below is not asserted to be equivariant.

## Proof
Fix \(n\ge1\). Label the four directed arcs of arm \(i\) by
\[
A_i:o\to u_i,\quad B_i:u_i\to o,\quad
C_i:u_i\to w_i,\quad D_i:w_i\to u_i.
\]
The subcomplex without any \(A_i\) or \(B_i\) is \(B_n\). For each arm, \(C_i\) and \(D_i\) may not occur together, since they form a two-cycle. Arcs from distinct outer edges are mutually compatible. Hence \(B_n\) is the join of \(n\) two-point sets, which is exactly the boundary complex of the \(n\)-cross-polytope.

We give a complete acyclic matching on the face poset of \(X(D_n)\) outside \(B_n\). Order the center-adjacent arc vertices as \(A_1,B_1,A_2,B_2,\ldots,A_n,B_n\). For each face \(F\notin B_n\), let \(P(F)\) be its first center-adjacent arc under this order. If \(P(F)=A_i\), toggle \(C_i\); if \(P(F)=B_i\), toggle \(D_i\). This defines a matched pair consisting of the face without the designated outer arc and the face with it.

The pairing is well-defined. An occurrence of \(A_i\) excludes \(B_i\) (opposite arcs) and \(D_i\) (two arrows entering \(u_i\)); adding \(C_i\) neither creates a degree conflict nor a cycle. Similarly, \(B_i\) excludes \(A_i\) and \(C_i\), and adding \(D_i\) is permitted. Other arms and other center arcs do not affect this compatibility. Toggling the designated outer arc preserves the center-arc set and hence the chosen first center arc. Thus each face outside \(B_n\) belongs to exactly one pair; every face in \(B_n\) is unmatched.

This matching is acyclic. Direct matched Hasse covers upward and all other covers downward. Along every directed cover, the number of selected center-adjacent arcs never increases: matched covers change only an outer arc, while a cover changing a center arc points downward. A hypothetical directed cycle therefore holds the entire center-arc set fixed (individual center arcs can be removed but never added), so its designated pivot outer arc is also fixed. Along such a cycle, every change to a nonpivot outer arc is a downward deletion. Hence no nonpivot outer arc can change on a directed cycle. The pivot outer arc may only be added via its upward matched cover; it cannot be deleted because that particular cover is reversed. It also cannot change on a cycle. Thus there is no directed cycle. Since \(B_n\) is a subcomplex and the acyclic matching pairs every face outside it, the relative acyclic-matching collapse lemma gives an actual sequence of elementary simplicial collapses \(X(D_n)\searrow B_n\).

For the integral symmetry character, choose the fundamental cycle of \(B_n\) to be the simplicial join
\[
z=(C_1-D_1)*\cdots*(C_n-D_n),
\]
with each difference interpreted as a reduced zero-cycle. Under an arm permutation, permuting two zero-cycle factors in a join changes the top-dimensional orientation by \((-1)^{(0+1)(0+1)}=-1\). Thus \(\sigma\in S_n\) acts by \(\operatorname{sgn}(\sigma)\). Under simultaneous reversal, every \(C_i\) and \(D_i\) is exchanged, sending each factor to its negative, so \(\rho\) acts by \((-1)^n\). Inclusion \(B_n\hookrightarrow X(D_n)\) is both an integral homology isomorphism (by collapse) and equivariant for these graph automorphisms, which proves the character formula. No homology beyond degree \(n-1\) survives.

Finally, count faces by the number of chosen center-adjacent arcs. There can be zero (outer choices \((1+2t)^n\)), exactly one (\(2n\) choices, one compatible outer arc on its arm and two single-arc possibilities on each other arm), or exactly two (one \(A_i\) and one \(B_j\) with \(i\ne j\), yielding \(n(n-1)\) possibilities, one compatible outer arc on each chosen arm). Three center arcs are impossible because the center has indegree and outdegree at most one. These three disjoint cases give the stated enumerator. \(\square\)

## Verification
The standalone `verify.py` reconstructs the entire arc-face complex and the explicit relative matching for each \(1\le n\le7\) without external libraries. It checks every face, every matched pair, the entire Hasse cover set, and directed acyclicity by a full topological sort; all faces outside the cross-polytope subcomplex are matched. In the largest case, \(n=7\), it checks 63,423 faces including the empty face, 30,618 matching pairs and 381,024 oriented covers. It independently checks face-enumerator coefficients and the signed fundamental cycle under arm transpositions, a three-cycle and simultaneous reversal. Run `python3 verify.py`; the exact recorded standard output is `verify_output.txt`. The finite tests support implementation correctness; the proof of acyclicity above establishes the theorem for all \(n\), without extrapolation from experiments.

## Relationship to prior work
Caputi, Collari and Smith (2026, arXiv:2601.05670v1) define the same multipath complex and determine the homotopy types for bidirected **paths** and homological information for bidirected polygons. This includes the nonbranching special instances of the present statement for \(n=1,2\). Their directed-graph suspension operation and path and polygon results do not state this branching spider collapse or its integral automorphism character. Caputi, Collari, Di Trani and Smith (2024; preprint arXiv:2208.04656v1) analyze multipath complexes of various digraph families, including directed trees with particular orientations; these are not the present fully bidirected spiders. A published result on the fully bidirected **double-star** gives a different, generally mixed-dimensional homotopy type: its two adjacent branching centers and pendant leaves yield graph families nonisomorphic to the length-two spiders with \(n\ge3\). The present result is an explicit relative collapse and symmetry classification of this natural intermediate tree family, not a claim to a general theorem for all bidirected trees.

## Limitations
The classification is for finite fully bidirected spiders with all arms of length exactly two, and is not a classification of all bidirected trees or all arm lengths. The matching uses a chosen order and is not itself asserted equivariant. The two nonbranching special cases are covered by earlier path results and are included only to state the uniform theorem. Exhaustive computational verification ends at seven arms; the unbounded assertion follows from the explicit combinatorial proof. An unindexed or inaccessible equivalent statement elsewhere in the literature cannot be ruled out. No independent audit has been performed.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, https://arxiv.org/abs/2208.04656; Mathematika 70 (2024), e12235.
3. *Homotopy classification of bidirected double-star multipath complexes*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-homotopy-classification-of-bidirected-double-star-multipath-comp--9525e342e100.
